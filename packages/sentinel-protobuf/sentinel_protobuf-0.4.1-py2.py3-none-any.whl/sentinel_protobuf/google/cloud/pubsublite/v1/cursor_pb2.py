"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_runtime_version.ValidateProtobufRuntimeVersion(_runtime_version.Domain.PUBLIC, 5, 28, 1, '', 'google/cloud/pubsublite/v1/cursor.proto')
_sym_db = _symbol_database.Default()
from .....google.api import annotations_pb2 as google_dot_api_dot_annotations__pb2
from .....google.api import client_pb2 as google_dot_api_dot_client__pb2
from .....google.api import field_behavior_pb2 as google_dot_api_dot_field__behavior__pb2
from .....google.api import resource_pb2 as google_dot_api_dot_resource__pb2
from .....google.cloud.pubsublite.v1 import common_pb2 as google_dot_cloud_dot_pubsublite_dot_v1_dot_common__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\'google/cloud/pubsublite/v1/cursor.proto\x12\x1agoogle.cloud.pubsublite.v1\x1a\x1cgoogle/api/annotations.proto\x1a\x17google/api/client.proto\x1a\x1fgoogle/api/field_behavior.proto\x1a\x19google/api/resource.proto\x1a\'google/cloud/pubsublite/v1/common.proto"E\n\x1aInitialCommitCursorRequest\x12\x14\n\x0csubscription\x18\x01 \x01(\t\x12\x11\n\tpartition\x18\x02 \x01(\x03"\x1d\n\x1bInitialCommitCursorResponse"R\n\x1cSequencedCommitCursorRequest\x122\n\x06cursor\x18\x01 \x01(\x0b2".google.cloud.pubsublite.v1.Cursor"=\n\x1dSequencedCommitCursorResponse\x12\x1c\n\x14acknowledged_commits\x18\x01 \x01(\x03"\xc0\x01\n\x1cStreamingCommitCursorRequest\x12I\n\x07initial\x18\x01 \x01(\x0b26.google.cloud.pubsublite.v1.InitialCommitCursorRequestH\x00\x12J\n\x06commit\x18\x02 \x01(\x0b28.google.cloud.pubsublite.v1.SequencedCommitCursorRequestH\x00B\t\n\x07request"\xc3\x01\n\x1dStreamingCommitCursorResponse\x12J\n\x07initial\x18\x01 \x01(\x0b27.google.cloud.pubsublite.v1.InitialCommitCursorResponseH\x00\x12K\n\x06commit\x18\x02 \x01(\x0b29.google.cloud.pubsublite.v1.SequencedCommitCursorResponseH\x00B\t\n\x07request"r\n\x13CommitCursorRequest\x12\x14\n\x0csubscription\x18\x01 \x01(\t\x12\x11\n\tpartition\x18\x02 \x01(\x03\x122\n\x06cursor\x18\x03 \x01(\x0b2".google.cloud.pubsublite.v1.Cursor"\x16\n\x14CommitCursorResponse"\x84\x01\n\x1bListPartitionCursorsRequest\x12>\n\x06parent\x18\x01 \x01(\tB.\xe0A\x02\xfaA(\n&pubsublite.googleapis.com/Subscription\x12\x11\n\tpage_size\x18\x02 \x01(\x05\x12\x12\n\npage_token\x18\x03 \x01(\t"X\n\x0fPartitionCursor\x12\x11\n\tpartition\x18\x01 \x01(\x03\x122\n\x06cursor\x18\x02 \x01(\x0b2".google.cloud.pubsublite.v1.Cursor"\x7f\n\x1cListPartitionCursorsResponse\x12F\n\x11partition_cursors\x18\x01 \x03(\x0b2+.google.cloud.pubsublite.v1.PartitionCursor\x12\x17\n\x0fnext_page_token\x18\x02 \x01(\t2\xa2\x05\n\rCursorService\x12\x92\x01\n\x15StreamingCommitCursor\x128.google.cloud.pubsublite.v1.StreamingCommitCursorRequest\x1a9.google.cloud.pubsublite.v1.StreamingCommitCursorResponse"\x00(\x010\x01\x12\xcb\x01\n\x0cCommitCursor\x12/.google.cloud.pubsublite.v1.CommitCursorRequest\x1a0.google.cloud.pubsublite.v1.CommitCursorResponse"X\x82\xd3\xe4\x93\x02R"M/v1/cursor/{subscription=projects/*/locations/*/subscriptions/*}:commitCursor:\x01*\x12\xde\x01\n\x14ListPartitionCursors\x127.google.cloud.pubsublite.v1.ListPartitionCursorsRequest\x1a8.google.cloud.pubsublite.v1.ListPartitionCursorsResponse"S\xdaA\x06parent\x82\xd3\xe4\x93\x02D\x12B/v1/cursor/{parent=projects/*/locations/*/subscriptions/*}/cursors\x1aM\xcaA\x19pubsublite.googleapis.com\xd2A.https://www.googleapis.com/auth/cloud-platformB\xcf\x01\n!com.google.cloud.pubsublite.protoB\x0bCursorProtoP\x01Z>cloud.google.com/go/pubsublite/apiv1/pubsublitepb;pubsublitepb\xf8\x01\x01\xaa\x02\x1aGoogle.Cloud.PubSubLite.V1\xca\x02\x1aGoogle\\Cloud\\PubSubLite\\V1\xea\x02\x1dGoogle::Cloud::PubSubLite::V1b\x06proto3')
_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'google.cloud.pubsublite.v1.cursor_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
    _globals['DESCRIPTOR']._loaded_options = None
    _globals['DESCRIPTOR']._serialized_options = b'\n!com.google.cloud.pubsublite.protoB\x0bCursorProtoP\x01Z>cloud.google.com/go/pubsublite/apiv1/pubsublitepb;pubsublitepb\xf8\x01\x01\xaa\x02\x1aGoogle.Cloud.PubSubLite.V1\xca\x02\x1aGoogle\\Cloud\\PubSubLite\\V1\xea\x02\x1dGoogle::Cloud::PubSubLite::V1'
    _globals['_LISTPARTITIONCURSORSREQUEST'].fields_by_name['parent']._loaded_options = None
    _globals['_LISTPARTITIONCURSORSREQUEST'].fields_by_name['parent']._serialized_options = b'\xe0A\x02\xfaA(\n&pubsublite.googleapis.com/Subscription'
    _globals['_CURSORSERVICE']._loaded_options = None
    _globals['_CURSORSERVICE']._serialized_options = b'\xcaA\x19pubsublite.googleapis.com\xd2A.https://www.googleapis.com/auth/cloud-platform'
    _globals['_CURSORSERVICE'].methods_by_name['CommitCursor']._loaded_options = None
    _globals['_CURSORSERVICE'].methods_by_name['CommitCursor']._serialized_options = b'\x82\xd3\xe4\x93\x02R"M/v1/cursor/{subscription=projects/*/locations/*/subscriptions/*}:commitCursor:\x01*'
    _globals['_CURSORSERVICE'].methods_by_name['ListPartitionCursors']._loaded_options = None
    _globals['_CURSORSERVICE'].methods_by_name['ListPartitionCursors']._serialized_options = b'\xdaA\x06parent\x82\xd3\xe4\x93\x02D\x12B/v1/cursor/{parent=projects/*/locations/*/subscriptions/*}/cursors'
    _globals['_INITIALCOMMITCURSORREQUEST']._serialized_start = 227
    _globals['_INITIALCOMMITCURSORREQUEST']._serialized_end = 296
    _globals['_INITIALCOMMITCURSORRESPONSE']._serialized_start = 298
    _globals['_INITIALCOMMITCURSORRESPONSE']._serialized_end = 327
    _globals['_SEQUENCEDCOMMITCURSORREQUEST']._serialized_start = 329
    _globals['_SEQUENCEDCOMMITCURSORREQUEST']._serialized_end = 411
    _globals['_SEQUENCEDCOMMITCURSORRESPONSE']._serialized_start = 413
    _globals['_SEQUENCEDCOMMITCURSORRESPONSE']._serialized_end = 474
    _globals['_STREAMINGCOMMITCURSORREQUEST']._serialized_start = 477
    _globals['_STREAMINGCOMMITCURSORREQUEST']._serialized_end = 669
    _globals['_STREAMINGCOMMITCURSORRESPONSE']._serialized_start = 672
    _globals['_STREAMINGCOMMITCURSORRESPONSE']._serialized_end = 867
    _globals['_COMMITCURSORREQUEST']._serialized_start = 869
    _globals['_COMMITCURSORREQUEST']._serialized_end = 983
    _globals['_COMMITCURSORRESPONSE']._serialized_start = 985
    _globals['_COMMITCURSORRESPONSE']._serialized_end = 1007
    _globals['_LISTPARTITIONCURSORSREQUEST']._serialized_start = 1010
    _globals['_LISTPARTITIONCURSORSREQUEST']._serialized_end = 1142
    _globals['_PARTITIONCURSOR']._serialized_start = 1144
    _globals['_PARTITIONCURSOR']._serialized_end = 1232
    _globals['_LISTPARTITIONCURSORSRESPONSE']._serialized_start = 1234
    _globals['_LISTPARTITIONCURSORSRESPONSE']._serialized_end = 1361
    _globals['_CURSORSERVICE']._serialized_start = 1364
    _globals['_CURSORSERVICE']._serialized_end = 2038