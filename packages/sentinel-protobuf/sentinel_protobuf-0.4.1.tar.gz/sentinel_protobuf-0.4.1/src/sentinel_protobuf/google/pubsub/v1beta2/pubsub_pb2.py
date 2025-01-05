"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_runtime_version.ValidateProtobufRuntimeVersion(_runtime_version.Domain.PUBLIC, 5, 28, 1, '', 'google/pubsub/v1beta2/pubsub.proto')
_sym_db = _symbol_database.Default()
from google.protobuf import empty_pb2 as google_dot_protobuf_dot_empty__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n"google/pubsub/v1beta2/pubsub.proto\x12\x15google.pubsub.v1beta2\x1a\x1bgoogle/protobuf/empty.proto"\x15\n\x05Topic\x12\x0c\n\x04name\x18\x01 \x01(\t"\xae\x01\n\rPubsubMessage\x12\x0c\n\x04data\x18\x01 \x01(\x0c\x12H\n\nattributes\x18\x02 \x03(\x0b24.google.pubsub.v1beta2.PubsubMessage.AttributesEntry\x12\x12\n\nmessage_id\x18\x03 \x01(\t\x1a1\n\x0fAttributesEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\r\n\x05value\x18\x02 \x01(\t:\x028\x01" \n\x0fGetTopicRequest\x12\r\n\x05topic\x18\x01 \x01(\t"W\n\x0ePublishRequest\x12\r\n\x05topic\x18\x01 \x01(\t\x126\n\x08messages\x18\x02 \x03(\x0b2$.google.pubsub.v1beta2.PubsubMessage"&\n\x0fPublishResponse\x12\x13\n\x0bmessage_ids\x18\x01 \x03(\t"K\n\x11ListTopicsRequest\x12\x0f\n\x07project\x18\x01 \x01(\t\x12\x11\n\tpage_size\x18\x02 \x01(\x05\x12\x12\n\npage_token\x18\x03 \x01(\t"[\n\x12ListTopicsResponse\x12,\n\x06topics\x18\x01 \x03(\x0b2\x1c.google.pubsub.v1beta2.Topic\x12\x17\n\x0fnext_page_token\x18\x02 \x01(\t"U\n\x1dListTopicSubscriptionsRequest\x12\r\n\x05topic\x18\x01 \x01(\t\x12\x11\n\tpage_size\x18\x02 \x01(\x05\x12\x12\n\npage_token\x18\x03 \x01(\t"P\n\x1eListTopicSubscriptionsResponse\x12\x15\n\rsubscriptions\x18\x01 \x03(\t\x12\x17\n\x0fnext_page_token\x18\x02 \x01(\t"#\n\x12DeleteTopicRequest\x12\r\n\x05topic\x18\x01 \x01(\t"\x81\x01\n\x0cSubscription\x12\x0c\n\x04name\x18\x01 \x01(\t\x12\r\n\x05topic\x18\x02 \x01(\t\x126\n\x0bpush_config\x18\x04 \x01(\x0b2!.google.pubsub.v1beta2.PushConfig\x12\x1c\n\x14ack_deadline_seconds\x18\x05 \x01(\x05"\x9d\x01\n\nPushConfig\x12\x15\n\rpush_endpoint\x18\x01 \x01(\t\x12E\n\nattributes\x18\x02 \x03(\x0b21.google.pubsub.v1beta2.PushConfig.AttributesEntry\x1a1\n\x0fAttributesEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\r\n\x05value\x18\x02 \x01(\t:\x028\x01"X\n\x0fReceivedMessage\x12\x0e\n\x06ack_id\x18\x01 \x01(\t\x125\n\x07message\x18\x02 \x01(\x0b2$.google.pubsub.v1beta2.PubsubMessage".\n\x16GetSubscriptionRequest\x12\x14\n\x0csubscription\x18\x01 \x01(\t"R\n\x18ListSubscriptionsRequest\x12\x0f\n\x07project\x18\x01 \x01(\t\x12\x11\n\tpage_size\x18\x02 \x01(\x05\x12\x12\n\npage_token\x18\x03 \x01(\t"p\n\x19ListSubscriptionsResponse\x12:\n\rsubscriptions\x18\x01 \x03(\x0b2#.google.pubsub.v1beta2.Subscription\x12\x17\n\x0fnext_page_token\x18\x02 \x01(\t"1\n\x19DeleteSubscriptionRequest\x12\x14\n\x0csubscription\x18\x01 \x01(\t"g\n\x17ModifyPushConfigRequest\x12\x14\n\x0csubscription\x18\x01 \x01(\t\x126\n\x0bpush_config\x18\x02 \x01(\x0b2!.google.pubsub.v1beta2.PushConfig"U\n\x0bPullRequest\x12\x14\n\x0csubscription\x18\x01 \x01(\t\x12\x1a\n\x12return_immediately\x18\x02 \x01(\x08\x12\x14\n\x0cmax_messages\x18\x03 \x01(\x05"Q\n\x0cPullResponse\x12A\n\x11received_messages\x18\x01 \x03(\x0b2&.google.pubsub.v1beta2.ReceivedMessage"^\n\x18ModifyAckDeadlineRequest\x12\x14\n\x0csubscription\x18\x01 \x01(\t\x12\x0e\n\x06ack_id\x18\x02 \x01(\t\x12\x1c\n\x14ack_deadline_seconds\x18\x03 \x01(\x05";\n\x12AcknowledgeRequest\x12\x14\n\x0csubscription\x18\x01 \x01(\t\x12\x0f\n\x07ack_ids\x18\x02 \x03(\t2\x88\x06\n\nSubscriber\x12^\n\x12CreateSubscription\x12#.google.pubsub.v1beta2.Subscription\x1a#.google.pubsub.v1beta2.Subscription\x12e\n\x0fGetSubscription\x12-.google.pubsub.v1beta2.GetSubscriptionRequest\x1a#.google.pubsub.v1beta2.Subscription\x12v\n\x11ListSubscriptions\x12/.google.pubsub.v1beta2.ListSubscriptionsRequest\x1a0.google.pubsub.v1beta2.ListSubscriptionsResponse\x12^\n\x12DeleteSubscription\x120.google.pubsub.v1beta2.DeleteSubscriptionRequest\x1a\x16.google.protobuf.Empty\x12\\\n\x11ModifyAckDeadline\x12/.google.pubsub.v1beta2.ModifyAckDeadlineRequest\x1a\x16.google.protobuf.Empty\x12P\n\x0bAcknowledge\x12).google.pubsub.v1beta2.AcknowledgeRequest\x1a\x16.google.protobuf.Empty\x12O\n\x04Pull\x12".google.pubsub.v1beta2.PullRequest\x1a#.google.pubsub.v1beta2.PullResponse\x12Z\n\x10ModifyPushConfig\x12..google.pubsub.v1beta2.ModifyPushConfigRequest\x1a\x16.google.protobuf.Empty2\xbf\x04\n\tPublisher\x12I\n\x0bCreateTopic\x12\x1c.google.pubsub.v1beta2.Topic\x1a\x1c.google.pubsub.v1beta2.Topic\x12X\n\x07Publish\x12%.google.pubsub.v1beta2.PublishRequest\x1a&.google.pubsub.v1beta2.PublishResponse\x12P\n\x08GetTopic\x12&.google.pubsub.v1beta2.GetTopicRequest\x1a\x1c.google.pubsub.v1beta2.Topic\x12a\n\nListTopics\x12(.google.pubsub.v1beta2.ListTopicsRequest\x1a).google.pubsub.v1beta2.ListTopicsResponse\x12\x85\x01\n\x16ListTopicSubscriptions\x124.google.pubsub.v1beta2.ListTopicSubscriptionsRequest\x1a5.google.pubsub.v1beta2.ListTopicSubscriptionsResponse\x12P\n\x0bDeleteTopic\x12).google.pubsub.v1beta2.DeleteTopicRequest\x1a\x16.google.protobuf.EmptyBg\n\x19com.google.pubsub.v1beta2B\x0bPubsubProtoP\x01Z;google.golang.org/genproto/googleapis/pubsub/v1beta2;pubsubb\x06proto3')
_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'google.pubsub.v1beta2.pubsub_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
    _globals['DESCRIPTOR']._loaded_options = None
    _globals['DESCRIPTOR']._serialized_options = b'\n\x19com.google.pubsub.v1beta2B\x0bPubsubProtoP\x01Z;google.golang.org/genproto/googleapis/pubsub/v1beta2;pubsub'
    _globals['_PUBSUBMESSAGE_ATTRIBUTESENTRY']._loaded_options = None
    _globals['_PUBSUBMESSAGE_ATTRIBUTESENTRY']._serialized_options = b'8\x01'
    _globals['_PUSHCONFIG_ATTRIBUTESENTRY']._loaded_options = None
    _globals['_PUSHCONFIG_ATTRIBUTESENTRY']._serialized_options = b'8\x01'
    _globals['_TOPIC']._serialized_start = 90
    _globals['_TOPIC']._serialized_end = 111
    _globals['_PUBSUBMESSAGE']._serialized_start = 114
    _globals['_PUBSUBMESSAGE']._serialized_end = 288
    _globals['_PUBSUBMESSAGE_ATTRIBUTESENTRY']._serialized_start = 239
    _globals['_PUBSUBMESSAGE_ATTRIBUTESENTRY']._serialized_end = 288
    _globals['_GETTOPICREQUEST']._serialized_start = 290
    _globals['_GETTOPICREQUEST']._serialized_end = 322
    _globals['_PUBLISHREQUEST']._serialized_start = 324
    _globals['_PUBLISHREQUEST']._serialized_end = 411
    _globals['_PUBLISHRESPONSE']._serialized_start = 413
    _globals['_PUBLISHRESPONSE']._serialized_end = 451
    _globals['_LISTTOPICSREQUEST']._serialized_start = 453
    _globals['_LISTTOPICSREQUEST']._serialized_end = 528
    _globals['_LISTTOPICSRESPONSE']._serialized_start = 530
    _globals['_LISTTOPICSRESPONSE']._serialized_end = 621
    _globals['_LISTTOPICSUBSCRIPTIONSREQUEST']._serialized_start = 623
    _globals['_LISTTOPICSUBSCRIPTIONSREQUEST']._serialized_end = 708
    _globals['_LISTTOPICSUBSCRIPTIONSRESPONSE']._serialized_start = 710
    _globals['_LISTTOPICSUBSCRIPTIONSRESPONSE']._serialized_end = 790
    _globals['_DELETETOPICREQUEST']._serialized_start = 792
    _globals['_DELETETOPICREQUEST']._serialized_end = 827
    _globals['_SUBSCRIPTION']._serialized_start = 830
    _globals['_SUBSCRIPTION']._serialized_end = 959
    _globals['_PUSHCONFIG']._serialized_start = 962
    _globals['_PUSHCONFIG']._serialized_end = 1119
    _globals['_PUSHCONFIG_ATTRIBUTESENTRY']._serialized_start = 239
    _globals['_PUSHCONFIG_ATTRIBUTESENTRY']._serialized_end = 288
    _globals['_RECEIVEDMESSAGE']._serialized_start = 1121
    _globals['_RECEIVEDMESSAGE']._serialized_end = 1209
    _globals['_GETSUBSCRIPTIONREQUEST']._serialized_start = 1211
    _globals['_GETSUBSCRIPTIONREQUEST']._serialized_end = 1257
    _globals['_LISTSUBSCRIPTIONSREQUEST']._serialized_start = 1259
    _globals['_LISTSUBSCRIPTIONSREQUEST']._serialized_end = 1341
    _globals['_LISTSUBSCRIPTIONSRESPONSE']._serialized_start = 1343
    _globals['_LISTSUBSCRIPTIONSRESPONSE']._serialized_end = 1455
    _globals['_DELETESUBSCRIPTIONREQUEST']._serialized_start = 1457
    _globals['_DELETESUBSCRIPTIONREQUEST']._serialized_end = 1506
    _globals['_MODIFYPUSHCONFIGREQUEST']._serialized_start = 1508
    _globals['_MODIFYPUSHCONFIGREQUEST']._serialized_end = 1611
    _globals['_PULLREQUEST']._serialized_start = 1613
    _globals['_PULLREQUEST']._serialized_end = 1698
    _globals['_PULLRESPONSE']._serialized_start = 1700
    _globals['_PULLRESPONSE']._serialized_end = 1781
    _globals['_MODIFYACKDEADLINEREQUEST']._serialized_start = 1783
    _globals['_MODIFYACKDEADLINEREQUEST']._serialized_end = 1877
    _globals['_ACKNOWLEDGEREQUEST']._serialized_start = 1879
    _globals['_ACKNOWLEDGEREQUEST']._serialized_end = 1938
    _globals['_SUBSCRIBER']._serialized_start = 1941
    _globals['_SUBSCRIBER']._serialized_end = 2717
    _globals['_PUBLISHER']._serialized_start = 2720
    _globals['_PUBLISHER']._serialized_end = 3295