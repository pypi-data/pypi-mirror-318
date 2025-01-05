"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_runtime_version.ValidateProtobufRuntimeVersion(_runtime_version.Domain.PUBLIC, 5, 28, 1, '', 'google/cloud/aiplatform/v1/saved_query.proto')
_sym_db = _symbol_database.Default()
from .....google.api import field_behavior_pb2 as google_dot_api_dot_field__behavior__pb2
from .....google.api import resource_pb2 as google_dot_api_dot_resource__pb2
from google.protobuf import struct_pb2 as google_dot_protobuf_dot_struct__pb2
from google.protobuf import timestamp_pb2 as google_dot_protobuf_dot_timestamp__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n,google/cloud/aiplatform/v1/saved_query.proto\x12\x1agoogle.cloud.aiplatform.v1\x1a\x1fgoogle/api/field_behavior.proto\x1a\x19google/api/resource.proto\x1a\x1cgoogle/protobuf/struct.proto\x1a\x1fgoogle/protobuf/timestamp.proto"\xe6\x03\n\nSavedQuery\x12\x11\n\x04name\x18\x01 \x01(\tB\x03\xe0A\x03\x12\x19\n\x0cdisplay_name\x18\x02 \x01(\tB\x03\xe0A\x02\x12(\n\x08metadata\x18\x0c \x01(\x0b2\x16.google.protobuf.Value\x124\n\x0bcreate_time\x18\x03 \x01(\x0b2\x1a.google.protobuf.TimestampB\x03\xe0A\x03\x124\n\x0bupdate_time\x18\x04 \x01(\x0b2\x1a.google.protobuf.TimestampB\x03\xe0A\x03\x12\x1e\n\x11annotation_filter\x18\x05 \x01(\tB\x03\xe0A\x03\x12\x19\n\x0cproblem_type\x18\x06 \x01(\tB\x03\xe0A\x02\x12"\n\x15annotation_spec_count\x18\n \x01(\x05B\x03\xe0A\x03\x12\x0c\n\x04etag\x18\x08 \x01(\t\x12$\n\x17support_automl_training\x18\t \x01(\x08B\x03\xe0A\x03:\x80\x01\xeaA}\n$aiplatform.googleapis.com/SavedQuery\x12Uprojects/{project}/locations/{location}/datasets/{dataset}/savedQueries/{saved_query}B\xcd\x01\n\x1ecom.google.cloud.aiplatform.v1B\x0fSavedQueryProtoP\x01Z>cloud.google.com/go/aiplatform/apiv1/aiplatformpb;aiplatformpb\xaa\x02\x1aGoogle.Cloud.AIPlatform.V1\xca\x02\x1aGoogle\\Cloud\\AIPlatform\\V1\xea\x02\x1dGoogle::Cloud::AIPlatform::V1b\x06proto3')
_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'google.cloud.aiplatform.v1.saved_query_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
    _globals['DESCRIPTOR']._loaded_options = None
    _globals['DESCRIPTOR']._serialized_options = b'\n\x1ecom.google.cloud.aiplatform.v1B\x0fSavedQueryProtoP\x01Z>cloud.google.com/go/aiplatform/apiv1/aiplatformpb;aiplatformpb\xaa\x02\x1aGoogle.Cloud.AIPlatform.V1\xca\x02\x1aGoogle\\Cloud\\AIPlatform\\V1\xea\x02\x1dGoogle::Cloud::AIPlatform::V1'
    _globals['_SAVEDQUERY'].fields_by_name['name']._loaded_options = None
    _globals['_SAVEDQUERY'].fields_by_name['name']._serialized_options = b'\xe0A\x03'
    _globals['_SAVEDQUERY'].fields_by_name['display_name']._loaded_options = None
    _globals['_SAVEDQUERY'].fields_by_name['display_name']._serialized_options = b'\xe0A\x02'
    _globals['_SAVEDQUERY'].fields_by_name['create_time']._loaded_options = None
    _globals['_SAVEDQUERY'].fields_by_name['create_time']._serialized_options = b'\xe0A\x03'
    _globals['_SAVEDQUERY'].fields_by_name['update_time']._loaded_options = None
    _globals['_SAVEDQUERY'].fields_by_name['update_time']._serialized_options = b'\xe0A\x03'
    _globals['_SAVEDQUERY'].fields_by_name['annotation_filter']._loaded_options = None
    _globals['_SAVEDQUERY'].fields_by_name['annotation_filter']._serialized_options = b'\xe0A\x03'
    _globals['_SAVEDQUERY'].fields_by_name['problem_type']._loaded_options = None
    _globals['_SAVEDQUERY'].fields_by_name['problem_type']._serialized_options = b'\xe0A\x02'
    _globals['_SAVEDQUERY'].fields_by_name['annotation_spec_count']._loaded_options = None
    _globals['_SAVEDQUERY'].fields_by_name['annotation_spec_count']._serialized_options = b'\xe0A\x03'
    _globals['_SAVEDQUERY'].fields_by_name['support_automl_training']._loaded_options = None
    _globals['_SAVEDQUERY'].fields_by_name['support_automl_training']._serialized_options = b'\xe0A\x03'
    _globals['_SAVEDQUERY']._loaded_options = None
    _globals['_SAVEDQUERY']._serialized_options = b'\xeaA}\n$aiplatform.googleapis.com/SavedQuery\x12Uprojects/{project}/locations/{location}/datasets/{dataset}/savedQueries/{saved_query}'
    _globals['_SAVEDQUERY']._serialized_start = 200
    _globals['_SAVEDQUERY']._serialized_end = 686