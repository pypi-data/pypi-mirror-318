from google.api import annotations_pb2 as _annotations_pb2
from google.api import client_pb2 as _client_pb2
from google.api import field_behavior_pb2 as _field_behavior_pb2
from google.api import resource_pb2 as _resource_pb2
from google.cloud.dialogflow.v2 import validation_result_pb2 as _validation_result_pb2
from google.longrunning import operations_pb2 as _operations_pb2
from google.protobuf import empty_pb2 as _empty_pb2
from google.protobuf import field_mask_pb2 as _field_mask_pb2
from google.protobuf import struct_pb2 as _struct_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union
DESCRIPTOR: _descriptor.FileDescriptor

class Agent(_message.Message):
    __slots__ = ('parent', 'display_name', 'default_language_code', 'supported_language_codes', 'time_zone', 'description', 'avatar_uri', 'enable_logging', 'match_mode', 'classification_threshold', 'api_version', 'tier')

    class MatchMode(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        MATCH_MODE_UNSPECIFIED: _ClassVar[Agent.MatchMode]
        MATCH_MODE_HYBRID: _ClassVar[Agent.MatchMode]
        MATCH_MODE_ML_ONLY: _ClassVar[Agent.MatchMode]
    MATCH_MODE_UNSPECIFIED: Agent.MatchMode
    MATCH_MODE_HYBRID: Agent.MatchMode
    MATCH_MODE_ML_ONLY: Agent.MatchMode

    class ApiVersion(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        API_VERSION_UNSPECIFIED: _ClassVar[Agent.ApiVersion]
        API_VERSION_V1: _ClassVar[Agent.ApiVersion]
        API_VERSION_V2: _ClassVar[Agent.ApiVersion]
        API_VERSION_V2_BETA_1: _ClassVar[Agent.ApiVersion]
    API_VERSION_UNSPECIFIED: Agent.ApiVersion
    API_VERSION_V1: Agent.ApiVersion
    API_VERSION_V2: Agent.ApiVersion
    API_VERSION_V2_BETA_1: Agent.ApiVersion

    class Tier(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        TIER_UNSPECIFIED: _ClassVar[Agent.Tier]
        TIER_STANDARD: _ClassVar[Agent.Tier]
        TIER_ENTERPRISE: _ClassVar[Agent.Tier]
        TIER_ENTERPRISE_PLUS: _ClassVar[Agent.Tier]
    TIER_UNSPECIFIED: Agent.Tier
    TIER_STANDARD: Agent.Tier
    TIER_ENTERPRISE: Agent.Tier
    TIER_ENTERPRISE_PLUS: Agent.Tier
    PARENT_FIELD_NUMBER: _ClassVar[int]
    DISPLAY_NAME_FIELD_NUMBER: _ClassVar[int]
    DEFAULT_LANGUAGE_CODE_FIELD_NUMBER: _ClassVar[int]
    SUPPORTED_LANGUAGE_CODES_FIELD_NUMBER: _ClassVar[int]
    TIME_ZONE_FIELD_NUMBER: _ClassVar[int]
    DESCRIPTION_FIELD_NUMBER: _ClassVar[int]
    AVATAR_URI_FIELD_NUMBER: _ClassVar[int]
    ENABLE_LOGGING_FIELD_NUMBER: _ClassVar[int]
    MATCH_MODE_FIELD_NUMBER: _ClassVar[int]
    CLASSIFICATION_THRESHOLD_FIELD_NUMBER: _ClassVar[int]
    API_VERSION_FIELD_NUMBER: _ClassVar[int]
    TIER_FIELD_NUMBER: _ClassVar[int]
    parent: str
    display_name: str
    default_language_code: str
    supported_language_codes: _containers.RepeatedScalarFieldContainer[str]
    time_zone: str
    description: str
    avatar_uri: str
    enable_logging: bool
    match_mode: Agent.MatchMode
    classification_threshold: float
    api_version: Agent.ApiVersion
    tier: Agent.Tier

    def __init__(self, parent: _Optional[str]=..., display_name: _Optional[str]=..., default_language_code: _Optional[str]=..., supported_language_codes: _Optional[_Iterable[str]]=..., time_zone: _Optional[str]=..., description: _Optional[str]=..., avatar_uri: _Optional[str]=..., enable_logging: bool=..., match_mode: _Optional[_Union[Agent.MatchMode, str]]=..., classification_threshold: _Optional[float]=..., api_version: _Optional[_Union[Agent.ApiVersion, str]]=..., tier: _Optional[_Union[Agent.Tier, str]]=...) -> None:
        ...

class GetAgentRequest(_message.Message):
    __slots__ = ('parent',)
    PARENT_FIELD_NUMBER: _ClassVar[int]
    parent: str

    def __init__(self, parent: _Optional[str]=...) -> None:
        ...

class SetAgentRequest(_message.Message):
    __slots__ = ('agent', 'update_mask')
    AGENT_FIELD_NUMBER: _ClassVar[int]
    UPDATE_MASK_FIELD_NUMBER: _ClassVar[int]
    agent: Agent
    update_mask: _field_mask_pb2.FieldMask

    def __init__(self, agent: _Optional[_Union[Agent, _Mapping]]=..., update_mask: _Optional[_Union[_field_mask_pb2.FieldMask, _Mapping]]=...) -> None:
        ...

class DeleteAgentRequest(_message.Message):
    __slots__ = ('parent',)
    PARENT_FIELD_NUMBER: _ClassVar[int]
    parent: str

    def __init__(self, parent: _Optional[str]=...) -> None:
        ...

class SearchAgentsRequest(_message.Message):
    __slots__ = ('parent', 'page_size', 'page_token')
    PARENT_FIELD_NUMBER: _ClassVar[int]
    PAGE_SIZE_FIELD_NUMBER: _ClassVar[int]
    PAGE_TOKEN_FIELD_NUMBER: _ClassVar[int]
    parent: str
    page_size: int
    page_token: str

    def __init__(self, parent: _Optional[str]=..., page_size: _Optional[int]=..., page_token: _Optional[str]=...) -> None:
        ...

class SearchAgentsResponse(_message.Message):
    __slots__ = ('agents', 'next_page_token')
    AGENTS_FIELD_NUMBER: _ClassVar[int]
    NEXT_PAGE_TOKEN_FIELD_NUMBER: _ClassVar[int]
    agents: _containers.RepeatedCompositeFieldContainer[Agent]
    next_page_token: str

    def __init__(self, agents: _Optional[_Iterable[_Union[Agent, _Mapping]]]=..., next_page_token: _Optional[str]=...) -> None:
        ...

class TrainAgentRequest(_message.Message):
    __slots__ = ('parent',)
    PARENT_FIELD_NUMBER: _ClassVar[int]
    parent: str

    def __init__(self, parent: _Optional[str]=...) -> None:
        ...

class ExportAgentRequest(_message.Message):
    __slots__ = ('parent', 'agent_uri')
    PARENT_FIELD_NUMBER: _ClassVar[int]
    AGENT_URI_FIELD_NUMBER: _ClassVar[int]
    parent: str
    agent_uri: str

    def __init__(self, parent: _Optional[str]=..., agent_uri: _Optional[str]=...) -> None:
        ...

class ExportAgentResponse(_message.Message):
    __slots__ = ('agent_uri', 'agent_content')
    AGENT_URI_FIELD_NUMBER: _ClassVar[int]
    AGENT_CONTENT_FIELD_NUMBER: _ClassVar[int]
    agent_uri: str
    agent_content: bytes

    def __init__(self, agent_uri: _Optional[str]=..., agent_content: _Optional[bytes]=...) -> None:
        ...

class ImportAgentRequest(_message.Message):
    __slots__ = ('parent', 'agent_uri', 'agent_content')
    PARENT_FIELD_NUMBER: _ClassVar[int]
    AGENT_URI_FIELD_NUMBER: _ClassVar[int]
    AGENT_CONTENT_FIELD_NUMBER: _ClassVar[int]
    parent: str
    agent_uri: str
    agent_content: bytes

    def __init__(self, parent: _Optional[str]=..., agent_uri: _Optional[str]=..., agent_content: _Optional[bytes]=...) -> None:
        ...

class RestoreAgentRequest(_message.Message):
    __slots__ = ('parent', 'agent_uri', 'agent_content')
    PARENT_FIELD_NUMBER: _ClassVar[int]
    AGENT_URI_FIELD_NUMBER: _ClassVar[int]
    AGENT_CONTENT_FIELD_NUMBER: _ClassVar[int]
    parent: str
    agent_uri: str
    agent_content: bytes

    def __init__(self, parent: _Optional[str]=..., agent_uri: _Optional[str]=..., agent_content: _Optional[bytes]=...) -> None:
        ...

class GetValidationResultRequest(_message.Message):
    __slots__ = ('parent', 'language_code')
    PARENT_FIELD_NUMBER: _ClassVar[int]
    LANGUAGE_CODE_FIELD_NUMBER: _ClassVar[int]
    parent: str
    language_code: str

    def __init__(self, parent: _Optional[str]=..., language_code: _Optional[str]=...) -> None:
        ...