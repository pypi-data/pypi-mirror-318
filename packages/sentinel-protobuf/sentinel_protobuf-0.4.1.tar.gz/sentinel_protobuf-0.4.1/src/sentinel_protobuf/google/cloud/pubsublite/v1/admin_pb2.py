"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_runtime_version.ValidateProtobufRuntimeVersion(_runtime_version.Domain.PUBLIC, 5, 28, 1, '', 'google/cloud/pubsublite/v1/admin.proto')
_sym_db = _symbol_database.Default()
from .....google.api import annotations_pb2 as google_dot_api_dot_annotations__pb2
from .....google.api import client_pb2 as google_dot_api_dot_client__pb2
from .....google.api import field_behavior_pb2 as google_dot_api_dot_field__behavior__pb2
from .....google.api import resource_pb2 as google_dot_api_dot_resource__pb2
from .....google.cloud.pubsublite.v1 import common_pb2 as google_dot_cloud_dot_pubsublite_dot_v1_dot_common__pb2
from .....google.longrunning import operations_pb2 as google_dot_longrunning_dot_operations__pb2
from google.protobuf import empty_pb2 as google_dot_protobuf_dot_empty__pb2
from google.protobuf import field_mask_pb2 as google_dot_protobuf_dot_field__mask__pb2
from google.protobuf import timestamp_pb2 as google_dot_protobuf_dot_timestamp__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n&google/cloud/pubsublite/v1/admin.proto\x12\x1agoogle.cloud.pubsublite.v1\x1a\x1cgoogle/api/annotations.proto\x1a\x17google/api/client.proto\x1a\x1fgoogle/api/field_behavior.proto\x1a\x19google/api/resource.proto\x1a\'google/cloud/pubsublite/v1/common.proto\x1a#google/longrunning/operations.proto\x1a\x1bgoogle/protobuf/empty.proto\x1a google/protobuf/field_mask.proto\x1a\x1fgoogle/protobuf/timestamp.proto"\x9d\x01\n\x12CreateTopicRequest\x129\n\x06parent\x18\x01 \x01(\tB)\xe0A\x02\xfaA#\n!locations.googleapis.com/Location\x125\n\x05topic\x18\x02 \x01(\x0b2!.google.cloud.pubsublite.v1.TopicB\x03\xe0A\x02\x12\x15\n\x08topic_id\x18\x03 \x01(\tB\x03\xe0A\x02"H\n\x0fGetTopicRequest\x125\n\x04name\x18\x01 \x01(\tB\'\xe0A\x02\xfaA!\n\x1fpubsublite.googleapis.com/Topic"R\n\x19GetTopicPartitionsRequest\x125\n\x04name\x18\x01 \x01(\tB\'\xe0A\x02\xfaA!\n\x1fpubsublite.googleapis.com/Topic"*\n\x0fTopicPartitions\x12\x17\n\x0fpartition_count\x18\x01 \x01(\x03"u\n\x11ListTopicsRequest\x129\n\x06parent\x18\x01 \x01(\tB)\xe0A\x02\xfaA#\n!locations.googleapis.com/Location\x12\x11\n\tpage_size\x18\x02 \x01(\x05\x12\x12\n\npage_token\x18\x03 \x01(\t"`\n\x12ListTopicsResponse\x121\n\x06topics\x18\x01 \x03(\x0b2!.google.cloud.pubsublite.v1.Topic\x12\x17\n\x0fnext_page_token\x18\x02 \x01(\t"\x81\x01\n\x12UpdateTopicRequest\x125\n\x05topic\x18\x01 \x01(\x0b2!.google.cloud.pubsublite.v1.TopicB\x03\xe0A\x02\x124\n\x0bupdate_mask\x18\x02 \x01(\x0b2\x1a.google.protobuf.FieldMaskB\x03\xe0A\x02"K\n\x12DeleteTopicRequest\x125\n\x04name\x18\x01 \x01(\tB\'\xe0A\x02\xfaA!\n\x1fpubsublite.googleapis.com/Topic"}\n\x1dListTopicSubscriptionsRequest\x125\n\x04name\x18\x01 \x01(\tB\'\xe0A\x02\xfaA!\n\x1fpubsublite.googleapis.com/Topic\x12\x11\n\tpage_size\x18\x02 \x01(\x05\x12\x12\n\npage_token\x18\x03 \x01(\t"P\n\x1eListTopicSubscriptionsResponse\x12\x15\n\rsubscriptions\x18\x01 \x03(\t\x12\x17\n\x0fnext_page_token\x18\x02 \x01(\t"\xcf\x01\n\x19CreateSubscriptionRequest\x129\n\x06parent\x18\x01 \x01(\tB)\xe0A\x02\xfaA#\n!locations.googleapis.com/Location\x12C\n\x0csubscription\x18\x02 \x01(\x0b2(.google.cloud.pubsublite.v1.SubscriptionB\x03\xe0A\x02\x12\x1c\n\x0fsubscription_id\x18\x03 \x01(\tB\x03\xe0A\x02\x12\x14\n\x0cskip_backlog\x18\x04 \x01(\x08"V\n\x16GetSubscriptionRequest\x12<\n\x04name\x18\x01 \x01(\tB.\xe0A\x02\xfaA(\n&pubsublite.googleapis.com/Subscription"|\n\x18ListSubscriptionsRequest\x129\n\x06parent\x18\x01 \x01(\tB)\xe0A\x02\xfaA#\n!locations.googleapis.com/Location\x12\x11\n\tpage_size\x18\x02 \x01(\x05\x12\x12\n\npage_token\x18\x03 \x01(\t"u\n\x19ListSubscriptionsResponse\x12?\n\rsubscriptions\x18\x01 \x03(\x0b2(.google.cloud.pubsublite.v1.Subscription\x12\x17\n\x0fnext_page_token\x18\x02 \x01(\t"\x96\x01\n\x19UpdateSubscriptionRequest\x12C\n\x0csubscription\x18\x01 \x01(\x0b2(.google.cloud.pubsublite.v1.SubscriptionB\x03\xe0A\x02\x124\n\x0bupdate_mask\x18\x02 \x01(\x0b2\x1a.google.protobuf.FieldMaskB\x03\xe0A\x02"Y\n\x19DeleteSubscriptionRequest\x12<\n\x04name\x18\x01 \x01(\tB.\xe0A\x02\xfaA(\n&pubsublite.googleapis.com/Subscription"\xba\x02\n\x17SeekSubscriptionRequest\x12<\n\x04name\x18\x01 \x01(\tB.\xe0A\x02\xfaA(\n&pubsublite.googleapis.com/Subscription\x12W\n\x0cnamed_target\x18\x02 \x01(\x0e2?.google.cloud.pubsublite.v1.SeekSubscriptionRequest.NamedTargetH\x00\x12=\n\x0btime_target\x18\x03 \x01(\x0b2&.google.cloud.pubsublite.v1.TimeTargetH\x00"?\n\x0bNamedTarget\x12\x1c\n\x18NAMED_TARGET_UNSPECIFIED\x10\x00\x12\x08\n\x04TAIL\x10\x01\x12\x08\n\x04HEAD\x10\x02B\x08\n\x06target"\x1a\n\x18SeekSubscriptionResponse"\x90\x01\n\x11OperationMetadata\x12/\n\x0bcreate_time\x18\x01 \x01(\x0b2\x1a.google.protobuf.Timestamp\x12,\n\x08end_time\x18\x02 \x01(\x0b2\x1a.google.protobuf.Timestamp\x12\x0e\n\x06target\x18\x03 \x01(\t\x12\x0c\n\x04verb\x18\x04 \x01(\t"\xb5\x01\n\x18CreateReservationRequest\x129\n\x06parent\x18\x01 \x01(\tB)\xe0A\x02\xfaA#\n!locations.googleapis.com/Location\x12A\n\x0breservation\x18\x02 \x01(\x0b2\'.google.cloud.pubsublite.v1.ReservationB\x03\xe0A\x02\x12\x1b\n\x0ereservation_id\x18\x03 \x01(\tB\x03\xe0A\x02"T\n\x15GetReservationRequest\x12;\n\x04name\x18\x01 \x01(\tB-\xe0A\x02\xfaA\'\n%pubsublite.googleapis.com/Reservation"{\n\x17ListReservationsRequest\x129\n\x06parent\x18\x01 \x01(\tB)\xe0A\x02\xfaA#\n!locations.googleapis.com/Location\x12\x11\n\tpage_size\x18\x02 \x01(\x05\x12\x12\n\npage_token\x18\x03 \x01(\t"r\n\x18ListReservationsResponse\x12=\n\x0creservations\x18\x01 \x03(\x0b2\'.google.cloud.pubsublite.v1.Reservation\x12\x17\n\x0fnext_page_token\x18\x02 \x01(\t"\x93\x01\n\x18UpdateReservationRequest\x12A\n\x0breservation\x18\x01 \x01(\x0b2\'.google.cloud.pubsublite.v1.ReservationB\x03\xe0A\x02\x124\n\x0bupdate_mask\x18\x02 \x01(\x0b2\x1a.google.protobuf.FieldMaskB\x03\xe0A\x02"W\n\x18DeleteReservationRequest\x12;\n\x04name\x18\x01 \x01(\tB-\xe0A\x02\xfaA\'\n%pubsublite.googleapis.com/Reservation"\x82\x01\n\x1cListReservationTopicsRequest\x12;\n\x04name\x18\x01 \x01(\tB-\xe0A\x02\xfaA\'\n%pubsublite.googleapis.com/Reservation\x12\x11\n\tpage_size\x18\x02 \x01(\x05\x12\x12\n\npage_token\x18\x03 \x01(\t"H\n\x1dListReservationTopicsResponse\x12\x0e\n\x06topics\x18\x01 \x03(\t\x12\x17\n\x0fnext_page_token\x18\x02 \x01(\t2\xaf\x1e\n\x0cAdminService\x12\xb9\x01\n\x0bCreateTopic\x12..google.cloud.pubsublite.v1.CreateTopicRequest\x1a!.google.cloud.pubsublite.v1.Topic"W\xdaA\x15parent,topic,topic_id\x82\xd3\xe4\x93\x029"0/v1/admin/{parent=projects/*/locations/*}/topics:\x05topic\x12\x9b\x01\n\x08GetTopic\x12+.google.cloud.pubsublite.v1.GetTopicRequest\x1a!.google.cloud.pubsublite.v1.Topic"?\xdaA\x04name\x82\xd3\xe4\x93\x022\x120/v1/admin/{name=projects/*/locations/*/topics/*}\x12\xc4\x01\n\x12GetTopicPartitions\x125.google.cloud.pubsublite.v1.GetTopicPartitionsRequest\x1a+.google.cloud.pubsublite.v1.TopicPartitions"J\xdaA\x04name\x82\xd3\xe4\x93\x02=\x12;/v1/admin/{name=projects/*/locations/*/topics/*}/partitions\x12\xae\x01\n\nListTopics\x12-.google.cloud.pubsublite.v1.ListTopicsRequest\x1a..google.cloud.pubsublite.v1.ListTopicsResponse"A\xdaA\x06parent\x82\xd3\xe4\x93\x022\x120/v1/admin/{parent=projects/*/locations/*}/topics\x12\xbb\x01\n\x0bUpdateTopic\x12..google.cloud.pubsublite.v1.UpdateTopicRequest\x1a!.google.cloud.pubsublite.v1.Topic"Y\xdaA\x11topic,update_mask\x82\xd3\xe4\x93\x02?26/v1/admin/{topic.name=projects/*/locations/*/topics/*}:\x05topic\x12\x96\x01\n\x0bDeleteTopic\x12..google.cloud.pubsublite.v1.DeleteTopicRequest\x1a\x16.google.protobuf.Empty"?\xdaA\x04name\x82\xd3\xe4\x93\x022*0/v1/admin/{name=projects/*/locations/*/topics/*}\x12\xde\x01\n\x16ListTopicSubscriptions\x129.google.cloud.pubsublite.v1.ListTopicSubscriptionsRequest\x1a:.google.cloud.pubsublite.v1.ListTopicSubscriptionsResponse"M\xdaA\x04name\x82\xd3\xe4\x93\x02@\x12>/v1/admin/{name=projects/*/locations/*/topics/*}/subscriptions\x12\xea\x01\n\x12CreateSubscription\x125.google.cloud.pubsublite.v1.CreateSubscriptionRequest\x1a(.google.cloud.pubsublite.v1.Subscription"s\xdaA#parent,subscription,subscription_id\x82\xd3\xe4\x93\x02G"7/v1/admin/{parent=projects/*/locations/*}/subscriptions:\x0csubscription\x12\xb7\x01\n\x0fGetSubscription\x122.google.cloud.pubsublite.v1.GetSubscriptionRequest\x1a(.google.cloud.pubsublite.v1.Subscription"F\xdaA\x04name\x82\xd3\xe4\x93\x029\x127/v1/admin/{name=projects/*/locations/*/subscriptions/*}\x12\xca\x01\n\x11ListSubscriptions\x124.google.cloud.pubsublite.v1.ListSubscriptionsRequest\x1a5.google.cloud.pubsublite.v1.ListSubscriptionsResponse"H\xdaA\x06parent\x82\xd3\xe4\x93\x029\x127/v1/admin/{parent=projects/*/locations/*}/subscriptions\x12\xec\x01\n\x12UpdateSubscription\x125.google.cloud.pubsublite.v1.UpdateSubscriptionRequest\x1a(.google.cloud.pubsublite.v1.Subscription"u\xdaA\x18subscription,update_mask\x82\xd3\xe4\x93\x02T2D/v1/admin/{subscription.name=projects/*/locations/*/subscriptions/*}:\x0csubscription\x12\xab\x01\n\x12DeleteSubscription\x125.google.cloud.pubsublite.v1.DeleteSubscriptionRequest\x1a\x16.google.protobuf.Empty"F\xdaA\x04name\x82\xd3\xe4\x93\x029*7/v1/admin/{name=projects/*/locations/*/subscriptions/*}\x12\xdf\x01\n\x10SeekSubscription\x123.google.cloud.pubsublite.v1.SeekSubscriptionRequest\x1a\x1d.google.longrunning.Operation"w\xcaA-\n\x18SeekSubscriptionResponse\x12\x11OperationMetadata\x82\xd3\xe4\x93\x02A"</v1/admin/{name=projects/*/locations/*/subscriptions/*}:seek:\x01*\x12\xe3\x01\n\x11CreateReservation\x124.google.cloud.pubsublite.v1.CreateReservationRequest\x1a\'.google.cloud.pubsublite.v1.Reservation"o\xdaA!parent,reservation,reservation_id\x82\xd3\xe4\x93\x02E"6/v1/admin/{parent=projects/*/locations/*}/reservations:\x0breservation\x12\xb3\x01\n\x0eGetReservation\x121.google.cloud.pubsublite.v1.GetReservationRequest\x1a\'.google.cloud.pubsublite.v1.Reservation"E\xdaA\x04name\x82\xd3\xe4\x93\x028\x126/v1/admin/{name=projects/*/locations/*/reservations/*}\x12\xc6\x01\n\x10ListReservations\x123.google.cloud.pubsublite.v1.ListReservationsRequest\x1a4.google.cloud.pubsublite.v1.ListReservationsResponse"G\xdaA\x06parent\x82\xd3\xe4\x93\x028\x126/v1/admin/{parent=projects/*/locations/*}/reservations\x12\xe5\x01\n\x11UpdateReservation\x124.google.cloud.pubsublite.v1.UpdateReservationRequest\x1a\'.google.cloud.pubsublite.v1.Reservation"q\xdaA\x17reservation,update_mask\x82\xd3\xe4\x93\x02Q2B/v1/admin/{reservation.name=projects/*/locations/*/reservations/*}:\x0breservation\x12\xa8\x01\n\x11DeleteReservation\x124.google.cloud.pubsublite.v1.DeleteReservationRequest\x1a\x16.google.protobuf.Empty"E\xdaA\x04name\x82\xd3\xe4\x93\x028*6/v1/admin/{name=projects/*/locations/*/reservations/*}\x12\xda\x01\n\x15ListReservationTopics\x128.google.cloud.pubsublite.v1.ListReservationTopicsRequest\x1a9.google.cloud.pubsublite.v1.ListReservationTopicsResponse"L\xdaA\x04name\x82\xd3\xe4\x93\x02?\x12=/v1/admin/{name=projects/*/locations/*/reservations/*}/topics\x1aM\xcaA\x19pubsublite.googleapis.com\xd2A.https://www.googleapis.com/auth/cloud-platformB\xcb\x01\n!com.google.cloud.pubsublite.protoB\nAdminProtoP\x01Z>cloud.google.com/go/pubsublite/apiv1/pubsublitepb;pubsublitepb\xaa\x02\x1aGoogle.Cloud.PubSubLite.V1\xca\x02\x1aGoogle\\Cloud\\PubSubLite\\V1\xea\x02\x1dGoogle::Cloud::PubSubLite::V1b\x06proto3')
_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'google.cloud.pubsublite.v1.admin_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
    _globals['DESCRIPTOR']._loaded_options = None
    _globals['DESCRIPTOR']._serialized_options = b'\n!com.google.cloud.pubsublite.protoB\nAdminProtoP\x01Z>cloud.google.com/go/pubsublite/apiv1/pubsublitepb;pubsublitepb\xaa\x02\x1aGoogle.Cloud.PubSubLite.V1\xca\x02\x1aGoogle\\Cloud\\PubSubLite\\V1\xea\x02\x1dGoogle::Cloud::PubSubLite::V1'
    _globals['_CREATETOPICREQUEST'].fields_by_name['parent']._loaded_options = None
    _globals['_CREATETOPICREQUEST'].fields_by_name['parent']._serialized_options = b'\xe0A\x02\xfaA#\n!locations.googleapis.com/Location'
    _globals['_CREATETOPICREQUEST'].fields_by_name['topic']._loaded_options = None
    _globals['_CREATETOPICREQUEST'].fields_by_name['topic']._serialized_options = b'\xe0A\x02'
    _globals['_CREATETOPICREQUEST'].fields_by_name['topic_id']._loaded_options = None
    _globals['_CREATETOPICREQUEST'].fields_by_name['topic_id']._serialized_options = b'\xe0A\x02'
    _globals['_GETTOPICREQUEST'].fields_by_name['name']._loaded_options = None
    _globals['_GETTOPICREQUEST'].fields_by_name['name']._serialized_options = b'\xe0A\x02\xfaA!\n\x1fpubsublite.googleapis.com/Topic'
    _globals['_GETTOPICPARTITIONSREQUEST'].fields_by_name['name']._loaded_options = None
    _globals['_GETTOPICPARTITIONSREQUEST'].fields_by_name['name']._serialized_options = b'\xe0A\x02\xfaA!\n\x1fpubsublite.googleapis.com/Topic'
    _globals['_LISTTOPICSREQUEST'].fields_by_name['parent']._loaded_options = None
    _globals['_LISTTOPICSREQUEST'].fields_by_name['parent']._serialized_options = b'\xe0A\x02\xfaA#\n!locations.googleapis.com/Location'
    _globals['_UPDATETOPICREQUEST'].fields_by_name['topic']._loaded_options = None
    _globals['_UPDATETOPICREQUEST'].fields_by_name['topic']._serialized_options = b'\xe0A\x02'
    _globals['_UPDATETOPICREQUEST'].fields_by_name['update_mask']._loaded_options = None
    _globals['_UPDATETOPICREQUEST'].fields_by_name['update_mask']._serialized_options = b'\xe0A\x02'
    _globals['_DELETETOPICREQUEST'].fields_by_name['name']._loaded_options = None
    _globals['_DELETETOPICREQUEST'].fields_by_name['name']._serialized_options = b'\xe0A\x02\xfaA!\n\x1fpubsublite.googleapis.com/Topic'
    _globals['_LISTTOPICSUBSCRIPTIONSREQUEST'].fields_by_name['name']._loaded_options = None
    _globals['_LISTTOPICSUBSCRIPTIONSREQUEST'].fields_by_name['name']._serialized_options = b'\xe0A\x02\xfaA!\n\x1fpubsublite.googleapis.com/Topic'
    _globals['_CREATESUBSCRIPTIONREQUEST'].fields_by_name['parent']._loaded_options = None
    _globals['_CREATESUBSCRIPTIONREQUEST'].fields_by_name['parent']._serialized_options = b'\xe0A\x02\xfaA#\n!locations.googleapis.com/Location'
    _globals['_CREATESUBSCRIPTIONREQUEST'].fields_by_name['subscription']._loaded_options = None
    _globals['_CREATESUBSCRIPTIONREQUEST'].fields_by_name['subscription']._serialized_options = b'\xe0A\x02'
    _globals['_CREATESUBSCRIPTIONREQUEST'].fields_by_name['subscription_id']._loaded_options = None
    _globals['_CREATESUBSCRIPTIONREQUEST'].fields_by_name['subscription_id']._serialized_options = b'\xe0A\x02'
    _globals['_GETSUBSCRIPTIONREQUEST'].fields_by_name['name']._loaded_options = None
    _globals['_GETSUBSCRIPTIONREQUEST'].fields_by_name['name']._serialized_options = b'\xe0A\x02\xfaA(\n&pubsublite.googleapis.com/Subscription'
    _globals['_LISTSUBSCRIPTIONSREQUEST'].fields_by_name['parent']._loaded_options = None
    _globals['_LISTSUBSCRIPTIONSREQUEST'].fields_by_name['parent']._serialized_options = b'\xe0A\x02\xfaA#\n!locations.googleapis.com/Location'
    _globals['_UPDATESUBSCRIPTIONREQUEST'].fields_by_name['subscription']._loaded_options = None
    _globals['_UPDATESUBSCRIPTIONREQUEST'].fields_by_name['subscription']._serialized_options = b'\xe0A\x02'
    _globals['_UPDATESUBSCRIPTIONREQUEST'].fields_by_name['update_mask']._loaded_options = None
    _globals['_UPDATESUBSCRIPTIONREQUEST'].fields_by_name['update_mask']._serialized_options = b'\xe0A\x02'
    _globals['_DELETESUBSCRIPTIONREQUEST'].fields_by_name['name']._loaded_options = None
    _globals['_DELETESUBSCRIPTIONREQUEST'].fields_by_name['name']._serialized_options = b'\xe0A\x02\xfaA(\n&pubsublite.googleapis.com/Subscription'
    _globals['_SEEKSUBSCRIPTIONREQUEST'].fields_by_name['name']._loaded_options = None
    _globals['_SEEKSUBSCRIPTIONREQUEST'].fields_by_name['name']._serialized_options = b'\xe0A\x02\xfaA(\n&pubsublite.googleapis.com/Subscription'
    _globals['_CREATERESERVATIONREQUEST'].fields_by_name['parent']._loaded_options = None
    _globals['_CREATERESERVATIONREQUEST'].fields_by_name['parent']._serialized_options = b'\xe0A\x02\xfaA#\n!locations.googleapis.com/Location'
    _globals['_CREATERESERVATIONREQUEST'].fields_by_name['reservation']._loaded_options = None
    _globals['_CREATERESERVATIONREQUEST'].fields_by_name['reservation']._serialized_options = b'\xe0A\x02'
    _globals['_CREATERESERVATIONREQUEST'].fields_by_name['reservation_id']._loaded_options = None
    _globals['_CREATERESERVATIONREQUEST'].fields_by_name['reservation_id']._serialized_options = b'\xe0A\x02'
    _globals['_GETRESERVATIONREQUEST'].fields_by_name['name']._loaded_options = None
    _globals['_GETRESERVATIONREQUEST'].fields_by_name['name']._serialized_options = b"\xe0A\x02\xfaA'\n%pubsublite.googleapis.com/Reservation"
    _globals['_LISTRESERVATIONSREQUEST'].fields_by_name['parent']._loaded_options = None
    _globals['_LISTRESERVATIONSREQUEST'].fields_by_name['parent']._serialized_options = b'\xe0A\x02\xfaA#\n!locations.googleapis.com/Location'
    _globals['_UPDATERESERVATIONREQUEST'].fields_by_name['reservation']._loaded_options = None
    _globals['_UPDATERESERVATIONREQUEST'].fields_by_name['reservation']._serialized_options = b'\xe0A\x02'
    _globals['_UPDATERESERVATIONREQUEST'].fields_by_name['update_mask']._loaded_options = None
    _globals['_UPDATERESERVATIONREQUEST'].fields_by_name['update_mask']._serialized_options = b'\xe0A\x02'
    _globals['_DELETERESERVATIONREQUEST'].fields_by_name['name']._loaded_options = None
    _globals['_DELETERESERVATIONREQUEST'].fields_by_name['name']._serialized_options = b"\xe0A\x02\xfaA'\n%pubsublite.googleapis.com/Reservation"
    _globals['_LISTRESERVATIONTOPICSREQUEST'].fields_by_name['name']._loaded_options = None
    _globals['_LISTRESERVATIONTOPICSREQUEST'].fields_by_name['name']._serialized_options = b"\xe0A\x02\xfaA'\n%pubsublite.googleapis.com/Reservation"
    _globals['_ADMINSERVICE']._loaded_options = None
    _globals['_ADMINSERVICE']._serialized_options = b'\xcaA\x19pubsublite.googleapis.com\xd2A.https://www.googleapis.com/auth/cloud-platform'
    _globals['_ADMINSERVICE'].methods_by_name['CreateTopic']._loaded_options = None
    _globals['_ADMINSERVICE'].methods_by_name['CreateTopic']._serialized_options = b'\xdaA\x15parent,topic,topic_id\x82\xd3\xe4\x93\x029"0/v1/admin/{parent=projects/*/locations/*}/topics:\x05topic'
    _globals['_ADMINSERVICE'].methods_by_name['GetTopic']._loaded_options = None
    _globals['_ADMINSERVICE'].methods_by_name['GetTopic']._serialized_options = b'\xdaA\x04name\x82\xd3\xe4\x93\x022\x120/v1/admin/{name=projects/*/locations/*/topics/*}'
    _globals['_ADMINSERVICE'].methods_by_name['GetTopicPartitions']._loaded_options = None
    _globals['_ADMINSERVICE'].methods_by_name['GetTopicPartitions']._serialized_options = b'\xdaA\x04name\x82\xd3\xe4\x93\x02=\x12;/v1/admin/{name=projects/*/locations/*/topics/*}/partitions'
    _globals['_ADMINSERVICE'].methods_by_name['ListTopics']._loaded_options = None
    _globals['_ADMINSERVICE'].methods_by_name['ListTopics']._serialized_options = b'\xdaA\x06parent\x82\xd3\xe4\x93\x022\x120/v1/admin/{parent=projects/*/locations/*}/topics'
    _globals['_ADMINSERVICE'].methods_by_name['UpdateTopic']._loaded_options = None
    _globals['_ADMINSERVICE'].methods_by_name['UpdateTopic']._serialized_options = b'\xdaA\x11topic,update_mask\x82\xd3\xe4\x93\x02?26/v1/admin/{topic.name=projects/*/locations/*/topics/*}:\x05topic'
    _globals['_ADMINSERVICE'].methods_by_name['DeleteTopic']._loaded_options = None
    _globals['_ADMINSERVICE'].methods_by_name['DeleteTopic']._serialized_options = b'\xdaA\x04name\x82\xd3\xe4\x93\x022*0/v1/admin/{name=projects/*/locations/*/topics/*}'
    _globals['_ADMINSERVICE'].methods_by_name['ListTopicSubscriptions']._loaded_options = None
    _globals['_ADMINSERVICE'].methods_by_name['ListTopicSubscriptions']._serialized_options = b'\xdaA\x04name\x82\xd3\xe4\x93\x02@\x12>/v1/admin/{name=projects/*/locations/*/topics/*}/subscriptions'
    _globals['_ADMINSERVICE'].methods_by_name['CreateSubscription']._loaded_options = None
    _globals['_ADMINSERVICE'].methods_by_name['CreateSubscription']._serialized_options = b'\xdaA#parent,subscription,subscription_id\x82\xd3\xe4\x93\x02G"7/v1/admin/{parent=projects/*/locations/*}/subscriptions:\x0csubscription'
    _globals['_ADMINSERVICE'].methods_by_name['GetSubscription']._loaded_options = None
    _globals['_ADMINSERVICE'].methods_by_name['GetSubscription']._serialized_options = b'\xdaA\x04name\x82\xd3\xe4\x93\x029\x127/v1/admin/{name=projects/*/locations/*/subscriptions/*}'
    _globals['_ADMINSERVICE'].methods_by_name['ListSubscriptions']._loaded_options = None
    _globals['_ADMINSERVICE'].methods_by_name['ListSubscriptions']._serialized_options = b'\xdaA\x06parent\x82\xd3\xe4\x93\x029\x127/v1/admin/{parent=projects/*/locations/*}/subscriptions'
    _globals['_ADMINSERVICE'].methods_by_name['UpdateSubscription']._loaded_options = None
    _globals['_ADMINSERVICE'].methods_by_name['UpdateSubscription']._serialized_options = b'\xdaA\x18subscription,update_mask\x82\xd3\xe4\x93\x02T2D/v1/admin/{subscription.name=projects/*/locations/*/subscriptions/*}:\x0csubscription'
    _globals['_ADMINSERVICE'].methods_by_name['DeleteSubscription']._loaded_options = None
    _globals['_ADMINSERVICE'].methods_by_name['DeleteSubscription']._serialized_options = b'\xdaA\x04name\x82\xd3\xe4\x93\x029*7/v1/admin/{name=projects/*/locations/*/subscriptions/*}'
    _globals['_ADMINSERVICE'].methods_by_name['SeekSubscription']._loaded_options = None
    _globals['_ADMINSERVICE'].methods_by_name['SeekSubscription']._serialized_options = b'\xcaA-\n\x18SeekSubscriptionResponse\x12\x11OperationMetadata\x82\xd3\xe4\x93\x02A"</v1/admin/{name=projects/*/locations/*/subscriptions/*}:seek:\x01*'
    _globals['_ADMINSERVICE'].methods_by_name['CreateReservation']._loaded_options = None
    _globals['_ADMINSERVICE'].methods_by_name['CreateReservation']._serialized_options = b'\xdaA!parent,reservation,reservation_id\x82\xd3\xe4\x93\x02E"6/v1/admin/{parent=projects/*/locations/*}/reservations:\x0breservation'
    _globals['_ADMINSERVICE'].methods_by_name['GetReservation']._loaded_options = None
    _globals['_ADMINSERVICE'].methods_by_name['GetReservation']._serialized_options = b'\xdaA\x04name\x82\xd3\xe4\x93\x028\x126/v1/admin/{name=projects/*/locations/*/reservations/*}'
    _globals['_ADMINSERVICE'].methods_by_name['ListReservations']._loaded_options = None
    _globals['_ADMINSERVICE'].methods_by_name['ListReservations']._serialized_options = b'\xdaA\x06parent\x82\xd3\xe4\x93\x028\x126/v1/admin/{parent=projects/*/locations/*}/reservations'
    _globals['_ADMINSERVICE'].methods_by_name['UpdateReservation']._loaded_options = None
    _globals['_ADMINSERVICE'].methods_by_name['UpdateReservation']._serialized_options = b'\xdaA\x17reservation,update_mask\x82\xd3\xe4\x93\x02Q2B/v1/admin/{reservation.name=projects/*/locations/*/reservations/*}:\x0breservation'
    _globals['_ADMINSERVICE'].methods_by_name['DeleteReservation']._loaded_options = None
    _globals['_ADMINSERVICE'].methods_by_name['DeleteReservation']._serialized_options = b'\xdaA\x04name\x82\xd3\xe4\x93\x028*6/v1/admin/{name=projects/*/locations/*/reservations/*}'
    _globals['_ADMINSERVICE'].methods_by_name['ListReservationTopics']._loaded_options = None
    _globals['_ADMINSERVICE'].methods_by_name['ListReservationTopics']._serialized_options = b'\xdaA\x04name\x82\xd3\xe4\x93\x02?\x12=/v1/admin/{name=projects/*/locations/*/reservations/*}/topics'
    _globals['_CREATETOPICREQUEST']._serialized_start = 360
    _globals['_CREATETOPICREQUEST']._serialized_end = 517
    _globals['_GETTOPICREQUEST']._serialized_start = 519
    _globals['_GETTOPICREQUEST']._serialized_end = 591
    _globals['_GETTOPICPARTITIONSREQUEST']._serialized_start = 593
    _globals['_GETTOPICPARTITIONSREQUEST']._serialized_end = 675
    _globals['_TOPICPARTITIONS']._serialized_start = 677
    _globals['_TOPICPARTITIONS']._serialized_end = 719
    _globals['_LISTTOPICSREQUEST']._serialized_start = 721
    _globals['_LISTTOPICSREQUEST']._serialized_end = 838
    _globals['_LISTTOPICSRESPONSE']._serialized_start = 840
    _globals['_LISTTOPICSRESPONSE']._serialized_end = 936
    _globals['_UPDATETOPICREQUEST']._serialized_start = 939
    _globals['_UPDATETOPICREQUEST']._serialized_end = 1068
    _globals['_DELETETOPICREQUEST']._serialized_start = 1070
    _globals['_DELETETOPICREQUEST']._serialized_end = 1145
    _globals['_LISTTOPICSUBSCRIPTIONSREQUEST']._serialized_start = 1147
    _globals['_LISTTOPICSUBSCRIPTIONSREQUEST']._serialized_end = 1272
    _globals['_LISTTOPICSUBSCRIPTIONSRESPONSE']._serialized_start = 1274
    _globals['_LISTTOPICSUBSCRIPTIONSRESPONSE']._serialized_end = 1354
    _globals['_CREATESUBSCRIPTIONREQUEST']._serialized_start = 1357
    _globals['_CREATESUBSCRIPTIONREQUEST']._serialized_end = 1564
    _globals['_GETSUBSCRIPTIONREQUEST']._serialized_start = 1566
    _globals['_GETSUBSCRIPTIONREQUEST']._serialized_end = 1652
    _globals['_LISTSUBSCRIPTIONSREQUEST']._serialized_start = 1654
    _globals['_LISTSUBSCRIPTIONSREQUEST']._serialized_end = 1778
    _globals['_LISTSUBSCRIPTIONSRESPONSE']._serialized_start = 1780
    _globals['_LISTSUBSCRIPTIONSRESPONSE']._serialized_end = 1897
    _globals['_UPDATESUBSCRIPTIONREQUEST']._serialized_start = 1900
    _globals['_UPDATESUBSCRIPTIONREQUEST']._serialized_end = 2050
    _globals['_DELETESUBSCRIPTIONREQUEST']._serialized_start = 2052
    _globals['_DELETESUBSCRIPTIONREQUEST']._serialized_end = 2141
    _globals['_SEEKSUBSCRIPTIONREQUEST']._serialized_start = 2144
    _globals['_SEEKSUBSCRIPTIONREQUEST']._serialized_end = 2458
    _globals['_SEEKSUBSCRIPTIONREQUEST_NAMEDTARGET']._serialized_start = 2385
    _globals['_SEEKSUBSCRIPTIONREQUEST_NAMEDTARGET']._serialized_end = 2448
    _globals['_SEEKSUBSCRIPTIONRESPONSE']._serialized_start = 2460
    _globals['_SEEKSUBSCRIPTIONRESPONSE']._serialized_end = 2486
    _globals['_OPERATIONMETADATA']._serialized_start = 2489
    _globals['_OPERATIONMETADATA']._serialized_end = 2633
    _globals['_CREATERESERVATIONREQUEST']._serialized_start = 2636
    _globals['_CREATERESERVATIONREQUEST']._serialized_end = 2817
    _globals['_GETRESERVATIONREQUEST']._serialized_start = 2819
    _globals['_GETRESERVATIONREQUEST']._serialized_end = 2903
    _globals['_LISTRESERVATIONSREQUEST']._serialized_start = 2905
    _globals['_LISTRESERVATIONSREQUEST']._serialized_end = 3028
    _globals['_LISTRESERVATIONSRESPONSE']._serialized_start = 3030
    _globals['_LISTRESERVATIONSRESPONSE']._serialized_end = 3144
    _globals['_UPDATERESERVATIONREQUEST']._serialized_start = 3147
    _globals['_UPDATERESERVATIONREQUEST']._serialized_end = 3294
    _globals['_DELETERESERVATIONREQUEST']._serialized_start = 3296
    _globals['_DELETERESERVATIONREQUEST']._serialized_end = 3383
    _globals['_LISTRESERVATIONTOPICSREQUEST']._serialized_start = 3386
    _globals['_LISTRESERVATIONTOPICSREQUEST']._serialized_end = 3516
    _globals['_LISTRESERVATIONTOPICSRESPONSE']._serialized_start = 3518
    _globals['_LISTRESERVATIONTOPICSRESPONSE']._serialized_end = 3590
    _globals['_ADMINSERVICE']._serialized_start = 3593
    _globals['_ADMINSERVICE']._serialized_end = 7480