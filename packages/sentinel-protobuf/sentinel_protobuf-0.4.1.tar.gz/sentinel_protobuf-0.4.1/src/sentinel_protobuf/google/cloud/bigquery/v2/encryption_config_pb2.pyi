from google.api import field_behavior_pb2 as _field_behavior_pb2
from google.protobuf import wrappers_pb2 as _wrappers_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Mapping as _Mapping, Optional as _Optional, Union as _Union
DESCRIPTOR: _descriptor.FileDescriptor

class EncryptionConfiguration(_message.Message):
    __slots__ = ('kms_key_name',)
    KMS_KEY_NAME_FIELD_NUMBER: _ClassVar[int]
    kms_key_name: _wrappers_pb2.StringValue

    def __init__(self, kms_key_name: _Optional[_Union[_wrappers_pb2.StringValue, _Mapping]]=...) -> None:
        ...