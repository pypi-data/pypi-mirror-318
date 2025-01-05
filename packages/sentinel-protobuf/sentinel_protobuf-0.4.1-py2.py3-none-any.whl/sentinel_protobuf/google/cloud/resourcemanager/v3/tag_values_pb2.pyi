from google.api import annotations_pb2 as _annotations_pb2
from google.api import client_pb2 as _client_pb2
from google.api import field_behavior_pb2 as _field_behavior_pb2
from google.api import resource_pb2 as _resource_pb2
from google.iam.v1 import iam_policy_pb2 as _iam_policy_pb2
from google.iam.v1 import policy_pb2 as _policy_pb2
from google.longrunning import operations_pb2 as _operations_pb2
from google.protobuf import field_mask_pb2 as _field_mask_pb2
from google.protobuf import timestamp_pb2 as _timestamp_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union
DESCRIPTOR: _descriptor.FileDescriptor

class TagValue(_message.Message):
    __slots__ = ('name', 'parent', 'short_name', 'namespaced_name', 'description', 'create_time', 'update_time', 'etag')
    NAME_FIELD_NUMBER: _ClassVar[int]
    PARENT_FIELD_NUMBER: _ClassVar[int]
    SHORT_NAME_FIELD_NUMBER: _ClassVar[int]
    NAMESPACED_NAME_FIELD_NUMBER: _ClassVar[int]
    DESCRIPTION_FIELD_NUMBER: _ClassVar[int]
    CREATE_TIME_FIELD_NUMBER: _ClassVar[int]
    UPDATE_TIME_FIELD_NUMBER: _ClassVar[int]
    ETAG_FIELD_NUMBER: _ClassVar[int]
    name: str
    parent: str
    short_name: str
    namespaced_name: str
    description: str
    create_time: _timestamp_pb2.Timestamp
    update_time: _timestamp_pb2.Timestamp
    etag: str

    def __init__(self, name: _Optional[str]=..., parent: _Optional[str]=..., short_name: _Optional[str]=..., namespaced_name: _Optional[str]=..., description: _Optional[str]=..., create_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]]=..., update_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]]=..., etag: _Optional[str]=...) -> None:
        ...

class ListTagValuesRequest(_message.Message):
    __slots__ = ('parent', 'page_size', 'page_token')
    PARENT_FIELD_NUMBER: _ClassVar[int]
    PAGE_SIZE_FIELD_NUMBER: _ClassVar[int]
    PAGE_TOKEN_FIELD_NUMBER: _ClassVar[int]
    parent: str
    page_size: int
    page_token: str

    def __init__(self, parent: _Optional[str]=..., page_size: _Optional[int]=..., page_token: _Optional[str]=...) -> None:
        ...

class ListTagValuesResponse(_message.Message):
    __slots__ = ('tag_values', 'next_page_token')
    TAG_VALUES_FIELD_NUMBER: _ClassVar[int]
    NEXT_PAGE_TOKEN_FIELD_NUMBER: _ClassVar[int]
    tag_values: _containers.RepeatedCompositeFieldContainer[TagValue]
    next_page_token: str

    def __init__(self, tag_values: _Optional[_Iterable[_Union[TagValue, _Mapping]]]=..., next_page_token: _Optional[str]=...) -> None:
        ...

class GetTagValueRequest(_message.Message):
    __slots__ = ('name',)
    NAME_FIELD_NUMBER: _ClassVar[int]
    name: str

    def __init__(self, name: _Optional[str]=...) -> None:
        ...

class GetNamespacedTagValueRequest(_message.Message):
    __slots__ = ('name',)
    NAME_FIELD_NUMBER: _ClassVar[int]
    name: str

    def __init__(self, name: _Optional[str]=...) -> None:
        ...

class CreateTagValueRequest(_message.Message):
    __slots__ = ('tag_value', 'validate_only')
    TAG_VALUE_FIELD_NUMBER: _ClassVar[int]
    VALIDATE_ONLY_FIELD_NUMBER: _ClassVar[int]
    tag_value: TagValue
    validate_only: bool

    def __init__(self, tag_value: _Optional[_Union[TagValue, _Mapping]]=..., validate_only: bool=...) -> None:
        ...

class CreateTagValueMetadata(_message.Message):
    __slots__ = ()

    def __init__(self) -> None:
        ...

class UpdateTagValueRequest(_message.Message):
    __slots__ = ('tag_value', 'update_mask', 'validate_only')
    TAG_VALUE_FIELD_NUMBER: _ClassVar[int]
    UPDATE_MASK_FIELD_NUMBER: _ClassVar[int]
    VALIDATE_ONLY_FIELD_NUMBER: _ClassVar[int]
    tag_value: TagValue
    update_mask: _field_mask_pb2.FieldMask
    validate_only: bool

    def __init__(self, tag_value: _Optional[_Union[TagValue, _Mapping]]=..., update_mask: _Optional[_Union[_field_mask_pb2.FieldMask, _Mapping]]=..., validate_only: bool=...) -> None:
        ...

class UpdateTagValueMetadata(_message.Message):
    __slots__ = ()

    def __init__(self) -> None:
        ...

class DeleteTagValueRequest(_message.Message):
    __slots__ = ('name', 'validate_only', 'etag')
    NAME_FIELD_NUMBER: _ClassVar[int]
    VALIDATE_ONLY_FIELD_NUMBER: _ClassVar[int]
    ETAG_FIELD_NUMBER: _ClassVar[int]
    name: str
    validate_only: bool
    etag: str

    def __init__(self, name: _Optional[str]=..., validate_only: bool=..., etag: _Optional[str]=...) -> None:
        ...

class DeleteTagValueMetadata(_message.Message):
    __slots__ = ()

    def __init__(self) -> None:
        ...