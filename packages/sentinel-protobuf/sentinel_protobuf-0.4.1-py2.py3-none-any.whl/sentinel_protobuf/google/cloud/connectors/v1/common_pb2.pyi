from google.api import field_behavior_pb2 as _field_behavior_pb2
from google.protobuf import timestamp_pb2 as _timestamp_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union
DESCRIPTOR: _descriptor.FileDescriptor

class LaunchStage(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    LAUNCH_STAGE_UNSPECIFIED: _ClassVar[LaunchStage]
    PREVIEW: _ClassVar[LaunchStage]
    GA: _ClassVar[LaunchStage]
    DEPRECATED: _ClassVar[LaunchStage]
    PRIVATE_PREVIEW: _ClassVar[LaunchStage]
LAUNCH_STAGE_UNSPECIFIED: LaunchStage
PREVIEW: LaunchStage
GA: LaunchStage
DEPRECATED: LaunchStage
PRIVATE_PREVIEW: LaunchStage

class OperationMetadata(_message.Message):
    __slots__ = ('create_time', 'end_time', 'target', 'verb', 'status_message', 'requested_cancellation', 'api_version')
    CREATE_TIME_FIELD_NUMBER: _ClassVar[int]
    END_TIME_FIELD_NUMBER: _ClassVar[int]
    TARGET_FIELD_NUMBER: _ClassVar[int]
    VERB_FIELD_NUMBER: _ClassVar[int]
    STATUS_MESSAGE_FIELD_NUMBER: _ClassVar[int]
    REQUESTED_CANCELLATION_FIELD_NUMBER: _ClassVar[int]
    API_VERSION_FIELD_NUMBER: _ClassVar[int]
    create_time: _timestamp_pb2.Timestamp
    end_time: _timestamp_pb2.Timestamp
    target: str
    verb: str
    status_message: str
    requested_cancellation: bool
    api_version: str

    def __init__(self, create_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]]=..., end_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]]=..., target: _Optional[str]=..., verb: _Optional[str]=..., status_message: _Optional[str]=..., requested_cancellation: bool=..., api_version: _Optional[str]=...) -> None:
        ...

