from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union
DESCRIPTOR: _descriptor.FileDescriptor

class CVSSv3(_message.Message):
    __slots__ = ('base_score', 'exploitability_score', 'impact_score', 'attack_vector', 'attack_complexity', 'privileges_required', 'user_interaction', 'scope', 'confidentiality_impact', 'integrity_impact', 'availability_impact')

    class AttackVector(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        ATTACK_VECTOR_UNSPECIFIED: _ClassVar[CVSSv3.AttackVector]
        ATTACK_VECTOR_NETWORK: _ClassVar[CVSSv3.AttackVector]
        ATTACK_VECTOR_ADJACENT: _ClassVar[CVSSv3.AttackVector]
        ATTACK_VECTOR_LOCAL: _ClassVar[CVSSv3.AttackVector]
        ATTACK_VECTOR_PHYSICAL: _ClassVar[CVSSv3.AttackVector]
    ATTACK_VECTOR_UNSPECIFIED: CVSSv3.AttackVector
    ATTACK_VECTOR_NETWORK: CVSSv3.AttackVector
    ATTACK_VECTOR_ADJACENT: CVSSv3.AttackVector
    ATTACK_VECTOR_LOCAL: CVSSv3.AttackVector
    ATTACK_VECTOR_PHYSICAL: CVSSv3.AttackVector

    class AttackComplexity(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        ATTACK_COMPLEXITY_UNSPECIFIED: _ClassVar[CVSSv3.AttackComplexity]
        ATTACK_COMPLEXITY_LOW: _ClassVar[CVSSv3.AttackComplexity]
        ATTACK_COMPLEXITY_HIGH: _ClassVar[CVSSv3.AttackComplexity]
    ATTACK_COMPLEXITY_UNSPECIFIED: CVSSv3.AttackComplexity
    ATTACK_COMPLEXITY_LOW: CVSSv3.AttackComplexity
    ATTACK_COMPLEXITY_HIGH: CVSSv3.AttackComplexity

    class PrivilegesRequired(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        PRIVILEGES_REQUIRED_UNSPECIFIED: _ClassVar[CVSSv3.PrivilegesRequired]
        PRIVILEGES_REQUIRED_NONE: _ClassVar[CVSSv3.PrivilegesRequired]
        PRIVILEGES_REQUIRED_LOW: _ClassVar[CVSSv3.PrivilegesRequired]
        PRIVILEGES_REQUIRED_HIGH: _ClassVar[CVSSv3.PrivilegesRequired]
    PRIVILEGES_REQUIRED_UNSPECIFIED: CVSSv3.PrivilegesRequired
    PRIVILEGES_REQUIRED_NONE: CVSSv3.PrivilegesRequired
    PRIVILEGES_REQUIRED_LOW: CVSSv3.PrivilegesRequired
    PRIVILEGES_REQUIRED_HIGH: CVSSv3.PrivilegesRequired

    class UserInteraction(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        USER_INTERACTION_UNSPECIFIED: _ClassVar[CVSSv3.UserInteraction]
        USER_INTERACTION_NONE: _ClassVar[CVSSv3.UserInteraction]
        USER_INTERACTION_REQUIRED: _ClassVar[CVSSv3.UserInteraction]
    USER_INTERACTION_UNSPECIFIED: CVSSv3.UserInteraction
    USER_INTERACTION_NONE: CVSSv3.UserInteraction
    USER_INTERACTION_REQUIRED: CVSSv3.UserInteraction

    class Scope(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        SCOPE_UNSPECIFIED: _ClassVar[CVSSv3.Scope]
        SCOPE_UNCHANGED: _ClassVar[CVSSv3.Scope]
        SCOPE_CHANGED: _ClassVar[CVSSv3.Scope]
    SCOPE_UNSPECIFIED: CVSSv3.Scope
    SCOPE_UNCHANGED: CVSSv3.Scope
    SCOPE_CHANGED: CVSSv3.Scope

    class Impact(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        IMPACT_UNSPECIFIED: _ClassVar[CVSSv3.Impact]
        IMPACT_HIGH: _ClassVar[CVSSv3.Impact]
        IMPACT_LOW: _ClassVar[CVSSv3.Impact]
        IMPACT_NONE: _ClassVar[CVSSv3.Impact]
    IMPACT_UNSPECIFIED: CVSSv3.Impact
    IMPACT_HIGH: CVSSv3.Impact
    IMPACT_LOW: CVSSv3.Impact
    IMPACT_NONE: CVSSv3.Impact
    BASE_SCORE_FIELD_NUMBER: _ClassVar[int]
    EXPLOITABILITY_SCORE_FIELD_NUMBER: _ClassVar[int]
    IMPACT_SCORE_FIELD_NUMBER: _ClassVar[int]
    ATTACK_VECTOR_FIELD_NUMBER: _ClassVar[int]
    ATTACK_COMPLEXITY_FIELD_NUMBER: _ClassVar[int]
    PRIVILEGES_REQUIRED_FIELD_NUMBER: _ClassVar[int]
    USER_INTERACTION_FIELD_NUMBER: _ClassVar[int]
    SCOPE_FIELD_NUMBER: _ClassVar[int]
    CONFIDENTIALITY_IMPACT_FIELD_NUMBER: _ClassVar[int]
    INTEGRITY_IMPACT_FIELD_NUMBER: _ClassVar[int]
    AVAILABILITY_IMPACT_FIELD_NUMBER: _ClassVar[int]
    base_score: float
    exploitability_score: float
    impact_score: float
    attack_vector: CVSSv3.AttackVector
    attack_complexity: CVSSv3.AttackComplexity
    privileges_required: CVSSv3.PrivilegesRequired
    user_interaction: CVSSv3.UserInteraction
    scope: CVSSv3.Scope
    confidentiality_impact: CVSSv3.Impact
    integrity_impact: CVSSv3.Impact
    availability_impact: CVSSv3.Impact

    def __init__(self, base_score: _Optional[float]=..., exploitability_score: _Optional[float]=..., impact_score: _Optional[float]=..., attack_vector: _Optional[_Union[CVSSv3.AttackVector, str]]=..., attack_complexity: _Optional[_Union[CVSSv3.AttackComplexity, str]]=..., privileges_required: _Optional[_Union[CVSSv3.PrivilegesRequired, str]]=..., user_interaction: _Optional[_Union[CVSSv3.UserInteraction, str]]=..., scope: _Optional[_Union[CVSSv3.Scope, str]]=..., confidentiality_impact: _Optional[_Union[CVSSv3.Impact, str]]=..., integrity_impact: _Optional[_Union[CVSSv3.Impact, str]]=..., availability_impact: _Optional[_Union[CVSSv3.Impact, str]]=...) -> None:
        ...