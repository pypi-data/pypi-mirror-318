"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_runtime_version.ValidateProtobufRuntimeVersion(_runtime_version.Domain.PUBLIC, 5, 28, 1, '', 'google/cloud/eventarc/publishing/v1/publisher.proto')
_sym_db = _symbol_database.Default()
from ......google.api import annotations_pb2 as google_dot_api_dot_annotations__pb2
from ......google.api import client_pb2 as google_dot_api_dot_client__pb2
from ......google.api import field_behavior_pb2 as google_dot_api_dot_field__behavior__pb2
from ......google.api import field_info_pb2 as google_dot_api_dot_field__info__pb2
from ......google.cloud.eventarc.publishing.v1 import cloud_event_pb2 as google_dot_cloud_dot_eventarc_dot_publishing_dot_v1_dot_cloud__event__pb2
from google.protobuf import any_pb2 as google_dot_protobuf_dot_any__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n3google/cloud/eventarc/publishing/v1/publisher.proto\x12#google.cloud.eventarc.publishing.v1\x1a\x1cgoogle/api/annotations.proto\x1a\x17google/api/client.proto\x1a\x1fgoogle/api/field_behavior.proto\x1a\x1bgoogle/api/field_info.proto\x1a5google/cloud/eventarc/publishing/v1/cloud_event.proto\x1a\x19google/protobuf/any.proto"~\n%PublishChannelConnectionEventsRequest\x12\x1a\n\x12channel_connection\x18\x01 \x01(\t\x12$\n\x06events\x18\x02 \x03(\x0b2\x14.google.protobuf.Any\x12\x13\n\x0btext_events\x18\x03 \x03(\t"(\n&PublishChannelConnectionEventsResponse"b\n\x14PublishEventsRequest\x12\x0f\n\x07channel\x18\x01 \x01(\t\x12$\n\x06events\x18\x02 \x03(\x0b2\x14.google.protobuf.Any\x12\x13\n\x0btext_events\x18\x03 \x03(\t"\x17\n\x15PublishEventsResponse"\xae\x01\n\x0ePublishRequest\x12\x18\n\x0bmessage_bus\x18\x01 \x01(\tB\x03\xe0A\x02\x12H\n\rproto_message\x18\x02 \x01(\x0b2/.google.cloud.eventarc.publishing.v1.CloudEventH\x00\x12\x16\n\x0cjson_message\x18\x03 \x01(\tH\x00\x12\x16\n\x0cavro_message\x18\x04 \x01(\x0cH\x00B\x08\n\x06format"\x11\n\x0fPublishResponse2\x93\x06\n\tPublisher\x12\x98\x02\n\x1ePublishChannelConnectionEvents\x12J.google.cloud.eventarc.publishing.v1.PublishChannelConnectionEventsRequest\x1aK.google.cloud.eventarc.publishing.v1.PublishChannelConnectionEventsResponse"]\x82\xd3\xe4\x93\x02W"R/v1/{channel_connection=projects/*/locations/*/channelConnections/*}:publishEvents:\x01*\x12\xd0\x01\n\rPublishEvents\x129.google.cloud.eventarc.publishing.v1.PublishEventsRequest\x1a:.google.cloud.eventarc.publishing.v1.PublishEventsResponse"H\x82\xd3\xe4\x93\x02B"=/v1/{channel=projects/*/locations/*/channels/*}:publishEvents:\x01*\x12\xc0\x01\n\x07Publish\x123.google.cloud.eventarc.publishing.v1.PublishRequest\x1a4.google.cloud.eventarc.publishing.v1.PublishResponse"J\x82\xd3\xe4\x93\x02D"?/v1/{message_bus=projects/*/locations/*/messageBuses/*}:publish:\x01*\x1aU\xcaA!eventarcpublishing.googleapis.com\xd2A.https://www.googleapis.com/auth/cloud-platformB\xfa\x01\n\'com.google.cloud.eventarc.publishing.v1B\x0ePublisherProtoP\x01ZGcloud.google.com/go/eventarc/publishing/apiv1/publishingpb;publishingpb\xaa\x02#Google.Cloud.Eventarc.Publishing.V1\xca\x02#Google\\Cloud\\Eventarc\\Publishing\\V1\xea\x02\'Google::Cloud::Eventarc::Publishing::V1b\x06proto3')
_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'google.cloud.eventarc.publishing.v1.publisher_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
    _globals['DESCRIPTOR']._loaded_options = None
    _globals['DESCRIPTOR']._serialized_options = b"\n'com.google.cloud.eventarc.publishing.v1B\x0ePublisherProtoP\x01ZGcloud.google.com/go/eventarc/publishing/apiv1/publishingpb;publishingpb\xaa\x02#Google.Cloud.Eventarc.Publishing.V1\xca\x02#Google\\Cloud\\Eventarc\\Publishing\\V1\xea\x02'Google::Cloud::Eventarc::Publishing::V1"
    _globals['_PUBLISHREQUEST'].fields_by_name['message_bus']._loaded_options = None
    _globals['_PUBLISHREQUEST'].fields_by_name['message_bus']._serialized_options = b'\xe0A\x02'
    _globals['_PUBLISHER']._loaded_options = None
    _globals['_PUBLISHER']._serialized_options = b'\xcaA!eventarcpublishing.googleapis.com\xd2A.https://www.googleapis.com/auth/cloud-platform'
    _globals['_PUBLISHER'].methods_by_name['PublishChannelConnectionEvents']._loaded_options = None
    _globals['_PUBLISHER'].methods_by_name['PublishChannelConnectionEvents']._serialized_options = b'\x82\xd3\xe4\x93\x02W"R/v1/{channel_connection=projects/*/locations/*/channelConnections/*}:publishEvents:\x01*'
    _globals['_PUBLISHER'].methods_by_name['PublishEvents']._loaded_options = None
    _globals['_PUBLISHER'].methods_by_name['PublishEvents']._serialized_options = b'\x82\xd3\xe4\x93\x02B"=/v1/{channel=projects/*/locations/*/channels/*}:publishEvents:\x01*'
    _globals['_PUBLISHER'].methods_by_name['Publish']._loaded_options = None
    _globals['_PUBLISHER'].methods_by_name['Publish']._serialized_options = b'\x82\xd3\xe4\x93\x02D"?/v1/{message_bus=projects/*/locations/*/messageBuses/*}:publish:\x01*'
    _globals['_PUBLISHCHANNELCONNECTIONEVENTSREQUEST']._serialized_start = 291
    _globals['_PUBLISHCHANNELCONNECTIONEVENTSREQUEST']._serialized_end = 417
    _globals['_PUBLISHCHANNELCONNECTIONEVENTSRESPONSE']._serialized_start = 419
    _globals['_PUBLISHCHANNELCONNECTIONEVENTSRESPONSE']._serialized_end = 459
    _globals['_PUBLISHEVENTSREQUEST']._serialized_start = 461
    _globals['_PUBLISHEVENTSREQUEST']._serialized_end = 559
    _globals['_PUBLISHEVENTSRESPONSE']._serialized_start = 561
    _globals['_PUBLISHEVENTSRESPONSE']._serialized_end = 584
    _globals['_PUBLISHREQUEST']._serialized_start = 587
    _globals['_PUBLISHREQUEST']._serialized_end = 761
    _globals['_PUBLISHRESPONSE']._serialized_start = 763
    _globals['_PUBLISHRESPONSE']._serialized_end = 780
    _globals['_PUBLISHER']._serialized_start = 783
    _globals['_PUBLISHER']._serialized_end = 1570