"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_runtime_version.ValidateProtobufRuntimeVersion(_runtime_version.Domain.PUBLIC, 5, 28, 1, '', 'google/actions/sdk/v2/interactionmodel/type/regular_expression_type.proto')
_sym_db = _symbol_database.Default()
from .......google.actions.sdk.v2.interactionmodel.type import entity_display_pb2 as google_dot_actions_dot_sdk_dot_v2_dot_interactionmodel_dot_type_dot_entity__display__pb2
from .......google.api import field_behavior_pb2 as google_dot_api_dot_field__behavior__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\nIgoogle/actions/sdk/v2/interactionmodel/type/regular_expression_type.proto\x12+google.actions.sdk.v2.interactionmodel.type\x1a@google/actions/sdk/v2/interactionmodel/type/entity_display.proto\x1a\x1fgoogle/api/field_behavior.proto"\xfa\x02\n\x15RegularExpressionType\x12g\n\x08entities\x18\x01 \x03(\x0b2P.google.actions.sdk.v2.interactionmodel.type.RegularExpressionType.EntitiesEntryB\x03\xe0A\x02\x1a|\n\x06Entity\x12P\n\x07display\x18\x01 \x01(\x0b2:.google.actions.sdk.v2.interactionmodel.type.EntityDisplayB\x03\xe0A\x01\x12 \n\x13regular_expressions\x18\x02 \x03(\tB\x03\xe0A\x02\x1az\n\rEntitiesEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12X\n\x05value\x18\x02 \x01(\x0b2I.google.actions.sdk.v2.interactionmodel.type.RegularExpressionType.Entity:\x028\x01B\x9b\x01\n/com.google.actions.sdk.v2.interactionmodel.typeB\x1aRegularExpressionTypeProtoP\x01ZJgoogle.golang.org/genproto/googleapis/actions/sdk/v2/interactionmodel/typeb\x06proto3')
_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'google.actions.sdk.v2.interactionmodel.type.regular_expression_type_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
    _globals['DESCRIPTOR']._loaded_options = None
    _globals['DESCRIPTOR']._serialized_options = b'\n/com.google.actions.sdk.v2.interactionmodel.typeB\x1aRegularExpressionTypeProtoP\x01ZJgoogle.golang.org/genproto/googleapis/actions/sdk/v2/interactionmodel/type'
    _globals['_REGULAREXPRESSIONTYPE_ENTITY'].fields_by_name['display']._loaded_options = None
    _globals['_REGULAREXPRESSIONTYPE_ENTITY'].fields_by_name['display']._serialized_options = b'\xe0A\x01'
    _globals['_REGULAREXPRESSIONTYPE_ENTITY'].fields_by_name['regular_expressions']._loaded_options = None
    _globals['_REGULAREXPRESSIONTYPE_ENTITY'].fields_by_name['regular_expressions']._serialized_options = b'\xe0A\x02'
    _globals['_REGULAREXPRESSIONTYPE_ENTITIESENTRY']._loaded_options = None
    _globals['_REGULAREXPRESSIONTYPE_ENTITIESENTRY']._serialized_options = b'8\x01'
    _globals['_REGULAREXPRESSIONTYPE'].fields_by_name['entities']._loaded_options = None
    _globals['_REGULAREXPRESSIONTYPE'].fields_by_name['entities']._serialized_options = b'\xe0A\x02'
    _globals['_REGULAREXPRESSIONTYPE']._serialized_start = 222
    _globals['_REGULAREXPRESSIONTYPE']._serialized_end = 600
    _globals['_REGULAREXPRESSIONTYPE_ENTITY']._serialized_start = 352
    _globals['_REGULAREXPRESSIONTYPE_ENTITY']._serialized_end = 476
    _globals['_REGULAREXPRESSIONTYPE_ENTITIESENTRY']._serialized_start = 478
    _globals['_REGULAREXPRESSIONTYPE_ENTITIESENTRY']._serialized_end = 600