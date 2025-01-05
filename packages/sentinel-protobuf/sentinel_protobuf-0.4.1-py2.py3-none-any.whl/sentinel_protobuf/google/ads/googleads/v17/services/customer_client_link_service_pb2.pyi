from google.ads.googleads.v17.resources import customer_client_link_pb2 as _customer_client_link_pb2
from google.api import annotations_pb2 as _annotations_pb2
from google.api import client_pb2 as _client_pb2
from google.api import field_behavior_pb2 as _field_behavior_pb2
from google.api import resource_pb2 as _resource_pb2
from google.protobuf import field_mask_pb2 as _field_mask_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class MutateCustomerClientLinkRequest(_message.Message):
    __slots__ = ("customer_id", "operation", "validate_only")
    CUSTOMER_ID_FIELD_NUMBER: _ClassVar[int]
    OPERATION_FIELD_NUMBER: _ClassVar[int]
    VALIDATE_ONLY_FIELD_NUMBER: _ClassVar[int]
    customer_id: str
    operation: CustomerClientLinkOperation
    validate_only: bool
    def __init__(self, customer_id: _Optional[str] = ..., operation: _Optional[_Union[CustomerClientLinkOperation, _Mapping]] = ..., validate_only: bool = ...) -> None: ...

class CustomerClientLinkOperation(_message.Message):
    __slots__ = ("update_mask", "create", "update")
    UPDATE_MASK_FIELD_NUMBER: _ClassVar[int]
    CREATE_FIELD_NUMBER: _ClassVar[int]
    UPDATE_FIELD_NUMBER: _ClassVar[int]
    update_mask: _field_mask_pb2.FieldMask
    create: _customer_client_link_pb2.CustomerClientLink
    update: _customer_client_link_pb2.CustomerClientLink
    def __init__(self, update_mask: _Optional[_Union[_field_mask_pb2.FieldMask, _Mapping]] = ..., create: _Optional[_Union[_customer_client_link_pb2.CustomerClientLink, _Mapping]] = ..., update: _Optional[_Union[_customer_client_link_pb2.CustomerClientLink, _Mapping]] = ...) -> None: ...

class MutateCustomerClientLinkResponse(_message.Message):
    __slots__ = ("result",)
    RESULT_FIELD_NUMBER: _ClassVar[int]
    result: MutateCustomerClientLinkResult
    def __init__(self, result: _Optional[_Union[MutateCustomerClientLinkResult, _Mapping]] = ...) -> None: ...

class MutateCustomerClientLinkResult(_message.Message):
    __slots__ = ("resource_name",)
    RESOURCE_NAME_FIELD_NUMBER: _ClassVar[int]
    resource_name: str
    def __init__(self, resource_name: _Optional[str] = ...) -> None: ...
