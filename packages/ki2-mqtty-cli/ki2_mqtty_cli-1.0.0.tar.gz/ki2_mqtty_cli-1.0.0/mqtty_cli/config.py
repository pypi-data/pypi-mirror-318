from __future__ import annotations
from typing import TYPE_CHECKING, cast
from typing_extensions import Optional, Annotated, Literal, TypeAlias
from pathlib import Path

import tomli
from pydantic import BaseModel, AfterValidator

if TYPE_CHECKING:
    pass


ParityFullType: TypeAlias = Literal["None", "Even", "Odd", "Mark", "Space"]
ParityLimitedType: TypeAlias = Literal["N", "E", "O", "M", "S"]
ParityType: TypeAlias = ParityFullType | ParityLimitedType


def convert_parity(value: ParityType) -> ParityLimitedType:
    if len(value) > 0:
        value = cast(ParityLimitedType, value[0])
    return cast(ParityLimitedType, value)


class MqttAuthConfig(BaseModel):
    username: str
    password: str


class MqttConfig(BaseModel):
    host: str = "localhost"
    port: int = 1883
    auth: Optional[MqttAuthConfig] = None


def one_char_string(value: str) -> str:
    if len(value) != 1:
        raise ValueError("Must be a single character")
    return value


class DeviceConfig(BaseModel):
    topic: str
    port: str
    baudrate: int = 9600
    bytesize: int = 8
    parity: ParityType = "None"
    stopbits: float = 1
    timeout: Optional[int] = None
    xonxoff: bool = False
    rtscts: bool = False
    write_timeout: Optional[float] = None
    dsrdtr: bool = False
    inter_byte_timeout: Optional[float] = None
    exclusive: Optional[bool] = None
    endline_char: Annotated[str, AfterValidator(one_char_string)] = "\n"
    mqtt_start: Annotated[str, AfterValidator(one_char_string)] = "@"
    mqtt_separator: Annotated[str, AfterValidator(one_char_string)] = ":"


class TomlConfig(BaseModel):
    mqtt: MqttConfig = MqttConfig()
    devices: list[DeviceConfig] = []


def load_config(path: str | Path) -> TomlConfig:
    with open(path, "rb") as f:
        data = tomli.load(f)
    return TomlConfig(**data)
