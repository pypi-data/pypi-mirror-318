from google.api import field_behavior_pb2 as _field_behavior_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class AggregationThresholdPolicy(_message.Message):
    __slots__ = ("threshold", "privacy_unit_columns")
    THRESHOLD_FIELD_NUMBER: _ClassVar[int]
    PRIVACY_UNIT_COLUMNS_FIELD_NUMBER: _ClassVar[int]
    threshold: int
    privacy_unit_columns: _containers.RepeatedScalarFieldContainer[str]
    def __init__(self, threshold: _Optional[int] = ..., privacy_unit_columns: _Optional[_Iterable[str]] = ...) -> None: ...

class DifferentialPrivacyPolicy(_message.Message):
    __slots__ = ("max_epsilon_per_query", "delta_per_query", "max_groups_contributed", "privacy_unit_column", "epsilon_budget", "delta_budget", "epsilon_budget_remaining", "delta_budget_remaining")
    MAX_EPSILON_PER_QUERY_FIELD_NUMBER: _ClassVar[int]
    DELTA_PER_QUERY_FIELD_NUMBER: _ClassVar[int]
    MAX_GROUPS_CONTRIBUTED_FIELD_NUMBER: _ClassVar[int]
    PRIVACY_UNIT_COLUMN_FIELD_NUMBER: _ClassVar[int]
    EPSILON_BUDGET_FIELD_NUMBER: _ClassVar[int]
    DELTA_BUDGET_FIELD_NUMBER: _ClassVar[int]
    EPSILON_BUDGET_REMAINING_FIELD_NUMBER: _ClassVar[int]
    DELTA_BUDGET_REMAINING_FIELD_NUMBER: _ClassVar[int]
    max_epsilon_per_query: float
    delta_per_query: float
    max_groups_contributed: int
    privacy_unit_column: str
    epsilon_budget: float
    delta_budget: float
    epsilon_budget_remaining: float
    delta_budget_remaining: float
    def __init__(self, max_epsilon_per_query: _Optional[float] = ..., delta_per_query: _Optional[float] = ..., max_groups_contributed: _Optional[int] = ..., privacy_unit_column: _Optional[str] = ..., epsilon_budget: _Optional[float] = ..., delta_budget: _Optional[float] = ..., epsilon_budget_remaining: _Optional[float] = ..., delta_budget_remaining: _Optional[float] = ...) -> None: ...

class JoinRestrictionPolicy(_message.Message):
    __slots__ = ("join_condition", "join_allowed_columns")
    class JoinCondition(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        JOIN_CONDITION_UNSPECIFIED: _ClassVar[JoinRestrictionPolicy.JoinCondition]
        JOIN_ANY: _ClassVar[JoinRestrictionPolicy.JoinCondition]
        JOIN_ALL: _ClassVar[JoinRestrictionPolicy.JoinCondition]
        JOIN_NOT_REQUIRED: _ClassVar[JoinRestrictionPolicy.JoinCondition]
        JOIN_BLOCKED: _ClassVar[JoinRestrictionPolicy.JoinCondition]
    JOIN_CONDITION_UNSPECIFIED: JoinRestrictionPolicy.JoinCondition
    JOIN_ANY: JoinRestrictionPolicy.JoinCondition
    JOIN_ALL: JoinRestrictionPolicy.JoinCondition
    JOIN_NOT_REQUIRED: JoinRestrictionPolicy.JoinCondition
    JOIN_BLOCKED: JoinRestrictionPolicy.JoinCondition
    JOIN_CONDITION_FIELD_NUMBER: _ClassVar[int]
    JOIN_ALLOWED_COLUMNS_FIELD_NUMBER: _ClassVar[int]
    join_condition: JoinRestrictionPolicy.JoinCondition
    join_allowed_columns: _containers.RepeatedScalarFieldContainer[str]
    def __init__(self, join_condition: _Optional[_Union[JoinRestrictionPolicy.JoinCondition, str]] = ..., join_allowed_columns: _Optional[_Iterable[str]] = ...) -> None: ...

class PrivacyPolicy(_message.Message):
    __slots__ = ("aggregation_threshold_policy", "differential_privacy_policy", "join_restriction_policy")
    AGGREGATION_THRESHOLD_POLICY_FIELD_NUMBER: _ClassVar[int]
    DIFFERENTIAL_PRIVACY_POLICY_FIELD_NUMBER: _ClassVar[int]
    JOIN_RESTRICTION_POLICY_FIELD_NUMBER: _ClassVar[int]
    aggregation_threshold_policy: AggregationThresholdPolicy
    differential_privacy_policy: DifferentialPrivacyPolicy
    join_restriction_policy: JoinRestrictionPolicy
    def __init__(self, aggregation_threshold_policy: _Optional[_Union[AggregationThresholdPolicy, _Mapping]] = ..., differential_privacy_policy: _Optional[_Union[DifferentialPrivacyPolicy, _Mapping]] = ..., join_restriction_policy: _Optional[_Union[JoinRestrictionPolicy, _Mapping]] = ...) -> None: ...
