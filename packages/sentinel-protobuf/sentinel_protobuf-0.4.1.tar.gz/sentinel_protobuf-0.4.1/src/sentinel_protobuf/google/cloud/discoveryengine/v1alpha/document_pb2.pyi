from google.api import field_behavior_pb2 as _field_behavior_pb2
from google.api import resource_pb2 as _resource_pb2
from google.cloud.discoveryengine.v1alpha import common_pb2 as _common_pb2
from google.protobuf import struct_pb2 as _struct_pb2
from google.protobuf import timestamp_pb2 as _timestamp_pb2
from google.rpc import status_pb2 as _status_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union
DESCRIPTOR: _descriptor.FileDescriptor

class Document(_message.Message):
    __slots__ = ('struct_data', 'json_data', 'name', 'id', 'schema_id', 'content', 'parent_document_id', 'derived_struct_data', 'acl_info', 'index_time', 'index_status')

    class Content(_message.Message):
        __slots__ = ('raw_bytes', 'uri', 'mime_type')
        RAW_BYTES_FIELD_NUMBER: _ClassVar[int]
        URI_FIELD_NUMBER: _ClassVar[int]
        MIME_TYPE_FIELD_NUMBER: _ClassVar[int]
        raw_bytes: bytes
        uri: str
        mime_type: str

        def __init__(self, raw_bytes: _Optional[bytes]=..., uri: _Optional[str]=..., mime_type: _Optional[str]=...) -> None:
            ...

    class AclInfo(_message.Message):
        __slots__ = ('readers',)

        class AccessRestriction(_message.Message):
            __slots__ = ('principals', 'idp_wide')
            PRINCIPALS_FIELD_NUMBER: _ClassVar[int]
            IDP_WIDE_FIELD_NUMBER: _ClassVar[int]
            principals: _containers.RepeatedCompositeFieldContainer[_common_pb2.Principal]
            idp_wide: bool

            def __init__(self, principals: _Optional[_Iterable[_Union[_common_pb2.Principal, _Mapping]]]=..., idp_wide: bool=...) -> None:
                ...
        READERS_FIELD_NUMBER: _ClassVar[int]
        readers: _containers.RepeatedCompositeFieldContainer[Document.AclInfo.AccessRestriction]

        def __init__(self, readers: _Optional[_Iterable[_Union[Document.AclInfo.AccessRestriction, _Mapping]]]=...) -> None:
            ...

    class IndexStatus(_message.Message):
        __slots__ = ('index_time', 'error_samples')
        INDEX_TIME_FIELD_NUMBER: _ClassVar[int]
        ERROR_SAMPLES_FIELD_NUMBER: _ClassVar[int]
        index_time: _timestamp_pb2.Timestamp
        error_samples: _containers.RepeatedCompositeFieldContainer[_status_pb2.Status]

        def __init__(self, index_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]]=..., error_samples: _Optional[_Iterable[_Union[_status_pb2.Status, _Mapping]]]=...) -> None:
            ...
    STRUCT_DATA_FIELD_NUMBER: _ClassVar[int]
    JSON_DATA_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    ID_FIELD_NUMBER: _ClassVar[int]
    SCHEMA_ID_FIELD_NUMBER: _ClassVar[int]
    CONTENT_FIELD_NUMBER: _ClassVar[int]
    PARENT_DOCUMENT_ID_FIELD_NUMBER: _ClassVar[int]
    DERIVED_STRUCT_DATA_FIELD_NUMBER: _ClassVar[int]
    ACL_INFO_FIELD_NUMBER: _ClassVar[int]
    INDEX_TIME_FIELD_NUMBER: _ClassVar[int]
    INDEX_STATUS_FIELD_NUMBER: _ClassVar[int]
    struct_data: _struct_pb2.Struct
    json_data: str
    name: str
    id: str
    schema_id: str
    content: Document.Content
    parent_document_id: str
    derived_struct_data: _struct_pb2.Struct
    acl_info: Document.AclInfo
    index_time: _timestamp_pb2.Timestamp
    index_status: Document.IndexStatus

    def __init__(self, struct_data: _Optional[_Union[_struct_pb2.Struct, _Mapping]]=..., json_data: _Optional[str]=..., name: _Optional[str]=..., id: _Optional[str]=..., schema_id: _Optional[str]=..., content: _Optional[_Union[Document.Content, _Mapping]]=..., parent_document_id: _Optional[str]=..., derived_struct_data: _Optional[_Union[_struct_pb2.Struct, _Mapping]]=..., acl_info: _Optional[_Union[Document.AclInfo, _Mapping]]=..., index_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]]=..., index_status: _Optional[_Union[Document.IndexStatus, _Mapping]]=...) -> None:
        ...

class ProcessedDocument(_message.Message):
    __slots__ = ('json_data', 'document')
    JSON_DATA_FIELD_NUMBER: _ClassVar[int]
    DOCUMENT_FIELD_NUMBER: _ClassVar[int]
    json_data: str
    document: str

    def __init__(self, json_data: _Optional[str]=..., document: _Optional[str]=...) -> None:
        ...