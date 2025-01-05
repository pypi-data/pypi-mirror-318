"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_runtime_version.ValidateProtobufRuntimeVersion(_runtime_version.Domain.PUBLIC, 5, 28, 1, '', 'google/cloud/dialogflow/v2beta1/validation_result.proto')
_sym_db = _symbol_database.Default()
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n7google/cloud/dialogflow/v2beta1/validation_result.proto\x12\x1fgoogle.cloud.dialogflow.v2beta1"\xdc\x01\n\x0fValidationError\x12K\n\x08severity\x18\x01 \x01(\x0e29.google.cloud.dialogflow.v2beta1.ValidationError.Severity\x12\x0f\n\x07entries\x18\x03 \x03(\t\x12\x15\n\rerror_message\x18\x04 \x01(\t"T\n\x08Severity\x12\x18\n\x14SEVERITY_UNSPECIFIED\x10\x00\x12\x08\n\x04INFO\x10\x01\x12\x0b\n\x07WARNING\x10\x02\x12\t\n\x05ERROR\x10\x03\x12\x0c\n\x08CRITICAL\x10\x04"_\n\x10ValidationResult\x12K\n\x11validation_errors\x18\x01 \x03(\x0b20.google.cloud.dialogflow.v2beta1.ValidationErrorB\xaa\x01\n#com.google.cloud.dialogflow.v2beta1B\x15ValidationResultProtoP\x01ZCcloud.google.com/go/dialogflow/apiv2beta1/dialogflowpb;dialogflowpb\xa2\x02\x02DF\xaa\x02\x1fGoogle.Cloud.Dialogflow.V2Beta1b\x06proto3')
_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'google.cloud.dialogflow.v2beta1.validation_result_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
    _globals['DESCRIPTOR']._loaded_options = None
    _globals['DESCRIPTOR']._serialized_options = b'\n#com.google.cloud.dialogflow.v2beta1B\x15ValidationResultProtoP\x01ZCcloud.google.com/go/dialogflow/apiv2beta1/dialogflowpb;dialogflowpb\xa2\x02\x02DF\xaa\x02\x1fGoogle.Cloud.Dialogflow.V2Beta1'
    _globals['_VALIDATIONERROR']._serialized_start = 93
    _globals['_VALIDATIONERROR']._serialized_end = 313
    _globals['_VALIDATIONERROR_SEVERITY']._serialized_start = 229
    _globals['_VALIDATIONERROR_SEVERITY']._serialized_end = 313
    _globals['_VALIDATIONRESULT']._serialized_start = 315
    _globals['_VALIDATIONRESULT']._serialized_end = 410