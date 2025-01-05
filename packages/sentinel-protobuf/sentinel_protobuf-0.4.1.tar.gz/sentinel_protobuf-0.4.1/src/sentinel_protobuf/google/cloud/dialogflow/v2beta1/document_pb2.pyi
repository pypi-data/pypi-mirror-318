from google.api import annotations_pb2 as _annotations_pb2
from google.api import client_pb2 as _client_pb2
from google.api import field_behavior_pb2 as _field_behavior_pb2
from google.api import resource_pb2 as _resource_pb2
from google.cloud.dialogflow.v2beta1 import gcs_pb2 as _gcs_pb2
from google.longrunning import operations_pb2 as _operations_pb2
from google.protobuf import empty_pb2 as _empty_pb2
from google.protobuf import field_mask_pb2 as _field_mask_pb2
from google.protobuf import timestamp_pb2 as _timestamp_pb2
from google.rpc import status_pb2 as _status_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union
DESCRIPTOR: _descriptor.FileDescriptor

class Document(_message.Message):
    __slots__ = ('name', 'display_name', 'mime_type', 'knowledge_types', 'content_uri', 'content', 'raw_content', 'enable_auto_reload', 'latest_reload_status', 'metadata', 'state')

    class KnowledgeType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        KNOWLEDGE_TYPE_UNSPECIFIED: _ClassVar[Document.KnowledgeType]
        FAQ: _ClassVar[Document.KnowledgeType]
        EXTRACTIVE_QA: _ClassVar[Document.KnowledgeType]
        ARTICLE_SUGGESTION: _ClassVar[Document.KnowledgeType]
        AGENT_FACING_SMART_REPLY: _ClassVar[Document.KnowledgeType]
        SMART_REPLY: _ClassVar[Document.KnowledgeType]
    KNOWLEDGE_TYPE_UNSPECIFIED: Document.KnowledgeType
    FAQ: Document.KnowledgeType
    EXTRACTIVE_QA: Document.KnowledgeType
    ARTICLE_SUGGESTION: Document.KnowledgeType
    AGENT_FACING_SMART_REPLY: Document.KnowledgeType
    SMART_REPLY: Document.KnowledgeType

    class State(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        STATE_UNSPECIFIED: _ClassVar[Document.State]
        CREATING: _ClassVar[Document.State]
        ACTIVE: _ClassVar[Document.State]
        UPDATING: _ClassVar[Document.State]
        RELOADING: _ClassVar[Document.State]
        DELETING: _ClassVar[Document.State]
    STATE_UNSPECIFIED: Document.State
    CREATING: Document.State
    ACTIVE: Document.State
    UPDATING: Document.State
    RELOADING: Document.State
    DELETING: Document.State

    class ReloadStatus(_message.Message):
        __slots__ = ('time', 'status')
        TIME_FIELD_NUMBER: _ClassVar[int]
        STATUS_FIELD_NUMBER: _ClassVar[int]
        time: _timestamp_pb2.Timestamp
        status: _status_pb2.Status

        def __init__(self, time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]]=..., status: _Optional[_Union[_status_pb2.Status, _Mapping]]=...) -> None:
            ...

    class MetadataEntry(_message.Message):
        __slots__ = ('key', 'value')
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: str

        def __init__(self, key: _Optional[str]=..., value: _Optional[str]=...) -> None:
            ...
    NAME_FIELD_NUMBER: _ClassVar[int]
    DISPLAY_NAME_FIELD_NUMBER: _ClassVar[int]
    MIME_TYPE_FIELD_NUMBER: _ClassVar[int]
    KNOWLEDGE_TYPES_FIELD_NUMBER: _ClassVar[int]
    CONTENT_URI_FIELD_NUMBER: _ClassVar[int]
    CONTENT_FIELD_NUMBER: _ClassVar[int]
    RAW_CONTENT_FIELD_NUMBER: _ClassVar[int]
    ENABLE_AUTO_RELOAD_FIELD_NUMBER: _ClassVar[int]
    LATEST_RELOAD_STATUS_FIELD_NUMBER: _ClassVar[int]
    METADATA_FIELD_NUMBER: _ClassVar[int]
    STATE_FIELD_NUMBER: _ClassVar[int]
    name: str
    display_name: str
    mime_type: str
    knowledge_types: _containers.RepeatedScalarFieldContainer[Document.KnowledgeType]
    content_uri: str
    content: str
    raw_content: bytes
    enable_auto_reload: bool
    latest_reload_status: Document.ReloadStatus
    metadata: _containers.ScalarMap[str, str]
    state: Document.State

    def __init__(self, name: _Optional[str]=..., display_name: _Optional[str]=..., mime_type: _Optional[str]=..., knowledge_types: _Optional[_Iterable[_Union[Document.KnowledgeType, str]]]=..., content_uri: _Optional[str]=..., content: _Optional[str]=..., raw_content: _Optional[bytes]=..., enable_auto_reload: bool=..., latest_reload_status: _Optional[_Union[Document.ReloadStatus, _Mapping]]=..., metadata: _Optional[_Mapping[str, str]]=..., state: _Optional[_Union[Document.State, str]]=...) -> None:
        ...

