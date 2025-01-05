"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_runtime_version.ValidateProtobufRuntimeVersion(_runtime_version.Domain.PUBLIC, 5, 28, 1, '', 'google/cloud/optimization/v1/async_model.proto')
_sym_db = _symbol_database.Default()
from .....google.api import field_behavior_pb2 as google_dot_api_dot_field__behavior__pb2
from google.protobuf import timestamp_pb2 as google_dot_protobuf_dot_timestamp__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n.google/cloud/optimization/v1/async_model.proto\x12\x1cgoogle.cloud.optimization.v1\x1a\x1fgoogle/api/field_behavior.proto\x1a\x1fgoogle/protobuf/timestamp.proto"\x95\x01\n\x0bInputConfig\x12=\n\ngcs_source\x18\x01 \x01(\x0b2\'.google.cloud.optimization.v1.GcsSourceH\x00\x12=\n\x0bdata_format\x18\x02 \x01(\x0e2(.google.cloud.optimization.v1.DataFormatB\x08\n\x06source"\xa5\x01\n\x0cOutputConfig\x12G\n\x0fgcs_destination\x18\x01 \x01(\x0b2,.google.cloud.optimization.v1.GcsDestinationH\x00\x12=\n\x0bdata_format\x18\x02 \x01(\x0e2(.google.cloud.optimization.v1.DataFormatB\r\n\x0bdestination"\x1d\n\tGcsSource\x12\x10\n\x03uri\x18\x01 \x01(\tB\x03\xe0A\x02""\n\x0eGcsDestination\x12\x10\n\x03uri\x18\x01 \x01(\tB\x03\xe0A\x02"\xab\x02\n\x12AsyncModelMetadata\x12E\n\x05state\x18\x01 \x01(\x0e26.google.cloud.optimization.v1.AsyncModelMetadata.State\x12\x15\n\rstate_message\x18\x02 \x01(\t\x12/\n\x0bcreate_time\x18\x03 \x01(\x0b2\x1a.google.protobuf.Timestamp\x12/\n\x0bupdate_time\x18\x04 \x01(\x0b2\x1a.google.protobuf.Timestamp"U\n\x05State\x12\x15\n\x11STATE_UNSPECIFIED\x10\x00\x12\x0b\n\x07RUNNING\x10\x01\x12\r\n\tSUCCEEDED\x10\x02\x12\r\n\tCANCELLED\x10\x03\x12\n\n\x06FAILED\x10\x04*?\n\nDataFormat\x12\x1b\n\x17DATA_FORMAT_UNSPECIFIED\x10\x00\x12\x08\n\x04JSON\x10\x01\x12\n\n\x06STRING\x10\x02B{\n com.google.cloud.optimization.v1B\x0fAsyncModelProtoP\x01ZDcloud.google.com/go/optimization/apiv1/optimizationpb;optimizationpbb\x06proto3')
_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'google.cloud.optimization.v1.async_model_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
    _globals['DESCRIPTOR']._loaded_options = None
    _globals['DESCRIPTOR']._serialized_options = b'\n com.google.cloud.optimization.v1B\x0fAsyncModelProtoP\x01ZDcloud.google.com/go/optimization/apiv1/optimizationpb;optimizationpb'
    _globals['_GCSSOURCE'].fields_by_name['uri']._loaded_options = None
    _globals['_GCSSOURCE'].fields_by_name['uri']._serialized_options = b'\xe0A\x02'
    _globals['_GCSDESTINATION'].fields_by_name['uri']._loaded_options = None
    _globals['_GCSDESTINATION'].fields_by_name['uri']._serialized_options = b'\xe0A\x02'
    _globals['_DATAFORMAT']._serialized_start = 835
    _globals['_DATAFORMAT']._serialized_end = 898
    _globals['_INPUTCONFIG']._serialized_start = 147
    _globals['_INPUTCONFIG']._serialized_end = 296
    _globals['_OUTPUTCONFIG']._serialized_start = 299
    _globals['_OUTPUTCONFIG']._serialized_end = 464
    _globals['_GCSSOURCE']._serialized_start = 466
    _globals['_GCSSOURCE']._serialized_end = 495
    _globals['_GCSDESTINATION']._serialized_start = 497
    _globals['_GCSDESTINATION']._serialized_end = 531
    _globals['_ASYNCMODELMETADATA']._serialized_start = 534
    _globals['_ASYNCMODELMETADATA']._serialized_end = 833
    _globals['_ASYNCMODELMETADATA_STATE']._serialized_start = 748
    _globals['_ASYNCMODELMETADATA_STATE']._serialized_end = 833