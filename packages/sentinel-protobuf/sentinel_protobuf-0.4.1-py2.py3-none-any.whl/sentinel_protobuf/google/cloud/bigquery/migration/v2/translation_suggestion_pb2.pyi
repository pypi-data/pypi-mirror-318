from google.api import field_behavior_pb2 as _field_behavior_pb2
from google.api import resource_pb2 as _resource_pb2
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union
DESCRIPTOR: _descriptor.FileDescriptor

class TranslationReportRecord(_message.Message):
    __slots__ = ('severity', 'script_line', 'script_column', 'category', 'message')

    class Severity(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        SEVERITY_UNSPECIFIED: _ClassVar[TranslationReportRecord.Severity]
        INFO: _ClassVar[TranslationReportRecord.Severity]
        WARNING: _ClassVar[TranslationReportRecord.Severity]
        ERROR: _ClassVar[TranslationReportRecord.Severity]
    SEVERITY_UNSPECIFIED: TranslationReportRecord.Severity
    INFO: TranslationReportRecord.Severity
    WARNING: TranslationReportRecord.Severity
    ERROR: TranslationReportRecord.Severity
    SEVERITY_FIELD_NUMBER: _ClassVar[int]
    SCRIPT_LINE_FIELD_NUMBER: _ClassVar[int]
    SCRIPT_COLUMN_FIELD_NUMBER: _ClassVar[int]
    CATEGORY_FIELD_NUMBER: _ClassVar[int]
    MESSAGE_FIELD_NUMBER: _ClassVar[int]
    severity: TranslationReportRecord.Severity
    script_line: int
    script_column: int
    category: str
    message: str

    def __init__(self, severity: _Optional[_Union[TranslationReportRecord.Severity, str]]=..., script_line: _Optional[int]=..., script_column: _Optional[int]=..., category: _Optional[str]=..., message: _Optional[str]=...) -> None:
        ...