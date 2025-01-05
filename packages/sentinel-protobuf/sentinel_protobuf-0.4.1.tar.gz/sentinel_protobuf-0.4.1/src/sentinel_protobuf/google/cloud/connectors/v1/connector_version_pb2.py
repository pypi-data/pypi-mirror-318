"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_runtime_version.ValidateProtobufRuntimeVersion(_runtime_version.Domain.PUBLIC, 5, 28, 1, '', 'google/cloud/connectors/v1/connector_version.proto')
_sym_db = _symbol_database.Default()
from .....google.api import field_behavior_pb2 as google_dot_api_dot_field__behavior__pb2
from .....google.api import resource_pb2 as google_dot_api_dot_resource__pb2
from .....google.cloud.connectors.v1 import authconfig_pb2 as google_dot_cloud_dot_connectors_dot_v1_dot_authconfig__pb2
from .....google.cloud.connectors.v1 import common_pb2 as google_dot_cloud_dot_connectors_dot_v1_dot_common__pb2
from .....google.cloud.connectors.v1 import ssl_config_pb2 as google_dot_cloud_dot_connectors_dot_v1_dot_ssl__config__pb2
from google.protobuf import timestamp_pb2 as google_dot_protobuf_dot_timestamp__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n2google/cloud/connectors/v1/connector_version.proto\x12\x1agoogle.cloud.connectors.v1\x1a\x1fgoogle/api/field_behavior.proto\x1a\x19google/api/resource.proto\x1a+google/cloud/connectors/v1/authconfig.proto\x1a\'google/cloud/connectors/v1/common.proto\x1a+google/cloud/connectors/v1/ssl_config.proto\x1a\x1fgoogle/protobuf/timestamp.proto"\xdd\x08\n\x10ConnectorVersion\x12\x11\n\x04name\x18\x01 \x01(\tB\x03\xe0A\x03\x124\n\x0bcreate_time\x18\x02 \x01(\x0b2\x1a.google.protobuf.TimestampB\x03\xe0A\x03\x124\n\x0bupdate_time\x18\x03 \x01(\x0b2\x1a.google.protobuf.TimestampB\x03\xe0A\x03\x12M\n\x06labels\x18\x04 \x03(\x0b28.google.cloud.connectors.v1.ConnectorVersion.LabelsEntryB\x03\xe0A\x03\x12B\n\x0claunch_stage\x18\x06 \x01(\x0e2\'.google.cloud.connectors.v1.LaunchStageB\x03\xe0A\x03\x12\x1c\n\x0frelease_version\x18\x07 \x01(\tB\x03\xe0A\x03\x12R\n\x15auth_config_templates\x18\x08 \x03(\x0b2..google.cloud.connectors.v1.AuthConfigTemplateB\x03\xe0A\x03\x12Z\n\x19config_variable_templates\x18\t \x03(\x0b22.google.cloud.connectors.v1.ConfigVariableTemplateB\x03\xe0A\x03\x12]\n\x1asupported_runtime_features\x18\n \x01(\x0b24.google.cloud.connectors.v1.SupportedRuntimeFeaturesB\x03\xe0A\x03\x12\x19\n\x0cdisplay_name\x18\x0b \x01(\tB\x03\xe0A\x03\x12S\n\x15egress_control_config\x18\x0c \x01(\x0b2/.google.cloud.connectors.v1.EgressControlConfigB\x03\xe0A\x03\x12?\n\x0brole_grants\x18\x0e \x03(\x0b2%.google.cloud.connectors.v1.RoleGrantB\x03\xe0A\x03\x12>\n\nrole_grant\x18\x0f \x01(\x0b2%.google.cloud.connectors.v1.RoleGrantB\x03\xe0A\x03\x12O\n\x13ssl_config_template\x18\x11 \x01(\x0b2-.google.cloud.connectors.v1.SslConfigTemplateB\x03\xe0A\x03\x1a-\n\x0bLabelsEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\r\n\x05value\x18\x02 \x01(\t:\x028\x01:\x98\x01\xeaA\x94\x01\n*connectors.googleapis.com/ConnectorVersion\x12fprojects/{project}/locations/{location}/providers/{provider}/connectors/{connector}/versions/{version}"\x9e\x01\n\x1aGetConnectorVersionRequest\x12@\n\x04name\x18\x01 \x01(\tB2\xe0A\x02\xfaA,\n*connectors.googleapis.com/ConnectorVersion\x12>\n\x04view\x18\x02 \x01(\x0e20.google.cloud.connectors.v1.ConnectorVersionView"\xc2\x01\n\x1cListConnectorVersionsRequest\x12;\n\x06parent\x18\x01 \x01(\tB+\xe0A\x02\xfaA%\n#connectors.googleapis.com/Connector\x12\x11\n\tpage_size\x18\x02 \x01(\x05\x12\x12\n\npage_token\x18\x03 \x01(\t\x12>\n\x04view\x18\x04 \x01(\x0e20.google.cloud.connectors.v1.ConnectorVersionView"\x97\x01\n\x1dListConnectorVersionsResponse\x12H\n\x12connector_versions\x18\x01 \x03(\x0b2,.google.cloud.connectors.v1.ConnectorVersion\x12\x17\n\x0fnext_page_token\x18\x02 \x01(\t\x12\x13\n\x0bunreachable\x18\x03 \x03(\t"W\n\x18SupportedRuntimeFeatures\x12\x13\n\x0bentity_apis\x18\x01 \x01(\x08\x12\x13\n\x0baction_apis\x18\x02 \x01(\x08\x12\x11\n\tsql_query\x18\x03 \x01(\x08"\x84\x01\n\x13EgressControlConfig\x12\x12\n\x08backends\x18\x01 \x01(\tH\x00\x12G\n\x10extraction_rules\x18\x02 \x01(\x0b2+.google.cloud.connectors.v1.ExtractionRulesH\x00B\x10\n\x0eoneof_backends"V\n\x0fExtractionRules\x12C\n\x0fextraction_rule\x18\x01 \x03(\x0b2*.google.cloud.connectors.v1.ExtractionRule"\x95\x02\n\x0eExtractionRule\x12A\n\x06source\x18\x01 \x01(\x0b21.google.cloud.connectors.v1.ExtractionRule.Source\x12\x18\n\x10extraction_regex\x18\x02 \x01(\t\x1af\n\x06Source\x12J\n\x0bsource_type\x18\x01 \x01(\x0e25.google.cloud.connectors.v1.ExtractionRule.SourceType\x12\x10\n\x08field_id\x18\x02 \x01(\t">\n\nSourceType\x12\x1b\n\x17SOURCE_TYPE_UNSPECIFIED\x10\x00\x12\x13\n\x0fCONFIG_VARIABLE\x10\x01*\x81\x01\n\x14ConnectorVersionView\x12&\n"CONNECTOR_VERSION_VIEW_UNSPECIFIED\x10\x00\x12 \n\x1cCONNECTOR_VERSION_VIEW_BASIC\x10\x01\x12\x1f\n\x1bCONNECTOR_VERSION_VIEW_FULL\x10\x02By\n\x1ecom.google.cloud.connectors.v1B\x15ConnectorVersionProtoP\x01Z>cloud.google.com/go/connectors/apiv1/connectorspb;connectorspbb\x06proto3')
_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'google.cloud.connectors.v1.connector_version_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
    _globals['DESCRIPTOR']._loaded_options = None
    _globals['DESCRIPTOR']._serialized_options = b'\n\x1ecom.google.cloud.connectors.v1B\x15ConnectorVersionProtoP\x01Z>cloud.google.com/go/connectors/apiv1/connectorspb;connectorspb'
    _globals['_CONNECTORVERSION_LABELSENTRY']._loaded_options = None
    _globals['_CONNECTORVERSION_LABELSENTRY']._serialized_options = b'8\x01'
    _globals['_CONNECTORVERSION'].fields_by_name['name']._loaded_options = None
    _globals['_CONNECTORVERSION'].fields_by_name['name']._serialized_options = b'\xe0A\x03'
    _globals['_CONNECTORVERSION'].fields_by_name['create_time']._loaded_options = None
    _globals['_CONNECTORVERSION'].fields_by_name['create_time']._serialized_options = b'\xe0A\x03'
    _globals['_CONNECTORVERSION'].fields_by_name['update_time']._loaded_options = None
    _globals['_CONNECTORVERSION'].fields_by_name['update_time']._serialized_options = b'\xe0A\x03'
    _globals['_CONNECTORVERSION'].fields_by_name['labels']._loaded_options = None
    _globals['_CONNECTORVERSION'].fields_by_name['labels']._serialized_options = b'\xe0A\x03'
    _globals['_CONNECTORVERSION'].fields_by_name['launch_stage']._loaded_options = None
    _globals['_CONNECTORVERSION'].fields_by_name['launch_stage']._serialized_options = b'\xe0A\x03'
    _globals['_CONNECTORVERSION'].fields_by_name['release_version']._loaded_options = None
    _globals['_CONNECTORVERSION'].fields_by_name['release_version']._serialized_options = b'\xe0A\x03'
    _globals['_CONNECTORVERSION'].fields_by_name['auth_config_templates']._loaded_options = None
    _globals['_CONNECTORVERSION'].fields_by_name['auth_config_templates']._serialized_options = b'\xe0A\x03'
    _globals['_CONNECTORVERSION'].fields_by_name['config_variable_templates']._loaded_options = None
    _globals['_CONNECTORVERSION'].fields_by_name['config_variable_templates']._serialized_options = b'\xe0A\x03'
    _globals['_CONNECTORVERSION'].fields_by_name['supported_runtime_features']._loaded_options = None
    _globals['_CONNECTORVERSION'].fields_by_name['supported_runtime_features']._serialized_options = b'\xe0A\x03'
    _globals['_CONNECTORVERSION'].fields_by_name['display_name']._loaded_options = None
    _globals['_CONNECTORVERSION'].fields_by_name['display_name']._serialized_options = b'\xe0A\x03'
    _globals['_CONNECTORVERSION'].fields_by_name['egress_control_config']._loaded_options = None
    _globals['_CONNECTORVERSION'].fields_by_name['egress_control_config']._serialized_options = b'\xe0A\x03'
    _globals['_CONNECTORVERSION'].fields_by_name['role_grants']._loaded_options = None
    _globals['_CONNECTORVERSION'].fields_by_name['role_grants']._serialized_options = b'\xe0A\x03'
    _globals['_CONNECTORVERSION'].fields_by_name['role_grant']._loaded_options = None
    _globals['_CONNECTORVERSION'].fields_by_name['role_grant']._serialized_options = b'\xe0A\x03'
    _globals['_CONNECTORVERSION'].fields_by_name['ssl_config_template']._loaded_options = None
    _globals['_CONNECTORVERSION'].fields_by_name['ssl_config_template']._serialized_options = b'\xe0A\x03'
    _globals['_CONNECTORVERSION']._loaded_options = None
    _globals['_CONNECTORVERSION']._serialized_options = b'\xeaA\x94\x01\n*connectors.googleapis.com/ConnectorVersion\x12fprojects/{project}/locations/{location}/providers/{provider}/connectors/{connector}/versions/{version}'
    _globals['_GETCONNECTORVERSIONREQUEST'].fields_by_name['name']._loaded_options = None
    _globals['_GETCONNECTORVERSIONREQUEST'].fields_by_name['name']._serialized_options = b'\xe0A\x02\xfaA,\n*connectors.googleapis.com/ConnectorVersion'
    _globals['_LISTCONNECTORVERSIONSREQUEST'].fields_by_name['parent']._loaded_options = None
    _globals['_LISTCONNECTORVERSIONSREQUEST'].fields_by_name['parent']._serialized_options = b'\xe0A\x02\xfaA%\n#connectors.googleapis.com/Connector'
    _globals['_CONNECTORVERSIONVIEW']._serialized_start = 2531
    _globals['_CONNECTORVERSIONVIEW']._serialized_end = 2660
    _globals['_CONNECTORVERSION']._serialized_start = 307
    _globals['_CONNECTORVERSION']._serialized_end = 1424
    _globals['_CONNECTORVERSION_LABELSENTRY']._serialized_start = 1224
    _globals['_CONNECTORVERSION_LABELSENTRY']._serialized_end = 1269
    _globals['_GETCONNECTORVERSIONREQUEST']._serialized_start = 1427
    _globals['_GETCONNECTORVERSIONREQUEST']._serialized_end = 1585
    _globals['_LISTCONNECTORVERSIONSREQUEST']._serialized_start = 1588
    _globals['_LISTCONNECTORVERSIONSREQUEST']._serialized_end = 1782
    _globals['_LISTCONNECTORVERSIONSRESPONSE']._serialized_start = 1785
    _globals['_LISTCONNECTORVERSIONSRESPONSE']._serialized_end = 1936
    _globals['_SUPPORTEDRUNTIMEFEATURES']._serialized_start = 1938
    _globals['_SUPPORTEDRUNTIMEFEATURES']._serialized_end = 2025
    _globals['_EGRESSCONTROLCONFIG']._serialized_start = 2028
    _globals['_EGRESSCONTROLCONFIG']._serialized_end = 2160
    _globals['_EXTRACTIONRULES']._serialized_start = 2162
    _globals['_EXTRACTIONRULES']._serialized_end = 2248
    _globals['_EXTRACTIONRULE']._serialized_start = 2251
    _globals['_EXTRACTIONRULE']._serialized_end = 2528
    _globals['_EXTRACTIONRULE_SOURCE']._serialized_start = 2362
    _globals['_EXTRACTIONRULE_SOURCE']._serialized_end = 2464
    _globals['_EXTRACTIONRULE_SOURCETYPE']._serialized_start = 2466
    _globals['_EXTRACTIONRULE_SOURCETYPE']._serialized_end = 2528