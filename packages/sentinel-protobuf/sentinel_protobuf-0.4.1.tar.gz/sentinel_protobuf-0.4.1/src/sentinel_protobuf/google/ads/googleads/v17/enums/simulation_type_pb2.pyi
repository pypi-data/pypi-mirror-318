from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar
DESCRIPTOR: _descriptor.FileDescriptor

class SimulationTypeEnum(_message.Message):
    __slots__ = ()

    class SimulationType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        UNSPECIFIED: _ClassVar[SimulationTypeEnum.SimulationType]
        UNKNOWN: _ClassVar[SimulationTypeEnum.SimulationType]
        CPC_BID: _ClassVar[SimulationTypeEnum.SimulationType]
        CPV_BID: _ClassVar[SimulationTypeEnum.SimulationType]
        TARGET_CPA: _ClassVar[SimulationTypeEnum.SimulationType]
        BID_MODIFIER: _ClassVar[SimulationTypeEnum.SimulationType]
        TARGET_ROAS: _ClassVar[SimulationTypeEnum.SimulationType]
        PERCENT_CPC_BID: _ClassVar[SimulationTypeEnum.SimulationType]
        TARGET_IMPRESSION_SHARE: _ClassVar[SimulationTypeEnum.SimulationType]
        BUDGET: _ClassVar[SimulationTypeEnum.SimulationType]
    UNSPECIFIED: SimulationTypeEnum.SimulationType
    UNKNOWN: SimulationTypeEnum.SimulationType
    CPC_BID: SimulationTypeEnum.SimulationType
    CPV_BID: SimulationTypeEnum.SimulationType
    TARGET_CPA: SimulationTypeEnum.SimulationType
    BID_MODIFIER: SimulationTypeEnum.SimulationType
    TARGET_ROAS: SimulationTypeEnum.SimulationType
    PERCENT_CPC_BID: SimulationTypeEnum.SimulationType
    TARGET_IMPRESSION_SHARE: SimulationTypeEnum.SimulationType
    BUDGET: SimulationTypeEnum.SimulationType

    def __init__(self) -> None:
        ...