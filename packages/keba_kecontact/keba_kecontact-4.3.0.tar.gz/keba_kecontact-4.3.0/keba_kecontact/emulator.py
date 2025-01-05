"""Charging station emulator."""

import asyncio
import json
import logging

import asyncio_dgram

from keba_kecontact import __version__ as version
from keba_kecontact.const import UDP_PORT

_LOGGER = logging.getLogger(__name__)

REPORT_ID_1 = 1
REPORT_ID_2 = 2
REPORT_ID_3 = 3
REPORT_ID_100 = 100


class Emulator:
    """Charging station emulator for testing purposes."""

    def __init__(self, loop: asyncio.AbstractEventLoop | None = None) -> None:
        """Initialize emulator.

        Args:
            loop (asyncio.AbstractEventLoop | None, optional): asyncio event loop. Defaults to None.

        """
        self._loop = asyncio.get_event_loop() if loop is None else loop
        self._stream = None

    async def start(self) -> None:
        """Start emulator."""
        self._stream = await asyncio_dgram.bind(("0.0.0.0", UDP_PORT))
        self._loop.create_task(self._listen())

    async def _listen(self) -> None:
        data, remote_addr = await self._stream.recv()  # Listen until something received
        self._loop.create_task(self._listen())  # Listen again
        self._loop.create_task(self._internal_callback(data, remote_addr))  # Callback

    async def _internal_callback(self, raw_data: bytes, remote_addr: tuple) -> None:
        data = raw_data.decode()
        _LOGGER.info("Datagram received from %s : %s", str(remote_addr), data)

        payload = ""
        matches_ok = [
            "unlock",
            "stop",
            "setenergy",
            "output",
            "currtime",
            "curr",
            "ena",
            "failsafe",
            "x2src",
            "x2",
        ]

        try:
            if data == "i":
                payload = '"Firmware":"Emulator v ' + version + '"\n'
            elif any(x in data for x in matches_ok):
                payload = "TCH-OK :done"
            elif "start" in data:
                split = data.split(" ")
                payload = '"RFID tag": "' + split[1] + '"\n' + '"RFID class": "' + split[2]
            elif "report" in data:
                split = data.split(" ")
                i = int(split[1])
                if i == REPORT_ID_1:
                    payload = {
                        "ID": "1",
                        "Product": "KC-P30-Emulator-000",
                        "Serial": "123456789",
                        "Firmware": "Emulator v " + version,
                        "COM-module": 0,
                        "Sec": 0,
                    }
                elif i == REPORT_ID_2:
                    payload = {
                        "ID": "2",
                        "State": 2,
                        "Error1": 99,
                        "Error2": 99,
                        "Plug": 1,
                        "Enable sys": 1,
                        "Enable user": 1,
                        "Max curr": 32000,
                        "Max curr %": 1000,
                        "Curr HW": 32000,
                        "Curr user": 63000,
                        "Curr FS": 63000,
                        "Tmo FS": 0,
                        "Curr timer": 0,
                        "Tmo CT": 0,
                        "Setenergy": 0,
                        "Output": 0,
                        "Input": 0,
                        "Serial": "15017355",
                        "Sec": 4294967296,
                        "X2 phaseSwitch source": 4,
                        "X2 phaseSwitch": 0,
                    }
                elif i == REPORT_ID_3:
                    payload = {
                        "ID": "3",
                        "U1": 230,
                        "U2": 230,
                        "U3": 230,
                        "I1": 99999,
                        "I2": 99999,
                        "I3": 99999,
                        "P": 99999999,
                        "PF": 1000,
                        "E pres": 999999,
                        "E total": 9999999999,
                        "Serial": "123456789",
                        "Sec": 4294967296,
                    }

                elif i >= REPORT_ID_100:
                    payload = {
                        "ID": str(i),
                        "Session ID": 35,
                        "Curr HW ": 20000,
                        "E Start ": 29532,
                        "E Pres ": 0,
                        "started[s]": 1698,
                        "ended[s] ": 0,
                        "reason ": 0,
                        "RFID tag": "e3f76b8d00000000",
                        "RFID class": "01010400000000000000",
                        "Serial": "123456789",
                        "Sec": 1704,
                    }
                payload = json.dumps(payload)
        except KeyError as exc:
            payload = "TCH-ERR"
            _LOGGER.warning(exc)

        _LOGGER.debug("Send %s to %s", payload, remote_addr)
        await self._stream.send(payload.encode("cp437", "ignore"), remote_addr)
