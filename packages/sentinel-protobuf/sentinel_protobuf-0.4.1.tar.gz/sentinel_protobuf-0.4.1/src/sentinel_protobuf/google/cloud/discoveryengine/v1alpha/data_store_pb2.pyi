from google.api import field_behavior_pb2 as _field_behavior_pb2
from google.api import resource_pb2 as _resource_pb2
from google.cloud.discoveryengine.v1alpha import common_pb2 as _common_pb2
from google.cloud.discoveryengine.v1alpha import document_processing_config_pb2 as _document_processing_config_pb2
from google.cloud.discoveryengine.v1alpha import schema_pb2 as _schema_pb2
from google.protobuf import timestamp_pb2 as _timestamp_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union
DESCRIPTOR: _descriptor.FileDescriptor

class DataStore(_message.Message):
    __slots__ = ('name', 'display_name', 'industry_vertical', 'solution_types', 'default_schema_id', 'content_config', 'create_time', 'language_info', 'idp_config', 'acl_enabled', 'workspace_config', 'document_processing_config', 'starting_schema')

    class ContentConfig(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        CONTENT_CONFIG_UNSPECIFIED: _ClassVar[DataStore.ContentConfig]
        NO_CONTENT: _ClassVar[DataStore.ContentConfig]
        CONTENT_REQUIRED: _ClassVar[DataStore.ContentConfig]
        PUBLIC_WEBSITE: _ClassVar[DataStore.ContentConfig]
        GOOGLE_WORKSPACE: _ClassVar[DataStore.ContentConfig]
    CONTENT_CONFIG_UNSPECIFIED: DataStore.ContentConfig
    NO_CONTENT: DataStore.ContentConfig
    CONTENT_REQUIRED: DataStore.ContentConfig
    PUBLIC_WEBSITE: DataStore.ContentConfig
    GOOGLE_WORKSPACE: DataStore.ContentConfig
    NAME_FIELD_NUMBER: _ClassVar[int]
    DISPLAY_NAME_FIELD_NUMBER: _ClassVar[int]
    INDUSTRY_VERTICAL_FIELD_NUMBER: _ClassVar[int]
    SOLUTION_TYPES_FIELD_NUMBER: _ClassVar[int]
    DEFAULT_SCHEMA_ID_FIELD_NUMBER: _ClassVar[int]
    CONTENT_CONFIG_FIELD_NUMBER: _ClassVar[int]
    CREATE_TIME_FIELD_NUMBER: _ClassVar[int]
    LANGUAGE_INFO_FIELD_NUMBER: _ClassVar[int]
    IDP_CONFIG_FIELD_NUMBER: _ClassVar[int]
    ACL_ENABLED_FIELD_NUMBER: _ClassVar[int]
    WORKSPACE_CONFIG_FIELD_NUMBER: _ClassVar[int]
    DOCUMENT_PROCESSING_CONFIG_FIELD_NUMBER: _ClassVar[int]
    STARTING_SCHEMA_FIELD_NUMBER: _ClassVar[int]
    name: str
    display_name: str
    industry_vertical: _common_pb2.IndustryVertical
    solution_types: _containers.RepeatedScalarFieldContainer[_common_pb2.SolutionType]
    default_schema_id: str
    content_config: DataStore.ContentConfig
    create_time: _timestamp_pb2.Timestamp
    language_info: LanguageInfo
    idp_config: _common_pb2.IdpConfig
    acl_enabled: bool
    workspace_config: WorkspaceConfig
    document_processing_config: _document_processing_config_pb2.DocumentProcessingConfig
    starting_schema: _schema_pb2.Schema

    def __init__(self, name: _Optional[str]=..., display_name: _Optional[str]=..., industry_vertical: _Optional[_Union[_common_pb2.IndustryVertical, str]]=..., solution_types: _Optional[_Iterable[_Union[_common_pb2.SolutionType, str]]]=..., default_schema_id: _Optional[str]=..., content_config: _Optional[_Union[DataStore.ContentConfig, str]]=..., create_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]]=..., language_info: _Optional[_Union[LanguageInfo, _Mapping]]=..., idp_config: _Optional[_Union[_common_pb2.IdpConfig, _Mapping]]=..., acl_enabled: bool=..., workspace_config: _Optional[_Union[WorkspaceConfig, _Mapping]]=..., document_processing_config: _Optional[_Union[_document_processing_config_pb2.DocumentProcessingConfig, _Mapping]]=..., starting_schema: _Optional[_Union[_schema_pb2.Schema, _Mapping]]=...) -> None:
        ...

class LanguageInfo(_message.Message):
    __slots__ = ('language_code', 'normalized_language_code', 'language', 'region')
    LANGUAGE_CODE_FIELD_NUMBER: _ClassVar[int]
    NORMALIZED_LANGUAGE_CODE_FIELD_NUMBER: _ClassVar[int]
    LANGUAGE_FIELD_NUMBER: _ClassVar[int]
    REGION_FIELD_NUMBER: _ClassVar[int]
    language_code: str
    normalized_language_code: str
    language: str
    region: str

    def __init__(self, language_code: _Optional[str]=..., normalized_language_code: _Optional[str]=..., language: _Optional[str]=..., region: _Optional[str]=...) -> None:
        ...

class WorkspaceConfig(_message.Message):
    __slots__ = ('type', 'dasher_customer_id')

    class Type(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        TYPE_UNSPECIFIED: _ClassVar[WorkspaceConfig.Type]
        GOOGLE_DRIVE: _ClassVar[WorkspaceConfig.Type]
        GOOGLE_MAIL: _ClassVar[WorkspaceConfig.Type]
        GOOGLE_SITES: _ClassVar[WorkspaceConfig.Type]
        GOOGLE_CALENDAR: _ClassVar[WorkspaceConfig.Type]
        GOOGLE_CHAT: _ClassVar[WorkspaceConfig.Type]
        GOOGLE_GROUPS: _ClassVar[WorkspaceConfig.Type]
        GOOGLE_KEEP: _ClassVar[WorkspaceConfig.Type]
    TYPE_UNSPECIFIED: WorkspaceConfig.Type
    GOOGLE_DRIVE: WorkspaceConfig.Type
    GOOGLE_MAIL: WorkspaceConfig.Type
    GOOGLE_SITES: WorkspaceConfig.Type
    GOOGLE_CALENDAR: WorkspaceConfig.Type
    GOOGLE_CHAT: WorkspaceConfig.Type
    GOOGLE_GROUPS: WorkspaceConfig.Type
    GOOGLE_KEEP: WorkspaceConfig.Type
    TYPE_FIELD_NUMBER: _ClassVar[int]
    DASHER_CUSTOMER_ID_FIELD_NUMBER: _ClassVar[int]
    type: WorkspaceConfig.Type
    dasher_customer_id: str

    def __init__(self, type: _Optional[_Union[WorkspaceConfig.Type, str]]=..., dasher_customer_id: _Optional[str]=...) -> None:
        ...