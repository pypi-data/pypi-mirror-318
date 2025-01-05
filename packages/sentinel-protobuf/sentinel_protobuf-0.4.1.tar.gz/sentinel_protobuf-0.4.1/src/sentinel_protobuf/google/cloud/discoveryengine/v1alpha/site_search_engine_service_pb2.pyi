from google.api import annotations_pb2 as _annotations_pb2
from google.api import client_pb2 as _client_pb2
from google.api import field_behavior_pb2 as _field_behavior_pb2
from google.api import resource_pb2 as _resource_pb2
from google.cloud.discoveryengine.v1alpha import site_search_engine_pb2 as _site_search_engine_pb2
from google.longrunning import operations_pb2 as _operations_pb2
from google.protobuf import empty_pb2 as _empty_pb2
from google.protobuf import struct_pb2 as _struct_pb2
from google.protobuf import timestamp_pb2 as _timestamp_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union
DESCRIPTOR: _descriptor.FileDescriptor

class GetSiteSearchEngineRequest(_message.Message):
    __slots__ = ('name',)
    NAME_FIELD_NUMBER: _ClassVar[int]
    name: str

    def __init__(self, name: _Optional[str]=...) -> None:
        ...

class CreateTargetSiteRequest(_message.Message):
    __slots__ = ('parent', 'target_site')
    PARENT_FIELD_NUMBER: _ClassVar[int]
    TARGET_SITE_FIELD_NUMBER: _ClassVar[int]
    parent: str
    target_site: _site_search_engine_pb2.TargetSite

    def __init__(self, parent: _Optional[str]=..., target_site: _Optional[_Union[_site_search_engine_pb2.TargetSite, _Mapping]]=...) -> None:
        ...

class CreateTargetSiteMetadata(_message.Message):
    __slots__ = ('create_time', 'update_time')
    CREATE_TIME_FIELD_NUMBER: _ClassVar[int]
    UPDATE_TIME_FIELD_NUMBER: _ClassVar[int]
    create_time: _timestamp_pb2.Timestamp
    update_time: _timestamp_pb2.Timestamp

    def __init__(self, create_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]]=..., update_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]]=...) -> None:
        ...

class BatchCreateTargetSitesRequest(_message.Message):
    __slots__ = ('parent', 'requests')
    PARENT_FIELD_NUMBER: _ClassVar[int]
    REQUESTS_FIELD_NUMBER: _ClassVar[int]
    parent: str
    requests: _containers.RepeatedCompositeFieldContainer[CreateTargetSiteRequest]

    def __init__(self, parent: _Optional[str]=..., requests: _Optional[_Iterable[_Union[CreateTargetSiteRequest, _Mapping]]]=...) -> None:
        ...

class GetTargetSiteRequest(_message.Message):
    __slots__ = ('name',)
    NAME_FIELD_NUMBER: _ClassVar[int]
    name: str

    def __init__(self, name: _Optional[str]=...) -> None:
        ...

class UpdateTargetSiteRequest(_message.Message):
    __slots__ = ('target_site',)
    TARGET_SITE_FIELD_NUMBER: _ClassVar[int]
    target_site: _site_search_engine_pb2.TargetSite

    def __init__(self, target_site: _Optional[_Union[_site_search_engine_pb2.TargetSite, _Mapping]]=...) -> None:
        ...

class UpdateTargetSiteMetadata(_message.Message):
    __slots__ = ('create_time', 'update_time')
    CREATE_TIME_FIELD_NUMBER: _ClassVar[int]
    UPDATE_TIME_FIELD_NUMBER: _ClassVar[int]
    create_time: _timestamp_pb2.Timestamp
    update_time: _timestamp_pb2.Timestamp

    def __init__(self, create_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]]=..., update_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]]=...) -> None:
        ...

class DeleteTargetSiteRequest(_message.Message):
    __slots__ = ('name',)
    NAME_FIELD_NUMBER: _ClassVar[int]
    name: str

    def __init__(self, name: _Optional[str]=...) -> None:
        ...

class DeleteTargetSiteMetadata(_message.Message):
    __slots__ = ('create_time', 'update_time')
    CREATE_TIME_FIELD_NUMBER: _ClassVar[int]
    UPDATE_TIME_FIELD_NUMBER: _ClassVar[int]
    create_time: _timestamp_pb2.Timestamp
    update_time: _timestamp_pb2.Timestamp

    def __init__(self, create_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]]=..., update_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]]=...) -> None:
        ...

