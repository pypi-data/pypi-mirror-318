from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar
DESCRIPTOR: _descriptor.FileDescriptor

class CalloutPlaceholderFieldEnum(_message.Message):
    __slots__ = ()

    class CalloutPlaceholderField(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        UNSPECIFIED: _ClassVar[CalloutPlaceholderFieldEnum.CalloutPlaceholderField]
        UNKNOWN: _ClassVar[CalloutPlaceholderFieldEnum.CalloutPlaceholderField]
        CALLOUT_TEXT: _ClassVar[CalloutPlaceholderFieldEnum.CalloutPlaceholderField]
    UNSPECIFIED: CalloutPlaceholderFieldEnum.CalloutPlaceholderField
    UNKNOWN: CalloutPlaceholderFieldEnum.CalloutPlaceholderField
    CALLOUT_TEXT: CalloutPlaceholderFieldEnum.CalloutPlaceholderField

    def __init__(self) -> None:
        ...