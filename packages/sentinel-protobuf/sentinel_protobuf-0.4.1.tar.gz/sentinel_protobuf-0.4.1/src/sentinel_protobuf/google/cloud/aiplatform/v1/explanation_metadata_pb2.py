"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_runtime_version.ValidateProtobufRuntimeVersion(_runtime_version.Domain.PUBLIC, 5, 28, 1, '', 'google/cloud/aiplatform/v1/explanation_metadata.proto')
_sym_db = _symbol_database.Default()
from .....google.api import field_behavior_pb2 as google_dot_api_dot_field__behavior__pb2
from google.protobuf import struct_pb2 as google_dot_protobuf_dot_struct__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n5google/cloud/aiplatform/v1/explanation_metadata.proto\x12\x1agoogle.cloud.aiplatform.v1\x1a\x1fgoogle/api/field_behavior.proto\x1a\x1cgoogle/protobuf/struct.proto"\xcf\x12\n\x13ExplanationMetadata\x12P\n\x06inputs\x18\x01 \x03(\x0b2;.google.cloud.aiplatform.v1.ExplanationMetadata.InputsEntryB\x03\xe0A\x02\x12R\n\x07outputs\x18\x02 \x03(\x0b2<.google.cloud.aiplatform.v1.ExplanationMetadata.OutputsEntryB\x03\xe0A\x02\x12\'\n\x1ffeature_attributions_schema_uri\x18\x03 \x01(\t\x12\x1b\n\x13latent_space_source\x18\x05 \x01(\t\x1a\xc4\r\n\rInputMetadata\x12/\n\x0finput_baselines\x18\x01 \x03(\x0b2\x16.google.protobuf.Value\x12\x19\n\x11input_tensor_name\x18\x02 \x01(\t\x12X\n\x08encoding\x18\x03 \x01(\x0e2F.google.cloud.aiplatform.v1.ExplanationMetadata.InputMetadata.Encoding\x12\x10\n\x08modality\x18\x04 \x01(\t\x12n\n\x14feature_value_domain\x18\x05 \x01(\x0b2P.google.cloud.aiplatform.v1.ExplanationMetadata.InputMetadata.FeatureValueDomain\x12\x1b\n\x13indices_tensor_name\x18\x06 \x01(\t\x12\x1f\n\x17dense_shape_tensor_name\x18\x07 \x01(\t\x12\x1d\n\x15index_feature_mapping\x18\x08 \x03(\t\x12\x1b\n\x13encoded_tensor_name\x18\t \x01(\t\x121\n\x11encoded_baselines\x18\n \x03(\x0b2\x16.google.protobuf.Value\x12b\n\rvisualization\x18\x0b \x01(\x0b2K.google.cloud.aiplatform.v1.ExplanationMetadata.InputMetadata.Visualization\x12\x12\n\ngroup_name\x18\x0c \x01(\t\x1aj\n\x12FeatureValueDomain\x12\x11\n\tmin_value\x18\x01 \x01(\x02\x12\x11\n\tmax_value\x18\x02 \x01(\x02\x12\x15\n\roriginal_mean\x18\x03 \x01(\x02\x12\x17\n\x0foriginal_stddev\x18\x04 \x01(\x02\x1a\xd6\x06\n\rVisualization\x12^\n\x04type\x18\x01 \x01(\x0e2P.google.cloud.aiplatform.v1.ExplanationMetadata.InputMetadata.Visualization.Type\x12f\n\x08polarity\x18\x02 \x01(\x0e2T.google.cloud.aiplatform.v1.ExplanationMetadata.InputMetadata.Visualization.Polarity\x12g\n\tcolor_map\x18\x03 \x01(\x0e2T.google.cloud.aiplatform.v1.ExplanationMetadata.InputMetadata.Visualization.ColorMap\x12\x1f\n\x17clip_percent_upperbound\x18\x04 \x01(\x02\x12\x1f\n\x17clip_percent_lowerbound\x18\x05 \x01(\x02\x12m\n\x0coverlay_type\x18\x06 \x01(\x0e2W.google.cloud.aiplatform.v1.ExplanationMetadata.InputMetadata.Visualization.OverlayType"6\n\x04Type\x12\x14\n\x10TYPE_UNSPECIFIED\x10\x00\x12\n\n\x06PIXELS\x10\x01\x12\x0c\n\x08OUTLINES\x10\x02"J\n\x08Polarity\x12\x18\n\x14POLARITY_UNSPECIFIED\x10\x00\x12\x0c\n\x08POSITIVE\x10\x01\x12\x0c\n\x08NEGATIVE\x10\x02\x12\x08\n\x04BOTH\x10\x03"{\n\x08ColorMap\x12\x19\n\x15COLOR_MAP_UNSPECIFIED\x10\x00\x12\x0e\n\nPINK_GREEN\x10\x01\x12\x0b\n\x07VIRIDIS\x10\x02\x12\x07\n\x03RED\x10\x03\x12\t\n\x05GREEN\x10\x04\x12\r\n\tRED_GREEN\x10\x06\x12\x14\n\x10PINK_WHITE_GREEN\x10\x05"b\n\x0bOverlayType\x12\x1c\n\x18OVERLAY_TYPE_UNSPECIFIED\x10\x00\x12\x08\n\x04NONE\x10\x01\x12\x0c\n\x08ORIGINAL\x10\x02\x12\r\n\tGRAYSCALE\x10\x03\x12\x0e\n\nMASK_BLACK\x10\x04"\xa0\x01\n\x08Encoding\x12\x18\n\x14ENCODING_UNSPECIFIED\x10\x00\x12\x0c\n\x08IDENTITY\x10\x01\x12\x13\n\x0fBAG_OF_FEATURES\x10\x02\x12\x1a\n\x16BAG_OF_FEATURES_SPARSE\x10\x03\x12\r\n\tINDICATOR\x10\x04\x12\x16\n\x12COMBINED_EMBEDDING\x10\x05\x12\x14\n\x10CONCAT_EMBEDDING\x10\x06\x1a\xa6\x01\n\x0eOutputMetadata\x12<\n\x1aindex_display_name_mapping\x18\x01 \x01(\x0b2\x16.google.protobuf.ValueH\x00\x12"\n\x18display_name_mapping_key\x18\x02 \x01(\tH\x00\x12\x1a\n\x12output_tensor_name\x18\x03 \x01(\tB\x16\n\x14display_name_mapping\x1al\n\x0bInputsEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12L\n\x05value\x18\x02 \x01(\x0b2=.google.cloud.aiplatform.v1.ExplanationMetadata.InputMetadata:\x028\x01\x1an\n\x0cOutputsEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12M\n\x05value\x18\x02 \x01(\x0b2>.google.cloud.aiplatform.v1.ExplanationMetadata.OutputMetadata:\x028\x01B\xd6\x01\n\x1ecom.google.cloud.aiplatform.v1B\x18ExplanationMetadataProtoP\x01Z>cloud.google.com/go/aiplatform/apiv1/aiplatformpb;aiplatformpb\xaa\x02\x1aGoogle.Cloud.AIPlatform.V1\xca\x02\x1aGoogle\\Cloud\\AIPlatform\\V1\xea\x02\x1dGoogle::Cloud::AIPlatform::V1b\x06proto3')
_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'google.cloud.aiplatform.v1.explanation_metadata_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
    _globals['DESCRIPTOR']._loaded_options = None
    _globals['DESCRIPTOR']._serialized_options = b'\n\x1ecom.google.cloud.aiplatform.v1B\x18ExplanationMetadataProtoP\x01Z>cloud.google.com/go/aiplatform/apiv1/aiplatformpb;aiplatformpb\xaa\x02\x1aGoogle.Cloud.AIPlatform.V1\xca\x02\x1aGoogle\\Cloud\\AIPlatform\\V1\xea\x02\x1dGoogle::Cloud::AIPlatform::V1'
    _globals['_EXPLANATIONMETADATA_INPUTSENTRY']._loaded_options = None
    _globals['_EXPLANATIONMETADATA_INPUTSENTRY']._serialized_options = b'8\x01'
    _globals['_EXPLANATIONMETADATA_OUTPUTSENTRY']._loaded_options = None
    _globals['_EXPLANATIONMETADATA_OUTPUTSENTRY']._serialized_options = b'8\x01'
    _globals['_EXPLANATIONMETADATA'].fields_by_name['inputs']._loaded_options = None
    _globals['_EXPLANATIONMETADATA'].fields_by_name['inputs']._serialized_options = b'\xe0A\x02'
    _globals['_EXPLANATIONMETADATA'].fields_by_name['outputs']._loaded_options = None
    _globals['_EXPLANATIONMETADATA'].fields_by_name['outputs']._serialized_options = b'\xe0A\x02'
    _globals['_EXPLANATIONMETADATA']._serialized_start = 149
    _globals['_EXPLANATIONMETADATA']._serialized_end = 2532
    _globals['_EXPLANATIONMETADATA_INPUTMETADATA']._serialized_start = 409
    _globals['_EXPLANATIONMETADATA_INPUTMETADATA']._serialized_end = 2141
    _globals['_EXPLANATIONMETADATA_INPUTMETADATA_FEATUREVALUEDOMAIN']._serialized_start = 1015
    _globals['_EXPLANATIONMETADATA_INPUTMETADATA_FEATUREVALUEDOMAIN']._serialized_end = 1121
    _globals['_EXPLANATIONMETADATA_INPUTMETADATA_VISUALIZATION']._serialized_start = 1124
    _globals['_EXPLANATIONMETADATA_INPUTMETADATA_VISUALIZATION']._serialized_end = 1978
    _globals['_EXPLANATIONMETADATA_INPUTMETADATA_VISUALIZATION_TYPE']._serialized_start = 1623
    _globals['_EXPLANATIONMETADATA_INPUTMETADATA_VISUALIZATION_TYPE']._serialized_end = 1677
    _globals['_EXPLANATIONMETADATA_INPUTMETADATA_VISUALIZATION_POLARITY']._serialized_start = 1679
    _globals['_EXPLANATIONMETADATA_INPUTMETADATA_VISUALIZATION_POLARITY']._serialized_end = 1753
    _globals['_EXPLANATIONMETADATA_INPUTMETADATA_VISUALIZATION_COLORMAP']._serialized_start = 1755
    _globals['_EXPLANATIONMETADATA_INPUTMETADATA_VISUALIZATION_COLORMAP']._serialized_end = 1878
    _globals['_EXPLANATIONMETADATA_INPUTMETADATA_VISUALIZATION_OVERLAYTYPE']._serialized_start = 1880
    _globals['_EXPLANATIONMETADATA_INPUTMETADATA_VISUALIZATION_OVERLAYTYPE']._serialized_end = 1978
    _globals['_EXPLANATIONMETADATA_INPUTMETADATA_ENCODING']._serialized_start = 1981
    _globals['_EXPLANATIONMETADATA_INPUTMETADATA_ENCODING']._serialized_end = 2141
    _globals['_EXPLANATIONMETADATA_OUTPUTMETADATA']._serialized_start = 2144
    _globals['_EXPLANATIONMETADATA_OUTPUTMETADATA']._serialized_end = 2310
    _globals['_EXPLANATIONMETADATA_INPUTSENTRY']._serialized_start = 2312
    _globals['_EXPLANATIONMETADATA_INPUTSENTRY']._serialized_end = 2420
    _globals['_EXPLANATIONMETADATA_OUTPUTSENTRY']._serialized_start = 2422
    _globals['_EXPLANATIONMETADATA_OUTPUTSENTRY']._serialized_end = 2532