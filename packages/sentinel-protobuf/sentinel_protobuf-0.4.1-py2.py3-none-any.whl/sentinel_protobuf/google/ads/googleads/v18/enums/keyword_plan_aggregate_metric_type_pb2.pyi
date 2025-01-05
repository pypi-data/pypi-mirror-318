from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar
DESCRIPTOR: _descriptor.FileDescriptor

class KeywordPlanAggregateMetricTypeEnum(_message.Message):
    __slots__ = ()

    class KeywordPlanAggregateMetricType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        UNSPECIFIED: _ClassVar[KeywordPlanAggregateMetricTypeEnum.KeywordPlanAggregateMetricType]
        UNKNOWN: _ClassVar[KeywordPlanAggregateMetricTypeEnum.KeywordPlanAggregateMetricType]
        DEVICE: _ClassVar[KeywordPlanAggregateMetricTypeEnum.KeywordPlanAggregateMetricType]
    UNSPECIFIED: KeywordPlanAggregateMetricTypeEnum.KeywordPlanAggregateMetricType
    UNKNOWN: KeywordPlanAggregateMetricTypeEnum.KeywordPlanAggregateMetricType
    DEVICE: KeywordPlanAggregateMetricTypeEnum.KeywordPlanAggregateMetricType

    def __init__(self) -> None:
        ...