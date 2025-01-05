from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Mapping as _Mapping, Optional as _Optional, Union as _Union
DESCRIPTOR: _descriptor.FileDescriptor

class MigrationState(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    MIGRATION_STATE_UNSPECIFIED: _ClassVar[MigrationState]
    RUNNING: _ClassVar[MigrationState]
    PAUSED: _ClassVar[MigrationState]
    COMPLETE: _ClassVar[MigrationState]

class MigrationStep(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    MIGRATION_STEP_UNSPECIFIED: _ClassVar[MigrationStep]
    PREPARE: _ClassVar[MigrationStep]
    START: _ClassVar[MigrationStep]
    APPLY_WRITES_SYNCHRONOUSLY: _ClassVar[MigrationStep]
    COPY_AND_VERIFY: _ClassVar[MigrationStep]
    REDIRECT_EVENTUALLY_CONSISTENT_READS: _ClassVar[MigrationStep]
    REDIRECT_STRONGLY_CONSISTENT_READS: _ClassVar[MigrationStep]
    REDIRECT_WRITES: _ClassVar[MigrationStep]
MIGRATION_STATE_UNSPECIFIED: MigrationState
RUNNING: MigrationState
PAUSED: MigrationState
COMPLETE: MigrationState
MIGRATION_STEP_UNSPECIFIED: MigrationStep
PREPARE: MigrationStep
START: MigrationStep
APPLY_WRITES_SYNCHRONOUSLY: MigrationStep
COPY_AND_VERIFY: MigrationStep
REDIRECT_EVENTUALLY_CONSISTENT_READS: MigrationStep
REDIRECT_STRONGLY_CONSISTENT_READS: MigrationStep
REDIRECT_WRITES: MigrationStep

class MigrationStateEvent(_message.Message):
    __slots__ = ('state',)
    STATE_FIELD_NUMBER: _ClassVar[int]
    state: MigrationState

    def __init__(self, state: _Optional[_Union[MigrationState, str]]=...) -> None:
        ...

class MigrationProgressEvent(_message.Message):
    __slots__ = ('step', 'prepare_step_details', 'redirect_writes_step_details')

    class ConcurrencyMode(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        CONCURRENCY_MODE_UNSPECIFIED: _ClassVar[MigrationProgressEvent.ConcurrencyMode]
        PESSIMISTIC: _ClassVar[MigrationProgressEvent.ConcurrencyMode]
        OPTIMISTIC: _ClassVar[MigrationProgressEvent.ConcurrencyMode]
        OPTIMISTIC_WITH_ENTITY_GROUPS: _ClassVar[MigrationProgressEvent.ConcurrencyMode]
    CONCURRENCY_MODE_UNSPECIFIED: MigrationProgressEvent.ConcurrencyMode
    PESSIMISTIC: MigrationProgressEvent.ConcurrencyMode
    OPTIMISTIC: MigrationProgressEvent.ConcurrencyMode
    OPTIMISTIC_WITH_ENTITY_GROUPS: MigrationProgressEvent.ConcurrencyMode

    class PrepareStepDetails(_message.Message):
        __slots__ = ('concurrency_mode',)
        CONCURRENCY_MODE_FIELD_NUMBER: _ClassVar[int]
        concurrency_mode: MigrationProgressEvent.ConcurrencyMode

        def __init__(self, concurrency_mode: _Optional[_Union[MigrationProgressEvent.ConcurrencyMode, str]]=...) -> None:
            ...

    class RedirectWritesStepDetails(_message.Message):
        __slots__ = ('concurrency_mode',)
        CONCURRENCY_MODE_FIELD_NUMBER: _ClassVar[int]
        concurrency_mode: MigrationProgressEvent.ConcurrencyMode

        def __init__(self, concurrency_mode: _Optional[_Union[MigrationProgressEvent.ConcurrencyMode, str]]=...) -> None:
            ...
    STEP_FIELD_NUMBER: _ClassVar[int]
    PREPARE_STEP_DETAILS_FIELD_NUMBER: _ClassVar[int]
    REDIRECT_WRITES_STEP_DETAILS_FIELD_NUMBER: _ClassVar[int]
    step: MigrationStep
    prepare_step_details: MigrationProgressEvent.PrepareStepDetails
    redirect_writes_step_details: MigrationProgressEvent.RedirectWritesStepDetails

    def __init__(self, step: _Optional[_Union[MigrationStep, str]]=..., prepare_step_details: _Optional[_Union[MigrationProgressEvent.PrepareStepDetails, _Mapping]]=..., redirect_writes_step_details: _Optional[_Union[MigrationProgressEvent.RedirectWritesStepDetails, _Mapping]]=...) -> None:
        ...