"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_runtime_version.ValidateProtobufRuntimeVersion(_runtime_version.Domain.PUBLIC, 5, 28, 1, '', 'google/cloud/aiplatform/v1beta1/accelerator_type.proto')
_sym_db = _symbol_database.Default()
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n6google/cloud/aiplatform/v1beta1/accelerator_type.proto\x12\x1fgoogle.cloud.aiplatform.v1beta1*\xce\x02\n\x0fAcceleratorType\x12 \n\x1cACCELERATOR_TYPE_UNSPECIFIED\x10\x00\x12\x18\n\x10NVIDIA_TESLA_K80\x10\x01\x1a\x02\x08\x01\x12\x15\n\x11NVIDIA_TESLA_P100\x10\x02\x12\x15\n\x11NVIDIA_TESLA_V100\x10\x03\x12\x13\n\x0fNVIDIA_TESLA_P4\x10\x04\x12\x13\n\x0fNVIDIA_TESLA_T4\x10\x05\x12\x15\n\x11NVIDIA_TESLA_A100\x10\x08\x12\x14\n\x10NVIDIA_A100_80GB\x10\t\x12\r\n\tNVIDIA_L4\x10\x0b\x12\x14\n\x10NVIDIA_H100_80GB\x10\r\x12\x19\n\x15NVIDIA_H100_MEGA_80GB\x10\x0e\x12\n\n\x06TPU_V2\x10\x06\x12\n\n\x06TPU_V3\x10\x07\x12\x0e\n\nTPU_V4_POD\x10\n\x12\x12\n\x0eTPU_V5_LITEPOD\x10\x0cB\xeb\x01\n#com.google.cloud.aiplatform.v1beta1B\x14AcceleratorTypeProtoP\x01ZCcloud.google.com/go/aiplatform/apiv1beta1/aiplatformpb;aiplatformpb\xaa\x02\x1fGoogle.Cloud.AIPlatform.V1Beta1\xca\x02\x1fGoogle\\Cloud\\AIPlatform\\V1beta1\xea\x02"Google::Cloud::AIPlatform::V1beta1b\x06proto3')
_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'google.cloud.aiplatform.v1beta1.accelerator_type_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
    _globals['DESCRIPTOR']._loaded_options = None
    _globals['DESCRIPTOR']._serialized_options = b'\n#com.google.cloud.aiplatform.v1beta1B\x14AcceleratorTypeProtoP\x01ZCcloud.google.com/go/aiplatform/apiv1beta1/aiplatformpb;aiplatformpb\xaa\x02\x1fGoogle.Cloud.AIPlatform.V1Beta1\xca\x02\x1fGoogle\\Cloud\\AIPlatform\\V1beta1\xea\x02"Google::Cloud::AIPlatform::V1beta1'
    _globals['_ACCELERATORTYPE'].values_by_name['NVIDIA_TESLA_K80']._loaded_options = None
    _globals['_ACCELERATORTYPE'].values_by_name['NVIDIA_TESLA_K80']._serialized_options = b'\x08\x01'
    _globals['_ACCELERATORTYPE']._serialized_start = 92
    _globals['_ACCELERATORTYPE']._serialized_end = 426