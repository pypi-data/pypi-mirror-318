from google.ads.googleads.v16.resources import billing_setup_pb2 as _billing_setup_pb2
from google.api import annotations_pb2 as _annotations_pb2
from google.api import client_pb2 as _client_pb2
from google.api import field_behavior_pb2 as _field_behavior_pb2
from google.api import resource_pb2 as _resource_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class MutateBillingSetupRequest(_message.Message):
    __slots__ = ("customer_id", "operation")
    CUSTOMER_ID_FIELD_NUMBER: _ClassVar[int]
    OPERATION_FIELD_NUMBER: _ClassVar[int]
    customer_id: str
    operation: BillingSetupOperation
    def __init__(self, customer_id: _Optional[str] = ..., operation: _Optional[_Union[BillingSetupOperation, _Mapping]] = ...) -> None: ...

class BillingSetupOperation(_message.Message):
    __slots__ = ("create", "remove")
    CREATE_FIELD_NUMBER: _ClassVar[int]
    REMOVE_FIELD_NUMBER: _ClassVar[int]
    create: _billing_setup_pb2.BillingSetup
    remove: str
    def __init__(self, create: _Optional[_Union[_billing_setup_pb2.BillingSetup, _Mapping]] = ..., remove: _Optional[str] = ...) -> None: ...

class MutateBillingSetupResponse(_message.Message):
    __slots__ = ("result",)
    RESULT_FIELD_NUMBER: _ClassVar[int]
    result: MutateBillingSetupResult
    def __init__(self, result: _Optional[_Union[MutateBillingSetupResult, _Mapping]] = ...) -> None: ...

class MutateBillingSetupResult(_message.Message):
    __slots__ = ("resource_name",)
    RESOURCE_NAME_FIELD_NUMBER: _ClassVar[int]
    resource_name: str
    def __init__(self, resource_name: _Optional[str] = ...) -> None: ...
