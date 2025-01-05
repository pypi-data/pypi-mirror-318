"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_runtime_version.ValidateProtobufRuntimeVersion(_runtime_version.Domain.PUBLIC, 5, 28, 1, '', 'google/actions/sdk/v2/interactionmodel/type/synonym_type.proto')
_sym_db = _symbol_database.Default()
from .......google.actions.sdk.v2.interactionmodel.type import entity_display_pb2 as google_dot_actions_dot_sdk_dot_v2_dot_interactionmodel_dot_type_dot_entity__display__pb2
from .......google.api import field_behavior_pb2 as google_dot_api_dot_field__behavior__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n>google/actions/sdk/v2/interactionmodel/type/synonym_type.proto\x12+google.actions.sdk.v2.interactionmodel.type\x1a@google/actions/sdk/v2/interactionmodel/type/entity_display.proto\x1a\x1fgoogle/api/field_behavior.proto"\x92\x04\n\x0bSynonymType\x12[\n\nmatch_type\x18\x01 \x01(\x0e2B.google.actions.sdk.v2.interactionmodel.type.SynonymType.MatchTypeB\x03\xe0A\x01\x12"\n\x15accept_unknown_values\x18\x03 \x01(\x08B\x03\xe0A\x01\x12]\n\x08entities\x18\x02 \x03(\x0b2F.google.actions.sdk.v2.interactionmodel.type.SynonymType.EntitiesEntryB\x03\xe0A\x02\x1aq\n\x06Entity\x12P\n\x07display\x18\x01 \x01(\x0b2:.google.actions.sdk.v2.interactionmodel.type.EntityDisplayB\x03\xe0A\x01\x12\x15\n\x08synonyms\x18\x02 \x03(\tB\x03\xe0A\x01\x1ap\n\rEntitiesEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12N\n\x05value\x18\x02 \x01(\x0b2?.google.actions.sdk.v2.interactionmodel.type.SynonymType.Entity:\x028\x01">\n\tMatchType\x12\x0f\n\x0bUNSPECIFIED\x10\x00\x12\x0f\n\x0bEXACT_MATCH\x10\x01\x12\x0f\n\x0bFUZZY_MATCH\x10\x02B\x91\x01\n/com.google.actions.sdk.v2.interactionmodel.typeB\x10SynonymTypeProtoP\x01ZJgoogle.golang.org/genproto/googleapis/actions/sdk/v2/interactionmodel/typeb\x06proto3')
_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'google.actions.sdk.v2.interactionmodel.type.synonym_type_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
    _globals['DESCRIPTOR']._loaded_options = None
    _globals['DESCRIPTOR']._serialized_options = b'\n/com.google.actions.sdk.v2.interactionmodel.typeB\x10SynonymTypeProtoP\x01ZJgoogle.golang.org/genproto/googleapis/actions/sdk/v2/interactionmodel/type'
    _globals['_SYNONYMTYPE_ENTITY'].fields_by_name['display']._loaded_options = None
    _globals['_SYNONYMTYPE_ENTITY'].fields_by_name['display']._serialized_options = b'\xe0A\x01'
    _globals['_SYNONYMTYPE_ENTITY'].fields_by_name['synonyms']._loaded_options = None
    _globals['_SYNONYMTYPE_ENTITY'].fields_by_name['synonyms']._serialized_options = b'\xe0A\x01'
    _globals['_SYNONYMTYPE_ENTITIESENTRY']._loaded_options = None
    _globals['_SYNONYMTYPE_ENTITIESENTRY']._serialized_options = b'8\x01'
    _globals['_SYNONYMTYPE'].fields_by_name['match_type']._loaded_options = None
    _globals['_SYNONYMTYPE'].fields_by_name['match_type']._serialized_options = b'\xe0A\x01'
    _globals['_SYNONYMTYPE'].fields_by_name['accept_unknown_values']._loaded_options = None
    _globals['_SYNONYMTYPE'].fields_by_name['accept_unknown_values']._serialized_options = b'\xe0A\x01'
    _globals['_SYNONYMTYPE'].fields_by_name['entities']._loaded_options = None
    _globals['_SYNONYMTYPE'].fields_by_name['entities']._serialized_options = b'\xe0A\x02'
    _globals['_SYNONYMTYPE']._serialized_start = 211
    _globals['_SYNONYMTYPE']._serialized_end = 741
    _globals['_SYNONYMTYPE_ENTITY']._serialized_start = 450
    _globals['_SYNONYMTYPE_ENTITY']._serialized_end = 563
    _globals['_SYNONYMTYPE_ENTITIESENTRY']._serialized_start = 565
    _globals['_SYNONYMTYPE_ENTITIESENTRY']._serialized_end = 677
    _globals['_SYNONYMTYPE_MATCHTYPE']._serialized_start = 679
    _globals['_SYNONYMTYPE_MATCHTYPE']._serialized_end = 741