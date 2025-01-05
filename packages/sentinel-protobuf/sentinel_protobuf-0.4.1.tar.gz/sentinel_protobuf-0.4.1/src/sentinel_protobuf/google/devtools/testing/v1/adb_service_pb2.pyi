from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Mapping as _Mapping, Optional as _Optional, Union as _Union
DESCRIPTOR: _descriptor.FileDescriptor

class DeviceMessage(_message.Message):
    __slots__ = ('status_update', 'stream_status', 'stream_data')
    STATUS_UPDATE_FIELD_NUMBER: _ClassVar[int]
    STREAM_STATUS_FIELD_NUMBER: _ClassVar[int]
    STREAM_DATA_FIELD_NUMBER: _ClassVar[int]
    status_update: StatusUpdate
    stream_status: StreamStatus
    stream_data: StreamData

    def __init__(self, status_update: _Optional[_Union[StatusUpdate, _Mapping]]=..., stream_status: _Optional[_Union[StreamStatus, _Mapping]]=..., stream_data: _Optional[_Union[StreamData, _Mapping]]=...) -> None:
        ...

class AdbMessage(_message.Message):
    __slots__ = ('open', 'stream_data')
    OPEN_FIELD_NUMBER: _ClassVar[int]
    STREAM_DATA_FIELD_NUMBER: _ClassVar[int]
    open: Open
    stream_data: StreamData

    def __init__(self, open: _Optional[_Union[Open, _Mapping]]=..., stream_data: _Optional[_Union[StreamData, _Mapping]]=...) -> None:
        ...

class StatusUpdate(_message.Message):
    __slots__ = ('state', 'properties', 'features')

    class DeviceState(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        DEVICE_STATE_UNSPECIFIED: _ClassVar[StatusUpdate.DeviceState]
        DEVICE: _ClassVar[StatusUpdate.DeviceState]
        RECOVERY: _ClassVar[StatusUpdate.DeviceState]
        RESCUE: _ClassVar[StatusUpdate.DeviceState]
        SIDELOAD: _ClassVar[StatusUpdate.DeviceState]
        MISSING: _ClassVar[StatusUpdate.DeviceState]
        OFFLINE: _ClassVar[StatusUpdate.DeviceState]
        UNAUTHORIZED: _ClassVar[StatusUpdate.DeviceState]
        AUTHORIZING: _ClassVar[StatusUpdate.DeviceState]
        CONNECTING: _ClassVar[StatusUpdate.DeviceState]
    DEVICE_STATE_UNSPECIFIED: StatusUpdate.DeviceState
    DEVICE: StatusUpdate.DeviceState
    RECOVERY: StatusUpdate.DeviceState
    RESCUE: StatusUpdate.DeviceState
    SIDELOAD: StatusUpdate.DeviceState
    MISSING: StatusUpdate.DeviceState
    OFFLINE: StatusUpdate.DeviceState
    UNAUTHORIZED: StatusUpdate.DeviceState
    AUTHORIZING: StatusUpdate.DeviceState
    CONNECTING: StatusUpdate.DeviceState

    class PropertiesEntry(_message.Message):
        __slots__ = ('key', 'value')
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: str

        def __init__(self, key: _Optional[str]=..., value: _Optional[str]=...) -> None:
            ...
    STATE_FIELD_NUMBER: _ClassVar[int]
    PROPERTIES_FIELD_NUMBER: _ClassVar[int]
    FEATURES_FIELD_NUMBER: _ClassVar[int]
    state: StatusUpdate.DeviceState
    properties: _containers.ScalarMap[str, str]
    features: str

    def __init__(self, state: _Optional[_Union[StatusUpdate.DeviceState, str]]=..., properties: _Optional[_Mapping[str, str]]=..., features: _Optional[str]=...) -> None:
        ...

class StreamStatus(_message.Message):
    __slots__ = ('stream_id', 'okay', 'fail')
    STREAM_ID_FIELD_NUMBER: _ClassVar[int]
    OKAY_FIELD_NUMBER: _ClassVar[int]
    FAIL_FIELD_NUMBER: _ClassVar[int]
    stream_id: int
    okay: Okay
    fail: Fail

    def __init__(self, stream_id: _Optional[int]=..., okay: _Optional[_Union[Okay, _Mapping]]=..., fail: _Optional[_Union[Fail, _Mapping]]=...) -> None:
        ...

class Open(_message.Message):
    __slots__ = ('stream_id', 'service')
    STREAM_ID_FIELD_NUMBER: _ClassVar[int]
    SERVICE_FIELD_NUMBER: _ClassVar[int]
    stream_id: int
    service: str

    def __init__(self, stream_id: _Optional[int]=..., service: _Optional[str]=...) -> None:
        ...

class StreamData(_message.Message):
    __slots__ = ('stream_id', 'data', 'close')
    STREAM_ID_FIELD_NUMBER: _ClassVar[int]
    DATA_FIELD_NUMBER: _ClassVar[int]
    CLOSE_FIELD_NUMBER: _ClassVar[int]
    stream_id: int
    data: bytes
    close: Close

    def __init__(self, stream_id: _Optional[int]=..., data: _Optional[bytes]=..., close: _Optional[_Union[Close, _Mapping]]=...) -> None:
        ...

class Okay(_message.Message):
    __slots__ = ()

    def __init__(self) -> None:
        ...

class Fail(_message.Message):
    __slots__ = ('reason',)
    REASON_FIELD_NUMBER: _ClassVar[int]
    reason: str

    def __init__(self, reason: _Optional[str]=...) -> None:
        ...

class Close(_message.Message):
    __slots__ = ()

    def __init__(self) -> None:
        ...