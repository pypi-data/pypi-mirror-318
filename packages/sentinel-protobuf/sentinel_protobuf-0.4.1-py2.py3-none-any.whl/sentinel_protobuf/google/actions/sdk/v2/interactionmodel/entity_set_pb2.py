"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_runtime_version.ValidateProtobufRuntimeVersion(_runtime_version.Domain.PUBLIC, 5, 28, 1, '', 'google/actions/sdk/v2/interactionmodel/entity_set.proto')
_sym_db = _symbol_database.Default()
from ......google.api import field_behavior_pb2 as google_dot_api_dot_field__behavior__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n7google/actions/sdk/v2/interactionmodel/entity_set.proto\x12&google.actions.sdk.v2.interactionmodel\x1a\x1fgoogle/api/field_behavior.proto"w\n\tEntitySet\x12O\n\x08entities\x18\x01 \x03(\x0b28.google.actions.sdk.v2.interactionmodel.EntitySet.EntityB\x03\xe0A\x02\x1a\x19\n\x06Entity\x12\x0f\n\x02id\x18\x01 \x01(\tB\x03\xe0A\x02B\x96\x01\n*com.google.actions.sdk.v2.interactionmodelB\x0eEntitySetProtoP\x01ZVgoogle.golang.org/genproto/googleapis/actions/sdk/v2/interactionmodel;interactionmodelb\x06proto3')
_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'google.actions.sdk.v2.interactionmodel.entity_set_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
    _globals['DESCRIPTOR']._loaded_options = None
    _globals['DESCRIPTOR']._serialized_options = b'\n*com.google.actions.sdk.v2.interactionmodelB\x0eEntitySetProtoP\x01ZVgoogle.golang.org/genproto/googleapis/actions/sdk/v2/interactionmodel;interactionmodel'
    _globals['_ENTITYSET_ENTITY'].fields_by_name['id']._loaded_options = None
    _globals['_ENTITYSET_ENTITY'].fields_by_name['id']._serialized_options = b'\xe0A\x02'
    _globals['_ENTITYSET'].fields_by_name['entities']._loaded_options = None
    _globals['_ENTITYSET'].fields_by_name['entities']._serialized_options = b'\xe0A\x02'
    _globals['_ENTITYSET']._serialized_start = 132
    _globals['_ENTITYSET']._serialized_end = 251
    _globals['_ENTITYSET_ENTITY']._serialized_start = 226
    _globals['_ENTITYSET_ENTITY']._serialized_end = 251