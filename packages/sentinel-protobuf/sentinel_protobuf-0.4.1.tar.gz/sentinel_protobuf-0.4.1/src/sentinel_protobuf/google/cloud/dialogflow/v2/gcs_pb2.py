"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_runtime_version.ValidateProtobufRuntimeVersion(_runtime_version.Domain.PUBLIC, 5, 28, 1, '', 'google/cloud/dialogflow/v2/gcs.proto')
_sym_db = _symbol_database.Default()
from .....google.api import field_behavior_pb2 as google_dot_api_dot_field__behavior__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n$google/cloud/dialogflow/v2/gcs.proto\x12\x1agoogle.cloud.dialogflow.v2\x1a\x1fgoogle/api/field_behavior.proto"\x1f\n\nGcsSources\x12\x11\n\x04uris\x18\x02 \x03(\tB\x03\xe0A\x02"\x1d\n\x0eGcsDestination\x12\x0b\n\x03uri\x18\x01 \x01(\tB\x8e\x01\n\x1ecom.google.cloud.dialogflow.v2B\x08GcsProtoP\x01Z>cloud.google.com/go/dialogflow/apiv2/dialogflowpb;dialogflowpb\xa2\x02\x02DF\xaa\x02\x1aGoogle.Cloud.Dialogflow.V2b\x06proto3')
_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'google.cloud.dialogflow.v2.gcs_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
    _globals['DESCRIPTOR']._loaded_options = None
    _globals['DESCRIPTOR']._serialized_options = b'\n\x1ecom.google.cloud.dialogflow.v2B\x08GcsProtoP\x01Z>cloud.google.com/go/dialogflow/apiv2/dialogflowpb;dialogflowpb\xa2\x02\x02DF\xaa\x02\x1aGoogle.Cloud.Dialogflow.V2'
    _globals['_GCSSOURCES'].fields_by_name['uris']._loaded_options = None
    _globals['_GCSSOURCES'].fields_by_name['uris']._serialized_options = b'\xe0A\x02'
    _globals['_GCSSOURCES']._serialized_start = 101
    _globals['_GCSSOURCES']._serialized_end = 132
    _globals['_GCSDESTINATION']._serialized_start = 134
    _globals['_GCSDESTINATION']._serialized_end = 163