from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar
DESCRIPTOR: _descriptor.FileDescriptor

class WebpageConditionOperandEnum(_message.Message):
    __slots__ = ()

    class WebpageConditionOperand(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        UNSPECIFIED: _ClassVar[WebpageConditionOperandEnum.WebpageConditionOperand]
        UNKNOWN: _ClassVar[WebpageConditionOperandEnum.WebpageConditionOperand]
        URL: _ClassVar[WebpageConditionOperandEnum.WebpageConditionOperand]
        CATEGORY: _ClassVar[WebpageConditionOperandEnum.WebpageConditionOperand]
        PAGE_TITLE: _ClassVar[WebpageConditionOperandEnum.WebpageConditionOperand]
        PAGE_CONTENT: _ClassVar[WebpageConditionOperandEnum.WebpageConditionOperand]
        CUSTOM_LABEL: _ClassVar[WebpageConditionOperandEnum.WebpageConditionOperand]
    UNSPECIFIED: WebpageConditionOperandEnum.WebpageConditionOperand
    UNKNOWN: WebpageConditionOperandEnum.WebpageConditionOperand
    URL: WebpageConditionOperandEnum.WebpageConditionOperand
    CATEGORY: WebpageConditionOperandEnum.WebpageConditionOperand
    PAGE_TITLE: WebpageConditionOperandEnum.WebpageConditionOperand
    PAGE_CONTENT: WebpageConditionOperandEnum.WebpageConditionOperand
    CUSTOM_LABEL: WebpageConditionOperandEnum.WebpageConditionOperand

    def __init__(self) -> None:
        ...