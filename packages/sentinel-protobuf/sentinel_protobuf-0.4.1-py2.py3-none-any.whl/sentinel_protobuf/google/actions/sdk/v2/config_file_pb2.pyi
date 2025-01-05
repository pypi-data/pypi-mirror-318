from google.actions.sdk.v2 import account_linking_secret_pb2 as _account_linking_secret_pb2
from google.actions.sdk.v2 import action_pb2 as _action_pb2
from google.actions.sdk.v2.interactionmodel import entity_set_pb2 as _entity_set_pb2
from google.actions.sdk.v2.interactionmodel import global_intent_event_pb2 as _global_intent_event_pb2
from google.actions.sdk.v2.interactionmodel import intent_pb2 as _intent_pb2
from google.actions.sdk.v2.interactionmodel.prompt import static_prompt_pb2 as _static_prompt_pb2
from google.actions.sdk.v2.interactionmodel import scene_pb2 as _scene_pb2
from google.actions.sdk.v2.interactionmodel.type import type_pb2 as _type_pb2
from google.actions.sdk.v2 import manifest_pb2 as _manifest_pb2
from google.actions.sdk.v2 import settings_pb2 as _settings_pb2
from google.actions.sdk.v2 import webhook_pb2 as _webhook_pb2
from google.protobuf import struct_pb2 as _struct_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union
DESCRIPTOR: _descriptor.FileDescriptor

class ConfigFiles(_message.Message):
    __slots__ = ('config_files',)
    CONFIG_FILES_FIELD_NUMBER: _ClassVar[int]
    config_files: _containers.RepeatedCompositeFieldContainer[ConfigFile]

    def __init__(self, config_files: _Optional[_Iterable[_Union[ConfigFile, _Mapping]]]=...) -> None:
        ...

class ConfigFile(_message.Message):
    __slots__ = ('file_path', 'manifest', 'actions', 'settings', 'webhook', 'intent', 'type', 'entity_set', 'global_intent_event', 'scene', 'static_prompt', 'account_linking_secret', 'resource_bundle')
    FILE_PATH_FIELD_NUMBER: _ClassVar[int]
    MANIFEST_FIELD_NUMBER: _ClassVar[int]
    ACTIONS_FIELD_NUMBER: _ClassVar[int]
    SETTINGS_FIELD_NUMBER: _ClassVar[int]
    WEBHOOK_FIELD_NUMBER: _ClassVar[int]
    INTENT_FIELD_NUMBER: _ClassVar[int]
    TYPE_FIELD_NUMBER: _ClassVar[int]
    ENTITY_SET_FIELD_NUMBER: _ClassVar[int]
    GLOBAL_INTENT_EVENT_FIELD_NUMBER: _ClassVar[int]
    SCENE_FIELD_NUMBER: _ClassVar[int]
    STATIC_PROMPT_FIELD_NUMBER: _ClassVar[int]
    ACCOUNT_LINKING_SECRET_FIELD_NUMBER: _ClassVar[int]
    RESOURCE_BUNDLE_FIELD_NUMBER: _ClassVar[int]
    file_path: str
    manifest: _manifest_pb2.Manifest
    actions: _action_pb2.Actions
    settings: _settings_pb2.Settings
    webhook: _webhook_pb2.Webhook
    intent: _intent_pb2.Intent
    type: _type_pb2.Type
    entity_set: _entity_set_pb2.EntitySet
    global_intent_event: _global_intent_event_pb2.GlobalIntentEvent
    scene: _scene_pb2.Scene
    static_prompt: _static_prompt_pb2.StaticPrompt
    account_linking_secret: _account_linking_secret_pb2.AccountLinkingSecret
    resource_bundle: _struct_pb2.Struct

    def __init__(self, file_path: _Optional[str]=..., manifest: _Optional[_Union[_manifest_pb2.Manifest, _Mapping]]=..., actions: _Optional[_Union[_action_pb2.Actions, _Mapping]]=..., settings: _Optional[_Union[_settings_pb2.Settings, _Mapping]]=..., webhook: _Optional[_Union[_webhook_pb2.Webhook, _Mapping]]=..., intent: _Optional[_Union[_intent_pb2.Intent, _Mapping]]=..., type: _Optional[_Union[_type_pb2.Type, _Mapping]]=..., entity_set: _Optional[_Union[_entity_set_pb2.EntitySet, _Mapping]]=..., global_intent_event: _Optional[_Union[_global_intent_event_pb2.GlobalIntentEvent, _Mapping]]=..., scene: _Optional[_Union[_scene_pb2.Scene, _Mapping]]=..., static_prompt: _Optional[_Union[_static_prompt_pb2.StaticPrompt, _Mapping]]=..., account_linking_secret: _Optional[_Union[_account_linking_secret_pb2.AccountLinkingSecret, _Mapping]]=..., resource_bundle: _Optional[_Union[_struct_pb2.Struct, _Mapping]]=...) -> None:
        ...