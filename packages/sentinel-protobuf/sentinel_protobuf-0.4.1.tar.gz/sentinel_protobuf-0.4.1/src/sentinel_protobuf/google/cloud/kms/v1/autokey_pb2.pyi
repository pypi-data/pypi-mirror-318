from google.api import annotations_pb2 as _annotations_pb2
from google.api import client_pb2 as _client_pb2
from google.api import field_behavior_pb2 as _field_behavior_pb2
from google.api import resource_pb2 as _resource_pb2
from google.longrunning import operations_pb2 as _operations_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union
DESCRIPTOR: _descriptor.FileDescriptor

class CreateKeyHandleRequest(_message.Message):
    __slots__ = ('parent', 'key_handle_id', 'key_handle')
    PARENT_FIELD_NUMBER: _ClassVar[int]
    KEY_HANDLE_ID_FIELD_NUMBER: _ClassVar[int]
    KEY_HANDLE_FIELD_NUMBER: _ClassVar[int]
    parent: str
    key_handle_id: str
    key_handle: KeyHandle

    def __init__(self, parent: _Optional[str]=..., key_handle_id: _Optional[str]=..., key_handle: _Optional[_Union[KeyHandle, _Mapping]]=...) -> None:
        ...

class GetKeyHandleRequest(_message.Message):
    __slots__ = ('name',)
    NAME_FIELD_NUMBER: _ClassVar[int]
    name: str

    def __init__(self, name: _Optional[str]=...) -> None:
        ...

class KeyHandle(_message.Message):
    __slots__ = ('name', 'kms_key', 'resource_type_selector')
    NAME_FIELD_NUMBER: _ClassVar[int]
    KMS_KEY_FIELD_NUMBER: _ClassVar[int]
    RESOURCE_TYPE_SELECTOR_FIELD_NUMBER: _ClassVar[int]
    name: str
    kms_key: str
    resource_type_selector: str

    def __init__(self, name: _Optional[str]=..., kms_key: _Optional[str]=..., resource_type_selector: _Optional[str]=...) -> None:
        ...

class CreateKeyHandleMetadata(_message.Message):
    __slots__ = ()

    def __init__(self) -> None:
        ...

class ListKeyHandlesRequest(_message.Message):
    __slots__ = ('parent', 'page_size', 'page_token', 'filter')
    PARENT_FIELD_NUMBER: _ClassVar[int]
    PAGE_SIZE_FIELD_NUMBER: _ClassVar[int]
    PAGE_TOKEN_FIELD_NUMBER: _ClassVar[int]
    FILTER_FIELD_NUMBER: _ClassVar[int]
    parent: str
    page_size: int
    page_token: str
    filter: str

    def __init__(self, parent: _Optional[str]=..., page_size: _Optional[int]=..., page_token: _Optional[str]=..., filter: _Optional[str]=...) -> None:
        ...

class ListKeyHandlesResponse(_message.Message):
    __slots__ = ('key_handles', 'next_page_token')
    KEY_HANDLES_FIELD_NUMBER: _ClassVar[int]
    NEXT_PAGE_TOKEN_FIELD_NUMBER: _ClassVar[int]
    key_handles: _containers.RepeatedCompositeFieldContainer[KeyHandle]
    next_page_token: str

    def __init__(self, key_handles: _Optional[_Iterable[_Union[KeyHandle, _Mapping]]]=..., next_page_token: _Optional[str]=...) -> None:
        ...