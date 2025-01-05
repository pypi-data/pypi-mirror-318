from google.ads.googleads.v17.enums import billing_setup_status_pb2 as _billing_setup_status_pb2
from google.ads.googleads.v17.enums import time_type_pb2 as _time_type_pb2
from google.api import field_behavior_pb2 as _field_behavior_pb2
from google.api import resource_pb2 as _resource_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class BillingSetup(_message.Message):
    __slots__ = ("resource_name", "id", "status", "payments_account", "payments_account_info", "start_date_time", "start_time_type", "end_date_time", "end_time_type")
    class PaymentsAccountInfo(_message.Message):
        __slots__ = ("payments_account_id", "payments_account_name", "payments_profile_id", "payments_profile_name", "secondary_payments_profile_id")
        PAYMENTS_ACCOUNT_ID_FIELD_NUMBER: _ClassVar[int]
        PAYMENTS_ACCOUNT_NAME_FIELD_NUMBER: _ClassVar[int]
        PAYMENTS_PROFILE_ID_FIELD_NUMBER: _ClassVar[int]
        PAYMENTS_PROFILE_NAME_FIELD_NUMBER: _ClassVar[int]
        SECONDARY_PAYMENTS_PROFILE_ID_FIELD_NUMBER: _ClassVar[int]
        payments_account_id: str
        payments_account_name: str
        payments_profile_id: str
        payments_profile_name: str
        secondary_payments_profile_id: str
        def __init__(self, payments_account_id: _Optional[str] = ..., payments_account_name: _Optional[str] = ..., payments_profile_id: _Optional[str] = ..., payments_profile_name: _Optional[str] = ..., secondary_payments_profile_id: _Optional[str] = ...) -> None: ...
    RESOURCE_NAME_FIELD_NUMBER: _ClassVar[int]
    ID_FIELD_NUMBER: _ClassVar[int]
    STATUS_FIELD_NUMBER: _ClassVar[int]
    PAYMENTS_ACCOUNT_FIELD_NUMBER: _ClassVar[int]
    PAYMENTS_ACCOUNT_INFO_FIELD_NUMBER: _ClassVar[int]
    START_DATE_TIME_FIELD_NUMBER: _ClassVar[int]
    START_TIME_TYPE_FIELD_NUMBER: _ClassVar[int]
    END_DATE_TIME_FIELD_NUMBER: _ClassVar[int]
    END_TIME_TYPE_FIELD_NUMBER: _ClassVar[int]
    resource_name: str
    id: int
    status: _billing_setup_status_pb2.BillingSetupStatusEnum.BillingSetupStatus
    payments_account: str
    payments_account_info: BillingSetup.PaymentsAccountInfo
    start_date_time: str
    start_time_type: _time_type_pb2.TimeTypeEnum.TimeType
    end_date_time: str
    end_time_type: _time_type_pb2.TimeTypeEnum.TimeType
    def __init__(self, resource_name: _Optional[str] = ..., id: _Optional[int] = ..., status: _Optional[_Union[_billing_setup_status_pb2.BillingSetupStatusEnum.BillingSetupStatus, str]] = ..., payments_account: _Optional[str] = ..., payments_account_info: _Optional[_Union[BillingSetup.PaymentsAccountInfo, _Mapping]] = ..., start_date_time: _Optional[str] = ..., start_time_type: _Optional[_Union[_time_type_pb2.TimeTypeEnum.TimeType, str]] = ..., end_date_time: _Optional[str] = ..., end_time_type: _Optional[_Union[_time_type_pb2.TimeTypeEnum.TimeType, str]] = ...) -> None: ...
