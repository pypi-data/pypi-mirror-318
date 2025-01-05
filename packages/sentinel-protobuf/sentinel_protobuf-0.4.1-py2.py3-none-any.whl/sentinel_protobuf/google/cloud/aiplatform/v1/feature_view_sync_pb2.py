"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_runtime_version.ValidateProtobufRuntimeVersion(_runtime_version.Domain.PUBLIC, 5, 28, 1, '', 'google/cloud/aiplatform/v1/feature_view_sync.proto')
_sym_db = _symbol_database.Default()
from .....google.api import field_behavior_pb2 as google_dot_api_dot_field__behavior__pb2
from .....google.api import resource_pb2 as google_dot_api_dot_resource__pb2
from google.protobuf import timestamp_pb2 as google_dot_protobuf_dot_timestamp__pb2
from .....google.rpc import status_pb2 as google_dot_rpc_dot_status__pb2
from .....google.type import interval_pb2 as google_dot_type_dot_interval__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n2google/cloud/aiplatform/v1/feature_view_sync.proto\x12\x1agoogle.cloud.aiplatform.v1\x1a\x1fgoogle/api/field_behavior.proto\x1a\x19google/api/resource.proto\x1a\x1fgoogle/protobuf/timestamp.proto\x1a\x17google/rpc/status.proto\x1a\x1agoogle/type/interval.proto"\x85\x05\n\x0fFeatureViewSync\x12\x11\n\x04name\x18\x01 \x01(\tB\x03\xe0A\x08\x124\n\x0bcreate_time\x18\x02 \x01(\x0b2\x1a.google.protobuf.TimestampB\x03\xe0A\x03\x12,\n\x08run_time\x18\x05 \x01(\x0b2\x15.google.type.IntervalB\x03\xe0A\x03\x12-\n\x0cfinal_status\x18\x04 \x01(\x0b2\x12.google.rpc.StatusB\x03\xe0A\x03\x12R\n\x0csync_summary\x18\x06 \x01(\x0b27.google.cloud.aiplatform.v1.FeatureViewSync.SyncSummaryB\x03\xe0A\x03\x12\x1a\n\rsatisfies_pzs\x18\x07 \x01(\x08B\x03\xe0A\x03\x12\x1a\n\rsatisfies_pzi\x18\x08 \x01(\x08B\x03\xe0A\x03\x1az\n\x0bSyncSummary\x12\x17\n\nrow_synced\x18\x01 \x01(\x03B\x03\xe0A\x03\x12\x17\n\ntotal_slot\x18\x02 \x01(\x03B\x03\xe0A\x03\x129\n\x15system_watermark_time\x18\x05 \x01(\x0b2\x1a.google.protobuf.Timestamp:\xc3\x01\xeaA\xbf\x01\n)aiplatform.googleapis.com/FeatureViewSync\x12\x91\x01projects/{project}/locations/{location}/featureOnlineStores/{feature_online_store}/featureViews/{feature_view}/featureViewSyncs/feature_view_syncB\xd2\x01\n\x1ecom.google.cloud.aiplatform.v1B\x14FeatureViewSyncProtoP\x01Z>cloud.google.com/go/aiplatform/apiv1/aiplatformpb;aiplatformpb\xaa\x02\x1aGoogle.Cloud.AIPlatform.V1\xca\x02\x1aGoogle\\Cloud\\AIPlatform\\V1\xea\x02\x1dGoogle::Cloud::Aiplatform::V1b\x06proto3')
_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'google.cloud.aiplatform.v1.feature_view_sync_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
    _globals['DESCRIPTOR']._loaded_options = None
    _globals['DESCRIPTOR']._serialized_options = b'\n\x1ecom.google.cloud.aiplatform.v1B\x14FeatureViewSyncProtoP\x01Z>cloud.google.com/go/aiplatform/apiv1/aiplatformpb;aiplatformpb\xaa\x02\x1aGoogle.Cloud.AIPlatform.V1\xca\x02\x1aGoogle\\Cloud\\AIPlatform\\V1\xea\x02\x1dGoogle::Cloud::Aiplatform::V1'
    _globals['_FEATUREVIEWSYNC_SYNCSUMMARY'].fields_by_name['row_synced']._loaded_options = None
    _globals['_FEATUREVIEWSYNC_SYNCSUMMARY'].fields_by_name['row_synced']._serialized_options = b'\xe0A\x03'
    _globals['_FEATUREVIEWSYNC_SYNCSUMMARY'].fields_by_name['total_slot']._loaded_options = None
    _globals['_FEATUREVIEWSYNC_SYNCSUMMARY'].fields_by_name['total_slot']._serialized_options = b'\xe0A\x03'
    _globals['_FEATUREVIEWSYNC'].fields_by_name['name']._loaded_options = None
    _globals['_FEATUREVIEWSYNC'].fields_by_name['name']._serialized_options = b'\xe0A\x08'
    _globals['_FEATUREVIEWSYNC'].fields_by_name['create_time']._loaded_options = None
    _globals['_FEATUREVIEWSYNC'].fields_by_name['create_time']._serialized_options = b'\xe0A\x03'
    _globals['_FEATUREVIEWSYNC'].fields_by_name['run_time']._loaded_options = None
    _globals['_FEATUREVIEWSYNC'].fields_by_name['run_time']._serialized_options = b'\xe0A\x03'
    _globals['_FEATUREVIEWSYNC'].fields_by_name['final_status']._loaded_options = None
    _globals['_FEATUREVIEWSYNC'].fields_by_name['final_status']._serialized_options = b'\xe0A\x03'
    _globals['_FEATUREVIEWSYNC'].fields_by_name['sync_summary']._loaded_options = None
    _globals['_FEATUREVIEWSYNC'].fields_by_name['sync_summary']._serialized_options = b'\xe0A\x03'
    _globals['_FEATUREVIEWSYNC'].fields_by_name['satisfies_pzs']._loaded_options = None
    _globals['_FEATUREVIEWSYNC'].fields_by_name['satisfies_pzs']._serialized_options = b'\xe0A\x03'
    _globals['_FEATUREVIEWSYNC'].fields_by_name['satisfies_pzi']._loaded_options = None
    _globals['_FEATUREVIEWSYNC'].fields_by_name['satisfies_pzi']._serialized_options = b'\xe0A\x03'
    _globals['_FEATUREVIEWSYNC']._loaded_options = None
    _globals['_FEATUREVIEWSYNC']._serialized_options = b'\xeaA\xbf\x01\n)aiplatform.googleapis.com/FeatureViewSync\x12\x91\x01projects/{project}/locations/{location}/featureOnlineStores/{feature_online_store}/featureViews/{feature_view}/featureViewSyncs/feature_view_sync'
    _globals['_FEATUREVIEWSYNC']._serialized_start = 229
    _globals['_FEATUREVIEWSYNC']._serialized_end = 874
    _globals['_FEATUREVIEWSYNC_SYNCSUMMARY']._serialized_start = 554
    _globals['_FEATUREVIEWSYNC_SYNCSUMMARY']._serialized_end = 676