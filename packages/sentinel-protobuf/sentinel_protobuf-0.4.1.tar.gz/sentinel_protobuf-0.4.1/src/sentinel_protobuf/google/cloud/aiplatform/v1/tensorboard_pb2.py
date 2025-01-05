"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_runtime_version.ValidateProtobufRuntimeVersion(_runtime_version.Domain.PUBLIC, 5, 28, 1, '', 'google/cloud/aiplatform/v1/tensorboard.proto')
_sym_db = _symbol_database.Default()
from .....google.api import field_behavior_pb2 as google_dot_api_dot_field__behavior__pb2
from .....google.api import resource_pb2 as google_dot_api_dot_resource__pb2
from .....google.cloud.aiplatform.v1 import encryption_spec_pb2 as google_dot_cloud_dot_aiplatform_dot_v1_dot_encryption__spec__pb2
from google.protobuf import timestamp_pb2 as google_dot_protobuf_dot_timestamp__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n,google/cloud/aiplatform/v1/tensorboard.proto\x12\x1agoogle.cloud.aiplatform.v1\x1a\x1fgoogle/api/field_behavior.proto\x1a\x19google/api/resource.proto\x1a0google/cloud/aiplatform/v1/encryption_spec.proto\x1a\x1fgoogle/protobuf/timestamp.proto"\xfe\x04\n\x0bTensorboard\x12\x11\n\x04name\x18\x01 \x01(\tB\x03\xe0A\x03\x12\x19\n\x0cdisplay_name\x18\x02 \x01(\tB\x03\xe0A\x02\x12\x13\n\x0bdescription\x18\x03 \x01(\t\x12C\n\x0fencryption_spec\x18\x0b \x01(\x0b2*.google.cloud.aiplatform.v1.EncryptionSpec\x12%\n\x18blob_storage_path_prefix\x18\n \x01(\tB\x03\xe0A\x03\x12\x16\n\trun_count\x18\x05 \x01(\x05B\x03\xe0A\x03\x124\n\x0bcreate_time\x18\x06 \x01(\x0b2\x1a.google.protobuf.TimestampB\x03\xe0A\x03\x124\n\x0bupdate_time\x18\x07 \x01(\x0b2\x1a.google.protobuf.TimestampB\x03\xe0A\x03\x12C\n\x06labels\x18\x08 \x03(\x0b23.google.cloud.aiplatform.v1.Tensorboard.LabelsEntry\x12\x0c\n\x04etag\x18\t \x01(\t\x12\x12\n\nis_default\x18\x0c \x01(\x08\x12\x1a\n\rsatisfies_pzs\x18\r \x01(\x08B\x03\xe0A\x03\x12\x1a\n\rsatisfies_pzi\x18\x0e \x01(\x08B\x03\xe0A\x03\x1a-\n\x0bLabelsEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\r\n\x05value\x18\x02 \x01(\t:\x028\x01:n\xeaAk\n%aiplatform.googleapis.com/Tensorboard\x12Bprojects/{project}/locations/{location}/tensorboards/{tensorboard}B\xce\x01\n\x1ecom.google.cloud.aiplatform.v1B\x10TensorboardProtoP\x01Z>cloud.google.com/go/aiplatform/apiv1/aiplatformpb;aiplatformpb\xaa\x02\x1aGoogle.Cloud.AIPlatform.V1\xca\x02\x1aGoogle\\Cloud\\AIPlatform\\V1\xea\x02\x1dGoogle::Cloud::AIPlatform::V1b\x06proto3')
_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'google.cloud.aiplatform.v1.tensorboard_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
    _globals['DESCRIPTOR']._loaded_options = None
    _globals['DESCRIPTOR']._serialized_options = b'\n\x1ecom.google.cloud.aiplatform.v1B\x10TensorboardProtoP\x01Z>cloud.google.com/go/aiplatform/apiv1/aiplatformpb;aiplatformpb\xaa\x02\x1aGoogle.Cloud.AIPlatform.V1\xca\x02\x1aGoogle\\Cloud\\AIPlatform\\V1\xea\x02\x1dGoogle::Cloud::AIPlatform::V1'
    _globals['_TENSORBOARD_LABELSENTRY']._loaded_options = None
    _globals['_TENSORBOARD_LABELSENTRY']._serialized_options = b'8\x01'
    _globals['_TENSORBOARD'].fields_by_name['name']._loaded_options = None
    _globals['_TENSORBOARD'].fields_by_name['name']._serialized_options = b'\xe0A\x03'
    _globals['_TENSORBOARD'].fields_by_name['display_name']._loaded_options = None
    _globals['_TENSORBOARD'].fields_by_name['display_name']._serialized_options = b'\xe0A\x02'
    _globals['_TENSORBOARD'].fields_by_name['blob_storage_path_prefix']._loaded_options = None
    _globals['_TENSORBOARD'].fields_by_name['blob_storage_path_prefix']._serialized_options = b'\xe0A\x03'
    _globals['_TENSORBOARD'].fields_by_name['run_count']._loaded_options = None
    _globals['_TENSORBOARD'].fields_by_name['run_count']._serialized_options = b'\xe0A\x03'
    _globals['_TENSORBOARD'].fields_by_name['create_time']._loaded_options = None
    _globals['_TENSORBOARD'].fields_by_name['create_time']._serialized_options = b'\xe0A\x03'
    _globals['_TENSORBOARD'].fields_by_name['update_time']._loaded_options = None
    _globals['_TENSORBOARD'].fields_by_name['update_time']._serialized_options = b'\xe0A\x03'
    _globals['_TENSORBOARD'].fields_by_name['satisfies_pzs']._loaded_options = None
    _globals['_TENSORBOARD'].fields_by_name['satisfies_pzs']._serialized_options = b'\xe0A\x03'
    _globals['_TENSORBOARD'].fields_by_name['satisfies_pzi']._loaded_options = None
    _globals['_TENSORBOARD'].fields_by_name['satisfies_pzi']._serialized_options = b'\xe0A\x03'
    _globals['_TENSORBOARD']._loaded_options = None
    _globals['_TENSORBOARD']._serialized_options = b'\xeaAk\n%aiplatform.googleapis.com/Tensorboard\x12Bprojects/{project}/locations/{location}/tensorboards/{tensorboard}'
    _globals['_TENSORBOARD']._serialized_start = 220
    _globals['_TENSORBOARD']._serialized_end = 858
    _globals['_TENSORBOARD_LABELSENTRY']._serialized_start = 701
    _globals['_TENSORBOARD_LABELSENTRY']._serialized_end = 746