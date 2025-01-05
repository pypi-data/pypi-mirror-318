"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_runtime_version.ValidateProtobufRuntimeVersion(_runtime_version.Domain.PUBLIC, 5, 28, 1, '', 'google/cloud/dialogflow/v2/validation_result.proto')
_sym_db = _symbol_database.Default()
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n2google/cloud/dialogflow/v2/validation_result.proto\x12\x1agoogle.cloud.dialogflow.v2"\xd7\x01\n\x0fValidationError\x12F\n\x08severity\x18\x01 \x01(\x0e24.google.cloud.dialogflow.v2.ValidationError.Severity\x12\x0f\n\x07entries\x18\x03 \x03(\t\x12\x15\n\rerror_message\x18\x04 \x01(\t"T\n\x08Severity\x12\x18\n\x14SEVERITY_UNSPECIFIED\x10\x00\x12\x08\n\x04INFO\x10\x01\x12\x0b\n\x07WARNING\x10\x02\x12\t\n\x05ERROR\x10\x03\x12\x0c\n\x08CRITICAL\x10\x04"Z\n\x10ValidationResult\x12F\n\x11validation_errors\x18\x01 \x03(\x0b2+.google.cloud.dialogflow.v2.ValidationErrorB\x9b\x01\n\x1ecom.google.cloud.dialogflow.v2B\x15ValidationResultProtoP\x01Z>cloud.google.com/go/dialogflow/apiv2/dialogflowpb;dialogflowpb\xa2\x02\x02DF\xaa\x02\x1aGoogle.Cloud.Dialogflow.V2b\x06proto3')
_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'google.cloud.dialogflow.v2.validation_result_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
    _globals['DESCRIPTOR']._loaded_options = None
    _globals['DESCRIPTOR']._serialized_options = b'\n\x1ecom.google.cloud.dialogflow.v2B\x15ValidationResultProtoP\x01Z>cloud.google.com/go/dialogflow/apiv2/dialogflowpb;dialogflowpb\xa2\x02\x02DF\xaa\x02\x1aGoogle.Cloud.Dialogflow.V2'
    _globals['_VALIDATIONERROR']._serialized_start = 83
    _globals['_VALIDATIONERROR']._serialized_end = 298
    _globals['_VALIDATIONERROR_SEVERITY']._serialized_start = 214
    _globals['_VALIDATIONERROR_SEVERITY']._serialized_end = 298
    _globals['_VALIDATIONRESULT']._serialized_start = 300
    _globals['_VALIDATIONRESULT']._serialized_end = 390