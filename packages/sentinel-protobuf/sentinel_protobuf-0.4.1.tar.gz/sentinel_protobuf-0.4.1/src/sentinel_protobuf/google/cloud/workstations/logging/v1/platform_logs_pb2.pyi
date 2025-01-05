from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Mapping as _Mapping, Optional as _Optional, Union as _Union
DESCRIPTOR: _descriptor.FileDescriptor

class WorkstationEvent(_message.Message):
    __slots__ = ('vm_assignment_event', 'disk_assignment_event')
    VM_ASSIGNMENT_EVENT_FIELD_NUMBER: _ClassVar[int]
    DISK_ASSIGNMENT_EVENT_FIELD_NUMBER: _ClassVar[int]
    vm_assignment_event: VmAssignmentEvent
    disk_assignment_event: DiskAssignmentEvent

    def __init__(self, vm_assignment_event: _Optional[_Union[VmAssignmentEvent, _Mapping]]=..., disk_assignment_event: _Optional[_Union[DiskAssignmentEvent, _Mapping]]=...) -> None:
        ...

class VmAssignmentEvent(_message.Message):
    __slots__ = ('vm',)
    VM_FIELD_NUMBER: _ClassVar[int]
    vm: str

    def __init__(self, vm: _Optional[str]=...) -> None:
        ...

class DiskAssignmentEvent(_message.Message):
    __slots__ = ('disk',)
    DISK_FIELD_NUMBER: _ClassVar[int]
    disk: str

    def __init__(self, disk: _Optional[str]=...) -> None:
        ...