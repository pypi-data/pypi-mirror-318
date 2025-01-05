"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_runtime_version.ValidateProtobufRuntimeVersion(_runtime_version.Domain.PUBLIC, 5, 28, 1, '', 'google/cloud/automl/v1beta1/data_types.proto')
_sym_db = _symbol_database.Default()
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n,google/cloud/automl/v1beta1/data_types.proto\x12\x1bgoogle.cloud.automl.v1beta1"\xfc\x01\n\x08DataType\x12B\n\x11list_element_type\x18\x02 \x01(\x0b2%.google.cloud.automl.v1beta1.DataTypeH\x00\x12>\n\x0bstruct_type\x18\x03 \x01(\x0b2\'.google.cloud.automl.v1beta1.StructTypeH\x00\x12\x15\n\x0btime_format\x18\x05 \x01(\tH\x00\x128\n\ttype_code\x18\x01 \x01(\x0e2%.google.cloud.automl.v1beta1.TypeCode\x12\x10\n\x08nullable\x18\x04 \x01(\x08B\t\n\x07details"\xa7\x01\n\nStructType\x12C\n\x06fields\x18\x01 \x03(\x0b23.google.cloud.automl.v1beta1.StructType.FieldsEntry\x1aT\n\x0bFieldsEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x124\n\x05value\x18\x02 \x01(\x0b2%.google.cloud.automl.v1beta1.DataType:\x028\x01*r\n\x08TypeCode\x12\x19\n\x15TYPE_CODE_UNSPECIFIED\x10\x00\x12\x0b\n\x07FLOAT64\x10\x03\x12\r\n\tTIMESTAMP\x10\x04\x12\n\n\x06STRING\x10\x06\x12\t\n\x05ARRAY\x10\x08\x12\n\n\x06STRUCT\x10\t\x12\x0c\n\x08CATEGORY\x10\nB\x9b\x01\n\x1fcom.google.cloud.automl.v1beta1P\x01Z7cloud.google.com/go/automl/apiv1beta1/automlpb;automlpb\xca\x02\x1bGoogle\\Cloud\\AutoMl\\V1beta1\xea\x02\x1eGoogle::Cloud::AutoML::V1beta1b\x06proto3')
_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'google.cloud.automl.v1beta1.data_types_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
    _globals['DESCRIPTOR']._loaded_options = None
    _globals['DESCRIPTOR']._serialized_options = b'\n\x1fcom.google.cloud.automl.v1beta1P\x01Z7cloud.google.com/go/automl/apiv1beta1/automlpb;automlpb\xca\x02\x1bGoogle\\Cloud\\AutoMl\\V1beta1\xea\x02\x1eGoogle::Cloud::AutoML::V1beta1'
    _globals['_STRUCTTYPE_FIELDSENTRY']._loaded_options = None
    _globals['_STRUCTTYPE_FIELDSENTRY']._serialized_options = b'8\x01'
    _globals['_TYPECODE']._serialized_start = 502
    _globals['_TYPECODE']._serialized_end = 616
    _globals['_DATATYPE']._serialized_start = 78
    _globals['_DATATYPE']._serialized_end = 330
    _globals['_STRUCTTYPE']._serialized_start = 333
    _globals['_STRUCTTYPE']._serialized_end = 500
    _globals['_STRUCTTYPE_FIELDSENTRY']._serialized_start = 416
    _globals['_STRUCTTYPE_FIELDSENTRY']._serialized_end = 500