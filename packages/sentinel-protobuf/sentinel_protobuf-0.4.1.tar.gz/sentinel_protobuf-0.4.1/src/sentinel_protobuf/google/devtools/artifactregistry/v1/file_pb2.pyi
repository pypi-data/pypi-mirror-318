from google.api import field_behavior_pb2 as _field_behavior_pb2
from google.api import resource_pb2 as _resource_pb2
from google.protobuf import field_mask_pb2 as _field_mask_pb2
from google.protobuf import timestamp_pb2 as _timestamp_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union
DESCRIPTOR: _descriptor.FileDescriptor

class Hash(_message.Message):
    __slots__ = ('type', 'value')

    class HashType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        HASH_TYPE_UNSPECIFIED: _ClassVar[Hash.HashType]
        SHA256: _ClassVar[Hash.HashType]
        MD5: _ClassVar[Hash.HashType]
    HASH_TYPE_UNSPECIFIED: Hash.HashType
    SHA256: Hash.HashType
    MD5: Hash.HashType
    TYPE_FIELD_NUMBER: _ClassVar[int]
    VALUE_FIELD_NUMBER: _ClassVar[int]
    type: Hash.HashType
    value: bytes

    def __init__(self, type: _Optional[_Union[Hash.HashType, str]]=..., value: _Optional[bytes]=...) -> None:
        ...

class File(_message.Message):
    __slots__ = ('name', 'size_bytes', 'hashes', 'create_time', 'update_time', 'owner', 'fetch_time', 'annotations')

    class AnnotationsEntry(_message.Message):
        __slots__ = ('key', 'value')
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: str

        def __init__(self, key: _Optional[str]=..., value: _Optional[str]=...) -> None:
            ...
    NAME_FIELD_NUMBER: _ClassVar[int]
    SIZE_BYTES_FIELD_NUMBER: _ClassVar[int]
    HASHES_FIELD_NUMBER: _ClassVar[int]
    CREATE_TIME_FIELD_NUMBER: _ClassVar[int]
    UPDATE_TIME_FIELD_NUMBER: _ClassVar[int]
    OWNER_FIELD_NUMBER: _ClassVar[int]
    FETCH_TIME_FIELD_NUMBER: _ClassVar[int]
    ANNOTATIONS_FIELD_NUMBER: _ClassVar[int]
    name: str
    size_bytes: int
    hashes: _containers.RepeatedCompositeFieldContainer[Hash]
    create_time: _timestamp_pb2.Timestamp
    update_time: _timestamp_pb2.Timestamp
    owner: str
    fetch_time: _timestamp_pb2.Timestamp
    annotations: _containers.ScalarMap[str, str]

    def __init__(self, name: _Optional[str]=..., size_bytes: _Optional[int]=..., hashes: _Optional[_Iterable[_Union[Hash, _Mapping]]]=..., create_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]]=..., update_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]]=..., owner: _Optional[str]=..., fetch_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]]=..., annotations: _Optional[_Mapping[str, str]]=...) -> None:
        ...

class ListFilesRequest(_message.Message):
    __slots__ = ('parent', 'filter', 'page_size', 'page_token', 'order_by')
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

    def __init__(self, parent: _Optional[str]=..., filter: _Optional[str]=..., page_size: _Optional[int]=..., page_token: _Optional[str]=..., order_by: _Optional[str]=...) -> None:
        ...

class ListFilesResponse(_message.Message):
    __slots__ = ('files', 'next_page_token')
    FILES_FIELD_NUMBER: _ClassVar[int]
    NEXT_PAGE_TOKEN_FIELD_NUMBER: _ClassVar[int]
    files: _containers.RepeatedCompositeFieldContainer[File]
    next_page_token: str

    def __init__(self, files: _Optional[_Iterable[_Union[File, _Mapping]]]=..., next_page_token: _Optional[str]=...) -> None:
        ...

class GetFileRequest(_message.Message):
    __slots__ = ('name',)
    NAME_FIELD_NUMBER: _ClassVar[int]
    name: str

    def __init__(self, name: _Optional[str]=...) -> None:
        ...

class DeleteFileRequest(_message.Message):
    __slots__ = ('name',)
    NAME_FIELD_NUMBER: _ClassVar[int]
    name: str

    def __init__(self, name: _Optional[str]=...) -> None:
        ...

class UpdateFileRequest(_message.Message):
    __slots__ = ('file', 'update_mask')
    FILE_FIELD_NUMBER: _ClassVar[int]
    UPDATE_MASK_FIELD_NUMBER: _ClassVar[int]
    file: File
    update_mask: _field_mask_pb2.FieldMask

    def __init__(self, file: _Optional[_Union[File, _Mapping]]=..., update_mask: _Optional[_Union[_field_mask_pb2.FieldMask, _Mapping]]=...) -> None:
        ...