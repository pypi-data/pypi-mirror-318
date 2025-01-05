from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional
DESCRIPTOR: _descriptor.FileDescriptor

class InstanceConfig(_message.Message):
    __slots__ = ('notebook_upgrade_schedule', 'enable_health_monitoring')
    NOTEBOOK_UPGRADE_SCHEDULE_FIELD_NUMBER: _ClassVar[int]
    ENABLE_HEALTH_MONITORING_FIELD_NUMBER: _ClassVar[int]
    notebook_upgrade_schedule: str
    enable_health_monitoring: bool

    def __init__(self, notebook_upgrade_schedule: _Optional[str]=..., enable_health_monitoring: bool=...) -> None:
        ...