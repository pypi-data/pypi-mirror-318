"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_runtime_version.ValidateProtobufRuntimeVersion(_runtime_version.Domain.PUBLIC, 5, 28, 1, '', 'google/cloud/datacatalog/v1beta1/usage.proto')
_sym_db = _symbol_database.Default()
from google.protobuf import timestamp_pb2 as google_dot_protobuf_dot_timestamp__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n,google/cloud/datacatalog/v1beta1/usage.proto\x12 google.cloud.datacatalog.v1beta1\x1a\x1fgoogle/protobuf/timestamp.proto"\x91\x01\n\nUsageStats\x12\x19\n\x11total_completions\x18\x01 \x01(\x02\x12\x16\n\x0etotal_failures\x18\x02 \x01(\x02\x12\x1b\n\x13total_cancellations\x18\x03 \x01(\x02\x123\n+total_execution_time_for_completions_millis\x18\x04 \x01(\x02"\x93\x02\n\x0bUsageSignal\x12/\n\x0bupdate_time\x18\x01 \x01(\x0b2\x1a.google.protobuf.Timestamp\x12h\n\x17usage_within_time_range\x18\x02 \x03(\x0b2G.google.cloud.datacatalog.v1beta1.UsageSignal.UsageWithinTimeRangeEntry\x1ai\n\x19UsageWithinTimeRangeEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12;\n\x05value\x18\x02 \x01(\x0b2,.google.cloud.datacatalog.v1beta1.UsageStats:\x028\x01B\xdc\x01\n$com.google.cloud.datacatalog.v1beta1P\x01ZFcloud.google.com/go/datacatalog/apiv1beta1/datacatalogpb;datacatalogpb\xaa\x02 Google.Cloud.DataCatalog.V1Beta1\xca\x02 Google\\Cloud\\DataCatalog\\V1beta1\xea\x02#Google::Cloud::DataCatalog::V1beta1b\x06proto3')
_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'google.cloud.datacatalog.v1beta1.usage_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
    _globals['DESCRIPTOR']._loaded_options = None
    _globals['DESCRIPTOR']._serialized_options = b'\n$com.google.cloud.datacatalog.v1beta1P\x01ZFcloud.google.com/go/datacatalog/apiv1beta1/datacatalogpb;datacatalogpb\xaa\x02 Google.Cloud.DataCatalog.V1Beta1\xca\x02 Google\\Cloud\\DataCatalog\\V1beta1\xea\x02#Google::Cloud::DataCatalog::V1beta1'
    _globals['_USAGESIGNAL_USAGEWITHINTIMERANGEENTRY']._loaded_options = None
    _globals['_USAGESIGNAL_USAGEWITHINTIMERANGEENTRY']._serialized_options = b'8\x01'
    _globals['_USAGESTATS']._serialized_start = 116
    _globals['_USAGESTATS']._serialized_end = 261
    _globals['_USAGESIGNAL']._serialized_start = 264
    _globals['_USAGESIGNAL']._serialized_end = 539
    _globals['_USAGESIGNAL_USAGEWITHINTIMERANGEENTRY']._serialized_start = 434
    _globals['_USAGESIGNAL_USAGEWITHINTIMERANGEENTRY']._serialized_end = 539