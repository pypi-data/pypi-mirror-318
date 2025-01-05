"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_runtime_version.ValidateProtobufRuntimeVersion(_runtime_version.Domain.PUBLIC, 5, 28, 1, '', 'google/actions/sdk/v2/interactionmodel/type/type.proto')
_sym_db = _symbol_database.Default()
from .......google.actions.sdk.v2.interactionmodel.type import free_text_type_pb2 as google_dot_actions_dot_sdk_dot_v2_dot_interactionmodel_dot_type_dot_free__text__type__pb2
from .......google.actions.sdk.v2.interactionmodel.type import regular_expression_type_pb2 as google_dot_actions_dot_sdk_dot_v2_dot_interactionmodel_dot_type_dot_regular__expression__type__pb2
from .......google.actions.sdk.v2.interactionmodel.type import synonym_type_pb2 as google_dot_actions_dot_sdk_dot_v2_dot_interactionmodel_dot_type_dot_synonym__type__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n6google/actions/sdk/v2/interactionmodel/type/type.proto\x12+google.actions.sdk.v2.interactionmodel.type\x1a@google/actions/sdk/v2/interactionmodel/type/free_text_type.proto\x1aIgoogle/actions/sdk/v2/interactionmodel/type/regular_expression_type.proto\x1a>google/actions/sdk/v2/interactionmodel/type/synonym_type.proto"\xa5\x02\n\x04Type\x12K\n\x07synonym\x18\x01 \x01(\x0b28.google.actions.sdk.v2.interactionmodel.type.SynonymTypeH\x00\x12`\n\x12regular_expression\x18\x02 \x01(\x0b2B.google.actions.sdk.v2.interactionmodel.type.RegularExpressionTypeH\x00\x12N\n\tfree_text\x18\x03 \x01(\x0b29.google.actions.sdk.v2.interactionmodel.type.FreeTextTypeH\x00\x12\x12\n\nexclusions\x18\x04 \x03(\tB\n\n\x08sub_typeB\x8a\x01\n/com.google.actions.sdk.v2.interactionmodel.typeB\tTypeProtoP\x01ZJgoogle.golang.org/genproto/googleapis/actions/sdk/v2/interactionmodel/typeb\x06proto3')
_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'google.actions.sdk.v2.interactionmodel.type.type_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
    _globals['DESCRIPTOR']._loaded_options = None
    _globals['DESCRIPTOR']._serialized_options = b'\n/com.google.actions.sdk.v2.interactionmodel.typeB\tTypeProtoP\x01ZJgoogle.golang.org/genproto/googleapis/actions/sdk/v2/interactionmodel/type'
    _globals['_TYPE']._serialized_start = 309
    _globals['_TYPE']._serialized_end = 602