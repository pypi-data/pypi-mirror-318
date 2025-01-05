"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_runtime_version.ValidateProtobufRuntimeVersion(_runtime_version.Domain.PUBLIC, 5, 28, 1, '', 'google/cloud/recommender/logging/v1beta1/action_log.proto')
_sym_db = _symbol_database.Default()
from ......google.api import field_behavior_pb2 as google_dot_api_dot_field__behavior__pb2
from ......google.cloud.recommender.v1beta1 import insight_pb2 as google_dot_cloud_dot_recommender_dot_v1beta1_dot_insight__pb2
from ......google.cloud.recommender.v1beta1 import recommendation_pb2 as google_dot_cloud_dot_recommender_dot_v1beta1_dot_recommendation__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n9google/cloud/recommender/logging/v1beta1/action_log.proto\x12(google.cloud.recommender.logging.v1beta1\x1a\x1fgoogle/api/field_behavior.proto\x1a.google/cloud/recommender/v1beta1/insight.proto\x1a5google/cloud/recommender/v1beta1/recommendation.proto"\x9d\x02\n\tActionLog\x12\r\n\x05actor\x18\x01 \x01(\t\x12N\n\x05state\x18\x02 \x01(\x0e2?.google.cloud.recommender.v1beta1.RecommendationStateInfo.State\x12^\n\x0estate_metadata\x18\x03 \x03(\x0b2F.google.cloud.recommender.logging.v1beta1.ActionLog.StateMetadataEntry\x12\x1b\n\x13recommendation_name\x18\x04 \x01(\t\x1a4\n\x12StateMetadataEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\r\n\x05value\x18\x02 \x01(\t:\x028\x01"\xac\x02\n\x10InsightActionLog\x12\x12\n\x05actor\x18\x01 \x01(\tB\x03\xe0A\x02\x12L\n\x05state\x18\x02 \x01(\x0e28.google.cloud.recommender.v1beta1.InsightStateInfo.StateB\x03\xe0A\x02\x12j\n\x0estate_metadata\x18\x03 \x03(\x0b2M.google.cloud.recommender.logging.v1beta1.InsightActionLog.StateMetadataEntryB\x03\xe0A\x01\x12\x14\n\x07insight\x18\x04 \x01(\tB\x03\xe0A\x02\x1a4\n\x12StateMetadataEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\r\n\x05value\x18\x02 \x01(\t:\x028\x01B\x88\x01\n,com.google.cloud.recommender.logging.v1beta1B\x0eActionLogProtoP\x01ZFcloud.google.com/go/recommender/logging/apiv1beta1/loggingpb;loggingpbb\x06proto3')
_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'google.cloud.recommender.logging.v1beta1.action_log_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
    _globals['DESCRIPTOR']._loaded_options = None
    _globals['DESCRIPTOR']._serialized_options = b'\n,com.google.cloud.recommender.logging.v1beta1B\x0eActionLogProtoP\x01ZFcloud.google.com/go/recommender/logging/apiv1beta1/loggingpb;loggingpb'
    _globals['_ACTIONLOG_STATEMETADATAENTRY']._loaded_options = None
    _globals['_ACTIONLOG_STATEMETADATAENTRY']._serialized_options = b'8\x01'
    _globals['_INSIGHTACTIONLOG_STATEMETADATAENTRY']._loaded_options = None
    _globals['_INSIGHTACTIONLOG_STATEMETADATAENTRY']._serialized_options = b'8\x01'
    _globals['_INSIGHTACTIONLOG'].fields_by_name['actor']._loaded_options = None
    _globals['_INSIGHTACTIONLOG'].fields_by_name['actor']._serialized_options = b'\xe0A\x02'
    _globals['_INSIGHTACTIONLOG'].fields_by_name['state']._loaded_options = None
    _globals['_INSIGHTACTIONLOG'].fields_by_name['state']._serialized_options = b'\xe0A\x02'
    _globals['_INSIGHTACTIONLOG'].fields_by_name['state_metadata']._loaded_options = None
    _globals['_INSIGHTACTIONLOG'].fields_by_name['state_metadata']._serialized_options = b'\xe0A\x01'
    _globals['_INSIGHTACTIONLOG'].fields_by_name['insight']._loaded_options = None
    _globals['_INSIGHTACTIONLOG'].fields_by_name['insight']._serialized_options = b'\xe0A\x02'
    _globals['_ACTIONLOG']._serialized_start = 240
    _globals['_ACTIONLOG']._serialized_end = 525
    _globals['_ACTIONLOG_STATEMETADATAENTRY']._serialized_start = 473
    _globals['_ACTIONLOG_STATEMETADATAENTRY']._serialized_end = 525
    _globals['_INSIGHTACTIONLOG']._serialized_start = 528
    _globals['_INSIGHTACTIONLOG']._serialized_end = 828
    _globals['_INSIGHTACTIONLOG_STATEMETADATAENTRY']._serialized_start = 473
    _globals['_INSIGHTACTIONLOG_STATEMETADATAENTRY']._serialized_end = 525