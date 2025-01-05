from google.api import field_behavior_pb2 as _field_behavior_pb2
from google.api import resource_pb2 as _resource_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional
DESCRIPTOR: _descriptor.FileDescriptor

class UserCapabilities(_message.Message):
    __slots__ = ('name', 'can_access_label_manager', 'can_administrate_labels', 'can_create_shared_labels', 'can_create_admin_labels')
    NAME_FIELD_NUMBER: _ClassVar[int]
    CAN_ACCESS_LABEL_MANAGER_FIELD_NUMBER: _ClassVar[int]
    CAN_ADMINISTRATE_LABELS_FIELD_NUMBER: _ClassVar[int]
    CAN_CREATE_SHARED_LABELS_FIELD_NUMBER: _ClassVar[int]
    CAN_CREATE_ADMIN_LABELS_FIELD_NUMBER: _ClassVar[int]
    name: str
    can_access_label_manager: bool
    can_administrate_labels: bool
    can_create_shared_labels: bool
    can_create_admin_labels: bool

    def __init__(self, name: _Optional[str]=..., can_access_label_manager: bool=..., can_administrate_labels: bool=..., can_create_shared_labels: bool=..., can_create_admin_labels: bool=...) -> None:
        ...