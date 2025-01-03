from typing import Self
import numpy as np
from pyautd3.derive.derive_builder import builder
from pyautd3.native_methods.autd3capi import NativeMethods as Base
from pyautd3.native_methods.autd3capi_driver import DevicePtr
from pyautd3.native_methods.autd3capi_driver import TransducerPtr



class Transducer():
    _ptr: TransducerPtr
    def __init__(self: Transducer, idx: int, dev_idx: int, ptr: DevicePtr) -> None: ...
    @property
    def position(self: Transducer) -> np.ndarray: ...
    @property
    def idx(self: Transducer) -> int: ...
    @property
    def dev_idx(self: Transducer) -> int: ...
