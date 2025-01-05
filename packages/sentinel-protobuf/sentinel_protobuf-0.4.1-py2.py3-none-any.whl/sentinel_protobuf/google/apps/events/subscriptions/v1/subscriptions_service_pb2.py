"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_runtime_version.ValidateProtobufRuntimeVersion(_runtime_version.Domain.PUBLIC, 5, 28, 1, '', 'google/apps/events/subscriptions/v1/subscriptions_service.proto')
_sym_db = _symbol_database.Default()
from ......google.api import annotations_pb2 as google_dot_api_dot_annotations__pb2
from ......google.api import client_pb2 as google_dot_api_dot_client__pb2
from ......google.api import field_behavior_pb2 as google_dot_api_dot_field__behavior__pb2
from ......google.api import resource_pb2 as google_dot_api_dot_resource__pb2
from ......google.apps.events.subscriptions.v1 import subscription_resource_pb2 as google_dot_apps_dot_events_dot_subscriptions_dot_v1_dot_subscription__resource__pb2
from ......google.longrunning import operations_pb2 as google_dot_longrunning_dot_operations__pb2
from google.protobuf import empty_pb2 as google_dot_protobuf_dot_empty__pb2
from google.protobuf import field_mask_pb2 as google_dot_protobuf_dot_field__mask__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n?google/apps/events/subscriptions/v1/subscriptions_service.proto\x12#google.apps.events.subscriptions.v1\x1a\x1cgoogle/api/annotations.proto\x1a\x17google/api/client.proto\x1a\x1fgoogle/api/field_behavior.proto\x1a\x19google/api/resource.proto\x1a?google/apps/events/subscriptions/v1/subscription_resource.proto\x1a#google/longrunning/operations.proto\x1a\x1bgoogle/protobuf/empty.proto\x1a google/protobuf/field_mask.proto"\x85\x01\n\x19CreateSubscriptionRequest\x12L\n\x0csubscription\x18\x01 \x01(\x0b21.google.apps.events.subscriptions.v1.SubscriptionB\x03\xe0A\x02\x12\x1a\n\rvalidate_only\x18\x02 \x01(\x08B\x03\xe0A\x01"\xa9\x01\n\x19DeleteSubscriptionRequest\x12A\n\x04name\x18\x01 \x01(\tB3\xe0A\x02\xfaA-\n+workspaceevents.googleapis.com/Subscription\x12\x1a\n\rvalidate_only\x18\x02 \x01(\x08B\x03\xe0A\x01\x12\x1a\n\rallow_missing\x18\x03 \x01(\x08B\x03\xe0A\x01\x12\x11\n\x04etag\x18\x04 \x01(\tB\x03\xe0A\x01"[\n\x16GetSubscriptionRequest\x12A\n\x04name\x18\x01 \x01(\tB3\xe0A\x02\xfaA-\n+workspaceevents.googleapis.com/Subscription"\xbb\x01\n\x19UpdateSubscriptionRequest\x12L\n\x0csubscription\x18\x01 \x01(\x0b21.google.apps.events.subscriptions.v1.SubscriptionB\x03\xe0A\x02\x124\n\x0bupdate_mask\x18\x02 \x01(\x0b2\x1a.google.protobuf.FieldMaskB\x03\xe0A\x01\x12\x1a\n\rvalidate_only\x18\x03 \x01(\x08B\x03\xe0A\x01"b\n\x1dReactivateSubscriptionRequest\x12A\n\x04name\x18\x01 \x01(\tB3\xe0A\x02\xfaA-\n+workspaceevents.googleapis.com/Subscription"`\n\x18ListSubscriptionsRequest\x12\x16\n\tpage_size\x18\x01 \x01(\x05B\x03\xe0A\x01\x12\x17\n\npage_token\x18\x02 \x01(\tB\x03\xe0A\x01\x12\x13\n\x06filter\x18\x03 \x01(\tB\x03\xe0A\x02"~\n\x19ListSubscriptionsResponse\x12H\n\rsubscriptions\x18\x01 \x03(\x0b21.google.apps.events.subscriptions.v1.Subscription\x12\x17\n\x0fnext_page_token\x18\x02 \x01(\t"\x1c\n\x1aUpdateSubscriptionMetadata"\x1c\n\x1aCreateSubscriptionMetadata"\x1c\n\x1aDeleteSubscriptionMetadata" \n\x1eReactivateSubscriptionMetadata2\xff\x0e\n\x14SubscriptionsService\x12\xd8\x01\n\x12CreateSubscription\x12>.google.apps.events.subscriptions.v1.CreateSubscriptionRequest\x1a\x1d.google.longrunning.Operation"c\xcaA*\n\x0cSubscription\x12\x1aCreateSubscriptionMetadata\xdaA\x0csubscription\x82\xd3\xe4\x93\x02!"\x11/v1/subscriptions:\x0csubscription\x12\xd4\x01\n\x12DeleteSubscription\x12>.google.apps.events.subscriptions.v1.DeleteSubscriptionRequest\x1a\x1d.google.longrunning.Operation"_\xcaA3\n\x15google.protobuf.Empty\x12\x1aDeleteSubscriptionMetadata\xdaA\x04name\x82\xd3\xe4\x93\x02\x1c*\x1a/v1/{name=subscriptions/*}\x12\xac\x01\n\x0fGetSubscription\x12;.google.apps.events.subscriptions.v1.GetSubscriptionRequest\x1a1.google.apps.events.subscriptions.v1.Subscription")\xdaA\x04name\x82\xd3\xe4\x93\x02\x1c\x12\x1a/v1/{name=subscriptions/*}\x12\xb6\x01\n\x11ListSubscriptions\x12=.google.apps.events.subscriptions.v1.ListSubscriptionsRequest\x1a>.google.apps.events.subscriptions.v1.ListSubscriptionsResponse""\xdaA\x06filter\x82\xd3\xe4\x93\x02\x13\x12\x11/v1/subscriptions\x12\xfb\x01\n\x12UpdateSubscription\x12>.google.apps.events.subscriptions.v1.UpdateSubscriptionRequest\x1a\x1d.google.longrunning.Operation"\x85\x01\xcaA*\n\x0cSubscription\x12\x1aUpdateSubscriptionMetadata\xdaA\x18subscription,update_mask\x82\xd3\xe4\x93\x0272\'/v1/{subscription.name=subscriptions/*}:\x0csubscription\x12\xe5\x01\n\x16ReactivateSubscription\x12B.google.apps.events.subscriptions.v1.ReactivateSubscriptionRequest\x1a\x1d.google.longrunning.Operation"h\xcaA.\n\x0cSubscription\x12\x1eReactivateSubscriptionMetadata\xdaA\x04name\x82\xd3\xe4\x93\x02*"%/v1/{name=subscriptions/*}:reactivate:\x01*\x1a\xe6\x04\xcaA\x1eworkspaceevents.googleapis.com\xd2A\xc1\x04https://www.googleapis.com/auth/chat.bot,https://www.googleapis.com/auth/chat.memberships,https://www.googleapis.com/auth/chat.memberships.readonly,https://www.googleapis.com/auth/chat.messages,https://www.googleapis.com/auth/chat.messages.reactions,https://www.googleapis.com/auth/chat.messages.reactions.readonly,https://www.googleapis.com/auth/chat.messages.readonly,https://www.googleapis.com/auth/chat.spaces,https://www.googleapis.com/auth/chat.spaces.readonly,https://www.googleapis.com/auth/meetings.space.created,https://www.googleapis.com/auth/meetings.space.readonlyB\x91\x02\n\'com.google.apps.events.subscriptions.v1B\x19SubscriptionsServiceProtoP\x01ZScloud.google.com/go/apps/events/subscriptions/apiv1/subscriptionspb;subscriptionspb\xaa\x02#Google.Apps.Events.Subscriptions.V1\xca\x02#Google\\Apps\\Events\\Subscriptions\\V1\xea\x02\'Google::Apps::Events::Subscriptions::V1b\x06proto3')
_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'google.apps.events.subscriptions.v1.subscriptions_service_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
    _globals['DESCRIPTOR']._loaded_options = None
    _globals['DESCRIPTOR']._serialized_options = b"\n'com.google.apps.events.subscriptions.v1B\x19SubscriptionsServiceProtoP\x01ZScloud.google.com/go/apps/events/subscriptions/apiv1/subscriptionspb;subscriptionspb\xaa\x02#Google.Apps.Events.Subscriptions.V1\xca\x02#Google\\Apps\\Events\\Subscriptions\\V1\xea\x02'Google::Apps::Events::Subscriptions::V1"
    _globals['_CREATESUBSCRIPTIONREQUEST'].fields_by_name['subscription']._loaded_options = None
    _globals['_CREATESUBSCRIPTIONREQUEST'].fields_by_name['subscription']._serialized_options = b'\xe0A\x02'
    _globals['_CREATESUBSCRIPTIONREQUEST'].fields_by_name['validate_only']._loaded_options = None
    _globals['_CREATESUBSCRIPTIONREQUEST'].fields_by_name['validate_only']._serialized_options = b'\xe0A\x01'
    _globals['_DELETESUBSCRIPTIONREQUEST'].fields_by_name['name']._loaded_options = None
    _globals['_DELETESUBSCRIPTIONREQUEST'].fields_by_name['name']._serialized_options = b'\xe0A\x02\xfaA-\n+workspaceevents.googleapis.com/Subscription'
    _globals['_DELETESUBSCRIPTIONREQUEST'].fields_by_name['validate_only']._loaded_options = None
    _globals['_DELETESUBSCRIPTIONREQUEST'].fields_by_name['validate_only']._serialized_options = b'\xe0A\x01'
    _globals['_DELETESUBSCRIPTIONREQUEST'].fields_by_name['allow_missing']._loaded_options = None
    _globals['_DELETESUBSCRIPTIONREQUEST'].fields_by_name['allow_missing']._serialized_options = b'\xe0A\x01'
    _globals['_DELETESUBSCRIPTIONREQUEST'].fields_by_name['etag']._loaded_options = None
    _globals['_DELETESUBSCRIPTIONREQUEST'].fields_by_name['etag']._serialized_options = b'\xe0A\x01'
    _globals['_GETSUBSCRIPTIONREQUEST'].fields_by_name['name']._loaded_options = None
    _globals['_GETSUBSCRIPTIONREQUEST'].fields_by_name['name']._serialized_options = b'\xe0A\x02\xfaA-\n+workspaceevents.googleapis.com/Subscription'
    _globals['_UPDATESUBSCRIPTIONREQUEST'].fields_by_name['subscription']._loaded_options = None
    _globals['_UPDATESUBSCRIPTIONREQUEST'].fields_by_name['subscription']._serialized_options = b'\xe0A\x02'
    _globals['_UPDATESUBSCRIPTIONREQUEST'].fields_by_name['update_mask']._loaded_options = None
    _globals['_UPDATESUBSCRIPTIONREQUEST'].fields_by_name['update_mask']._serialized_options = b'\xe0A\x01'
    _globals['_UPDATESUBSCRIPTIONREQUEST'].fields_by_name['validate_only']._loaded_options = None
    _globals['_UPDATESUBSCRIPTIONREQUEST'].fields_by_name['validate_only']._serialized_options = b'\xe0A\x01'
    _globals['_REACTIVATESUBSCRIPTIONREQUEST'].fields_by_name['name']._loaded_options = None
    _globals['_REACTIVATESUBSCRIPTIONREQUEST'].fields_by_name['name']._serialized_options = b'\xe0A\x02\xfaA-\n+workspaceevents.googleapis.com/Subscription'
    _globals['_LISTSUBSCRIPTIONSREQUEST'].fields_by_name['page_size']._loaded_options = None
    _globals['_LISTSUBSCRIPTIONSREQUEST'].fields_by_name['page_size']._serialized_options = b'\xe0A\x01'
    _globals['_LISTSUBSCRIPTIONSREQUEST'].fields_by_name['page_token']._loaded_options = None
    _globals['_LISTSUBSCRIPTIONSREQUEST'].fields_by_name['page_token']._serialized_options = b'\xe0A\x01'
    _globals['_LISTSUBSCRIPTIONSREQUEST'].fields_by_name['filter']._loaded_options = None
    _globals['_LISTSUBSCRIPTIONSREQUEST'].fields_by_name['filter']._serialized_options = b'\xe0A\x02'
    _globals['_SUBSCRIPTIONSSERVICE']._loaded_options = None
    _globals['_SUBSCRIPTIONSSERVICE']._serialized_options = b'\xcaA\x1eworkspaceevents.googleapis.com\xd2A\xc1\x04https://www.googleapis.com/auth/chat.bot,https://www.googleapis.com/auth/chat.memberships,https://www.googleapis.com/auth/chat.memberships.readonly,https://www.googleapis.com/auth/chat.messages,https://www.googleapis.com/auth/chat.messages.reactions,https://www.googleapis.com/auth/chat.messages.reactions.readonly,https://www.googleapis.com/auth/chat.messages.readonly,https://www.googleapis.com/auth/chat.spaces,https://www.googleapis.com/auth/chat.spaces.readonly,https://www.googleapis.com/auth/meetings.space.created,https://www.googleapis.com/auth/meetings.space.readonly'
    _globals['_SUBSCRIPTIONSSERVICE'].methods_by_name['CreateSubscription']._loaded_options = None
    _globals['_SUBSCRIPTIONSSERVICE'].methods_by_name['CreateSubscription']._serialized_options = b'\xcaA*\n\x0cSubscription\x12\x1aCreateSubscriptionMetadata\xdaA\x0csubscription\x82\xd3\xe4\x93\x02!"\x11/v1/subscriptions:\x0csubscription'
    _globals['_SUBSCRIPTIONSSERVICE'].methods_by_name['DeleteSubscription']._loaded_options = None
    _globals['_SUBSCRIPTIONSSERVICE'].methods_by_name['DeleteSubscription']._serialized_options = b'\xcaA3\n\x15google.protobuf.Empty\x12\x1aDeleteSubscriptionMetadata\xdaA\x04name\x82\xd3\xe4\x93\x02\x1c*\x1a/v1/{name=subscriptions/*}'
    _globals['_SUBSCRIPTIONSSERVICE'].methods_by_name['GetSubscription']._loaded_options = None
    _globals['_SUBSCRIPTIONSSERVICE'].methods_by_name['GetSubscription']._serialized_options = b'\xdaA\x04name\x82\xd3\xe4\x93\x02\x1c\x12\x1a/v1/{name=subscriptions/*}'
    _globals['_SUBSCRIPTIONSSERVICE'].methods_by_name['ListSubscriptions']._loaded_options = None
    _globals['_SUBSCRIPTIONSSERVICE'].methods_by_name['ListSubscriptions']._serialized_options = b'\xdaA\x06filter\x82\xd3\xe4\x93\x02\x13\x12\x11/v1/subscriptions'
    _globals['_SUBSCRIPTIONSSERVICE'].methods_by_name['UpdateSubscription']._loaded_options = None
    _globals['_SUBSCRIPTIONSSERVICE'].methods_by_name['UpdateSubscription']._serialized_options = b"\xcaA*\n\x0cSubscription\x12\x1aUpdateSubscriptionMetadata\xdaA\x18subscription,update_mask\x82\xd3\xe4\x93\x0272'/v1/{subscription.name=subscriptions/*}:\x0csubscription"
    _globals['_SUBSCRIPTIONSSERVICE'].methods_by_name['ReactivateSubscription']._loaded_options = None
    _globals['_SUBSCRIPTIONSSERVICE'].methods_by_name['ReactivateSubscription']._serialized_options = b'\xcaA.\n\x0cSubscription\x12\x1eReactivateSubscriptionMetadata\xdaA\x04name\x82\xd3\xe4\x93\x02*"%/v1/{name=subscriptions/*}:reactivate:\x01*'
    _globals['_CREATESUBSCRIPTIONREQUEST']._serialized_start = 385
    _globals['_CREATESUBSCRIPTIONREQUEST']._serialized_end = 518
    _globals['_DELETESUBSCRIPTIONREQUEST']._serialized_start = 521
    _globals['_DELETESUBSCRIPTIONREQUEST']._serialized_end = 690
    _globals['_GETSUBSCRIPTIONREQUEST']._serialized_start = 692
    _globals['_GETSUBSCRIPTIONREQUEST']._serialized_end = 783
    _globals['_UPDATESUBSCRIPTIONREQUEST']._serialized_start = 786
    _globals['_UPDATESUBSCRIPTIONREQUEST']._serialized_end = 973
    _globals['_REACTIVATESUBSCRIPTIONREQUEST']._serialized_start = 975
    _globals['_REACTIVATESUBSCRIPTIONREQUEST']._serialized_end = 1073
    _globals['_LISTSUBSCRIPTIONSREQUEST']._serialized_start = 1075
    _globals['_LISTSUBSCRIPTIONSREQUEST']._serialized_end = 1171
    _globals['_LISTSUBSCRIPTIONSRESPONSE']._serialized_start = 1173
    _globals['_LISTSUBSCRIPTIONSRESPONSE']._serialized_end = 1299
    _globals['_UPDATESUBSCRIPTIONMETADATA']._serialized_start = 1301
    _globals['_UPDATESUBSCRIPTIONMETADATA']._serialized_end = 1329
    _globals['_CREATESUBSCRIPTIONMETADATA']._serialized_start = 1331
    _globals['_CREATESUBSCRIPTIONMETADATA']._serialized_end = 1359
    _globals['_DELETESUBSCRIPTIONMETADATA']._serialized_start = 1361
    _globals['_DELETESUBSCRIPTIONMETADATA']._serialized_end = 1389
    _globals['_REACTIVATESUBSCRIPTIONMETADATA']._serialized_start = 1391
    _globals['_REACTIVATESUBSCRIPTIONMETADATA']._serialized_end = 1423
    _globals['_SUBSCRIPTIONSSERVICE']._serialized_start = 1426
    _globals['_SUBSCRIPTIONSSERVICE']._serialized_end = 3345