"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_runtime_version.ValidateProtobufRuntimeVersion(_runtime_version.Domain.PUBLIC, 5, 28, 1, '', 'google/cloud/connectors/v1/common.proto')
_sym_db = _symbol_database.Default()
from .....google.api import field_behavior_pb2 as google_dot_api_dot_field__behavior__pb2
from google.protobuf import timestamp_pb2 as google_dot_protobuf_dot_timestamp__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\'google/cloud/connectors/v1/common.proto\x12\x1agoogle.cloud.connectors.v1\x1a\x1fgoogle/api/field_behavior.proto\x1a\x1fgoogle/protobuf/timestamp.proto"\x80\x02\n\x11OperationMetadata\x124\n\x0bcreate_time\x18\x01 \x01(\x0b2\x1a.google.protobuf.TimestampB\x03\xe0A\x03\x121\n\x08end_time\x18\x02 \x01(\x0b2\x1a.google.protobuf.TimestampB\x03\xe0A\x03\x12\x13\n\x06target\x18\x03 \x01(\tB\x03\xe0A\x03\x12\x11\n\x04verb\x18\x04 \x01(\tB\x03\xe0A\x03\x12\x1b\n\x0estatus_message\x18\x05 \x01(\tB\x03\xe0A\x03\x12#\n\x16requested_cancellation\x18\x06 \x01(\x08B\x03\xe0A\x03\x12\x18\n\x0bapi_version\x18\x07 \x01(\tB\x03\xe0A\x03"\xab\x05\n\x16ConfigVariableTemplate\x12\x0b\n\x03key\x18\x01 \x01(\t\x12P\n\nvalue_type\x18\x02 \x01(\x0e2<.google.cloud.connectors.v1.ConfigVariableTemplate.ValueType\x12\x14\n\x0cdisplay_name\x18\x03 \x01(\t\x12\x13\n\x0bdescription\x18\x04 \x01(\t\x12\x18\n\x10validation_regex\x18\x05 \x01(\t\x12\x10\n\x08required\x18\x06 \x01(\x08\x129\n\nrole_grant\x18\x07 \x01(\x0b2%.google.cloud.connectors.v1.RoleGrant\x12<\n\x0cenum_options\x18\x08 \x03(\x0b2&.google.cloud.connectors.v1.EnumOption\x12R\n\x17authorization_code_link\x18\t \x01(\x0b21.google.cloud.connectors.v1.AuthorizationCodeLink\x12G\n\x05state\x18\n \x01(\x0e28.google.cloud.connectors.v1.ConfigVariableTemplate.State\x12\x13\n\x0bis_advanced\x18\x0b \x01(\x08"t\n\tValueType\x12\x1a\n\x16VALUE_TYPE_UNSPECIFIED\x10\x00\x12\n\n\x06STRING\x10\x01\x12\x07\n\x03INT\x10\x02\x12\x08\n\x04BOOL\x10\x03\x12\n\n\x06SECRET\x10\x04\x12\x08\n\x04ENUM\x10\x05\x12\x16\n\x12AUTHORIZATION_CODE\x10\x06":\n\x05State\x12\x15\n\x11STATE_UNSPECIFIED\x10\x00\x12\n\n\x06ACTIVE\x10\x01\x12\x0e\n\nDEPRECATED\x10\x02" \n\x06Secret\x12\x16\n\x0esecret_version\x18\x01 \x01(\t".\n\nEnumOption\x12\n\n\x02id\x18\x01 \x01(\t\x12\x14\n\x0cdisplay_name\x18\x02 \x01(\t"\xa5\x01\n\x0eConfigVariable\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\x13\n\tint_value\x18\x02 \x01(\x03H\x00\x12\x14\n\nbool_value\x18\x03 \x01(\x08H\x00\x12\x16\n\x0cstring_value\x18\x04 \x01(\tH\x00\x12:\n\x0csecret_value\x18\x05 \x01(\x0b2".google.cloud.connectors.v1.SecretH\x00B\x07\n\x05value"\xe5\x03\n\tRoleGrant\x12B\n\tprincipal\x18\x01 \x01(\x0e2/.google.cloud.connectors.v1.RoleGrant.Principal\x12\r\n\x05roles\x18\x02 \x03(\t\x12@\n\x08resource\x18\x03 \x01(\x0b2..google.cloud.connectors.v1.RoleGrant.Resource\x12\x1c\n\x14helper_text_template\x18\x04 \x01(\t\x1a\xea\x01\n\x08Resource\x12A\n\x04type\x18\x01 \x01(\x0e23.google.cloud.connectors.v1.RoleGrant.Resource.Type\x12\x15\n\rpath_template\x18\x03 \x01(\t"\x83\x01\n\x04Type\x12\x14\n\x10TYPE_UNSPECIFIED\x10\x00\x12\x0f\n\x0bGCP_PROJECT\x10\x01\x12\x10\n\x0cGCP_RESOURCE\x10\x02\x12\x1c\n\x18GCP_SECRETMANAGER_SECRET\x10\x03\x12$\n GCP_SECRETMANAGER_SECRET_VERSION\x10\x04"8\n\tPrincipal\x12\x19\n\x15PRINCIPAL_UNSPECIFIED\x10\x00\x12\x10\n\x0cCONNECTOR_SA\x10\x01"\\\n\x15AuthorizationCodeLink\x12\x0b\n\x03uri\x18\x01 \x01(\t\x12\x0e\n\x06scopes\x18\x02 \x03(\t\x12\x11\n\tclient_id\x18\x03 \x01(\t\x12\x13\n\x0benable_pkce\x18\x04 \x01(\x08*e\n\x0bLaunchStage\x12\x1c\n\x18LAUNCH_STAGE_UNSPECIFIED\x10\x00\x12\x0b\n\x07PREVIEW\x10\x01\x12\x06\n\x02GA\x10\x02\x12\x0e\n\nDEPRECATED\x10\x03\x12\x13\n\x0fPRIVATE_PREVIEW\x10\x05Bo\n\x1ecom.google.cloud.connectors.v1B\x0bCommonProtoP\x01Z>cloud.google.com/go/connectors/apiv1/connectorspb;connectorspbb\x06proto3')
_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'google.cloud.connectors.v1.common_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
    _globals['DESCRIPTOR']._loaded_options = None
    _globals['DESCRIPTOR']._serialized_options = b'\n\x1ecom.google.cloud.connectors.v1B\x0bCommonProtoP\x01Z>cloud.google.com/go/connectors/apiv1/connectorspb;connectorspb'
    _globals['_OPERATIONMETADATA'].fields_by_name['create_time']._loaded_options = None
    _globals['_OPERATIONMETADATA'].fields_by_name['create_time']._serialized_options = b'\xe0A\x03'
    _globals['_OPERATIONMETADATA'].fields_by_name['end_time']._loaded_options = None
    _globals['_OPERATIONMETADATA'].fields_by_name['end_time']._serialized_options = b'\xe0A\x03'
    _globals['_OPERATIONMETADATA'].fields_by_name['target']._loaded_options = None
    _globals['_OPERATIONMETADATA'].fields_by_name['target']._serialized_options = b'\xe0A\x03'
    _globals['_OPERATIONMETADATA'].fields_by_name['verb']._loaded_options = None
    _globals['_OPERATIONMETADATA'].fields_by_name['verb']._serialized_options = b'\xe0A\x03'
    _globals['_OPERATIONMETADATA'].fields_by_name['status_message']._loaded_options = None
    _globals['_OPERATIONMETADATA'].fields_by_name['status_message']._serialized_options = b'\xe0A\x03'
    _globals['_OPERATIONMETADATA'].fields_by_name['requested_cancellation']._loaded_options = None
    _globals['_OPERATIONMETADATA'].fields_by_name['requested_cancellation']._serialized_options = b'\xe0A\x03'
    _globals['_OPERATIONMETADATA'].fields_by_name['api_version']._loaded_options = None
    _globals['_OPERATIONMETADATA'].fields_by_name['api_version']._serialized_options = b'\xe0A\x03'
    _globals['_LAUNCHSTAGE']._serialized_start = 1914
    _globals['_LAUNCHSTAGE']._serialized_end = 2015
    _globals['_OPERATIONMETADATA']._serialized_start = 138
    _globals['_OPERATIONMETADATA']._serialized_end = 394
    _globals['_CONFIGVARIABLETEMPLATE']._serialized_start = 397
    _globals['_CONFIGVARIABLETEMPLATE']._serialized_end = 1080
    _globals['_CONFIGVARIABLETEMPLATE_VALUETYPE']._serialized_start = 904
    _globals['_CONFIGVARIABLETEMPLATE_VALUETYPE']._serialized_end = 1020
    _globals['_CONFIGVARIABLETEMPLATE_STATE']._serialized_start = 1022
    _globals['_CONFIGVARIABLETEMPLATE_STATE']._serialized_end = 1080
    _globals['_SECRET']._serialized_start = 1082
    _globals['_SECRET']._serialized_end = 1114
    _globals['_ENUMOPTION']._serialized_start = 1116
    _globals['_ENUMOPTION']._serialized_end = 1162
    _globals['_CONFIGVARIABLE']._serialized_start = 1165
    _globals['_CONFIGVARIABLE']._serialized_end = 1330
    _globals['_ROLEGRANT']._serialized_start = 1333
    _globals['_ROLEGRANT']._serialized_end = 1818
    _globals['_ROLEGRANT_RESOURCE']._serialized_start = 1526
    _globals['_ROLEGRANT_RESOURCE']._serialized_end = 1760
    _globals['_ROLEGRANT_RESOURCE_TYPE']._serialized_start = 1629
    _globals['_ROLEGRANT_RESOURCE_TYPE']._serialized_end = 1760
    _globals['_ROLEGRANT_PRINCIPAL']._serialized_start = 1762
    _globals['_ROLEGRANT_PRINCIPAL']._serialized_end = 1818
    _globals['_AUTHORIZATIONCODELINK']._serialized_start = 1820
    _globals['_AUTHORIZATIONCODELINK']._serialized_end = 1912