"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_runtime_version.ValidateProtobufRuntimeVersion(_runtime_version.Domain.PUBLIC, 5, 28, 1, '', 'google/actions/sdk/v2/interactionmodel/prompt/content/static_link_prompt.proto')
_sym_db = _symbol_database.Default()
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\nNgoogle/actions/sdk/v2/interactionmodel/prompt/content/static_link_prompt.proto\x12-google.actions.sdk.v2.interactionmodel.prompt"f\n\x10StaticLinkPrompt\x12\x0c\n\x04name\x18\x01 \x01(\t\x12D\n\x04open\x18\x02 \x01(\x0b26.google.actions.sdk.v2.interactionmodel.prompt.OpenUrl"\\\n\x07OpenUrl\x12\x0b\n\x03url\x18\x01 \x01(\t\x12D\n\x04hint\x18\x02 \x01(\x0e26.google.actions.sdk.v2.interactionmodel.prompt.UrlHint*(\n\x07UrlHint\x12\x14\n\x10HINT_UNSPECIFIED\x10\x00\x12\x07\n\x03AMP\x10\x01B\xa1\x01\n1com.google.actions.sdk.v2.interactionmodel.promptB\x15StaticLinkPromptProtoP\x01ZSgoogle.golang.org/genproto/googleapis/actions/sdk/v2/interactionmodel/prompt;promptb\x06proto3')
_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'google.actions.sdk.v2.interactionmodel.prompt.content.static_link_prompt_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
    _globals['DESCRIPTOR']._loaded_options = None
    _globals['DESCRIPTOR']._serialized_options = b'\n1com.google.actions.sdk.v2.interactionmodel.promptB\x15StaticLinkPromptProtoP\x01ZSgoogle.golang.org/genproto/googleapis/actions/sdk/v2/interactionmodel/prompt;prompt'
    _globals['_URLHINT']._serialized_start = 327
    _globals['_URLHINT']._serialized_end = 367
    _globals['_STATICLINKPROMPT']._serialized_start = 129
    _globals['_STATICLINKPROMPT']._serialized_end = 231
    _globals['_OPENURL']._serialized_start = 233
    _globals['_OPENURL']._serialized_end = 325