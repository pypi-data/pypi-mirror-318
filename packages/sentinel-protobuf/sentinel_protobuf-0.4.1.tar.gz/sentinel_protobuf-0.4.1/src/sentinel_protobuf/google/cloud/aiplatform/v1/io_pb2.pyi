from google.api import field_behavior_pb2 as _field_behavior_pb2
from google.cloud.aiplatform.v1 import api_auth_pb2 as _api_auth_pb2
from google.protobuf import timestamp_pb2 as _timestamp_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union
DESCRIPTOR: _descriptor.FileDescriptor

class AvroSource(_message.Message):
    __slots__ = ('gcs_source',)
    GCS_SOURCE_FIELD_NUMBER: _ClassVar[int]
    gcs_source: GcsSource

    def __init__(self, gcs_source: _Optional[_Union[GcsSource, _Mapping]]=...) -> None:
        ...

class CsvSource(_message.Message):
    __slots__ = ('gcs_source',)
    GCS_SOURCE_FIELD_NUMBER: _ClassVar[int]
    gcs_source: GcsSource

    def __init__(self, gcs_source: _Optional[_Union[GcsSource, _Mapping]]=...) -> None:
        ...

class GcsSource(_message.Message):
    __slots__ = ('uris',)
    URIS_FIELD_NUMBER: _ClassVar[int]
    uris: _containers.RepeatedScalarFieldContainer[str]

    def __init__(self, uris: _Optional[_Iterable[str]]=...) -> None:
        ...

class GcsDestination(_message.Message):
    __slots__ = ('output_uri_prefix',)
    OUTPUT_URI_PREFIX_FIELD_NUMBER: _ClassVar[int]
    output_uri_prefix: str

    def __init__(self, output_uri_prefix: _Optional[str]=...) -> None:
        ...

class BigQuerySource(_message.Message):
    __slots__ = ('input_uri',)
    INPUT_URI_FIELD_NUMBER: _ClassVar[int]
    input_uri: str

    def __init__(self, input_uri: _Optional[str]=...) -> None:
        ...

class BigQueryDestination(_message.Message):
    __slots__ = ('output_uri',)
    OUTPUT_URI_FIELD_NUMBER: _ClassVar[int]
    output_uri: str

    def __init__(self, output_uri: _Optional[str]=...) -> None:
        ...

class CsvDestination(_message.Message):
    __slots__ = ('gcs_destination',)
    GCS_DESTINATION_FIELD_NUMBER: _ClassVar[int]
    gcs_destination: GcsDestination

    def __init__(self, gcs_destination: _Optional[_Union[GcsDestination, _Mapping]]=...) -> None:
        ...

class TFRecordDestination(_message.Message):
    __slots__ = ('gcs_destination',)
    GCS_DESTINATION_FIELD_NUMBER: _ClassVar[int]
    gcs_destination: GcsDestination

    def __init__(self, gcs_destination: _Optional[_Union[GcsDestination, _Mapping]]=...) -> None:
        ...

class ContainerRegistryDestination(_message.Message):
    __slots__ = ('output_uri',)
    OUTPUT_URI_FIELD_NUMBER: _ClassVar[int]
    output_uri: str

    def __init__(self, output_uri: _Optional[str]=...) -> None:
        ...

class GoogleDriveSource(_message.Message):
    __slots__ = ('resource_ids',)

    class ResourceId(_message.Message):
        __slots__ = ('resource_type', 'resource_id')

        class ResourceType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
            __slots__ = ()
            RESOURCE_TYPE_UNSPECIFIED: _ClassVar[GoogleDriveSource.ResourceId.ResourceType]
            RESOURCE_TYPE_FILE: _ClassVar[GoogleDriveSource.ResourceId.ResourceType]
            RESOURCE_TYPE_FOLDER: _ClassVar[GoogleDriveSource.ResourceId.ResourceType]
        RESOURCE_TYPE_UNSPECIFIED: GoogleDriveSource.ResourceId.ResourceType
        RESOURCE_TYPE_FILE: GoogleDriveSource.ResourceId.ResourceType
        RESOURCE_TYPE_FOLDER: GoogleDriveSource.ResourceId.ResourceType
        RESOURCE_TYPE_FIELD_NUMBER: _ClassVar[int]
        RESOURCE_ID_FIELD_NUMBER: _ClassVar[int]
        resource_type: GoogleDriveSource.ResourceId.ResourceType
        resource_id: str

        def __init__(self, resource_type: _Optional[_Union[GoogleDriveSource.ResourceId.ResourceType, str]]=..., resource_id: _Optional[str]=...) -> None:
            ...
    RESOURCE_IDS_FIELD_NUMBER: _ClassVar[int]
    resource_ids: _containers.RepeatedCompositeFieldContainer[GoogleDriveSource.ResourceId]

    def __init__(self, resource_ids: _Optional[_Iterable[_Union[GoogleDriveSource.ResourceId, _Mapping]]]=...) -> None:
        ...

class DirectUploadSource(_message.Message):
    __slots__ = ()

    def __init__(self) -> None:
        ...

