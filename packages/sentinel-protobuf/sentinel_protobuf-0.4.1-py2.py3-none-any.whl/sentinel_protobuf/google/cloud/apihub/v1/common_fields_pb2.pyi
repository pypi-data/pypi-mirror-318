from google.api import field_behavior_pb2 as _field_behavior_pb2
from google.api import resource_pb2 as _resource_pb2
from google.protobuf import timestamp_pb2 as _timestamp_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union
DESCRIPTOR: _descriptor.FileDescriptor

class LintState(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    LINT_STATE_UNSPECIFIED: _ClassVar[LintState]
    LINT_STATE_SUCCESS: _ClassVar[LintState]
    LINT_STATE_ERROR: _ClassVar[LintState]

class Linter(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    LINTER_UNSPECIFIED: _ClassVar[Linter]
    SPECTRAL: _ClassVar[Linter]
    OTHER: _ClassVar[Linter]

class Severity(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    SEVERITY_UNSPECIFIED: _ClassVar[Severity]
    SEVERITY_ERROR: _ClassVar[Severity]
    SEVERITY_WARNING: _ClassVar[Severity]
    SEVERITY_INFO: _ClassVar[Severity]
    SEVERITY_HINT: _ClassVar[Severity]
LINT_STATE_UNSPECIFIED: LintState
LINT_STATE_SUCCESS: LintState
LINT_STATE_ERROR: LintState
LINTER_UNSPECIFIED: Linter
SPECTRAL: Linter
OTHER: Linter
SEVERITY_UNSPECIFIED: Severity
SEVERITY_ERROR: Severity
SEVERITY_WARNING: Severity
SEVERITY_INFO: Severity
SEVERITY_HINT: Severity

class Api(_message.Message):
    __slots__ = ('name', 'display_name', 'description', 'documentation', 'owner', 'versions', 'create_time', 'update_time', 'target_user', 'team', 'business_unit', 'maturity_level', 'attributes', 'api_style', 'selected_version')

    class AttributesEntry(_message.Message):
        __slots__ = ('key', 'value')
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: AttributeValues

        def __init__(self, key: _Optional[str]=..., value: _Optional[_Union[AttributeValues, _Mapping]]=...) -> None:
            ...
    NAME_FIELD_NUMBER: _ClassVar[int]
    DISPLAY_NAME_FIELD_NUMBER: _ClassVar[int]
    DESCRIPTION_FIELD_NUMBER: _ClassVar[int]
    DOCUMENTATION_FIELD_NUMBER: _ClassVar[int]
    OWNER_FIELD_NUMBER: _ClassVar[int]
    VERSIONS_FIELD_NUMBER: _ClassVar[int]
    CREATE_TIME_FIELD_NUMBER: _ClassVar[int]
    UPDATE_TIME_FIELD_NUMBER: _ClassVar[int]
    TARGET_USER_FIELD_NUMBER: _ClassVar[int]
    TEAM_FIELD_NUMBER: _ClassVar[int]
    BUSINESS_UNIT_FIELD_NUMBER: _ClassVar[int]
    MATURITY_LEVEL_FIELD_NUMBER: _ClassVar[int]
    ATTRIBUTES_FIELD_NUMBER: _ClassVar[int]
    API_STYLE_FIELD_NUMBER: _ClassVar[int]
    SELECTED_VERSION_FIELD_NUMBER: _ClassVar[int]
    name: str
    display_name: str
    description: str
    documentation: Documentation
    owner: Owner
    versions: _containers.RepeatedScalarFieldContainer[str]
    create_time: _timestamp_pb2.Timestamp
    update_time: _timestamp_pb2.Timestamp
    target_user: AttributeValues
    team: AttributeValues
    business_unit: AttributeValues
    maturity_level: AttributeValues
    attributes: _containers.MessageMap[str, AttributeValues]
    api_style: AttributeValues
    selected_version: str

    def __init__(self, name: _Optional[str]=..., display_name: _Optional[str]=..., description: _Optional[str]=..., documentation: _Optional[_Union[Documentation, _Mapping]]=..., owner: _Optional[_Union[Owner, _Mapping]]=..., versions: _Optional[_Iterable[str]]=..., create_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]]=..., update_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]]=..., target_user: _Optional[_Union[AttributeValues, _Mapping]]=..., team: _Optional[_Union[AttributeValues, _Mapping]]=..., business_unit: _Optional[_Union[AttributeValues, _Mapping]]=..., maturity_level: _Optional[_Union[AttributeValues, _Mapping]]=..., attributes: _Optional[_Mapping[str, AttributeValues]]=..., api_style: _Optional[_Union[AttributeValues, _Mapping]]=..., selected_version: _Optional[str]=...) -> None:
        ...

