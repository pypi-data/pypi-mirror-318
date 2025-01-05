"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_runtime_version.ValidateProtobufRuntimeVersion(_runtime_version.Domain.PUBLIC, 5, 28, 1, '', 'google/cloud/aiplatform/v1beta1/types.proto')
_sym_db = _symbol_database.Default()
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n+google/cloud/aiplatform/v1beta1/types.proto\x12\x1fgoogle.cloud.aiplatform.v1beta1"\x1b\n\tBoolArray\x12\x0e\n\x06values\x18\x01 \x03(\x08"\x1d\n\x0bDoubleArray\x12\x0e\n\x06values\x18\x01 \x03(\x01"\x1c\n\nInt64Array\x12\x0e\n\x06values\x18\x01 \x03(\x03"\x1d\n\x0bStringArray\x12\x0e\n\x06values\x18\x01 \x03(\t"\xa7\x05\n\x06Tensor\x12?\n\x05dtype\x18\x01 \x01(\x0e20.google.cloud.aiplatform.v1beta1.Tensor.DataType\x12\r\n\x05shape\x18\x02 \x03(\x03\x12\x10\n\x08bool_val\x18\x03 \x03(\x08\x12\x12\n\nstring_val\x18\x0e \x03(\t\x12\x11\n\tbytes_val\x18\x0f \x03(\x0c\x12\x11\n\tfloat_val\x18\x05 \x03(\x02\x12\x12\n\ndouble_val\x18\x06 \x03(\x01\x12\x0f\n\x07int_val\x18\x07 \x03(\x05\x12\x11\n\tint64_val\x18\x08 \x03(\x03\x12\x10\n\x08uint_val\x18\t \x03(\r\x12\x12\n\nuint64_val\x18\n \x03(\x04\x129\n\x08list_val\x18\x0b \x03(\x0b2\'.google.cloud.aiplatform.v1beta1.Tensor\x12J\n\nstruct_val\x18\x0c \x03(\x0b26.google.cloud.aiplatform.v1beta1.Tensor.StructValEntry\x12\x12\n\ntensor_val\x18\r \x01(\x0c\x1aY\n\x0eStructValEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x126\n\x05value\x18\x02 \x01(\x0b2\'.google.cloud.aiplatform.v1beta1.Tensor:\x028\x01"\xac\x01\n\x08DataType\x12\x19\n\x15DATA_TYPE_UNSPECIFIED\x10\x00\x12\x08\n\x04BOOL\x10\x01\x12\n\n\x06STRING\x10\x02\x12\t\n\x05FLOAT\x10\x03\x12\n\n\x06DOUBLE\x10\x04\x12\x08\n\x04INT8\x10\x05\x12\t\n\x05INT16\x10\x06\x12\t\n\x05INT32\x10\x07\x12\t\n\x05INT64\x10\x08\x12\t\n\x05UINT8\x10\t\x12\n\n\x06UINT16\x10\n\x12\n\n\x06UINT32\x10\x0b\x12\n\n\x06UINT64\x10\x0cB\xe1\x01\n#com.google.cloud.aiplatform.v1beta1B\nTypesProtoP\x01ZCcloud.google.com/go/aiplatform/apiv1beta1/aiplatformpb;aiplatformpb\xaa\x02\x1fGoogle.Cloud.AIPlatform.V1Beta1\xca\x02\x1fGoogle\\Cloud\\AIPlatform\\V1beta1\xea\x02"Google::Cloud::AIPlatform::V1beta1b\x06proto3')
_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'google.cloud.aiplatform.v1beta1.types_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
    _globals['DESCRIPTOR']._loaded_options = None
    _globals['DESCRIPTOR']._serialized_options = b'\n#com.google.cloud.aiplatform.v1beta1B\nTypesProtoP\x01ZCcloud.google.com/go/aiplatform/apiv1beta1/aiplatformpb;aiplatformpb\xaa\x02\x1fGoogle.Cloud.AIPlatform.V1Beta1\xca\x02\x1fGoogle\\Cloud\\AIPlatform\\V1beta1\xea\x02"Google::Cloud::AIPlatform::V1beta1'
    _globals['_TENSOR_STRUCTVALENTRY']._loaded_options = None
    _globals['_TENSOR_STRUCTVALENTRY']._serialized_options = b'8\x01'
    _globals['_BOOLARRAY']._serialized_start = 80
    _globals['_BOOLARRAY']._serialized_end = 107
    _globals['_DOUBLEARRAY']._serialized_start = 109
    _globals['_DOUBLEARRAY']._serialized_end = 138
    _globals['_INT64ARRAY']._serialized_start = 140
    _globals['_INT64ARRAY']._serialized_end = 168
    _globals['_STRINGARRAY']._serialized_start = 170
    _globals['_STRINGARRAY']._serialized_end = 199
    _globals['_TENSOR']._serialized_start = 202
    _globals['_TENSOR']._serialized_end = 881
    _globals['_TENSOR_STRUCTVALENTRY']._serialized_start = 617
    _globals['_TENSOR_STRUCTVALENTRY']._serialized_end = 706
    _globals['_TENSOR_DATATYPE']._serialized_start = 709
    _globals['_TENSOR_DATATYPE']._serialized_end = 881