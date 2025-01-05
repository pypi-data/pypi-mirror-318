from google.api import field_behavior_pb2 as _field_behavior_pb2
from google.api import resource_pb2 as _resource_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional
DESCRIPTOR: _descriptor.FileDescriptor

class GcsReportLogMessage(_message.Message):
    __slots__ = ('severity', 'category', 'file_path', 'filename', 'source_script_line', 'source_script_column', 'message', 'script_context', 'action', 'effect', 'object_name')
    SEVERITY_FIELD_NUMBER: _ClassVar[int]
    CATEGORY_FIELD_NUMBER: _ClassVar[int]
    FILE_PATH_FIELD_NUMBER: _ClassVar[int]
    FILENAME_FIELD_NUMBER: _ClassVar[int]
    SOURCE_SCRIPT_LINE_FIELD_NUMBER: _ClassVar[int]
    SOURCE_SCRIPT_COLUMN_FIELD_NUMBER: _ClassVar[int]
    MESSAGE_FIELD_NUMBER: _ClassVar[int]
    SCRIPT_CONTEXT_FIELD_NUMBER: _ClassVar[int]
    ACTION_FIELD_NUMBER: _ClassVar[int]
    EFFECT_FIELD_NUMBER: _ClassVar[int]
    OBJECT_NAME_FIELD_NUMBER: _ClassVar[int]
    severity: str
    category: str
    file_path: str
    filename: str
    source_script_line: int
    source_script_column: int
    message: str
    script_context: str
    action: str
    effect: str
    object_name: str

    def __init__(self, severity: _Optional[str]=..., category: _Optional[str]=..., file_path: _Optional[str]=..., filename: _Optional[str]=..., source_script_line: _Optional[int]=..., source_script_column: _Optional[int]=..., message: _Optional[str]=..., script_context: _Optional[str]=..., action: _Optional[str]=..., effect: _Optional[str]=..., object_name: _Optional[str]=...) -> None:
        ...