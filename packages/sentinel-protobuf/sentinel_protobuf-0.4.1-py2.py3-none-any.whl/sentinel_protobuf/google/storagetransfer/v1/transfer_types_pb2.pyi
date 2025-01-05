from google.api import field_behavior_pb2 as _field_behavior_pb2
from google.api import resource_pb2 as _resource_pb2
from google.protobuf import duration_pb2 as _duration_pb2
from google.protobuf import timestamp_pb2 as _timestamp_pb2
from google.rpc import code_pb2 as _code_pb2
from google.type import date_pb2 as _date_pb2
from google.type import timeofday_pb2 as _timeofday_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union
DESCRIPTOR: _descriptor.FileDescriptor

class GoogleServiceAccount(_message.Message):
    __slots__ = ('account_email', 'subject_id')
    ACCOUNT_EMAIL_FIELD_NUMBER: _ClassVar[int]
    SUBJECT_ID_FIELD_NUMBER: _ClassVar[int]
    account_email: str
    subject_id: str

    def __init__(self, account_email: _Optional[str]=..., subject_id: _Optional[str]=...) -> None:
        ...

class AwsAccessKey(_message.Message):
    __slots__ = ('access_key_id', 'secret_access_key')
    ACCESS_KEY_ID_FIELD_NUMBER: _ClassVar[int]
    SECRET_ACCESS_KEY_FIELD_NUMBER: _ClassVar[int]
    access_key_id: str
    secret_access_key: str

    def __init__(self, access_key_id: _Optional[str]=..., secret_access_key: _Optional[str]=...) -> None:
        ...

class AzureCredentials(_message.Message):
    __slots__ = ('sas_token',)
    SAS_TOKEN_FIELD_NUMBER: _ClassVar[int]
    sas_token: str

    def __init__(self, sas_token: _Optional[str]=...) -> None:
        ...

class ObjectConditions(_message.Message):
    __slots__ = ('min_time_elapsed_since_last_modification', 'max_time_elapsed_since_last_modification', 'include_prefixes', 'exclude_prefixes', 'last_modified_since', 'last_modified_before')
    MIN_TIME_ELAPSED_SINCE_LAST_MODIFICATION_FIELD_NUMBER: _ClassVar[int]
    MAX_TIME_ELAPSED_SINCE_LAST_MODIFICATION_FIELD_NUMBER: _ClassVar[int]
    INCLUDE_PREFIXES_FIELD_NUMBER: _ClassVar[int]
    EXCLUDE_PREFIXES_FIELD_NUMBER: _ClassVar[int]
    LAST_MODIFIED_SINCE_FIELD_NUMBER: _ClassVar[int]
    LAST_MODIFIED_BEFORE_FIELD_NUMBER: _ClassVar[int]
    min_time_elapsed_since_last_modification: _duration_pb2.Duration
    max_time_elapsed_since_last_modification: _duration_pb2.Duration
    include_prefixes: _containers.RepeatedScalarFieldContainer[str]
    exclude_prefixes: _containers.RepeatedScalarFieldContainer[str]
    last_modified_since: _timestamp_pb2.Timestamp
    last_modified_before: _timestamp_pb2.Timestamp

    def __init__(self, min_time_elapsed_since_last_modification: _Optional[_Union[_duration_pb2.Duration, _Mapping]]=..., max_time_elapsed_since_last_modification: _Optional[_Union[_duration_pb2.Duration, _Mapping]]=..., include_prefixes: _Optional[_Iterable[str]]=..., exclude_prefixes: _Optional[_Iterable[str]]=..., last_modified_since: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]]=..., last_modified_before: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]]=...) -> None:
        ...

class GcsData(_message.Message):
    __slots__ = ('bucket_name', 'path', 'managed_folder_transfer_enabled')
    BUCKET_NAME_FIELD_NUMBER: _ClassVar[int]
    PATH_FIELD_NUMBER: _ClassVar[int]
    MANAGED_FOLDER_TRANSFER_ENABLED_FIELD_NUMBER: _ClassVar[int]
    bucket_name: str
    path: str
    managed_folder_transfer_enabled: bool

    def __init__(self, bucket_name: _Optional[str]=..., path: _Optional[str]=..., managed_folder_transfer_enabled: bool=...) -> None:
        ...

class AwsS3Data(_message.Message):
    __slots__ = ('bucket_name', 'aws_access_key', 'path', 'role_arn', 'cloudfront_domain', 'credentials_secret', 'managed_private_network')
    BUCKET_NAME_FIELD_NUMBER: _ClassVar[int]
    AWS_ACCESS_KEY_FIELD_NUMBER: _ClassVar[int]
    PATH_FIELD_NUMBER: _ClassVar[int]
    ROLE_ARN_FIELD_NUMBER: _ClassVar[int]
    CLOUDFRONT_DOMAIN_FIELD_NUMBER: _ClassVar[int]
    CREDENTIALS_SECRET_FIELD_NUMBER: _ClassVar[int]
    MANAGED_PRIVATE_NETWORK_FIELD_NUMBER: _ClassVar[int]
    bucket_name: str
    aws_access_key: AwsAccessKey
    path: str
    role_arn: str
    cloudfront_domain: str
    credentials_secret: str
    managed_private_network: bool

    def __init__(self, bucket_name: _Optional[str]=..., aws_access_key: _Optional[_Union[AwsAccessKey, _Mapping]]=..., path: _Optional[str]=..., role_arn: _Optional[str]=..., cloudfront_domain: _Optional[str]=..., credentials_secret: _Optional[str]=..., managed_private_network: bool=...) -> None:
        ...

