"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_runtime_version.ValidateProtobufRuntimeVersion(_runtime_version.Domain.PUBLIC, 5, 28, 1, '', 'google/cloud/aiplatform/v1/tensorboard_experiment.proto')
_sym_db = _symbol_database.Default()
from .....google.api import field_behavior_pb2 as google_dot_api_dot_field__behavior__pb2
from .....google.api import resource_pb2 as google_dot_api_dot_resource__pb2
from google.protobuf import timestamp_pb2 as google_dot_protobuf_dot_timestamp__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n7google/cloud/aiplatform/v1/tensorboard_experiment.proto\x12\x1agoogle.cloud.aiplatform.v1\x1a\x1fgoogle/api/field_behavior.proto\x1a\x19google/api/resource.proto\x1a\x1fgoogle/protobuf/timestamp.proto"\xf7\x03\n\x15TensorboardExperiment\x12\x11\n\x04name\x18\x01 \x01(\tB\x03\xe0A\x03\x12\x14\n\x0cdisplay_name\x18\x02 \x01(\t\x12\x13\n\x0bdescription\x18\x03 \x01(\t\x124\n\x0bcreate_time\x18\x04 \x01(\x0b2\x1a.google.protobuf.TimestampB\x03\xe0A\x03\x124\n\x0bupdate_time\x18\x05 \x01(\x0b2\x1a.google.protobuf.TimestampB\x03\xe0A\x03\x12M\n\x06labels\x18\x06 \x03(\x0b2=.google.cloud.aiplatform.v1.TensorboardExperiment.LabelsEntry\x12\x0c\n\x04etag\x18\x07 \x01(\t\x12\x13\n\x06source\x18\x08 \x01(\tB\x03\xe0A\x05\x1a-\n\x0bLabelsEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\r\n\x05value\x18\x02 \x01(\t:\x028\x01:\x92\x01\xeaA\x8e\x01\n/aiplatform.googleapis.com/TensorboardExperiment\x12[projects/{project}/locations/{location}/tensorboards/{tensorboard}/experiments/{experiment}B\xd8\x01\n\x1ecom.google.cloud.aiplatform.v1B\x1aTensorboardExperimentProtoP\x01Z>cloud.google.com/go/aiplatform/apiv1/aiplatformpb;aiplatformpb\xaa\x02\x1aGoogle.Cloud.AIPlatform.V1\xca\x02\x1aGoogle\\Cloud\\AIPlatform\\V1\xea\x02\x1dGoogle::Cloud::AIPlatform::V1b\x06proto3')
_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'google.cloud.aiplatform.v1.tensorboard_experiment_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
    _globals['DESCRIPTOR']._loaded_options = None
    _globals['DESCRIPTOR']._serialized_options = b'\n\x1ecom.google.cloud.aiplatform.v1B\x1aTensorboardExperimentProtoP\x01Z>cloud.google.com/go/aiplatform/apiv1/aiplatformpb;aiplatformpb\xaa\x02\x1aGoogle.Cloud.AIPlatform.V1\xca\x02\x1aGoogle\\Cloud\\AIPlatform\\V1\xea\x02\x1dGoogle::Cloud::AIPlatform::V1'
    _globals['_TENSORBOARDEXPERIMENT_LABELSENTRY']._loaded_options = None
    _globals['_TENSORBOARDEXPERIMENT_LABELSENTRY']._serialized_options = b'8\x01'
    _globals['_TENSORBOARDEXPERIMENT'].fields_by_name['name']._loaded_options = None
    _globals['_TENSORBOARDEXPERIMENT'].fields_by_name['name']._serialized_options = b'\xe0A\x03'
    _globals['_TENSORBOARDEXPERIMENT'].fields_by_name['create_time']._loaded_options = None
    _globals['_TENSORBOARDEXPERIMENT'].fields_by_name['create_time']._serialized_options = b'\xe0A\x03'
    _globals['_TENSORBOARDEXPERIMENT'].fields_by_name['update_time']._loaded_options = None
    _globals['_TENSORBOARDEXPERIMENT'].fields_by_name['update_time']._serialized_options = b'\xe0A\x03'
    _globals['_TENSORBOARDEXPERIMENT'].fields_by_name['source']._loaded_options = None
    _globals['_TENSORBOARDEXPERIMENT'].fields_by_name['source']._serialized_options = b'\xe0A\x05'
    _globals['_TENSORBOARDEXPERIMENT']._loaded_options = None
    _globals['_TENSORBOARDEXPERIMENT']._serialized_options = b'\xeaA\x8e\x01\n/aiplatform.googleapis.com/TensorboardExperiment\x12[projects/{project}/locations/{location}/tensorboards/{tensorboard}/experiments/{experiment}'
    _globals['_TENSORBOARDEXPERIMENT']._serialized_start = 181
    _globals['_TENSORBOARDEXPERIMENT']._serialized_end = 684
    _globals['_TENSORBOARDEXPERIMENT_LABELSENTRY']._serialized_start = 490
    _globals['_TENSORBOARDEXPERIMENT_LABELSENTRY']._serialized_end = 535