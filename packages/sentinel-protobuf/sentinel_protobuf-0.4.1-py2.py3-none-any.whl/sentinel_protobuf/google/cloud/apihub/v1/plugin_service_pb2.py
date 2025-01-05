"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_runtime_version.ValidateProtobufRuntimeVersion(_runtime_version.Domain.PUBLIC, 5, 28, 1, '', 'google/cloud/apihub/v1/plugin_service.proto')
_sym_db = _symbol_database.Default()
from .....google.api import annotations_pb2 as google_dot_api_dot_annotations__pb2
from .....google.api import client_pb2 as google_dot_api_dot_client__pb2
from .....google.api import field_behavior_pb2 as google_dot_api_dot_field__behavior__pb2
from .....google.api import resource_pb2 as google_dot_api_dot_resource__pb2
from .....google.cloud.apihub.v1 import common_fields_pb2 as google_dot_cloud_dot_apihub_dot_v1_dot_common__fields__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n+google/cloud/apihub/v1/plugin_service.proto\x12\x16google.cloud.apihub.v1\x1a\x1cgoogle/api/annotations.proto\x1a\x17google/api/client.proto\x1a\x1fgoogle/api/field_behavior.proto\x1a\x19google/api/resource.proto\x1a*google/cloud/apihub/v1/common_fields.proto"\xef\x02\n\x06Plugin\x12\x11\n\x04name\x18\x01 \x01(\tB\x03\xe0A\x08\x12\x19\n\x0cdisplay_name\x18\x02 \x01(\tB\x03\xe0A\x02\x12:\n\x04type\x18\x03 \x01(\x0b2\'.google.cloud.apihub.v1.AttributeValuesB\x03\xe0A\x02\x12\x18\n\x0bdescription\x18\x04 \x01(\tB\x03\xe0A\x01\x128\n\x05state\x18\x05 \x01(\x0e2$.google.cloud.apihub.v1.Plugin.StateB\x03\xe0A\x03"9\n\x05State\x12\x15\n\x11STATE_UNSPECIFIED\x10\x00\x12\x0b\n\x07ENABLED\x10\x01\x12\x0c\n\x08DISABLED\x10\x02:l\xeaAi\n\x1capihub.googleapis.com/Plugin\x128projects/{project}/locations/{location}/plugins/{plugin}*\x07plugins2\x06plugin"F\n\x10GetPluginRequest\x122\n\x04name\x18\x01 \x01(\tB$\xe0A\x02\xfaA\x1e\n\x1capihub.googleapis.com/Plugin"I\n\x13EnablePluginRequest\x122\n\x04name\x18\x01 \x01(\tB$\xe0A\x02\xfaA\x1e\n\x1capihub.googleapis.com/Plugin"J\n\x14DisablePluginRequest\x122\n\x04name\x18\x01 \x01(\tB$\xe0A\x02\xfaA\x1e\n\x1capihub.googleapis.com/Plugin2\xb8\x04\n\x0cApiHubPlugin\x12\x91\x01\n\tGetPlugin\x12(.google.cloud.apihub.v1.GetPluginRequest\x1a\x1e.google.cloud.apihub.v1.Plugin":\xdaA\x04name\x82\xd3\xe4\x93\x02-\x12+/v1/{name=projects/*/locations/*/plugins/*}\x12\xa1\x01\n\x0cEnablePlugin\x12+.google.cloud.apihub.v1.EnablePluginRequest\x1a\x1e.google.cloud.apihub.v1.Plugin"D\xdaA\x04name\x82\xd3\xe4\x93\x027"2/v1/{name=projects/*/locations/*/plugins/*}:enable:\x01*\x12\xa4\x01\n\rDisablePlugin\x12,.google.cloud.apihub.v1.DisablePluginRequest\x1a\x1e.google.cloud.apihub.v1.Plugin"E\xdaA\x04name\x82\xd3\xe4\x93\x028"3/v1/{name=projects/*/locations/*/plugins/*}:disable:\x01*\x1aI\xcaA\x15apihub.googleapis.com\xd2A.https://www.googleapis.com/auth/cloud-platformB\xb4\x01\n\x1acom.google.cloud.apihub.v1B\x12PluginServiceProtoP\x01Z2cloud.google.com/go/apihub/apiv1/apihubpb;apihubpb\xaa\x02\x16Google.Cloud.ApiHub.V1\xca\x02\x16Google\\Cloud\\ApiHub\\V1\xea\x02\x19Google::Cloud::ApiHub::V1b\x06proto3')
_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'google.cloud.apihub.v1.plugin_service_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
    _globals['DESCRIPTOR']._loaded_options = None
    _globals['DESCRIPTOR']._serialized_options = b'\n\x1acom.google.cloud.apihub.v1B\x12PluginServiceProtoP\x01Z2cloud.google.com/go/apihub/apiv1/apihubpb;apihubpb\xaa\x02\x16Google.Cloud.ApiHub.V1\xca\x02\x16Google\\Cloud\\ApiHub\\V1\xea\x02\x19Google::Cloud::ApiHub::V1'
    _globals['_PLUGIN'].fields_by_name['name']._loaded_options = None
    _globals['_PLUGIN'].fields_by_name['name']._serialized_options = b'\xe0A\x08'
    _globals['_PLUGIN'].fields_by_name['display_name']._loaded_options = None
    _globals['_PLUGIN'].fields_by_name['display_name']._serialized_options = b'\xe0A\x02'
    _globals['_PLUGIN'].fields_by_name['type']._loaded_options = None
    _globals['_PLUGIN'].fields_by_name['type']._serialized_options = b'\xe0A\x02'
    _globals['_PLUGIN'].fields_by_name['description']._loaded_options = None
    _globals['_PLUGIN'].fields_by_name['description']._serialized_options = b'\xe0A\x01'
    _globals['_PLUGIN'].fields_by_name['state']._loaded_options = None
    _globals['_PLUGIN'].fields_by_name['state']._serialized_options = b'\xe0A\x03'
    _globals['_PLUGIN']._loaded_options = None
    _globals['_PLUGIN']._serialized_options = b'\xeaAi\n\x1capihub.googleapis.com/Plugin\x128projects/{project}/locations/{location}/plugins/{plugin}*\x07plugins2\x06plugin'
    _globals['_GETPLUGINREQUEST'].fields_by_name['name']._loaded_options = None
    _globals['_GETPLUGINREQUEST'].fields_by_name['name']._serialized_options = b'\xe0A\x02\xfaA\x1e\n\x1capihub.googleapis.com/Plugin'
    _globals['_ENABLEPLUGINREQUEST'].fields_by_name['name']._loaded_options = None
    _globals['_ENABLEPLUGINREQUEST'].fields_by_name['name']._serialized_options = b'\xe0A\x02\xfaA\x1e\n\x1capihub.googleapis.com/Plugin'
    _globals['_DISABLEPLUGINREQUEST'].fields_by_name['name']._loaded_options = None
    _globals['_DISABLEPLUGINREQUEST'].fields_by_name['name']._serialized_options = b'\xe0A\x02\xfaA\x1e\n\x1capihub.googleapis.com/Plugin'
    _globals['_APIHUBPLUGIN']._loaded_options = None
    _globals['_APIHUBPLUGIN']._serialized_options = b'\xcaA\x15apihub.googleapis.com\xd2A.https://www.googleapis.com/auth/cloud-platform'
    _globals['_APIHUBPLUGIN'].methods_by_name['GetPlugin']._loaded_options = None
    _globals['_APIHUBPLUGIN'].methods_by_name['GetPlugin']._serialized_options = b'\xdaA\x04name\x82\xd3\xe4\x93\x02-\x12+/v1/{name=projects/*/locations/*/plugins/*}'
    _globals['_APIHUBPLUGIN'].methods_by_name['EnablePlugin']._loaded_options = None
    _globals['_APIHUBPLUGIN'].methods_by_name['EnablePlugin']._serialized_options = b'\xdaA\x04name\x82\xd3\xe4\x93\x027"2/v1/{name=projects/*/locations/*/plugins/*}:enable:\x01*'
    _globals['_APIHUBPLUGIN'].methods_by_name['DisablePlugin']._loaded_options = None
    _globals['_APIHUBPLUGIN'].methods_by_name['DisablePlugin']._serialized_options = b'\xdaA\x04name\x82\xd3\xe4\x93\x028"3/v1/{name=projects/*/locations/*/plugins/*}:disable:\x01*'
    _globals['_PLUGIN']._serialized_start = 231
    _globals['_PLUGIN']._serialized_end = 598
    _globals['_PLUGIN_STATE']._serialized_start = 431
    _globals['_PLUGIN_STATE']._serialized_end = 488
    _globals['_GETPLUGINREQUEST']._serialized_start = 600
    _globals['_GETPLUGINREQUEST']._serialized_end = 670
    _globals['_ENABLEPLUGINREQUEST']._serialized_start = 672
    _globals['_ENABLEPLUGINREQUEST']._serialized_end = 745
    _globals['_DISABLEPLUGINREQUEST']._serialized_start = 747
    _globals['_DISABLEPLUGINREQUEST']._serialized_end = 821
    _globals['_APIHUBPLUGIN']._serialized_start = 824
    _globals['_APIHUBPLUGIN']._serialized_end = 1392