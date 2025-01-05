"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_runtime_version.ValidateProtobufRuntimeVersion(_runtime_version.Domain.PUBLIC, 5, 28, 1, '', 'google/cloud/automl/v1beta1/data_stats.proto')
_sym_db = _symbol_database.Default()
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n,google/cloud/automl/v1beta1/data_stats.proto\x12\x1bgoogle.cloud.automl.v1beta1"\xfd\x03\n\tDataStats\x12B\n\rfloat64_stats\x18\x03 \x01(\x0b2).google.cloud.automl.v1beta1.Float64StatsH\x00\x12@\n\x0cstring_stats\x18\x04 \x01(\x0b2(.google.cloud.automl.v1beta1.StringStatsH\x00\x12F\n\x0ftimestamp_stats\x18\x05 \x01(\x0b2+.google.cloud.automl.v1beta1.TimestampStatsH\x00\x12>\n\x0barray_stats\x18\x06 \x01(\x0b2\'.google.cloud.automl.v1beta1.ArrayStatsH\x00\x12@\n\x0cstruct_stats\x18\x07 \x01(\x0b2(.google.cloud.automl.v1beta1.StructStatsH\x00\x12D\n\x0ecategory_stats\x18\x08 \x01(\x0b2*.google.cloud.automl.v1beta1.CategoryStatsH\x00\x12\x1c\n\x14distinct_value_count\x18\x01 \x01(\x03\x12\x18\n\x10null_value_count\x18\x02 \x01(\x03\x12\x19\n\x11valid_value_count\x18\t \x01(\x03B\x07\n\x05stats"\xdd\x01\n\x0cFloat64Stats\x12\x0c\n\x04mean\x18\x01 \x01(\x01\x12\x1a\n\x12standard_deviation\x18\x02 \x01(\x01\x12\x11\n\tquantiles\x18\x03 \x03(\x01\x12T\n\x11histogram_buckets\x18\x04 \x03(\x0b29.google.cloud.automl.v1beta1.Float64Stats.HistogramBucket\x1a:\n\x0fHistogramBucket\x12\x0b\n\x03min\x18\x01 \x01(\x01\x12\x0b\n\x03max\x18\x02 \x01(\x01\x12\r\n\x05count\x18\x03 \x01(\x03"\x8d\x01\n\x0bStringStats\x12P\n\x11top_unigram_stats\x18\x01 \x03(\x0b25.google.cloud.automl.v1beta1.StringStats.UnigramStats\x1a,\n\x0cUnigramStats\x12\r\n\x05value\x18\x01 \x01(\t\x12\r\n\x05count\x18\x02 \x01(\x03"\xf4\x02\n\x0eTimestampStats\x12V\n\x0egranular_stats\x18\x01 \x03(\x0b2>.google.cloud.automl.v1beta1.TimestampStats.GranularStatsEntry\x1a\x98\x01\n\rGranularStats\x12W\n\x07buckets\x18\x01 \x03(\x0b2F.google.cloud.automl.v1beta1.TimestampStats.GranularStats.BucketsEntry\x1a.\n\x0cBucketsEntry\x12\x0b\n\x03key\x18\x01 \x01(\x05\x12\r\n\x05value\x18\x02 \x01(\x03:\x028\x01\x1ao\n\x12GranularStatsEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12H\n\x05value\x18\x02 \x01(\x0b29.google.cloud.automl.v1beta1.TimestampStats.GranularStats:\x028\x01"J\n\nArrayStats\x12<\n\x0cmember_stats\x18\x02 \x01(\x0b2&.google.cloud.automl.v1beta1.DataStats"\xb7\x01\n\x0bStructStats\x12M\n\x0bfield_stats\x18\x01 \x03(\x0b28.google.cloud.automl.v1beta1.StructStats.FieldStatsEntry\x1aY\n\x0fFieldStatsEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x125\n\x05value\x18\x02 \x01(\x0b2&.google.cloud.automl.v1beta1.DataStats:\x028\x01"\xa0\x01\n\rCategoryStats\x12Z\n\x12top_category_stats\x18\x01 \x03(\x0b2>.google.cloud.automl.v1beta1.CategoryStats.SingleCategoryStats\x1a3\n\x13SingleCategoryStats\x12\r\n\x05value\x18\x01 \x01(\t\x12\r\n\x05count\x18\x02 \x01(\x03"%\n\x10CorrelationStats\x12\x11\n\tcramers_v\x18\x01 \x01(\x01B\x9b\x01\n\x1fcom.google.cloud.automl.v1beta1P\x01Z7cloud.google.com/go/automl/apiv1beta1/automlpb;automlpb\xca\x02\x1bGoogle\\Cloud\\AutoMl\\V1beta1\xea\x02\x1eGoogle::Cloud::AutoML::V1beta1b\x06proto3')
_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'google.cloud.automl.v1beta1.data_stats_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
    _globals['DESCRIPTOR']._loaded_options = None
    _globals['DESCRIPTOR']._serialized_options = b'\n\x1fcom.google.cloud.automl.v1beta1P\x01Z7cloud.google.com/go/automl/apiv1beta1/automlpb;automlpb\xca\x02\x1bGoogle\\Cloud\\AutoMl\\V1beta1\xea\x02\x1eGoogle::Cloud::AutoML::V1beta1'
    _globals['_TIMESTAMPSTATS_GRANULARSTATS_BUCKETSENTRY']._loaded_options = None
    _globals['_TIMESTAMPSTATS_GRANULARSTATS_BUCKETSENTRY']._serialized_options = b'8\x01'
    _globals['_TIMESTAMPSTATS_GRANULARSTATSENTRY']._loaded_options = None
    _globals['_TIMESTAMPSTATS_GRANULARSTATSENTRY']._serialized_options = b'8\x01'
    _globals['_STRUCTSTATS_FIELDSTATSENTRY']._loaded_options = None
    _globals['_STRUCTSTATS_FIELDSTATSENTRY']._serialized_options = b'8\x01'
    _globals['_DATASTATS']._serialized_start = 78
    _globals['_DATASTATS']._serialized_end = 587
    _globals['_FLOAT64STATS']._serialized_start = 590
    _globals['_FLOAT64STATS']._serialized_end = 811
    _globals['_FLOAT64STATS_HISTOGRAMBUCKET']._serialized_start = 753
    _globals['_FLOAT64STATS_HISTOGRAMBUCKET']._serialized_end = 811
    _globals['_STRINGSTATS']._serialized_start = 814
    _globals['_STRINGSTATS']._serialized_end = 955
    _globals['_STRINGSTATS_UNIGRAMSTATS']._serialized_start = 911
    _globals['_STRINGSTATS_UNIGRAMSTATS']._serialized_end = 955
    _globals['_TIMESTAMPSTATS']._serialized_start = 958
    _globals['_TIMESTAMPSTATS']._serialized_end = 1330
    _globals['_TIMESTAMPSTATS_GRANULARSTATS']._serialized_start = 1065
    _globals['_TIMESTAMPSTATS_GRANULARSTATS']._serialized_end = 1217
    _globals['_TIMESTAMPSTATS_GRANULARSTATS_BUCKETSENTRY']._serialized_start = 1171
    _globals['_TIMESTAMPSTATS_GRANULARSTATS_BUCKETSENTRY']._serialized_end = 1217
    _globals['_TIMESTAMPSTATS_GRANULARSTATSENTRY']._serialized_start = 1219
    _globals['_TIMESTAMPSTATS_GRANULARSTATSENTRY']._serialized_end = 1330
    _globals['_ARRAYSTATS']._serialized_start = 1332
    _globals['_ARRAYSTATS']._serialized_end = 1406
    _globals['_STRUCTSTATS']._serialized_start = 1409
    _globals['_STRUCTSTATS']._serialized_end = 1592
    _globals['_STRUCTSTATS_FIELDSTATSENTRY']._serialized_start = 1503
    _globals['_STRUCTSTATS_FIELDSTATSENTRY']._serialized_end = 1592
    _globals['_CATEGORYSTATS']._serialized_start = 1595
    _globals['_CATEGORYSTATS']._serialized_end = 1755
    _globals['_CATEGORYSTATS_SINGLECATEGORYSTATS']._serialized_start = 1704
    _globals['_CATEGORYSTATS_SINGLECATEGORYSTATS']._serialized_end = 1755
    _globals['_CORRELATIONSTATS']._serialized_start = 1757
    _globals['_CORRELATIONSTATS']._serialized_end = 1794