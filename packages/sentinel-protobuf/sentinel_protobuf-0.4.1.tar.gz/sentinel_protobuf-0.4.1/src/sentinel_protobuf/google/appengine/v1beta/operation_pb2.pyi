from google.protobuf import timestamp_pb2 as _timestamp_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union
DESCRIPTOR: _descriptor.FileDescriptor

class OperationMetadataV1Beta(_message.Message):
    __slots__ = ('method', 'insert_time', 'end_time', 'user', 'target', 'ephemeral_message', 'warning', 'create_version_metadata')
    METHOD_FIELD_NUMBER: _ClassVar[int]
    INSERT_TIME_FIELD_NUMBER: _ClassVar[int]
    END_TIME_FIELD_NUMBER: _ClassVar[int]
    USER_FIELD_NUMBER: _ClassVar[int]
    TARGET_FIELD_NUMBER: _ClassVar[int]
    EPHEMERAL_MESSAGE_FIELD_NUMBER: _ClassVar[int]
    WARNING_FIELD_NUMBER: _ClassVar[int]
    CREATE_VERSION_METADATA_FIELD_NUMBER: _ClassVar[int]
    method: str
    insert_time: _timestamp_pb2.Timestamp
    end_time: _timestamp_pb2.Timestamp
    user: str
    target: str
    ephemeral_message: str
    warning: _containers.RepeatedScalarFieldContainer[str]
    create_version_metadata: CreateVersionMetadataV1Beta

    def __init__(self, method: _Optional[str]=..., insert_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]]=..., end_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]]=..., user: _Optional[str]=..., target: _Optional[str]=..., ephemeral_message: _Optional[str]=..., warning: _Optional[_Iterable[str]]=..., create_version_metadata: _Optional[_Union[CreateVersionMetadataV1Beta, _Mapping]]=...) -> None:
        ...

class CreateVersionMetadataV1Beta(_message.Message):
    __slots__ = ('cloud_build_id',)
    CLOUD_BUILD_ID_FIELD_NUMBER: _ClassVar[int]
    cloud_build_id: str

    def __init__(self, cloud_build_id: _Optional[str]=...) -> None:
        ...