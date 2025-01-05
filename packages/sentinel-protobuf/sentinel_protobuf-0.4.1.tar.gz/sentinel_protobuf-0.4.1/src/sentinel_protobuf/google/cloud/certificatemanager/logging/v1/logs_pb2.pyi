from google.protobuf import timestamp_pb2 as _timestamp_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union
DESCRIPTOR: _descriptor.FileDescriptor

class CertificatesExpiry(_message.Message):
    __slots__ = ('count', 'certificates', 'state', 'expire_time')

    class State(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        STATE_UNSPECIFIED: _ClassVar[CertificatesExpiry.State]
        CLOSE_TO_EXPIRY: _ClassVar[CertificatesExpiry.State]
        EXPIRED: _ClassVar[CertificatesExpiry.State]
    STATE_UNSPECIFIED: CertificatesExpiry.State
    CLOSE_TO_EXPIRY: CertificatesExpiry.State
    EXPIRED: CertificatesExpiry.State
    COUNT_FIELD_NUMBER: _ClassVar[int]
    CERTIFICATES_FIELD_NUMBER: _ClassVar[int]
    STATE_FIELD_NUMBER: _ClassVar[int]
    EXPIRE_TIME_FIELD_NUMBER: _ClassVar[int]
    count: int
    certificates: _containers.RepeatedScalarFieldContainer[str]
    state: CertificatesExpiry.State
    expire_time: _timestamp_pb2.Timestamp

    def __init__(self, count: _Optional[int]=..., certificates: _Optional[_Iterable[str]]=..., state: _Optional[_Union[CertificatesExpiry.State, str]]=..., expire_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]]=...) -> None:
        ...