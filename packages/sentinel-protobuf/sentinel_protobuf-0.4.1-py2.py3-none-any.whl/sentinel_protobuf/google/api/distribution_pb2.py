"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_runtime_version.ValidateProtobufRuntimeVersion(_runtime_version.Domain.PUBLIC, 5, 28, 1, '', 'google/api/distribution.proto')
_sym_db = _symbol_database.Default()
from google.protobuf import any_pb2 as google_dot_protobuf_dot_any__pb2
from google.protobuf import timestamp_pb2 as google_dot_protobuf_dot_timestamp__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x1dgoogle/api/distribution.proto\x12\ngoogle.api\x1a\x19google/protobuf/any.proto\x1a\x1fgoogle/protobuf/timestamp.proto"\xd9\x06\n\x0cDistribution\x12\r\n\x05count\x18\x01 \x01(\x03\x12\x0c\n\x04mean\x18\x02 \x01(\x01\x12 \n\x18sum_of_squared_deviation\x18\x03 \x01(\x01\x12-\n\x05range\x18\x04 \x01(\x0b2\x1e.google.api.Distribution.Range\x12>\n\x0ebucket_options\x18\x06 \x01(\x0b2&.google.api.Distribution.BucketOptions\x12\x15\n\rbucket_counts\x18\x07 \x03(\x03\x124\n\texemplars\x18\n \x03(\x0b2!.google.api.Distribution.Exemplar\x1a!\n\x05Range\x12\x0b\n\x03min\x18\x01 \x01(\x01\x12\x0b\n\x03max\x18\x02 \x01(\x01\x1a\xb5\x03\n\rBucketOptions\x12G\n\x0elinear_buckets\x18\x01 \x01(\x0b2-.google.api.Distribution.BucketOptions.LinearH\x00\x12Q\n\x13exponential_buckets\x18\x02 \x01(\x0b22.google.api.Distribution.BucketOptions.ExponentialH\x00\x12K\n\x10explicit_buckets\x18\x03 \x01(\x0b2/.google.api.Distribution.BucketOptions.ExplicitH\x00\x1aC\n\x06Linear\x12\x1a\n\x12num_finite_buckets\x18\x01 \x01(\x05\x12\r\n\x05width\x18\x02 \x01(\x01\x12\x0e\n\x06offset\x18\x03 \x01(\x01\x1aO\n\x0bExponential\x12\x1a\n\x12num_finite_buckets\x18\x01 \x01(\x05\x12\x15\n\rgrowth_factor\x18\x02 \x01(\x01\x12\r\n\x05scale\x18\x03 \x01(\x01\x1a\x1a\n\x08Explicit\x12\x0e\n\x06bounds\x18\x01 \x03(\x01B\t\n\x07options\x1as\n\x08Exemplar\x12\r\n\x05value\x18\x01 \x01(\x01\x12-\n\ttimestamp\x18\x02 \x01(\x0b2\x1a.google.protobuf.Timestamp\x12)\n\x0battachments\x18\x03 \x03(\x0b2\x14.google.protobuf.AnyBq\n\x0ecom.google.apiB\x11DistributionProtoP\x01ZCgoogle.golang.org/genproto/googleapis/api/distribution;distribution\xa2\x02\x04GAPIb\x06proto3')
_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'google.api.distribution_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
    _globals['DESCRIPTOR']._loaded_options = None
    _globals['DESCRIPTOR']._serialized_options = b'\n\x0ecom.google.apiB\x11DistributionProtoP\x01ZCgoogle.golang.org/genproto/googleapis/api/distribution;distribution\xa2\x02\x04GAPI'
    _globals['_DISTRIBUTION']._serialized_start = 106
    _globals['_DISTRIBUTION']._serialized_end = 963
    _globals['_DISTRIBUTION_RANGE']._serialized_start = 373
    _globals['_DISTRIBUTION_RANGE']._serialized_end = 406
    _globals['_DISTRIBUTION_BUCKETOPTIONS']._serialized_start = 409
    _globals['_DISTRIBUTION_BUCKETOPTIONS']._serialized_end = 846
    _globals['_DISTRIBUTION_BUCKETOPTIONS_LINEAR']._serialized_start = 659
    _globals['_DISTRIBUTION_BUCKETOPTIONS_LINEAR']._serialized_end = 726
    _globals['_DISTRIBUTION_BUCKETOPTIONS_EXPONENTIAL']._serialized_start = 728
    _globals['_DISTRIBUTION_BUCKETOPTIONS_EXPONENTIAL']._serialized_end = 807
    _globals['_DISTRIBUTION_BUCKETOPTIONS_EXPLICIT']._serialized_start = 809
    _globals['_DISTRIBUTION_BUCKETOPTIONS_EXPLICIT']._serialized_end = 835
    _globals['_DISTRIBUTION_EXEMPLAR']._serialized_start = 848
    _globals['_DISTRIBUTION_EXEMPLAR']._serialized_end = 963