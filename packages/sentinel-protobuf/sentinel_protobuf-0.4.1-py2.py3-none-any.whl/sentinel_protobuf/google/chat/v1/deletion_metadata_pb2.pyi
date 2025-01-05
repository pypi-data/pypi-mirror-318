from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union
DESCRIPTOR: _descriptor.FileDescriptor

class DeletionMetadata(_message.Message):
    __slots__ = ('deletion_type',)

    class DeletionType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        DELETION_TYPE_UNSPECIFIED: _ClassVar[DeletionMetadata.DeletionType]
        CREATOR: _ClassVar[DeletionMetadata.DeletionType]
        SPACE_OWNER: _ClassVar[DeletionMetadata.DeletionType]
        ADMIN: _ClassVar[DeletionMetadata.DeletionType]
        APP_MESSAGE_EXPIRY: _ClassVar[DeletionMetadata.DeletionType]
        CREATOR_VIA_APP: _ClassVar[DeletionMetadata.DeletionType]
        SPACE_OWNER_VIA_APP: _ClassVar[DeletionMetadata.DeletionType]
    DELETION_TYPE_UNSPECIFIED: DeletionMetadata.DeletionType
    CREATOR: DeletionMetadata.DeletionType
    SPACE_OWNER: DeletionMetadata.DeletionType
    ADMIN: DeletionMetadata.DeletionType
    APP_MESSAGE_EXPIRY: DeletionMetadata.DeletionType
    CREATOR_VIA_APP: DeletionMetadata.DeletionType
    SPACE_OWNER_VIA_APP: DeletionMetadata.DeletionType
    DELETION_TYPE_FIELD_NUMBER: _ClassVar[int]
    deletion_type: DeletionMetadata.DeletionType

    def __init__(self, deletion_type: _Optional[_Union[DeletionMetadata.DeletionType, str]]=...) -> None:
        ...