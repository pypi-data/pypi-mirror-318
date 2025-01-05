"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_runtime_version.ValidateProtobufRuntimeVersion(_runtime_version.Domain.PUBLIC, 5, 28, 1, '', 'google/cloud/automl/v1beta1/regression.proto')
_sym_db = _symbol_database.Default()
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n,google/cloud/automl/v1beta1/regression.proto\x12\x1bgoogle.cloud.automl.v1beta1"\xbb\x01\n\x1bRegressionEvaluationMetrics\x12\x1f\n\x17root_mean_squared_error\x18\x01 \x01(\x02\x12\x1b\n\x13mean_absolute_error\x18\x02 \x01(\x02\x12&\n\x1emean_absolute_percentage_error\x18\x03 \x01(\x02\x12\x11\n\tr_squared\x18\x04 \x01(\x02\x12#\n\x1broot_mean_squared_log_error\x18\x05 \x01(\x02B\xaa\x01\n\x1fcom.google.cloud.automl.v1beta1B\x0fRegressionProtoZ7cloud.google.com/go/automl/apiv1beta1/automlpb;automlpb\xca\x02\x1bGoogle\\Cloud\\AutoMl\\V1beta1\xea\x02\x1eGoogle::Cloud::AutoML::V1beta1b\x06proto3')
_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'google.cloud.automl.v1beta1.regression_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
    _globals['DESCRIPTOR']._loaded_options = None
    _globals['DESCRIPTOR']._serialized_options = b'\n\x1fcom.google.cloud.automl.v1beta1B\x0fRegressionProtoZ7cloud.google.com/go/automl/apiv1beta1/automlpb;automlpb\xca\x02\x1bGoogle\\Cloud\\AutoMl\\V1beta1\xea\x02\x1eGoogle::Cloud::AutoML::V1beta1'
    _globals['_REGRESSIONEVALUATIONMETRICS']._serialized_start = 78
    _globals['_REGRESSIONEVALUATIONMETRICS']._serialized_end = 265