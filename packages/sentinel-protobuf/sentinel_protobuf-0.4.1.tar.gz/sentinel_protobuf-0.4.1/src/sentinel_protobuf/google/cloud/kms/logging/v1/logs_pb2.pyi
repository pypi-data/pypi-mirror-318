from google.rpc import status_pb2 as _status_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Mapping as _Mapping, Optional as _Optional, Union as _Union
DESCRIPTOR: _descriptor.FileDescriptor

class CryptoKeyEvent(_message.Message):
    __slots__ = ('rotation_event',)

    class RotationEvent(_message.Message):
        __slots__ = ('status',)
        STATUS_FIELD_NUMBER: _ClassVar[int]
        status: _status_pb2.Status

        def __init__(self, status: _Optional[_Union[_status_pb2.Status, _Mapping]]=...) -> None:
            ...
    ROTATION_EVENT_FIELD_NUMBER: _ClassVar[int]
    rotation_event: CryptoKeyEvent.RotationEvent

    def __init__(self, rotation_event: _Optional[_Union[CryptoKeyEvent.RotationEvent, _Mapping]]=...) -> None:
        ...

class CryptoKeyVersionEvent(_message.Message):
    __slots__ = ('scheduled_destruction_event', 'key_generation_event', 'import_event')

    class ScheduledDestructionEvent(_message.Message):
        __slots__ = ('status', 'key_access_justification_reason')
        STATUS_FIELD_NUMBER: _ClassVar[int]
        KEY_ACCESS_JUSTIFICATION_REASON_FIELD_NUMBER: _ClassVar[int]
        status: _status_pb2.Status
        key_access_justification_reason: str

        def __init__(self, status: _Optional[_Union[_status_pb2.Status, _Mapping]]=..., key_access_justification_reason: _Optional[str]=...) -> None:
            ...

    class KeyGenerationEvent(_message.Message):
        __slots__ = ('status', 'key_access_justification_reason')
        STATUS_FIELD_NUMBER: _ClassVar[int]
        KEY_ACCESS_JUSTIFICATION_REASON_FIELD_NUMBER: _ClassVar[int]
        status: _status_pb2.Status
        key_access_justification_reason: str

        def __init__(self, status: _Optional[_Union[_status_pb2.Status, _Mapping]]=..., key_access_justification_reason: _Optional[str]=...) -> None:
            ...

    class ImportEvent(_message.Message):
        __slots__ = ('status',)
        STATUS_FIELD_NUMBER: _ClassVar[int]
        status: _status_pb2.Status

        def __init__(self, status: _Optional[_Union[_status_pb2.Status, _Mapping]]=...) -> None:
            ...
    SCHEDULED_DESTRUCTION_EVENT_FIELD_NUMBER: _ClassVar[int]
    KEY_GENERATION_EVENT_FIELD_NUMBER: _ClassVar[int]
    IMPORT_EVENT_FIELD_NUMBER: _ClassVar[int]
    scheduled_destruction_event: CryptoKeyVersionEvent.ScheduledDestructionEvent
    key_generation_event: CryptoKeyVersionEvent.KeyGenerationEvent
    import_event: CryptoKeyVersionEvent.ImportEvent

    def __init__(self, scheduled_destruction_event: _Optional[_Union[CryptoKeyVersionEvent.ScheduledDestructionEvent, _Mapping]]=..., key_generation_event: _Optional[_Union[CryptoKeyVersionEvent.KeyGenerationEvent, _Mapping]]=..., import_event: _Optional[_Union[CryptoKeyVersionEvent.ImportEvent, _Mapping]]=...) -> None:
        ...