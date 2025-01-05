"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_runtime_version.ValidateProtobufRuntimeVersion(_runtime_version.Domain.PUBLIC, 5, 28, 1, '', 'google/actions/sdk/v2/interactionmodel/prompt/content/static_collection_prompt.proto')
_sym_db = _symbol_database.Default()
from ........google.actions.sdk.v2.interactionmodel.prompt.content import static_image_prompt_pb2 as google_dot_actions_dot_sdk_dot_v2_dot_interactionmodel_dot_prompt_dot_content_dot_static__image__prompt__pb2
from ........google.api import field_behavior_pb2 as google_dot_api_dot_field__behavior__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\nTgoogle/actions/sdk/v2/interactionmodel/prompt/content/static_collection_prompt.proto\x12-google.actions.sdk.v2.interactionmodel.prompt\x1aOgoogle/actions/sdk/v2/interactionmodel/prompt/content/static_image_prompt.proto\x1a\x1fgoogle/api/field_behavior.proto"\xbb\x03\n\x16StaticCollectionPrompt\x12\x12\n\x05title\x18\x01 \x01(\tB\x03\xe0A\x01\x12\x15\n\x08subtitle\x18\x02 \x01(\tB\x03\xe0A\x01\x12h\n\x05items\x18\x03 \x03(\x0b2T.google.actions.sdk.v2.interactionmodel.prompt.StaticCollectionPrompt.CollectionItemB\x03\xe0A\x02\x12c\n\nimage_fill\x18\x04 \x01(\x0e2J.google.actions.sdk.v2.interactionmodel.prompt.StaticImagePrompt.ImageFillB\x03\xe0A\x01\x1a\xa6\x01\n\x0eCollectionItem\x12\x10\n\x03key\x18\x01 \x01(\tB\x03\xe0A\x02\x12\x12\n\x05title\x18\x02 \x01(\tB\x03\xe0A\x02\x12\x18\n\x0bdescription\x18\x03 \x01(\tB\x03\xe0A\x01\x12T\n\x05image\x18\x04 \x01(\x0b2@.google.actions.sdk.v2.interactionmodel.prompt.StaticImagePromptB\x03\xe0A\x01B\xa7\x01\n1com.google.actions.sdk.v2.interactionmodel.promptB\x1bStaticCollectionPromptProtoP\x01ZSgoogle.golang.org/genproto/googleapis/actions/sdk/v2/interactionmodel/prompt;promptb\x06proto3')
_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'google.actions.sdk.v2.interactionmodel.prompt.content.static_collection_prompt_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
    _globals['DESCRIPTOR']._loaded_options = None
    _globals['DESCRIPTOR']._serialized_options = b'\n1com.google.actions.sdk.v2.interactionmodel.promptB\x1bStaticCollectionPromptProtoP\x01ZSgoogle.golang.org/genproto/googleapis/actions/sdk/v2/interactionmodel/prompt;prompt'
    _globals['_STATICCOLLECTIONPROMPT_COLLECTIONITEM'].fields_by_name['key']._loaded_options = None
    _globals['_STATICCOLLECTIONPROMPT_COLLECTIONITEM'].fields_by_name['key']._serialized_options = b'\xe0A\x02'
    _globals['_STATICCOLLECTIONPROMPT_COLLECTIONITEM'].fields_by_name['title']._loaded_options = None
    _globals['_STATICCOLLECTIONPROMPT_COLLECTIONITEM'].fields_by_name['title']._serialized_options = b'\xe0A\x02'
    _globals['_STATICCOLLECTIONPROMPT_COLLECTIONITEM'].fields_by_name['description']._loaded_options = None
    _globals['_STATICCOLLECTIONPROMPT_COLLECTIONITEM'].fields_by_name['description']._serialized_options = b'\xe0A\x01'
    _globals['_STATICCOLLECTIONPROMPT_COLLECTIONITEM'].fields_by_name['image']._loaded_options = None
    _globals['_STATICCOLLECTIONPROMPT_COLLECTIONITEM'].fields_by_name['image']._serialized_options = b'\xe0A\x01'
    _globals['_STATICCOLLECTIONPROMPT'].fields_by_name['title']._loaded_options = None
    _globals['_STATICCOLLECTIONPROMPT'].fields_by_name['title']._serialized_options = b'\xe0A\x01'
    _globals['_STATICCOLLECTIONPROMPT'].fields_by_name['subtitle']._loaded_options = None
    _globals['_STATICCOLLECTIONPROMPT'].fields_by_name['subtitle']._serialized_options = b'\xe0A\x01'
    _globals['_STATICCOLLECTIONPROMPT'].fields_by_name['items']._loaded_options = None
    _globals['_STATICCOLLECTIONPROMPT'].fields_by_name['items']._serialized_options = b'\xe0A\x02'
    _globals['_STATICCOLLECTIONPROMPT'].fields_by_name['image_fill']._loaded_options = None
    _globals['_STATICCOLLECTIONPROMPT'].fields_by_name['image_fill']._serialized_options = b'\xe0A\x01'
    _globals['_STATICCOLLECTIONPROMPT']._serialized_start = 250
    _globals['_STATICCOLLECTIONPROMPT']._serialized_end = 693
    _globals['_STATICCOLLECTIONPROMPT_COLLECTIONITEM']._serialized_start = 527
    _globals['_STATICCOLLECTIONPROMPT_COLLECTIONITEM']._serialized_end = 693