class Version(_message.Message):
    __slots__ = ('name', 'display_name', 'description', 'documentation', 'specs', 'api_operations', 'definitions', 'deployments', 'create_time', 'update_time', 'lifecycle', 'compliance', 'accreditation', 'attributes', 'selected_deployment')

    class AttributesEntry(_message.Message):
        __slots__ = ('key', 'value')
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: AttributeValues

        def __init__(self, key: _Optional[str]=..., value: _Optional[_Union[AttributeValues, _Mapping]]=...) -> None:
            ...
    NAME_FIELD_NUMBER: _ClassVar[int]
    DISPLAY_NAME_FIELD_NUMBER: _ClassVar[int]
    DESCRIPTION_FIELD_NUMBER: _ClassVar[int]
    DOCUMENTATION_FIELD_NUMBER: _ClassVar[int]
    SPECS_FIELD_NUMBER: _ClassVar[int]
    API_OPERATIONS_FIELD_NUMBER: _ClassVar[int]
    DEFINITIONS_FIELD_NUMBER: _ClassVar[int]
    DEPLOYMENTS_FIELD_NUMBER: _ClassVar[int]
    CREATE_TIME_FIELD_NUMBER: _ClassVar[int]
    UPDATE_TIME_FIELD_NUMBER: _ClassVar[int]
    LIFECYCLE_FIELD_NUMBER: _ClassVar[int]
    COMPLIANCE_FIELD_NUMBER: _ClassVar[int]
    ACCREDITATION_FIELD_NUMBER: _ClassVar[int]
    ATTRIBUTES_FIELD_NUMBER: _ClassVar[int]
    SELECTED_DEPLOYMENT_FIELD_NUMBER: _ClassVar[int]
    name: str
    display_name: str
    description: str
    documentation: Documentation
    specs: _containers.RepeatedScalarFieldContainer[str]
    api_operations: _containers.RepeatedScalarFieldContainer[str]
    definitions: _containers.RepeatedScalarFieldContainer[str]
    deployments: _containers.RepeatedScalarFieldContainer[str]
    create_time: _timestamp_pb2.Timestamp
    update_time: _timestamp_pb2.Timestamp
    lifecycle: AttributeValues
    compliance: AttributeValues
    accreditation: AttributeValues
    attributes: _containers.MessageMap[str, AttributeValues]
    selected_deployment: str

    def __init__(self, name: _Optional[str]=..., display_name: _Optional[str]=..., description: _Optional[str]=..., documentation: _Optional[_Union[Documentation, _Mapping]]=..., specs: _Optional[_Iterable[str]]=..., api_operations: _Optional[_Iterable[str]]=..., definitions: _Optional[_Iterable[str]]=..., deployments: _Optional[_Iterable[str]]=..., create_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]]=..., update_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]]=..., lifecycle: _Optional[_Union[AttributeValues, _Mapping]]=..., compliance: _Optional[_Union[AttributeValues, _Mapping]]=..., accreditation: _Optional[_Union[AttributeValues, _Mapping]]=..., attributes: _Optional[_Mapping[str, AttributeValues]]=..., selected_deployment: _Optional[str]=...) -> None:
        ...

class Spec(_message.Message):
    __slots__ = ('name', 'display_name', 'spec_type', 'contents', 'details', 'source_uri', 'create_time', 'update_time', 'lint_response', 'attributes', 'documentation', 'parsing_mode')

    class ParsingMode(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        PARSING_MODE_UNSPECIFIED: _ClassVar[Spec.ParsingMode]
        RELAXED: _ClassVar[Spec.ParsingMode]
        STRICT: _ClassVar[Spec.ParsingMode]
    PARSING_MODE_UNSPECIFIED: Spec.ParsingMode
    RELAXED: Spec.ParsingMode
    STRICT: Spec.ParsingMode

    class AttributesEntry(_message.Message):
        __slots__ = ('key', 'value')
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: AttributeValues

        def __init__(self, key: _Optional[str]=..., value: _Optional[_Union[AttributeValues, _Mapping]]=...) -> None:
            ...
    NAME_FIELD_NUMBER: _ClassVar[int]
    DISPLAY_NAME_FIELD_NUMBER: _ClassVar[int]
    SPEC_TYPE_FIELD_NUMBER: _ClassVar[int]
    CONTENTS_FIELD_NUMBER: _ClassVar[int]
    DETAILS_FIELD_NUMBER: _ClassVar[int]
    SOURCE_URI_FIELD_NUMBER: _ClassVar[int]
    CREATE_TIME_FIELD_NUMBER: _ClassVar[int]
    UPDATE_TIME_FIELD_NUMBER: _ClassVar[int]
    LINT_RESPONSE_FIELD_NUMBER: _ClassVar[int]
    ATTRIBUTES_FIELD_NUMBER: _ClassVar[int]
    DOCUMENTATION_FIELD_NUMBER: _ClassVar[int]
    PARSING_MODE_FIELD_NUMBER: _ClassVar[int]
    name: str
    display_name: str
    spec_type: AttributeValues
    contents: SpecContents
    details: SpecDetails
    source_uri: str
    create_time: _timestamp_pb2.Timestamp
    update_time: _timestamp_pb2.Timestamp
    lint_response: LintResponse
    attributes: _containers.MessageMap[str, AttributeValues]
    documentation: Documentation
    parsing_mode: Spec.ParsingMode

    def __init__(self, name: _Optional[str]=..., display_name: _Optional[str]=..., spec_type: _Optional[_Union[AttributeValues, _Mapping]]=..., contents: _Optional[_Union[SpecContents, _Mapping]]=..., details: _Optional[_Union[SpecDetails, _Mapping]]=..., source_uri: _Optional[str]=..., create_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]]=..., update_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]]=..., lint_response: _Optional[_Union[LintResponse, _Mapping]]=..., attributes: _Optional[_Mapping[str, AttributeValues]]=..., documentation: _Optional[_Union[Documentation, _Mapping]]=..., parsing_mode: _Optional[_Union[Spec.ParsingMode, str]]=...) -> None:
        ...

