from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar
DESCRIPTOR: _descriptor.FileDescriptor

class AdCustomizerPlaceholderFieldEnum(_message.Message):
    __slots__ = ()

    class AdCustomizerPlaceholderField(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        UNSPECIFIED: _ClassVar[AdCustomizerPlaceholderFieldEnum.AdCustomizerPlaceholderField]
        UNKNOWN: _ClassVar[AdCustomizerPlaceholderFieldEnum.AdCustomizerPlaceholderField]
        INTEGER: _ClassVar[AdCustomizerPlaceholderFieldEnum.AdCustomizerPlaceholderField]
        PRICE: _ClassVar[AdCustomizerPlaceholderFieldEnum.AdCustomizerPlaceholderField]
        DATE: _ClassVar[AdCustomizerPlaceholderFieldEnum.AdCustomizerPlaceholderField]
        STRING: _ClassVar[AdCustomizerPlaceholderFieldEnum.AdCustomizerPlaceholderField]
    UNSPECIFIED: AdCustomizerPlaceholderFieldEnum.AdCustomizerPlaceholderField
    UNKNOWN: AdCustomizerPlaceholderFieldEnum.AdCustomizerPlaceholderField
    INTEGER: AdCustomizerPlaceholderFieldEnum.AdCustomizerPlaceholderField
    PRICE: AdCustomizerPlaceholderFieldEnum.AdCustomizerPlaceholderField
    DATE: AdCustomizerPlaceholderFieldEnum.AdCustomizerPlaceholderField
    STRING: AdCustomizerPlaceholderFieldEnum.AdCustomizerPlaceholderField

    def __init__(self) -> None:
        ...