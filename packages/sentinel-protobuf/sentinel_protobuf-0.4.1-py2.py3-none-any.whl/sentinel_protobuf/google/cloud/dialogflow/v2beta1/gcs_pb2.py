"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_runtime_version.ValidateProtobufRuntimeVersion(_runtime_version.Domain.PUBLIC, 5, 28, 1, '', 'google/cloud/dialogflow/v2beta1/gcs.proto')
_sym_db = _symbol_database.Default()
from .....google.api import field_behavior_pb2 as google_dot_api_dot_field__behavior__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n)google/cloud/dialogflow/v2beta1/gcs.proto\x12\x1fgoogle.cloud.dialogflow.v2beta1\x1a\x1fgoogle/api/field_behavior.proto"\x1f\n\nGcsSources\x12\x11\n\x04uris\x18\x02 \x03(\tB\x03\xe0A\x02"\x18\n\tGcsSource\x12\x0b\n\x03uri\x18\x01 \x01(\t"\x1d\n\x0eGcsDestination\x12\x0b\n\x03uri\x18\x01 \x01(\tB\x9d\x01\n#com.google.cloud.dialogflow.v2beta1B\x08GcsProtoP\x01ZCcloud.google.com/go/dialogflow/apiv2beta1/dialogflowpb;dialogflowpb\xa2\x02\x02DF\xaa\x02\x1fGoogle.Cloud.Dialogflow.V2Beta1b\x06proto3')
_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'google.cloud.dialogflow.v2beta1.gcs_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
    _globals['DESCRIPTOR']._loaded_options = None
    _globals['DESCRIPTOR']._serialized_options = b'\n#com.google.cloud.dialogflow.v2beta1B\x08GcsProtoP\x01ZCcloud.google.com/go/dialogflow/apiv2beta1/dialogflowpb;dialogflowpb\xa2\x02\x02DF\xaa\x02\x1fGoogle.Cloud.Dialogflow.V2Beta1'
    _globals['_GCSSOURCES'].fields_by_name['uris']._loaded_options = None
    _globals['_GCSSOURCES'].fields_by_name['uris']._serialized_options = b'\xe0A\x02'
    _globals['_GCSSOURCES']._serialized_start = 111
    _globals['_GCSSOURCES']._serialized_end = 142
    _globals['_GCSSOURCE']._serialized_start = 144
    _globals['_GCSSOURCE']._serialized_end = 168
    _globals['_GCSDESTINATION']._serialized_start = 170
    _globals['_GCSDESTINATION']._serialized_end = 199