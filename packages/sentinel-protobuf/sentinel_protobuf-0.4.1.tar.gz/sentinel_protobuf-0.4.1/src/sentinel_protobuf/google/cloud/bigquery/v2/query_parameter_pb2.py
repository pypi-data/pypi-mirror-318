"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_runtime_version.ValidateProtobufRuntimeVersion(_runtime_version.Domain.PUBLIC, 5, 28, 1, '', 'google/cloud/bigquery/v2/query_parameter.proto')
_sym_db = _symbol_database.Default()
from .....google.api import field_behavior_pb2 as google_dot_api_dot_field__behavior__pb2
from google.protobuf import struct_pb2 as google_dot_protobuf_dot_struct__pb2
from google.protobuf import wrappers_pb2 as google_dot_protobuf_dot_wrappers__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n.google/cloud/bigquery/v2/query_parameter.proto\x12\x18google.cloud.bigquery.v2\x1a\x1fgoogle/api/field_behavior.proto\x1a\x1cgoogle/protobuf/struct.proto\x1a\x1egoogle/protobuf/wrappers.proto"\x88\x01\n\x18QueryParameterStructType\x12\x11\n\x04name\x18\x01 \x01(\tB\x03\xe0A\x01\x12?\n\x04type\x18\x02 \x01(\x0b2,.google.cloud.bigquery.v2.QueryParameterTypeB\x03\xe0A\x02\x12\x18\n\x0bdescription\x18\x03 \x01(\tB\x03\xe0A\x01"\x8c\x02\n\x12QueryParameterType\x12\x11\n\x04type\x18\x01 \x01(\tB\x03\xe0A\x02\x12E\n\narray_type\x18\x02 \x01(\x0b2,.google.cloud.bigquery.v2.QueryParameterTypeB\x03\xe0A\x01\x12M\n\x0cstruct_types\x18\x03 \x03(\x0b22.google.cloud.bigquery.v2.QueryParameterStructTypeB\x03\xe0A\x01\x12M\n\x12range_element_type\x18\x04 \x01(\x0b2,.google.cloud.bigquery.v2.QueryParameterTypeB\x03\xe0A\x01"\x90\x01\n\nRangeValue\x12A\n\x05start\x18\x01 \x01(\x0b2-.google.cloud.bigquery.v2.QueryParameterValueB\x03\xe0A\x01\x12?\n\x03end\x18\x02 \x01(\x0b2-.google.cloud.bigquery.v2.QueryParameterValueB\x03\xe0A\x01"\xc0\x03\n\x13QueryParameterValue\x120\n\x05value\x18\x01 \x01(\x0b2\x1c.google.protobuf.StringValueB\x03\xe0A\x01\x12H\n\x0carray_values\x18\x02 \x03(\x0b2-.google.cloud.bigquery.v2.QueryParameterValueB\x03\xe0A\x01\x12V\n\rstruct_values\x18\x03 \x03(\x0b2?.google.cloud.bigquery.v2.QueryParameterValue.StructValuesEntry\x12>\n\x0brange_value\x18\x06 \x01(\x0b2$.google.cloud.bigquery.v2.RangeValueB\x03\xe0A\x01\x121\n\x11alt_struct_values\x18\x05 \x03(\x0b2\x16.google.protobuf.Value\x1ab\n\x11StructValuesEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12<\n\x05value\x18\x02 \x01(\x0b2-.google.cloud.bigquery.v2.QueryParameterValue:\x028\x01"\xbb\x01\n\x0eQueryParameter\x12\x11\n\x04name\x18\x01 \x01(\tB\x03\xe0A\x01\x12I\n\x0eparameter_type\x18\x02 \x01(\x0b2,.google.cloud.bigquery.v2.QueryParameterTypeB\x03\xe0A\x02\x12K\n\x0fparameter_value\x18\x03 \x01(\x0b2-.google.cloud.bigquery.v2.QueryParameterValueB\x03\xe0A\x02Bm\n\x1ccom.google.cloud.bigquery.v2B\x13QueryParameterProtoZ8cloud.google.com/go/bigquery/apiv2/bigquerypb;bigquerypbb\x06proto3')
_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'google.cloud.bigquery.v2.query_parameter_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
    _globals['DESCRIPTOR']._loaded_options = None
    _globals['DESCRIPTOR']._serialized_options = b'\n\x1ccom.google.cloud.bigquery.v2B\x13QueryParameterProtoZ8cloud.google.com/go/bigquery/apiv2/bigquerypb;bigquerypb'
    _globals['_QUERYPARAMETERSTRUCTTYPE'].fields_by_name['name']._loaded_options = None
    _globals['_QUERYPARAMETERSTRUCTTYPE'].fields_by_name['name']._serialized_options = b'\xe0A\x01'
    _globals['_QUERYPARAMETERSTRUCTTYPE'].fields_by_name['type']._loaded_options = None
    _globals['_QUERYPARAMETERSTRUCTTYPE'].fields_by_name['type']._serialized_options = b'\xe0A\x02'
    _globals['_QUERYPARAMETERSTRUCTTYPE'].fields_by_name['description']._loaded_options = None
    _globals['_QUERYPARAMETERSTRUCTTYPE'].fields_by_name['description']._serialized_options = b'\xe0A\x01'
    _globals['_QUERYPARAMETERTYPE'].fields_by_name['type']._loaded_options = None
    _globals['_QUERYPARAMETERTYPE'].fields_by_name['type']._serialized_options = b'\xe0A\x02'
    _globals['_QUERYPARAMETERTYPE'].fields_by_name['array_type']._loaded_options = None
    _globals['_QUERYPARAMETERTYPE'].fields_by_name['array_type']._serialized_options = b'\xe0A\x01'
    _globals['_QUERYPARAMETERTYPE'].fields_by_name['struct_types']._loaded_options = None
    _globals['_QUERYPARAMETERTYPE'].fields_by_name['struct_types']._serialized_options = b'\xe0A\x01'
    _globals['_QUERYPARAMETERTYPE'].fields_by_name['range_element_type']._loaded_options = None
    _globals['_QUERYPARAMETERTYPE'].fields_by_name['range_element_type']._serialized_options = b'\xe0A\x01'
    _globals['_RANGEVALUE'].fields_by_name['start']._loaded_options = None
    _globals['_RANGEVALUE'].fields_by_name['start']._serialized_options = b'\xe0A\x01'
    _globals['_RANGEVALUE'].fields_by_name['end']._loaded_options = None
    _globals['_RANGEVALUE'].fields_by_name['end']._serialized_options = b'\xe0A\x01'
    _globals['_QUERYPARAMETERVALUE_STRUCTVALUESENTRY']._loaded_options = None
    _globals['_QUERYPARAMETERVALUE_STRUCTVALUESENTRY']._serialized_options = b'8\x01'
    _globals['_QUERYPARAMETERVALUE'].fields_by_name['value']._loaded_options = None
    _globals['_QUERYPARAMETERVALUE'].fields_by_name['value']._serialized_options = b'\xe0A\x01'
    _globals['_QUERYPARAMETERVALUE'].fields_by_name['array_values']._loaded_options = None
    _globals['_QUERYPARAMETERVALUE'].fields_by_name['array_values']._serialized_options = b'\xe0A\x01'
    _globals['_QUERYPARAMETERVALUE'].fields_by_name['range_value']._loaded_options = None
    _globals['_QUERYPARAMETERVALUE'].fields_by_name['range_value']._serialized_options = b'\xe0A\x01'
    _globals['_QUERYPARAMETER'].fields_by_name['name']._loaded_options = None
    _globals['_QUERYPARAMETER'].fields_by_name['name']._serialized_options = b'\xe0A\x01'
    _globals['_QUERYPARAMETER'].fields_by_name['parameter_type']._loaded_options = None
    _globals['_QUERYPARAMETER'].fields_by_name['parameter_type']._serialized_options = b'\xe0A\x02'
    _globals['_QUERYPARAMETER'].fields_by_name['parameter_value']._loaded_options = None
    _globals['_QUERYPARAMETER'].fields_by_name['parameter_value']._serialized_options = b'\xe0A\x02'
    _globals['_QUERYPARAMETERSTRUCTTYPE']._serialized_start = 172
    _globals['_QUERYPARAMETERSTRUCTTYPE']._serialized_end = 308
    _globals['_QUERYPARAMETERTYPE']._serialized_start = 311
    _globals['_QUERYPARAMETERTYPE']._serialized_end = 579
    _globals['_RANGEVALUE']._serialized_start = 582
    _globals['_RANGEVALUE']._serialized_end = 726
    _globals['_QUERYPARAMETERVALUE']._serialized_start = 729
    _globals['_QUERYPARAMETERVALUE']._serialized_end = 1177
    _globals['_QUERYPARAMETERVALUE_STRUCTVALUESENTRY']._serialized_start = 1079
    _globals['_QUERYPARAMETERVALUE_STRUCTVALUESENTRY']._serialized_end = 1177
    _globals['_QUERYPARAMETER']._serialized_start = 1180
    _globals['_QUERYPARAMETER']._serialized_end = 1367