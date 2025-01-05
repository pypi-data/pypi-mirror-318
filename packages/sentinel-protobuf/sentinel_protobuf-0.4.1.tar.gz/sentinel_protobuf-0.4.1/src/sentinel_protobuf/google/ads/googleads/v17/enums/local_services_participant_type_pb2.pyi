from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar
DESCRIPTOR: _descriptor.FileDescriptor

class LocalServicesParticipantTypeEnum(_message.Message):
    __slots__ = ()

    class ParticipantType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        UNSPECIFIED: _ClassVar[LocalServicesParticipantTypeEnum.ParticipantType]
        UNKNOWN: _ClassVar[LocalServicesParticipantTypeEnum.ParticipantType]
        ADVERTISER: _ClassVar[LocalServicesParticipantTypeEnum.ParticipantType]
        CONSUMER: _ClassVar[LocalServicesParticipantTypeEnum.ParticipantType]
    UNSPECIFIED: LocalServicesParticipantTypeEnum.ParticipantType
    UNKNOWN: LocalServicesParticipantTypeEnum.ParticipantType
    ADVERTISER: LocalServicesParticipantTypeEnum.ParticipantType
    CONSUMER: LocalServicesParticipantTypeEnum.ParticipantType

    def __init__(self) -> None:
        ...