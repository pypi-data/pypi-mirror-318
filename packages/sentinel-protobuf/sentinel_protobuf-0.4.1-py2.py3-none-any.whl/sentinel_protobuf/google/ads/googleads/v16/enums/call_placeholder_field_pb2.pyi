from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar
DESCRIPTOR: _descriptor.FileDescriptor

class CallPlaceholderFieldEnum(_message.Message):
    __slots__ = ()

    class CallPlaceholderField(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        UNSPECIFIED: _ClassVar[CallPlaceholderFieldEnum.CallPlaceholderField]
        UNKNOWN: _ClassVar[CallPlaceholderFieldEnum.CallPlaceholderField]
        PHONE_NUMBER: _ClassVar[CallPlaceholderFieldEnum.CallPlaceholderField]
        COUNTRY_CODE: _ClassVar[CallPlaceholderFieldEnum.CallPlaceholderField]
        TRACKED: _ClassVar[CallPlaceholderFieldEnum.CallPlaceholderField]
        CONVERSION_TYPE_ID: _ClassVar[CallPlaceholderFieldEnum.CallPlaceholderField]
        CONVERSION_REPORTING_STATE: _ClassVar[CallPlaceholderFieldEnum.CallPlaceholderField]
    UNSPECIFIED: CallPlaceholderFieldEnum.CallPlaceholderField
    UNKNOWN: CallPlaceholderFieldEnum.CallPlaceholderField
    PHONE_NUMBER: CallPlaceholderFieldEnum.CallPlaceholderField
    COUNTRY_CODE: CallPlaceholderFieldEnum.CallPlaceholderField
    TRACKED: CallPlaceholderFieldEnum.CallPlaceholderField
    CONVERSION_TYPE_ID: CallPlaceholderFieldEnum.CallPlaceholderField
    CONVERSION_REPORTING_STATE: CallPlaceholderFieldEnum.CallPlaceholderField

    def __init__(self) -> None:
        ...