class ListTargetSitesRequest(_message.Message):
    __slots__ = ('parent', 'page_size', 'page_token')
    PARENT_FIELD_NUMBER: _ClassVar[int]
    PAGE_SIZE_FIELD_NUMBER: _ClassVar[int]
    PAGE_TOKEN_FIELD_NUMBER: _ClassVar[int]
    parent: str
    page_size: int
    page_token: str

    def __init__(self, parent: _Optional[str]=..., page_size: _Optional[int]=..., page_token: _Optional[str]=...) -> None:
        ...

class ListTargetSitesResponse(_message.Message):
    __slots__ = ('target_sites', 'next_page_token', 'total_size')
    TARGET_SITES_FIELD_NUMBER: _ClassVar[int]
    NEXT_PAGE_TOKEN_FIELD_NUMBER: _ClassVar[int]
    TOTAL_SIZE_FIELD_NUMBER: _ClassVar[int]
    target_sites: _containers.RepeatedCompositeFieldContainer[_site_search_engine_pb2.TargetSite]
    next_page_token: str
    total_size: int

    def __init__(self, target_sites: _Optional[_Iterable[_Union[_site_search_engine_pb2.TargetSite, _Mapping]]]=..., next_page_token: _Optional[str]=..., total_size: _Optional[int]=...) -> None:
        ...

class BatchCreateTargetSiteMetadata(_message.Message):
    __slots__ = ('create_time', 'update_time')
    CREATE_TIME_FIELD_NUMBER: _ClassVar[int]
    UPDATE_TIME_FIELD_NUMBER: _ClassVar[int]
    create_time: _timestamp_pb2.Timestamp
    update_time: _timestamp_pb2.Timestamp

    def __init__(self, create_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]]=..., update_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]]=...) -> None:
        ...

class BatchCreateTargetSitesResponse(_message.Message):
    __slots__ = ('target_sites',)
    TARGET_SITES_FIELD_NUMBER: _ClassVar[int]
    target_sites: _containers.RepeatedCompositeFieldContainer[_site_search_engine_pb2.TargetSite]

    def __init__(self, target_sites: _Optional[_Iterable[_Union[_site_search_engine_pb2.TargetSite, _Mapping]]]=...) -> None:
        ...

class EnableAdvancedSiteSearchRequest(_message.Message):
    __slots__ = ('site_search_engine',)
    SITE_SEARCH_ENGINE_FIELD_NUMBER: _ClassVar[int]
    site_search_engine: str

    def __init__(self, site_search_engine: _Optional[str]=...) -> None:
        ...

class EnableAdvancedSiteSearchResponse(_message.Message):
    __slots__ = ()

    def __init__(self) -> None:
        ...

class EnableAdvancedSiteSearchMetadata(_message.Message):
    __slots__ = ('create_time', 'update_time')
    CREATE_TIME_FIELD_NUMBER: _ClassVar[int]
    UPDATE_TIME_FIELD_NUMBER: _ClassVar[int]
    create_time: _timestamp_pb2.Timestamp
    update_time: _timestamp_pb2.Timestamp

    def __init__(self, create_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]]=..., update_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]]=...) -> None:
        ...

class DisableAdvancedSiteSearchRequest(_message.Message):
    __slots__ = ('site_search_engine',)
    SITE_SEARCH_ENGINE_FIELD_NUMBER: _ClassVar[int]
    site_search_engine: str

    def __init__(self, site_search_engine: _Optional[str]=...) -> None:
        ...

class DisableAdvancedSiteSearchResponse(_message.Message):
    __slots__ = ()

    def __init__(self) -> None:
        ...

class DisableAdvancedSiteSearchMetadata(_message.Message):
    __slots__ = ('create_time', 'update_time')
    CREATE_TIME_FIELD_NUMBER: _ClassVar[int]
    UPDATE_TIME_FIELD_NUMBER: _ClassVar[int]
    create_time: _timestamp_pb2.Timestamp
    update_time: _timestamp_pb2.Timestamp

    def __init__(self, create_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]]=..., update_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]]=...) -> None:
        ...

class RecrawlUrisRequest(_message.Message):
    __slots__ = ('site_search_engine', 'uris')
    SITE_SEARCH_ENGINE_FIELD_NUMBER: _ClassVar[int]
    URIS_FIELD_NUMBER: _ClassVar[int]
    site_search_engine: str
    uris: _containers.RepeatedScalarFieldContainer[str]

    def __init__(self, site_search_engine: _Optional[str]=..., uris: _Optional[_Iterable[str]]=...) -> None:
        ...

