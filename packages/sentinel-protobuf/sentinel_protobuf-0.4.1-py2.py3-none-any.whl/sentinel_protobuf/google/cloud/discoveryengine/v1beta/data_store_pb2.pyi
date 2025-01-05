from google.api import field_behavior_pb2 as _field_behavior_pb2
from google.api import resource_pb2 as _resource_pb2
from google.cloud.discoveryengine.v1beta import common_pb2 as _common_pb2
from google.cloud.discoveryengine.v1beta import document_processing_config_pb2 as _document_processing_config_pb2
from google.cloud.discoveryengine.v1beta import schema_pb2 as _schema_pb2
from google.protobuf import timestamp_pb2 as _timestamp_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union
DESCRIPTOR: _descriptor.FileDescriptor

class DataStore(_message.Message):
    __slots__ = ('name', 'display_name', 'industry_vertical', 'solution_types', 'default_schema_id', 'content_config', 'create_time', 'language_info', 'natural_language_query_understanding_config', 'billing_estimation', 'workspace_config', 'document_processing_config', 'starting_schema', 'serving_config_data_store')

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

    class BillingEstimation(_message.Message):
        __slots__ = ('structured_data_size', 'unstructured_data_size', 'website_data_size', 'structured_data_update_time', 'unstructured_data_update_time', 'website_data_update_time')
        STRUCTURED_DATA_SIZE_FIELD_NUMBER: _ClassVar[int]
        UNSTRUCTURED_DATA_SIZE_FIELD_NUMBER: _ClassVar[int]
        WEBSITE_DATA_SIZE_FIELD_NUMBER: _ClassVar[int]
        STRUCTURED_DATA_UPDATE_TIME_FIELD_NUMBER: _ClassVar[int]
        UNSTRUCTURED_DATA_UPDATE_TIME_FIELD_NUMBER: _ClassVar[int]
        WEBSITE_DATA_UPDATE_TIME_FIELD_NUMBER: _ClassVar[int]
        structured_data_size: int
        unstructured_data_size: int
        website_data_size: int
        structured_data_update_time: _timestamp_pb2.Timestamp
        unstructured_data_update_time: _timestamp_pb2.Timestamp
        website_data_update_time: _timestamp_pb2.Timestamp

        def __init__(self, structured_data_size: _Optional[int]=..., unstructured_data_size: _Optional[int]=..., website_data_size: _Optional[int]=..., structured_data_update_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]]=..., unstructured_data_update_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]]=..., website_data_update_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]]=...) -> None:
            ...

    class ServingConfigDataStore(_message.Message):
        __slots__ = ('disabled_for_serving',)
        DISABLED_FOR_SERVING_FIELD_NUMBER: _ClassVar[int]
        disabled_for_serving: bool

        def __init__(self, disabled_for_serving: bool=...) -> None:
            ...
    NAME_FIELD_NUMBER: _ClassVar[int]
    DISPLAY_NAME_FIELD_NUMBER: _ClassVar[int]
    INDUSTRY_VERTICAL_FIELD_NUMBER: _ClassVar[int]
    SOLUTION_TYPES_FIELD_NUMBER: _ClassVar[int]
    DEFAULT_SCHEMA_ID_FIELD_NUMBER: _ClassVar[int]
    CONTENT_CONFIG_FIELD_NUMBER: _ClassVar[int]
    CREATE_TIME_FIELD_NUMBER: _ClassVar[int]
    LANGUAGE_INFO_FIELD_NUMBER: _ClassVar[int]
    NATURAL_LANGUAGE_QUERY_UNDERSTANDING_CONFIG_FIELD_NUMBER: _ClassVar[int]
    BILLING_ESTIMATION_FIELD_NUMBER: _ClassVar[int]
    WORKSPACE_CONFIG_FIELD_NUMBER: _ClassVar[int]
    DOCUMENT_PROCESSING_CONFIG_FIELD_NUMBER: _ClassVar[int]
    STARTING_SCHEMA_FIELD_NUMBER: _ClassVar[int]
    SERVING_CONFIG_DATA_STORE_FIELD_NUMBER: _ClassVar[int]
    name: str
    display_name: str
    industry_vertical: _common_pb2.IndustryVertical
    solution_types: _containers.RepeatedScalarFieldContainer[_common_pb2.SolutionType]
    default_schema_id: str
    content_config: DataStore.ContentConfig
    create_time: _timestamp_pb2.Timestamp
    language_info: LanguageInfo
    natural_language_query_understanding_config: NaturalLanguageQueryUnderstandingConfig
    billing_estimation: DataStore.BillingEstimation
    workspace_config: WorkspaceConfig
    document_processing_config: _document_processing_config_pb2.DocumentProcessingConfig
    starting_schema: _schema_pb2.Schema
    serving_config_data_store: DataStore.ServingConfigDataStore

    def __init__(self, name: _Optional[str]=..., display_name: _Optional[str]=..., industry_vertical: _Optional[_Union[_common_pb2.IndustryVertical, str]]=..., solution_types: _Optional[_Iterable[_Union[_common_pb2.SolutionType, str]]]=..., default_schema_id: _Optional[str]=..., content_config: _Optional[_Union[DataStore.ContentConfig, str]]=..., create_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]]=..., language_info: _Optional[_Union[LanguageInfo, _Mapping]]=..., natural_language_query_understanding_config: _Optional[_Union[NaturalLanguageQueryUnderstandingConfig, _Mapping]]=..., billing_estimation: _Optional[_Union[DataStore.BillingEstimation, _Mapping]]=..., workspace_config: _Optional[_Union[WorkspaceConfig, _Mapping]]=..., document_processing_config: _Optional[_Union[_document_processing_config_pb2.DocumentProcessingConfig, _Mapping]]=..., starting_schema: _Optional[_Union[_schema_pb2.Schema, _Mapping]]=..., serving_config_data_store: _Optional[_Union[DataStore.ServingConfigDataStore, _Mapping]]=...) -> None:
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

