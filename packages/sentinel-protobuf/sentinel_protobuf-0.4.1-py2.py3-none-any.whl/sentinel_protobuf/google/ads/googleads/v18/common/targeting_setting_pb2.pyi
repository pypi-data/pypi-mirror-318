from google.ads.googleads.v18.enums import targeting_dimension_pb2 as _targeting_dimension_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class TargetingSetting(_message.Message):
    __slots__ = ("target_restrictions", "target_restriction_operations")
    TARGET_RESTRICTIONS_FIELD_NUMBER: _ClassVar[int]
    TARGET_RESTRICTION_OPERATIONS_FIELD_NUMBER: _ClassVar[int]
    target_restrictions: _containers.RepeatedCompositeFieldContainer[TargetRestriction]
    target_restriction_operations: _containers.RepeatedCompositeFieldContainer[TargetRestrictionOperation]
    def __init__(self, target_restrictions: _Optional[_Iterable[_Union[TargetRestriction, _Mapping]]] = ..., target_restriction_operations: _Optional[_Iterable[_Union[TargetRestrictionOperation, _Mapping]]] = ...) -> None: ...

class TargetRestriction(_message.Message):
    __slots__ = ("targeting_dimension", "bid_only")
    TARGETING_DIMENSION_FIELD_NUMBER: _ClassVar[int]
    BID_ONLY_FIELD_NUMBER: _ClassVar[int]
    targeting_dimension: _targeting_dimension_pb2.TargetingDimensionEnum.TargetingDimension
    bid_only: bool
    def __init__(self, targeting_dimension: _Optional[_Union[_targeting_dimension_pb2.TargetingDimensionEnum.TargetingDimension, str]] = ..., bid_only: bool = ...) -> None: ...

class TargetRestrictionOperation(_message.Message):
    __slots__ = ("operator", "value")
    class Operator(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        UNSPECIFIED: _ClassVar[TargetRestrictionOperation.Operator]
        UNKNOWN: _ClassVar[TargetRestrictionOperation.Operator]
        ADD: _ClassVar[TargetRestrictionOperation.Operator]
        REMOVE: _ClassVar[TargetRestrictionOperation.Operator]
    UNSPECIFIED: TargetRestrictionOperation.Operator
    UNKNOWN: TargetRestrictionOperation.Operator
    ADD: TargetRestrictionOperation.Operator
    REMOVE: TargetRestrictionOperation.Operator
    OPERATOR_FIELD_NUMBER: _ClassVar[int]
    VALUE_FIELD_NUMBER: _ClassVar[int]
    operator: TargetRestrictionOperation.Operator
    value: TargetRestriction
    def __init__(self, operator: _Optional[_Union[TargetRestrictionOperation.Operator, str]] = ..., value: _Optional[_Union[TargetRestriction, _Mapping]] = ...) -> None: ...
