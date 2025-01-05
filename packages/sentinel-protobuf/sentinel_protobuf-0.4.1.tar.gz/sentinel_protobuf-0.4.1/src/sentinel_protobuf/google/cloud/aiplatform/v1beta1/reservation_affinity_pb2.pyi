from google.api import field_behavior_pb2 as _field_behavior_pb2
from google.api import resource_pb2 as _resource_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Optional as _Optional, Union as _Union
DESCRIPTOR: _descriptor.FileDescriptor

class ReservationAffinity(_message.Message):
    __slots__ = ('reservation_affinity_type', 'key', 'values')

    class Type(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        TYPE_UNSPECIFIED: _ClassVar[ReservationAffinity.Type]
        NO_RESERVATION: _ClassVar[ReservationAffinity.Type]
        ANY_RESERVATION: _ClassVar[ReservationAffinity.Type]
        SPECIFIC_RESERVATION: _ClassVar[ReservationAffinity.Type]
    TYPE_UNSPECIFIED: ReservationAffinity.Type
    NO_RESERVATION: ReservationAffinity.Type
    ANY_RESERVATION: ReservationAffinity.Type
    SPECIFIC_RESERVATION: ReservationAffinity.Type
    RESERVATION_AFFINITY_TYPE_FIELD_NUMBER: _ClassVar[int]
    KEY_FIELD_NUMBER: _ClassVar[int]
    VALUES_FIELD_NUMBER: _ClassVar[int]
    reservation_affinity_type: ReservationAffinity.Type
    key: str
    values: _containers.RepeatedScalarFieldContainer[str]

    def __init__(self, reservation_affinity_type: _Optional[_Union[ReservationAffinity.Type, str]]=..., key: _Optional[str]=..., values: _Optional[_Iterable[str]]=...) -> None:
        ...