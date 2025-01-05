from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar
DESCRIPTOR: _descriptor.FileDescriptor

class ValueRuleOperationEnum(_message.Message):
    __slots__ = ()

    class ValueRuleOperation(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        UNSPECIFIED: _ClassVar[ValueRuleOperationEnum.ValueRuleOperation]
        UNKNOWN: _ClassVar[ValueRuleOperationEnum.ValueRuleOperation]
        ADD: _ClassVar[ValueRuleOperationEnum.ValueRuleOperation]
        MULTIPLY: _ClassVar[ValueRuleOperationEnum.ValueRuleOperation]
        SET: _ClassVar[ValueRuleOperationEnum.ValueRuleOperation]
    UNSPECIFIED: ValueRuleOperationEnum.ValueRuleOperation
    UNKNOWN: ValueRuleOperationEnum.ValueRuleOperation
    ADD: ValueRuleOperationEnum.ValueRuleOperation
    MULTIPLY: ValueRuleOperationEnum.ValueRuleOperation
    SET: ValueRuleOperationEnum.ValueRuleOperation

    def __init__(self) -> None:
        ...