class AzureBlobStorageData(_message.Message):
    __slots__ = ('storage_account', 'azure_credentials', 'container', 'path', 'credentials_secret')
    STORAGE_ACCOUNT_FIELD_NUMBER: _ClassVar[int]
    AZURE_CREDENTIALS_FIELD_NUMBER: _ClassVar[int]
    CONTAINER_FIELD_NUMBER: _ClassVar[int]
    PATH_FIELD_NUMBER: _ClassVar[int]
    CREDENTIALS_SECRET_FIELD_NUMBER: _ClassVar[int]
    storage_account: str
    azure_credentials: AzureCredentials
    container: str
    path: str
    credentials_secret: str

    def __init__(self, storage_account: _Optional[str]=..., azure_credentials: _Optional[_Union[AzureCredentials, _Mapping]]=..., container: _Optional[str]=..., path: _Optional[str]=..., credentials_secret: _Optional[str]=...) -> None:
        ...

class HttpData(_message.Message):
    __slots__ = ('list_url',)
    LIST_URL_FIELD_NUMBER: _ClassVar[int]
    list_url: str

    def __init__(self, list_url: _Optional[str]=...) -> None:
        ...

class PosixFilesystem(_message.Message):
    __slots__ = ('root_directory',)
    ROOT_DIRECTORY_FIELD_NUMBER: _ClassVar[int]
    root_directory: str

    def __init__(self, root_directory: _Optional[str]=...) -> None:
        ...

class HdfsData(_message.Message):
    __slots__ = ('path',)
    PATH_FIELD_NUMBER: _ClassVar[int]
    path: str

    def __init__(self, path: _Optional[str]=...) -> None:
        ...

class AwsS3CompatibleData(_message.Message):
    __slots__ = ('bucket_name', 'path', 'endpoint', 'region', 's3_metadata')
    BUCKET_NAME_FIELD_NUMBER: _ClassVar[int]
    PATH_FIELD_NUMBER: _ClassVar[int]
    ENDPOINT_FIELD_NUMBER: _ClassVar[int]
    REGION_FIELD_NUMBER: _ClassVar[int]
    S3_METADATA_FIELD_NUMBER: _ClassVar[int]
    bucket_name: str
    path: str
    endpoint: str
    region: str
    s3_metadata: S3CompatibleMetadata

    def __init__(self, bucket_name: _Optional[str]=..., path: _Optional[str]=..., endpoint: _Optional[str]=..., region: _Optional[str]=..., s3_metadata: _Optional[_Union[S3CompatibleMetadata, _Mapping]]=...) -> None:
        ...

