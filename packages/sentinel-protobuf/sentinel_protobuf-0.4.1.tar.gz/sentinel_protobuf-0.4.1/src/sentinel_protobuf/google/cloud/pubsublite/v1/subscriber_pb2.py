"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_runtime_version.ValidateProtobufRuntimeVersion(_runtime_version.Domain.PUBLIC, 5, 28, 1, '', 'google/cloud/pubsublite/v1/subscriber.proto')
_sym_db = _symbol_database.Default()
from .....google.api import annotations_pb2 as google_dot_api_dot_annotations__pb2
from .....google.api import client_pb2 as google_dot_api_dot_client__pb2
from .....google.api import field_behavior_pb2 as google_dot_api_dot_field__behavior__pb2
from .....google.cloud.pubsublite.v1 import common_pb2 as google_dot_cloud_dot_pubsublite_dot_v1_dot_common__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n+google/cloud/pubsublite/v1/subscriber.proto\x12\x1agoogle.cloud.pubsublite.v1\x1a\x1cgoogle/api/annotations.proto\x1a\x17google/api/client.proto\x1a\x1fgoogle/api/field_behavior.proto\x1a\'google/cloud/pubsublite/v1/common.proto"\x8a\x01\n\x17InitialSubscribeRequest\x12\x14\n\x0csubscription\x18\x01 \x01(\t\x12\x11\n\tpartition\x18\x02 \x01(\x03\x12F\n\x10initial_location\x18\x04 \x01(\x0b2\'.google.cloud.pubsublite.v1.SeekRequestB\x03\xe0A\x01"N\n\x18InitialSubscribeResponse\x122\n\x06cursor\x18\x01 \x01(\x0b2".google.cloud.pubsublite.v1.Cursor"\xe7\x01\n\x0bSeekRequest\x12K\n\x0cnamed_target\x18\x01 \x01(\x0e23.google.cloud.pubsublite.v1.SeekRequest.NamedTargetH\x00\x124\n\x06cursor\x18\x02 \x01(\x0b2".google.cloud.pubsublite.v1.CursorH\x00"K\n\x0bNamedTarget\x12\x1c\n\x18NAMED_TARGET_UNSPECIFIED\x10\x00\x12\x08\n\x04HEAD\x10\x01\x12\x14\n\x10COMMITTED_CURSOR\x10\x02B\x08\n\x06target"B\n\x0cSeekResponse\x122\n\x06cursor\x18\x01 \x01(\x0b2".google.cloud.pubsublite.v1.Cursor"E\n\x12FlowControlRequest\x12\x18\n\x10allowed_messages\x18\x01 \x01(\x03\x12\x15\n\rallowed_bytes\x18\x02 \x01(\x03"\xe6\x01\n\x10SubscribeRequest\x12F\n\x07initial\x18\x01 \x01(\x0b23.google.cloud.pubsublite.v1.InitialSubscribeRequestH\x00\x127\n\x04seek\x18\x02 \x01(\x0b2\'.google.cloud.pubsublite.v1.SeekRequestH\x00\x12F\n\x0cflow_control\x18\x03 \x01(\x0b2..google.cloud.pubsublite.v1.FlowControlRequestH\x00B\t\n\x07request"Q\n\x0fMessageResponse\x12>\n\x08messages\x18\x01 \x03(\x0b2,.google.cloud.pubsublite.v1.SequencedMessage"\xe3\x01\n\x11SubscribeResponse\x12G\n\x07initial\x18\x01 \x01(\x0b24.google.cloud.pubsublite.v1.InitialSubscribeResponseH\x00\x128\n\x04seek\x18\x02 \x01(\x0b2(.google.cloud.pubsublite.v1.SeekResponseH\x00\x12?\n\x08messages\x18\x03 \x01(\x0b2+.google.cloud.pubsublite.v1.MessageResponseH\x00B\n\n\x08response"L\n!InitialPartitionAssignmentRequest\x12\x14\n\x0csubscription\x18\x01 \x01(\t\x12\x11\n\tclient_id\x18\x02 \x01(\x0c")\n\x13PartitionAssignment\x12\x12\n\npartitions\x18\x01 \x03(\x03"\x18\n\x16PartitionAssignmentAck"\xbc\x01\n\x1aPartitionAssignmentRequest\x12P\n\x07initial\x18\x01 \x01(\x0b2=.google.cloud.pubsublite.v1.InitialPartitionAssignmentRequestH\x00\x12A\n\x03ack\x18\x02 \x01(\x0b22.google.cloud.pubsublite.v1.PartitionAssignmentAckH\x00B\t\n\x07request2\xd2\x01\n\x11SubscriberService\x12n\n\tSubscribe\x12,.google.cloud.pubsublite.v1.SubscribeRequest\x1a-.google.cloud.pubsublite.v1.SubscribeResponse"\x00(\x010\x01\x1aM\xcaA\x19pubsublite.googleapis.com\xd2A.https://www.googleapis.com/auth/cloud-platform2\xef\x01\n\x1aPartitionAssignmentService\x12\x81\x01\n\x10AssignPartitions\x126.google.cloud.pubsublite.v1.PartitionAssignmentRequest\x1a/.google.cloud.pubsublite.v1.PartitionAssignment"\x00(\x010\x01\x1aM\xcaA\x19pubsublite.googleapis.com\xd2A.https://www.googleapis.com/auth/cloud-platformB\xd3\x01\n!com.google.cloud.pubsublite.protoB\x0fSubscriberProtoP\x01Z>cloud.google.com/go/pubsublite/apiv1/pubsublitepb;pubsublitepb\xf8\x01\x01\xaa\x02\x1aGoogle.Cloud.PubSubLite.V1\xca\x02\x1aGoogle\\Cloud\\PubSubLite\\V1\xea\x02\x1dGoogle::Cloud::PubSubLite::V1b\x06proto3')
_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'google.cloud.pubsublite.v1.subscriber_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
    _globals['DESCRIPTOR']._loaded_options = None
    _globals['DESCRIPTOR']._serialized_options = b'\n!com.google.cloud.pubsublite.protoB\x0fSubscriberProtoP\x01Z>cloud.google.com/go/pubsublite/apiv1/pubsublitepb;pubsublitepb\xf8\x01\x01\xaa\x02\x1aGoogle.Cloud.PubSubLite.V1\xca\x02\x1aGoogle\\Cloud\\PubSubLite\\V1\xea\x02\x1dGoogle::Cloud::PubSubLite::V1'
    _globals['_INITIALSUBSCRIBEREQUEST'].fields_by_name['initial_location']._loaded_options = None
    _globals['_INITIALSUBSCRIBEREQUEST'].fields_by_name['initial_location']._serialized_options = b'\xe0A\x01'
    _globals['_SUBSCRIBERSERVICE']._loaded_options = None
    _globals['_SUBSCRIBERSERVICE']._serialized_options = b'\xcaA\x19pubsublite.googleapis.com\xd2A.https://www.googleapis.com/auth/cloud-platform'
    _globals['_PARTITIONASSIGNMENTSERVICE']._loaded_options = None
    _globals['_PARTITIONASSIGNMENTSERVICE']._serialized_options = b'\xcaA\x19pubsublite.googleapis.com\xd2A.https://www.googleapis.com/auth/cloud-platform'
    _globals['_INITIALSUBSCRIBEREQUEST']._serialized_start = 205
    _globals['_INITIALSUBSCRIBEREQUEST']._serialized_end = 343
    _globals['_INITIALSUBSCRIBERESPONSE']._serialized_start = 345
    _globals['_INITIALSUBSCRIBERESPONSE']._serialized_end = 423
    _globals['_SEEKREQUEST']._serialized_start = 426
    _globals['_SEEKREQUEST']._serialized_end = 657
    _globals['_SEEKREQUEST_NAMEDTARGET']._serialized_start = 572
    _globals['_SEEKREQUEST_NAMEDTARGET']._serialized_end = 647
    _globals['_SEEKRESPONSE']._serialized_start = 659
    _globals['_SEEKRESPONSE']._serialized_end = 725
    _globals['_FLOWCONTROLREQUEST']._serialized_start = 727
    _globals['_FLOWCONTROLREQUEST']._serialized_end = 796
    _globals['_SUBSCRIBEREQUEST']._serialized_start = 799
    _globals['_SUBSCRIBEREQUEST']._serialized_end = 1029
    _globals['_MESSAGERESPONSE']._serialized_start = 1031
    _globals['_MESSAGERESPONSE']._serialized_end = 1112
    _globals['_SUBSCRIBERESPONSE']._serialized_start = 1115
    _globals['_SUBSCRIBERESPONSE']._serialized_end = 1342
    _globals['_INITIALPARTITIONASSIGNMENTREQUEST']._serialized_start = 1344
    _globals['_INITIALPARTITIONASSIGNMENTREQUEST']._serialized_end = 1420
    _globals['_PARTITIONASSIGNMENT']._serialized_start = 1422
    _globals['_PARTITIONASSIGNMENT']._serialized_end = 1463
    _globals['_PARTITIONASSIGNMENTACK']._serialized_start = 1465
    _globals['_PARTITIONASSIGNMENTACK']._serialized_end = 1489
    _globals['_PARTITIONASSIGNMENTREQUEST']._serialized_start = 1492
    _globals['_PARTITIONASSIGNMENTREQUEST']._serialized_end = 1680
    _globals['_SUBSCRIBERSERVICE']._serialized_start = 1683
    _globals['_SUBSCRIBERSERVICE']._serialized_end = 1893
    _globals['_PARTITIONASSIGNMENTSERVICE']._serialized_start = 1896
    _globals['_PARTITIONASSIGNMENTSERVICE']._serialized_end = 2135