from __future__ import annotations
from typing import TYPE_CHECKING
from typing_extensions import Any
import asyncio
import sys
import os
from pathlib import Path

from aiomqtt import Client as AioMqttClient

from ki2_python_utils import run_parallel
from mqtty import serial_device_factory, manager_setup, connect_aio_mqtt

from .config import load_config, convert_parity

if TYPE_CHECKING:
    pass


def get_path():
    if len(sys.argv) > 1:
        return Path(sys.argv[1])
    env_conf = os.getenv("MQTTY_CONFIG")
    if env_conf is not None:
        return Path(env_conf)
    return Path("settings.toml")


async def _main():
    path = get_path()
    print(f"Path = {path}")
    config = load_config(path)

    if len(config.devices) == 0:
        print("No devices configured")
        return

    mqtt_config: dict[str, Any] = {
        "hostname": config.mqtt.host,
        "port": config.mqtt.port,
    }

    if config.mqtt.auth is not None:
        mqtt_config["username"] = config.mqtt.auth.username
        mqtt_config["password"] = config.mqtt.auth.password

    mqtt_client = AioMqttClient(**mqtt_config)

    manager = manager_setup("async")
    for device in config.devices:
        topic = device.topic
        serial_config = device.model_dump(exclude={"topic"})
        serial_config["parity"] = convert_parity(serial_config["parity"])
        serial_device = serial_device_factory(**serial_config)
        manager.register(topic, serial_device)
        print(f"New device '{device.port}' on topic '{topic}'")

    mqtt_loop = connect_aio_mqtt(mqtt_client, manager=manager)

    await run_parallel(manager.loop, mqtt_loop)


def main():
    asyncio.run(_main())
