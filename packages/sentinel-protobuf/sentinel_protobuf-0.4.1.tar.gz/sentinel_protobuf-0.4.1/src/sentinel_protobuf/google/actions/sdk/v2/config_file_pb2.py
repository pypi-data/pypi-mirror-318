"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_runtime_version.ValidateProtobufRuntimeVersion(_runtime_version.Domain.PUBLIC, 5, 28, 1, '', 'google/actions/sdk/v2/config_file.proto')
_sym_db = _symbol_database.Default()
from .....google.actions.sdk.v2 import account_linking_secret_pb2 as google_dot_actions_dot_sdk_dot_v2_dot_account__linking__secret__pb2
from .....google.actions.sdk.v2 import action_pb2 as google_dot_actions_dot_sdk_dot_v2_dot_action__pb2
from .....google.actions.sdk.v2.interactionmodel import entity_set_pb2 as google_dot_actions_dot_sdk_dot_v2_dot_interactionmodel_dot_entity__set__pb2
from .....google.actions.sdk.v2.interactionmodel import global_intent_event_pb2 as google_dot_actions_dot_sdk_dot_v2_dot_interactionmodel_dot_global__intent__event__pb2
from .....google.actions.sdk.v2.interactionmodel import intent_pb2 as google_dot_actions_dot_sdk_dot_v2_dot_interactionmodel_dot_intent__pb2
from .....google.actions.sdk.v2.interactionmodel.prompt import static_prompt_pb2 as google_dot_actions_dot_sdk_dot_v2_dot_interactionmodel_dot_prompt_dot_static__prompt__pb2
from .....google.actions.sdk.v2.interactionmodel import scene_pb2 as google_dot_actions_dot_sdk_dot_v2_dot_interactionmodel_dot_scene__pb2
from .....google.actions.sdk.v2.interactionmodel.type import type_pb2 as google_dot_actions_dot_sdk_dot_v2_dot_interactionmodel_dot_type_dot_type__pb2
from .....google.actions.sdk.v2 import manifest_pb2 as google_dot_actions_dot_sdk_dot_v2_dot_manifest__pb2
from .....google.actions.sdk.v2 import settings_pb2 as google_dot_actions_dot_sdk_dot_v2_dot_settings__pb2
from .....google.actions.sdk.v2 import webhook_pb2 as google_dot_actions_dot_sdk_dot_v2_dot_webhook__pb2
from google.protobuf import struct_pb2 as google_dot_protobuf_dot_struct__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\'google/actions/sdk/v2/config_file.proto\x12\x15google.actions.sdk.v2\x1a2google/actions/sdk/v2/account_linking_secret.proto\x1a"google/actions/sdk/v2/action.proto\x1a7google/actions/sdk/v2/interactionmodel/entity_set.proto\x1a@google/actions/sdk/v2/interactionmodel/global_intent_event.proto\x1a3google/actions/sdk/v2/interactionmodel/intent.proto\x1aAgoogle/actions/sdk/v2/interactionmodel/prompt/static_prompt.proto\x1a2google/actions/sdk/v2/interactionmodel/scene.proto\x1a6google/actions/sdk/v2/interactionmodel/type/type.proto\x1a$google/actions/sdk/v2/manifest.proto\x1a$google/actions/sdk/v2/settings.proto\x1a#google/actions/sdk/v2/webhook.proto\x1a\x1cgoogle/protobuf/struct.proto"F\n\x0bConfigFiles\x127\n\x0cconfig_files\x18\x01 \x03(\x0b2!.google.actions.sdk.v2.ConfigFile"\xb8\x06\n\nConfigFile\x12\x11\n\tfile_path\x18\x01 \x01(\t\x123\n\x08manifest\x18\x02 \x01(\x0b2\x1f.google.actions.sdk.v2.ManifestH\x00\x121\n\x07actions\x18\x03 \x01(\x0b2\x1e.google.actions.sdk.v2.ActionsH\x00\x123\n\x08settings\x18\x04 \x01(\x0b2\x1f.google.actions.sdk.v2.SettingsH\x00\x121\n\x07webhook\x18\x06 \x01(\x0b2\x1e.google.actions.sdk.v2.WebhookH\x00\x12@\n\x06intent\x18\x07 \x01(\x0b2..google.actions.sdk.v2.interactionmodel.IntentH\x00\x12A\n\x04type\x18\x08 \x01(\x0b21.google.actions.sdk.v2.interactionmodel.type.TypeH\x00\x12G\n\nentity_set\x18\x0f \x01(\x0b21.google.actions.sdk.v2.interactionmodel.EntitySetH\x00\x12X\n\x13global_intent_event\x18\t \x01(\x0b29.google.actions.sdk.v2.interactionmodel.GlobalIntentEventH\x00\x12>\n\x05scene\x18\n \x01(\x0b2-.google.actions.sdk.v2.interactionmodel.SceneH\x00\x12T\n\rstatic_prompt\x18\x0b \x01(\x0b2;.google.actions.sdk.v2.interactionmodel.prompt.StaticPromptH\x00\x12M\n\x16account_linking_secret\x18\r \x01(\x0b2+.google.actions.sdk.v2.AccountLinkingSecretH\x00\x122\n\x0fresource_bundle\x18\x0c \x01(\x0b2\x17.google.protobuf.StructH\x00B\x06\n\x04fileBh\n\x19com.google.actions.sdk.v2B\x0fConfigFileProtoP\x01Z8google.golang.org/genproto/googleapis/actions/sdk/v2;sdkb\x06proto3')
_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'google.actions.sdk.v2.config_file_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
    _globals['DESCRIPTOR']._loaded_options = None
    _globals['DESCRIPTOR']._serialized_options = b'\n\x19com.google.actions.sdk.v2B\x0fConfigFileProtoP\x01Z8google.golang.org/genproto/googleapis/actions/sdk/v2;sdk'
    _globals['_CONFIGFILES']._serialized_start = 648
    _globals['_CONFIGFILES']._serialized_end = 718
    _globals['_CONFIGFILE']._serialized_start = 721
    _globals['_CONFIGFILE']._serialized_end = 1545