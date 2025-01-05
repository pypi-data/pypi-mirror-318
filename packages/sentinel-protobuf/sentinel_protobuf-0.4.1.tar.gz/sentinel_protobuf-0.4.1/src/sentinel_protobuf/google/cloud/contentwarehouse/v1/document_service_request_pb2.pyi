from google.api import field_behavior_pb2 as _field_behavior_pb2
from google.api import resource_pb2 as _resource_pb2
from google.cloud.contentwarehouse.v1 import common_pb2 as _common_pb2
from google.cloud.contentwarehouse.v1 import document_pb2 as _document_pb2
from google.cloud.contentwarehouse.v1 import filters_pb2 as _filters_pb2
from google.cloud.contentwarehouse.v1 import histogram_pb2 as _histogram_pb2
from google.iam.v1 import policy_pb2 as _policy_pb2
from google.protobuf import field_mask_pb2 as _field_mask_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class CloudAIDocumentOption(_message.Message):
    __slots__ = ("enable_entities_conversions", "customized_entities_properties_conversions")
    class CustomizedEntitiesPropertiesConversionsEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: str
        def __init__(self, key: _Optional[str] = ..., value: _Optional[str] = ...) -> None: ...
    ENABLE_ENTITIES_CONVERSIONS_FIELD_NUMBER: _ClassVar[int]
    CUSTOMIZED_ENTITIES_PROPERTIES_CONVERSIONS_FIELD_NUMBER: _ClassVar[int]
    enable_entities_conversions: bool
    customized_entities_properties_conversions: _containers.ScalarMap[str, str]
    def __init__(self, enable_entities_conversions: bool = ..., customized_entities_properties_conversions: _Optional[_Mapping[str, str]] = ...) -> None: ...

class CreateDocumentRequest(_message.Message):
    __slots__ = ("parent", "document", "request_metadata", "policy", "cloud_ai_document_option", "create_mask")
    PARENT_FIELD_NUMBER: _ClassVar[int]
    DOCUMENT_FIELD_NUMBER: _ClassVar[int]
    REQUEST_METADATA_FIELD_NUMBER: _ClassVar[int]
    POLICY_FIELD_NUMBER: _ClassVar[int]
    CLOUD_AI_DOCUMENT_OPTION_FIELD_NUMBER: _ClassVar[int]
    CREATE_MASK_FIELD_NUMBER: _ClassVar[int]
    parent: str
    document: _document_pb2.Document
    request_metadata: _common_pb2.RequestMetadata
    policy: _policy_pb2.Policy
    cloud_ai_document_option: CloudAIDocumentOption
    create_mask: _field_mask_pb2.FieldMask
    def __init__(self, parent: _Optional[str] = ..., document: _Optional[_Union[_document_pb2.Document, _Mapping]] = ..., request_metadata: _Optional[_Union[_common_pb2.RequestMetadata, _Mapping]] = ..., policy: _Optional[_Union[_policy_pb2.Policy, _Mapping]] = ..., cloud_ai_document_option: _Optional[_Union[CloudAIDocumentOption, _Mapping]] = ..., create_mask: _Optional[_Union[_field_mask_pb2.FieldMask, _Mapping]] = ...) -> None: ...

class GetDocumentRequest(_message.Message):
    __slots__ = ("name", "request_metadata")
    NAME_FIELD_NUMBER: _ClassVar[int]
    REQUEST_METADATA_FIELD_NUMBER: _ClassVar[int]
    name: str
    request_metadata: _common_pb2.RequestMetadata
    def __init__(self, name: _Optional[str] = ..., request_metadata: _Optional[_Union[_common_pb2.RequestMetadata, _Mapping]] = ...) -> None: ...

class UpdateDocumentRequest(_message.Message):
    __slots__ = ("name", "document", "request_metadata", "cloud_ai_document_option", "update_options")
    NAME_FIELD_NUMBER: _ClassVar[int]
    DOCUMENT_FIELD_NUMBER: _ClassVar[int]
    REQUEST_METADATA_FIELD_NUMBER: _ClassVar[int]
    CLOUD_AI_DOCUMENT_OPTION_FIELD_NUMBER: _ClassVar[int]
    UPDATE_OPTIONS_FIELD_NUMBER: _ClassVar[int]
    name: str
    document: _document_pb2.Document
    request_metadata: _common_pb2.RequestMetadata
    cloud_ai_document_option: CloudAIDocumentOption
    update_options: _common_pb2.UpdateOptions
    def __init__(self, name: _Optional[str] = ..., document: _Optional[_Union[_document_pb2.Document, _Mapping]] = ..., request_metadata: _Optional[_Union[_common_pb2.RequestMetadata, _Mapping]] = ..., cloud_ai_document_option: _Optional[_Union[CloudAIDocumentOption, _Mapping]] = ..., update_options: _Optional[_Union[_common_pb2.UpdateOptions, _Mapping]] = ...) -> None: ...

class DeleteDocumentRequest(_message.Message):
    __slots__ = ("name", "request_metadata")
    NAME_FIELD_NUMBER: _ClassVar[int]
    REQUEST_METADATA_FIELD_NUMBER: _ClassVar[int]
    name: str
    request_metadata: _common_pb2.RequestMetadata
    def __init__(self, name: _Optional[str] = ..., request_metadata: _Optional[_Union[_common_pb2.RequestMetadata, _Mapping]] = ...) -> None: ...

