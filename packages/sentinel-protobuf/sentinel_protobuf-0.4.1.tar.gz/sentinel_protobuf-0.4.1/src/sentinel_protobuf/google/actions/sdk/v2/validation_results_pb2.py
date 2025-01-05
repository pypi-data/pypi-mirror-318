"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_runtime_version.ValidateProtobufRuntimeVersion(_runtime_version.Domain.PUBLIC, 5, 28, 1, '', 'google/actions/sdk/v2/validation_results.proto')
_sym_db = _symbol_database.Default()
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n.google/actions/sdk/v2/validation_results.proto\x12\x15google.actions.sdk.v2"M\n\x11ValidationResults\x128\n\x07results\x18\x01 \x03(\x0b2\'.google.actions.sdk.v2.ValidationResult"\xb1\x01\n\x10ValidationResult\x12\x1a\n\x12validation_message\x18\x01 \x01(\t\x12U\n\x12validation_context\x18\x02 \x01(\x0b29.google.actions.sdk.v2.ValidationResult.ValidationContext\x1a*\n\x11ValidationContext\x12\x15\n\rlanguage_code\x18\x01 \x01(\tBo\n\x19com.google.actions.sdk.v2B\x16ValidationResultsProtoP\x01Z8google.golang.org/genproto/googleapis/actions/sdk/v2;sdkb\x06proto3')
_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'google.actions.sdk.v2.validation_results_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
    _globals['DESCRIPTOR']._loaded_options = None
    _globals['DESCRIPTOR']._serialized_options = b'\n\x19com.google.actions.sdk.v2B\x16ValidationResultsProtoP\x01Z8google.golang.org/genproto/googleapis/actions/sdk/v2;sdk'
    _globals['_VALIDATIONRESULTS']._serialized_start = 73
    _globals['_VALIDATIONRESULTS']._serialized_end = 150
    _globals['_VALIDATIONRESULT']._serialized_start = 153
    _globals['_VALIDATIONRESULT']._serialized_end = 330
    _globals['_VALIDATIONRESULT_VALIDATIONCONTEXT']._serialized_start = 288
    _globals['_VALIDATIONRESULT_VALIDATIONCONTEXT']._serialized_end = 330