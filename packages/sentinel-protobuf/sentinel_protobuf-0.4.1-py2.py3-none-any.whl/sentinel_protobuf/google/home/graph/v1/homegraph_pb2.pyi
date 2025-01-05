from google.api import annotations_pb2 as _annotations_pb2
from google.api import client_pb2 as _client_pb2
from google.api import field_behavior_pb2 as _field_behavior_pb2
from google.api import resource_pb2 as _resource_pb2
from google.home.graph.v1 import device_pb2 as _device_pb2
from google.protobuf import empty_pb2 as _empty_pb2
from google.protobuf import struct_pb2 as _struct_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union
DESCRIPTOR: _descriptor.FileDescriptor

class RequestSyncDevicesRequest(_message.Message):
    __slots__ = ('agent_user_id',)
    AGENT_USER_ID_FIELD_NUMBER: _ClassVar[int]
    ASYNC_FIELD_NUMBER: _ClassVar[int]
    agent_user_id: str

    def __init__(self, agent_user_id: _Optional[str]=..., **kwargs) -> None:
        ...

class RequestSyncDevicesResponse(_message.Message):
    __slots__ = ()

    def __init__(self) -> None:
        ...

class ReportStateAndNotificationRequest(_message.Message):
    __slots__ = ('request_id', 'event_id', 'agent_user_id', 'follow_up_token', 'payload')
    REQUEST_ID_FIELD_NUMBER: _ClassVar[int]
    EVENT_ID_FIELD_NUMBER: _ClassVar[int]
    AGENT_USER_ID_FIELD_NUMBER: _ClassVar[int]
    FOLLOW_UP_TOKEN_FIELD_NUMBER: _ClassVar[int]
    PAYLOAD_FIELD_NUMBER: _ClassVar[int]
    request_id: str
    event_id: str
    agent_user_id: str
    follow_up_token: str
    payload: StateAndNotificationPayload

    def __init__(self, request_id: _Optional[str]=..., event_id: _Optional[str]=..., agent_user_id: _Optional[str]=..., follow_up_token: _Optional[str]=..., payload: _Optional[_Union[StateAndNotificationPayload, _Mapping]]=...) -> None:
        ...

class ReportStateAndNotificationResponse(_message.Message):
    __slots__ = ('request_id',)
    REQUEST_ID_FIELD_NUMBER: _ClassVar[int]
    request_id: str

    def __init__(self, request_id: _Optional[str]=...) -> None:
        ...

class StateAndNotificationPayload(_message.Message):
    __slots__ = ('devices',)
    DEVICES_FIELD_NUMBER: _ClassVar[int]
    devices: ReportStateAndNotificationDevice

    def __init__(self, devices: _Optional[_Union[ReportStateAndNotificationDevice, _Mapping]]=...) -> None:
        ...

class ReportStateAndNotificationDevice(_message.Message):
    __slots__ = ('states', 'notifications')
    STATES_FIELD_NUMBER: _ClassVar[int]
    NOTIFICATIONS_FIELD_NUMBER: _ClassVar[int]
    states: _struct_pb2.Struct
    notifications: _struct_pb2.Struct

    def __init__(self, states: _Optional[_Union[_struct_pb2.Struct, _Mapping]]=..., notifications: _Optional[_Union[_struct_pb2.Struct, _Mapping]]=...) -> None:
        ...

class DeleteAgentUserRequest(_message.Message):
    __slots__ = ('request_id', 'agent_user_id')
    REQUEST_ID_FIELD_NUMBER: _ClassVar[int]
    AGENT_USER_ID_FIELD_NUMBER: _ClassVar[int]
    request_id: str
    agent_user_id: str

    def __init__(self, request_id: _Optional[str]=..., agent_user_id: _Optional[str]=...) -> None:
        ...

