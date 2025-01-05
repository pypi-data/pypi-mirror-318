from google.ads.googleads.v16.enums import matching_function_context_type_pb2 as _matching_function_context_type_pb2
from google.ads.googleads.v16.enums import matching_function_operator_pb2 as _matching_function_operator_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class MatchingFunction(_message.Message):
    __slots__ = ("function_string", "operator", "left_operands", "right_operands")
    FUNCTION_STRING_FIELD_NUMBER: _ClassVar[int]
    OPERATOR_FIELD_NUMBER: _ClassVar[int]
    LEFT_OPERANDS_FIELD_NUMBER: _ClassVar[int]
    RIGHT_OPERANDS_FIELD_NUMBER: _ClassVar[int]
    function_string: str
    operator: _matching_function_operator_pb2.MatchingFunctionOperatorEnum.MatchingFunctionOperator
    left_operands: _containers.RepeatedCompositeFieldContainer[Operand]
    right_operands: _containers.RepeatedCompositeFieldContainer[Operand]
    def __init__(self, function_string: _Optional[str] = ..., operator: _Optional[_Union[_matching_function_operator_pb2.MatchingFunctionOperatorEnum.MatchingFunctionOperator, str]] = ..., left_operands: _Optional[_Iterable[_Union[Operand, _Mapping]]] = ..., right_operands: _Optional[_Iterable[_Union[Operand, _Mapping]]] = ...) -> None: ...

class Operand(_message.Message):
    __slots__ = ("constant_operand", "feed_attribute_operand", "function_operand", "request_context_operand")
    class ConstantOperand(_message.Message):
        __slots__ = ("string_value", "long_value", "boolean_value", "double_value")
        STRING_VALUE_FIELD_NUMBER: _ClassVar[int]
        LONG_VALUE_FIELD_NUMBER: _ClassVar[int]
        BOOLEAN_VALUE_FIELD_NUMBER: _ClassVar[int]
        DOUBLE_VALUE_FIELD_NUMBER: _ClassVar[int]
        string_value: str
        long_value: int
        boolean_value: bool
        double_value: float
        def __init__(self, string_value: _Optional[str] = ..., long_value: _Optional[int] = ..., boolean_value: bool = ..., double_value: _Optional[float] = ...) -> None: ...
    class FeedAttributeOperand(_message.Message):
        __slots__ = ("feed_id", "feed_attribute_id")
        FEED_ID_FIELD_NUMBER: _ClassVar[int]
        FEED_ATTRIBUTE_ID_FIELD_NUMBER: _ClassVar[int]
        feed_id: int
        feed_attribute_id: int
        def __init__(self, feed_id: _Optional[int] = ..., feed_attribute_id: _Optional[int] = ...) -> None: ...
    class FunctionOperand(_message.Message):
        __slots__ = ("matching_function",)
        MATCHING_FUNCTION_FIELD_NUMBER: _ClassVar[int]
        matching_function: MatchingFunction
        def __init__(self, matching_function: _Optional[_Union[MatchingFunction, _Mapping]] = ...) -> None: ...
    class RequestContextOperand(_message.Message):
        __slots__ = ("context_type",)
        CONTEXT_TYPE_FIELD_NUMBER: _ClassVar[int]
        context_type: _matching_function_context_type_pb2.MatchingFunctionContextTypeEnum.MatchingFunctionContextType
        def __init__(self, context_type: _Optional[_Union[_matching_function_context_type_pb2.MatchingFunctionContextTypeEnum.MatchingFunctionContextType, str]] = ...) -> None: ...
    CONSTANT_OPERAND_FIELD_NUMBER: _ClassVar[int]
    FEED_ATTRIBUTE_OPERAND_FIELD_NUMBER: _ClassVar[int]
    FUNCTION_OPERAND_FIELD_NUMBER: _ClassVar[int]
    REQUEST_CONTEXT_OPERAND_FIELD_NUMBER: _ClassVar[int]
    constant_operand: Operand.ConstantOperand
    feed_attribute_operand: Operand.FeedAttributeOperand
    function_operand: Operand.FunctionOperand
    request_context_operand: Operand.RequestContextOperand
    def __init__(self, constant_operand: _Optional[_Union[Operand.ConstantOperand, _Mapping]] = ..., feed_attribute_operand: _Optional[_Union[Operand.FeedAttributeOperand, _Mapping]] = ..., function_operand: _Optional[_Union[Operand.FunctionOperand, _Mapping]] = ..., request_context_operand: _Optional[_Union[Operand.RequestContextOperand, _Mapping]] = ...) -> None: ...
