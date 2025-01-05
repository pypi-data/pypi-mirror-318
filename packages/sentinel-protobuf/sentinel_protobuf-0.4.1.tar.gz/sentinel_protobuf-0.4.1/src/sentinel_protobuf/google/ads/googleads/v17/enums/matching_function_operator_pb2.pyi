from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar
DESCRIPTOR: _descriptor.FileDescriptor

class MatchingFunctionOperatorEnum(_message.Message):
    __slots__ = ()

    class MatchingFunctionOperator(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        UNSPECIFIED: _ClassVar[MatchingFunctionOperatorEnum.MatchingFunctionOperator]
        UNKNOWN: _ClassVar[MatchingFunctionOperatorEnum.MatchingFunctionOperator]
        IN: _ClassVar[MatchingFunctionOperatorEnum.MatchingFunctionOperator]
        IDENTITY: _ClassVar[MatchingFunctionOperatorEnum.MatchingFunctionOperator]
        EQUALS: _ClassVar[MatchingFunctionOperatorEnum.MatchingFunctionOperator]
        AND: _ClassVar[MatchingFunctionOperatorEnum.MatchingFunctionOperator]
        CONTAINS_ANY: _ClassVar[MatchingFunctionOperatorEnum.MatchingFunctionOperator]
    UNSPECIFIED: MatchingFunctionOperatorEnum.MatchingFunctionOperator
    UNKNOWN: MatchingFunctionOperatorEnum.MatchingFunctionOperator
    IN: MatchingFunctionOperatorEnum.MatchingFunctionOperator
    IDENTITY: MatchingFunctionOperatorEnum.MatchingFunctionOperator
    EQUALS: MatchingFunctionOperatorEnum.MatchingFunctionOperator
    AND: MatchingFunctionOperatorEnum.MatchingFunctionOperator
    CONTAINS_ANY: MatchingFunctionOperatorEnum.MatchingFunctionOperator

    def __init__(self) -> None:
        ...