class QueryRequest(_message.Message):
    __slots__ = ('request_id', 'agent_user_id', 'inputs')
    REQUEST_ID_FIELD_NUMBER: _ClassVar[int]
    AGENT_USER_ID_FIELD_NUMBER: _ClassVar[int]
    INPUTS_FIELD_NUMBER: _ClassVar[int]
    request_id: str
    agent_user_id: str
    inputs: _containers.RepeatedCompositeFieldContainer[QueryRequestInput]

    def __init__(self, request_id: _Optional[str]=..., agent_user_id: _Optional[str]=..., inputs: _Optional[_Iterable[_Union[QueryRequestInput, _Mapping]]]=...) -> None:
        ...

class QueryRequestInput(_message.Message):
    __slots__ = ('payload',)
    PAYLOAD_FIELD_NUMBER: _ClassVar[int]
    payload: QueryRequestPayload

    def __init__(self, payload: _Optional[_Union[QueryRequestPayload, _Mapping]]=...) -> None:
        ...

class QueryRequestPayload(_message.Message):
    __slots__ = ('devices',)
    DEVICES_FIELD_NUMBER: _ClassVar[int]
    devices: _containers.RepeatedCompositeFieldContainer[AgentDeviceId]

    def __init__(self, devices: _Optional[_Iterable[_Union[AgentDeviceId, _Mapping]]]=...) -> None:
        ...

class AgentDeviceId(_message.Message):
    __slots__ = ('id',)
    ID_FIELD_NUMBER: _ClassVar[int]
    id: str

    def __init__(self, id: _Optional[str]=...) -> None:
        ...

class QueryResponse(_message.Message):
    __slots__ = ('request_id', 'payload')
    REQUEST_ID_FIELD_NUMBER: _ClassVar[int]
    PAYLOAD_FIELD_NUMBER: _ClassVar[int]
    request_id: str
    payload: QueryResponsePayload

    def __init__(self, request_id: _Optional[str]=..., payload: _Optional[_Union[QueryResponsePayload, _Mapping]]=...) -> None:
        ...

class QueryResponsePayload(_message.Message):
    __slots__ = ('devices',)

    class DevicesEntry(_message.Message):
        __slots__ = ('key', 'value')
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: _struct_pb2.Struct

        def __init__(self, key: _Optional[str]=..., value: _Optional[_Union[_struct_pb2.Struct, _Mapping]]=...) -> None:
            ...
    DEVICES_FIELD_NUMBER: _ClassVar[int]
    devices: _containers.MessageMap[str, _struct_pb2.Struct]

    def __init__(self, devices: _Optional[_Mapping[str, _struct_pb2.Struct]]=...) -> None:
        ...

class SyncRequest(_message.Message):
    __slots__ = ('request_id', 'agent_user_id')
    REQUEST_ID_FIELD_NUMBER: _ClassVar[int]
    AGENT_USER_ID_FIELD_NUMBER: _ClassVar[int]
    request_id: str
    agent_user_id: str

    def __init__(self, request_id: _Optional[str]=..., agent_user_id: _Optional[str]=...) -> None:
        ...

class SyncResponse(_message.Message):
    __slots__ = ('request_id', 'payload')
    REQUEST_ID_FIELD_NUMBER: _ClassVar[int]
    PAYLOAD_FIELD_NUMBER: _ClassVar[int]
    request_id: str
    payload: SyncResponsePayload

    def __init__(self, request_id: _Optional[str]=..., payload: _Optional[_Union[SyncResponsePayload, _Mapping]]=...) -> None:
        ...

class SyncResponsePayload(_message.Message):
    __slots__ = ('agent_user_id', 'devices')
    AGENT_USER_ID_FIELD_NUMBER: _ClassVar[int]
    DEVICES_FIELD_NUMBER: _ClassVar[int]
    agent_user_id: str
    devices: _containers.RepeatedCompositeFieldContainer[_device_pb2.Device]

    def __init__(self, agent_user_id: _Optional[str]=..., devices: _Optional[_Iterable[_Union[_device_pb2.Device, _Mapping]]]=...) -> None:
        ...