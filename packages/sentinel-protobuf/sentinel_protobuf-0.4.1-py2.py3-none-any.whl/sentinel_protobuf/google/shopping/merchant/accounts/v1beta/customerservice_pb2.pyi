from google.api import field_behavior_pb2 as _field_behavior_pb2
from google.type import phone_number_pb2 as _phone_number_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class CustomerService(_message.Message):
    __slots__ = ("uri", "email", "phone")
    URI_FIELD_NUMBER: _ClassVar[int]
    EMAIL_FIELD_NUMBER: _ClassVar[int]
    PHONE_FIELD_NUMBER: _ClassVar[int]
    uri: str
    email: str
    phone: _phone_number_pb2.PhoneNumber
    def __init__(self, uri: _Optional[str] = ..., email: _Optional[str] = ..., phone: _Optional[_Union[_phone_number_pb2.PhoneNumber, _Mapping]] = ...) -> None: ...
