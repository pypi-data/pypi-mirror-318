from google.api import field_behavior_pb2 as _field_behavior_pb2
from google.protobuf import timestamp_pb2 as _timestamp_pb2
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Mapping as _Mapping, Optional as _Optional, Union as _Union
DESCRIPTOR: _descriptor.FileDescriptor

class StorageSystemType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    STORAGE_SYSTEM_TYPE_UNSPECIFIED: _ClassVar[StorageSystemType]
    AWS_S3: _ClassVar[StorageSystemType]
    AZURE_BLOB: _ClassVar[StorageSystemType]
    GCS: _ClassVar[StorageSystemType]
    POSIX_FS: _ClassVar[StorageSystemType]
    HTTP: _ClassVar[StorageSystemType]
STORAGE_SYSTEM_TYPE_UNSPECIFIED: StorageSystemType
AWS_S3: StorageSystemType
AZURE_BLOB: StorageSystemType
GCS: StorageSystemType
POSIX_FS: StorageSystemType
HTTP: StorageSystemType

class AwsS3ObjectMetadata(_message.Message):
    __slots__ = ('bucket', 'object_key', 'last_modified_time', 'md5', 'size')
    BUCKET_FIELD_NUMBER: _ClassVar[int]
    OBJECT_KEY_FIELD_NUMBER: _ClassVar[int]
    LAST_MODIFIED_TIME_FIELD_NUMBER: _ClassVar[int]
    MD5_FIELD_NUMBER: _ClassVar[int]
    SIZE_FIELD_NUMBER: _ClassVar[int]
    bucket: str
    object_key: str
    last_modified_time: _timestamp_pb2.Timestamp
    md5: str
    size: int

    def __init__(self, bucket: _Optional[str]=..., object_key: _Optional[str]=..., last_modified_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]]=..., md5: _Optional[str]=..., size: _Optional[int]=...) -> None:
        ...

class AwsS3BucketMetadata(_message.Message):
    __slots__ = ('bucket', 'path')
    BUCKET_FIELD_NUMBER: _ClassVar[int]
    PATH_FIELD_NUMBER: _ClassVar[int]
    bucket: str
    path: str

    def __init__(self, bucket: _Optional[str]=..., path: _Optional[str]=...) -> None:
        ...

class GcsObjectMetadata(_message.Message):
    __slots__ = ('bucket', 'object_key', 'last_modified_time', 'md5', 'crc32c', 'size')
    BUCKET_FIELD_NUMBER: _ClassVar[int]
    OBJECT_KEY_FIELD_NUMBER: _ClassVar[int]
    LAST_MODIFIED_TIME_FIELD_NUMBER: _ClassVar[int]
    MD5_FIELD_NUMBER: _ClassVar[int]
    CRC32C_FIELD_NUMBER: _ClassVar[int]
    SIZE_FIELD_NUMBER: _ClassVar[int]
    bucket: str
    object_key: str
    last_modified_time: _timestamp_pb2.Timestamp
    md5: str
    crc32c: str
    size: int

    def __init__(self, bucket: _Optional[str]=..., object_key: _Optional[str]=..., last_modified_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]]=..., md5: _Optional[str]=..., crc32c: _Optional[str]=..., size: _Optional[int]=...) -> None:
        ...

class GcsBucketMetadata(_message.Message):
    __slots__ = ('bucket', 'path')
    BUCKET_FIELD_NUMBER: _ClassVar[int]
    PATH_FIELD_NUMBER: _ClassVar[int]
    bucket: str
    path: str

    def __init__(self, bucket: _Optional[str]=..., path: _Optional[str]=...) -> None:
        ...