class Deployment(_message.Message):
    __slots__ = ('name', 'display_name', 'description', 'documentation', 'deployment_type', 'resource_uri', 'endpoints', 'api_versions', 'create_time', 'update_time', 'slo', 'environment', 'attributes')

    class AttributesEntry(_message.Message):
        __slots__ = ('key', 'value')
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: AttributeValues

        def __init__(self, key: _Optional[str]=..., value: _Optional[_Union[AttributeValues, _Mapping]]=...) -> None:
            ...
    NAME_FIELD_NUMBER: _ClassVar[int]
    DISPLAY_NAME_FIELD_NUMBER: _ClassVar[int]
    DESCRIPTION_FIELD_NUMBER: _ClassVar[int]
    DOCUMENTATION_FIELD_NUMBER: _ClassVar[int]
    DEPLOYMENT_TYPE_FIELD_NUMBER: _ClassVar[int]
    RESOURCE_URI_FIELD_NUMBER: _ClassVar[int]
    ENDPOINTS_FIELD_NUMBER: _ClassVar[int]
    API_VERSIONS_FIELD_NUMBER: _ClassVar[int]
    CREATE_TIME_FIELD_NUMBER: _ClassVar[int]
    UPDATE_TIME_FIELD_NUMBER: _ClassVar[int]
    SLO_FIELD_NUMBER: _ClassVar[int]
    ENVIRONMENT_FIELD_NUMBER: _ClassVar[int]
    ATTRIBUTES_FIELD_NUMBER: _ClassVar[int]
    name: str
    display_name: str
    description: str
    documentation: Documentation
    deployment_type: AttributeValues
    resource_uri: str
    endpoints: _containers.RepeatedScalarFieldContainer[str]
    api_versions: _containers.RepeatedScalarFieldContainer[str]
    create_time: _timestamp_pb2.Timestamp
    update_time: _timestamp_pb2.Timestamp
    slo: AttributeValues
    environment: AttributeValues
    attributes: _containers.MessageMap[str, AttributeValues]

    def __init__(self, name: _Optional[str]=..., display_name: _Optional[str]=..., description: _Optional[str]=..., documentation: _Optional[_Union[Documentation, _Mapping]]=..., deployment_type: _Optional[_Union[AttributeValues, _Mapping]]=..., resource_uri: _Optional[str]=..., endpoints: _Optional[_Iterable[str]]=..., api_versions: _Optional[_Iterable[str]]=..., create_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]]=..., update_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]]=..., slo: _Optional[_Union[AttributeValues, _Mapping]]=..., environment: _Optional[_Union[AttributeValues, _Mapping]]=..., attributes: _Optional[_Mapping[str, AttributeValues]]=...) -> None:
        ...

class ApiOperation(_message.Message):
    __slots__ = ('name', 'spec', 'details', 'create_time', 'update_time', 'attributes')

    class AttributesEntry(_message.Message):
        __slots__ = ('key', 'value')
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: AttributeValues

        def __init__(self, key: _Optional[str]=..., value: _Optional[_Union[AttributeValues, _Mapping]]=...) -> None:
            ...
    NAME_FIELD_NUMBER: _ClassVar[int]
    SPEC_FIELD_NUMBER: _ClassVar[int]
    DETAILS_FIELD_NUMBER: _ClassVar[int]
    CREATE_TIME_FIELD_NUMBER: _ClassVar[int]
    UPDATE_TIME_FIELD_NUMBER: _ClassVar[int]
    ATTRIBUTES_FIELD_NUMBER: _ClassVar[int]
    name: str
    spec: str
    details: OperationDetails
    create_time: _timestamp_pb2.Timestamp
    update_time: _timestamp_pb2.Timestamp
    attributes: _containers.MessageMap[str, AttributeValues]

    def __init__(self, name: _Optional[str]=..., spec: _Optional[str]=..., details: _Optional[_Union[OperationDetails, _Mapping]]=..., create_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]]=..., update_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]]=..., attributes: _Optional[_Mapping[str, AttributeValues]]=...) -> None:
        ...

