from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union
DESCRIPTOR: _descriptor.FileDescriptor

class ExportStatusLog(_message.Message):
    __slots__ = ('export_date', 'status', 'event_count', 'message')

    class Status(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        UNKNOWN: _ClassVar[ExportStatusLog.Status]
        COMPLETE: _ClassVar[ExportStatusLog.Status]
        INCOMPLETE: _ClassVar[ExportStatusLog.Status]
        FAILED: _ClassVar[ExportStatusLog.Status]
    UNKNOWN: ExportStatusLog.Status
    COMPLETE: ExportStatusLog.Status
    INCOMPLETE: ExportStatusLog.Status
    FAILED: ExportStatusLog.Status
    EXPORT_DATE_FIELD_NUMBER: _ClassVar[int]
    STATUS_FIELD_NUMBER: _ClassVar[int]
    EVENT_COUNT_FIELD_NUMBER: _ClassVar[int]
    MESSAGE_FIELD_NUMBER: _ClassVar[int]
    export_date: str
    status: ExportStatusLog.Status
    event_count: int
    message: str

    def __init__(self, export_date: _Optional[str]=..., status: _Optional[_Union[ExportStatusLog.Status, str]]=..., event_count: _Optional[int]=..., message: _Optional[str]=...) -> None:
        ...