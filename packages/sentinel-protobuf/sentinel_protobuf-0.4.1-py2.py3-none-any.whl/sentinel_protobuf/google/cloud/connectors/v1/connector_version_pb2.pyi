from google.api import field_behavior_pb2 as _field_behavior_pb2
from google.api import resource_pb2 as _resource_pb2
from google.cloud.connectors.v1 import authconfig_pb2 as _authconfig_pb2
from google.cloud.connectors.v1 import common_pb2 as _common_pb2
from google.cloud.connectors.v1 import ssl_config_pb2 as _ssl_config_pb2
from google.protobuf import timestamp_pb2 as _timestamp_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union
DESCRIPTOR: _descriptor.FileDescriptor

class ConnectorVersionView(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    CONNECTOR_VERSION_VIEW_UNSPECIFIED: _ClassVar[ConnectorVersionView]
    CONNECTOR_VERSION_VIEW_BASIC: _ClassVar[ConnectorVersionView]
    CONNECTOR_VERSION_VIEW_FULL: _ClassVar[ConnectorVersionView]
CONNECTOR_VERSION_VIEW_UNSPECIFIED: ConnectorVersionView
CONNECTOR_VERSION_VIEW_BASIC: ConnectorVersionView
CONNECTOR_VERSION_VIEW_FULL: ConnectorVersionView

class ConnectorVersion(_message.Message):
    __slots__ = ('name', 'create_time', 'update_time', 'labels', 'launch_stage', 'release_version', 'auth_config_templates', 'config_variable_templates', 'supported_runtime_features', 'display_name', 'egress_control_config', 'role_grants', 'role_grant', 'ssl_config_template')

    class LabelsEntry(_message.Message):
        __slots__ = ('key', 'value')
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: str

        def __init__(self, key: _Optional[str]=..., value: _Optional[str]=...) -> None:
            ...
    NAME_FIELD_NUMBER: _ClassVar[int]
    CREATE_TIME_FIELD_NUMBER: _ClassVar[int]
    UPDATE_TIME_FIELD_NUMBER: _ClassVar[int]
    LABELS_FIELD_NUMBER: _ClassVar[int]
    LAUNCH_STAGE_FIELD_NUMBER: _ClassVar[int]
    RELEASE_VERSION_FIELD_NUMBER: _ClassVar[int]
    AUTH_CONFIG_TEMPLATES_FIELD_NUMBER: _ClassVar[int]
    CONFIG_VARIABLE_TEMPLATES_FIELD_NUMBER: _ClassVar[int]
    SUPPORTED_RUNTIME_FEATURES_FIELD_NUMBER: _ClassVar[int]
    DISPLAY_NAME_FIELD_NUMBER: _ClassVar[int]
    EGRESS_CONTROL_CONFIG_FIELD_NUMBER: _ClassVar[int]
    ROLE_GRANTS_FIELD_NUMBER: _ClassVar[int]
    ROLE_GRANT_FIELD_NUMBER: _ClassVar[int]
    SSL_CONFIG_TEMPLATE_FIELD_NUMBER: _ClassVar[int]
    name: str
    create_time: _timestamp_pb2.Timestamp
    update_time: _timestamp_pb2.Timestamp
    labels: _containers.ScalarMap[str, str]
    launch_stage: _common_pb2.LaunchStage
    release_version: str
    auth_config_templates: _containers.RepeatedCompositeFieldContainer[_authconfig_pb2.AuthConfigTemplate]
    config_variable_templates: _containers.RepeatedCompositeFieldContainer[_common_pb2.ConfigVariableTemplate]
    supported_runtime_features: SupportedRuntimeFeatures
    display_name: str
    egress_control_config: EgressControlConfig
    role_grants: _containers.RepeatedCompositeFieldContainer[_common_pb2.RoleGrant]
    role_grant: _common_pb2.RoleGrant
    ssl_config_template: _ssl_config_pb2.SslConfigTemplate

    def __init__(self, name: _Optional[str]=..., create_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]]=..., update_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]]=..., labels: _Optional[_Mapping[str, str]]=..., launch_stage: _Optional[_Union[_common_pb2.LaunchStage, str]]=..., release_version: _Optional[str]=..., auth_config_templates: _Optional[_Iterable[_Union[_authconfig_pb2.AuthConfigTemplate, _Mapping]]]=..., config_variable_templates: _Optional[_Iterable[_Union[_common_pb2.ConfigVariableTemplate, _Mapping]]]=..., supported_runtime_features: _Optional[_Union[SupportedRuntimeFeatures, _Mapping]]=..., display_name: _Optional[str]=..., egress_control_config: _Optional[_Union[EgressControlConfig, _Mapping]]=..., role_grants: _Optional[_Iterable[_Union[_common_pb2.RoleGrant, _Mapping]]]=..., role_grant: _Optional[_Union[_common_pb2.RoleGrant, _Mapping]]=..., ssl_config_template: _Optional[_Union[_ssl_config_pb2.SslConfigTemplate, _Mapping]]=...) -> None:
        ...

