from google.api import resource_pb2 as _resource_pb2
from google.devtools.resultstore.v2 import common_pb2 as _common_pb2
from google.protobuf import timestamp_pb2 as _timestamp_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Mapping as _Mapping, Optional as _Optional, Union as _Union
DESCRIPTOR: _descriptor.FileDescriptor

class DownloadMetadata(_message.Message):
    __slots__ = ('name', 'upload_status', 'create_time', 'finalize_time', 'immutable_time')
    NAME_FIELD_NUMBER: _ClassVar[int]
    UPLOAD_STATUS_FIELD_NUMBER: _ClassVar[int]
    CREATE_TIME_FIELD_NUMBER: _ClassVar[int]
    FINALIZE_TIME_FIELD_NUMBER: _ClassVar[int]
    IMMUTABLE_TIME_FIELD_NUMBER: _ClassVar[int]
    name: str
    upload_status: _common_pb2.UploadStatus
    create_time: _timestamp_pb2.Timestamp
    finalize_time: _timestamp_pb2.Timestamp
    immutable_time: _timestamp_pb2.Timestamp

    def __init__(self, name: _Optional[str]=..., upload_status: _Optional[_Union[_common_pb2.UploadStatus, str]]=..., create_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]]=..., finalize_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]]=..., immutable_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]]=...) -> None:
        ...