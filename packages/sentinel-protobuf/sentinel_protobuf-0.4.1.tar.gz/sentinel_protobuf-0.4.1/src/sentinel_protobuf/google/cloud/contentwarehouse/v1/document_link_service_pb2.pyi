from google.api import annotations_pb2 as _annotations_pb2
from google.api import client_pb2 as _client_pb2
from google.api import field_behavior_pb2 as _field_behavior_pb2
from google.api import resource_pb2 as _resource_pb2
from google.cloud.contentwarehouse.v1 import common_pb2 as _common_pb2
from google.cloud.contentwarehouse.v1 import document_pb2 as _document_pb2
from google.protobuf import empty_pb2 as _empty_pb2
from google.protobuf import timestamp_pb2 as _timestamp_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class ListLinkedTargetsResponse(_message.Message):
    __slots__ = ("document_links", "next_page_token")
    DOCUMENT_LINKS_FIELD_NUMBER: _ClassVar[int]
    NEXT_PAGE_TOKEN_FIELD_NUMBER: _ClassVar[int]
    document_links: _containers.RepeatedCompositeFieldContainer[DocumentLink]
    next_page_token: str
    def __init__(self, document_links: _Optional[_Iterable[_Union[DocumentLink, _Mapping]]] = ..., next_page_token: _Optional[str] = ...) -> None: ...

class ListLinkedTargetsRequest(_message.Message):
    __slots__ = ("parent", "request_metadata")
    PARENT_FIELD_NUMBER: _ClassVar[int]
    REQUEST_METADATA_FIELD_NUMBER: _ClassVar[int]
    parent: str
    request_metadata: _common_pb2.RequestMetadata
    def __init__(self, parent: _Optional[str] = ..., request_metadata: _Optional[_Union[_common_pb2.RequestMetadata, _Mapping]] = ...) -> None: ...

class ListLinkedSourcesResponse(_message.Message):
    __slots__ = ("document_links", "next_page_token")
    DOCUMENT_LINKS_FIELD_NUMBER: _ClassVar[int]
    NEXT_PAGE_TOKEN_FIELD_NUMBER: _ClassVar[int]
    document_links: _containers.RepeatedCompositeFieldContainer[DocumentLink]
    next_page_token: str
    def __init__(self, document_links: _Optional[_Iterable[_Union[DocumentLink, _Mapping]]] = ..., next_page_token: _Optional[str] = ...) -> None: ...

class ListLinkedSourcesRequest(_message.Message):
    __slots__ = ("parent", "page_size", "page_token", "request_metadata")
    PARENT_FIELD_NUMBER: _ClassVar[int]
    PAGE_SIZE_FIELD_NUMBER: _ClassVar[int]
    PAGE_TOKEN_FIELD_NUMBER: _ClassVar[int]
    REQUEST_METADATA_FIELD_NUMBER: _ClassVar[int]
    parent: str
    page_size: int
    page_token: str
    request_metadata: _common_pb2.RequestMetadata
    def __init__(self, parent: _Optional[str] = ..., page_size: _Optional[int] = ..., page_token: _Optional[str] = ..., request_metadata: _Optional[_Union[_common_pb2.RequestMetadata, _Mapping]] = ...) -> None: ...

class DocumentLink(_message.Message):
    __slots__ = ("name", "source_document_reference", "target_document_reference", "description", "update_time", "create_time", "state")
    class State(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        STATE_UNSPECIFIED: _ClassVar[DocumentLink.State]
        ACTIVE: _ClassVar[DocumentLink.State]
        SOFT_DELETED: _ClassVar[DocumentLink.State]
    STATE_UNSPECIFIED: DocumentLink.State
    ACTIVE: DocumentLink.State
    SOFT_DELETED: DocumentLink.State
    NAME_FIELD_NUMBER: _ClassVar[int]
    SOURCE_DOCUMENT_REFERENCE_FIELD_NUMBER: _ClassVar[int]
    TARGET_DOCUMENT_REFERENCE_FIELD_NUMBER: _ClassVar[int]
    DESCRIPTION_FIELD_NUMBER: _ClassVar[int]
    UPDATE_TIME_FIELD_NUMBER: _ClassVar[int]
    CREATE_TIME_FIELD_NUMBER: _ClassVar[int]
    STATE_FIELD_NUMBER: _ClassVar[int]
    name: str
    source_document_reference: _document_pb2.DocumentReference
    target_document_reference: _document_pb2.DocumentReference
    description: str
    update_time: _timestamp_pb2.Timestamp
    create_time: _timestamp_pb2.Timestamp
    state: DocumentLink.State
    def __init__(self, name: _Optional[str] = ..., source_document_reference: _Optional[_Union[_document_pb2.DocumentReference, _Mapping]] = ..., target_document_reference: _Optional[_Union[_document_pb2.DocumentReference, _Mapping]] = ..., description: _Optional[str] = ..., update_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., create_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., state: _Optional[_Union[DocumentLink.State, str]] = ...) -> None: ...

class CreateDocumentLinkRequest(_message.Message):
    __slots__ = ("parent", "document_link", "request_metadata")
    PARENT_FIELD_NUMBER: _ClassVar[int]
    DOCUMENT_LINK_FIELD_NUMBER: _ClassVar[int]
    REQUEST_METADATA_FIELD_NUMBER: _ClassVar[int]
    parent: str
    document_link: DocumentLink
    request_metadata: _common_pb2.RequestMetadata
    def __init__(self, parent: _Optional[str] = ..., document_link: _Optional[_Union[DocumentLink, _Mapping]] = ..., request_metadata: _Optional[_Union[_common_pb2.RequestMetadata, _Mapping]] = ...) -> None: ...

class DeleteDocumentLinkRequest(_message.Message):
    __slots__ = ("name", "request_metadata")
    NAME_FIELD_NUMBER: _ClassVar[int]
    REQUEST_METADATA_FIELD_NUMBER: _ClassVar[int]
    name: str
    request_metadata: _common_pb2.RequestMetadata
    def __init__(self, name: _Optional[str] = ..., request_metadata: _Optional[_Union[_common_pb2.RequestMetadata, _Mapping]] = ...) -> None: ...
