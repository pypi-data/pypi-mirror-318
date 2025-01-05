"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_runtime_version.ValidateProtobufRuntimeVersion(_runtime_version.Domain.PUBLIC, 5, 28, 1, '', 'google/cloud/aiplatform/v1beta1/tensorboard_data.proto')
_sym_db = _symbol_database.Default()
from .....google.api import field_behavior_pb2 as google_dot_api_dot_field__behavior__pb2
from .....google.cloud.aiplatform.v1beta1 import tensorboard_time_series_pb2 as google_dot_cloud_dot_aiplatform_dot_v1beta1_dot_tensorboard__time__series__pb2
from google.protobuf import timestamp_pb2 as google_dot_protobuf_dot_timestamp__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n6google/cloud/aiplatform/v1beta1/tensorboard_data.proto\x12\x1fgoogle.cloud.aiplatform.v1beta1\x1a\x1fgoogle/api/field_behavior.proto\x1a=google/cloud/aiplatform/v1beta1/tensorboard_time_series.proto\x1a\x1fgoogle/protobuf/timestamp.proto"\xe2\x01\n\x0eTimeSeriesData\x12\'\n\x1atensorboard_time_series_id\x18\x01 \x01(\tB\x03\xe0A\x02\x12\\\n\nvalue_type\x18\x02 \x01(\x0e2@.google.cloud.aiplatform.v1beta1.TensorboardTimeSeries.ValueTypeB\x06\xe0A\x02\xe0A\x05\x12I\n\x06values\x18\x03 \x03(\x0b24.google.cloud.aiplatform.v1beta1.TimeSeriesDataPointB\x03\xe0A\x02"\xa7\x02\n\x13TimeSeriesDataPoint\x129\n\x06scalar\x18\x03 \x01(\x0b2\'.google.cloud.aiplatform.v1beta1.ScalarH\x00\x12D\n\x06tensor\x18\x04 \x01(\x0b22.google.cloud.aiplatform.v1beta1.TensorboardTensorH\x00\x12I\n\x05blobs\x18\x05 \x01(\x0b28.google.cloud.aiplatform.v1beta1.TensorboardBlobSequenceH\x00\x12-\n\twall_time\x18\x01 \x01(\x0b2\x1a.google.protobuf.Timestamp\x12\x0c\n\x04step\x18\x02 \x01(\x03B\x07\n\x05value"\x17\n\x06Scalar\x12\r\n\x05value\x18\x01 \x01(\x01"D\n\x11TensorboardTensor\x12\x12\n\x05value\x18\x01 \x01(\x0cB\x03\xe0A\x02\x12\x1b\n\x0eversion_number\x18\x02 \x01(\x05B\x03\xe0A\x01"[\n\x17TensorboardBlobSequence\x12@\n\x06values\x18\x01 \x03(\x0b20.google.cloud.aiplatform.v1beta1.TensorboardBlob"5\n\x0fTensorboardBlob\x12\x0f\n\x02id\x18\x01 \x01(\tB\x03\xe0A\x03\x12\x11\n\x04data\x18\x02 \x01(\x0cB\x03\xe0A\x01B\xeb\x01\n#com.google.cloud.aiplatform.v1beta1B\x14TensorboardDataProtoP\x01ZCcloud.google.com/go/aiplatform/apiv1beta1/aiplatformpb;aiplatformpb\xaa\x02\x1fGoogle.Cloud.AIPlatform.V1Beta1\xca\x02\x1fGoogle\\Cloud\\AIPlatform\\V1beta1\xea\x02"Google::Cloud::AIPlatform::V1beta1b\x06proto3')
_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'google.cloud.aiplatform.v1beta1.tensorboard_data_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
    _globals['DESCRIPTOR']._loaded_options = None
    _globals['DESCRIPTOR']._serialized_options = b'\n#com.google.cloud.aiplatform.v1beta1B\x14TensorboardDataProtoP\x01ZCcloud.google.com/go/aiplatform/apiv1beta1/aiplatformpb;aiplatformpb\xaa\x02\x1fGoogle.Cloud.AIPlatform.V1Beta1\xca\x02\x1fGoogle\\Cloud\\AIPlatform\\V1beta1\xea\x02"Google::Cloud::AIPlatform::V1beta1'
    _globals['_TIMESERIESDATA'].fields_by_name['tensorboard_time_series_id']._loaded_options = None
    _globals['_TIMESERIESDATA'].fields_by_name['tensorboard_time_series_id']._serialized_options = b'\xe0A\x02'
    _globals['_TIMESERIESDATA'].fields_by_name['value_type']._loaded_options = None
    _globals['_TIMESERIESDATA'].fields_by_name['value_type']._serialized_options = b'\xe0A\x02\xe0A\x05'
    _globals['_TIMESERIESDATA'].fields_by_name['values']._loaded_options = None
    _globals['_TIMESERIESDATA'].fields_by_name['values']._serialized_options = b'\xe0A\x02'
    _globals['_TENSORBOARDTENSOR'].fields_by_name['value']._loaded_options = None
    _globals['_TENSORBOARDTENSOR'].fields_by_name['value']._serialized_options = b'\xe0A\x02'
    _globals['_TENSORBOARDTENSOR'].fields_by_name['version_number']._loaded_options = None
    _globals['_TENSORBOARDTENSOR'].fields_by_name['version_number']._serialized_options = b'\xe0A\x01'
    _globals['_TENSORBOARDBLOB'].fields_by_name['id']._loaded_options = None
    _globals['_TENSORBOARDBLOB'].fields_by_name['id']._serialized_options = b'\xe0A\x03'
    _globals['_TENSORBOARDBLOB'].fields_by_name['data']._loaded_options = None
    _globals['_TENSORBOARDBLOB'].fields_by_name['data']._serialized_options = b'\xe0A\x01'
    _globals['_TIMESERIESDATA']._serialized_start = 221
    _globals['_TIMESERIESDATA']._serialized_end = 447
    _globals['_TIMESERIESDATAPOINT']._serialized_start = 450
    _globals['_TIMESERIESDATAPOINT']._serialized_end = 745
    _globals['_SCALAR']._serialized_start = 747
    _globals['_SCALAR']._serialized_end = 770
    _globals['_TENSORBOARDTENSOR']._serialized_start = 772
    _globals['_TENSORBOARDTENSOR']._serialized_end = 840
    _globals['_TENSORBOARDBLOBSEQUENCE']._serialized_start = 842
    _globals['_TENSORBOARDBLOBSEQUENCE']._serialized_end = 933
    _globals['_TENSORBOARDBLOB']._serialized_start = 935
    _globals['_TENSORBOARDBLOB']._serialized_end = 988