from google.api import field_behavior_pb2 as _field_behavior_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional
DESCRIPTOR: _descriptor.FileDescriptor

class DiagnosticConfig(_message.Message):
    __slots__ = ('gcs_bucket', 'relative_path', 'repair_flag_enabled', 'packet_capture_flag_enabled', 'copy_home_files_flag_enabled')
    GCS_BUCKET_FIELD_NUMBER: _ClassVar[int]
    RELATIVE_PATH_FIELD_NUMBER: _ClassVar[int]
    REPAIR_FLAG_ENABLED_FIELD_NUMBER: _ClassVar[int]
    PACKET_CAPTURE_FLAG_ENABLED_FIELD_NUMBER: _ClassVar[int]
    COPY_HOME_FILES_FLAG_ENABLED_FIELD_NUMBER: _ClassVar[int]
    gcs_bucket: str
    relative_path: str
    repair_flag_enabled: bool
    packet_capture_flag_enabled: bool
    copy_home_files_flag_enabled: bool

    def __init__(self, gcs_bucket: _Optional[str]=..., relative_path: _Optional[str]=..., repair_flag_enabled: bool=..., packet_capture_flag_enabled: bool=..., copy_home_files_flag_enabled: bool=...) -> None:
        ...