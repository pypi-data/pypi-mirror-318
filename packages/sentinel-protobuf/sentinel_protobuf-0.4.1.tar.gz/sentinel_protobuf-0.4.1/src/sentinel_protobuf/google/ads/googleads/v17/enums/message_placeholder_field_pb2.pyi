from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar
DESCRIPTOR: _descriptor.FileDescriptor

class MessagePlaceholderFieldEnum(_message.Message):
    __slots__ = ()

    class MessagePlaceholderField(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        UNSPECIFIED: _ClassVar[MessagePlaceholderFieldEnum.MessagePlaceholderField]
        UNKNOWN: _ClassVar[MessagePlaceholderFieldEnum.MessagePlaceholderField]
        BUSINESS_NAME: _ClassVar[MessagePlaceholderFieldEnum.MessagePlaceholderField]
        COUNTRY_CODE: _ClassVar[MessagePlaceholderFieldEnum.MessagePlaceholderField]
        PHONE_NUMBER: _ClassVar[MessagePlaceholderFieldEnum.MessagePlaceholderField]
        MESSAGE_EXTENSION_TEXT: _ClassVar[MessagePlaceholderFieldEnum.MessagePlaceholderField]
        MESSAGE_TEXT: _ClassVar[MessagePlaceholderFieldEnum.MessagePlaceholderField]
    UNSPECIFIED: MessagePlaceholderFieldEnum.MessagePlaceholderField
    UNKNOWN: MessagePlaceholderFieldEnum.MessagePlaceholderField
    BUSINESS_NAME: MessagePlaceholderFieldEnum.MessagePlaceholderField
    COUNTRY_CODE: MessagePlaceholderFieldEnum.MessagePlaceholderField
    PHONE_NUMBER: MessagePlaceholderFieldEnum.MessagePlaceholderField
    MESSAGE_EXTENSION_TEXT: MessagePlaceholderFieldEnum.MessagePlaceholderField
    MESSAGE_TEXT: MessagePlaceholderFieldEnum.MessagePlaceholderField

    def __init__(self) -> None:
        ...