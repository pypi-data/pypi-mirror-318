import ctypes
from typing import Self
from pyautd3.derive.derive_builder import builder
from pyautd3.native_methods.autd3capi import NativeMethods as Base



class FirmwareInfo():
    def __init__(self: FirmwareInfo, info: str) -> None: ...
    def __str__(self: FirmwareInfo, ) -> str: ...
    @staticmethod
    def latest_version() -> str: ...
    @property
    def info(self: FirmwareInfo) -> str: ...