class SearchDocumentsRequest(_message.Message):
    __slots__ = ("parent", "request_metadata", "document_query", "offset", "page_size", "page_token", "order_by", "histogram_queries", "require_total_size", "total_result_size", "qa_size_limit")
    class TotalResultSize(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        TOTAL_RESULT_SIZE_UNSPECIFIED: _ClassVar[SearchDocumentsRequest.TotalResultSize]
        ESTIMATED_SIZE: _ClassVar[SearchDocumentsRequest.TotalResultSize]
        ACTUAL_SIZE: _ClassVar[SearchDocumentsRequest.TotalResultSize]
    TOTAL_RESULT_SIZE_UNSPECIFIED: SearchDocumentsRequest.TotalResultSize
    ESTIMATED_SIZE: SearchDocumentsRequest.TotalResultSize
    ACTUAL_SIZE: SearchDocumentsRequest.TotalResultSize
    PARENT_FIELD_NUMBER: _ClassVar[int]
    REQUEST_METADATA_FIELD_NUMBER: _ClassVar[int]
    DOCUMENT_QUERY_FIELD_NUMBER: _ClassVar[int]
    OFFSET_FIELD_NUMBER: _ClassVar[int]
    PAGE_SIZE_FIELD_NUMBER: _ClassVar[int]
    PAGE_TOKEN_FIELD_NUMBER: _ClassVar[int]
    ORDER_BY_FIELD_NUMBER: _ClassVar[int]
    HISTOGRAM_QUERIES_FIELD_NUMBER: _ClassVar[int]
    REQUIRE_TOTAL_SIZE_FIELD_NUMBER: _ClassVar[int]
    TOTAL_RESULT_SIZE_FIELD_NUMBER: _ClassVar[int]
    QA_SIZE_LIMIT_FIELD_NUMBER: _ClassVar[int]
    parent: str
    request_metadata: _common_pb2.RequestMetadata
    document_query: _filters_pb2.DocumentQuery
    offset: int
    page_size: int
    page_token: str
    order_by: str
    histogram_queries: _containers.RepeatedCompositeFieldContainer[_histogram_pb2.HistogramQuery]
    require_total_size: bool
    total_result_size: SearchDocumentsRequest.TotalResultSize
    qa_size_limit: int
    def __init__(self, parent: _Optional[str] = ..., request_metadata: _Optional[_Union[_common_pb2.RequestMetadata, _Mapping]] = ..., document_query: _Optional[_Union[_filters_pb2.DocumentQuery, _Mapping]] = ..., offset: _Optional[int] = ..., page_size: _Optional[int] = ..., page_token: _Optional[str] = ..., order_by: _Optional[str] = ..., histogram_queries: _Optional[_Iterable[_Union[_histogram_pb2.HistogramQuery, _Mapping]]] = ..., require_total_size: bool = ..., total_result_size: _Optional[_Union[SearchDocumentsRequest.TotalResultSize, str]] = ..., qa_size_limit: _Optional[int] = ...) -> None: ...

class LockDocumentRequest(_message.Message):
    __slots__ = ("name", "collection_id", "locking_user")
    NAME_FIELD_NUMBER: _ClassVar[int]
    COLLECTION_ID_FIELD_NUMBER: _ClassVar[int]
    LOCKING_USER_FIELD_NUMBER: _ClassVar[int]
    name: str
    collection_id: str
    locking_user: _common_pb2.UserInfo
    def __init__(self, name: _Optional[str] = ..., collection_id: _Optional[str] = ..., locking_user: _Optional[_Union[_common_pb2.UserInfo, _Mapping]] = ...) -> None: ...

class FetchAclRequest(_message.Message):
    __slots__ = ("resource", "request_metadata", "project_owner")
    RESOURCE_FIELD_NUMBER: _ClassVar[int]
    REQUEST_METADATA_FIELD_NUMBER: _ClassVar[int]
    PROJECT_OWNER_FIELD_NUMBER: _ClassVar[int]
    resource: str
    request_metadata: _common_pb2.RequestMetadata
    project_owner: bool
    def __init__(self, resource: _Optional[str] = ..., request_metadata: _Optional[_Union[_common_pb2.RequestMetadata, _Mapping]] = ..., project_owner: bool = ...) -> None: ...

class SetAclRequest(_message.Message):
    __slots__ = ("resource", "policy", "request_metadata", "project_owner")
    RESOURCE_FIELD_NUMBER: _ClassVar[int]
    POLICY_FIELD_NUMBER: _ClassVar[int]
    REQUEST_METADATA_FIELD_NUMBER: _ClassVar[int]
    PROJECT_OWNER_FIELD_NUMBER: _ClassVar[int]
    resource: str
    policy: _policy_pb2.Policy
    request_metadata: _common_pb2.RequestMetadata
    project_owner: bool
    def __init__(self, resource: _Optional[str] = ..., policy: _Optional[_Union[_policy_pb2.Policy, _Mapping]] = ..., request_metadata: _Optional[_Union[_common_pb2.RequestMetadata, _Mapping]] = ..., project_owner: bool = ...) -> None: ...
