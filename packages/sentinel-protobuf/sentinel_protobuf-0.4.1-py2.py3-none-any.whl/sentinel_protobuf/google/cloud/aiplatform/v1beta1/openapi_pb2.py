"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_runtime_version.ValidateProtobufRuntimeVersion(_runtime_version.Domain.PUBLIC, 5, 28, 1, '', 'google/cloud/aiplatform/v1beta1/openapi.proto')
_sym_db = _symbol_database.Default()
from .....google.api import field_behavior_pb2 as google_dot_api_dot_field__behavior__pb2
from google.protobuf import struct_pb2 as google_dot_protobuf_dot_struct__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n-google/cloud/aiplatform/v1beta1/openapi.proto\x12\x1fgoogle.cloud.aiplatform.v1beta1\x1a\x1fgoogle/api/field_behavior.proto\x1a\x1cgoogle/protobuf/struct.proto"\xc9\x06\n\x06Schema\x128\n\x04type\x18\x01 \x01(\x0e2%.google.cloud.aiplatform.v1beta1.TypeB\x03\xe0A\x01\x12\x13\n\x06format\x18\x07 \x01(\tB\x03\xe0A\x01\x12\x12\n\x05title\x18\x18 \x01(\tB\x03\xe0A\x01\x12\x18\n\x0bdescription\x18\x08 \x01(\tB\x03\xe0A\x01\x12\x15\n\x08nullable\x18\x06 \x01(\x08B\x03\xe0A\x01\x12,\n\x07default\x18\x17 \x01(\x0b2\x16.google.protobuf.ValueB\x03\xe0A\x01\x12;\n\x05items\x18\x02 \x01(\x0b2\'.google.cloud.aiplatform.v1beta1.SchemaB\x03\xe0A\x01\x12\x16\n\tmin_items\x18\x15 \x01(\x03B\x03\xe0A\x01\x12\x16\n\tmax_items\x18\x16 \x01(\x03B\x03\xe0A\x01\x12\x11\n\x04enum\x18\t \x03(\tB\x03\xe0A\x01\x12P\n\nproperties\x18\x03 \x03(\x0b27.google.cloud.aiplatform.v1beta1.Schema.PropertiesEntryB\x03\xe0A\x01\x12\x1e\n\x11property_ordering\x18\x19 \x03(\tB\x03\xe0A\x01\x12\x15\n\x08required\x18\x05 \x03(\tB\x03\xe0A\x01\x12\x1b\n\x0emin_properties\x18\x0e \x01(\x03B\x03\xe0A\x01\x12\x1b\n\x0emax_properties\x18\x0f \x01(\x03B\x03\xe0A\x01\x12\x14\n\x07minimum\x18\x10 \x01(\x01B\x03\xe0A\x01\x12\x14\n\x07maximum\x18\x11 \x01(\x01B\x03\xe0A\x01\x12\x17\n\nmin_length\x18\x12 \x01(\x03B\x03\xe0A\x01\x12\x17\n\nmax_length\x18\x13 \x01(\x03B\x03\xe0A\x01\x12\x14\n\x07pattern\x18\x14 \x01(\tB\x03\xe0A\x01\x12,\n\x07example\x18\x04 \x01(\x0b2\x16.google.protobuf.ValueB\x03\xe0A\x01\x12<\n\x06any_of\x18\x0b \x03(\x0b2\'.google.cloud.aiplatform.v1beta1.SchemaB\x03\xe0A\x01\x1aZ\n\x0fPropertiesEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x126\n\x05value\x18\x02 \x01(\x0b2\'.google.cloud.aiplatform.v1beta1.Schema:\x028\x01*e\n\x04Type\x12\x14\n\x10TYPE_UNSPECIFIED\x10\x00\x12\n\n\x06STRING\x10\x01\x12\n\n\x06NUMBER\x10\x02\x12\x0b\n\x07INTEGER\x10\x03\x12\x0b\n\x07BOOLEAN\x10\x04\x12\t\n\x05ARRAY\x10\x05\x12\n\n\x06OBJECT\x10\x06B\xe3\x01\n#com.google.cloud.aiplatform.v1beta1B\x0cOpenApiProtoP\x01ZCcloud.google.com/go/aiplatform/apiv1beta1/aiplatformpb;aiplatformpb\xaa\x02\x1fGoogle.Cloud.AIPlatform.V1Beta1\xca\x02\x1fGoogle\\Cloud\\AIPlatform\\V1beta1\xea\x02"Google::Cloud::AIPlatform::V1beta1b\x06proto3')
_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'google.cloud.aiplatform.v1beta1.openapi_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
    _globals['DESCRIPTOR']._loaded_options = None
    _globals['DESCRIPTOR']._serialized_options = b'\n#com.google.cloud.aiplatform.v1beta1B\x0cOpenApiProtoP\x01ZCcloud.google.com/go/aiplatform/apiv1beta1/aiplatformpb;aiplatformpb\xaa\x02\x1fGoogle.Cloud.AIPlatform.V1Beta1\xca\x02\x1fGoogle\\Cloud\\AIPlatform\\V1beta1\xea\x02"Google::Cloud::AIPlatform::V1beta1'
    _globals['_SCHEMA_PROPERTIESENTRY']._loaded_options = None
    _globals['_SCHEMA_PROPERTIESENTRY']._serialized_options = b'8\x01'
    _globals['_SCHEMA'].fields_by_name['type']._loaded_options = None
    _globals['_SCHEMA'].fields_by_name['type']._serialized_options = b'\xe0A\x01'
    _globals['_SCHEMA'].fields_by_name['format']._loaded_options = None
    _globals['_SCHEMA'].fields_by_name['format']._serialized_options = b'\xe0A\x01'
    _globals['_SCHEMA'].fields_by_name['title']._loaded_options = None
    _globals['_SCHEMA'].fields_by_name['title']._serialized_options = b'\xe0A\x01'
    _globals['_SCHEMA'].fields_by_name['description']._loaded_options = None
    _globals['_SCHEMA'].fields_by_name['description']._serialized_options = b'\xe0A\x01'
    _globals['_SCHEMA'].fields_by_name['nullable']._loaded_options = None
    _globals['_SCHEMA'].fields_by_name['nullable']._serialized_options = b'\xe0A\x01'
    _globals['_SCHEMA'].fields_by_name['default']._loaded_options = None
    _globals['_SCHEMA'].fields_by_name['default']._serialized_options = b'\xe0A\x01'
    _globals['_SCHEMA'].fields_by_name['items']._loaded_options = None
    _globals['_SCHEMA'].fields_by_name['items']._serialized_options = b'\xe0A\x01'
    _globals['_SCHEMA'].fields_by_name['min_items']._loaded_options = None
    _globals['_SCHEMA'].fields_by_name['min_items']._serialized_options = b'\xe0A\x01'
    _globals['_SCHEMA'].fields_by_name['max_items']._loaded_options = None
    _globals['_SCHEMA'].fields_by_name['max_items']._serialized_options = b'\xe0A\x01'
    _globals['_SCHEMA'].fields_by_name['enum']._loaded_options = None
    _globals['_SCHEMA'].fields_by_name['enum']._serialized_options = b'\xe0A\x01'
    _globals['_SCHEMA'].fields_by_name['properties']._loaded_options = None
    _globals['_SCHEMA'].fields_by_name['properties']._serialized_options = b'\xe0A\x01'
    _globals['_SCHEMA'].fields_by_name['property_ordering']._loaded_options = None
    _globals['_SCHEMA'].fields_by_name['property_ordering']._serialized_options = b'\xe0A\x01'
    _globals['_SCHEMA'].fields_by_name['required']._loaded_options = None
    _globals['_SCHEMA'].fields_by_name['required']._serialized_options = b'\xe0A\x01'
    _globals['_SCHEMA'].fields_by_name['min_properties']._loaded_options = None
    _globals['_SCHEMA'].fields_by_name['min_properties']._serialized_options = b'\xe0A\x01'
    _globals['_SCHEMA'].fields_by_name['max_properties']._loaded_options = None
    _globals['_SCHEMA'].fields_by_name['max_properties']._serialized_options = b'\xe0A\x01'
    _globals['_SCHEMA'].fields_by_name['minimum']._loaded_options = None
    _globals['_SCHEMA'].fields_by_name['minimum']._serialized_options = b'\xe0A\x01'
    _globals['_SCHEMA'].fields_by_name['maximum']._loaded_options = None
    _globals['_SCHEMA'].fields_by_name['maximum']._serialized_options = b'\xe0A\x01'
    _globals['_SCHEMA'].fields_by_name['min_length']._loaded_options = None
    _globals['_SCHEMA'].fields_by_name['min_length']._serialized_options = b'\xe0A\x01'
    _globals['_SCHEMA'].fields_by_name['max_length']._loaded_options = None
    _globals['_SCHEMA'].fields_by_name['max_length']._serialized_options = b'\xe0A\x01'
    _globals['_SCHEMA'].fields_by_name['pattern']._loaded_options = None
    _globals['_SCHEMA'].fields_by_name['pattern']._serialized_options = b'\xe0A\x01'
    _globals['_SCHEMA'].fields_by_name['example']._loaded_options = None
    _globals['_SCHEMA'].fields_by_name['example']._serialized_options = b'\xe0A\x01'
    _globals['_SCHEMA'].fields_by_name['any_of']._loaded_options = None
    _globals['_SCHEMA'].fields_by_name['any_of']._serialized_options = b'\xe0A\x01'
    _globals['_TYPE']._serialized_start = 989
    _globals['_TYPE']._serialized_end = 1090
    _globals['_SCHEMA']._serialized_start = 146
    _globals['_SCHEMA']._serialized_end = 987
    _globals['_SCHEMA_PROPERTIESENTRY']._serialized_start = 897
    _globals['_SCHEMA_PROPERTIESENTRY']._serialized_end = 987