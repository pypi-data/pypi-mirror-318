"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_runtime_version.ValidateProtobufRuntimeVersion(_runtime_version.Domain.PUBLIC, 5, 28, 1, '', 'google/cloud/aiplatform/v1/notebook_euc_config.proto')
_sym_db = _symbol_database.Default()
from .....google.api import field_behavior_pb2 as google_dot_api_dot_field__behavior__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n4google/cloud/aiplatform/v1/notebook_euc_config.proto\x12\x1agoogle.cloud.aiplatform.v1\x1a\x1fgoogle/api/field_behavior.proto"O\n\x11NotebookEucConfig\x12\x19\n\x0ceuc_disabled\x18\x01 \x01(\x08B\x03\xe0A\x04\x12\x1f\n\x12bypass_actas_check\x18\x02 \x01(\x08B\x03\xe0A\x03B\xd4\x01\n\x1ecom.google.cloud.aiplatform.v1B\x16NotebookEucConfigProtoP\x01Z>cloud.google.com/go/aiplatform/apiv1/aiplatformpb;aiplatformpb\xaa\x02\x1aGoogle.Cloud.AIPlatform.V1\xca\x02\x1aGoogle\\Cloud\\AIPlatform\\V1\xea\x02\x1dGoogle::Cloud::AIPlatform::V1b\x06proto3')
_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'google.cloud.aiplatform.v1.notebook_euc_config_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
    _globals['DESCRIPTOR']._loaded_options = None
    _globals['DESCRIPTOR']._serialized_options = b'\n\x1ecom.google.cloud.aiplatform.v1B\x16NotebookEucConfigProtoP\x01Z>cloud.google.com/go/aiplatform/apiv1/aiplatformpb;aiplatformpb\xaa\x02\x1aGoogle.Cloud.AIPlatform.V1\xca\x02\x1aGoogle\\Cloud\\AIPlatform\\V1\xea\x02\x1dGoogle::Cloud::AIPlatform::V1'
    _globals['_NOTEBOOKEUCCONFIG'].fields_by_name['euc_disabled']._loaded_options = None
    _globals['_NOTEBOOKEUCCONFIG'].fields_by_name['euc_disabled']._serialized_options = b'\xe0A\x04'
    _globals['_NOTEBOOKEUCCONFIG'].fields_by_name['bypass_actas_check']._loaded_options = None
    _globals['_NOTEBOOKEUCCONFIG'].fields_by_name['bypass_actas_check']._serialized_options = b'\xe0A\x03'
    _globals['_NOTEBOOKEUCCONFIG']._serialized_start = 117
    _globals['_NOTEBOOKEUCCONFIG']._serialized_end = 196