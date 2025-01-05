from google.ads.googleads.v16.resources import customer_user_access_pb2 as _customer_user_access_pb2
from google.api import annotations_pb2 as _annotations_pb2
from google.api import client_pb2 as _client_pb2
from google.api import field_behavior_pb2 as _field_behavior_pb2
from google.api import resource_pb2 as _resource_pb2
from google.protobuf import field_mask_pb2 as _field_mask_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class MutateCustomerUserAccessRequest(_message.Message):
    __slots__ = ("customer_id", "operation")
    CUSTOMER_ID_FIELD_NUMBER: _ClassVar[int]
    OPERATION_FIELD_NUMBER: _ClassVar[int]
    customer_id: str
    operation: CustomerUserAccessOperation
    def __init__(self, customer_id: _Optional[str] = ..., operation: _Optional[_Union[CustomerUserAccessOperation, _Mapping]] = ...) -> None: ...

class CustomerUserAccessOperation(_message.Message):
    __slots__ = ("update_mask", "update", "remove")
    UPDATE_MASK_FIELD_NUMBER: _ClassVar[int]
    UPDATE_FIELD_NUMBER: _ClassVar[int]
    REMOVE_FIELD_NUMBER: _ClassVar[int]
    update_mask: _field_mask_pb2.FieldMask
    update: _customer_user_access_pb2.CustomerUserAccess
    remove: str
    def __init__(self, update_mask: _Optional[_Union[_field_mask_pb2.FieldMask, _Mapping]] = ..., update: _Optional[_Union[_customer_user_access_pb2.CustomerUserAccess, _Mapping]] = ..., remove: _Optional[str] = ...) -> None: ...

class MutateCustomerUserAccessResponse(_message.Message):
    __slots__ = ("result",)
    RESULT_FIELD_NUMBER: _ClassVar[int]
    result: MutateCustomerUserAccessResult
    def __init__(self, result: _Optional[_Union[MutateCustomerUserAccessResult, _Mapping]] = ...) -> None: ...

class MutateCustomerUserAccessResult(_message.Message):
    __slots__ = ("resource_name",)
    RESOURCE_NAME_FIELD_NUMBER: _ClassVar[int]
    resource_name: str
    def __init__(self, resource_name: _Optional[str] = ...) -> None: ...
