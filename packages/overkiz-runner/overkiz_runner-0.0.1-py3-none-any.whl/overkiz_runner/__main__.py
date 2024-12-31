#!/usr/bin/env python3

import asyncio
import logging
import time

from pyoverkiz.client import OverkizClient
from pyoverkiz.const import SUPPORTED_SERVERS
from pyoverkiz.enums import (
    OverkizCommand,
    OverkizCommandParam,
    OverkizState,
    Server,
)
from pyoverkiz.models import Command

from overkiz_runner import printer
from overkiz_runner.configuration import conf

logger = logging.getLogger(__name__)


async def show_states():
    for creds in conf.credentials:
        server = SUPPORTED_SERVERS[Server[creds.servertype]]
        async with OverkizClient(
            creds.username, creds.password, server=server
        ) as client:
            try:
                await client.login()
            except Exception:  # pylint: disable=broad-except
                logger.exception(
                    "Something went wrong while connecting to %s (login=%r)",
                    server,
                    creds.username,
                )
                return
            printer.print_device_states(await client.get_devices())


async def listen_events(index):
    username = conf.credentials[index].username
    password = conf.credentials[index].password
    server = SUPPORTED_SERVERS[Server[conf.credentials[index].servertype]]

    async with OverkizClient(username, password, server=server) as client:
        try:
            await client.login()
        except Exception:  # pylint: disable=broad-except
            logger.exception(
                "Something went wrong while connecting to %s (login=%r)",
                server,
                username,
            )
            return
        print(
            f"Connected with {username} to {server.name!r}, listening...",
            flush=True,
        )
        while True:
            for event in await client.fetch_events():
                printer.print_event(event)
            yield


async def listen_all_events():
    listerners = [
        listen_events(index) for index in range(len(conf.credentials))
    ]
    while True:
        for listerner in listerners:
            async for _ in listerner:
                time.sleep(conf.watch.interval)


def get_dwh_values(device):
    return {
        "min-showers": device.states[
            OverkizState.CORE_MINIMAL_SHOWER_MANUAL_MODE
        ].value,
        "max-showers": device.states[
            OverkizState.CORE_MAXIMAL_SHOWER_MANUAL_MODE
        ].value,
        "is-absence-on": device.states[
            OverkizState.MODBUSLINK_DHW_ABSENCE_MODE
        ].value
        == OverkizCommandParam.ON,
    }


async def execute() -> None:
    for creds in conf.credentials:
        server = SUPPORTED_SERVERS[Server[creds.servertype]]
        async with OverkizClient(
            creds.username, creds.password, server=server
        ) as client:
            try:
                await client.login()
            except Exception:  # pylint: disable=broad-except
                logger.exception(
                    "Something went wrong while connecting to %s (login=%r)",
                    server,
                    creds.username,
                )
                return

            for device in await client.get_devices():
                if (
                    conf.appliance == "dwh"
                    and device.widget == "DomesticHotWaterProduction"
                ):
                    if conf.command == "stop":
                        await client.execute_commands(
                            device.id,
                            [
                                Command(
                                    OverkizCommand.SET_ABSENCE_MODE,
                                    [OverkizCommandParam.ON],
                                )
                            ],
                            "setting absence on",
                        )
                    elif conf.command in {"set-to-min", "set-to-max"}:
                        state = get_dwh_values(device)
                        if conf.command == "set-to-min":
                            nb_showers = state["min-showers"]
                        else:
                            nb_showers = state["max-showers"]

                        label = f"setting showers to {nb_showers}"
                        commands = [
                            Command(
                                OverkizCommand.SET_EXPECTED_NUMBER_OF_SHOWER,
                                [nb_showers],
                            )
                        ]
                        if state["is-absence-on"]:
                            wake_cmd = Command(
                                OverkizCommand.SET_ABSENCE_MODE,
                                [OverkizCommandParam.OFF],
                            )
                            commands.insert(0, wake_cmd)
                            label = "awake and " + label
                        await client.execute_commands(
                            device.id,
                            commands,
                            label,
                        )

                        await client.execute_commands(
                            device.id,
                            [
                                Command("refreshNumberControlShowerRequest"),
                                Command("refreshExpectedNumberOfShower"),
                            ],
                            f"refresh for ({label})",
                        )


async def main():
    if conf.command == "listen-events":
        await listen_all_events()
    elif conf.command == "show-states":
        await show_states()
    else:
        await execute()


if __name__ == "__main__":
    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        print("CTRL+C: EXITING")