class Definition(_message.Message):
    __slots__ = ('schema', 'name', 'spec', 'type', 'create_time', 'update_time', 'attributes')

    class Type(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        TYPE_UNSPECIFIED: _ClassVar[Definition.Type]
        SCHEMA: _ClassVar[Definition.Type]
    TYPE_UNSPECIFIED: Definition.Type
    SCHEMA: Definition.Type

    class AttributesEntry(_message.Message):
        __slots__ = ('key', 'value')
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: AttributeValues

        def __init__(self, key: _Optional[str]=..., value: _Optional[_Union[AttributeValues, _Mapping]]=...) -> None:
            ...
    SCHEMA_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    SPEC_FIELD_NUMBER: _ClassVar[int]
    TYPE_FIELD_NUMBER: _ClassVar[int]
    CREATE_TIME_FIELD_NUMBER: _ClassVar[int]
    UPDATE_TIME_FIELD_NUMBER: _ClassVar[int]
    ATTRIBUTES_FIELD_NUMBER: _ClassVar[int]
    schema: Schema
    name: str
    spec: str
    type: Definition.Type
    create_time: _timestamp_pb2.Timestamp
    update_time: _timestamp_pb2.Timestamp
    attributes: _containers.MessageMap[str, AttributeValues]

    def __init__(self, schema: _Optional[_Union[Schema, _Mapping]]=..., name: _Optional[str]=..., spec: _Optional[str]=..., type: _Optional[_Union[Definition.Type, str]]=..., create_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]]=..., update_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]]=..., attributes: _Optional[_Mapping[str, AttributeValues]]=...) -> None:
        ...

class Attribute(_message.Message):
    __slots__ = ('name', 'display_name', 'description', 'definition_type', 'scope', 'data_type', 'allowed_values', 'cardinality', 'mandatory', 'create_time', 'update_time')

    class DefinitionType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        DEFINITION_TYPE_UNSPECIFIED: _ClassVar[Attribute.DefinitionType]
        SYSTEM_DEFINED: _ClassVar[Attribute.DefinitionType]
        USER_DEFINED: _ClassVar[Attribute.DefinitionType]
    DEFINITION_TYPE_UNSPECIFIED: Attribute.DefinitionType
    SYSTEM_DEFINED: Attribute.DefinitionType
    USER_DEFINED: Attribute.DefinitionType

    class Scope(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        SCOPE_UNSPECIFIED: _ClassVar[Attribute.Scope]
        API: _ClassVar[Attribute.Scope]
        VERSION: _ClassVar[Attribute.Scope]
        SPEC: _ClassVar[Attribute.Scope]
        API_OPERATION: _ClassVar[Attribute.Scope]
        DEPLOYMENT: _ClassVar[Attribute.Scope]
        DEPENDENCY: _ClassVar[Attribute.Scope]
        DEFINITION: _ClassVar[Attribute.Scope]
        EXTERNAL_API: _ClassVar[Attribute.Scope]
        PLUGIN: _ClassVar[Attribute.Scope]
    SCOPE_UNSPECIFIED: Attribute.Scope
    API: Attribute.Scope
    VERSION: Attribute.Scope
    SPEC: Attribute.Scope
    API_OPERATION: Attribute.Scope
    DEPLOYMENT: Attribute.Scope
    DEPENDENCY: Attribute.Scope
    DEFINITION: Attribute.Scope
    EXTERNAL_API: Attribute.Scope
    PLUGIN: Attribute.Scope

    class DataType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        DATA_TYPE_UNSPECIFIED: _ClassVar[Attribute.DataType]
        ENUM: _ClassVar[Attribute.DataType]
        JSON: _ClassVar[Attribute.DataType]
        STRING: _ClassVar[Attribute.DataType]
    DATA_TYPE_UNSPECIFIED: Attribute.DataType
    ENUM: Attribute.DataType
    JSON: Attribute.DataType
    STRING: Attribute.DataType

    class AllowedValue(_message.Message):
        __slots__ = ('id', 'display_name', 'description', 'immutable')
        ID_FIELD_NUMBER: _ClassVar[int]
        DISPLAY_NAME_FIELD_NUMBER: _ClassVar[int]
        DESCRIPTION_FIELD_NUMBER: _ClassVar[int]
        IMMUTABLE_FIELD_NUMBER: _ClassVar[int]
        id: str
        display_name: str
        description: str
        immutable: bool

        def __init__(self, id: _Optional[str]=..., display_name: _Optional[str]=..., description: _Optional[str]=..., immutable: bool=...) -> None:
            ...
    NAME_FIELD_NUMBER: _ClassVar[int]
    DISPLAY_NAME_FIELD_NUMBER: _ClassVar[int]
    DESCRIPTION_FIELD_NUMBER: _ClassVar[int]
    DEFINITION_TYPE_FIELD_NUMBER: _ClassVar[int]
    SCOPE_FIELD_NUMBER: _ClassVar[int]
    DATA_TYPE_FIELD_NUMBER: _ClassVar[int]
    ALLOWED_VALUES_FIELD_NUMBER: _ClassVar[int]
    CARDINALITY_FIELD_NUMBER: _ClassVar[int]
    MANDATORY_FIELD_NUMBER: _ClassVar[int]
    CREATE_TIME_FIELD_NUMBER: _ClassVar[int]
    UPDATE_TIME_FIELD_NUMBER: _ClassVar[int]
    name: str
    display_name: str
    description: str
    definition_type: Attribute.DefinitionType
    scope: Attribute.Scope
    data_type: Attribute.DataType
    allowed_values: _containers.RepeatedCompositeFieldContainer[Attribute.AllowedValue]
    cardinality: int
    mandatory: bool
    create_time: _timestamp_pb2.Timestamp
    update_time: _timestamp_pb2.Timestamp

    def __init__(self, name: _Optional[str]=..., display_name: _Optional[str]=..., description: _Optional[str]=..., definition_type: _Optional[_Union[Attribute.DefinitionType, str]]=..., scope: _Optional[_Union[Attribute.Scope, str]]=..., data_type: _Optional[_Union[Attribute.DataType, str]]=..., allowed_values: _Optional[_Iterable[_Union[Attribute.AllowedValue, _Mapping]]]=..., cardinality: _Optional[int]=..., mandatory: bool=..., create_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]]=..., update_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]]=...) -> None:
        ...

