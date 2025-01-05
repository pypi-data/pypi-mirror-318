from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar
DESCRIPTOR: _descriptor.FileDescriptor

class ExperimentStatusEnum(_message.Message):
    __slots__ = ()

    class ExperimentStatus(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        UNSPECIFIED: _ClassVar[ExperimentStatusEnum.ExperimentStatus]
        UNKNOWN: _ClassVar[ExperimentStatusEnum.ExperimentStatus]
        ENABLED: _ClassVar[ExperimentStatusEnum.ExperimentStatus]
        REMOVED: _ClassVar[ExperimentStatusEnum.ExperimentStatus]
        HALTED: _ClassVar[ExperimentStatusEnum.ExperimentStatus]
        PROMOTED: _ClassVar[ExperimentStatusEnum.ExperimentStatus]
        SETUP: _ClassVar[ExperimentStatusEnum.ExperimentStatus]
        INITIATED: _ClassVar[ExperimentStatusEnum.ExperimentStatus]
        GRADUATED: _ClassVar[ExperimentStatusEnum.ExperimentStatus]
    UNSPECIFIED: ExperimentStatusEnum.ExperimentStatus
    UNKNOWN: ExperimentStatusEnum.ExperimentStatus
    ENABLED: ExperimentStatusEnum.ExperimentStatus
    REMOVED: ExperimentStatusEnum.ExperimentStatus
    HALTED: ExperimentStatusEnum.ExperimentStatus
    PROMOTED: ExperimentStatusEnum.ExperimentStatus
    SETUP: ExperimentStatusEnum.ExperimentStatus
    INITIATED: ExperimentStatusEnum.ExperimentStatus
    GRADUATED: ExperimentStatusEnum.ExperimentStatus

    def __init__(self) -> None:
        ...