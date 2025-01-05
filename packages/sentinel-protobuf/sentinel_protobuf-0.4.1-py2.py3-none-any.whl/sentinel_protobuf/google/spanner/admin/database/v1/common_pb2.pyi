from google.api import field_behavior_pb2 as _field_behavior_pb2
from google.api import resource_pb2 as _resource_pb2
from google.protobuf import timestamp_pb2 as _timestamp_pb2
from google.rpc import status_pb2 as _status_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union
DESCRIPTOR: _descriptor.FileDescriptor

class DatabaseDialect(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    DATABASE_DIALECT_UNSPECIFIED: _ClassVar[DatabaseDialect]
    GOOGLE_STANDARD_SQL: _ClassVar[DatabaseDialect]
    POSTGRESQL: _ClassVar[DatabaseDialect]
DATABASE_DIALECT_UNSPECIFIED: DatabaseDialect
GOOGLE_STANDARD_SQL: DatabaseDialect
POSTGRESQL: DatabaseDialect

class OperationProgress(_message.Message):
    __slots__ = ('progress_percent', 'start_time', 'end_time')
    PROGRESS_PERCENT_FIELD_NUMBER: _ClassVar[int]
    START_TIME_FIELD_NUMBER: _ClassVar[int]
    END_TIME_FIELD_NUMBER: _ClassVar[int]
    progress_percent: int
    start_time: _timestamp_pb2.Timestamp
    end_time: _timestamp_pb2.Timestamp

    def __init__(self, progress_percent: _Optional[int]=..., start_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]]=..., end_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]]=...) -> None:
        ...

class EncryptionConfig(_message.Message):
    __slots__ = ('kms_key_name', 'kms_key_names')
    KMS_KEY_NAME_FIELD_NUMBER: _ClassVar[int]
    KMS_KEY_NAMES_FIELD_NUMBER: _ClassVar[int]
    kms_key_name: str
    kms_key_names: _containers.RepeatedScalarFieldContainer[str]

    def __init__(self, kms_key_name: _Optional[str]=..., kms_key_names: _Optional[_Iterable[str]]=...) -> None:
        ...

class EncryptionInfo(_message.Message):
    __slots__ = ('encryption_type', 'encryption_status', 'kms_key_version')

    class Type(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        TYPE_UNSPECIFIED: _ClassVar[EncryptionInfo.Type]
        GOOGLE_DEFAULT_ENCRYPTION: _ClassVar[EncryptionInfo.Type]
        CUSTOMER_MANAGED_ENCRYPTION: _ClassVar[EncryptionInfo.Type]
    TYPE_UNSPECIFIED: EncryptionInfo.Type
    GOOGLE_DEFAULT_ENCRYPTION: EncryptionInfo.Type
    CUSTOMER_MANAGED_ENCRYPTION: EncryptionInfo.Type
    ENCRYPTION_TYPE_FIELD_NUMBER: _ClassVar[int]
    ENCRYPTION_STATUS_FIELD_NUMBER: _ClassVar[int]
    KMS_KEY_VERSION_FIELD_NUMBER: _ClassVar[int]
    encryption_type: EncryptionInfo.Type
    encryption_status: _status_pb2.Status
    kms_key_version: str

    def __init__(self, encryption_type: _Optional[_Union[EncryptionInfo.Type, str]]=..., encryption_status: _Optional[_Union[_status_pb2.Status, _Mapping]]=..., kms_key_version: _Optional[str]=...) -> None:
        ...