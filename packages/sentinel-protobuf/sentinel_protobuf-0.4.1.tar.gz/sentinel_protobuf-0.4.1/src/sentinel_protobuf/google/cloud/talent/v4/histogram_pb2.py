"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_runtime_version.ValidateProtobufRuntimeVersion(_runtime_version.Domain.PUBLIC, 5, 28, 1, '', 'google/cloud/talent/v4/histogram.proto')
_sym_db = _symbol_database.Default()
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n&google/cloud/talent/v4/histogram.proto\x12\x16google.cloud.talent.v4")\n\x0eHistogramQuery\x12\x17\n\x0fhistogram_query\x18\x01 \x01(\t"\xb1\x01\n\x14HistogramQueryResult\x12\x17\n\x0fhistogram_query\x18\x01 \x01(\t\x12N\n\thistogram\x18\x02 \x03(\x0b2;.google.cloud.talent.v4.HistogramQueryResult.HistogramEntry\x1a0\n\x0eHistogramEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\r\n\x05value\x18\x02 \x01(\x03:\x028\x01Bh\n\x1acom.google.cloud.talent.v4B\x0eHistogramProtoP\x01Z2cloud.google.com/go/talent/apiv4/talentpb;talentpb\xa2\x02\x03CTSb\x06proto3')
_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'google.cloud.talent.v4.histogram_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
    _globals['DESCRIPTOR']._loaded_options = None
    _globals['DESCRIPTOR']._serialized_options = b'\n\x1acom.google.cloud.talent.v4B\x0eHistogramProtoP\x01Z2cloud.google.com/go/talent/apiv4/talentpb;talentpb\xa2\x02\x03CTS'
    _globals['_HISTOGRAMQUERYRESULT_HISTOGRAMENTRY']._loaded_options = None
    _globals['_HISTOGRAMQUERYRESULT_HISTOGRAMENTRY']._serialized_options = b'8\x01'
    _globals['_HISTOGRAMQUERY']._serialized_start = 66
    _globals['_HISTOGRAMQUERY']._serialized_end = 107
    _globals['_HISTOGRAMQUERYRESULT']._serialized_start = 110
    _globals['_HISTOGRAMQUERYRESULT']._serialized_end = 287
    _globals['_HISTOGRAMQUERYRESULT_HISTOGRAMENTRY']._serialized_start = 239
    _globals['_HISTOGRAMQUERYRESULT_HISTOGRAMENTRY']._serialized_end = 287