class GetConnectorVersionRequest(_message.Message):
    __slots__ = ('name', 'view')
    NAME_FIELD_NUMBER: _ClassVar[int]
    VIEW_FIELD_NUMBER: _ClassVar[int]
    name: str
    view: ConnectorVersionView

    def __init__(self, name: _Optional[str]=..., view: _Optional[_Union[ConnectorVersionView, str]]=...) -> None:
        ...

class ListConnectorVersionsRequest(_message.Message):
    __slots__ = ('parent', 'page_size', 'page_token', 'view')
    PARENT_FIELD_NUMBER: _ClassVar[int]
    PAGE_SIZE_FIELD_NUMBER: _ClassVar[int]
    PAGE_TOKEN_FIELD_NUMBER: _ClassVar[int]
    VIEW_FIELD_NUMBER: _ClassVar[int]
    parent: str
    page_size: int
    page_token: str
    view: ConnectorVersionView

    def __init__(self, parent: _Optional[str]=..., page_size: _Optional[int]=..., page_token: _Optional[str]=..., view: _Optional[_Union[ConnectorVersionView, str]]=...) -> None:
        ...

class ListConnectorVersionsResponse(_message.Message):
    __slots__ = ('connector_versions', 'next_page_token', 'unreachable')
    CONNECTOR_VERSIONS_FIELD_NUMBER: _ClassVar[int]
    NEXT_PAGE_TOKEN_FIELD_NUMBER: _ClassVar[int]
    UNREACHABLE_FIELD_NUMBER: _ClassVar[int]
    connector_versions: _containers.RepeatedCompositeFieldContainer[ConnectorVersion]
    next_page_token: str
    unreachable: _containers.RepeatedScalarFieldContainer[str]

    def __init__(self, connector_versions: _Optional[_Iterable[_Union[ConnectorVersion, _Mapping]]]=..., next_page_token: _Optional[str]=..., unreachable: _Optional[_Iterable[str]]=...) -> None:
        ...

class SupportedRuntimeFeatures(_message.Message):
    __slots__ = ('entity_apis', 'action_apis', 'sql_query')
    ENTITY_APIS_FIELD_NUMBER: _ClassVar[int]
    ACTION_APIS_FIELD_NUMBER: _ClassVar[int]
    SQL_QUERY_FIELD_NUMBER: _ClassVar[int]
    entity_apis: bool
    action_apis: bool
    sql_query: bool

    def __init__(self, entity_apis: bool=..., action_apis: bool=..., sql_query: bool=...) -> None:
        ...

class EgressControlConfig(_message.Message):
    __slots__ = ('backends', 'extraction_rules')
    BACKENDS_FIELD_NUMBER: _ClassVar[int]
    EXTRACTION_RULES_FIELD_NUMBER: _ClassVar[int]
    backends: str
    extraction_rules: ExtractionRules

    def __init__(self, backends: _Optional[str]=..., extraction_rules: _Optional[_Union[ExtractionRules, _Mapping]]=...) -> None:
        ...

class ExtractionRules(_message.Message):
    __slots__ = ('extraction_rule',)
    EXTRACTION_RULE_FIELD_NUMBER: _ClassVar[int]
    extraction_rule: _containers.RepeatedCompositeFieldContainer[ExtractionRule]

    def __init__(self, extraction_rule: _Optional[_Iterable[_Union[ExtractionRule, _Mapping]]]=...) -> None:
        ...

class ExtractionRule(_message.Message):
    __slots__ = ('source', 'extraction_regex')

    class SourceType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        SOURCE_TYPE_UNSPECIFIED: _ClassVar[ExtractionRule.SourceType]
        CONFIG_VARIABLE: _ClassVar[ExtractionRule.SourceType]
    SOURCE_TYPE_UNSPECIFIED: ExtractionRule.SourceType
    CONFIG_VARIABLE: ExtractionRule.SourceType

    class Source(_message.Message):
        __slots__ = ('source_type', 'field_id')
        SOURCE_TYPE_FIELD_NUMBER: _ClassVar[int]
        FIELD_ID_FIELD_NUMBER: _ClassVar[int]
        source_type: ExtractionRule.SourceType
        field_id: str

        def __init__(self, source_type: _Optional[_Union[ExtractionRule.SourceType, str]]=..., field_id: _Optional[str]=...) -> None:
            ...
    SOURCE_FIELD_NUMBER: _ClassVar[int]
    EXTRACTION_REGEX_FIELD_NUMBER: _ClassVar[int]
    source: ExtractionRule.Source
    extraction_regex: str

    def __init__(self, source: _Optional[_Union[ExtractionRule.Source, _Mapping]]=..., extraction_regex: _Optional[str]=...) -> None:
        ...