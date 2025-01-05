from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar
DESCRIPTOR: _descriptor.FileDescriptor

class ExperimentMetricEnum(_message.Message):
    __slots__ = ()

    class ExperimentMetric(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        UNSPECIFIED: _ClassVar[ExperimentMetricEnum.ExperimentMetric]
        UNKNOWN: _ClassVar[ExperimentMetricEnum.ExperimentMetric]
        CLICKS: _ClassVar[ExperimentMetricEnum.ExperimentMetric]
        IMPRESSIONS: _ClassVar[ExperimentMetricEnum.ExperimentMetric]
        COST: _ClassVar[ExperimentMetricEnum.ExperimentMetric]
        CONVERSIONS_PER_INTERACTION_RATE: _ClassVar[ExperimentMetricEnum.ExperimentMetric]
        COST_PER_CONVERSION: _ClassVar[ExperimentMetricEnum.ExperimentMetric]
        CONVERSIONS_VALUE_PER_COST: _ClassVar[ExperimentMetricEnum.ExperimentMetric]
        AVERAGE_CPC: _ClassVar[ExperimentMetricEnum.ExperimentMetric]
        CTR: _ClassVar[ExperimentMetricEnum.ExperimentMetric]
        INCREMENTAL_CONVERSIONS: _ClassVar[ExperimentMetricEnum.ExperimentMetric]
        COMPLETED_VIDEO_VIEWS: _ClassVar[ExperimentMetricEnum.ExperimentMetric]
        CUSTOM_ALGORITHMS: _ClassVar[ExperimentMetricEnum.ExperimentMetric]
        CONVERSIONS: _ClassVar[ExperimentMetricEnum.ExperimentMetric]
        CONVERSION_VALUE: _ClassVar[ExperimentMetricEnum.ExperimentMetric]
    UNSPECIFIED: ExperimentMetricEnum.ExperimentMetric
    UNKNOWN: ExperimentMetricEnum.ExperimentMetric
    CLICKS: ExperimentMetricEnum.ExperimentMetric
    IMPRESSIONS: ExperimentMetricEnum.ExperimentMetric
    COST: ExperimentMetricEnum.ExperimentMetric
    CONVERSIONS_PER_INTERACTION_RATE: ExperimentMetricEnum.ExperimentMetric
    COST_PER_CONVERSION: ExperimentMetricEnum.ExperimentMetric
    CONVERSIONS_VALUE_PER_COST: ExperimentMetricEnum.ExperimentMetric
    AVERAGE_CPC: ExperimentMetricEnum.ExperimentMetric
    CTR: ExperimentMetricEnum.ExperimentMetric
    INCREMENTAL_CONVERSIONS: ExperimentMetricEnum.ExperimentMetric
    COMPLETED_VIDEO_VIEWS: ExperimentMetricEnum.ExperimentMetric
    CUSTOM_ALGORITHMS: ExperimentMetricEnum.ExperimentMetric
    CONVERSIONS: ExperimentMetricEnum.ExperimentMetric
    CONVERSION_VALUE: ExperimentMetricEnum.ExperimentMetric

    def __init__(self) -> None:
        ...