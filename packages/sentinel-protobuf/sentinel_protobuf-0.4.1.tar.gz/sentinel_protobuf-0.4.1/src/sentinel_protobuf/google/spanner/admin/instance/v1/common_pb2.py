"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_runtime_version.ValidateProtobufRuntimeVersion(_runtime_version.Domain.PUBLIC, 5, 28, 1, '', 'google/spanner/admin/instance/v1/common.proto')
_sym_db = _symbol_database.Default()
from ......google.api import field_behavior_pb2 as google_dot_api_dot_field__behavior__pb2
from ......google.api import resource_pb2 as google_dot_api_dot_resource__pb2
from google.protobuf import timestamp_pb2 as google_dot_protobuf_dot_timestamp__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n-google/spanner/admin/instance/v1/common.proto\x12 google.spanner.admin.instance.v1\x1a\x1fgoogle/api/field_behavior.proto\x1a\x19google/api/resource.proto\x1a\x1fgoogle/protobuf/timestamp.proto"\x8b\x01\n\x11OperationProgress\x12\x18\n\x10progress_percent\x18\x01 \x01(\x05\x12.\n\nstart_time\x18\x02 \x01(\x0b2\x1a.google.protobuf.Timestamp\x12,\n\x08end_time\x18\x03 \x01(\x0b2\x1a.google.protobuf.Timestamp")\n\x10ReplicaSelection\x12\x15\n\x08location\x18\x01 \x01(\tB\x03\xe0A\x02*w\n\x11FulfillmentPeriod\x12"\n\x1eFULFILLMENT_PERIOD_UNSPECIFIED\x10\x00\x12\x1d\n\x19FULFILLMENT_PERIOD_NORMAL\x10\x01\x12\x1f\n\x1bFULFILLMENT_PERIOD_EXTENDED\x10\x02B\xfd\x01\n$com.google.spanner.admin.instance.v1B\x0bCommonProtoP\x01ZFcloud.google.com/go/spanner/admin/instance/apiv1/instancepb;instancepb\xaa\x02&Google.Cloud.Spanner.Admin.Instance.V1\xca\x02&Google\\Cloud\\Spanner\\Admin\\Instance\\V1\xea\x02+Google::Cloud::Spanner::Admin::Instance::V1b\x06proto3')
_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'google.spanner.admin.instance.v1.common_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
    _globals['DESCRIPTOR']._loaded_options = None
    _globals['DESCRIPTOR']._serialized_options = b'\n$com.google.spanner.admin.instance.v1B\x0bCommonProtoP\x01ZFcloud.google.com/go/spanner/admin/instance/apiv1/instancepb;instancepb\xaa\x02&Google.Cloud.Spanner.Admin.Instance.V1\xca\x02&Google\\Cloud\\Spanner\\Admin\\Instance\\V1\xea\x02+Google::Cloud::Spanner::Admin::Instance::V1'
    _globals['_REPLICASELECTION'].fields_by_name['location']._loaded_options = None
    _globals['_REPLICASELECTION'].fields_by_name['location']._serialized_options = b'\xe0A\x02'
    _globals['_FULFILLMENTPERIOD']._serialized_start = 361
    _globals['_FULFILLMENTPERIOD']._serialized_end = 480
    _globals['_OPERATIONPROGRESS']._serialized_start = 177
    _globals['_OPERATIONPROGRESS']._serialized_end = 316
    _globals['_REPLICASELECTION']._serialized_start = 318
    _globals['_REPLICASELECTION']._serialized_end = 359