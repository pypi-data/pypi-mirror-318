from google.api import field_info_pb2 as _field_info_pb2
from google.protobuf import timestamp_pb2 as _timestamp_pb2
from google.rpc import status_pb2 as _status_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Mapping as _Mapping, Optional as _Optional, Union as _Union
DESCRIPTOR: _descriptor.FileDescriptor

class GoogleApiSourceActivity(_message.Message):
    __slots__ = ('message_uid', 'attributes', 'activity_time', 'published')

    class Published(_message.Message):
        __slots__ = ('message_bus', 'event_provider', 'details', 'error')
        MESSAGE_BUS_FIELD_NUMBER: _ClassVar[int]
        EVENT_PROVIDER_FIELD_NUMBER: _ClassVar[int]
        DETAILS_FIELD_NUMBER: _ClassVar[int]
        ERROR_FIELD_NUMBER: _ClassVar[int]
        message_bus: str
        event_provider: str
        details: str
        error: _status_pb2.Status

        def __init__(self, message_bus: _Optional[str]=..., event_provider: _Optional[str]=..., details: _Optional[str]=..., error: _Optional[_Union[_status_pb2.Status, _Mapping]]=...) -> None:
            ...

    class AttributesEntry(_message.Message):
        __slots__ = ('key', 'value')
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: str

        def __init__(self, key: _Optional[str]=..., value: _Optional[str]=...) -> None:
            ...
    MESSAGE_UID_FIELD_NUMBER: _ClassVar[int]
    ATTRIBUTES_FIELD_NUMBER: _ClassVar[int]
    ACTIVITY_TIME_FIELD_NUMBER: _ClassVar[int]
    PUBLISHED_FIELD_NUMBER: _ClassVar[int]
    message_uid: str
    attributes: _containers.ScalarMap[str, str]
    activity_time: _timestamp_pb2.Timestamp
    published: GoogleApiSourceActivity.Published

    def __init__(self, message_uid: _Optional[str]=..., attributes: _Optional[_Mapping[str, str]]=..., activity_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]]=..., published: _Optional[_Union[GoogleApiSourceActivity.Published, _Mapping]]=...) -> None:
        ...