class GetDocumentRequest(_message.Message):
    __slots__ = ('name',)
    NAME_FIELD_NUMBER: _ClassVar[int]
    name: str

    def __init__(self, name: _Optional[str]=...) -> None:
        ...

class ListDocumentsRequest(_message.Message):
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

class ListDocumentsResponse(_message.Message):
    __slots__ = ('documents', 'next_page_token')
    DOCUMENTS_FIELD_NUMBER: _ClassVar[int]
    NEXT_PAGE_TOKEN_FIELD_NUMBER: _ClassVar[int]
    documents: _containers.RepeatedCompositeFieldContainer[Document]
    next_page_token: str

    def __init__(self, documents: _Optional[_Iterable[_Union[Document, _Mapping]]]=..., next_page_token: _Optional[str]=...) -> None:
        ...

class CreateDocumentRequest(_message.Message):
    __slots__ = ('parent', 'document', 'import_gcs_custom_metadata')
    PARENT_FIELD_NUMBER: _ClassVar[int]
    DOCUMENT_FIELD_NUMBER: _ClassVar[int]
    IMPORT_GCS_CUSTOM_METADATA_FIELD_NUMBER: _ClassVar[int]
    parent: str
    document: Document
    import_gcs_custom_metadata: bool

    def __init__(self, parent: _Optional[str]=..., document: _Optional[_Union[Document, _Mapping]]=..., import_gcs_custom_metadata: bool=...) -> None:
        ...

class ImportDocumentsRequest(_message.Message):
    __slots__ = ('parent', 'gcs_source', 'document_template', 'import_gcs_custom_metadata')
    PARENT_FIELD_NUMBER: _ClassVar[int]
    GCS_SOURCE_FIELD_NUMBER: _ClassVar[int]
    DOCUMENT_TEMPLATE_FIELD_NUMBER: _ClassVar[int]
    IMPORT_GCS_CUSTOM_METADATA_FIELD_NUMBER: _ClassVar[int]
    parent: str
    gcs_source: _gcs_pb2.GcsSources
    document_template: ImportDocumentTemplate
    import_gcs_custom_metadata: bool

    def __init__(self, parent: _Optional[str]=..., gcs_source: _Optional[_Union[_gcs_pb2.GcsSources, _Mapping]]=..., document_template: _Optional[_Union[ImportDocumentTemplate, _Mapping]]=..., import_gcs_custom_metadata: bool=...) -> None:
        ...

class ImportDocumentTemplate(_message.Message):
    __slots__ = ('mime_type', 'knowledge_types', 'metadata')

    class MetadataEntry(_message.Message):
        __slots__ = ('key', 'value')
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: str

        def __init__(self, key: _Optional[str]=..., value: _Optional[str]=...) -> None:
            ...
    MIME_TYPE_FIELD_NUMBER: _ClassVar[int]
    KNOWLEDGE_TYPES_FIELD_NUMBER: _ClassVar[int]
    METADATA_FIELD_NUMBER: _ClassVar[int]
    mime_type: str
    knowledge_types: _containers.RepeatedScalarFieldContainer[Document.KnowledgeType]
    metadata: _containers.ScalarMap[str, str]

    def __init__(self, mime_type: _Optional[str]=..., knowledge_types: _Optional[_Iterable[_Union[Document.KnowledgeType, str]]]=..., metadata: _Optional[_Mapping[str, str]]=...) -> None:
        ...

