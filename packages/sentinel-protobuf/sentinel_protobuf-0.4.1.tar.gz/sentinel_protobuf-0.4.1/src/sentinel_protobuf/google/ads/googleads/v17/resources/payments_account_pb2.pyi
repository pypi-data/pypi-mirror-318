from google.api import field_behavior_pb2 as _field_behavior_pb2
from google.api import resource_pb2 as _resource_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional

DESCRIPTOR: _descriptor.FileDescriptor

class PaymentsAccount(_message.Message):
    __slots__ = ("resource_name", "payments_account_id", "name", "currency_code", "payments_profile_id", "secondary_payments_profile_id", "paying_manager_customer")
    RESOURCE_NAME_FIELD_NUMBER: _ClassVar[int]
    PAYMENTS_ACCOUNT_ID_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    CURRENCY_CODE_FIELD_NUMBER: _ClassVar[int]
    PAYMENTS_PROFILE_ID_FIELD_NUMBER: _ClassVar[int]
    SECONDARY_PAYMENTS_PROFILE_ID_FIELD_NUMBER: _ClassVar[int]
    PAYING_MANAGER_CUSTOMER_FIELD_NUMBER: _ClassVar[int]
    resource_name: str
    payments_account_id: str
    name: str
    currency_code: str
    payments_profile_id: str
    secondary_payments_profile_id: str
    paying_manager_customer: str
    def __init__(self, resource_name: _Optional[str] = ..., payments_account_id: _Optional[str] = ..., name: _Optional[str] = ..., currency_code: _Optional[str] = ..., payments_profile_id: _Optional[str] = ..., secondary_payments_profile_id: _Optional[str] = ..., paying_manager_customer: _Optional[str] = ...) -> None: ...
