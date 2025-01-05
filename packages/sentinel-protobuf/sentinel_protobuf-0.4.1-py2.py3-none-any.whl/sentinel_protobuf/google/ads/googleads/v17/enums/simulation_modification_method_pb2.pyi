from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar
DESCRIPTOR: _descriptor.FileDescriptor

class SimulationModificationMethodEnum(_message.Message):
    __slots__ = ()

    class SimulationModificationMethod(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        UNSPECIFIED: _ClassVar[SimulationModificationMethodEnum.SimulationModificationMethod]
        UNKNOWN: _ClassVar[SimulationModificationMethodEnum.SimulationModificationMethod]
        UNIFORM: _ClassVar[SimulationModificationMethodEnum.SimulationModificationMethod]
        DEFAULT: _ClassVar[SimulationModificationMethodEnum.SimulationModificationMethod]
        SCALING: _ClassVar[SimulationModificationMethodEnum.SimulationModificationMethod]
    UNSPECIFIED: SimulationModificationMethodEnum.SimulationModificationMethod
    UNKNOWN: SimulationModificationMethodEnum.SimulationModificationMethod
    UNIFORM: SimulationModificationMethodEnum.SimulationModificationMethod
    DEFAULT: SimulationModificationMethodEnum.SimulationModificationMethod
    SCALING: SimulationModificationMethodEnum.SimulationModificationMethod

    def __init__(self) -> None:
        ...