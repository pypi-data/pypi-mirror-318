from google.ads.googleads.v18.common import offline_user_data_pb2 as _offline_user_data_pb2
from google.ads.googleads.v18.enums import conversion_adjustment_type_pb2 as _conversion_adjustment_type_pb2
from google.api import annotations_pb2 as _annotations_pb2
from google.api import client_pb2 as _client_pb2
from google.api import field_behavior_pb2 as _field_behavior_pb2
from google.rpc import status_pb2 as _status_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class UploadConversionAdjustmentsRequest(_message.Message):
    __slots__ = ("customer_id", "conversion_adjustments", "partial_failure", "validate_only", "job_id")
    CUSTOMER_ID_FIELD_NUMBER: _ClassVar[int]
    CONVERSION_ADJUSTMENTS_FIELD_NUMBER: _ClassVar[int]
    PARTIAL_FAILURE_FIELD_NUMBER: _ClassVar[int]
    VALIDATE_ONLY_FIELD_NUMBER: _ClassVar[int]
    JOB_ID_FIELD_NUMBER: _ClassVar[int]
    customer_id: str
    conversion_adjustments: _containers.RepeatedCompositeFieldContainer[ConversionAdjustment]
    partial_failure: bool
    validate_only: bool
    job_id: int
    def __init__(self, customer_id: _Optional[str] = ..., conversion_adjustments: _Optional[_Iterable[_Union[ConversionAdjustment, _Mapping]]] = ..., partial_failure: bool = ..., validate_only: bool = ..., job_id: _Optional[int] = ...) -> None: ...

class UploadConversionAdjustmentsResponse(_message.Message):
    __slots__ = ("partial_failure_error", "results", "job_id")
    PARTIAL_FAILURE_ERROR_FIELD_NUMBER: _ClassVar[int]
    RESULTS_FIELD_NUMBER: _ClassVar[int]
    JOB_ID_FIELD_NUMBER: _ClassVar[int]
    partial_failure_error: _status_pb2.Status
    results: _containers.RepeatedCompositeFieldContainer[ConversionAdjustmentResult]
    job_id: int
    def __init__(self, partial_failure_error: _Optional[_Union[_status_pb2.Status, _Mapping]] = ..., results: _Optional[_Iterable[_Union[ConversionAdjustmentResult, _Mapping]]] = ..., job_id: _Optional[int] = ...) -> None: ...

class ConversionAdjustment(_message.Message):
    __slots__ = ("gclid_date_time_pair", "order_id", "conversion_action", "adjustment_date_time", "adjustment_type", "restatement_value", "user_identifiers", "user_agent")
    GCLID_DATE_TIME_PAIR_FIELD_NUMBER: _ClassVar[int]
    ORDER_ID_FIELD_NUMBER: _ClassVar[int]
    CONVERSION_ACTION_FIELD_NUMBER: _ClassVar[int]
    ADJUSTMENT_DATE_TIME_FIELD_NUMBER: _ClassVar[int]
    ADJUSTMENT_TYPE_FIELD_NUMBER: _ClassVar[int]
    RESTATEMENT_VALUE_FIELD_NUMBER: _ClassVar[int]
    USER_IDENTIFIERS_FIELD_NUMBER: _ClassVar[int]
    USER_AGENT_FIELD_NUMBER: _ClassVar[int]
    gclid_date_time_pair: GclidDateTimePair
    order_id: str
    conversion_action: str
    adjustment_date_time: str
    adjustment_type: _conversion_adjustment_type_pb2.ConversionAdjustmentTypeEnum.ConversionAdjustmentType
    restatement_value: RestatementValue
    user_identifiers: _containers.RepeatedCompositeFieldContainer[_offline_user_data_pb2.UserIdentifier]
    user_agent: str
    def __init__(self, gclid_date_time_pair: _Optional[_Union[GclidDateTimePair, _Mapping]] = ..., order_id: _Optional[str] = ..., conversion_action: _Optional[str] = ..., adjustment_date_time: _Optional[str] = ..., adjustment_type: _Optional[_Union[_conversion_adjustment_type_pb2.ConversionAdjustmentTypeEnum.ConversionAdjustmentType, str]] = ..., restatement_value: _Optional[_Union[RestatementValue, _Mapping]] = ..., user_identifiers: _Optional[_Iterable[_Union[_offline_user_data_pb2.UserIdentifier, _Mapping]]] = ..., user_agent: _Optional[str] = ...) -> None: ...

class RestatementValue(_message.Message):
    __slots__ = ("adjusted_value", "currency_code")
    ADJUSTED_VALUE_FIELD_NUMBER: _ClassVar[int]
    CURRENCY_CODE_FIELD_NUMBER: _ClassVar[int]
    adjusted_value: float
    currency_code: str
    def __init__(self, adjusted_value: _Optional[float] = ..., currency_code: _Optional[str] = ...) -> None: ...

class GclidDateTimePair(_message.Message):
    __slots__ = ("gclid", "conversion_date_time")
    GCLID_FIELD_NUMBER: _ClassVar[int]
    CONVERSION_DATE_TIME_FIELD_NUMBER: _ClassVar[int]
    gclid: str
    conversion_date_time: str
    def __init__(self, gclid: _Optional[str] = ..., conversion_date_time: _Optional[str] = ...) -> None: ...

class ConversionAdjustmentResult(_message.Message):
    __slots__ = ("gclid_date_time_pair", "order_id", "conversion_action", "adjustment_date_time", "adjustment_type")
    GCLID_DATE_TIME_PAIR_FIELD_NUMBER: _ClassVar[int]
    ORDER_ID_FIELD_NUMBER: _ClassVar[int]
    CONVERSION_ACTION_FIELD_NUMBER: _ClassVar[int]
    ADJUSTMENT_DATE_TIME_FIELD_NUMBER: _ClassVar[int]
    ADJUSTMENT_TYPE_FIELD_NUMBER: _ClassVar[int]
    gclid_date_time_pair: GclidDateTimePair
    order_id: str
    conversion_action: str
    adjustment_date_time: str
    adjustment_type: _conversion_adjustment_type_pb2.ConversionAdjustmentTypeEnum.ConversionAdjustmentType
    def __init__(self, gclid_date_time_pair: _Optional[_Union[GclidDateTimePair, _Mapping]] = ..., order_id: _Optional[str] = ..., conversion_action: _Optional[str] = ..., adjustment_date_time: _Optional[str] = ..., adjustment_type: _Optional[_Union[_conversion_adjustment_type_pb2.ConversionAdjustmentTypeEnum.ConversionAdjustmentType, str]] = ...) -> None: ...
