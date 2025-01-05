from google.api import field_behavior_pb2 as _field_behavior_pb2
from google.api import resource_pb2 as _resource_pb2
from google.protobuf import duration_pb2 as _duration_pb2
from google.protobuf import timestamp_pb2 as _timestamp_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union
DESCRIPTOR: _descriptor.FileDescriptor

class GenerateAccessTokenRequest(_message.Message):
    __slots__ = ('name', 'delegates', 'scope', 'lifetime')
    NAME_FIELD_NUMBER: _ClassVar[int]
    DELEGATES_FIELD_NUMBER: _ClassVar[int]
    SCOPE_FIELD_NUMBER: _ClassVar[int]
    LIFETIME_FIELD_NUMBER: _ClassVar[int]
    name: str
    delegates: _containers.RepeatedScalarFieldContainer[str]
    scope: _containers.RepeatedScalarFieldContainer[str]
    lifetime: _duration_pb2.Duration

    def __init__(self, name: _Optional[str]=..., delegates: _Optional[_Iterable[str]]=..., scope: _Optional[_Iterable[str]]=..., lifetime: _Optional[_Union[_duration_pb2.Duration, _Mapping]]=...) -> None:
        ...

class GenerateAccessTokenResponse(_message.Message):
    __slots__ = ('access_token', 'expire_time')
    ACCESS_TOKEN_FIELD_NUMBER: _ClassVar[int]
    EXPIRE_TIME_FIELD_NUMBER: _ClassVar[int]
    access_token: str
    expire_time: _timestamp_pb2.Timestamp

    def __init__(self, access_token: _Optional[str]=..., expire_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]]=...) -> None:
        ...

class SignBlobRequest(_message.Message):
    __slots__ = ('name', 'delegates', 'payload')
    NAME_FIELD_NUMBER: _ClassVar[int]
    DELEGATES_FIELD_NUMBER: _ClassVar[int]
    PAYLOAD_FIELD_NUMBER: _ClassVar[int]
    name: str
    delegates: _containers.RepeatedScalarFieldContainer[str]
    payload: bytes

    def __init__(self, name: _Optional[str]=..., delegates: _Optional[_Iterable[str]]=..., payload: _Optional[bytes]=...) -> None:
        ...

class SignBlobResponse(_message.Message):
    __slots__ = ('key_id', 'signed_blob')
    KEY_ID_FIELD_NUMBER: _ClassVar[int]
    SIGNED_BLOB_FIELD_NUMBER: _ClassVar[int]
    key_id: str
    signed_blob: bytes

    def __init__(self, key_id: _Optional[str]=..., signed_blob: _Optional[bytes]=...) -> None:
        ...

class SignJwtRequest(_message.Message):
    __slots__ = ('name', 'delegates', 'payload')
    NAME_FIELD_NUMBER: _ClassVar[int]
    DELEGATES_FIELD_NUMBER: _ClassVar[int]
    PAYLOAD_FIELD_NUMBER: _ClassVar[int]
    name: str
    delegates: _containers.RepeatedScalarFieldContainer[str]
    payload: str

    def __init__(self, name: _Optional[str]=..., delegates: _Optional[_Iterable[str]]=..., payload: _Optional[str]=...) -> None:
        ...

class SignJwtResponse(_message.Message):
    __slots__ = ('key_id', 'signed_jwt')
    KEY_ID_FIELD_NUMBER: _ClassVar[int]
    SIGNED_JWT_FIELD_NUMBER: _ClassVar[int]
    key_id: str
    signed_jwt: str

    def __init__(self, key_id: _Optional[str]=..., signed_jwt: _Optional[str]=...) -> None:
        ...

class GenerateIdTokenRequest(_message.Message):
    __slots__ = ('name', 'delegates', 'audience', 'include_email')
    NAME_FIELD_NUMBER: _ClassVar[int]
    DELEGATES_FIELD_NUMBER: _ClassVar[int]
    AUDIENCE_FIELD_NUMBER: _ClassVar[int]
    INCLUDE_EMAIL_FIELD_NUMBER: _ClassVar[int]
    name: str
    delegates: _containers.RepeatedScalarFieldContainer[str]
    audience: str
    include_email: bool

    def __init__(self, name: _Optional[str]=..., delegates: _Optional[_Iterable[str]]=..., audience: _Optional[str]=..., include_email: bool=...) -> None:
        ...

class GenerateIdTokenResponse(_message.Message):
    __slots__ = ('token',)
    TOKEN_FIELD_NUMBER: _ClassVar[int]
    token: str

    def __init__(self, token: _Optional[str]=...) -> None:
        ...