"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_runtime_version.ValidateProtobufRuntimeVersion(_runtime_version.Domain.PUBLIC, 5, 28, 1, '', 'google/actions/sdk/v2/interactionmodel/prompt/static_prompt.proto')
_sym_db = _symbol_database.Default()
from .......google.actions.sdk.v2.interactionmodel.prompt.content import static_canvas_prompt_pb2 as google_dot_actions_dot_sdk_dot_v2_dot_interactionmodel_dot_prompt_dot_content_dot_static__canvas__prompt__pb2
from .......google.actions.sdk.v2.interactionmodel.prompt.content import static_content_prompt_pb2 as google_dot_actions_dot_sdk_dot_v2_dot_interactionmodel_dot_prompt_dot_content_dot_static__content__prompt__pb2
from .......google.actions.sdk.v2.interactionmodel.prompt.content import static_link_prompt_pb2 as google_dot_actions_dot_sdk_dot_v2_dot_interactionmodel_dot_prompt_dot_content_dot_static__link__prompt__pb2
from .......google.actions.sdk.v2.interactionmodel.prompt import static_simple_prompt_pb2 as google_dot_actions_dot_sdk_dot_v2_dot_interactionmodel_dot_prompt_dot_static__simple__prompt__pb2
from .......google.actions.sdk.v2.interactionmodel.prompt import suggestion_pb2 as google_dot_actions_dot_sdk_dot_v2_dot_interactionmodel_dot_prompt_dot_suggestion__pb2
from .......google.actions.sdk.v2.interactionmodel.prompt import surface_capabilities_pb2 as google_dot_actions_dot_sdk_dot_v2_dot_interactionmodel_dot_prompt_dot_surface__capabilities__pb2
from .......google.api import field_behavior_pb2 as google_dot_api_dot_field__behavior__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\nAgoogle/actions/sdk/v2/interactionmodel/prompt/static_prompt.proto\x12-google.actions.sdk.v2.interactionmodel.prompt\x1aPgoogle/actions/sdk/v2/interactionmodel/prompt/content/static_canvas_prompt.proto\x1aQgoogle/actions/sdk/v2/interactionmodel/prompt/content/static_content_prompt.proto\x1aNgoogle/actions/sdk/v2/interactionmodel/prompt/content/static_link_prompt.proto\x1aHgoogle/actions/sdk/v2/interactionmodel/prompt/static_simple_prompt.proto\x1a>google/actions/sdk/v2/interactionmodel/prompt/suggestion.proto\x1aHgoogle/actions/sdk/v2/interactionmodel/prompt/surface_capabilities.proto\x1a\x1fgoogle/api/field_behavior.proto"\x9c\x08\n\x0cStaticPrompt\x12e\n\ncandidates\x18\x01 \x03(\x0b2Q.google.actions.sdk.v2.interactionmodel.prompt.StaticPrompt.StaticPromptCandidate\x1a\xb6\x06\n\x15StaticPromptCandidate\x12[\n\x08selector\x18\x01 \x01(\x0b2D.google.actions.sdk.v2.interactionmodel.prompt.StaticPrompt.SelectorB\x03\xe0A\x01\x12\x7f\n\x0fprompt_response\x18\x02 \x01(\x0b2f.google.actions.sdk.v2.interactionmodel.prompt.StaticPrompt.StaticPromptCandidate.StaticPromptResponse\x1a\xbe\x04\n\x14StaticPromptResponse\x12\\\n\x0cfirst_simple\x18\x02 \x01(\x0b2A.google.actions.sdk.v2.interactionmodel.prompt.StaticSimplePromptB\x03\xe0A\x01\x12X\n\x07content\x18\x03 \x01(\x0b2B.google.actions.sdk.v2.interactionmodel.prompt.StaticContentPromptB\x03\xe0A\x01\x12[\n\x0blast_simple\x18\x04 \x01(\x0b2A.google.actions.sdk.v2.interactionmodel.prompt.StaticSimplePromptB\x03\xe0A\x01\x12S\n\x0bsuggestions\x18\x05 \x03(\x0b29.google.actions.sdk.v2.interactionmodel.prompt.SuggestionB\x03\xe0A\x01\x12R\n\x04link\x18\x06 \x01(\x0b2?.google.actions.sdk.v2.interactionmodel.prompt.StaticLinkPromptB\x03\xe0A\x01\x12\x15\n\x08override\x18\x07 \x01(\x08B\x03\xe0A\x01\x12Q\n\x06canvas\x18\x08 \x01(\x0b2A.google.actions.sdk.v2.interactionmodel.prompt.StaticCanvasPrompt\x1al\n\x08Selector\x12`\n\x14surface_capabilities\x18\x01 \x01(\x0b2B.google.actions.sdk.v2.interactionmodel.prompt.SurfaceCapabilitiesB\x9d\x01\n1com.google.actions.sdk.v2.interactionmodel.promptB\x11StaticPromptProtoP\x01ZSgoogle.golang.org/genproto/googleapis/actions/sdk/v2/interactionmodel/prompt;promptb\x06proto3')
_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'google.actions.sdk.v2.interactionmodel.prompt.static_prompt_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
    _globals['DESCRIPTOR']._loaded_options = None
    _globals['DESCRIPTOR']._serialized_options = b'\n1com.google.actions.sdk.v2.interactionmodel.promptB\x11StaticPromptProtoP\x01ZSgoogle.golang.org/genproto/googleapis/actions/sdk/v2/interactionmodel/prompt;prompt'
    _globals['_STATICPROMPT_STATICPROMPTCANDIDATE_STATICPROMPTRESPONSE'].fields_by_name['first_simple']._loaded_options = None
    _globals['_STATICPROMPT_STATICPROMPTCANDIDATE_STATICPROMPTRESPONSE'].fields_by_name['first_simple']._serialized_options = b'\xe0A\x01'
    _globals['_STATICPROMPT_STATICPROMPTCANDIDATE_STATICPROMPTRESPONSE'].fields_by_name['content']._loaded_options = None
    _globals['_STATICPROMPT_STATICPROMPTCANDIDATE_STATICPROMPTRESPONSE'].fields_by_name['content']._serialized_options = b'\xe0A\x01'
    _globals['_STATICPROMPT_STATICPROMPTCANDIDATE_STATICPROMPTRESPONSE'].fields_by_name['last_simple']._loaded_options = None
    _globals['_STATICPROMPT_STATICPROMPTCANDIDATE_STATICPROMPTRESPONSE'].fields_by_name['last_simple']._serialized_options = b'\xe0A\x01'
    _globals['_STATICPROMPT_STATICPROMPTCANDIDATE_STATICPROMPTRESPONSE'].fields_by_name['suggestions']._loaded_options = None
    _globals['_STATICPROMPT_STATICPROMPTCANDIDATE_STATICPROMPTRESPONSE'].fields_by_name['suggestions']._serialized_options = b'\xe0A\x01'
    _globals['_STATICPROMPT_STATICPROMPTCANDIDATE_STATICPROMPTRESPONSE'].fields_by_name['link']._loaded_options = None
    _globals['_STATICPROMPT_STATICPROMPTCANDIDATE_STATICPROMPTRESPONSE'].fields_by_name['link']._serialized_options = b'\xe0A\x01'
    _globals['_STATICPROMPT_STATICPROMPTCANDIDATE_STATICPROMPTRESPONSE'].fields_by_name['override']._loaded_options = None
    _globals['_STATICPROMPT_STATICPROMPTCANDIDATE_STATICPROMPTRESPONSE'].fields_by_name['override']._serialized_options = b'\xe0A\x01'
    _globals['_STATICPROMPT_STATICPROMPTCANDIDATE'].fields_by_name['selector']._loaded_options = None
    _globals['_STATICPROMPT_STATICPROMPTCANDIDATE'].fields_by_name['selector']._serialized_options = b'\xe0A\x01'
    _globals['_STATICPROMPT']._serialized_start = 607
    _globals['_STATICPROMPT']._serialized_end = 1659
    _globals['_STATICPROMPT_STATICPROMPTCANDIDATE']._serialized_start = 727
    _globals['_STATICPROMPT_STATICPROMPTCANDIDATE']._serialized_end = 1549
    _globals['_STATICPROMPT_STATICPROMPTCANDIDATE_STATICPROMPTRESPONSE']._serialized_start = 975
    _globals['_STATICPROMPT_STATICPROMPTCANDIDATE_STATICPROMPTRESPONSE']._serialized_end = 1549
    _globals['_STATICPROMPT_SELECTOR']._serialized_start = 1551
    _globals['_STATICPROMPT_SELECTOR']._serialized_end = 1659