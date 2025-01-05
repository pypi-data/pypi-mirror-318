"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_runtime_version.ValidateProtobufRuntimeVersion(_runtime_version.Domain.PUBLIC, 5, 28, 1, '', 'google/cloud/connectors/v1/provider.proto')
_sym_db = _symbol_database.Default()
from .....google.api import field_behavior_pb2 as google_dot_api_dot_field__behavior__pb2
from .....google.api import resource_pb2 as google_dot_api_dot_resource__pb2
from .....google.cloud.connectors.v1 import common_pb2 as google_dot_cloud_dot_connectors_dot_v1_dot_common__pb2
from google.protobuf import timestamp_pb2 as google_dot_protobuf_dot_timestamp__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n)google/cloud/connectors/v1/provider.proto\x12\x1agoogle.cloud.connectors.v1\x1a\x1fgoogle/api/field_behavior.proto\x1a\x19google/api/resource.proto\x1a\'google/cloud/connectors/v1/common.proto\x1a\x1fgoogle/protobuf/timestamp.proto"\xbc\x04\n\x08Provider\x12\x11\n\x04name\x18\x01 \x01(\tB\x03\xe0A\x03\x124\n\x0bcreate_time\x18\x02 \x01(\x0b2\x1a.google.protobuf.TimestampB\x03\xe0A\x03\x124\n\x0bupdate_time\x18\x03 \x01(\x0b2\x1a.google.protobuf.TimestampB\x03\xe0A\x03\x12E\n\x06labels\x18\x04 \x03(\x0b20.google.cloud.connectors.v1.Provider.LabelsEntryB\x03\xe0A\x03\x12\x1e\n\x11documentation_uri\x18\x06 \x01(\tB\x03\xe0A\x03\x12\x19\n\x0cexternal_uri\x18\x07 \x01(\tB\x03\xe0A\x03\x12\x18\n\x0bdescription\x18\x08 \x01(\tB\x03\xe0A\x03\x12 \n\x13web_assets_location\x18\t \x01(\tB\x03\xe0A\x03\x12\x19\n\x0cdisplay_name\x18\n \x01(\tB\x03\xe0A\x03\x12B\n\x0claunch_stage\x18\x0b \x01(\x0e2\'.google.cloud.connectors.v1.LaunchStageB\x03\xe0A\x03\x1a-\n\x0bLabelsEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\r\n\x05value\x18\x02 \x01(\t:\x028\x01:e\xeaAb\n"connectors.googleapis.com/Provider\x12<projects/{project}/locations/{location}/providers/{provider}"N\n\x12GetProviderRequest\x128\n\x04name\x18\x01 \x01(\tB*\xe0A\x02\xfaA$\n"connectors.googleapis.com/Provider"y\n\x14ListProvidersRequest\x12:\n\x06parent\x18\x01 \x01(\tB*\xe0A\x02\xfaA$\x12"connectors.googleapis.com/Provider\x12\x11\n\tpage_size\x18\x02 \x01(\x05\x12\x12\n\npage_token\x18\x03 \x01(\t"~\n\x15ListProvidersResponse\x127\n\tproviders\x18\x01 \x03(\x0b2$.google.cloud.connectors.v1.Provider\x12\x17\n\x0fnext_page_token\x18\x02 \x01(\t\x12\x13\n\x0bunreachable\x18\x03 \x03(\tBq\n\x1ecom.google.cloud.connectors.v1B\rProviderProtoP\x01Z>cloud.google.com/go/connectors/apiv1/connectorspb;connectorspbb\x06proto3')
_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'google.cloud.connectors.v1.provider_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
    _globals['DESCRIPTOR']._loaded_options = None
    _globals['DESCRIPTOR']._serialized_options = b'\n\x1ecom.google.cloud.connectors.v1B\rProviderProtoP\x01Z>cloud.google.com/go/connectors/apiv1/connectorspb;connectorspb'
    _globals['_PROVIDER_LABELSENTRY']._loaded_options = None
    _globals['_PROVIDER_LABELSENTRY']._serialized_options = b'8\x01'
    _globals['_PROVIDER'].fields_by_name['name']._loaded_options = None
    _globals['_PROVIDER'].fields_by_name['name']._serialized_options = b'\xe0A\x03'
    _globals['_PROVIDER'].fields_by_name['create_time']._loaded_options = None
    _globals['_PROVIDER'].fields_by_name['create_time']._serialized_options = b'\xe0A\x03'
    _globals['_PROVIDER'].fields_by_name['update_time']._loaded_options = None
    _globals['_PROVIDER'].fields_by_name['update_time']._serialized_options = b'\xe0A\x03'
    _globals['_PROVIDER'].fields_by_name['labels']._loaded_options = None
    _globals['_PROVIDER'].fields_by_name['labels']._serialized_options = b'\xe0A\x03'
    _globals['_PROVIDER'].fields_by_name['documentation_uri']._loaded_options = None
    _globals['_PROVIDER'].fields_by_name['documentation_uri']._serialized_options = b'\xe0A\x03'
    _globals['_PROVIDER'].fields_by_name['external_uri']._loaded_options = None
    _globals['_PROVIDER'].fields_by_name['external_uri']._serialized_options = b'\xe0A\x03'
    _globals['_PROVIDER'].fields_by_name['description']._loaded_options = None
    _globals['_PROVIDER'].fields_by_name['description']._serialized_options = b'\xe0A\x03'
    _globals['_PROVIDER'].fields_by_name['web_assets_location']._loaded_options = None
    _globals['_PROVIDER'].fields_by_name['web_assets_location']._serialized_options = b'\xe0A\x03'
    _globals['_PROVIDER'].fields_by_name['display_name']._loaded_options = None
    _globals['_PROVIDER'].fields_by_name['display_name']._serialized_options = b'\xe0A\x03'
    _globals['_PROVIDER'].fields_by_name['launch_stage']._loaded_options = None
    _globals['_PROVIDER'].fields_by_name['launch_stage']._serialized_options = b'\xe0A\x03'
    _globals['_PROVIDER']._loaded_options = None
    _globals['_PROVIDER']._serialized_options = b'\xeaAb\n"connectors.googleapis.com/Provider\x12<projects/{project}/locations/{location}/providers/{provider}'
    _globals['_GETPROVIDERREQUEST'].fields_by_name['name']._loaded_options = None
    _globals['_GETPROVIDERREQUEST'].fields_by_name['name']._serialized_options = b'\xe0A\x02\xfaA$\n"connectors.googleapis.com/Provider'
    _globals['_LISTPROVIDERSREQUEST'].fields_by_name['parent']._loaded_options = None
    _globals['_LISTPROVIDERSREQUEST'].fields_by_name['parent']._serialized_options = b'\xe0A\x02\xfaA$\x12"connectors.googleapis.com/Provider'
    _globals['_PROVIDER']._serialized_start = 208
    _globals['_PROVIDER']._serialized_end = 780
    _globals['_PROVIDER_LABELSENTRY']._serialized_start = 632
    _globals['_PROVIDER_LABELSENTRY']._serialized_end = 677
    _globals['_GETPROVIDERREQUEST']._serialized_start = 782
    _globals['_GETPROVIDERREQUEST']._serialized_end = 860
    _globals['_LISTPROVIDERSREQUEST']._serialized_start = 862
    _globals['_LISTPROVIDERSREQUEST']._serialized_end = 983
    _globals['_LISTPROVIDERSRESPONSE']._serialized_start = 985
    _globals['_LISTPROVIDERSRESPONSE']._serialized_end = 1111