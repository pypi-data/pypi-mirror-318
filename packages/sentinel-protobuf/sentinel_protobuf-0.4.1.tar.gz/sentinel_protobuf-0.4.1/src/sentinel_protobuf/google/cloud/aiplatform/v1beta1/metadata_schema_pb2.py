"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_runtime_version.ValidateProtobufRuntimeVersion(_runtime_version.Domain.PUBLIC, 5, 28, 1, '', 'google/cloud/aiplatform/v1beta1/metadata_schema.proto')
_sym_db = _symbol_database.Default()
from .....google.api import field_behavior_pb2 as google_dot_api_dot_field__behavior__pb2
from .....google.api import resource_pb2 as google_dot_api_dot_resource__pb2
from google.protobuf import timestamp_pb2 as google_dot_protobuf_dot_timestamp__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n5google/cloud/aiplatform/v1beta1/metadata_schema.proto\x12\x1fgoogle.cloud.aiplatform.v1beta1\x1a\x1fgoogle/api/field_behavior.proto\x1a\x19google/api/resource.proto\x1a\x1fgoogle/protobuf/timestamp.proto"\x85\x04\n\x0eMetadataSchema\x12\x11\n\x04name\x18\x01 \x01(\tB\x03\xe0A\x03\x12\x16\n\x0eschema_version\x18\x02 \x01(\t\x12\x13\n\x06schema\x18\x03 \x01(\tB\x03\xe0A\x02\x12W\n\x0bschema_type\x18\x04 \x01(\x0e2B.google.cloud.aiplatform.v1beta1.MetadataSchema.MetadataSchemaType\x124\n\x0bcreate_time\x18\x05 \x01(\x0b2\x1a.google.protobuf.TimestampB\x03\xe0A\x03\x12\x13\n\x0bdescription\x18\x06 \x01(\t"s\n\x12MetadataSchemaType\x12$\n METADATA_SCHEMA_TYPE_UNSPECIFIED\x10\x00\x12\x11\n\rARTIFACT_TYPE\x10\x01\x12\x12\n\x0eEXECUTION_TYPE\x10\x02\x12\x10\n\x0cCONTEXT_TYPE\x10\x03:\x99\x01\xeaA\x95\x01\n(aiplatform.googleapis.com/MetadataSchema\x12iprojects/{project}/locations/{location}/metadataStores/{metadata_store}/metadataSchemas/{metadata_schema}B\xea\x01\n#com.google.cloud.aiplatform.v1beta1B\x13MetadataSchemaProtoP\x01ZCcloud.google.com/go/aiplatform/apiv1beta1/aiplatformpb;aiplatformpb\xaa\x02\x1fGoogle.Cloud.AIPlatform.V1Beta1\xca\x02\x1fGoogle\\Cloud\\AIPlatform\\V1beta1\xea\x02"Google::Cloud::AIPlatform::V1beta1b\x06proto3')
_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'google.cloud.aiplatform.v1beta1.metadata_schema_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
    _globals['DESCRIPTOR']._loaded_options = None
    _globals['DESCRIPTOR']._serialized_options = b'\n#com.google.cloud.aiplatform.v1beta1B\x13MetadataSchemaProtoP\x01ZCcloud.google.com/go/aiplatform/apiv1beta1/aiplatformpb;aiplatformpb\xaa\x02\x1fGoogle.Cloud.AIPlatform.V1Beta1\xca\x02\x1fGoogle\\Cloud\\AIPlatform\\V1beta1\xea\x02"Google::Cloud::AIPlatform::V1beta1'
    _globals['_METADATASCHEMA'].fields_by_name['name']._loaded_options = None
    _globals['_METADATASCHEMA'].fields_by_name['name']._serialized_options = b'\xe0A\x03'
    _globals['_METADATASCHEMA'].fields_by_name['schema']._loaded_options = None
    _globals['_METADATASCHEMA'].fields_by_name['schema']._serialized_options = b'\xe0A\x02'
    _globals['_METADATASCHEMA'].fields_by_name['create_time']._loaded_options = None
    _globals['_METADATASCHEMA'].fields_by_name['create_time']._serialized_options = b'\xe0A\x03'
    _globals['_METADATASCHEMA']._loaded_options = None
    _globals['_METADATASCHEMA']._serialized_options = b'\xeaA\x95\x01\n(aiplatform.googleapis.com/MetadataSchema\x12iprojects/{project}/locations/{location}/metadataStores/{metadata_store}/metadataSchemas/{metadata_schema}'
    _globals['_METADATASCHEMA']._serialized_start = 184
    _globals['_METADATASCHEMA']._serialized_end = 701
    _globals['_METADATASCHEMA_METADATASCHEMATYPE']._serialized_start = 430
    _globals['_METADATASCHEMA_METADATASCHEMATYPE']._serialized_end = 545