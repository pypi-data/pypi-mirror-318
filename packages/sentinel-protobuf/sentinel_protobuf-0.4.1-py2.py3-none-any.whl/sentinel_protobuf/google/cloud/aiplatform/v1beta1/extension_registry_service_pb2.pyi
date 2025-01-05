from google.api import annotations_pb2 as _annotations_pb2
from google.api import client_pb2 as _client_pb2
from google.api import field_behavior_pb2 as _field_behavior_pb2
from google.api import resource_pb2 as _resource_pb2
from google.cloud.aiplatform.v1beta1 import extension_pb2 as _extension_pb2
from google.cloud.aiplatform.v1beta1 import operation_pb2 as _operation_pb2
from google.longrunning import operations_pb2 as _operations_pb2
from google.protobuf import empty_pb2 as _empty_pb2
from google.protobuf import field_mask_pb2 as _field_mask_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class ImportExtensionRequest(_message.Message):
    __slots__ = ("parent", "extension")
    PARENT_FIELD_NUMBER: _ClassVar[int]
    EXTENSION_FIELD_NUMBER: _ClassVar[int]
    parent: str
    extension: _extension_pb2.Extension
    def __init__(self, parent: _Optional[str] = ..., extension: _Optional[_Union[_extension_pb2.Extension, _Mapping]] = ...) -> None: ...

class ImportExtensionOperationMetadata(_message.Message):
    __slots__ = ("generic_metadata",)
    GENERIC_METADATA_FIELD_NUMBER: _ClassVar[int]
    generic_metadata: _operation_pb2.GenericOperationMetadata
    def __init__(self, generic_metadata: _Optional[_Union[_operation_pb2.GenericOperationMetadata, _Mapping]] = ...) -> None: ...

class GetExtensionRequest(_message.Message):
    __slots__ = ("name",)
    NAME_FIELD_NUMBER: _ClassVar[int]
    name: str
    def __init__(self, name: _Optional[str] = ...) -> None: ...

class UpdateExtensionRequest(_message.Message):
    __slots__ = ("extension", "update_mask")
    EXTENSION_FIELD_NUMBER: _ClassVar[int]
    UPDATE_MASK_FIELD_NUMBER: _ClassVar[int]
    extension: _extension_pb2.Extension
    update_mask: _field_mask_pb2.FieldMask
    def __init__(self, extension: _Optional[_Union[_extension_pb2.Extension, _Mapping]] = ..., update_mask: _Optional[_Union[_field_mask_pb2.FieldMask, _Mapping]] = ...) -> None: ...

class ListExtensionsRequest(_message.Message):
    __slots__ = ("parent", "filter", "page_size", "page_token", "order_by")
    PARENT_FIELD_NUMBER: _ClassVar[int]
    FILTER_FIELD_NUMBER: _ClassVar[int]
    PAGE_SIZE_FIELD_NUMBER: _ClassVar[int]
    PAGE_TOKEN_FIELD_NUMBER: _ClassVar[int]
    ORDER_BY_FIELD_NUMBER: _ClassVar[int]
    parent: str
    filter: str
    page_size: int
    page_token: str
    order_by: str
    def __init__(self, parent: _Optional[str] = ..., filter: _Optional[str] = ..., page_size: _Optional[int] = ..., page_token: _Optional[str] = ..., order_by: _Optional[str] = ...) -> None: ...

class ListExtensionsResponse(_message.Message):
    __slots__ = ("extensions", "next_page_token")
    EXTENSIONS_FIELD_NUMBER: _ClassVar[int]
    NEXT_PAGE_TOKEN_FIELD_NUMBER: _ClassVar[int]
    extensions: _containers.RepeatedCompositeFieldContainer[_extension_pb2.Extension]
    next_page_token: str
    def __init__(self, extensions: _Optional[_Iterable[_Union[_extension_pb2.Extension, _Mapping]]] = ..., next_page_token: _Optional[str] = ...) -> None: ...

class DeleteExtensionRequest(_message.Message):
    __slots__ = ("name",)
    NAME_FIELD_NUMBER: _ClassVar[int]
    name: str
    def __init__(self, name: _Optional[str] = ...) -> None: ...
