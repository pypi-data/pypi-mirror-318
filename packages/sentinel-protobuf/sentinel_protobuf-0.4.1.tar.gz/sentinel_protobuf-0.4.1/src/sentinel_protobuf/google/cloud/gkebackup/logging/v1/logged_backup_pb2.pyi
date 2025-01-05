from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Mapping as _Mapping, Optional as _Optional, Union as _Union
DESCRIPTOR: _descriptor.FileDescriptor

class LoggedBackup(_message.Message):
    __slots__ = ('labels', 'delete_lock_days', 'retain_days', 'description', 'state', 'state_reason')

    class State(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        STATE_UNSPECIFIED: _ClassVar[LoggedBackup.State]
        CREATING: _ClassVar[LoggedBackup.State]
        IN_PROGRESS: _ClassVar[LoggedBackup.State]
        SUCCEEDED: _ClassVar[LoggedBackup.State]
        FAILED: _ClassVar[LoggedBackup.State]
        DELETING: _ClassVar[LoggedBackup.State]
    STATE_UNSPECIFIED: LoggedBackup.State
    CREATING: LoggedBackup.State
    IN_PROGRESS: LoggedBackup.State
    SUCCEEDED: LoggedBackup.State
    FAILED: LoggedBackup.State
    DELETING: LoggedBackup.State

    class LabelsEntry(_message.Message):
        __slots__ = ('key', 'value')
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: str

        def __init__(self, key: _Optional[str]=..., value: _Optional[str]=...) -> None:
            ...
    LABELS_FIELD_NUMBER: _ClassVar[int]
    DELETE_LOCK_DAYS_FIELD_NUMBER: _ClassVar[int]
    RETAIN_DAYS_FIELD_NUMBER: _ClassVar[int]
    DESCRIPTION_FIELD_NUMBER: _ClassVar[int]
    STATE_FIELD_NUMBER: _ClassVar[int]
    STATE_REASON_FIELD_NUMBER: _ClassVar[int]
    labels: _containers.ScalarMap[str, str]
    delete_lock_days: int
    retain_days: int
    description: str
    state: LoggedBackup.State
    state_reason: str

    def __init__(self, labels: _Optional[_Mapping[str, str]]=..., delete_lock_days: _Optional[int]=..., retain_days: _Optional[int]=..., description: _Optional[str]=..., state: _Optional[_Union[LoggedBackup.State, str]]=..., state_reason: _Optional[str]=...) -> None:
        ...