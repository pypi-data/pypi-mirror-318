from google.api import field_behavior_pb2 as _field_behavior_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional
DESCRIPTOR: _descriptor.FileDescriptor

class EncryptionSpec(_message.Message):
    __slots__ = ('kms_key_name',)
    KMS_KEY_NAME_FIELD_NUMBER: _ClassVar[int]
    kms_key_name: str

    def __init__(self, kms_key_name: _Optional[str]=...) -> None:
        ...