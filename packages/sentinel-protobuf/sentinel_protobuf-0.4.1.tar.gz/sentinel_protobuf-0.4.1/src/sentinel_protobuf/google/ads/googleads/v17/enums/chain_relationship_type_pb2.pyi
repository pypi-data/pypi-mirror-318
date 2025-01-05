from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar
DESCRIPTOR: _descriptor.FileDescriptor

class ChainRelationshipTypeEnum(_message.Message):
    __slots__ = ()

    class ChainRelationshipType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        UNSPECIFIED: _ClassVar[ChainRelationshipTypeEnum.ChainRelationshipType]
        UNKNOWN: _ClassVar[ChainRelationshipTypeEnum.ChainRelationshipType]
        AUTO_DEALERS: _ClassVar[ChainRelationshipTypeEnum.ChainRelationshipType]
        GENERAL_RETAILERS: _ClassVar[ChainRelationshipTypeEnum.ChainRelationshipType]
    UNSPECIFIED: ChainRelationshipTypeEnum.ChainRelationshipType
    UNKNOWN: ChainRelationshipTypeEnum.ChainRelationshipType
    AUTO_DEALERS: ChainRelationshipTypeEnum.ChainRelationshipType
    GENERAL_RETAILERS: ChainRelationshipTypeEnum.ChainRelationshipType

    def __init__(self) -> None:
        ...