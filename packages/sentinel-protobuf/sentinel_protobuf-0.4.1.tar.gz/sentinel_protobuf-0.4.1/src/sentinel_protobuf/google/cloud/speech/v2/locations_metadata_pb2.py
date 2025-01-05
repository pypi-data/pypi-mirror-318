"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_runtime_version.ValidateProtobufRuntimeVersion(_runtime_version.Domain.PUBLIC, 5, 28, 1, '', 'google/cloud/speech/v2/locations_metadata.proto')
_sym_db = _symbol_database.Default()
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n/google/cloud/speech/v2/locations_metadata.proto\x12\x16google.cloud.speech.v2"6\n\x0cModelFeature\x12\x0f\n\x07feature\x18\x01 \x01(\t\x12\x15\n\rrelease_state\x18\x02 \x01(\t"L\n\rModelFeatures\x12;\n\rmodel_feature\x18\x01 \x03(\x0b2$.google.cloud.speech.v2.ModelFeature"\xbe\x01\n\rModelMetadata\x12P\n\x0emodel_features\x18\x01 \x03(\x0b28.google.cloud.speech.v2.ModelMetadata.ModelFeaturesEntry\x1a[\n\x12ModelFeaturesEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x124\n\x05value\x18\x02 \x01(\x0b2%.google.cloud.speech.v2.ModelFeatures:\x028\x01"\xae\x01\n\x10LanguageMetadata\x12D\n\x06models\x18\x01 \x03(\x0b24.google.cloud.speech.v2.LanguageMetadata.ModelsEntry\x1aT\n\x0bModelsEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x124\n\x05value\x18\x02 \x01(\x0b2%.google.cloud.speech.v2.ModelMetadata:\x028\x01"\xc8\x01\n\x0eAccessMetadata\x12N\n\x0fconstraint_type\x18\x01 \x01(\x0e25.google.cloud.speech.v2.AccessMetadata.ConstraintType"f\n\x0eConstraintType\x12\x1f\n\x1bCONSTRAINT_TYPE_UNSPECIFIED\x10\x00\x123\n/RESOURCE_LOCATIONS_ORG_POLICY_CREATE_CONSTRAINT\x10\x01"\x91\x01\n\x11LocationsMetadata\x12;\n\tlanguages\x18\x01 \x01(\x0b2(.google.cloud.speech.v2.LanguageMetadata\x12?\n\x0faccess_metadata\x18\x02 \x01(\x0b2&.google.cloud.speech.v2.AccessMetadataBj\n\x1acom.google.cloud.speech.v2B\x16LocationsMetadataProtoP\x01Z2cloud.google.com/go/speech/apiv2/speechpb;speechpbb\x06proto3')
_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'google.cloud.speech.v2.locations_metadata_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
    _globals['DESCRIPTOR']._loaded_options = None
    _globals['DESCRIPTOR']._serialized_options = b'\n\x1acom.google.cloud.speech.v2B\x16LocationsMetadataProtoP\x01Z2cloud.google.com/go/speech/apiv2/speechpb;speechpb'
    _globals['_MODELMETADATA_MODELFEATURESENTRY']._loaded_options = None
    _globals['_MODELMETADATA_MODELFEATURESENTRY']._serialized_options = b'8\x01'
    _globals['_LANGUAGEMETADATA_MODELSENTRY']._loaded_options = None
    _globals['_LANGUAGEMETADATA_MODELSENTRY']._serialized_options = b'8\x01'
    _globals['_MODELFEATURE']._serialized_start = 75
    _globals['_MODELFEATURE']._serialized_end = 129
    _globals['_MODELFEATURES']._serialized_start = 131
    _globals['_MODELFEATURES']._serialized_end = 207
    _globals['_MODELMETADATA']._serialized_start = 210
    _globals['_MODELMETADATA']._serialized_end = 400
    _globals['_MODELMETADATA_MODELFEATURESENTRY']._serialized_start = 309
    _globals['_MODELMETADATA_MODELFEATURESENTRY']._serialized_end = 400
    _globals['_LANGUAGEMETADATA']._serialized_start = 403
    _globals['_LANGUAGEMETADATA']._serialized_end = 577
    _globals['_LANGUAGEMETADATA_MODELSENTRY']._serialized_start = 493
    _globals['_LANGUAGEMETADATA_MODELSENTRY']._serialized_end = 577
    _globals['_ACCESSMETADATA']._serialized_start = 580
    _globals['_ACCESSMETADATA']._serialized_end = 780
    _globals['_ACCESSMETADATA_CONSTRAINTTYPE']._serialized_start = 678
    _globals['_ACCESSMETADATA_CONSTRAINTTYPE']._serialized_end = 780
    _globals['_LOCATIONSMETADATA']._serialized_start = 783
    _globals['_LOCATIONSMETADATA']._serialized_end = 928