class SlackSource(_message.Message):
    __slots__ = ('channels',)

    class SlackChannels(_message.Message):
        __slots__ = ('channels', 'api_key_config')

        class SlackChannel(_message.Message):
            __slots__ = ('channel_id', 'start_time', 'end_time')
            CHANNEL_ID_FIELD_NUMBER: _ClassVar[int]
            START_TIME_FIELD_NUMBER: _ClassVar[int]
            END_TIME_FIELD_NUMBER: _ClassVar[int]
            channel_id: str
            start_time: _timestamp_pb2.Timestamp
            end_time: _timestamp_pb2.Timestamp

            def __init__(self, channel_id: _Optional[str]=..., start_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]]=..., end_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]]=...) -> None:
                ...
        CHANNELS_FIELD_NUMBER: _ClassVar[int]
        API_KEY_CONFIG_FIELD_NUMBER: _ClassVar[int]
        channels: _containers.RepeatedCompositeFieldContainer[SlackSource.SlackChannels.SlackChannel]
        api_key_config: _api_auth_pb2.ApiAuth.ApiKeyConfig

        def __init__(self, channels: _Optional[_Iterable[_Union[SlackSource.SlackChannels.SlackChannel, _Mapping]]]=..., api_key_config: _Optional[_Union[_api_auth_pb2.ApiAuth.ApiKeyConfig, _Mapping]]=...) -> None:
            ...
    CHANNELS_FIELD_NUMBER: _ClassVar[int]
    channels: _containers.RepeatedCompositeFieldContainer[SlackSource.SlackChannels]

    def __init__(self, channels: _Optional[_Iterable[_Union[SlackSource.SlackChannels, _Mapping]]]=...) -> None:
        ...

class JiraSource(_message.Message):
    __slots__ = ('jira_queries',)

    class JiraQueries(_message.Message):
        __slots__ = ('projects', 'custom_queries', 'email', 'server_uri', 'api_key_config')
        PROJECTS_FIELD_NUMBER: _ClassVar[int]
        CUSTOM_QUERIES_FIELD_NUMBER: _ClassVar[int]
        EMAIL_FIELD_NUMBER: _ClassVar[int]
        SERVER_URI_FIELD_NUMBER: _ClassVar[int]
        API_KEY_CONFIG_FIELD_NUMBER: _ClassVar[int]
        projects: _containers.RepeatedScalarFieldContainer[str]
        custom_queries: _containers.RepeatedScalarFieldContainer[str]
        email: str
        server_uri: str
        api_key_config: _api_auth_pb2.ApiAuth.ApiKeyConfig

        def __init__(self, projects: _Optional[_Iterable[str]]=..., custom_queries: _Optional[_Iterable[str]]=..., email: _Optional[str]=..., server_uri: _Optional[str]=..., api_key_config: _Optional[_Union[_api_auth_pb2.ApiAuth.ApiKeyConfig, _Mapping]]=...) -> None:
            ...
    JIRA_QUERIES_FIELD_NUMBER: _ClassVar[int]
    jira_queries: _containers.RepeatedCompositeFieldContainer[JiraSource.JiraQueries]

    def __init__(self, jira_queries: _Optional[_Iterable[_Union[JiraSource.JiraQueries, _Mapping]]]=...) -> None:
        ...

class SharePointSources(_message.Message):
    __slots__ = ('share_point_sources',)

    class SharePointSource(_message.Message):
        __slots__ = ('sharepoint_folder_path', 'sharepoint_folder_id', 'drive_name', 'drive_id', 'client_id', 'client_secret', 'tenant_id', 'sharepoint_site_name', 'file_id')
        SHAREPOINT_FOLDER_PATH_FIELD_NUMBER: _ClassVar[int]
        SHAREPOINT_FOLDER_ID_FIELD_NUMBER: _ClassVar[int]
        DRIVE_NAME_FIELD_NUMBER: _ClassVar[int]
        DRIVE_ID_FIELD_NUMBER: _ClassVar[int]
        CLIENT_ID_FIELD_NUMBER: _ClassVar[int]
        CLIENT_SECRET_FIELD_NUMBER: _ClassVar[int]
        TENANT_ID_FIELD_NUMBER: _ClassVar[int]
        SHAREPOINT_SITE_NAME_FIELD_NUMBER: _ClassVar[int]
        FILE_ID_FIELD_NUMBER: _ClassVar[int]
        sharepoint_folder_path: str
        sharepoint_folder_id: str
        drive_name: str
        drive_id: str
        client_id: str
        client_secret: _api_auth_pb2.ApiAuth.ApiKeyConfig
        tenant_id: str
        sharepoint_site_name: str
        file_id: str

        def __init__(self, sharepoint_folder_path: _Optional[str]=..., sharepoint_folder_id: _Optional[str]=..., drive_name: _Optional[str]=..., drive_id: _Optional[str]=..., client_id: _Optional[str]=..., client_secret: _Optional[_Union[_api_auth_pb2.ApiAuth.ApiKeyConfig, _Mapping]]=..., tenant_id: _Optional[str]=..., sharepoint_site_name: _Optional[str]=..., file_id: _Optional[str]=...) -> None:
            ...
    SHARE_POINT_SOURCES_FIELD_NUMBER: _ClassVar[int]
    share_point_sources: _containers.RepeatedCompositeFieldContainer[SharePointSources.SharePointSource]

    def __init__(self, share_point_sources: _Optional[_Iterable[_Union[SharePointSources.SharePointSource, _Mapping]]]=...) -> None:
        ...