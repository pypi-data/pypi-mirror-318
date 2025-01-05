from google.api import field_behavior_pb2 as _field_behavior_pb2
from google.api import resource_pb2 as _resource_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional
DESCRIPTOR: _descriptor.FileDescriptor

class ExternalAccountKey(_message.Message):
    __slots__ = ('name', 'key_id', 'b64_mac_key')
    NAME_FIELD_NUMBER: _ClassVar[int]
    KEY_ID_FIELD_NUMBER: _ClassVar[int]
    B64_MAC_KEY_FIELD_NUMBER: _ClassVar[int]
    name: str
    key_id: str
    b64_mac_key: bytes

    def __init__(self, name: _Optional[str]=..., key_id: _Optional[str]=..., b64_mac_key: _Optional[bytes]=...) -> None:
        ...