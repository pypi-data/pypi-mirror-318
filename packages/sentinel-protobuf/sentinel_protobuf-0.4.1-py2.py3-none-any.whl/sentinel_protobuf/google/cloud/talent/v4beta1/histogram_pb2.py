"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_runtime_version.ValidateProtobufRuntimeVersion(_runtime_version.Domain.PUBLIC, 5, 28, 1, '', 'google/cloud/talent/v4beta1/histogram.proto')
_sym_db = _symbol_database.Default()
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n+google/cloud/talent/v4beta1/histogram.proto\x12\x1bgoogle.cloud.talent.v4beta1")\n\x0eHistogramQuery\x12\x17\n\x0fhistogram_query\x18\x01 \x01(\t"\xb6\x01\n\x14HistogramQueryResult\x12\x17\n\x0fhistogram_query\x18\x01 \x01(\t\x12S\n\thistogram\x18\x02 \x03(\x0b2@.google.cloud.talent.v4beta1.HistogramQueryResult.HistogramEntry\x1a0\n\x0eHistogramEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\r\n\x05value\x18\x02 \x01(\x03:\x028\x01Br\n\x1fcom.google.cloud.talent.v4beta1B\x0eHistogramProtoP\x01Z7cloud.google.com/go/talent/apiv4beta1/talentpb;talentpb\xa2\x02\x03CTSb\x06proto3')
_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'google.cloud.talent.v4beta1.histogram_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
    _globals['DESCRIPTOR']._loaded_options = None
    _globals['DESCRIPTOR']._serialized_options = b'\n\x1fcom.google.cloud.talent.v4beta1B\x0eHistogramProtoP\x01Z7cloud.google.com/go/talent/apiv4beta1/talentpb;talentpb\xa2\x02\x03CTS'
    _globals['_HISTOGRAMQUERYRESULT_HISTOGRAMENTRY']._loaded_options = None
    _globals['_HISTOGRAMQUERYRESULT_HISTOGRAMENTRY']._serialized_options = b'8\x01'
    _globals['_HISTOGRAMQUERY']._serialized_start = 76
    _globals['_HISTOGRAMQUERY']._serialized_end = 117
    _globals['_HISTOGRAMQUERYRESULT']._serialized_start = 120
    _globals['_HISTOGRAMQUERYRESULT']._serialized_end = 302
    _globals['_HISTOGRAMQUERYRESULT_HISTOGRAMENTRY']._serialized_start = 254
    _globals['_HISTOGRAMQUERYRESULT_HISTOGRAMENTRY']._serialized_end = 302