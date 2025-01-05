"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_runtime_version.ValidateProtobufRuntimeVersion(_runtime_version.Domain.PUBLIC, 5, 28, 1, '', 'google/cloud/connectors/v1/settings.proto')
_sym_db = _symbol_database.Default()
from .....google.api import field_behavior_pb2 as google_dot_api_dot_field__behavior__pb2
from .....google.api import resource_pb2 as google_dot_api_dot_resource__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n)google/cloud/connectors/v1/settings.proto\x12\x1agoogle.cloud.connectors.v1\x1a\x1fgoogle/api/field_behavior.proto\x1a\x19google/api/resource.proto"T\n\x18GetGlobalSettingsRequest\x128\n\x04name\x18\x01 \x01(\tB*\xe0A\x02\xfaA$\n"connectors.googleapis.com/Settings"\x9b\x01\n\x08Settings\x12\x11\n\x04name\x18\x01 \x01(\tB\x03\xe0A\x03\x12\x12\n\x05vpcsc\x18\x02 \x01(\x08B\x03\xe0A\x01\x12\x11\n\x04payg\x18\x03 \x01(\x08B\x03\xe0A\x03:U\xeaAR\n"connectors.googleapis.com/Settings\x12,projects/{project}/locations/global/settingsBq\n\x1ecom.google.cloud.connectors.v1B\rSettingsProtoP\x01Z>cloud.google.com/go/connectors/apiv1/connectorspb;connectorspbb\x06proto3')
_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'google.cloud.connectors.v1.settings_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
    _globals['DESCRIPTOR']._loaded_options = None
    _globals['DESCRIPTOR']._serialized_options = b'\n\x1ecom.google.cloud.connectors.v1B\rSettingsProtoP\x01Z>cloud.google.com/go/connectors/apiv1/connectorspb;connectorspb'
    _globals['_GETGLOBALSETTINGSREQUEST'].fields_by_name['name']._loaded_options = None
    _globals['_GETGLOBALSETTINGSREQUEST'].fields_by_name['name']._serialized_options = b'\xe0A\x02\xfaA$\n"connectors.googleapis.com/Settings'
    _globals['_SETTINGS'].fields_by_name['name']._loaded_options = None
    _globals['_SETTINGS'].fields_by_name['name']._serialized_options = b'\xe0A\x03'
    _globals['_SETTINGS'].fields_by_name['vpcsc']._loaded_options = None
    _globals['_SETTINGS'].fields_by_name['vpcsc']._serialized_options = b'\xe0A\x01'
    _globals['_SETTINGS'].fields_by_name['payg']._loaded_options = None
    _globals['_SETTINGS'].fields_by_name['payg']._serialized_options = b'\xe0A\x03'
    _globals['_SETTINGS']._loaded_options = None
    _globals['_SETTINGS']._serialized_options = b'\xeaAR\n"connectors.googleapis.com/Settings\x12,projects/{project}/locations/global/settings'
    _globals['_GETGLOBALSETTINGSREQUEST']._serialized_start = 133
    _globals['_GETGLOBALSETTINGSREQUEST']._serialized_end = 217
    _globals['_SETTINGS']._serialized_start = 220
    _globals['_SETTINGS']._serialized_end = 375