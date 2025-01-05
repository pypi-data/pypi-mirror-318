from google.api import field_behavior_pb2 as _field_behavior_pb2
from google.api import resource_pb2 as _resource_pb2
from google.cloud.discoveryengine.v1beta import common_pb2 as _common_pb2
from google.protobuf import timestamp_pb2 as _timestamp_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union
DESCRIPTOR: _descriptor.FileDescriptor

class Engine(_message.Message):
    __slots__ = ('chat_engine_config', 'search_engine_config', 'chat_engine_metadata', 'name', 'display_name', 'create_time', 'update_time', 'data_store_ids', 'solution_type', 'industry_vertical', 'common_config', 'disable_analytics')

    class SearchEngineConfig(_message.Message):
        __slots__ = ('search_tier', 'search_add_ons')
        SEARCH_TIER_FIELD_NUMBER: _ClassVar[int]
        SEARCH_ADD_ONS_FIELD_NUMBER: _ClassVar[int]
        search_tier: _common_pb2.SearchTier
        search_add_ons: _containers.RepeatedScalarFieldContainer[_common_pb2.SearchAddOn]

        def __init__(self, search_tier: _Optional[_Union[_common_pb2.SearchTier, str]]=..., search_add_ons: _Optional[_Iterable[_Union[_common_pb2.SearchAddOn, str]]]=...) -> None:
            ...

    class ChatEngineConfig(_message.Message):
        __slots__ = ('agent_creation_config', 'dialogflow_agent_to_link')

        class AgentCreationConfig(_message.Message):
            __slots__ = ('business', 'default_language_code', 'time_zone', 'location')
            BUSINESS_FIELD_NUMBER: _ClassVar[int]
            DEFAULT_LANGUAGE_CODE_FIELD_NUMBER: _ClassVar[int]
            TIME_ZONE_FIELD_NUMBER: _ClassVar[int]
            LOCATION_FIELD_NUMBER: _ClassVar[int]
            business: str
            default_language_code: str
            time_zone: str
            location: str

            def __init__(self, business: _Optional[str]=..., default_language_code: _Optional[str]=..., time_zone: _Optional[str]=..., location: _Optional[str]=...) -> None:
                ...
        AGENT_CREATION_CONFIG_FIELD_NUMBER: _ClassVar[int]
        DIALOGFLOW_AGENT_TO_LINK_FIELD_NUMBER: _ClassVar[int]
        agent_creation_config: Engine.ChatEngineConfig.AgentCreationConfig
        dialogflow_agent_to_link: str

        def __init__(self, agent_creation_config: _Optional[_Union[Engine.ChatEngineConfig.AgentCreationConfig, _Mapping]]=..., dialogflow_agent_to_link: _Optional[str]=...) -> None:
            ...

    class CommonConfig(_message.Message):
        __slots__ = ('company_name',)
        COMPANY_NAME_FIELD_NUMBER: _ClassVar[int]
        company_name: str

        def __init__(self, company_name: _Optional[str]=...) -> None:
            ...

    class ChatEngineMetadata(_message.Message):
        __slots__ = ('dialogflow_agent',)
        DIALOGFLOW_AGENT_FIELD_NUMBER: _ClassVar[int]
        dialogflow_agent: str

        def __init__(self, dialogflow_agent: _Optional[str]=...) -> None:
            ...
    CHAT_ENGINE_CONFIG_FIELD_NUMBER: _ClassVar[int]
    SEARCH_ENGINE_CONFIG_FIELD_NUMBER: _ClassVar[int]
    CHAT_ENGINE_METADATA_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    DISPLAY_NAME_FIELD_NUMBER: _ClassVar[int]
    CREATE_TIME_FIELD_NUMBER: _ClassVar[int]
    UPDATE_TIME_FIELD_NUMBER: _ClassVar[int]
    DATA_STORE_IDS_FIELD_NUMBER: _ClassVar[int]
    SOLUTION_TYPE_FIELD_NUMBER: _ClassVar[int]
    INDUSTRY_VERTICAL_FIELD_NUMBER: _ClassVar[int]
    COMMON_CONFIG_FIELD_NUMBER: _ClassVar[int]
    DISABLE_ANALYTICS_FIELD_NUMBER: _ClassVar[int]
    chat_engine_config: Engine.ChatEngineConfig
    search_engine_config: Engine.SearchEngineConfig
    chat_engine_metadata: Engine.ChatEngineMetadata
    name: str
    display_name: str
    create_time: _timestamp_pb2.Timestamp
    update_time: _timestamp_pb2.Timestamp
    data_store_ids: _containers.RepeatedScalarFieldContainer[str]
    solution_type: _common_pb2.SolutionType
    industry_vertical: _common_pb2.IndustryVertical
    common_config: Engine.CommonConfig
    disable_analytics: bool

    def __init__(self, chat_engine_config: _Optional[_Union[Engine.ChatEngineConfig, _Mapping]]=..., search_engine_config: _Optional[_Union[Engine.SearchEngineConfig, _Mapping]]=..., chat_engine_metadata: _Optional[_Union[Engine.ChatEngineMetadata, _Mapping]]=..., name: _Optional[str]=..., display_name: _Optional[str]=..., create_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]]=..., update_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]]=..., data_store_ids: _Optional[_Iterable[str]]=..., solution_type: _Optional[_Union[_common_pb2.SolutionType, str]]=..., industry_vertical: _Optional[_Union[_common_pb2.IndustryVertical, str]]=..., common_config: _Optional[_Union[Engine.CommonConfig, _Mapping]]=..., disable_analytics: bool=...) -> None:
        ...