class RecrawlUrisResponse(_message.Message):
    __slots__ = ('failure_samples', 'failed_uris')

    class FailureInfo(_message.Message):
        __slots__ = ('uri', 'failure_reasons')

        class FailureReason(_message.Message):
            __slots__ = ('corpus_type', 'error_message')

            class CorpusType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
                __slots__ = ()
                CORPUS_TYPE_UNSPECIFIED: _ClassVar[RecrawlUrisResponse.FailureInfo.FailureReason.CorpusType]
                DESKTOP: _ClassVar[RecrawlUrisResponse.FailureInfo.FailureReason.CorpusType]
                MOBILE: _ClassVar[RecrawlUrisResponse.FailureInfo.FailureReason.CorpusType]
            CORPUS_TYPE_UNSPECIFIED: RecrawlUrisResponse.FailureInfo.FailureReason.CorpusType
            DESKTOP: RecrawlUrisResponse.FailureInfo.FailureReason.CorpusType
            MOBILE: RecrawlUrisResponse.FailureInfo.FailureReason.CorpusType
            CORPUS_TYPE_FIELD_NUMBER: _ClassVar[int]
            ERROR_MESSAGE_FIELD_NUMBER: _ClassVar[int]
            corpus_type: RecrawlUrisResponse.FailureInfo.FailureReason.CorpusType
            error_message: str

            def __init__(self, corpus_type: _Optional[_Union[RecrawlUrisResponse.FailureInfo.FailureReason.CorpusType, str]]=..., error_message: _Optional[str]=...) -> None:
                ...
        URI_FIELD_NUMBER: _ClassVar[int]
        FAILURE_REASONS_FIELD_NUMBER: _ClassVar[int]
        uri: str
        failure_reasons: _containers.RepeatedCompositeFieldContainer[RecrawlUrisResponse.FailureInfo.FailureReason]

        def __init__(self, uri: _Optional[str]=..., failure_reasons: _Optional[_Iterable[_Union[RecrawlUrisResponse.FailureInfo.FailureReason, _Mapping]]]=...) -> None:
            ...
    FAILURE_SAMPLES_FIELD_NUMBER: _ClassVar[int]
    FAILED_URIS_FIELD_NUMBER: _ClassVar[int]
    failure_samples: _containers.RepeatedCompositeFieldContainer[RecrawlUrisResponse.FailureInfo]
    failed_uris: _containers.RepeatedScalarFieldContainer[str]

    def __init__(self, failure_samples: _Optional[_Iterable[_Union[RecrawlUrisResponse.FailureInfo, _Mapping]]]=..., failed_uris: _Optional[_Iterable[str]]=...) -> None:
        ...

class RecrawlUrisMetadata(_message.Message):
    __slots__ = ('create_time', 'update_time', 'invalid_uris', 'valid_uris_count', 'success_count', 'pending_count', 'quota_exceeded_count')
    CREATE_TIME_FIELD_NUMBER: _ClassVar[int]
    UPDATE_TIME_FIELD_NUMBER: _ClassVar[int]
    INVALID_URIS_FIELD_NUMBER: _ClassVar[int]
    VALID_URIS_COUNT_FIELD_NUMBER: _ClassVar[int]
    SUCCESS_COUNT_FIELD_NUMBER: _ClassVar[int]
    PENDING_COUNT_FIELD_NUMBER: _ClassVar[int]
    QUOTA_EXCEEDED_COUNT_FIELD_NUMBER: _ClassVar[int]
    create_time: _timestamp_pb2.Timestamp
    update_time: _timestamp_pb2.Timestamp
    invalid_uris: _containers.RepeatedScalarFieldContainer[str]
    valid_uris_count: int
    success_count: int
    pending_count: int
    quota_exceeded_count: int

    def __init__(self, create_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]]=..., update_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]]=..., invalid_uris: _Optional[_Iterable[str]]=..., valid_uris_count: _Optional[int]=..., success_count: _Optional[int]=..., pending_count: _Optional[int]=..., quota_exceeded_count: _Optional[int]=...) -> None:
        ...

class BatchVerifyTargetSitesRequest(_message.Message):
    __slots__ = ('parent',)
    PARENT_FIELD_NUMBER: _ClassVar[int]
    parent: str

    def __init__(self, parent: _Optional[str]=...) -> None:
        ...

class BatchVerifyTargetSitesResponse(_message.Message):
    __slots__ = ()

    def __init__(self) -> None:
        ...