class SpecContents(_message.Message):
    __slots__ = ('contents', 'mime_type')
    CONTENTS_FIELD_NUMBER: _ClassVar[int]
    MIME_TYPE_FIELD_NUMBER: _ClassVar[int]
    contents: bytes
    mime_type: str

    def __init__(self, contents: _Optional[bytes]=..., mime_type: _Optional[str]=...) -> None:
        ...

class SpecDetails(_message.Message):
    __slots__ = ('open_api_spec_details', 'description')
    OPEN_API_SPEC_DETAILS_FIELD_NUMBER: _ClassVar[int]
    DESCRIPTION_FIELD_NUMBER: _ClassVar[int]
    open_api_spec_details: OpenApiSpecDetails
    description: str

    def __init__(self, open_api_spec_details: _Optional[_Union[OpenApiSpecDetails, _Mapping]]=..., description: _Optional[str]=...) -> None:
        ...

class OpenApiSpecDetails(_message.Message):
    __slots__ = ('format', 'version', 'owner')

    class Format(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        FORMAT_UNSPECIFIED: _ClassVar[OpenApiSpecDetails.Format]
        OPEN_API_SPEC_2_0: _ClassVar[OpenApiSpecDetails.Format]
        OPEN_API_SPEC_3_0: _ClassVar[OpenApiSpecDetails.Format]
        OPEN_API_SPEC_3_1: _ClassVar[OpenApiSpecDetails.Format]
    FORMAT_UNSPECIFIED: OpenApiSpecDetails.Format
    OPEN_API_SPEC_2_0: OpenApiSpecDetails.Format
    OPEN_API_SPEC_3_0: OpenApiSpecDetails.Format
    OPEN_API_SPEC_3_1: OpenApiSpecDetails.Format
    FORMAT_FIELD_NUMBER: _ClassVar[int]
    VERSION_FIELD_NUMBER: _ClassVar[int]
    OWNER_FIELD_NUMBER: _ClassVar[int]
    format: OpenApiSpecDetails.Format
    version: str
    owner: Owner

    def __init__(self, format: _Optional[_Union[OpenApiSpecDetails.Format, str]]=..., version: _Optional[str]=..., owner: _Optional[_Union[Owner, _Mapping]]=...) -> None:
        ...

class OperationDetails(_message.Message):
    __slots__ = ('http_operation', 'description', 'documentation', 'deprecated')
    HTTP_OPERATION_FIELD_NUMBER: _ClassVar[int]
    DESCRIPTION_FIELD_NUMBER: _ClassVar[int]
    DOCUMENTATION_FIELD_NUMBER: _ClassVar[int]
    DEPRECATED_FIELD_NUMBER: _ClassVar[int]
    http_operation: HttpOperation
    description: str
    documentation: Documentation
    deprecated: bool

    def __init__(self, http_operation: _Optional[_Union[HttpOperation, _Mapping]]=..., description: _Optional[str]=..., documentation: _Optional[_Union[Documentation, _Mapping]]=..., deprecated: bool=...) -> None:
        ...

class HttpOperation(_message.Message):
    __slots__ = ('path', 'method')

    class Method(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        METHOD_UNSPECIFIED: _ClassVar[HttpOperation.Method]
        GET: _ClassVar[HttpOperation.Method]
        PUT: _ClassVar[HttpOperation.Method]
        POST: _ClassVar[HttpOperation.Method]
        DELETE: _ClassVar[HttpOperation.Method]
        OPTIONS: _ClassVar[HttpOperation.Method]
        HEAD: _ClassVar[HttpOperation.Method]
        PATCH: _ClassVar[HttpOperation.Method]
        TRACE: _ClassVar[HttpOperation.Method]
    METHOD_UNSPECIFIED: HttpOperation.Method
    GET: HttpOperation.Method
    PUT: HttpOperation.Method
    POST: HttpOperation.Method
    DELETE: HttpOperation.Method
    OPTIONS: HttpOperation.Method
    HEAD: HttpOperation.Method
    PATCH: HttpOperation.Method
    TRACE: HttpOperation.Method
    PATH_FIELD_NUMBER: _ClassVar[int]
    METHOD_FIELD_NUMBER: _ClassVar[int]
    path: Path
    method: HttpOperation.Method

    def __init__(self, path: _Optional[_Union[Path, _Mapping]]=..., method: _Optional[_Union[HttpOperation.Method, str]]=...) -> None:
        ...

class Path(_message.Message):
    __slots__ = ('path', 'description')
    PATH_FIELD_NUMBER: _ClassVar[int]
    DESCRIPTION_FIELD_NUMBER: _ClassVar[int]
    path: str
    description: str

    def __init__(self, path: _Optional[str]=..., description: _Optional[str]=...) -> None:
        ...

class Schema(_message.Message):
    __slots__ = ('display_name', 'raw_value')
    DISPLAY_NAME_FIELD_NUMBER: _ClassVar[int]
    RAW_VALUE_FIELD_NUMBER: _ClassVar[int]
    display_name: str
    raw_value: bytes

    def __init__(self, display_name: _Optional[str]=..., raw_value: _Optional[bytes]=...) -> None:
        ...

class Owner(_message.Message):
    __slots__ = ('display_name', 'email')
    DISPLAY_NAME_FIELD_NUMBER: _ClassVar[int]
    EMAIL_FIELD_NUMBER: _ClassVar[int]
    display_name: str
    email: str

    def __init__(self, display_name: _Optional[str]=..., email: _Optional[str]=...) -> None:
        ...

class Documentation(_message.Message):
    __slots__ = ('external_uri',)
    EXTERNAL_URI_FIELD_NUMBER: _ClassVar[int]
    external_uri: str

    def __init__(self, external_uri: _Optional[str]=...) -> None:
        ...

class AttributeValues(_message.Message):
    __slots__ = ('enum_values', 'string_values', 'json_values', 'attribute')

    class EnumAttributeValues(_message.Message):
        __slots__ = ('values',)
        VALUES_FIELD_NUMBER: _ClassVar[int]
        values: _containers.RepeatedCompositeFieldContainer[Attribute.AllowedValue]

        def __init__(self, values: _Optional[_Iterable[_Union[Attribute.AllowedValue, _Mapping]]]=...) -> None:
            ...

    class StringAttributeValues(_message.Message):
        __slots__ = ('values',)
        VALUES_FIELD_NUMBER: _ClassVar[int]
        values: _containers.RepeatedScalarFieldContainer[str]

        def __init__(self, values: _Optional[_Iterable[str]]=...) -> None:
            ...
    ENUM_VALUES_FIELD_NUMBER: _ClassVar[int]
    STRING_VALUES_FIELD_NUMBER: _ClassVar[int]
    JSON_VALUES_FIELD_NUMBER: _ClassVar[int]
    ATTRIBUTE_FIELD_NUMBER: _ClassVar[int]
    enum_values: AttributeValues.EnumAttributeValues
    string_values: AttributeValues.StringAttributeValues
    json_values: AttributeValues.StringAttributeValues
    attribute: str

    def __init__(self, enum_values: _Optional[_Union[AttributeValues.EnumAttributeValues, _Mapping]]=..., string_values: _Optional[_Union[AttributeValues.StringAttributeValues, _Mapping]]=..., json_values: _Optional[_Union[AttributeValues.StringAttributeValues, _Mapping]]=..., attribute: _Optional[str]=...) -> None:
        ...

class Dependency(_message.Message):
    __slots__ = ('name', 'consumer', 'supplier', 'state', 'description', 'discovery_mode', 'error_detail', 'create_time', 'update_time', 'attributes')

    class State(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        STATE_UNSPECIFIED: _ClassVar[Dependency.State]
        PROPOSED: _ClassVar[Dependency.State]
        VALIDATED: _ClassVar[Dependency.State]
    STATE_UNSPECIFIED: Dependency.State
    PROPOSED: Dependency.State
    VALIDATED: Dependency.State

    class DiscoveryMode(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        DISCOVERY_MODE_UNSPECIFIED: _ClassVar[Dependency.DiscoveryMode]
        MANUAL: _ClassVar[Dependency.DiscoveryMode]
    DISCOVERY_MODE_UNSPECIFIED: Dependency.DiscoveryMode
    MANUAL: Dependency.DiscoveryMode

    class AttributesEntry(_message.Message):
        __slots__ = ('key', 'value')
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: AttributeValues

        def __init__(self, key: _Optional[str]=..., value: _Optional[_Union[AttributeValues, _Mapping]]=...) -> None:
            ...
    NAME_FIELD_NUMBER: _ClassVar[int]
    CONSUMER_FIELD_NUMBER: _ClassVar[int]
    SUPPLIER_FIELD_NUMBER: _ClassVar[int]
    STATE_FIELD_NUMBER: _ClassVar[int]
    DESCRIPTION_FIELD_NUMBER: _ClassVar[int]
    DISCOVERY_MODE_FIELD_NUMBER: _ClassVar[int]
    ERROR_DETAIL_FIELD_NUMBER: _ClassVar[int]
    CREATE_TIME_FIELD_NUMBER: _ClassVar[int]
    UPDATE_TIME_FIELD_NUMBER: _ClassVar[int]
    ATTRIBUTES_FIELD_NUMBER: _ClassVar[int]
    name: str
    consumer: DependencyEntityReference
    supplier: DependencyEntityReference
    state: Dependency.State
    description: str
    discovery_mode: Dependency.DiscoveryMode
    error_detail: DependencyErrorDetail
    create_time: _timestamp_pb2.Timestamp
    update_time: _timestamp_pb2.Timestamp
    attributes: _containers.MessageMap[str, AttributeValues]

    def __init__(self, name: _Optional[str]=..., consumer: _Optional[_Union[DependencyEntityReference, _Mapping]]=..., supplier: _Optional[_Union[DependencyEntityReference, _Mapping]]=..., state: _Optional[_Union[Dependency.State, str]]=..., description: _Optional[str]=..., discovery_mode: _Optional[_Union[Dependency.DiscoveryMode, str]]=..., error_detail: _Optional[_Union[DependencyErrorDetail, _Mapping]]=..., create_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]]=..., update_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]]=..., attributes: _Optional[_Mapping[str, AttributeValues]]=...) -> None:
        ...

