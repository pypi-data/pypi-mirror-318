from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional
DESCRIPTOR: _descriptor.FileDescriptor

class Event(_message.Message):
    __slots__ = ('event_time', 'srcid', 'error_message', 'event_id', 'component', 'appliance_name', 'app_name', 'app_type', 'job_name')
    EVENT_TIME_FIELD_NUMBER: _ClassVar[int]
    SRCID_FIELD_NUMBER: _ClassVar[int]
    ERROR_MESSAGE_FIELD_NUMBER: _ClassVar[int]
    EVENT_ID_FIELD_NUMBER: _ClassVar[int]
    COMPONENT_FIELD_NUMBER: _ClassVar[int]
    APPLIANCE_NAME_FIELD_NUMBER: _ClassVar[int]
    APP_NAME_FIELD_NUMBER: _ClassVar[int]
    APP_TYPE_FIELD_NUMBER: _ClassVar[int]
    JOB_NAME_FIELD_NUMBER: _ClassVar[int]
    event_time: str
    srcid: int
    error_message: str
    event_id: int
    component: str
    appliance_name: int
    app_name: str
    app_type: str
    job_name: str

    def __init__(self, event_time: _Optional[str]=..., srcid: _Optional[int]=..., error_message: _Optional[str]=..., event_id: _Optional[int]=..., component: _Optional[str]=..., appliance_name: _Optional[int]=..., app_name: _Optional[str]=..., app_type: _Optional[str]=..., job_name: _Optional[str]=...) -> None:
        ...