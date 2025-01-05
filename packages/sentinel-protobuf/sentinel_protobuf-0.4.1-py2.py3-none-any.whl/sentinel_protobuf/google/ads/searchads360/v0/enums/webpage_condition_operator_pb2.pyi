from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar
DESCRIPTOR: _descriptor.FileDescriptor

class WebpageConditionOperatorEnum(_message.Message):
    __slots__ = ()

    class WebpageConditionOperator(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        UNSPECIFIED: _ClassVar[WebpageConditionOperatorEnum.WebpageConditionOperator]
        UNKNOWN: _ClassVar[WebpageConditionOperatorEnum.WebpageConditionOperator]
        EQUALS: _ClassVar[WebpageConditionOperatorEnum.WebpageConditionOperator]
        CONTAINS: _ClassVar[WebpageConditionOperatorEnum.WebpageConditionOperator]
    UNSPECIFIED: WebpageConditionOperatorEnum.WebpageConditionOperator
    UNKNOWN: WebpageConditionOperatorEnum.WebpageConditionOperator
    EQUALS: WebpageConditionOperatorEnum.WebpageConditionOperator
    CONTAINS: WebpageConditionOperatorEnum.WebpageConditionOperator

    def __init__(self) -> None:
        ...