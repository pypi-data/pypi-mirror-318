"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_runtime_version.ValidateProtobufRuntimeVersion(_runtime_version.Domain.PUBLIC, 5, 28, 1, '', 'google/cloud/pubsublite/v1/topic_stats.proto')
_sym_db = _symbol_database.Default()
from .....google.api import annotations_pb2 as google_dot_api_dot_annotations__pb2
from .....google.api import client_pb2 as google_dot_api_dot_client__pb2
from .....google.api import field_behavior_pb2 as google_dot_api_dot_field__behavior__pb2
from .....google.api import resource_pb2 as google_dot_api_dot_resource__pb2
from .....google.cloud.pubsublite.v1 import common_pb2 as google_dot_cloud_dot_pubsublite_dot_v1_dot_common__pb2
from google.protobuf import timestamp_pb2 as google_dot_protobuf_dot_timestamp__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n,google/cloud/pubsublite/v1/topic_stats.proto\x12\x1agoogle.cloud.pubsublite.v1\x1a\x1cgoogle/api/annotations.proto\x1a\x17google/api/client.proto\x1a\x1fgoogle/api/field_behavior.proto\x1a\x19google/api/resource.proto\x1a\'google/cloud/pubsublite/v1/common.proto\x1a\x1fgoogle/protobuf/timestamp.proto"\xde\x01\n\x1aComputeMessageStatsRequest\x126\n\x05topic\x18\x01 \x01(\tB\'\xe0A\x02\xfaA!\n\x1fpubsublite.googleapis.com/Topic\x12\x16\n\tpartition\x18\x02 \x01(\x03B\x03\xe0A\x02\x128\n\x0cstart_cursor\x18\x03 \x01(\x0b2".google.cloud.pubsublite.v1.Cursor\x126\n\nend_cursor\x18\x04 \x01(\x0b2".google.cloud.pubsublite.v1.Cursor"\xbd\x01\n\x1bComputeMessageStatsResponse\x12\x15\n\rmessage_count\x18\x01 \x01(\x03\x12\x15\n\rmessage_bytes\x18\x02 \x01(\x03\x128\n\x14minimum_publish_time\x18\x03 \x01(\x0b2\x1a.google.protobuf.Timestamp\x126\n\x12minimum_event_time\x18\x04 \x01(\x0b2\x1a.google.protobuf.Timestamp"j\n\x18ComputeHeadCursorRequest\x126\n\x05topic\x18\x01 \x01(\tB\'\xe0A\x02\xfaA!\n\x1fpubsublite.googleapis.com/Topic\x12\x16\n\tpartition\x18\x02 \x01(\x03B\x03\xe0A\x02"T\n\x19ComputeHeadCursorResponse\x127\n\x0bhead_cursor\x18\x01 \x01(\x0b2".google.cloud.pubsublite.v1.Cursor"\xa7\x01\n\x18ComputeTimeCursorRequest\x126\n\x05topic\x18\x01 \x01(\tB\'\xe0A\x02\xfaA!\n\x1fpubsublite.googleapis.com/Topic\x12\x16\n\tpartition\x18\x02 \x01(\x03B\x03\xe0A\x02\x12;\n\x06target\x18\x03 \x01(\x0b2&.google.cloud.pubsublite.v1.TimeTargetB\x03\xe0A\x02"O\n\x19ComputeTimeCursorResponse\x122\n\x06cursor\x18\x01 \x01(\x0b2".google.cloud.pubsublite.v1.Cursor2\xf2\x05\n\x11TopicStatsService\x12\xdd\x01\n\x13ComputeMessageStats\x126.google.cloud.pubsublite.v1.ComputeMessageStatsRequest\x1a7.google.cloud.pubsublite.v1.ComputeMessageStatsResponse"U\x82\xd3\xe4\x93\x02O"J/v1/topicStats/{topic=projects/*/locations/*/topics/*}:computeMessageStats:\x01*\x12\xd5\x01\n\x11ComputeHeadCursor\x124.google.cloud.pubsublite.v1.ComputeHeadCursorRequest\x1a5.google.cloud.pubsublite.v1.ComputeHeadCursorResponse"S\x82\xd3\xe4\x93\x02M"H/v1/topicStats/{topic=projects/*/locations/*/topics/*}:computeHeadCursor:\x01*\x12\xd5\x01\n\x11ComputeTimeCursor\x124.google.cloud.pubsublite.v1.ComputeTimeCursorRequest\x1a5.google.cloud.pubsublite.v1.ComputeTimeCursorResponse"S\x82\xd3\xe4\x93\x02M"H/v1/topicStats/{topic=projects/*/locations/*/topics/*}:computeTimeCursor:\x01*\x1aM\xcaA\x19pubsublite.googleapis.com\xd2A.https://www.googleapis.com/auth/cloud-platformB\xd0\x01\n!com.google.cloud.pubsublite.protoB\x0fTopicStatsProtoP\x01Z>cloud.google.com/go/pubsublite/apiv1/pubsublitepb;pubsublitepb\xaa\x02\x1aGoogle.Cloud.PubSubLite.V1\xca\x02\x1aGoogle\\Cloud\\PubSubLite\\V1\xea\x02\x1dGoogle::Cloud::PubSubLite::V1b\x06proto3')
_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'google.cloud.pubsublite.v1.topic_stats_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
    _globals['DESCRIPTOR']._loaded_options = None
    _globals['DESCRIPTOR']._serialized_options = b'\n!com.google.cloud.pubsublite.protoB\x0fTopicStatsProtoP\x01Z>cloud.google.com/go/pubsublite/apiv1/pubsublitepb;pubsublitepb\xaa\x02\x1aGoogle.Cloud.PubSubLite.V1\xca\x02\x1aGoogle\\Cloud\\PubSubLite\\V1\xea\x02\x1dGoogle::Cloud::PubSubLite::V1'
    _globals['_COMPUTEMESSAGESTATSREQUEST'].fields_by_name['topic']._loaded_options = None
    _globals['_COMPUTEMESSAGESTATSREQUEST'].fields_by_name['topic']._serialized_options = b'\xe0A\x02\xfaA!\n\x1fpubsublite.googleapis.com/Topic'
    _globals['_COMPUTEMESSAGESTATSREQUEST'].fields_by_name['partition']._loaded_options = None
    _globals['_COMPUTEMESSAGESTATSREQUEST'].fields_by_name['partition']._serialized_options = b'\xe0A\x02'
    _globals['_COMPUTEHEADCURSORREQUEST'].fields_by_name['topic']._loaded_options = None
    _globals['_COMPUTEHEADCURSORREQUEST'].fields_by_name['topic']._serialized_options = b'\xe0A\x02\xfaA!\n\x1fpubsublite.googleapis.com/Topic'
    _globals['_COMPUTEHEADCURSORREQUEST'].fields_by_name['partition']._loaded_options = None
    _globals['_COMPUTEHEADCURSORREQUEST'].fields_by_name['partition']._serialized_options = b'\xe0A\x02'
    _globals['_COMPUTETIMECURSORREQUEST'].fields_by_name['topic']._loaded_options = None
    _globals['_COMPUTETIMECURSORREQUEST'].fields_by_name['topic']._serialized_options = b'\xe0A\x02\xfaA!\n\x1fpubsublite.googleapis.com/Topic'
    _globals['_COMPUTETIMECURSORREQUEST'].fields_by_name['partition']._loaded_options = None
    _globals['_COMPUTETIMECURSORREQUEST'].fields_by_name['partition']._serialized_options = b'\xe0A\x02'
    _globals['_COMPUTETIMECURSORREQUEST'].fields_by_name['target']._loaded_options = None
    _globals['_COMPUTETIMECURSORREQUEST'].fields_by_name['target']._serialized_options = b'\xe0A\x02'
    _globals['_TOPICSTATSSERVICE']._loaded_options = None
    _globals['_TOPICSTATSSERVICE']._serialized_options = b'\xcaA\x19pubsublite.googleapis.com\xd2A.https://www.googleapis.com/auth/cloud-platform'
    _globals['_TOPICSTATSSERVICE'].methods_by_name['ComputeMessageStats']._loaded_options = None
    _globals['_TOPICSTATSSERVICE'].methods_by_name['ComputeMessageStats']._serialized_options = b'\x82\xd3\xe4\x93\x02O"J/v1/topicStats/{topic=projects/*/locations/*/topics/*}:computeMessageStats:\x01*'
    _globals['_TOPICSTATSSERVICE'].methods_by_name['ComputeHeadCursor']._loaded_options = None
    _globals['_TOPICSTATSSERVICE'].methods_by_name['ComputeHeadCursor']._serialized_options = b'\x82\xd3\xe4\x93\x02M"H/v1/topicStats/{topic=projects/*/locations/*/topics/*}:computeHeadCursor:\x01*'
    _globals['_TOPICSTATSSERVICE'].methods_by_name['ComputeTimeCursor']._loaded_options = None
    _globals['_TOPICSTATSSERVICE'].methods_by_name['ComputeTimeCursor']._serialized_options = b'\x82\xd3\xe4\x93\x02M"H/v1/topicStats/{topic=projects/*/locations/*/topics/*}:computeTimeCursor:\x01*'
    _globals['_COMPUTEMESSAGESTATSREQUEST']._serialized_start = 266
    _globals['_COMPUTEMESSAGESTATSREQUEST']._serialized_end = 488
    _globals['_COMPUTEMESSAGESTATSRESPONSE']._serialized_start = 491
    _globals['_COMPUTEMESSAGESTATSRESPONSE']._serialized_end = 680
    _globals['_COMPUTEHEADCURSORREQUEST']._serialized_start = 682
    _globals['_COMPUTEHEADCURSORREQUEST']._serialized_end = 788
    _globals['_COMPUTEHEADCURSORRESPONSE']._serialized_start = 790
    _globals['_COMPUTEHEADCURSORRESPONSE']._serialized_end = 874
    _globals['_COMPUTETIMECURSORREQUEST']._serialized_start = 877
    _globals['_COMPUTETIMECURSORREQUEST']._serialized_end = 1044
    _globals['_COMPUTETIMECURSORRESPONSE']._serialized_start = 1046
    _globals['_COMPUTETIMECURSORRESPONSE']._serialized_end = 1125
    _globals['_TOPICSTATSSERVICE']._serialized_start = 1128
    _globals['_TOPICSTATSSERVICE']._serialized_end = 1882