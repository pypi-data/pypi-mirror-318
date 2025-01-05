"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_runtime_version.ValidateProtobufRuntimeVersion(_runtime_version.Domain.PUBLIC, 5, 28, 1, '', 'google/actions/sdk/v2/interactionmodel/intent.proto')
_sym_db = _symbol_database.Default()
from ......google.actions.sdk.v2.interactionmodel.type import class_reference_pb2 as google_dot_actions_dot_sdk_dot_v2_dot_interactionmodel_dot_type_dot_class__reference__pb2
from ......google.api import field_behavior_pb2 as google_dot_api_dot_field__behavior__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n3google/actions/sdk/v2/interactionmodel/intent.proto\x12&google.actions.sdk.v2.interactionmodel\x1aAgoogle/actions/sdk/v2/interactionmodel/type/class_reference.proto\x1a\x1fgoogle/api/field_behavior.proto"\xce\x04\n\x06Intent\x12R\n\nparameters\x18\x01 \x03(\x0b2>.google.actions.sdk.v2.interactionmodel.Intent.IntentParameter\x12\x18\n\x10training_phrases\x18\x02 \x03(\t\x1a\xd5\x03\n\x0fIntentParameter\x12\x11\n\x04name\x18\x01 \x01(\tB\x03\xe0A\x02\x12P\n\x04type\x18\x02 \x01(\x0b2;.google.actions.sdk.v2.interactionmodel.type.ClassReferenceB\x03\xe0A\x01H\x00\x12x\n\x15entity_set_references\x18\x03 \x01(\x0b2R.google.actions.sdk.v2.interactionmodel.Intent.IntentParameter.EntitySetReferencesB\x03\xe0A\x01H\x00\x1a\xd0\x01\n\x13EntitySetReferences\x12\x89\x01\n\x15entity_set_references\x18\x01 \x03(\x0b2e.google.actions.sdk.v2.interactionmodel.Intent.IntentParameter.EntitySetReferences.EntitySetReferenceB\x03\xe0A\x02\x1a-\n\x12EntitySetReference\x12\x17\n\nentity_set\x18\x01 \x01(\tB\x03\xe0A\x02B\x10\n\x0eparameter_typeB\x93\x01\n*com.google.actions.sdk.v2.interactionmodelB\x0bIntentProtoP\x01ZVgoogle.golang.org/genproto/googleapis/actions/sdk/v2/interactionmodel;interactionmodelb\x06proto3')
_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'google.actions.sdk.v2.interactionmodel.intent_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
    _globals['DESCRIPTOR']._loaded_options = None
    _globals['DESCRIPTOR']._serialized_options = b'\n*com.google.actions.sdk.v2.interactionmodelB\x0bIntentProtoP\x01ZVgoogle.golang.org/genproto/googleapis/actions/sdk/v2/interactionmodel;interactionmodel'
    _globals['_INTENT_INTENTPARAMETER_ENTITYSETREFERENCES_ENTITYSETREFERENCE'].fields_by_name['entity_set']._loaded_options = None
    _globals['_INTENT_INTENTPARAMETER_ENTITYSETREFERENCES_ENTITYSETREFERENCE'].fields_by_name['entity_set']._serialized_options = b'\xe0A\x02'
    _globals['_INTENT_INTENTPARAMETER_ENTITYSETREFERENCES'].fields_by_name['entity_set_references']._loaded_options = None
    _globals['_INTENT_INTENTPARAMETER_ENTITYSETREFERENCES'].fields_by_name['entity_set_references']._serialized_options = b'\xe0A\x02'
    _globals['_INTENT_INTENTPARAMETER'].fields_by_name['name']._loaded_options = None
    _globals['_INTENT_INTENTPARAMETER'].fields_by_name['name']._serialized_options = b'\xe0A\x02'
    _globals['_INTENT_INTENTPARAMETER'].fields_by_name['type']._loaded_options = None
    _globals['_INTENT_INTENTPARAMETER'].fields_by_name['type']._serialized_options = b'\xe0A\x01'
    _globals['_INTENT_INTENTPARAMETER'].fields_by_name['entity_set_references']._loaded_options = None
    _globals['_INTENT_INTENTPARAMETER'].fields_by_name['entity_set_references']._serialized_options = b'\xe0A\x01'
    _globals['_INTENT']._serialized_start = 196
    _globals['_INTENT']._serialized_end = 786
    _globals['_INTENT_INTENTPARAMETER']._serialized_start = 317
    _globals['_INTENT_INTENTPARAMETER']._serialized_end = 786
    _globals['_INTENT_INTENTPARAMETER_ENTITYSETREFERENCES']._serialized_start = 560
    _globals['_INTENT_INTENTPARAMETER_ENTITYSETREFERENCES']._serialized_end = 768
    _globals['_INTENT_INTENTPARAMETER_ENTITYSETREFERENCES_ENTITYSETREFERENCE']._serialized_start = 723
    _globals['_INTENT_INTENTPARAMETER_ENTITYSETREFERENCES_ENTITYSETREFERENCE']._serialized_end = 768