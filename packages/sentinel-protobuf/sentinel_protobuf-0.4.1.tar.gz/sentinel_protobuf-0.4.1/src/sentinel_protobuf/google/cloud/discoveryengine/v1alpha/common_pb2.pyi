from google.api import resource_pb2 as _resource_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union
DESCRIPTOR: _descriptor.FileDescriptor

class IndustryVertical(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    INDUSTRY_VERTICAL_UNSPECIFIED: _ClassVar[IndustryVertical]
    GENERIC: _ClassVar[IndustryVertical]
    MEDIA: _ClassVar[IndustryVertical]
    HEALTHCARE_FHIR: _ClassVar[IndustryVertical]

class SolutionType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    SOLUTION_TYPE_UNSPECIFIED: _ClassVar[SolutionType]
    SOLUTION_TYPE_RECOMMENDATION: _ClassVar[SolutionType]
    SOLUTION_TYPE_SEARCH: _ClassVar[SolutionType]
    SOLUTION_TYPE_CHAT: _ClassVar[SolutionType]
    SOLUTION_TYPE_GENERATIVE_CHAT: _ClassVar[SolutionType]

class SearchUseCase(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    SEARCH_USE_CASE_UNSPECIFIED: _ClassVar[SearchUseCase]
    SEARCH_USE_CASE_SEARCH: _ClassVar[SearchUseCase]
    SEARCH_USE_CASE_BROWSE: _ClassVar[SearchUseCase]

class SearchTier(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    SEARCH_TIER_UNSPECIFIED: _ClassVar[SearchTier]
    SEARCH_TIER_STANDARD: _ClassVar[SearchTier]
    SEARCH_TIER_ENTERPRISE: _ClassVar[SearchTier]

class SearchAddOn(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    SEARCH_ADD_ON_UNSPECIFIED: _ClassVar[SearchAddOn]
    SEARCH_ADD_ON_LLM: _ClassVar[SearchAddOn]
INDUSTRY_VERTICAL_UNSPECIFIED: IndustryVertical
GENERIC: IndustryVertical
MEDIA: IndustryVertical
HEALTHCARE_FHIR: IndustryVertical
SOLUTION_TYPE_UNSPECIFIED: SolutionType
SOLUTION_TYPE_RECOMMENDATION: SolutionType
SOLUTION_TYPE_SEARCH: SolutionType
SOLUTION_TYPE_CHAT: SolutionType
SOLUTION_TYPE_GENERATIVE_CHAT: SolutionType
SEARCH_USE_CASE_UNSPECIFIED: SearchUseCase
SEARCH_USE_CASE_SEARCH: SearchUseCase
SEARCH_USE_CASE_BROWSE: SearchUseCase
SEARCH_TIER_UNSPECIFIED: SearchTier
SEARCH_TIER_STANDARD: SearchTier
SEARCH_TIER_ENTERPRISE: SearchTier
SEARCH_ADD_ON_UNSPECIFIED: SearchAddOn
SEARCH_ADD_ON_LLM: SearchAddOn

class Interval(_message.Message):
    __slots__ = ('minimum', 'exclusive_minimum', 'maximum', 'exclusive_maximum')
    MINIMUM_FIELD_NUMBER: _ClassVar[int]
    EXCLUSIVE_MINIMUM_FIELD_NUMBER: _ClassVar[int]
    MAXIMUM_FIELD_NUMBER: _ClassVar[int]
    EXCLUSIVE_MAXIMUM_FIELD_NUMBER: _ClassVar[int]
    minimum: float
    exclusive_minimum: float
    maximum: float
    exclusive_maximum: float

    def __init__(self, minimum: _Optional[float]=..., exclusive_minimum: _Optional[float]=..., maximum: _Optional[float]=..., exclusive_maximum: _Optional[float]=...) -> None:
        ...

class CustomAttribute(_message.Message):
    __slots__ = ('text', 'numbers')
    TEXT_FIELD_NUMBER: _ClassVar[int]
    NUMBERS_FIELD_NUMBER: _ClassVar[int]
    text: _containers.RepeatedScalarFieldContainer[str]
    numbers: _containers.RepeatedScalarFieldContainer[float]

    def __init__(self, text: _Optional[_Iterable[str]]=..., numbers: _Optional[_Iterable[float]]=...) -> None:
        ...

class UserInfo(_message.Message):
    __slots__ = ('user_id', 'user_agent')
    USER_ID_FIELD_NUMBER: _ClassVar[int]
    USER_AGENT_FIELD_NUMBER: _ClassVar[int]
    user_id: str
    user_agent: str

    def __init__(self, user_id: _Optional[str]=..., user_agent: _Optional[str]=...) -> None:
        ...

class EmbeddingConfig(_message.Message):
    __slots__ = ('field_path',)
    FIELD_PATH_FIELD_NUMBER: _ClassVar[int]
    field_path: str

    def __init__(self, field_path: _Optional[str]=...) -> None:
        ...

class DoubleList(_message.Message):
    __slots__ = ('values',)
    VALUES_FIELD_NUMBER: _ClassVar[int]
    values: _containers.RepeatedScalarFieldContainer[float]

    def __init__(self, values: _Optional[_Iterable[float]]=...) -> None:
        ...

class GuidedSearchSpec(_message.Message):
    __slots__ = ('enable_refinement_attributes', 'enable_related_questions', 'max_related_questions')
    ENABLE_REFINEMENT_ATTRIBUTES_FIELD_NUMBER: _ClassVar[int]
    ENABLE_RELATED_QUESTIONS_FIELD_NUMBER: _ClassVar[int]
    MAX_RELATED_QUESTIONS_FIELD_NUMBER: _ClassVar[int]
    enable_refinement_attributes: bool
    enable_related_questions: bool
    max_related_questions: int

    def __init__(self, enable_refinement_attributes: bool=..., enable_related_questions: bool=..., max_related_questions: _Optional[int]=...) -> None:
        ...

class CustomFineTuningSpec(_message.Message):
    __slots__ = ('enable_search_adaptor',)
    ENABLE_SEARCH_ADAPTOR_FIELD_NUMBER: _ClassVar[int]
    enable_search_adaptor: bool

    def __init__(self, enable_search_adaptor: bool=...) -> None:
        ...

class IdpConfig(_message.Message):
    __slots__ = ('idp_type', 'external_idp_config')

    class IdpType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        IDP_TYPE_UNSPECIFIED: _ClassVar[IdpConfig.IdpType]
        GSUITE: _ClassVar[IdpConfig.IdpType]
        THIRD_PARTY: _ClassVar[IdpConfig.IdpType]
    IDP_TYPE_UNSPECIFIED: IdpConfig.IdpType
    GSUITE: IdpConfig.IdpType
    THIRD_PARTY: IdpConfig.IdpType

    class ExternalIdpConfig(_message.Message):
        __slots__ = ('workforce_pool_name',)
        WORKFORCE_POOL_NAME_FIELD_NUMBER: _ClassVar[int]
        workforce_pool_name: str

        def __init__(self, workforce_pool_name: _Optional[str]=...) -> None:
            ...
    IDP_TYPE_FIELD_NUMBER: _ClassVar[int]
    EXTERNAL_IDP_CONFIG_FIELD_NUMBER: _ClassVar[int]
    idp_type: IdpConfig.IdpType
    external_idp_config: IdpConfig.ExternalIdpConfig

    def __init__(self, idp_type: _Optional[_Union[IdpConfig.IdpType, str]]=..., external_idp_config: _Optional[_Union[IdpConfig.ExternalIdpConfig, _Mapping]]=...) -> None:
        ...

class Principal(_message.Message):
    __slots__ = ('user_id', 'group_id')
    USER_ID_FIELD_NUMBER: _ClassVar[int]
    GROUP_ID_FIELD_NUMBER: _ClassVar[int]
    user_id: str
    group_id: str

    def __init__(self, user_id: _Optional[str]=..., group_id: _Optional[str]=...) -> None:
        ...