class NaturalLanguageQueryUnderstandingConfig(_message.Message):
    __slots__ = ('mode',)

    class Mode(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        MODE_UNSPECIFIED: _ClassVar[NaturalLanguageQueryUnderstandingConfig.Mode]
        DISABLED: _ClassVar[NaturalLanguageQueryUnderstandingConfig.Mode]
        ENABLED: _ClassVar[NaturalLanguageQueryUnderstandingConfig.Mode]
    MODE_UNSPECIFIED: NaturalLanguageQueryUnderstandingConfig.Mode
    DISABLED: NaturalLanguageQueryUnderstandingConfig.Mode
    ENABLED: NaturalLanguageQueryUnderstandingConfig.Mode
    MODE_FIELD_NUMBER: _ClassVar[int]
    mode: NaturalLanguageQueryUnderstandingConfig.Mode

    def __init__(self, mode: _Optional[_Union[NaturalLanguageQueryUnderstandingConfig.Mode, str]]=...) -> None:
        ...

class WorkspaceConfig(_message.Message):
    __slots__ = ('type', 'dasher_customer_id', 'super_admin_service_account', 'super_admin_email_address')

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
    SUPER_ADMIN_SERVICE_ACCOUNT_FIELD_NUMBER: _ClassVar[int]
    SUPER_ADMIN_EMAIL_ADDRESS_FIELD_NUMBER: _ClassVar[int]
    type: WorkspaceConfig.Type
    dasher_customer_id: str
    super_admin_service_account: str
    super_admin_email_address: str

    def __init__(self, type: _Optional[_Union[WorkspaceConfig.Type, str]]=..., dasher_customer_id: _Optional[str]=..., super_admin_service_account: _Optional[str]=..., super_admin_email_address: _Optional[str]=...) -> None:
        ...