class ImportDocumentsResponse(_message.Message):
    __slots__ = ('warnings',)
    WARNINGS_FIELD_NUMBER: _ClassVar[int]
    warnings: _containers.RepeatedCompositeFieldContainer[_status_pb2.Status]

    def __init__(self, warnings: _Optional[_Iterable[_Union[_status_pb2.Status, _Mapping]]]=...) -> None:
        ...

class DeleteDocumentRequest(_message.Message):
    __slots__ = ('name',)
    NAME_FIELD_NUMBER: _ClassVar[int]
    name: str

    def __init__(self, name: _Optional[str]=...) -> None:
        ...

class UpdateDocumentRequest(_message.Message):
    __slots__ = ('document', 'update_mask')
    DOCUMENT_FIELD_NUMBER: _ClassVar[int]
    UPDATE_MASK_FIELD_NUMBER: _ClassVar[int]
    document: Document
    update_mask: _field_mask_pb2.FieldMask

    def __init__(self, document: _Optional[_Union[Document, _Mapping]]=..., update_mask: _Optional[_Union[_field_mask_pb2.FieldMask, _Mapping]]=...) -> None:
        ...

class ExportOperationMetadata(_message.Message):
    __slots__ = ('exported_gcs_destination',)
    EXPORTED_GCS_DESTINATION_FIELD_NUMBER: _ClassVar[int]
    exported_gcs_destination: _gcs_pb2.GcsDestination

    def __init__(self, exported_gcs_destination: _Optional[_Union[_gcs_pb2.GcsDestination, _Mapping]]=...) -> None:
        ...

class KnowledgeOperationMetadata(_message.Message):
    __slots__ = ('state', 'knowledge_base', 'export_operation_metadata')

    class State(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        STATE_UNSPECIFIED: _ClassVar[KnowledgeOperationMetadata.State]
        PENDING: _ClassVar[KnowledgeOperationMetadata.State]
        RUNNING: _ClassVar[KnowledgeOperationMetadata.State]
        DONE: _ClassVar[KnowledgeOperationMetadata.State]
    STATE_UNSPECIFIED: KnowledgeOperationMetadata.State
    PENDING: KnowledgeOperationMetadata.State
    RUNNING: KnowledgeOperationMetadata.State
    DONE: KnowledgeOperationMetadata.State
    STATE_FIELD_NUMBER: _ClassVar[int]
    KNOWLEDGE_BASE_FIELD_NUMBER: _ClassVar[int]
    EXPORT_OPERATION_METADATA_FIELD_NUMBER: _ClassVar[int]
    state: KnowledgeOperationMetadata.State
    knowledge_base: str
    export_operation_metadata: ExportOperationMetadata

    def __init__(self, state: _Optional[_Union[KnowledgeOperationMetadata.State, str]]=..., knowledge_base: _Optional[str]=..., export_operation_metadata: _Optional[_Union[ExportOperationMetadata, _Mapping]]=...) -> None:
        ...

class ReloadDocumentRequest(_message.Message):
    __slots__ = ('name', 'gcs_source', 'import_gcs_custom_metadata')
    NAME_FIELD_NUMBER: _ClassVar[int]
    GCS_SOURCE_FIELD_NUMBER: _ClassVar[int]
    IMPORT_GCS_CUSTOM_METADATA_FIELD_NUMBER: _ClassVar[int]
    name: str
    gcs_source: _gcs_pb2.GcsSource
    import_gcs_custom_metadata: bool

    def __init__(self, name: _Optional[str]=..., gcs_source: _Optional[_Union[_gcs_pb2.GcsSource, _Mapping]]=..., import_gcs_custom_metadata: bool=...) -> None:
        ...