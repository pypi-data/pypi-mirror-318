"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_runtime_version.ValidateProtobufRuntimeVersion(_runtime_version.Domain.PUBLIC, 5, 28, 1, '', 'google/api/quota.proto')
_sym_db = _symbol_database.Default()
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x16google/api/quota.proto\x12\ngoogle.api"]\n\x05Quota\x12&\n\x06limits\x18\x03 \x03(\x0b2\x16.google.api.QuotaLimit\x12,\n\x0cmetric_rules\x18\x04 \x03(\x0b2\x16.google.api.MetricRule"\x91\x01\n\nMetricRule\x12\x10\n\x08selector\x18\x01 \x01(\t\x12=\n\x0cmetric_costs\x18\x02 \x03(\x0b2\'.google.api.MetricRule.MetricCostsEntry\x1a2\n\x10MetricCostsEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\r\n\x05value\x18\x02 \x01(\x03:\x028\x01"\x95\x02\n\nQuotaLimit\x12\x0c\n\x04name\x18\x06 \x01(\t\x12\x13\n\x0bdescription\x18\x02 \x01(\t\x12\x15\n\rdefault_limit\x18\x03 \x01(\x03\x12\x11\n\tmax_limit\x18\x04 \x01(\x03\x12\x11\n\tfree_tier\x18\x07 \x01(\x03\x12\x10\n\x08duration\x18\x05 \x01(\t\x12\x0e\n\x06metric\x18\x08 \x01(\t\x12\x0c\n\x04unit\x18\t \x01(\t\x122\n\x06values\x18\n \x03(\x0b2".google.api.QuotaLimit.ValuesEntry\x12\x14\n\x0cdisplay_name\x18\x0c \x01(\t\x1a-\n\x0bValuesEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\r\n\x05value\x18\x02 \x01(\x03:\x028\x01Bl\n\x0ecom.google.apiB\nQuotaProtoP\x01ZEgoogle.golang.org/genproto/googleapis/api/serviceconfig;serviceconfig\xa2\x02\x04GAPIb\x06proto3')
_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'google.api.quota_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
    _globals['DESCRIPTOR']._loaded_options = None
    _globals['DESCRIPTOR']._serialized_options = b'\n\x0ecom.google.apiB\nQuotaProtoP\x01ZEgoogle.golang.org/genproto/googleapis/api/serviceconfig;serviceconfig\xa2\x02\x04GAPI'
    _globals['_METRICRULE_METRICCOSTSENTRY']._loaded_options = None
    _globals['_METRICRULE_METRICCOSTSENTRY']._serialized_options = b'8\x01'
    _globals['_QUOTALIMIT_VALUESENTRY']._loaded_options = None
    _globals['_QUOTALIMIT_VALUESENTRY']._serialized_options = b'8\x01'
    _globals['_QUOTA']._serialized_start = 38
    _globals['_QUOTA']._serialized_end = 131
    _globals['_METRICRULE']._serialized_start = 134
    _globals['_METRICRULE']._serialized_end = 279
    _globals['_METRICRULE_METRICCOSTSENTRY']._serialized_start = 229
    _globals['_METRICRULE_METRICCOSTSENTRY']._serialized_end = 279
    _globals['_QUOTALIMIT']._serialized_start = 282
    _globals['_QUOTALIMIT']._serialized_end = 559
    _globals['_QUOTALIMIT_VALUESENTRY']._serialized_start = 514
    _globals['_QUOTALIMIT_VALUESENTRY']._serialized_end = 559