class DependencyEntityReference(_message.Message):
    __slots__ = ('operation_resource_name', 'external_api_resource_name', 'display_name')
    OPERATION_RESOURCE_NAME_FIELD_NUMBER: _ClassVar[int]
    EXTERNAL_API_RESOURCE_NAME_FIELD_NUMBER: _ClassVar[int]
    DISPLAY_NAME_FIELD_NUMBER: _ClassVar[int]
    operation_resource_name: str
    external_api_resource_name: str
    display_name: str

    def __init__(self, operation_resource_name: _Optional[str]=..., external_api_resource_name: _Optional[str]=..., display_name: _Optional[str]=...) -> None:
        ...

class DependencyErrorDetail(_message.Message):
    __slots__ = ('error', 'error_time')

    class Error(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        ERROR_UNSPECIFIED: _ClassVar[DependencyErrorDetail.Error]
        SUPPLIER_NOT_FOUND: _ClassVar[DependencyErrorDetail.Error]
        SUPPLIER_RECREATED: _ClassVar[DependencyErrorDetail.Error]
    ERROR_UNSPECIFIED: DependencyErrorDetail.Error
    SUPPLIER_NOT_FOUND: DependencyErrorDetail.Error
    SUPPLIER_RECREATED: DependencyErrorDetail.Error
    ERROR_FIELD_NUMBER: _ClassVar[int]
    ERROR_TIME_FIELD_NUMBER: _ClassVar[int]
    error: DependencyErrorDetail.Error
    error_time: _timestamp_pb2.Timestamp

    def __init__(self, error: _Optional[_Union[DependencyErrorDetail.Error, str]]=..., error_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]]=...) -> None:
        ...