class AzureBlobMetadata(_message.Message):
    __slots__ = ('account', 'container', 'blob_name', 'last_modified_time', 'md5', 'size')
    ACCOUNT_FIELD_NUMBER: _ClassVar[int]
    CONTAINER_FIELD_NUMBER: _ClassVar[int]
    BLOB_NAME_FIELD_NUMBER: _ClassVar[int]
    LAST_MODIFIED_TIME_FIELD_NUMBER: _ClassVar[int]
    MD5_FIELD_NUMBER: _ClassVar[int]
    SIZE_FIELD_NUMBER: _ClassVar[int]
    account: str
    container: str
    blob_name: str
    last_modified_time: _timestamp_pb2.Timestamp
    md5: str
    size: int

    def __init__(self, account: _Optional[str]=..., container: _Optional[str]=..., blob_name: _Optional[str]=..., last_modified_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]]=..., md5: _Optional[str]=..., size: _Optional[int]=...) -> None:
        ...

class AzureBlobContainerMetadata(_message.Message):
    __slots__ = ('account', 'container', 'path')
    ACCOUNT_FIELD_NUMBER: _ClassVar[int]
    CONTAINER_FIELD_NUMBER: _ClassVar[int]
    PATH_FIELD_NUMBER: _ClassVar[int]
    account: str
    container: str
    path: str

    def __init__(self, account: _Optional[str]=..., container: _Optional[str]=..., path: _Optional[str]=...) -> None:
        ...

class PosixFileMetadata(_message.Message):
    __slots__ = ('path', 'last_modified_time', 'crc32c', 'size')
    PATH_FIELD_NUMBER: _ClassVar[int]
    LAST_MODIFIED_TIME_FIELD_NUMBER: _ClassVar[int]
    CRC32C_FIELD_NUMBER: _ClassVar[int]
    SIZE_FIELD_NUMBER: _ClassVar[int]
    path: str
    last_modified_time: _timestamp_pb2.Timestamp
    crc32c: str
    size: int

    def __init__(self, path: _Optional[str]=..., last_modified_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]]=..., crc32c: _Optional[str]=..., size: _Optional[int]=...) -> None:
        ...

class HttpFileMetadata(_message.Message):
    __slots__ = ('url', 'md5', 'size')
    URL_FIELD_NUMBER: _ClassVar[int]
    MD5_FIELD_NUMBER: _ClassVar[int]
    SIZE_FIELD_NUMBER: _ClassVar[int]
    url: str
    md5: str
    size: int

    def __init__(self, url: _Optional[str]=..., md5: _Optional[str]=..., size: _Optional[int]=...) -> None:
        ...

class HttpManifestMetadata(_message.Message):
    __slots__ = ('url',)
    URL_FIELD_NUMBER: _ClassVar[int]
    url: str

    def __init__(self, url: _Optional[str]=...) -> None:
        ...

class ObjectMetadata(_message.Message):
    __slots__ = ('type', 'aws_s3_object', 'azure_blob', 'gcs_object', 'posix_file', 'http_file')
    TYPE_FIELD_NUMBER: _ClassVar[int]
    AWS_S3_OBJECT_FIELD_NUMBER: _ClassVar[int]
    AZURE_BLOB_FIELD_NUMBER: _ClassVar[int]
    GCS_OBJECT_FIELD_NUMBER: _ClassVar[int]
    POSIX_FILE_FIELD_NUMBER: _ClassVar[int]
    HTTP_FILE_FIELD_NUMBER: _ClassVar[int]
    type: StorageSystemType
    aws_s3_object: AwsS3ObjectMetadata
    azure_blob: AzureBlobMetadata
    gcs_object: GcsObjectMetadata
    posix_file: PosixFileMetadata
    http_file: HttpFileMetadata

    def __init__(self, type: _Optional[_Union[StorageSystemType, str]]=..., aws_s3_object: _Optional[_Union[AwsS3ObjectMetadata, _Mapping]]=..., azure_blob: _Optional[_Union[AzureBlobMetadata, _Mapping]]=..., gcs_object: _Optional[_Union[GcsObjectMetadata, _Mapping]]=..., posix_file: _Optional[_Union[PosixFileMetadata, _Mapping]]=..., http_file: _Optional[_Union[HttpFileMetadata, _Mapping]]=...) -> None:
        ...

