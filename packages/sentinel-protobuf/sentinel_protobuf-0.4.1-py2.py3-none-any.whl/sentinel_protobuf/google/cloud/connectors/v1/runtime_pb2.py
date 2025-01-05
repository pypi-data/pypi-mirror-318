"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_runtime_version.ValidateProtobufRuntimeVersion(_runtime_version.Domain.PUBLIC, 5, 28, 1, '', 'google/cloud/connectors/v1/runtime.proto')
_sym_db = _symbol_database.Default()
from .....google.api import field_behavior_pb2 as google_dot_api_dot_field__behavior__pb2
from .....google.api import resource_pb2 as google_dot_api_dot_resource__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n(google/cloud/connectors/v1/runtime.proto\x12\x1agoogle.cloud.connectors.v1\x1a\x1fgoogle/api/field_behavior.proto\x1a\x19google/api/resource.proto"X\n\x17GetRuntimeConfigRequest\x12=\n\x04name\x18\x01 \x01(\tB/\xe0A\x02\xfaA)\n\'connectors.googleapis.com/RuntimeConfig"\xc7\x04\n\rRuntimeConfig\x12\x18\n\x0blocation_id\x18\x01 \x01(\tB\x03\xe0A\x03\x12\x18\n\x0bconnd_topic\x18\x02 \x01(\tB\x03\xe0A\x03\x12\x1f\n\x12connd_subscription\x18\x03 \x01(\tB\x03\xe0A\x03\x12 \n\x13control_plane_topic\x18\x04 \x01(\tB\x03\xe0A\x03\x12\'\n\x1acontrol_plane_subscription\x18\x05 \x01(\tB\x03\xe0A\x03\x12\x1d\n\x10runtime_endpoint\x18\x06 \x01(\tB\x03\xe0A\x03\x12C\n\x05state\x18\x07 \x01(\x0e2/.google.cloud.connectors.v1.RuntimeConfig.StateB\x03\xe0A\x03\x12\x1e\n\x11schema_gcs_bucket\x18\x08 \x01(\tB\x03\xe0A\x03\x12\x1e\n\x11service_directory\x18\t \x01(\tB\x03\xe0A\x03\x12\x11\n\x04name\x18\x0b \x01(\tB\x03\xe0A\x03"z\n\x05State\x12\x15\n\x11STATE_UNSPECIFIED\x10\x00\x12\x10\n\x08INACTIVE\x10\x01\x1a\x02\x08\x01\x12\x12\n\nACTIVATING\x10\x02\x1a\x02\x08\x01\x12\n\n\x06ACTIVE\x10\x03\x12\x0c\n\x08CREATING\x10\x04\x12\x0c\n\x08DELETING\x10\x05\x12\x0c\n\x08UPDATING\x10\x06:c\xeaA`\n\'connectors.googleapis.com/RuntimeConfig\x125projects/{project}/locations/{location}/runtimeConfigBp\n\x1ecom.google.cloud.connectors.v1B\x0cRuntimeProtoP\x01Z>cloud.google.com/go/connectors/apiv1/connectorspb;connectorspbb\x06proto3')
_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'google.cloud.connectors.v1.runtime_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
    _globals['DESCRIPTOR']._loaded_options = None
    _globals['DESCRIPTOR']._serialized_options = b'\n\x1ecom.google.cloud.connectors.v1B\x0cRuntimeProtoP\x01Z>cloud.google.com/go/connectors/apiv1/connectorspb;connectorspb'
    _globals['_GETRUNTIMECONFIGREQUEST'].fields_by_name['name']._loaded_options = None
    _globals['_GETRUNTIMECONFIGREQUEST'].fields_by_name['name']._serialized_options = b"\xe0A\x02\xfaA)\n'connectors.googleapis.com/RuntimeConfig"
    _globals['_RUNTIMECONFIG_STATE'].values_by_name['INACTIVE']._loaded_options = None
    _globals['_RUNTIMECONFIG_STATE'].values_by_name['INACTIVE']._serialized_options = b'\x08\x01'
    _globals['_RUNTIMECONFIG_STATE'].values_by_name['ACTIVATING']._loaded_options = None
    _globals['_RUNTIMECONFIG_STATE'].values_by_name['ACTIVATING']._serialized_options = b'\x08\x01'
    _globals['_RUNTIMECONFIG'].fields_by_name['location_id']._loaded_options = None
    _globals['_RUNTIMECONFIG'].fields_by_name['location_id']._serialized_options = b'\xe0A\x03'
    _globals['_RUNTIMECONFIG'].fields_by_name['connd_topic']._loaded_options = None
    _globals['_RUNTIMECONFIG'].fields_by_name['connd_topic']._serialized_options = b'\xe0A\x03'
    _globals['_RUNTIMECONFIG'].fields_by_name['connd_subscription']._loaded_options = None
    _globals['_RUNTIMECONFIG'].fields_by_name['connd_subscription']._serialized_options = b'\xe0A\x03'
    _globals['_RUNTIMECONFIG'].fields_by_name['control_plane_topic']._loaded_options = None
    _globals['_RUNTIMECONFIG'].fields_by_name['control_plane_topic']._serialized_options = b'\xe0A\x03'
    _globals['_RUNTIMECONFIG'].fields_by_name['control_plane_subscription']._loaded_options = None
    _globals['_RUNTIMECONFIG'].fields_by_name['control_plane_subscription']._serialized_options = b'\xe0A\x03'
    _globals['_RUNTIMECONFIG'].fields_by_name['runtime_endpoint']._loaded_options = None
    _globals['_RUNTIMECONFIG'].fields_by_name['runtime_endpoint']._serialized_options = b'\xe0A\x03'
    _globals['_RUNTIMECONFIG'].fields_by_name['state']._loaded_options = None
    _globals['_RUNTIMECONFIG'].fields_by_name['state']._serialized_options = b'\xe0A\x03'
    _globals['_RUNTIMECONFIG'].fields_by_name['schema_gcs_bucket']._loaded_options = None
    _globals['_RUNTIMECONFIG'].fields_by_name['schema_gcs_bucket']._serialized_options = b'\xe0A\x03'
    _globals['_RUNTIMECONFIG'].fields_by_name['service_directory']._loaded_options = None
    _globals['_RUNTIMECONFIG'].fields_by_name['service_directory']._serialized_options = b'\xe0A\x03'
    _globals['_RUNTIMECONFIG'].fields_by_name['name']._loaded_options = None
    _globals['_RUNTIMECONFIG'].fields_by_name['name']._serialized_options = b'\xe0A\x03'
    _globals['_RUNTIMECONFIG']._loaded_options = None
    _globals['_RUNTIMECONFIG']._serialized_options = b"\xeaA`\n'connectors.googleapis.com/RuntimeConfig\x125projects/{project}/locations/{location}/runtimeConfig"
    _globals['_GETRUNTIMECONFIGREQUEST']._serialized_start = 132
    _globals['_GETRUNTIMECONFIGREQUEST']._serialized_end = 220
    _globals['_RUNTIMECONFIG']._serialized_start = 223
    _globals['_RUNTIMECONFIG']._serialized_end = 806
    _globals['_RUNTIMECONFIG_STATE']._serialized_start = 583
    _globals['_RUNTIMECONFIG_STATE']._serialized_end = 705