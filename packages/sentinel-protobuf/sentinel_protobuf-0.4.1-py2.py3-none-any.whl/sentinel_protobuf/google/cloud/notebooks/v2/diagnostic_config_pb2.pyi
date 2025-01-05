from google.api import field_behavior_pb2 as _field_behavior_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional
DESCRIPTOR: _descriptor.FileDescriptor

class DiagnosticConfig(_message.Message):
    __slots__ = ('gcs_bucket', 'relative_path', 'enable_repair_flag', 'enable_packet_capture_flag', 'enable_copy_home_files_flag')
    GCS_BUCKET_FIELD_NUMBER: _ClassVar[int]
    RELATIVE_PATH_FIELD_NUMBER: _ClassVar[int]
    ENABLE_REPAIR_FLAG_FIELD_NUMBER: _ClassVar[int]
    ENABLE_PACKET_CAPTURE_FLAG_FIELD_NUMBER: _ClassVar[int]
    ENABLE_COPY_HOME_FILES_FLAG_FIELD_NUMBER: _ClassVar[int]
    gcs_bucket: str
    relative_path: str
    enable_repair_flag: bool
    enable_packet_capture_flag: bool
    enable_copy_home_files_flag: bool

    def __init__(self, gcs_bucket: _Optional[str]=..., relative_path: _Optional[str]=..., enable_repair_flag: bool=..., enable_packet_capture_flag: bool=..., enable_copy_home_files_flag: bool=...) -> None:
        ...