from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar
DESCRIPTOR: _descriptor.FileDescriptor

class ExperimentMetricDirectionEnum(_message.Message):
    __slots__ = ()

    class ExperimentMetricDirection(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        UNSPECIFIED: _ClassVar[ExperimentMetricDirectionEnum.ExperimentMetricDirection]
        UNKNOWN: _ClassVar[ExperimentMetricDirectionEnum.ExperimentMetricDirection]
        NO_CHANGE: _ClassVar[ExperimentMetricDirectionEnum.ExperimentMetricDirection]
        INCREASE: _ClassVar[ExperimentMetricDirectionEnum.ExperimentMetricDirection]
        DECREASE: _ClassVar[ExperimentMetricDirectionEnum.ExperimentMetricDirection]
        NO_CHANGE_OR_INCREASE: _ClassVar[ExperimentMetricDirectionEnum.ExperimentMetricDirection]
        NO_CHANGE_OR_DECREASE: _ClassVar[ExperimentMetricDirectionEnum.ExperimentMetricDirection]
    UNSPECIFIED: ExperimentMetricDirectionEnum.ExperimentMetricDirection
    UNKNOWN: ExperimentMetricDirectionEnum.ExperimentMetricDirection
    NO_CHANGE: ExperimentMetricDirectionEnum.ExperimentMetricDirection
    INCREASE: ExperimentMetricDirectionEnum.ExperimentMetricDirection
    DECREASE: ExperimentMetricDirectionEnum.ExperimentMetricDirection
    NO_CHANGE_OR_INCREASE: ExperimentMetricDirectionEnum.ExperimentMetricDirection
    NO_CHANGE_OR_DECREASE: ExperimentMetricDirectionEnum.ExperimentMetricDirection

    def __init__(self) -> None:
        ...