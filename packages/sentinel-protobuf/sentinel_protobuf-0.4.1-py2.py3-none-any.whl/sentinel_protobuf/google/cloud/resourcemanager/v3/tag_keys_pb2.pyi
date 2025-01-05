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
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union
DESCRIPTOR: _descriptor.FileDescriptor

class Purpose(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    PURPOSE_UNSPECIFIED: _ClassVar[Purpose]
    GCE_FIREWALL: _ClassVar[Purpose]
PURPOSE_UNSPECIFIED: Purpose
GCE_FIREWALL: Purpose

class TagKey(_message.Message):
    __slots__ = ('name', 'parent', 'short_name', 'namespaced_name', 'description', 'create_time', 'update_time', 'etag', 'purpose', 'purpose_data')

    class PurposeDataEntry(_message.Message):
        __slots__ = ('key', 'value')
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: str

        def __init__(self, key: _Optional[str]=..., value: _Optional[str]=...) -> None:
            ...
    NAME_FIELD_NUMBER: _ClassVar[int]
    PARENT_FIELD_NUMBER: _ClassVar[int]
    SHORT_NAME_FIELD_NUMBER: _ClassVar[int]
    NAMESPACED_NAME_FIELD_NUMBER: _ClassVar[int]
    DESCRIPTION_FIELD_NUMBER: _ClassVar[int]
    CREATE_TIME_FIELD_NUMBER: _ClassVar[int]
    UPDATE_TIME_FIELD_NUMBER: _ClassVar[int]
    ETAG_FIELD_NUMBER: _ClassVar[int]
    PURPOSE_FIELD_NUMBER: _ClassVar[int]
    PURPOSE_DATA_FIELD_NUMBER: _ClassVar[int]
    name: str
    parent: str
    short_name: str
    namespaced_name: str
    description: str
    create_time: _timestamp_pb2.Timestamp
    update_time: _timestamp_pb2.Timestamp
    etag: str
    purpose: Purpose
    purpose_data: _containers.ScalarMap[str, str]

    def __init__(self, name: _Optional[str]=..., parent: _Optional[str]=..., short_name: _Optional[str]=..., namespaced_name: _Optional[str]=..., description: _Optional[str]=..., create_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]]=..., update_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]]=..., etag: _Optional[str]=..., purpose: _Optional[_Union[Purpose, str]]=..., purpose_data: _Optional[_Mapping[str, str]]=...) -> None:
        ...

class ListTagKeysRequest(_message.Message):
    __slots__ = ('parent', 'page_size', 'page_token')
    PARENT_FIELD_NUMBER: _ClassVar[int]
    PAGE_SIZE_FIELD_NUMBER: _ClassVar[int]
    PAGE_TOKEN_FIELD_NUMBER: _ClassVar[int]
    parent: str
    page_size: int
    page_token: str

    def __init__(self, parent: _Optional[str]=..., page_size: _Optional[int]=..., page_token: _Optional[str]=...) -> None:
        ...

class ListTagKeysResponse(_message.Message):
    __slots__ = ('tag_keys', 'next_page_token')
    TAG_KEYS_FIELD_NUMBER: _ClassVar[int]
    NEXT_PAGE_TOKEN_FIELD_NUMBER: _ClassVar[int]
    tag_keys: _containers.RepeatedCompositeFieldContainer[TagKey]
    next_page_token: str

    def __init__(self, tag_keys: _Optional[_Iterable[_Union[TagKey, _Mapping]]]=..., next_page_token: _Optional[str]=...) -> None:
        ...

class GetTagKeyRequest(_message.Message):
    __slots__ = ('name',)
    NAME_FIELD_NUMBER: _ClassVar[int]
    name: str

    def __init__(self, name: _Optional[str]=...) -> None:
        ...

class GetNamespacedTagKeyRequest(_message.Message):
    __slots__ = ('name',)
    NAME_FIELD_NUMBER: _ClassVar[int]
    name: str

    def __init__(self, name: _Optional[str]=...) -> None:
        ...

class CreateTagKeyRequest(_message.Message):
    __slots__ = ('tag_key', 'validate_only')
    TAG_KEY_FIELD_NUMBER: _ClassVar[int]
    VALIDATE_ONLY_FIELD_NUMBER: _ClassVar[int]
    tag_key: TagKey
    validate_only: bool

    def __init__(self, tag_key: _Optional[_Union[TagKey, _Mapping]]=..., validate_only: bool=...) -> None:
        ...

class CreateTagKeyMetadata(_message.Message):
    __slots__ = ()

    def __init__(self) -> None:
        ...

class UpdateTagKeyRequest(_message.Message):
    __slots__ = ('tag_key', 'update_mask', 'validate_only')
    TAG_KEY_FIELD_NUMBER: _ClassVar[int]
    UPDATE_MASK_FIELD_NUMBER: _ClassVar[int]
    VALIDATE_ONLY_FIELD_NUMBER: _ClassVar[int]
    tag_key: TagKey
    update_mask: _field_mask_pb2.FieldMask
    validate_only: bool

    def __init__(self, tag_key: _Optional[_Union[TagKey, _Mapping]]=..., update_mask: _Optional[_Union[_field_mask_pb2.FieldMask, _Mapping]]=..., validate_only: bool=...) -> None:
        ...

class UpdateTagKeyMetadata(_message.Message):
    __slots__ = ()

    def __init__(self) -> None:
        ...

class DeleteTagKeyRequest(_message.Message):
    __slots__ = ('name', 'validate_only', 'etag')
    NAME_FIELD_NUMBER: _ClassVar[int]
    VALIDATE_ONLY_FIELD_NUMBER: _ClassVar[int]
    ETAG_FIELD_NUMBER: _ClassVar[int]
    name: str
    validate_only: bool
    etag: str

    def __init__(self, name: _Optional[str]=..., validate_only: bool=..., etag: _Optional[str]=...) -> None:
        ...

class DeleteTagKeyMetadata(_message.Message):
    __slots__ = ()

    def __init__(self) -> None:
        ...