class BatchVerifyTargetSitesMetadata(_message.Message):
    __slots__ = ('create_time', 'update_time')
    CREATE_TIME_FIELD_NUMBER: _ClassVar[int]
    UPDATE_TIME_FIELD_NUMBER: _ClassVar[int]
    create_time: _timestamp_pb2.Timestamp
    update_time: _timestamp_pb2.Timestamp

    def __init__(self, create_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]]=..., update_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]]=...) -> None:
        ...

class FetchDomainVerificationStatusRequest(_message.Message):
    __slots__ = ('site_search_engine', 'page_size', 'page_token')
    SITE_SEARCH_ENGINE_FIELD_NUMBER: _ClassVar[int]
    PAGE_SIZE_FIELD_NUMBER: _ClassVar[int]
    PAGE_TOKEN_FIELD_NUMBER: _ClassVar[int]
    site_search_engine: str
    page_size: int
    page_token: str

    def __init__(self, site_search_engine: _Optional[str]=..., page_size: _Optional[int]=..., page_token: _Optional[str]=...) -> None:
        ...

class FetchDomainVerificationStatusResponse(_message.Message):
    __slots__ = ('target_sites', 'next_page_token', 'total_size')
    TARGET_SITES_FIELD_NUMBER: _ClassVar[int]
    NEXT_PAGE_TOKEN_FIELD_NUMBER: _ClassVar[int]
    TOTAL_SIZE_FIELD_NUMBER: _ClassVar[int]
    target_sites: _containers.RepeatedCompositeFieldContainer[_site_search_engine_pb2.TargetSite]
    next_page_token: str
    total_size: int

    def __init__(self, target_sites: _Optional[_Iterable[_Union[_site_search_engine_pb2.TargetSite, _Mapping]]]=..., next_page_token: _Optional[str]=..., total_size: _Optional[int]=...) -> None:
        ...

class SetUriPatternDocumentDataRequest(_message.Message):
    __slots__ = ('site_search_engine', 'document_data_map', 'empty_document_data_map', 'schema')

    class DocumentDataMapEntry(_message.Message):
        __slots__ = ('key', 'value')
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: _struct_pb2.Struct

        def __init__(self, key: _Optional[str]=..., value: _Optional[_Union[_struct_pb2.Struct, _Mapping]]=...) -> None:
            ...
    SITE_SEARCH_ENGINE_FIELD_NUMBER: _ClassVar[int]
    DOCUMENT_DATA_MAP_FIELD_NUMBER: _ClassVar[int]
    EMPTY_DOCUMENT_DATA_MAP_FIELD_NUMBER: _ClassVar[int]
    SCHEMA_FIELD_NUMBER: _ClassVar[int]
    site_search_engine: str
    document_data_map: _containers.MessageMap[str, _struct_pb2.Struct]
    empty_document_data_map: bool
    schema: _struct_pb2.Struct

    def __init__(self, site_search_engine: _Optional[str]=..., document_data_map: _Optional[_Mapping[str, _struct_pb2.Struct]]=..., empty_document_data_map: bool=..., schema: _Optional[_Union[_struct_pb2.Struct, _Mapping]]=...) -> None:
        ...

class SetUriPatternDocumentDataResponse(_message.Message):
    __slots__ = ()

    def __init__(self) -> None:
        ...

class SetUriPatternDocumentDataMetadata(_message.Message):
    __slots__ = ('create_time', 'update_time')
    CREATE_TIME_FIELD_NUMBER: _ClassVar[int]
    UPDATE_TIME_FIELD_NUMBER: _ClassVar[int]
    create_time: _timestamp_pb2.Timestamp
    update_time: _timestamp_pb2.Timestamp

    def __init__(self, create_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]]=..., update_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]]=...) -> None:
        ...

class GetUriPatternDocumentDataRequest(_message.Message):
    __slots__ = ('site_search_engine',)
    SITE_SEARCH_ENGINE_FIELD_NUMBER: _ClassVar[int]
    site_search_engine: str

    def __init__(self, site_search_engine: _Optional[str]=...) -> None:
        ...

class GetUriPatternDocumentDataResponse(_message.Message):
    __slots__ = ('document_data_map',)

    class DocumentDataMapEntry(_message.Message):
        __slots__ = ('key', 'value')
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: _struct_pb2.Struct

        def __init__(self, key: _Optional[str]=..., value: _Optional[_Union[_struct_pb2.Struct, _Mapping]]=...) -> None:
            ...
    DOCUMENT_DATA_MAP_FIELD_NUMBER: _ClassVar[int]
    document_data_map: _containers.MessageMap[str, _struct_pb2.Struct]

    def __init__(self, document_data_map: _Optional[_Mapping[str, _struct_pb2.Struct]]=...) -> None:
        ...