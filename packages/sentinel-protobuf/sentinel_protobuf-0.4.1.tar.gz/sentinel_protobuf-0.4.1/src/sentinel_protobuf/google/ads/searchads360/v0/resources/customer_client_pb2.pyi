from google.ads.searchads360.v0.enums import customer_status_pb2 as _customer_status_pb2
from google.api import field_behavior_pb2 as _field_behavior_pb2
from google.api import resource_pb2 as _resource_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class CustomerClient(_message.Message):
    __slots__ = ("resource_name", "client_customer", "hidden", "level", "time_zone", "test_account", "manager", "descriptive_name", "currency_code", "id", "applied_labels", "status")
    RESOURCE_NAME_FIELD_NUMBER: _ClassVar[int]
    CLIENT_CUSTOMER_FIELD_NUMBER: _ClassVar[int]
    HIDDEN_FIELD_NUMBER: _ClassVar[int]
    LEVEL_FIELD_NUMBER: _ClassVar[int]
    TIME_ZONE_FIELD_NUMBER: _ClassVar[int]
    TEST_ACCOUNT_FIELD_NUMBER: _ClassVar[int]
    MANAGER_FIELD_NUMBER: _ClassVar[int]
    DESCRIPTIVE_NAME_FIELD_NUMBER: _ClassVar[int]
    CURRENCY_CODE_FIELD_NUMBER: _ClassVar[int]
    ID_FIELD_NUMBER: _ClassVar[int]
    APPLIED_LABELS_FIELD_NUMBER: _ClassVar[int]
    STATUS_FIELD_NUMBER: _ClassVar[int]
    resource_name: str
    client_customer: str
    hidden: bool
    level: int
    time_zone: str
    test_account: bool
    manager: bool
    descriptive_name: str
    currency_code: str
    id: int
    applied_labels: _containers.RepeatedScalarFieldContainer[str]
    status: _customer_status_pb2.CustomerStatusEnum.CustomerStatus
    def __init__(self, resource_name: _Optional[str] = ..., client_customer: _Optional[str] = ..., hidden: bool = ..., level: _Optional[int] = ..., time_zone: _Optional[str] = ..., test_account: bool = ..., manager: bool = ..., descriptive_name: _Optional[str] = ..., currency_code: _Optional[str] = ..., id: _Optional[int] = ..., applied_labels: _Optional[_Iterable[str]] = ..., status: _Optional[_Union[_customer_status_pb2.CustomerStatusEnum.CustomerStatus, str]] = ...) -> None: ...