class LintResponse(_message.Message):
    __slots__ = ('issues', 'summary', 'state', 'source', 'linter', 'create_time')

    class SummaryEntry(_message.Message):
        __slots__ = ('severity', 'count')
        SEVERITY_FIELD_NUMBER: _ClassVar[int]
        COUNT_FIELD_NUMBER: _ClassVar[int]
        severity: Severity
        count: int

        def __init__(self, severity: _Optional[_Union[Severity, str]]=..., count: _Optional[int]=...) -> None:
            ...
    ISSUES_FIELD_NUMBER: _ClassVar[int]
    SUMMARY_FIELD_NUMBER: _ClassVar[int]
    STATE_FIELD_NUMBER: _ClassVar[int]
    SOURCE_FIELD_NUMBER: _ClassVar[int]
    LINTER_FIELD_NUMBER: _ClassVar[int]
    CREATE_TIME_FIELD_NUMBER: _ClassVar[int]
    issues: _containers.RepeatedCompositeFieldContainer[Issue]
    summary: _containers.RepeatedCompositeFieldContainer[LintResponse.SummaryEntry]
    state: LintState
    source: str
    linter: Linter
    create_time: _timestamp_pb2.Timestamp

    def __init__(self, issues: _Optional[_Iterable[_Union[Issue, _Mapping]]]=..., summary: _Optional[_Iterable[_Union[LintResponse.SummaryEntry, _Mapping]]]=..., state: _Optional[_Union[LintState, str]]=..., source: _Optional[str]=..., linter: _Optional[_Union[Linter, str]]=..., create_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]]=...) -> None:
        ...

class Issue(_message.Message):
    __slots__ = ('code', 'path', 'message', 'severity', 'range')
    CODE_FIELD_NUMBER: _ClassVar[int]
    PATH_FIELD_NUMBER: _ClassVar[int]
    MESSAGE_FIELD_NUMBER: _ClassVar[int]
    SEVERITY_FIELD_NUMBER: _ClassVar[int]
    RANGE_FIELD_NUMBER: _ClassVar[int]
    code: str
    path: _containers.RepeatedScalarFieldContainer[str]
    message: str
    severity: Severity
    range: Range

    def __init__(self, code: _Optional[str]=..., path: _Optional[_Iterable[str]]=..., message: _Optional[str]=..., severity: _Optional[_Union[Severity, str]]=..., range: _Optional[_Union[Range, _Mapping]]=...) -> None:
        ...

