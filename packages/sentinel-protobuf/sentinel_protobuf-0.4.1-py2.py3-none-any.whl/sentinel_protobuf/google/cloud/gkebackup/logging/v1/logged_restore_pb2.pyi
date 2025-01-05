from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Mapping as _Mapping, Optional as _Optional, Union as _Union
DESCRIPTOR: _descriptor.FileDescriptor

class LoggedRestore(_message.Message):
    __slots__ = ('backup', 'labels', 'description', 'state', 'state_reason')

    class State(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        STATE_UNSPECIFIED: _ClassVar[LoggedRestore.State]
        CREATING: _ClassVar[LoggedRestore.State]
        IN_PROGRESS: _ClassVar[LoggedRestore.State]
        SUCCEEDED: _ClassVar[LoggedRestore.State]
        FAILED: _ClassVar[LoggedRestore.State]
        DELETING: _ClassVar[LoggedRestore.State]
    STATE_UNSPECIFIED: LoggedRestore.State
    CREATING: LoggedRestore.State
    IN_PROGRESS: LoggedRestore.State
    SUCCEEDED: LoggedRestore.State
    FAILED: LoggedRestore.State
    DELETING: LoggedRestore.State

    class LabelsEntry(_message.Message):
        __slots__ = ('key', 'value')
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: str

        def __init__(self, key: _Optional[str]=..., value: _Optional[str]=...) -> None:
            ...
    BACKUP_FIELD_NUMBER: _ClassVar[int]
    LABELS_FIELD_NUMBER: _ClassVar[int]
    DESCRIPTION_FIELD_NUMBER: _ClassVar[int]
    STATE_FIELD_NUMBER: _ClassVar[int]
    STATE_REASON_FIELD_NUMBER: _ClassVar[int]
    backup: str
    labels: _containers.ScalarMap[str, str]
    description: str
    state: LoggedRestore.State
    state_reason: str

    def __init__(self, backup: _Optional[str]=..., labels: _Optional[_Mapping[str, str]]=..., description: _Optional[str]=..., state: _Optional[_Union[LoggedRestore.State, str]]=..., state_reason: _Optional[str]=...) -> None:
        ...