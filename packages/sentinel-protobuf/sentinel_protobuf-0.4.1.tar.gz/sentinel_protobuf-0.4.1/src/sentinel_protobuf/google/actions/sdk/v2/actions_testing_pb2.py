"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_runtime_version.ValidateProtobufRuntimeVersion(_runtime_version.Domain.PUBLIC, 5, 28, 1, '', 'google/actions/sdk/v2/actions_testing.proto')
_sym_db = _symbol_database.Default()
from .....google.actions.sdk.v2.conversation import intent_pb2 as google_dot_actions_dot_sdk_dot_v2_dot_conversation_dot_intent__pb2
from .....google.actions.sdk.v2.conversation.prompt.content import canvas_pb2 as google_dot_actions_dot_sdk_dot_v2_dot_conversation_dot_prompt_dot_content_dot_canvas__pb2
from .....google.actions.sdk.v2.conversation.prompt import prompt_pb2 as google_dot_actions_dot_sdk_dot_v2_dot_conversation_dot_prompt_dot_prompt__pb2
from .....google.actions.sdk.v2 import event_logs_pb2 as google_dot_actions_dot_sdk_dot_v2_dot_event__logs__pb2
from .....google.api import annotations_pb2 as google_dot_api_dot_annotations__pb2
from .....google.api import client_pb2 as google_dot_api_dot_client__pb2
from .....google.api import field_behavior_pb2 as google_dot_api_dot_field__behavior__pb2
from google.protobuf import empty_pb2 as google_dot_protobuf_dot_empty__pb2
from .....google.type import latlng_pb2 as google_dot_type_dot_latlng__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n+google/actions/sdk/v2/actions_testing.proto\x12\x15google.actions.sdk.v2\x1a/google/actions/sdk/v2/conversation/intent.proto\x1a>google/actions/sdk/v2/conversation/prompt/content/canvas.proto\x1a6google/actions/sdk/v2/conversation/prompt/prompt.proto\x1a&google/actions/sdk/v2/event_logs.proto\x1a\x1cgoogle/api/annotations.proto\x1a\x17google/api/client.proto\x1a\x1fgoogle/api/field_behavior.proto\x1a\x1bgoogle/protobuf/empty.proto\x1a\x18google/type/latlng.proto"\xc9\x01\n\x16SendInteractionRequest\x12\x14\n\x07project\x18\x01 \x01(\tB\x03\xe0A\x02\x124\n\x05input\x18\x02 \x01(\x0b2 .google.actions.sdk.v2.UserInputB\x03\xe0A\x02\x12G\n\x11device_properties\x18\x03 \x01(\x0b2\'.google.actions.sdk.v2.DevicePropertiesB\x03\xe0A\x02\x12\x1a\n\x12conversation_token\x18\x04 \x01(\t"\xaa\x01\n\tUserInput\x12\r\n\x05query\x18\x01 \x01(\t\x128\n\x04type\x18\x02 \x01(\x0e2*.google.actions.sdk.v2.UserInput.InputType"T\n\tInputType\x12\x1a\n\x16INPUT_TYPE_UNSPECIFIED\x10\x00\x12\t\n\x05TOUCH\x10\x01\x12\t\n\x05VOICE\x10\x02\x12\x0c\n\x08KEYBOARD\x10\x03\x12\x07\n\x03URL\x10\x04"\x8f\x02\n\x10DeviceProperties\x12@\n\x07surface\x18\x01 \x01(\x0e2/.google.actions.sdk.v2.DeviceProperties.Surface\x121\n\x08location\x18\x02 \x01(\x0b2\x1f.google.actions.sdk.v2.Location\x12\x0e\n\x06locale\x18\x03 \x01(\t\x12\x11\n\ttime_zone\x18\x04 \x01(\t"c\n\x07Surface\x12\x17\n\x13SURFACE_UNSPECIFIED\x10\x00\x12\x0b\n\x07SPEAKER\x10\x01\x12\t\n\x05PHONE\x10\x02\x12\x08\n\x04ALLO\x10\x03\x12\x11\n\rSMART_DISPLAY\x10\x04\x12\n\n\x06KAI_OS\x10\x05"o\n\x08Location\x12(\n\x0bcoordinates\x18\x01 \x01(\x0b2\x13.google.type.LatLng\x12\x19\n\x11formatted_address\x18\x02 \x01(\t\x12\x10\n\x08zip_code\x18\x03 \x01(\t\x12\x0c\n\x04city\x18\x04 \x01(\t"\x9d\x01\n\x17SendInteractionResponse\x12-\n\x06output\x18\x01 \x01(\x0b2\x1d.google.actions.sdk.v2.Output\x127\n\x0bdiagnostics\x18\x02 \x01(\x0b2".google.actions.sdk.v2.Diagnostics\x12\x1a\n\x12conversation_token\x18\x03 \x01(\t"\xae\x01\n\x06Output\x12\x0c\n\x04text\x18\x01 \x01(\t\x12\x0e\n\x06speech\x18\x02 \x03(\t\x12:\n\x06canvas\x18\x03 \x01(\x0b2*.google.actions.sdk.v2.conversation.Canvas\x12J\n\x16actions_builder_prompt\x18\x04 \x01(\x0b2*.google.actions.sdk.v2.conversation.Prompt"T\n\x0bDiagnostics\x12E\n\x16actions_builder_events\x18\x01 \x03(\x0b2%.google.actions.sdk.v2.ExecutionEvent"T\n\x13MatchIntentsRequest\x12\x14\n\x07project\x18\x01 \x01(\tB\x03\xe0A\x02\x12\x12\n\x05query\x18\x02 \x01(\tB\x03\xe0A\x02\x12\x13\n\x06locale\x18\x03 \x01(\tB\x03\xe0A\x02"[\n\x14MatchIntentsResponse\x12C\n\x0fmatched_intents\x18\x01 \x03(\x0b2*.google.actions.sdk.v2.conversation.Intent"5\n"SetWebAndAppActivityControlRequest\x12\x0f\n\x07enabled\x18\x01 \x01(\x082\xaf\x04\n\x0eActionsTesting\x12\xa5\x01\n\x0fSendInteraction\x12-.google.actions.sdk.v2.SendInteractionRequest\x1a..google.actions.sdk.v2.SendInteractionResponse"3\x82\xd3\xe4\x93\x02-"(/v2/{project=projects/*}:sendInteraction:\x01*\x12\xb0\x01\n\x0cMatchIntents\x12*.google.actions.sdk.v2.MatchIntentsRequest\x1a+.google.actions.sdk.v2.MatchIntentsResponse"G\xdaA\x14project,query,locale\x82\xd3\xe4\x93\x02*"%/v2/{project=projects/*}:matchIntents:\x01*\x12\xa6\x01\n\x1bSetWebAndAppActivityControl\x129.google.actions.sdk.v2.SetWebAndAppActivityControlRequest\x1a\x16.google.protobuf.Empty"4\xdaA\x07enabled\x82\xd3\xe4\x93\x02$"\x1f/v2:setWebAndAppActivityControl:\x01*\x1a\x19\xcaA\x16actions.googleapis.comBl\n\x19com.google.actions.sdk.v2B\x13ActionsTestingProtoP\x01Z8google.golang.org/genproto/googleapis/actions/sdk/v2;sdkb\x06proto3')
_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'google.actions.sdk.v2.actions_testing_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
    _globals['DESCRIPTOR']._loaded_options = None
    _globals['DESCRIPTOR']._serialized_options = b'\n\x19com.google.actions.sdk.v2B\x13ActionsTestingProtoP\x01Z8google.golang.org/genproto/googleapis/actions/sdk/v2;sdk'
    _globals['_SENDINTERACTIONREQUEST'].fields_by_name['project']._loaded_options = None
    _globals['_SENDINTERACTIONREQUEST'].fields_by_name['project']._serialized_options = b'\xe0A\x02'
    _globals['_SENDINTERACTIONREQUEST'].fields_by_name['input']._loaded_options = None
    _globals['_SENDINTERACTIONREQUEST'].fields_by_name['input']._serialized_options = b'\xe0A\x02'
    _globals['_SENDINTERACTIONREQUEST'].fields_by_name['device_properties']._loaded_options = None
    _globals['_SENDINTERACTIONREQUEST'].fields_by_name['device_properties']._serialized_options = b'\xe0A\x02'
    _globals['_MATCHINTENTSREQUEST'].fields_by_name['project']._loaded_options = None
    _globals['_MATCHINTENTSREQUEST'].fields_by_name['project']._serialized_options = b'\xe0A\x02'
    _globals['_MATCHINTENTSREQUEST'].fields_by_name['query']._loaded_options = None
    _globals['_MATCHINTENTSREQUEST'].fields_by_name['query']._serialized_options = b'\xe0A\x02'
    _globals['_MATCHINTENTSREQUEST'].fields_by_name['locale']._loaded_options = None
    _globals['_MATCHINTENTSREQUEST'].fields_by_name['locale']._serialized_options = b'\xe0A\x02'
    _globals['_ACTIONSTESTING']._loaded_options = None
    _globals['_ACTIONSTESTING']._serialized_options = b'\xcaA\x16actions.googleapis.com'
    _globals['_ACTIONSTESTING'].methods_by_name['SendInteraction']._loaded_options = None
    _globals['_ACTIONSTESTING'].methods_by_name['SendInteraction']._serialized_options = b'\x82\xd3\xe4\x93\x02-"(/v2/{project=projects/*}:sendInteraction:\x01*'
    _globals['_ACTIONSTESTING'].methods_by_name['MatchIntents']._loaded_options = None
    _globals['_ACTIONSTESTING'].methods_by_name['MatchIntents']._serialized_options = b'\xdaA\x14project,query,locale\x82\xd3\xe4\x93\x02*"%/v2/{project=projects/*}:matchIntents:\x01*'
    _globals['_ACTIONSTESTING'].methods_by_name['SetWebAndAppActivityControl']._loaded_options = None
    _globals['_ACTIONSTESTING'].methods_by_name['SetWebAndAppActivityControl']._serialized_options = b'\xdaA\x07enabled\x82\xd3\xe4\x93\x02$"\x1f/v2:setWebAndAppActivityControl:\x01*'
    _globals['_SENDINTERACTIONREQUEST']._serialized_start = 423
    _globals['_SENDINTERACTIONREQUEST']._serialized_end = 624
    _globals['_USERINPUT']._serialized_start = 627
    _globals['_USERINPUT']._serialized_end = 797
    _globals['_USERINPUT_INPUTTYPE']._serialized_start = 713
    _globals['_USERINPUT_INPUTTYPE']._serialized_end = 797
    _globals['_DEVICEPROPERTIES']._serialized_start = 800
    _globals['_DEVICEPROPERTIES']._serialized_end = 1071
    _globals['_DEVICEPROPERTIES_SURFACE']._serialized_start = 972
    _globals['_DEVICEPROPERTIES_SURFACE']._serialized_end = 1071
    _globals['_LOCATION']._serialized_start = 1073
    _globals['_LOCATION']._serialized_end = 1184
    _globals['_SENDINTERACTIONRESPONSE']._serialized_start = 1187
    _globals['_SENDINTERACTIONRESPONSE']._serialized_end = 1344
    _globals['_OUTPUT']._serialized_start = 1347
    _globals['_OUTPUT']._serialized_end = 1521
    _globals['_DIAGNOSTICS']._serialized_start = 1523
    _globals['_DIAGNOSTICS']._serialized_end = 1607
    _globals['_MATCHINTENTSREQUEST']._serialized_start = 1609
    _globals['_MATCHINTENTSREQUEST']._serialized_end = 1693
    _globals['_MATCHINTENTSRESPONSE']._serialized_start = 1695
    _globals['_MATCHINTENTSRESPONSE']._serialized_end = 1786
    _globals['_SETWEBANDAPPACTIVITYCONTROLREQUEST']._serialized_start = 1788
    _globals['_SETWEBANDAPPACTIVITYCONTROLREQUEST']._serialized_end = 1841
    _globals['_ACTIONSTESTING']._serialized_start = 1844
    _globals['_ACTIONSTESTING']._serialized_end = 2403