class Range(_message.Message):
    __slots__ = ('start', 'end')
    START_FIELD_NUMBER: _ClassVar[int]
    END_FIELD_NUMBER: _ClassVar[int]
    start: Point
    end: Point

    def __init__(self, start: _Optional[_Union[Point, _Mapping]]=..., end: _Optional[_Union[Point, _Mapping]]=...) -> None:
        ...

class Point(_message.Message):
    __slots__ = ('line', 'character')
    LINE_FIELD_NUMBER: _ClassVar[int]
    CHARACTER_FIELD_NUMBER: _ClassVar[int]
    line: int
    character: int

    def __init__(self, line: _Optional[int]=..., character: _Optional[int]=...) -> None:
        ...

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

class ApiHubInstance(_message.Message):
    __slots__ = ('name', 'create_time', 'update_time', 'state', 'state_message', 'config', 'labels', 'description')

    class State(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        STATE_UNSPECIFIED: _ClassVar[ApiHubInstance.State]
        INACTIVE: _ClassVar[ApiHubInstance.State]
        CREATING: _ClassVar[ApiHubInstance.State]
        ACTIVE: _ClassVar[ApiHubInstance.State]
        UPDATING: _ClassVar[ApiHubInstance.State]
        DELETING: _ClassVar[ApiHubInstance.State]
        FAILED: _ClassVar[ApiHubInstance.State]
    STATE_UNSPECIFIED: ApiHubInstance.State
    INACTIVE: ApiHubInstance.State
    CREATING: ApiHubInstance.State
    ACTIVE: ApiHubInstance.State
    UPDATING: ApiHubInstance.State
    DELETING: ApiHubInstance.State
    FAILED: ApiHubInstance.State

    class Config(_message.Message):
        __slots__ = ('cmek_key_name',)
        CMEK_KEY_NAME_FIELD_NUMBER: _ClassVar[int]
        cmek_key_name: str

        def __init__(self, cmek_key_name: _Optional[str]=...) -> None:
            ...

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
    STATE_FIELD_NUMBER: _ClassVar[int]
    STATE_MESSAGE_FIELD_NUMBER: _ClassVar[int]
    CONFIG_FIELD_NUMBER: _ClassVar[int]
    LABELS_FIELD_NUMBER: _ClassVar[int]
    DESCRIPTION_FIELD_NUMBER: _ClassVar[int]
    name: str
    create_time: _timestamp_pb2.Timestamp
    update_time: _timestamp_pb2.Timestamp
    state: ApiHubInstance.State
    state_message: str
    config: ApiHubInstance.Config
    labels: _containers.ScalarMap[str, str]
    description: str

    def __init__(self, name: _Optional[str]=..., create_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]]=..., update_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]]=..., state: _Optional[_Union[ApiHubInstance.State, str]]=..., state_message: _Optional[str]=..., config: _Optional[_Union[ApiHubInstance.Config, _Mapping]]=..., labels: _Optional[_Mapping[str, str]]=..., description: _Optional[str]=...) -> None:
        ...

class ExternalApi(_message.Message):
    __slots__ = ('name', 'display_name', 'description', 'endpoints', 'paths', 'documentation', 'attributes', 'create_time', 'update_time')

    class AttributesEntry(_message.Message):
        __slots__ = ('key', 'value')
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: AttributeValues

        def __init__(self, key: _Optional[str]=..., value: _Optional[_Union[AttributeValues, _Mapping]]=...) -> None:
            ...
    NAME_FIELD_NUMBER: _ClassVar[int]
    DISPLAY_NAME_FIELD_NUMBER: _ClassVar[int]
    DESCRIPTION_FIELD_NUMBER: _ClassVar[int]
    ENDPOINTS_FIELD_NUMBER: _ClassVar[int]
    PATHS_FIELD_NUMBER: _ClassVar[int]
    DOCUMENTATION_FIELD_NUMBER: _ClassVar[int]
    ATTRIBUTES_FIELD_NUMBER: _ClassVar[int]
    CREATE_TIME_FIELD_NUMBER: _ClassVar[int]
    UPDATE_TIME_FIELD_NUMBER: _ClassVar[int]
    name: str
    display_name: str
    description: str
    endpoints: _containers.RepeatedScalarFieldContainer[str]
    paths: _containers.RepeatedScalarFieldContainer[str]
    documentation: Documentation
    attributes: _containers.MessageMap[str, AttributeValues]
    create_time: _timestamp_pb2.Timestamp
    update_time: _timestamp_pb2.Timestamp

    def __init__(self, name: _Optional[str]=..., display_name: _Optional[str]=..., description: _Optional[str]=..., endpoints: _Optional[_Iterable[str]]=..., paths: _Optional[_Iterable[str]]=..., documentation: _Optional[_Union[Documentation, _Mapping]]=..., attributes: _Optional[_Mapping[str, AttributeValues]]=..., create_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]]=..., update_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]]=...) -> None:
        ...