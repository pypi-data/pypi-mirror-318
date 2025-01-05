from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar
DESCRIPTOR: _descriptor.FileDescriptor

class AndroidPrivacyInteractionTypeEnum(_message.Message):
    __slots__ = ()

    class AndroidPrivacyInteractionType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        UNSPECIFIED: _ClassVar[AndroidPrivacyInteractionTypeEnum.AndroidPrivacyInteractionType]
        UNKNOWN: _ClassVar[AndroidPrivacyInteractionTypeEnum.AndroidPrivacyInteractionType]
        CLICK: _ClassVar[AndroidPrivacyInteractionTypeEnum.AndroidPrivacyInteractionType]
        ENGAGED_VIEW: _ClassVar[AndroidPrivacyInteractionTypeEnum.AndroidPrivacyInteractionType]
        VIEW: _ClassVar[AndroidPrivacyInteractionTypeEnum.AndroidPrivacyInteractionType]
    UNSPECIFIED: AndroidPrivacyInteractionTypeEnum.AndroidPrivacyInteractionType
    UNKNOWN: AndroidPrivacyInteractionTypeEnum.AndroidPrivacyInteractionType
    CLICK: AndroidPrivacyInteractionTypeEnum.AndroidPrivacyInteractionType
    ENGAGED_VIEW: AndroidPrivacyInteractionTypeEnum.AndroidPrivacyInteractionType
    VIEW: AndroidPrivacyInteractionTypeEnum.AndroidPrivacyInteractionType

    def __init__(self) -> None:
        ...