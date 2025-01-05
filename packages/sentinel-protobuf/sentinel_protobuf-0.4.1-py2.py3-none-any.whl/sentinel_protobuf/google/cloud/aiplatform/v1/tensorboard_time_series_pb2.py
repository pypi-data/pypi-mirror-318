"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_runtime_version.ValidateProtobufRuntimeVersion(_runtime_version.Domain.PUBLIC, 5, 28, 1, '', 'google/cloud/aiplatform/v1/tensorboard_time_series.proto')
_sym_db = _symbol_database.Default()
from .....google.api import field_behavior_pb2 as google_dot_api_dot_field__behavior__pb2
from .....google.api import resource_pb2 as google_dot_api_dot_resource__pb2
from google.protobuf import timestamp_pb2 as google_dot_protobuf_dot_timestamp__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n8google/cloud/aiplatform/v1/tensorboard_time_series.proto\x12\x1agoogle.cloud.aiplatform.v1\x1a\x1fgoogle/api/field_behavior.proto\x1a\x19google/api/resource.proto\x1a\x1fgoogle/protobuf/timestamp.proto"\xbf\x06\n\x15TensorboardTimeSeries\x12\x11\n\x04name\x18\x01 \x01(\tB\x03\xe0A\x03\x12\x19\n\x0cdisplay_name\x18\x02 \x01(\tB\x03\xe0A\x02\x12\x13\n\x0bdescription\x18\x03 \x01(\t\x12W\n\nvalue_type\x18\x04 \x01(\x0e2;.google.cloud.aiplatform.v1.TensorboardTimeSeries.ValueTypeB\x06\xe0A\x02\xe0A\x05\x124\n\x0bcreate_time\x18\x05 \x01(\x0b2\x1a.google.protobuf.TimestampB\x03\xe0A\x03\x124\n\x0bupdate_time\x18\x06 \x01(\x0b2\x1a.google.protobuf.TimestampB\x03\xe0A\x03\x12\x0c\n\x04etag\x18\x07 \x01(\t\x12\x18\n\x0bplugin_name\x18\x08 \x01(\tB\x03\xe0A\x05\x12\x13\n\x0bplugin_data\x18\t \x01(\x0c\x12Q\n\x08metadata\x18\n \x01(\x0b2:.google.cloud.aiplatform.v1.TensorboardTimeSeries.MetadataB\x03\xe0A\x03\x1a\x80\x01\n\x08Metadata\x12\x15\n\x08max_step\x18\x01 \x01(\x03B\x03\xe0A\x03\x126\n\rmax_wall_time\x18\x02 \x01(\x0b2\x1a.google.protobuf.TimestampB\x03\xe0A\x03\x12%\n\x18max_blob_sequence_length\x18\x03 \x01(\x03B\x03\xe0A\x03"R\n\tValueType\x12\x1a\n\x16VALUE_TYPE_UNSPECIFIED\x10\x00\x12\n\n\x06SCALAR\x10\x01\x12\n\n\x06TENSOR\x10\x02\x12\x11\n\rBLOB_SEQUENCE\x10\x03:\xb6\x01\xeaA\xb2\x01\n/aiplatform.googleapis.com/TensorboardTimeSeries\x12\x7fprojects/{project}/locations/{location}/tensorboards/{tensorboard}/experiments/{experiment}/runs/{run}/timeSeries/{time_series}B\xd8\x01\n\x1ecom.google.cloud.aiplatform.v1B\x1aTensorboardTimeSeriesProtoP\x01Z>cloud.google.com/go/aiplatform/apiv1/aiplatformpb;aiplatformpb\xaa\x02\x1aGoogle.Cloud.AIPlatform.V1\xca\x02\x1aGoogle\\Cloud\\AIPlatform\\V1\xea\x02\x1dGoogle::Cloud::AIPlatform::V1b\x06proto3')
_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'google.cloud.aiplatform.v1.tensorboard_time_series_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
    _globals['DESCRIPTOR']._loaded_options = None
    _globals['DESCRIPTOR']._serialized_options = b'\n\x1ecom.google.cloud.aiplatform.v1B\x1aTensorboardTimeSeriesProtoP\x01Z>cloud.google.com/go/aiplatform/apiv1/aiplatformpb;aiplatformpb\xaa\x02\x1aGoogle.Cloud.AIPlatform.V1\xca\x02\x1aGoogle\\Cloud\\AIPlatform\\V1\xea\x02\x1dGoogle::Cloud::AIPlatform::V1'
    _globals['_TENSORBOARDTIMESERIES_METADATA'].fields_by_name['max_step']._loaded_options = None
    _globals['_TENSORBOARDTIMESERIES_METADATA'].fields_by_name['max_step']._serialized_options = b'\xe0A\x03'
    _globals['_TENSORBOARDTIMESERIES_METADATA'].fields_by_name['max_wall_time']._loaded_options = None
    _globals['_TENSORBOARDTIMESERIES_METADATA'].fields_by_name['max_wall_time']._serialized_options = b'\xe0A\x03'
    _globals['_TENSORBOARDTIMESERIES_METADATA'].fields_by_name['max_blob_sequence_length']._loaded_options = None
    _globals['_TENSORBOARDTIMESERIES_METADATA'].fields_by_name['max_blob_sequence_length']._serialized_options = b'\xe0A\x03'
    _globals['_TENSORBOARDTIMESERIES'].fields_by_name['name']._loaded_options = None
    _globals['_TENSORBOARDTIMESERIES'].fields_by_name['name']._serialized_options = b'\xe0A\x03'
    _globals['_TENSORBOARDTIMESERIES'].fields_by_name['display_name']._loaded_options = None
    _globals['_TENSORBOARDTIMESERIES'].fields_by_name['display_name']._serialized_options = b'\xe0A\x02'
    _globals['_TENSORBOARDTIMESERIES'].fields_by_name['value_type']._loaded_options = None
    _globals['_TENSORBOARDTIMESERIES'].fields_by_name['value_type']._serialized_options = b'\xe0A\x02\xe0A\x05'
    _globals['_TENSORBOARDTIMESERIES'].fields_by_name['create_time']._loaded_options = None
    _globals['_TENSORBOARDTIMESERIES'].fields_by_name['create_time']._serialized_options = b'\xe0A\x03'
    _globals['_TENSORBOARDTIMESERIES'].fields_by_name['update_time']._loaded_options = None
    _globals['_TENSORBOARDTIMESERIES'].fields_by_name['update_time']._serialized_options = b'\xe0A\x03'
    _globals['_TENSORBOARDTIMESERIES'].fields_by_name['plugin_name']._loaded_options = None
    _globals['_TENSORBOARDTIMESERIES'].fields_by_name['plugin_name']._serialized_options = b'\xe0A\x05'
    _globals['_TENSORBOARDTIMESERIES'].fields_by_name['metadata']._loaded_options = None
    _globals['_TENSORBOARDTIMESERIES'].fields_by_name['metadata']._serialized_options = b'\xe0A\x03'
    _globals['_TENSORBOARDTIMESERIES']._loaded_options = None
    _globals['_TENSORBOARDTIMESERIES']._serialized_options = b'\xeaA\xb2\x01\n/aiplatform.googleapis.com/TensorboardTimeSeries\x12\x7fprojects/{project}/locations/{location}/tensorboards/{tensorboard}/experiments/{experiment}/runs/{run}/timeSeries/{time_series}'
    _globals['_TENSORBOARDTIMESERIES']._serialized_start = 182
    _globals['_TENSORBOARDTIMESERIES']._serialized_end = 1013
    _globals['_TENSORBOARDTIMESERIES_METADATA']._serialized_start = 616
    _globals['_TENSORBOARDTIMESERIES_METADATA']._serialized_end = 744
    _globals['_TENSORBOARDTIMESERIES_VALUETYPE']._serialized_start = 746
    _globals['_TENSORBOARDTIMESERIES_VALUETYPE']._serialized_end = 828