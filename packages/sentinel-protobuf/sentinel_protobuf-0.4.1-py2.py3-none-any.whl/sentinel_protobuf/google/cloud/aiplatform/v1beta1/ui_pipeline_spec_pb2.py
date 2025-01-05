"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_runtime_version.ValidateProtobufRuntimeVersion(_runtime_version.Domain.PUBLIC, 5, 28, 1, '', 'google/cloud/aiplatform/v1beta1/ui_pipeline_spec.proto')
_sym_db = _symbol_database.Default()
from .....google.api import field_behavior_pb2 as google_dot_api_dot_field__behavior__pb2
from .....google.api import resource_pb2 as google_dot_api_dot_resource__pb2
from .....google.cloud.aiplatform.v1beta1 import value_pb2 as google_dot_cloud_dot_aiplatform_dot_v1beta1_dot_value__pb2
from google.protobuf import struct_pb2 as google_dot_protobuf_dot_struct__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n6google/cloud/aiplatform/v1beta1/ui_pipeline_spec.proto\x12\x1fgoogle.cloud.aiplatform.v1beta1\x1a\x1fgoogle/api/field_behavior.proto\x1a\x19google/api/resource.proto\x1a+google/cloud/aiplatform/v1beta1/value.proto\x1a\x1cgoogle/protobuf/struct.proto"\x81\x01\n\x12ArtifactTypeSchema\x12\x16\n\x0cschema_title\x18\x01 \x01(\tH\x00\x12\x18\n\nschema_uri\x18\x02 \x01(\tB\x02\x18\x01H\x00\x12\x19\n\x0finstance_schema\x18\x03 \x01(\tH\x00\x12\x16\n\x0eschema_version\x18\x04 \x01(\tB\x06\n\x04kind"\x97\x04\n\x0fRuntimeArtifact\x12\x0c\n\x04name\x18\x01 \x01(\t\x12A\n\x04type\x18\x02 \x01(\x0b23.google.cloud.aiplatform.v1beta1.ArtifactTypeSchema\x12\x0b\n\x03uri\x18\x03 \x01(\t\x12X\n\nproperties\x18\x04 \x03(\x0b2@.google.cloud.aiplatform.v1beta1.RuntimeArtifact.PropertiesEntryB\x02\x18\x01\x12e\n\x11custom_properties\x18\x05 \x03(\x0b2F.google.cloud.aiplatform.v1beta1.RuntimeArtifact.CustomPropertiesEntryB\x02\x18\x01\x12)\n\x08metadata\x18\x06 \x01(\x0b2\x17.google.protobuf.Struct\x1aY\n\x0fPropertiesEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x125\n\x05value\x18\x02 \x01(\x0b2&.google.cloud.aiplatform.v1beta1.Value:\x028\x01\x1a_\n\x15CustomPropertiesEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x125\n\x05value\x18\x02 \x01(\x0b2&.google.cloud.aiplatform.v1beta1.Value:\x028\x01B\xea\x01\n#com.google.cloud.aiplatform.v1beta1B\x13UiPipelineSpecProtoP\x01ZCcloud.google.com/go/aiplatform/apiv1beta1/aiplatformpb;aiplatformpb\xaa\x02\x1fGoogle.Cloud.AIPlatform.V1Beta1\xca\x02\x1fGoogle\\Cloud\\AIPlatform\\V1beta1\xea\x02"Google::Cloud::AIPlatform::V1beta1b\x06proto3')
_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'google.cloud.aiplatform.v1beta1.ui_pipeline_spec_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
    _globals['DESCRIPTOR']._loaded_options = None
    _globals['DESCRIPTOR']._serialized_options = b'\n#com.google.cloud.aiplatform.v1beta1B\x13UiPipelineSpecProtoP\x01ZCcloud.google.com/go/aiplatform/apiv1beta1/aiplatformpb;aiplatformpb\xaa\x02\x1fGoogle.Cloud.AIPlatform.V1Beta1\xca\x02\x1fGoogle\\Cloud\\AIPlatform\\V1beta1\xea\x02"Google::Cloud::AIPlatform::V1beta1'
    _globals['_ARTIFACTTYPESCHEMA'].fields_by_name['schema_uri']._loaded_options = None
    _globals['_ARTIFACTTYPESCHEMA'].fields_by_name['schema_uri']._serialized_options = b'\x18\x01'
    _globals['_RUNTIMEARTIFACT_PROPERTIESENTRY']._loaded_options = None
    _globals['_RUNTIMEARTIFACT_PROPERTIESENTRY']._serialized_options = b'8\x01'
    _globals['_RUNTIMEARTIFACT_CUSTOMPROPERTIESENTRY']._loaded_options = None
    _globals['_RUNTIMEARTIFACT_CUSTOMPROPERTIESENTRY']._serialized_options = b'8\x01'
    _globals['_RUNTIMEARTIFACT'].fields_by_name['properties']._loaded_options = None
    _globals['_RUNTIMEARTIFACT'].fields_by_name['properties']._serialized_options = b'\x18\x01'
    _globals['_RUNTIMEARTIFACT'].fields_by_name['custom_properties']._loaded_options = None
    _globals['_RUNTIMEARTIFACT'].fields_by_name['custom_properties']._serialized_options = b'\x18\x01'
    _globals['_ARTIFACTTYPESCHEMA']._serialized_start = 227
    _globals['_ARTIFACTTYPESCHEMA']._serialized_end = 356
    _globals['_RUNTIMEARTIFACT']._serialized_start = 359
    _globals['_RUNTIMEARTIFACT']._serialized_end = 894
    _globals['_RUNTIMEARTIFACT_PROPERTIESENTRY']._serialized_start = 708
    _globals['_RUNTIMEARTIFACT_PROPERTIESENTRY']._serialized_end = 797
    _globals['_RUNTIMEARTIFACT_CUSTOMPROPERTIESENTRY']._serialized_start = 799
    _globals['_RUNTIMEARTIFACT_CUSTOMPROPERTIESENTRY']._serialized_end = 894