class S3CompatibleMetadata(_message.Message):
    __slots__ = ('auth_method', 'request_model', 'protocol', 'list_api')

    class AuthMethod(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        AUTH_METHOD_UNSPECIFIED: _ClassVar[S3CompatibleMetadata.AuthMethod]
        AUTH_METHOD_AWS_SIGNATURE_V4: _ClassVar[S3CompatibleMetadata.AuthMethod]
        AUTH_METHOD_AWS_SIGNATURE_V2: _ClassVar[S3CompatibleMetadata.AuthMethod]
    AUTH_METHOD_UNSPECIFIED: S3CompatibleMetadata.AuthMethod
    AUTH_METHOD_AWS_SIGNATURE_V4: S3CompatibleMetadata.AuthMethod
    AUTH_METHOD_AWS_SIGNATURE_V2: S3CompatibleMetadata.AuthMethod

    class RequestModel(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        REQUEST_MODEL_UNSPECIFIED: _ClassVar[S3CompatibleMetadata.RequestModel]
        REQUEST_MODEL_VIRTUAL_HOSTED_STYLE: _ClassVar[S3CompatibleMetadata.RequestModel]
        REQUEST_MODEL_PATH_STYLE: _ClassVar[S3CompatibleMetadata.RequestModel]
    REQUEST_MODEL_UNSPECIFIED: S3CompatibleMetadata.RequestModel
    REQUEST_MODEL_VIRTUAL_HOSTED_STYLE: S3CompatibleMetadata.RequestModel
    REQUEST_MODEL_PATH_STYLE: S3CompatibleMetadata.RequestModel

    class NetworkProtocol(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        NETWORK_PROTOCOL_UNSPECIFIED: _ClassVar[S3CompatibleMetadata.NetworkProtocol]
        NETWORK_PROTOCOL_HTTPS: _ClassVar[S3CompatibleMetadata.NetworkProtocol]
        NETWORK_PROTOCOL_HTTP: _ClassVar[S3CompatibleMetadata.NetworkProtocol]
    NETWORK_PROTOCOL_UNSPECIFIED: S3CompatibleMetadata.NetworkProtocol
    NETWORK_PROTOCOL_HTTPS: S3CompatibleMetadata.NetworkProtocol
    NETWORK_PROTOCOL_HTTP: S3CompatibleMetadata.NetworkProtocol

    class ListApi(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        LIST_API_UNSPECIFIED: _ClassVar[S3CompatibleMetadata.ListApi]
        LIST_OBJECTS_V2: _ClassVar[S3CompatibleMetadata.ListApi]
        LIST_OBJECTS: _ClassVar[S3CompatibleMetadata.ListApi]
    LIST_API_UNSPECIFIED: S3CompatibleMetadata.ListApi
    LIST_OBJECTS_V2: S3CompatibleMetadata.ListApi
    LIST_OBJECTS: S3CompatibleMetadata.ListApi
    AUTH_METHOD_FIELD_NUMBER: _ClassVar[int]
    REQUEST_MODEL_FIELD_NUMBER: _ClassVar[int]
    PROTOCOL_FIELD_NUMBER: _ClassVar[int]
    LIST_API_FIELD_NUMBER: _ClassVar[int]
    auth_method: S3CompatibleMetadata.AuthMethod
    request_model: S3CompatibleMetadata.RequestModel
    protocol: S3CompatibleMetadata.NetworkProtocol
    list_api: S3CompatibleMetadata.ListApi

    def __init__(self, auth_method: _Optional[_Union[S3CompatibleMetadata.AuthMethod, str]]=..., request_model: _Optional[_Union[S3CompatibleMetadata.RequestModel, str]]=..., protocol: _Optional[_Union[S3CompatibleMetadata.NetworkProtocol, str]]=..., list_api: _Optional[_Union[S3CompatibleMetadata.ListApi, str]]=...) -> None:
        ...

class AgentPool(_message.Message):
    __slots__ = ('name', 'display_name', 'state', 'bandwidth_limit')

    class State(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        STATE_UNSPECIFIED: _ClassVar[AgentPool.State]
        CREATING: _ClassVar[AgentPool.State]
        CREATED: _ClassVar[AgentPool.State]
        DELETING: _ClassVar[AgentPool.State]
    STATE_UNSPECIFIED: AgentPool.State
    CREATING: AgentPool.State
    CREATED: AgentPool.State
    DELETING: AgentPool.State

    class BandwidthLimit(_message.Message):
        __slots__ = ('limit_mbps',)
        LIMIT_MBPS_FIELD_NUMBER: _ClassVar[int]
        limit_mbps: int

        def __init__(self, limit_mbps: _Optional[int]=...) -> None:
            ...
    NAME_FIELD_NUMBER: _ClassVar[int]
    DISPLAY_NAME_FIELD_NUMBER: _ClassVar[int]
    STATE_FIELD_NUMBER: _ClassVar[int]
    BANDWIDTH_LIMIT_FIELD_NUMBER: _ClassVar[int]
    name: str
    display_name: str
    state: AgentPool.State
    bandwidth_limit: AgentPool.BandwidthLimit

    def __init__(self, name: _Optional[str]=..., display_name: _Optional[str]=..., state: _Optional[_Union[AgentPool.State, str]]=..., bandwidth_limit: _Optional[_Union[AgentPool.BandwidthLimit, _Mapping]]=...) -> None:
        ...

class TransferOptions(_message.Message):
    __slots__ = ('overwrite_objects_already_existing_in_sink', 'delete_objects_unique_in_sink', 'delete_objects_from_source_after_transfer', 'overwrite_when', 'metadata_options')

    class OverwriteWhen(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        OVERWRITE_WHEN_UNSPECIFIED: _ClassVar[TransferOptions.OverwriteWhen]
        DIFFERENT: _ClassVar[TransferOptions.OverwriteWhen]
        NEVER: _ClassVar[TransferOptions.OverwriteWhen]
        ALWAYS: _ClassVar[TransferOptions.OverwriteWhen]
    OVERWRITE_WHEN_UNSPECIFIED: TransferOptions.OverwriteWhen
    DIFFERENT: TransferOptions.OverwriteWhen
    NEVER: TransferOptions.OverwriteWhen
    ALWAYS: TransferOptions.OverwriteWhen
    OVERWRITE_OBJECTS_ALREADY_EXISTING_IN_SINK_FIELD_NUMBER: _ClassVar[int]
    DELETE_OBJECTS_UNIQUE_IN_SINK_FIELD_NUMBER: _ClassVar[int]
    DELETE_OBJECTS_FROM_SOURCE_AFTER_TRANSFER_FIELD_NUMBER: _ClassVar[int]
    OVERWRITE_WHEN_FIELD_NUMBER: _ClassVar[int]
    METADATA_OPTIONS_FIELD_NUMBER: _ClassVar[int]
    overwrite_objects_already_existing_in_sink: bool
    delete_objects_unique_in_sink: bool
    delete_objects_from_source_after_transfer: bool
    overwrite_when: TransferOptions.OverwriteWhen
    metadata_options: MetadataOptions

    def __init__(self, overwrite_objects_already_existing_in_sink: bool=..., delete_objects_unique_in_sink: bool=..., delete_objects_from_source_after_transfer: bool=..., overwrite_when: _Optional[_Union[TransferOptions.OverwriteWhen, str]]=..., metadata_options: _Optional[_Union[MetadataOptions, _Mapping]]=...) -> None:
        ...

class TransferSpec(_message.Message):
    __slots__ = ('gcs_data_sink', 'posix_data_sink', 'gcs_data_source', 'aws_s3_data_source', 'http_data_source', 'posix_data_source', 'azure_blob_storage_data_source', 'aws_s3_compatible_data_source', 'hdfs_data_source', 'gcs_intermediate_data_location', 'object_conditions', 'transfer_options', 'transfer_manifest', 'source_agent_pool_name', 'sink_agent_pool_name')
    GCS_DATA_SINK_FIELD_NUMBER: _ClassVar[int]
    POSIX_DATA_SINK_FIELD_NUMBER: _ClassVar[int]
    GCS_DATA_SOURCE_FIELD_NUMBER: _ClassVar[int]
    AWS_S3_DATA_SOURCE_FIELD_NUMBER: _ClassVar[int]
    HTTP_DATA_SOURCE_FIELD_NUMBER: _ClassVar[int]
    POSIX_DATA_SOURCE_FIELD_NUMBER: _ClassVar[int]
    AZURE_BLOB_STORAGE_DATA_SOURCE_FIELD_NUMBER: _ClassVar[int]
    AWS_S3_COMPATIBLE_DATA_SOURCE_FIELD_NUMBER: _ClassVar[int]
    HDFS_DATA_SOURCE_FIELD_NUMBER: _ClassVar[int]
    GCS_INTERMEDIATE_DATA_LOCATION_FIELD_NUMBER: _ClassVar[int]
    OBJECT_CONDITIONS_FIELD_NUMBER: _ClassVar[int]
    TRANSFER_OPTIONS_FIELD_NUMBER: _ClassVar[int]
    TRANSFER_MANIFEST_FIELD_NUMBER: _ClassVar[int]
    SOURCE_AGENT_POOL_NAME_FIELD_NUMBER: _ClassVar[int]
    SINK_AGENT_POOL_NAME_FIELD_NUMBER: _ClassVar[int]
    gcs_data_sink: GcsData
    posix_data_sink: PosixFilesystem
    gcs_data_source: GcsData
    aws_s3_data_source: AwsS3Data
    http_data_source: HttpData
    posix_data_source: PosixFilesystem
    azure_blob_storage_data_source: AzureBlobStorageData
    aws_s3_compatible_data_source: AwsS3CompatibleData
    hdfs_data_source: HdfsData
    gcs_intermediate_data_location: GcsData
    object_conditions: ObjectConditions
    transfer_options: TransferOptions
    transfer_manifest: TransferManifest
    source_agent_pool_name: str
    sink_agent_pool_name: str

    def __init__(self, gcs_data_sink: _Optional[_Union[GcsData, _Mapping]]=..., posix_data_sink: _Optional[_Union[PosixFilesystem, _Mapping]]=..., gcs_data_source: _Optional[_Union[GcsData, _Mapping]]=..., aws_s3_data_source: _Optional[_Union[AwsS3Data, _Mapping]]=..., http_data_source: _Optional[_Union[HttpData, _Mapping]]=..., posix_data_source: _Optional[_Union[PosixFilesystem, _Mapping]]=..., azure_blob_storage_data_source: _Optional[_Union[AzureBlobStorageData, _Mapping]]=..., aws_s3_compatible_data_source: _Optional[_Union[AwsS3CompatibleData, _Mapping]]=..., hdfs_data_source: _Optional[_Union[HdfsData, _Mapping]]=..., gcs_intermediate_data_location: _Optional[_Union[GcsData, _Mapping]]=..., object_conditions: _Optional[_Union[ObjectConditions, _Mapping]]=..., transfer_options: _Optional[_Union[TransferOptions, _Mapping]]=..., transfer_manifest: _Optional[_Union[TransferManifest, _Mapping]]=..., source_agent_pool_name: _Optional[str]=..., sink_agent_pool_name: _Optional[str]=...) -> None:
        ...

class ReplicationSpec(_message.Message):
    __slots__ = ('gcs_data_source', 'gcs_data_sink', 'object_conditions', 'transfer_options')
    GCS_DATA_SOURCE_FIELD_NUMBER: _ClassVar[int]
    GCS_DATA_SINK_FIELD_NUMBER: _ClassVar[int]
    OBJECT_CONDITIONS_FIELD_NUMBER: _ClassVar[int]
    TRANSFER_OPTIONS_FIELD_NUMBER: _ClassVar[int]
    gcs_data_source: GcsData
    gcs_data_sink: GcsData
    object_conditions: ObjectConditions
    transfer_options: TransferOptions

    def __init__(self, gcs_data_source: _Optional[_Union[GcsData, _Mapping]]=..., gcs_data_sink: _Optional[_Union[GcsData, _Mapping]]=..., object_conditions: _Optional[_Union[ObjectConditions, _Mapping]]=..., transfer_options: _Optional[_Union[TransferOptions, _Mapping]]=...) -> None:
        ...

class MetadataOptions(_message.Message):
    __slots__ = ('symlink', 'mode', 'gid', 'uid', 'acl', 'storage_class', 'temporary_hold', 'kms_key', 'time_created')

    class Symlink(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        SYMLINK_UNSPECIFIED: _ClassVar[MetadataOptions.Symlink]
        SYMLINK_SKIP: _ClassVar[MetadataOptions.Symlink]
        SYMLINK_PRESERVE: _ClassVar[MetadataOptions.Symlink]
    SYMLINK_UNSPECIFIED: MetadataOptions.Symlink
    SYMLINK_SKIP: MetadataOptions.Symlink
    SYMLINK_PRESERVE: MetadataOptions.Symlink

    class Mode(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        MODE_UNSPECIFIED: _ClassVar[MetadataOptions.Mode]
        MODE_SKIP: _ClassVar[MetadataOptions.Mode]
        MODE_PRESERVE: _ClassVar[MetadataOptions.Mode]
    MODE_UNSPECIFIED: MetadataOptions.Mode
    MODE_SKIP: MetadataOptions.Mode
    MODE_PRESERVE: MetadataOptions.Mode

    class GID(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        GID_UNSPECIFIED: _ClassVar[MetadataOptions.GID]
        GID_SKIP: _ClassVar[MetadataOptions.GID]
        GID_NUMBER: _ClassVar[MetadataOptions.GID]
    GID_UNSPECIFIED: MetadataOptions.GID
    GID_SKIP: MetadataOptions.GID
    GID_NUMBER: MetadataOptions.GID

    class UID(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        UID_UNSPECIFIED: _ClassVar[MetadataOptions.UID]
        UID_SKIP: _ClassVar[MetadataOptions.UID]
        UID_NUMBER: _ClassVar[MetadataOptions.UID]
    UID_UNSPECIFIED: MetadataOptions.UID
    UID_SKIP: MetadataOptions.UID
    UID_NUMBER: MetadataOptions.UID

    class Acl(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        ACL_UNSPECIFIED: _ClassVar[MetadataOptions.Acl]
        ACL_DESTINATION_BUCKET_DEFAULT: _ClassVar[MetadataOptions.Acl]
        ACL_PRESERVE: _ClassVar[MetadataOptions.Acl]
    ACL_UNSPECIFIED: MetadataOptions.Acl
    ACL_DESTINATION_BUCKET_DEFAULT: MetadataOptions.Acl
    ACL_PRESERVE: MetadataOptions.Acl

    class StorageClass(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        STORAGE_CLASS_UNSPECIFIED: _ClassVar[MetadataOptions.StorageClass]
        STORAGE_CLASS_DESTINATION_BUCKET_DEFAULT: _ClassVar[MetadataOptions.StorageClass]
        STORAGE_CLASS_PRESERVE: _ClassVar[MetadataOptions.StorageClass]
        STORAGE_CLASS_STANDARD: _ClassVar[MetadataOptions.StorageClass]
        STORAGE_CLASS_NEARLINE: _ClassVar[MetadataOptions.StorageClass]
        STORAGE_CLASS_COLDLINE: _ClassVar[MetadataOptions.StorageClass]
        STORAGE_CLASS_ARCHIVE: _ClassVar[MetadataOptions.StorageClass]
    STORAGE_CLASS_UNSPECIFIED: MetadataOptions.StorageClass
    STORAGE_CLASS_DESTINATION_BUCKET_DEFAULT: MetadataOptions.StorageClass
    STORAGE_CLASS_PRESERVE: MetadataOptions.StorageClass
    STORAGE_CLASS_STANDARD: MetadataOptions.StorageClass
    STORAGE_CLASS_NEARLINE: MetadataOptions.StorageClass
    STORAGE_CLASS_COLDLINE: MetadataOptions.StorageClass
    STORAGE_CLASS_ARCHIVE: MetadataOptions.StorageClass

    class TemporaryHold(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        TEMPORARY_HOLD_UNSPECIFIED: _ClassVar[MetadataOptions.TemporaryHold]
        TEMPORARY_HOLD_SKIP: _ClassVar[MetadataOptions.TemporaryHold]
        TEMPORARY_HOLD_PRESERVE: _ClassVar[MetadataOptions.TemporaryHold]
    TEMPORARY_HOLD_UNSPECIFIED: MetadataOptions.TemporaryHold
    TEMPORARY_HOLD_SKIP: MetadataOptions.TemporaryHold
    TEMPORARY_HOLD_PRESERVE: MetadataOptions.TemporaryHold

    class KmsKey(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        KMS_KEY_UNSPECIFIED: _ClassVar[MetadataOptions.KmsKey]
        KMS_KEY_DESTINATION_BUCKET_DEFAULT: _ClassVar[MetadataOptions.KmsKey]
        KMS_KEY_PRESERVE: _ClassVar[MetadataOptions.KmsKey]
    KMS_KEY_UNSPECIFIED: MetadataOptions.KmsKey
    KMS_KEY_DESTINATION_BUCKET_DEFAULT: MetadataOptions.KmsKey
    KMS_KEY_PRESERVE: MetadataOptions.KmsKey

    class TimeCreated(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        TIME_CREATED_UNSPECIFIED: _ClassVar[MetadataOptions.TimeCreated]
        TIME_CREATED_SKIP: _ClassVar[MetadataOptions.TimeCreated]
        TIME_CREATED_PRESERVE_AS_CUSTOM_TIME: _ClassVar[MetadataOptions.TimeCreated]
    TIME_CREATED_UNSPECIFIED: MetadataOptions.TimeCreated
    TIME_CREATED_SKIP: MetadataOptions.TimeCreated
    TIME_CREATED_PRESERVE_AS_CUSTOM_TIME: MetadataOptions.TimeCreated
    SYMLINK_FIELD_NUMBER: _ClassVar[int]
    MODE_FIELD_NUMBER: _ClassVar[int]
    GID_FIELD_NUMBER: _ClassVar[int]
    UID_FIELD_NUMBER: _ClassVar[int]
    ACL_FIELD_NUMBER: _ClassVar[int]
    STORAGE_CLASS_FIELD_NUMBER: _ClassVar[int]
    TEMPORARY_HOLD_FIELD_NUMBER: _ClassVar[int]
    KMS_KEY_FIELD_NUMBER: _ClassVar[int]
    TIME_CREATED_FIELD_NUMBER: _ClassVar[int]
    symlink: MetadataOptions.Symlink
    mode: MetadataOptions.Mode
    gid: MetadataOptions.GID
    uid: MetadataOptions.UID
    acl: MetadataOptions.Acl
    storage_class: MetadataOptions.StorageClass
    temporary_hold: MetadataOptions.TemporaryHold
    kms_key: MetadataOptions.KmsKey
    time_created: MetadataOptions.TimeCreated

    def __init__(self, symlink: _Optional[_Union[MetadataOptions.Symlink, str]]=..., mode: _Optional[_Union[MetadataOptions.Mode, str]]=..., gid: _Optional[_Union[MetadataOptions.GID, str]]=..., uid: _Optional[_Union[MetadataOptions.UID, str]]=..., acl: _Optional[_Union[MetadataOptions.Acl, str]]=..., storage_class: _Optional[_Union[MetadataOptions.StorageClass, str]]=..., temporary_hold: _Optional[_Union[MetadataOptions.TemporaryHold, str]]=..., kms_key: _Optional[_Union[MetadataOptions.KmsKey, str]]=..., time_created: _Optional[_Union[MetadataOptions.TimeCreated, str]]=...) -> None:
        ...

class TransferManifest(_message.Message):
    __slots__ = ('location',)
    LOCATION_FIELD_NUMBER: _ClassVar[int]
    location: str

    def __init__(self, location: _Optional[str]=...) -> None:
        ...

class Schedule(_message.Message):
    __slots__ = ('schedule_start_date', 'schedule_end_date', 'start_time_of_day', 'end_time_of_day', 'repeat_interval')
    SCHEDULE_START_DATE_FIELD_NUMBER: _ClassVar[int]
    SCHEDULE_END_DATE_FIELD_NUMBER: _ClassVar[int]
    START_TIME_OF_DAY_FIELD_NUMBER: _ClassVar[int]
    END_TIME_OF_DAY_FIELD_NUMBER: _ClassVar[int]
    REPEAT_INTERVAL_FIELD_NUMBER: _ClassVar[int]
    schedule_start_date: _date_pb2.Date
    schedule_end_date: _date_pb2.Date
    start_time_of_day: _timeofday_pb2.TimeOfDay
    end_time_of_day: _timeofday_pb2.TimeOfDay
    repeat_interval: _duration_pb2.Duration

    def __init__(self, schedule_start_date: _Optional[_Union[_date_pb2.Date, _Mapping]]=..., schedule_end_date: _Optional[_Union[_date_pb2.Date, _Mapping]]=..., start_time_of_day: _Optional[_Union[_timeofday_pb2.TimeOfDay, _Mapping]]=..., end_time_of_day: _Optional[_Union[_timeofday_pb2.TimeOfDay, _Mapping]]=..., repeat_interval: _Optional[_Union[_duration_pb2.Duration, _Mapping]]=...) -> None:
        ...

class EventStream(_message.Message):
    __slots__ = ('name', 'event_stream_start_time', 'event_stream_expiration_time')
    NAME_FIELD_NUMBER: _ClassVar[int]
    EVENT_STREAM_START_TIME_FIELD_NUMBER: _ClassVar[int]
    EVENT_STREAM_EXPIRATION_TIME_FIELD_NUMBER: _ClassVar[int]
    name: str
    event_stream_start_time: _timestamp_pb2.Timestamp
    event_stream_expiration_time: _timestamp_pb2.Timestamp

    def __init__(self, name: _Optional[str]=..., event_stream_start_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]]=..., event_stream_expiration_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]]=...) -> None:
        ...

class TransferJob(_message.Message):
    __slots__ = ('name', 'description', 'project_id', 'transfer_spec', 'replication_spec', 'notification_config', 'logging_config', 'schedule', 'event_stream', 'status', 'creation_time', 'last_modification_time', 'deletion_time', 'latest_operation_name')

    class Status(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        STATUS_UNSPECIFIED: _ClassVar[TransferJob.Status]
        ENABLED: _ClassVar[TransferJob.Status]
        DISABLED: _ClassVar[TransferJob.Status]
        DELETED: _ClassVar[TransferJob.Status]
    STATUS_UNSPECIFIED: TransferJob.Status
    ENABLED: TransferJob.Status
    DISABLED: TransferJob.Status
    DELETED: TransferJob.Status
    NAME_FIELD_NUMBER: _ClassVar[int]
    DESCRIPTION_FIELD_NUMBER: _ClassVar[int]
    PROJECT_ID_FIELD_NUMBER: _ClassVar[int]
    TRANSFER_SPEC_FIELD_NUMBER: _ClassVar[int]
    REPLICATION_SPEC_FIELD_NUMBER: _ClassVar[int]
    NOTIFICATION_CONFIG_FIELD_NUMBER: _ClassVar[int]
    LOGGING_CONFIG_FIELD_NUMBER: _ClassVar[int]
    SCHEDULE_FIELD_NUMBER: _ClassVar[int]
    EVENT_STREAM_FIELD_NUMBER: _ClassVar[int]
    STATUS_FIELD_NUMBER: _ClassVar[int]
    CREATION_TIME_FIELD_NUMBER: _ClassVar[int]
    LAST_MODIFICATION_TIME_FIELD_NUMBER: _ClassVar[int]
    DELETION_TIME_FIELD_NUMBER: _ClassVar[int]
    LATEST_OPERATION_NAME_FIELD_NUMBER: _ClassVar[int]
    name: str
    description: str
    project_id: str
    transfer_spec: TransferSpec
    replication_spec: ReplicationSpec
    notification_config: NotificationConfig
    logging_config: LoggingConfig
    schedule: Schedule
    event_stream: EventStream
    status: TransferJob.Status
    creation_time: _timestamp_pb2.Timestamp
    last_modification_time: _timestamp_pb2.Timestamp
    deletion_time: _timestamp_pb2.Timestamp
    latest_operation_name: str

    def __init__(self, name: _Optional[str]=..., description: _Optional[str]=..., project_id: _Optional[str]=..., transfer_spec: _Optional[_Union[TransferSpec, _Mapping]]=..., replication_spec: _Optional[_Union[ReplicationSpec, _Mapping]]=..., notification_config: _Optional[_Union[NotificationConfig, _Mapping]]=..., logging_config: _Optional[_Union[LoggingConfig, _Mapping]]=..., schedule: _Optional[_Union[Schedule, _Mapping]]=..., event_stream: _Optional[_Union[EventStream, _Mapping]]=..., status: _Optional[_Union[TransferJob.Status, str]]=..., creation_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]]=..., last_modification_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]]=..., deletion_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]]=..., latest_operation_name: _Optional[str]=...) -> None:
        ...

class ErrorLogEntry(_message.Message):
    __slots__ = ('url', 'error_details')
    URL_FIELD_NUMBER: _ClassVar[int]
    ERROR_DETAILS_FIELD_NUMBER: _ClassVar[int]
    url: str
    error_details: _containers.RepeatedScalarFieldContainer[str]

    def __init__(self, url: _Optional[str]=..., error_details: _Optional[_Iterable[str]]=...) -> None:
        ...

class ErrorSummary(_message.Message):
    __slots__ = ('error_code', 'error_count', 'error_log_entries')
    ERROR_CODE_FIELD_NUMBER: _ClassVar[int]
    ERROR_COUNT_FIELD_NUMBER: _ClassVar[int]
    ERROR_LOG_ENTRIES_FIELD_NUMBER: _ClassVar[int]
    error_code: _code_pb2.Code
    error_count: int
    error_log_entries: _containers.RepeatedCompositeFieldContainer[ErrorLogEntry]

    def __init__(self, error_code: _Optional[_Union[_code_pb2.Code, str]]=..., error_count: _Optional[int]=..., error_log_entries: _Optional[_Iterable[_Union[ErrorLogEntry, _Mapping]]]=...) -> None:
        ...

class TransferCounters(_message.Message):
    __slots__ = ('objects_found_from_source', 'bytes_found_from_source', 'objects_found_only_from_sink', 'bytes_found_only_from_sink', 'objects_from_source_skipped_by_sync', 'bytes_from_source_skipped_by_sync', 'objects_copied_to_sink', 'bytes_copied_to_sink', 'objects_deleted_from_source', 'bytes_deleted_from_source', 'objects_deleted_from_sink', 'bytes_deleted_from_sink', 'objects_from_source_failed', 'bytes_from_source_failed', 'objects_failed_to_delete_from_sink', 'bytes_failed_to_delete_from_sink', 'directories_found_from_source', 'directories_failed_to_list_from_source', 'directories_successfully_listed_from_source', 'intermediate_objects_cleaned_up', 'intermediate_objects_failed_cleaned_up')
    OBJECTS_FOUND_FROM_SOURCE_FIELD_NUMBER: _ClassVar[int]
    BYTES_FOUND_FROM_SOURCE_FIELD_NUMBER: _ClassVar[int]
    OBJECTS_FOUND_ONLY_FROM_SINK_FIELD_NUMBER: _ClassVar[int]
    BYTES_FOUND_ONLY_FROM_SINK_FIELD_NUMBER: _ClassVar[int]
    OBJECTS_FROM_SOURCE_SKIPPED_BY_SYNC_FIELD_NUMBER: _ClassVar[int]
    BYTES_FROM_SOURCE_SKIPPED_BY_SYNC_FIELD_NUMBER: _ClassVar[int]
    OBJECTS_COPIED_TO_SINK_FIELD_NUMBER: _ClassVar[int]
    BYTES_COPIED_TO_SINK_FIELD_NUMBER: _ClassVar[int]
    OBJECTS_DELETED_FROM_SOURCE_FIELD_NUMBER: _ClassVar[int]
    BYTES_DELETED_FROM_SOURCE_FIELD_NUMBER: _ClassVar[int]
    OBJECTS_DELETED_FROM_SINK_FIELD_NUMBER: _ClassVar[int]
    BYTES_DELETED_FROM_SINK_FIELD_NUMBER: _ClassVar[int]
    OBJECTS_FROM_SOURCE_FAILED_FIELD_NUMBER: _ClassVar[int]
    BYTES_FROM_SOURCE_FAILED_FIELD_NUMBER: _ClassVar[int]
    OBJECTS_FAILED_TO_DELETE_FROM_SINK_FIELD_NUMBER: _ClassVar[int]
    BYTES_FAILED_TO_DELETE_FROM_SINK_FIELD_NUMBER: _ClassVar[int]
    DIRECTORIES_FOUND_FROM_SOURCE_FIELD_NUMBER: _ClassVar[int]
    DIRECTORIES_FAILED_TO_LIST_FROM_SOURCE_FIELD_NUMBER: _ClassVar[int]
    DIRECTORIES_SUCCESSFULLY_LISTED_FROM_SOURCE_FIELD_NUMBER: _ClassVar[int]
    INTERMEDIATE_OBJECTS_CLEANED_UP_FIELD_NUMBER: _ClassVar[int]
    INTERMEDIATE_OBJECTS_FAILED_CLEANED_UP_FIELD_NUMBER: _ClassVar[int]
    objects_found_from_source: int
    bytes_found_from_source: int
    objects_found_only_from_sink: int
    bytes_found_only_from_sink: int
    objects_from_source_skipped_by_sync: int
    bytes_from_source_skipped_by_sync: int
    objects_copied_to_sink: int
    bytes_copied_to_sink: int
    objects_deleted_from_source: int
    bytes_deleted_from_source: int
    objects_deleted_from_sink: int
    bytes_deleted_from_sink: int
    objects_from_source_failed: int
    bytes_from_source_failed: int
    objects_failed_to_delete_from_sink: int
    bytes_failed_to_delete_from_sink: int
    directories_found_from_source: int
    directories_failed_to_list_from_source: int
    directories_successfully_listed_from_source: int
    intermediate_objects_cleaned_up: int
    intermediate_objects_failed_cleaned_up: int

    def __init__(self, objects_found_from_source: _Optional[int]=..., bytes_found_from_source: _Optional[int]=..., objects_found_only_from_sink: _Optional[int]=..., bytes_found_only_from_sink: _Optional[int]=..., objects_from_source_skipped_by_sync: _Optional[int]=..., bytes_from_source_skipped_by_sync: _Optional[int]=..., objects_copied_to_sink: _Optional[int]=..., bytes_copied_to_sink: _Optional[int]=..., objects_deleted_from_source: _Optional[int]=..., bytes_deleted_from_source: _Optional[int]=..., objects_deleted_from_sink: _Optional[int]=..., bytes_deleted_from_sink: _Optional[int]=..., objects_from_source_failed: _Optional[int]=..., bytes_from_source_failed: _Optional[int]=..., objects_failed_to_delete_from_sink: _Optional[int]=..., bytes_failed_to_delete_from_sink: _Optional[int]=..., directories_found_from_source: _Optional[int]=..., directories_failed_to_list_from_source: _Optional[int]=..., directories_successfully_listed_from_source: _Optional[int]=..., intermediate_objects_cleaned_up: _Optional[int]=..., intermediate_objects_failed_cleaned_up: _Optional[int]=...) -> None:
        ...

class NotificationConfig(_message.Message):
    __slots__ = ('pubsub_topic', 'event_types', 'payload_format')

    class EventType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        EVENT_TYPE_UNSPECIFIED: _ClassVar[NotificationConfig.EventType]
        TRANSFER_OPERATION_SUCCESS: _ClassVar[NotificationConfig.EventType]
        TRANSFER_OPERATION_FAILED: _ClassVar[NotificationConfig.EventType]
        TRANSFER_OPERATION_ABORTED: _ClassVar[NotificationConfig.EventType]
    EVENT_TYPE_UNSPECIFIED: NotificationConfig.EventType
    TRANSFER_OPERATION_SUCCESS: NotificationConfig.EventType
    TRANSFER_OPERATION_FAILED: NotificationConfig.EventType
    TRANSFER_OPERATION_ABORTED: NotificationConfig.EventType

    class PayloadFormat(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        PAYLOAD_FORMAT_UNSPECIFIED: _ClassVar[NotificationConfig.PayloadFormat]
        NONE: _ClassVar[NotificationConfig.PayloadFormat]
        JSON: _ClassVar[NotificationConfig.PayloadFormat]
    PAYLOAD_FORMAT_UNSPECIFIED: NotificationConfig.PayloadFormat
    NONE: NotificationConfig.PayloadFormat
    JSON: NotificationConfig.PayloadFormat
    PUBSUB_TOPIC_FIELD_NUMBER: _ClassVar[int]
    EVENT_TYPES_FIELD_NUMBER: _ClassVar[int]
    PAYLOAD_FORMAT_FIELD_NUMBER: _ClassVar[int]
    pubsub_topic: str
    event_types: _containers.RepeatedScalarFieldContainer[NotificationConfig.EventType]
    payload_format: NotificationConfig.PayloadFormat

    def __init__(self, pubsub_topic: _Optional[str]=..., event_types: _Optional[_Iterable[_Union[NotificationConfig.EventType, str]]]=..., payload_format: _Optional[_Union[NotificationConfig.PayloadFormat, str]]=...) -> None:
        ...

class LoggingConfig(_message.Message):
    __slots__ = ('log_actions', 'log_action_states', 'enable_onprem_gcs_transfer_logs')

    class LoggableAction(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        LOGGABLE_ACTION_UNSPECIFIED: _ClassVar[LoggingConfig.LoggableAction]
        FIND: _ClassVar[LoggingConfig.LoggableAction]
        DELETE: _ClassVar[LoggingConfig.LoggableAction]
        COPY: _ClassVar[LoggingConfig.LoggableAction]
    LOGGABLE_ACTION_UNSPECIFIED: LoggingConfig.LoggableAction
    FIND: LoggingConfig.LoggableAction
    DELETE: LoggingConfig.LoggableAction
    COPY: LoggingConfig.LoggableAction

    class LoggableActionState(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        LOGGABLE_ACTION_STATE_UNSPECIFIED: _ClassVar[LoggingConfig.LoggableActionState]
        SUCCEEDED: _ClassVar[LoggingConfig.LoggableActionState]
        FAILED: _ClassVar[LoggingConfig.LoggableActionState]
    LOGGABLE_ACTION_STATE_UNSPECIFIED: LoggingConfig.LoggableActionState
    SUCCEEDED: LoggingConfig.LoggableActionState
    FAILED: LoggingConfig.LoggableActionState
    LOG_ACTIONS_FIELD_NUMBER: _ClassVar[int]
    LOG_ACTION_STATES_FIELD_NUMBER: _ClassVar[int]
    ENABLE_ONPREM_GCS_TRANSFER_LOGS_FIELD_NUMBER: _ClassVar[int]
    log_actions: _containers.RepeatedScalarFieldContainer[LoggingConfig.LoggableAction]
    log_action_states: _containers.RepeatedScalarFieldContainer[LoggingConfig.LoggableActionState]
    enable_onprem_gcs_transfer_logs: bool

    def __init__(self, log_actions: _Optional[_Iterable[_Union[LoggingConfig.LoggableAction, str]]]=..., log_action_states: _Optional[_Iterable[_Union[LoggingConfig.LoggableActionState, str]]]=..., enable_onprem_gcs_transfer_logs: bool=...) -> None:
        ...

class TransferOperation(_message.Message):
    __slots__ = ('name', 'project_id', 'transfer_spec', 'notification_config', 'logging_config', 'start_time', 'end_time', 'status', 'counters', 'error_breakdowns', 'transfer_job_name')

    class Status(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        STATUS_UNSPECIFIED: _ClassVar[TransferOperation.Status]
        IN_PROGRESS: _ClassVar[TransferOperation.Status]
        PAUSED: _ClassVar[TransferOperation.Status]
        SUCCESS: _ClassVar[TransferOperation.Status]
        FAILED: _ClassVar[TransferOperation.Status]
        ABORTED: _ClassVar[TransferOperation.Status]
        QUEUED: _ClassVar[TransferOperation.Status]
        SUSPENDING: _ClassVar[TransferOperation.Status]
    STATUS_UNSPECIFIED: TransferOperation.Status
    IN_PROGRESS: TransferOperation.Status
    PAUSED: TransferOperation.Status
    SUCCESS: TransferOperation.Status
    FAILED: TransferOperation.Status
    ABORTED: TransferOperation.Status
    QUEUED: TransferOperation.Status
    SUSPENDING: TransferOperation.Status
    NAME_FIELD_NUMBER: _ClassVar[int]
    PROJECT_ID_FIELD_NUMBER: _ClassVar[int]
    TRANSFER_SPEC_FIELD_NUMBER: _ClassVar[int]
    NOTIFICATION_CONFIG_FIELD_NUMBER: _ClassVar[int]
    LOGGING_CONFIG_FIELD_NUMBER: _ClassVar[int]
    START_TIME_FIELD_NUMBER: _ClassVar[int]
    END_TIME_FIELD_NUMBER: _ClassVar[int]
    STATUS_FIELD_NUMBER: _ClassVar[int]
    COUNTERS_FIELD_NUMBER: _ClassVar[int]
    ERROR_BREAKDOWNS_FIELD_NUMBER: _ClassVar[int]
    TRANSFER_JOB_NAME_FIELD_NUMBER: _ClassVar[int]
    name: str
    project_id: str
    transfer_spec: TransferSpec
    notification_config: NotificationConfig
    logging_config: LoggingConfig
    start_time: _timestamp_pb2.Timestamp
    end_time: _timestamp_pb2.Timestamp
    status: TransferOperation.Status
    counters: TransferCounters
    error_breakdowns: _containers.RepeatedCompositeFieldContainer[ErrorSummary]
    transfer_job_name: str

    def __init__(self, name: _Optional[str]=..., project_id: _Optional[str]=..., transfer_spec: _Optional[_Union[TransferSpec, _Mapping]]=..., notification_config: _Optional[_Union[NotificationConfig, _Mapping]]=..., logging_config: _Optional[_Union[LoggingConfig, _Mapping]]=..., start_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]]=..., end_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]]=..., status: _Optional[_Union[TransferOperation.Status, str]]=..., counters: _Optional[_Union[TransferCounters, _Mapping]]=..., error_breakdowns: _Optional[_Iterable[_Union[ErrorSummary, _Mapping]]]=..., transfer_job_name: _Optional[str]=...) -> None:
        ...