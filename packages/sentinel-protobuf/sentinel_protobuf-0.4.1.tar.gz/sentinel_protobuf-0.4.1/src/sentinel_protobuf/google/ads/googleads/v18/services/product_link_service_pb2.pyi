from google.ads.googleads.v18.resources import product_link_pb2 as _product_link_pb2
from google.api import annotations_pb2 as _annotations_pb2
from google.api import client_pb2 as _client_pb2
from google.api import field_behavior_pb2 as _field_behavior_pb2
from google.api import resource_pb2 as _resource_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class CreateProductLinkRequest(_message.Message):
    __slots__ = ("customer_id", "product_link")
    CUSTOMER_ID_FIELD_NUMBER: _ClassVar[int]
    PRODUCT_LINK_FIELD_NUMBER: _ClassVar[int]
    customer_id: str
    product_link: _product_link_pb2.ProductLink
    def __init__(self, customer_id: _Optional[str] = ..., product_link: _Optional[_Union[_product_link_pb2.ProductLink, _Mapping]] = ...) -> None: ...

class CreateProductLinkResponse(_message.Message):
    __slots__ = ("resource_name",)
    RESOURCE_NAME_FIELD_NUMBER: _ClassVar[int]
    resource_name: str
    def __init__(self, resource_name: _Optional[str] = ...) -> None: ...

class RemoveProductLinkRequest(_message.Message):
    __slots__ = ("customer_id", "resource_name", "validate_only")
    CUSTOMER_ID_FIELD_NUMBER: _ClassVar[int]
    RESOURCE_NAME_FIELD_NUMBER: _ClassVar[int]
    VALIDATE_ONLY_FIELD_NUMBER: _ClassVar[int]
    customer_id: str
    resource_name: str
    validate_only: bool
    def __init__(self, customer_id: _Optional[str] = ..., resource_name: _Optional[str] = ..., validate_only: bool = ...) -> None: ...

class RemoveProductLinkResponse(_message.Message):
    __slots__ = ("resource_name",)
    RESOURCE_NAME_FIELD_NUMBER: _ClassVar[int]
    resource_name: str
    def __init__(self, resource_name: _Optional[str] = ...) -> None: ...
