# Copyright 2025 Carnegie Mellon University
# Licensed under a MIT (SEI)-style license, please see LICENSE.md or contact permission@sei.cmu.edu for full terms.

"""
This runner is an example!
You will likely want to make your own.
"""
import asyncio
import logging
import signal
from jtak import TakClient, ClientConf, UserConf


logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger(__name__)

def tak_shutdown(client: TakClient):
    """graceful shutdown"""
    client.close()

async def tak_runner():
    """"Create and run a TakClient"""

    conf = ClientConf(
        UserConf(
            uid="jtak-71a415c001",
            callsign="JTAK.ME",
            lat=40.44163,
            lon=-80.01095,
            hae=200.0
        )
    )

    client = await TakClient.create(conf)

    loop = asyncio.get_event_loop()
    loop.add_signal_handler(signal.SIGINT, tak_shutdown, client)

    await client.run()

def main():
    """main entrypoint"""

    try:
        print("\nStarting jtak...")
        print("Press Ctrl-C to exit...\n")
        asyncio.run(tak_runner())

    except asyncio.CancelledError:
        pass

if __name__ == "__main__":
    main()