class ConfigVariableTemplate(_message.Message):
    __slots__ = ('key', 'value_type', 'display_name', 'description', 'validation_regex', 'required', 'role_grant', 'enum_options', 'authorization_code_link', 'state', 'is_advanced')

    class ValueType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        VALUE_TYPE_UNSPECIFIED: _ClassVar[ConfigVariableTemplate.ValueType]
        STRING: _ClassVar[ConfigVariableTemplate.ValueType]
        INT: _ClassVar[ConfigVariableTemplate.ValueType]
        BOOL: _ClassVar[ConfigVariableTemplate.ValueType]
        SECRET: _ClassVar[ConfigVariableTemplate.ValueType]
        ENUM: _ClassVar[ConfigVariableTemplate.ValueType]
        AUTHORIZATION_CODE: _ClassVar[ConfigVariableTemplate.ValueType]
    VALUE_TYPE_UNSPECIFIED: ConfigVariableTemplate.ValueType
    STRING: ConfigVariableTemplate.ValueType
    INT: ConfigVariableTemplate.ValueType
    BOOL: ConfigVariableTemplate.ValueType
    SECRET: ConfigVariableTemplate.ValueType
    ENUM: ConfigVariableTemplate.ValueType
    AUTHORIZATION_CODE: ConfigVariableTemplate.ValueType

    class State(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        STATE_UNSPECIFIED: _ClassVar[ConfigVariableTemplate.State]
        ACTIVE: _ClassVar[ConfigVariableTemplate.State]
        DEPRECATED: _ClassVar[ConfigVariableTemplate.State]
    STATE_UNSPECIFIED: ConfigVariableTemplate.State
    ACTIVE: ConfigVariableTemplate.State
    DEPRECATED: ConfigVariableTemplate.State
    KEY_FIELD_NUMBER: _ClassVar[int]
    VALUE_TYPE_FIELD_NUMBER: _ClassVar[int]
    DISPLAY_NAME_FIELD_NUMBER: _ClassVar[int]
    DESCRIPTION_FIELD_NUMBER: _ClassVar[int]
    VALIDATION_REGEX_FIELD_NUMBER: _ClassVar[int]
    REQUIRED_FIELD_NUMBER: _ClassVar[int]
    ROLE_GRANT_FIELD_NUMBER: _ClassVar[int]
    ENUM_OPTIONS_FIELD_NUMBER: _ClassVar[int]
    AUTHORIZATION_CODE_LINK_FIELD_NUMBER: _ClassVar[int]
    STATE_FIELD_NUMBER: _ClassVar[int]
    IS_ADVANCED_FIELD_NUMBER: _ClassVar[int]
    key: str
    value_type: ConfigVariableTemplate.ValueType
    display_name: str
    description: str
    validation_regex: str
    required: bool
    role_grant: RoleGrant
    enum_options: _containers.RepeatedCompositeFieldContainer[EnumOption]
    authorization_code_link: AuthorizationCodeLink
    state: ConfigVariableTemplate.State
    is_advanced: bool

    def __init__(self, key: _Optional[str]=..., value_type: _Optional[_Union[ConfigVariableTemplate.ValueType, str]]=..., display_name: _Optional[str]=..., description: _Optional[str]=..., validation_regex: _Optional[str]=..., required: bool=..., role_grant: _Optional[_Union[RoleGrant, _Mapping]]=..., enum_options: _Optional[_Iterable[_Union[EnumOption, _Mapping]]]=..., authorization_code_link: _Optional[_Union[AuthorizationCodeLink, _Mapping]]=..., state: _Optional[_Union[ConfigVariableTemplate.State, str]]=..., is_advanced: bool=...) -> None:
        ...

class Secret(_message.Message):
    __slots__ = ('secret_version',)
    SECRET_VERSION_FIELD_NUMBER: _ClassVar[int]
    secret_version: str

    def __init__(self, secret_version: _Optional[str]=...) -> None:
        ...

class EnumOption(_message.Message):
    __slots__ = ('id', 'display_name')
    ID_FIELD_NUMBER: _ClassVar[int]
    DISPLAY_NAME_FIELD_NUMBER: _ClassVar[int]
    id: str
    display_name: str

    def __init__(self, id: _Optional[str]=..., display_name: _Optional[str]=...) -> None:
        ...

class ConfigVariable(_message.Message):
    __slots__ = ('key', 'int_value', 'bool_value', 'string_value', 'secret_value')
    KEY_FIELD_NUMBER: _ClassVar[int]
    INT_VALUE_FIELD_NUMBER: _ClassVar[int]
    BOOL_VALUE_FIELD_NUMBER: _ClassVar[int]
    STRING_VALUE_FIELD_NUMBER: _ClassVar[int]
    SECRET_VALUE_FIELD_NUMBER: _ClassVar[int]
    key: str
    int_value: int
    bool_value: bool
    string_value: str
    secret_value: Secret

    def __init__(self, key: _Optional[str]=..., int_value: _Optional[int]=..., bool_value: bool=..., string_value: _Optional[str]=..., secret_value: _Optional[_Union[Secret, _Mapping]]=...) -> None:
        ...

class RoleGrant(_message.Message):
    __slots__ = ('principal', 'roles', 'resource', 'helper_text_template')

    class Principal(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        PRINCIPAL_UNSPECIFIED: _ClassVar[RoleGrant.Principal]
        CONNECTOR_SA: _ClassVar[RoleGrant.Principal]
    PRINCIPAL_UNSPECIFIED: RoleGrant.Principal
    CONNECTOR_SA: RoleGrant.Principal

    class Resource(_message.Message):
        __slots__ = ('type', 'path_template')

        class Type(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
            __slots__ = ()
            TYPE_UNSPECIFIED: _ClassVar[RoleGrant.Resource.Type]
            GCP_PROJECT: _ClassVar[RoleGrant.Resource.Type]
            GCP_RESOURCE: _ClassVar[RoleGrant.Resource.Type]
            GCP_SECRETMANAGER_SECRET: _ClassVar[RoleGrant.Resource.Type]
            GCP_SECRETMANAGER_SECRET_VERSION: _ClassVar[RoleGrant.Resource.Type]
        TYPE_UNSPECIFIED: RoleGrant.Resource.Type
        GCP_PROJECT: RoleGrant.Resource.Type
        GCP_RESOURCE: RoleGrant.Resource.Type
        GCP_SECRETMANAGER_SECRET: RoleGrant.Resource.Type
        GCP_SECRETMANAGER_SECRET_VERSION: RoleGrant.Resource.Type
        TYPE_FIELD_NUMBER: _ClassVar[int]
        PATH_TEMPLATE_FIELD_NUMBER: _ClassVar[int]
        type: RoleGrant.Resource.Type
        path_template: str

        def __init__(self, type: _Optional[_Union[RoleGrant.Resource.Type, str]]=..., path_template: _Optional[str]=...) -> None:
            ...
    PRINCIPAL_FIELD_NUMBER: _ClassVar[int]
    ROLES_FIELD_NUMBER: _ClassVar[int]
    RESOURCE_FIELD_NUMBER: _ClassVar[int]
    HELPER_TEXT_TEMPLATE_FIELD_NUMBER: _ClassVar[int]
    principal: RoleGrant.Principal
    roles: _containers.RepeatedScalarFieldContainer[str]
    resource: RoleGrant.Resource
    helper_text_template: str

    def __init__(self, principal: _Optional[_Union[RoleGrant.Principal, str]]=..., roles: _Optional[_Iterable[str]]=..., resource: _Optional[_Union[RoleGrant.Resource, _Mapping]]=..., helper_text_template: _Optional[str]=...) -> None:
        ...

class AuthorizationCodeLink(_message.Message):
    __slots__ = ('uri', 'scopes', 'client_id', 'enable_pkce')
    URI_FIELD_NUMBER: _ClassVar[int]
    SCOPES_FIELD_NUMBER: _ClassVar[int]
    CLIENT_ID_FIELD_NUMBER: _ClassVar[int]
    ENABLE_PKCE_FIELD_NUMBER: _ClassVar[int]
    uri: str
    scopes: _containers.RepeatedScalarFieldContainer[str]
    client_id: str
    enable_pkce: bool

    def __init__(self, uri: _Optional[str]=..., scopes: _Optional[_Iterable[str]]=..., client_id: _Optional[str]=..., enable_pkce: bool=...) -> None:
        ...