class ContainerMetadata(_message.Message):
    __slots__ = ('type', 'aws_s3_bucket', 'azure_blob_container', 'gcs_bucket', 'posix_directory', 'http_manifest')
    TYPE_FIELD_NUMBER: _ClassVar[int]
    AWS_S3_BUCKET_FIELD_NUMBER: _ClassVar[int]
    AZURE_BLOB_CONTAINER_FIELD_NUMBER: _ClassVar[int]
    GCS_BUCKET_FIELD_NUMBER: _ClassVar[int]
    POSIX_DIRECTORY_FIELD_NUMBER: _ClassVar[int]
    HTTP_MANIFEST_FIELD_NUMBER: _ClassVar[int]
    type: StorageSystemType
    aws_s3_bucket: AwsS3BucketMetadata
    azure_blob_container: AzureBlobContainerMetadata
    gcs_bucket: GcsBucketMetadata
    posix_directory: PosixFileMetadata
    http_manifest: HttpManifestMetadata

    def __init__(self, type: _Optional[_Union[StorageSystemType, str]]=..., aws_s3_bucket: _Optional[_Union[AwsS3BucketMetadata, _Mapping]]=..., azure_blob_container: _Optional[_Union[AzureBlobContainerMetadata, _Mapping]]=..., gcs_bucket: _Optional[_Union[GcsBucketMetadata, _Mapping]]=..., posix_directory: _Optional[_Union[PosixFileMetadata, _Mapping]]=..., http_manifest: _Optional[_Union[HttpManifestMetadata, _Mapping]]=...) -> None:
        ...

class TransferActivityLog(_message.Message):
    __slots__ = ('operation', 'action', 'status', 'source_container', 'destination_container', 'source_object', 'destination_object', 'complete_time')

    class Action(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        ACTION_UNSPECIFIED: _ClassVar[TransferActivityLog.Action]
        FIND: _ClassVar[TransferActivityLog.Action]
        COPY: _ClassVar[TransferActivityLog.Action]
        DELETE: _ClassVar[TransferActivityLog.Action]
    ACTION_UNSPECIFIED: TransferActivityLog.Action
    FIND: TransferActivityLog.Action
    COPY: TransferActivityLog.Action
    DELETE: TransferActivityLog.Action

    class Status(_message.Message):
        __slots__ = ('status_code', 'error_type', 'error_message')
        STATUS_CODE_FIELD_NUMBER: _ClassVar[int]
        ERROR_TYPE_FIELD_NUMBER: _ClassVar[int]
        ERROR_MESSAGE_FIELD_NUMBER: _ClassVar[int]
        status_code: str
        error_type: str
        error_message: str

        def __init__(self, status_code: _Optional[str]=..., error_type: _Optional[str]=..., error_message: _Optional[str]=...) -> None:
            ...
    OPERATION_FIELD_NUMBER: _ClassVar[int]
    ACTION_FIELD_NUMBER: _ClassVar[int]
    STATUS_FIELD_NUMBER: _ClassVar[int]
    SOURCE_CONTAINER_FIELD_NUMBER: _ClassVar[int]
    DESTINATION_CONTAINER_FIELD_NUMBER: _ClassVar[int]
    SOURCE_OBJECT_FIELD_NUMBER: _ClassVar[int]
    DESTINATION_OBJECT_FIELD_NUMBER: _ClassVar[int]
    COMPLETE_TIME_FIELD_NUMBER: _ClassVar[int]
    operation: str
    action: TransferActivityLog.Action
    status: TransferActivityLog.Status
    source_container: ContainerMetadata
    destination_container: ContainerMetadata
    source_object: ObjectMetadata
    destination_object: ObjectMetadata
    complete_time: _timestamp_pb2.Timestamp

    def __init__(self, operation: _Optional[str]=..., action: _Optional[_Union[TransferActivityLog.Action, str]]=..., status: _Optional[_Union[TransferActivityLog.Status, _Mapping]]=..., source_container: _Optional[_Union[ContainerMetadata, _Mapping]]=..., destination_container: _Optional[_Union[ContainerMetadata, _Mapping]]=..., source_object: _Optional[_Union[ObjectMetadata, _Mapping]]=..., destination_object: _Optional[_Union[ObjectMetadata, _Mapping]]=..., complete_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]]=...) -> None:
        ...