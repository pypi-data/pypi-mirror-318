"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_runtime_version.ValidateProtobufRuntimeVersion(_runtime_version.Domain.PUBLIC, 5, 28, 1, '', 'google/actions/sdk/v2/action.proto')
_sym_db = _symbol_database.Default()
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n"google/actions/sdk/v2/action.proto\x12\x15google.actions.sdk.v2"\xcc\x05\n\x07Actions\x12:\n\x06custom\x18\x03 \x03(\x0b2*.google.actions.sdk.v2.Actions.CustomEntry\x1a\xd9\x03\n\nEngagement\x12\r\n\x05title\x18\x01 \x01(\t\x12U\n\x11push_notification\x18\x02 \x01(\x0b2:.google.actions.sdk.v2.Actions.Engagement.PushNotification\x12M\n\x0cdaily_update\x18\x03 \x01(\x0b25.google.actions.sdk.v2.Actions.Engagement.DailyUpdateH\x00\x12M\n\x0baction_link\x18\x04 \x01(\x0b24.google.actions.sdk.v2.Actions.Engagement.ActionLinkB\x02\x18\x01\x12O\n\x0eassistant_link\x18\x06 \x01(\x0b27.google.actions.sdk.v2.Actions.Engagement.AssistantLink\x1a\x12\n\x10PushNotification\x1a\r\n\x0bDailyUpdate\x1a\x1f\n\nActionLink\x12\r\n\x05title\x18\x01 \x01(\t:\x02\x18\x01\x1a\x1e\n\rAssistantLink\x12\r\n\x05title\x18\x01 \x01(\tB\x12\n\x10recurring_update\x1aM\n\x0cCustomAction\x12=\n\nengagement\x18\x02 \x01(\x0b2).google.actions.sdk.v2.Actions.Engagement\x1aZ\n\x0bCustomEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12:\n\x05value\x18\x02 \x01(\x0b2+.google.actions.sdk.v2.Actions.CustomAction:\x028\x01Bd\n\x19com.google.actions.sdk.v2B\x0bActionProtoP\x01Z8google.golang.org/genproto/googleapis/actions/sdk/v2;sdkb\x06proto3')
_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'google.actions.sdk.v2.action_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
    _globals['DESCRIPTOR']._loaded_options = None
    _globals['DESCRIPTOR']._serialized_options = b'\n\x19com.google.actions.sdk.v2B\x0bActionProtoP\x01Z8google.golang.org/genproto/googleapis/actions/sdk/v2;sdk'
    _globals['_ACTIONS_ENGAGEMENT_ACTIONLINK']._loaded_options = None
    _globals['_ACTIONS_ENGAGEMENT_ACTIONLINK']._serialized_options = b'\x18\x01'
    _globals['_ACTIONS_ENGAGEMENT'].fields_by_name['action_link']._loaded_options = None
    _globals['_ACTIONS_ENGAGEMENT'].fields_by_name['action_link']._serialized_options = b'\x18\x01'
    _globals['_ACTIONS_CUSTOMENTRY']._loaded_options = None
    _globals['_ACTIONS_CUSTOMENTRY']._serialized_options = b'8\x01'
    _globals['_ACTIONS']._serialized_start = 62
    _globals['_ACTIONS']._serialized_end = 778
    _globals['_ACTIONS_ENGAGEMENT']._serialized_start = 134
    _globals['_ACTIONS_ENGAGEMENT']._serialized_end = 607
    _globals['_ACTIONS_ENGAGEMENT_PUSHNOTIFICATION']._serialized_start = 489
    _globals['_ACTIONS_ENGAGEMENT_PUSHNOTIFICATION']._serialized_end = 507
    _globals['_ACTIONS_ENGAGEMENT_DAILYUPDATE']._serialized_start = 509
    _globals['_ACTIONS_ENGAGEMENT_DAILYUPDATE']._serialized_end = 522
    _globals['_ACTIONS_ENGAGEMENT_ACTIONLINK']._serialized_start = 524
    _globals['_ACTIONS_ENGAGEMENT_ACTIONLINK']._serialized_end = 555
    _globals['_ACTIONS_ENGAGEMENT_ASSISTANTLINK']._serialized_start = 557
    _globals['_ACTIONS_ENGAGEMENT_ASSISTANTLINK']._serialized_end = 587
    _globals['_ACTIONS_CUSTOMACTION']._serialized_start = 609
    _globals['_ACTIONS_CUSTOMACTION']._serialized_end = 686
    _globals['_ACTIONS_CUSTOMENTRY']._serialized_start = 688
    _globals['_ACTIONS_CUSTOMENTRY']._serialized_end = 778