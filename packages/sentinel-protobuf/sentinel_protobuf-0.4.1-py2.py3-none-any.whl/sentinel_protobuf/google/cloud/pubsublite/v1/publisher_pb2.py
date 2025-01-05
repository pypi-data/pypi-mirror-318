"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_runtime_version.ValidateProtobufRuntimeVersion(_runtime_version.Domain.PUBLIC, 5, 28, 1, '', 'google/cloud/pubsublite/v1/publisher.proto')
_sym_db = _symbol_database.Default()
from .....google.api import annotations_pb2 as google_dot_api_dot_annotations__pb2
from .....google.api import client_pb2 as google_dot_api_dot_client__pb2
from .....google.cloud.pubsublite.v1 import common_pb2 as google_dot_cloud_dot_pubsublite_dot_v1_dot_common__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n*google/cloud/pubsublite/v1/publisher.proto\x12\x1agoogle.cloud.pubsublite.v1\x1a\x1cgoogle/api/annotations.proto\x1a\x17google/api/client.proto\x1a\'google/cloud/pubsublite/v1/common.proto"L\n\x15InitialPublishRequest\x12\r\n\x05topic\x18\x01 \x01(\t\x12\x11\n\tpartition\x18\x02 \x01(\x03\x12\x11\n\tclient_id\x18\x03 \x01(\x0c"\x18\n\x16InitialPublishResponse"s\n\x15MessagePublishRequest\x12;\n\x08messages\x18\x01 \x03(\x0b2).google.cloud.pubsublite.v1.PubSubMessage\x12\x1d\n\x15first_sequence_number\x18\x02 \x01(\x03"\x9a\x02\n\x16MessagePublishResponse\x128\n\x0cstart_cursor\x18\x01 \x01(\x0b2".google.cloud.pubsublite.v1.Cursor\x12U\n\rcursor_ranges\x18\x02 \x03(\x0b2>.google.cloud.pubsublite.v1.MessagePublishResponse.CursorRange\x1ao\n\x0bCursorRange\x128\n\x0cstart_cursor\x18\x01 \x01(\x0b2".google.cloud.pubsublite.v1.Cursor\x12\x13\n\x0bstart_index\x18\x02 \x01(\x05\x12\x11\n\tend_index\x18\x03 \x01(\x05"\xc4\x01\n\x0ePublishRequest\x12L\n\x0finitial_request\x18\x01 \x01(\x0b21.google.cloud.pubsublite.v1.InitialPublishRequestH\x00\x12T\n\x17message_publish_request\x18\x02 \x01(\x0b21.google.cloud.pubsublite.v1.MessagePublishRequestH\x00B\x0e\n\x0crequest_type"\xc2\x01\n\x0fPublishResponse\x12N\n\x10initial_response\x18\x01 \x01(\x0b22.google.cloud.pubsublite.v1.InitialPublishResponseH\x00\x12N\n\x10message_response\x18\x02 \x01(\x0b22.google.cloud.pubsublite.v1.MessagePublishResponseH\x00B\x0f\n\rresponse_type2\xcb\x01\n\x10PublisherService\x12h\n\x07Publish\x12*.google.cloud.pubsublite.v1.PublishRequest\x1a+.google.cloud.pubsublite.v1.PublishResponse"\x00(\x010\x01\x1aM\xcaA\x19pubsublite.googleapis.com\xd2A.https://www.googleapis.com/auth/cloud-platformB\xd2\x01\n!com.google.cloud.pubsublite.protoB\x0ePublisherProtoP\x01Z>cloud.google.com/go/pubsublite/apiv1/pubsublitepb;pubsublitepb\xf8\x01\x01\xaa\x02\x1aGoogle.Cloud.PubSubLite.V1\xca\x02\x1aGoogle\\Cloud\\PubSubLite\\V1\xea\x02\x1dGoogle::Cloud::PubSubLite::V1b\x06proto3')
_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'google.cloud.pubsublite.v1.publisher_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
    _globals['DESCRIPTOR']._loaded_options = None
    _globals['DESCRIPTOR']._serialized_options = b'\n!com.google.cloud.pubsublite.protoB\x0ePublisherProtoP\x01Z>cloud.google.com/go/pubsublite/apiv1/pubsublitepb;pubsublitepb\xf8\x01\x01\xaa\x02\x1aGoogle.Cloud.PubSubLite.V1\xca\x02\x1aGoogle\\Cloud\\PubSubLite\\V1\xea\x02\x1dGoogle::Cloud::PubSubLite::V1'
    _globals['_PUBLISHERSERVICE']._loaded_options = None
    _globals['_PUBLISHERSERVICE']._serialized_options = b'\xcaA\x19pubsublite.googleapis.com\xd2A.https://www.googleapis.com/auth/cloud-platform'
    _globals['_INITIALPUBLISHREQUEST']._serialized_start = 170
    _globals['_INITIALPUBLISHREQUEST']._serialized_end = 246
    _globals['_INITIALPUBLISHRESPONSE']._serialized_start = 248
    _globals['_INITIALPUBLISHRESPONSE']._serialized_end = 272
    _globals['_MESSAGEPUBLISHREQUEST']._serialized_start = 274
    _globals['_MESSAGEPUBLISHREQUEST']._serialized_end = 389
    _globals['_MESSAGEPUBLISHRESPONSE']._serialized_start = 392
    _globals['_MESSAGEPUBLISHRESPONSE']._serialized_end = 674
    _globals['_MESSAGEPUBLISHRESPONSE_CURSORRANGE']._serialized_start = 563
    _globals['_MESSAGEPUBLISHRESPONSE_CURSORRANGE']._serialized_end = 674
    _globals['_PUBLISHREQUEST']._serialized_start = 677
    _globals['_PUBLISHREQUEST']._serialized_end = 873
    _globals['_PUBLISHRESPONSE']._serialized_start = 876
    _globals['_PUBLISHRESPONSE']._serialized_end = 1070
    _globals['_PUBLISHERSERVICE']._serialized_start = 1073
    _globals['_PUBLISHERSERVICE']._serialized_end = 1276