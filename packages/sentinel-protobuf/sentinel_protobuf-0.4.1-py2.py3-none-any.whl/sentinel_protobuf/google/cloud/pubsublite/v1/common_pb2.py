"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_runtime_version.ValidateProtobufRuntimeVersion(_runtime_version.Domain.PUBLIC, 5, 28, 1, '', 'google/cloud/pubsublite/v1/common.proto')
_sym_db = _symbol_database.Default()
from .....google.api import field_behavior_pb2 as google_dot_api_dot_field__behavior__pb2
from .....google.api import resource_pb2 as google_dot_api_dot_resource__pb2
from google.protobuf import duration_pb2 as google_dot_protobuf_dot_duration__pb2
from google.protobuf import timestamp_pb2 as google_dot_protobuf_dot_timestamp__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\'google/cloud/pubsublite/v1/common.proto\x12\x1agoogle.cloud.pubsublite.v1\x1a\x1fgoogle/api/field_behavior.proto\x1a\x19google/api/resource.proto\x1a\x1egoogle/protobuf/duration.proto\x1a\x1fgoogle/protobuf/timestamp.proto"!\n\x0fAttributeValues\x12\x0e\n\x06values\x18\x01 \x03(\x0c"\x89\x02\n\rPubSubMessage\x12\x0b\n\x03key\x18\x01 \x01(\x0c\x12\x0c\n\x04data\x18\x02 \x01(\x0c\x12M\n\nattributes\x18\x03 \x03(\x0b29.google.cloud.pubsublite.v1.PubSubMessage.AttributesEntry\x12.\n\nevent_time\x18\x04 \x01(\x0b2\x1a.google.protobuf.Timestamp\x1a^\n\x0fAttributesEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12:\n\x05value\x18\x02 \x01(\x0b2+.google.cloud.pubsublite.v1.AttributeValues:\x028\x01"\x18\n\x06Cursor\x12\x0e\n\x06offset\x18\x01 \x01(\x03"\xc8\x01\n\x10SequencedMessage\x122\n\x06cursor\x18\x01 \x01(\x0b2".google.cloud.pubsublite.v1.Cursor\x120\n\x0cpublish_time\x18\x02 \x01(\x0b2\x1a.google.protobuf.Timestamp\x12:\n\x07message\x18\x03 \x01(\x0b2).google.cloud.pubsublite.v1.PubSubMessage\x12\x12\n\nsize_bytes\x18\x04 \x01(\x03"\xa8\x01\n\x0bReservation\x12\x0c\n\x04name\x18\x01 \x01(\t\x12\x1b\n\x13throughput_capacity\x18\x02 \x01(\x03:n\xeaAk\n%pubsublite.googleapis.com/Reservation\x12Bprojects/{project}/locations/{location}/reservations/{reservation}"\xf7\x05\n\x05Topic\x12\x0c\n\x04name\x18\x01 \x01(\t\x12K\n\x10partition_config\x18\x02 \x01(\x0b21.google.cloud.pubsublite.v1.Topic.PartitionConfig\x12K\n\x10retention_config\x18\x03 \x01(\x0b21.google.cloud.pubsublite.v1.Topic.RetentionConfig\x12O\n\x12reservation_config\x18\x04 \x01(\x0b23.google.cloud.pubsublite.v1.Topic.ReservationConfig\x1a\xda\x01\n\x0fPartitionConfig\x12\r\n\x05count\x18\x01 \x01(\x03\x12\x13\n\x05scale\x18\x02 \x01(\x05B\x02\x18\x01H\x00\x12N\n\x08capacity\x18\x03 \x01(\x0b2:.google.cloud.pubsublite.v1.Topic.PartitionConfig.CapacityH\x00\x1aF\n\x08Capacity\x12\x1b\n\x13publish_mib_per_sec\x18\x01 \x01(\x05\x12\x1d\n\x15subscribe_mib_per_sec\x18\x02 \x01(\x05B\x0b\n\tdimension\x1aY\n\x0fRetentionConfig\x12\x1b\n\x13per_partition_bytes\x18\x01 \x01(\x03\x12)\n\x06period\x18\x02 \x01(\x0b2\x19.google.protobuf.Duration\x1a_\n\x11ReservationConfig\x12J\n\x16throughput_reservation\x18\x01 \x01(\tB*\xfaA\'\n%pubsublite.googleapis.com/Reservation:\\\xeaAY\n\x1fpubsublite.googleapis.com/Topic\x126projects/{project}/locations/{location}/topics/{topic}"\xc5\x04\n\x0cSubscription\x12\x0c\n\x04name\x18\x01 \x01(\t\x123\n\x05topic\x18\x02 \x01(\tB$\xfaA!\n\x1fpubsublite.googleapis.com/Topic\x12P\n\x0fdelivery_config\x18\x03 \x01(\x0b27.google.cloud.pubsublite.v1.Subscription.DeliveryConfig\x12?\n\rexport_config\x18\x04 \x01(\x0b2(.google.cloud.pubsublite.v1.ExportConfig\x1a\xeb\x01\n\x0eDeliveryConfig\x12i\n\x14delivery_requirement\x18\x03 \x01(\x0e2K.google.cloud.pubsublite.v1.Subscription.DeliveryConfig.DeliveryRequirement"n\n\x13DeliveryRequirement\x12$\n DELIVERY_REQUIREMENT_UNSPECIFIED\x10\x00\x12\x17\n\x13DELIVER_IMMEDIATELY\x10\x01\x12\x18\n\x14DELIVER_AFTER_STORED\x10\x02:q\xeaAn\n&pubsublite.googleapis.com/Subscription\x12Dprojects/{project}/locations/{location}/subscriptions/{subscription}"\xc1\x03\n\x0cExportConfig\x12E\n\rdesired_state\x18\x01 \x01(\x0e2..google.cloud.pubsublite.v1.ExportConfig.State\x12J\n\rcurrent_state\x18\x06 \x01(\x0e2..google.cloud.pubsublite.v1.ExportConfig.StateB\x03\xe0A\x03\x12B\n\x11dead_letter_topic\x18\x05 \x01(\tB\'\xe0A\x01\xfaA!\n\x1fpubsublite.googleapis.com/Topic\x12N\n\rpubsub_config\x18\x03 \x01(\x0b25.google.cloud.pubsublite.v1.ExportConfig.PubSubConfigH\x00\x1a\x1d\n\x0cPubSubConfig\x12\r\n\x05topic\x18\x01 \x01(\t"\\\n\x05State\x12\x15\n\x11STATE_UNSPECIFIED\x10\x00\x12\n\n\x06ACTIVE\x10\x01\x12\n\n\x06PAUSED\x10\x02\x12\x15\n\x11PERMISSION_DENIED\x10\x03\x12\r\n\tNOT_FOUND\x10\x04B\r\n\x0bdestination"z\n\nTimeTarget\x122\n\x0cpublish_time\x18\x01 \x01(\x0b2\x1a.google.protobuf.TimestampH\x00\x120\n\nevent_time\x18\x02 \x01(\x0b2\x1a.google.protobuf.TimestampH\x00B\x06\n\x04timeB\xcf\x01\n!com.google.cloud.pubsublite.protoB\x0bCommonProtoP\x01Z>cloud.google.com/go/pubsublite/apiv1/pubsublitepb;pubsublitepb\xf8\x01\x01\xaa\x02\x1aGoogle.Cloud.PubSubLite.V1\xca\x02\x1aGoogle\\Cloud\\PubSubLite\\V1\xea\x02\x1dGoogle::Cloud::PubSubLite::V1b\x06proto3')
_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'google.cloud.pubsublite.v1.common_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
    _globals['DESCRIPTOR']._loaded_options = None
    _globals['DESCRIPTOR']._serialized_options = b'\n!com.google.cloud.pubsublite.protoB\x0bCommonProtoP\x01Z>cloud.google.com/go/pubsublite/apiv1/pubsublitepb;pubsublitepb\xf8\x01\x01\xaa\x02\x1aGoogle.Cloud.PubSubLite.V1\xca\x02\x1aGoogle\\Cloud\\PubSubLite\\V1\xea\x02\x1dGoogle::Cloud::PubSubLite::V1'
    _globals['_PUBSUBMESSAGE_ATTRIBUTESENTRY']._loaded_options = None
    _globals['_PUBSUBMESSAGE_ATTRIBUTESENTRY']._serialized_options = b'8\x01'
    _globals['_RESERVATION']._loaded_options = None
    _globals['_RESERVATION']._serialized_options = b'\xeaAk\n%pubsublite.googleapis.com/Reservation\x12Bprojects/{project}/locations/{location}/reservations/{reservation}'
    _globals['_TOPIC_PARTITIONCONFIG'].fields_by_name['scale']._loaded_options = None
    _globals['_TOPIC_PARTITIONCONFIG'].fields_by_name['scale']._serialized_options = b'\x18\x01'
    _globals['_TOPIC_RESERVATIONCONFIG'].fields_by_name['throughput_reservation']._loaded_options = None
    _globals['_TOPIC_RESERVATIONCONFIG'].fields_by_name['throughput_reservation']._serialized_options = b"\xfaA'\n%pubsublite.googleapis.com/Reservation"
    _globals['_TOPIC']._loaded_options = None
    _globals['_TOPIC']._serialized_options = b'\xeaAY\n\x1fpubsublite.googleapis.com/Topic\x126projects/{project}/locations/{location}/topics/{topic}'
    _globals['_SUBSCRIPTION'].fields_by_name['topic']._loaded_options = None
    _globals['_SUBSCRIPTION'].fields_by_name['topic']._serialized_options = b'\xfaA!\n\x1fpubsublite.googleapis.com/Topic'
    _globals['_SUBSCRIPTION']._loaded_options = None
    _globals['_SUBSCRIPTION']._serialized_options = b'\xeaAn\n&pubsublite.googleapis.com/Subscription\x12Dprojects/{project}/locations/{location}/subscriptions/{subscription}'
    _globals['_EXPORTCONFIG'].fields_by_name['current_state']._loaded_options = None
    _globals['_EXPORTCONFIG'].fields_by_name['current_state']._serialized_options = b'\xe0A\x03'
    _globals['_EXPORTCONFIG'].fields_by_name['dead_letter_topic']._loaded_options = None
    _globals['_EXPORTCONFIG'].fields_by_name['dead_letter_topic']._serialized_options = b'\xe0A\x01\xfaA!\n\x1fpubsublite.googleapis.com/Topic'
    _globals['_ATTRIBUTEVALUES']._serialized_start = 196
    _globals['_ATTRIBUTEVALUES']._serialized_end = 229
    _globals['_PUBSUBMESSAGE']._serialized_start = 232
    _globals['_PUBSUBMESSAGE']._serialized_end = 497
    _globals['_PUBSUBMESSAGE_ATTRIBUTESENTRY']._serialized_start = 403
    _globals['_PUBSUBMESSAGE_ATTRIBUTESENTRY']._serialized_end = 497
    _globals['_CURSOR']._serialized_start = 499
    _globals['_CURSOR']._serialized_end = 523
    _globals['_SEQUENCEDMESSAGE']._serialized_start = 526
    _globals['_SEQUENCEDMESSAGE']._serialized_end = 726
    _globals['_RESERVATION']._serialized_start = 729
    _globals['_RESERVATION']._serialized_end = 897
    _globals['_TOPIC']._serialized_start = 900
    _globals['_TOPIC']._serialized_end = 1659
    _globals['_TOPIC_PARTITIONCONFIG']._serialized_start = 1159
    _globals['_TOPIC_PARTITIONCONFIG']._serialized_end = 1377
    _globals['_TOPIC_PARTITIONCONFIG_CAPACITY']._serialized_start = 1294
    _globals['_TOPIC_PARTITIONCONFIG_CAPACITY']._serialized_end = 1364
    _globals['_TOPIC_RETENTIONCONFIG']._serialized_start = 1379
    _globals['_TOPIC_RETENTIONCONFIG']._serialized_end = 1468
    _globals['_TOPIC_RESERVATIONCONFIG']._serialized_start = 1470
    _globals['_TOPIC_RESERVATIONCONFIG']._serialized_end = 1565
    _globals['_SUBSCRIPTION']._serialized_start = 1662
    _globals['_SUBSCRIPTION']._serialized_end = 2243
    _globals['_SUBSCRIPTION_DELIVERYCONFIG']._serialized_start = 1893
    _globals['_SUBSCRIPTION_DELIVERYCONFIG']._serialized_end = 2128
    _globals['_SUBSCRIPTION_DELIVERYCONFIG_DELIVERYREQUIREMENT']._serialized_start = 2018
    _globals['_SUBSCRIPTION_DELIVERYCONFIG_DELIVERYREQUIREMENT']._serialized_end = 2128
    _globals['_EXPORTCONFIG']._serialized_start = 2246
    _globals['_EXPORTCONFIG']._serialized_end = 2695
    _globals['_EXPORTCONFIG_PUBSUBCONFIG']._serialized_start = 2557
    _globals['_EXPORTCONFIG_PUBSUBCONFIG']._serialized_end = 2586
    _globals['_EXPORTCONFIG_STATE']._serialized_start = 2588
    _globals['_EXPORTCONFIG_STATE']._serialized_end = 2680
    _globals['_TIMETARGET']._serialized_start = 2697
    _globals['_TIMETARGET']._serialized_end = 2819