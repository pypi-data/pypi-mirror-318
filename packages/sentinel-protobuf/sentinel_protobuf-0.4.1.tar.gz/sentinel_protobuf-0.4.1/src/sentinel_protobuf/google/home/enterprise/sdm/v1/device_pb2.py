"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_runtime_version.ValidateProtobufRuntimeVersion(_runtime_version.Domain.PUBLIC, 5, 28, 1, '', 'google/home/enterprise/sdm/v1/device.proto')
_sym_db = _symbol_database.Default()
from ......google.api import field_behavior_pb2 as google_dot_api_dot_field__behavior__pb2
from ......google.api import resource_pb2 as google_dot_api_dot_resource__pb2
from google.protobuf import struct_pb2 as google_dot_protobuf_dot_struct__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n*google/home/enterprise/sdm/v1/device.proto\x12\x1dgoogle.home.enterprise.sdm.v1\x1a\x1fgoogle/api/field_behavior.proto\x1a\x19google/api/resource.proto\x1a\x1cgoogle/protobuf/struct.proto"\xfd\x01\n\x06Device\x12\x0c\n\x04name\x18\x01 \x01(\t\x12\x11\n\x04type\x18\x02 \x01(\tB\x03\xe0A\x03\x12,\n\x06traits\x18\x04 \x01(\x0b2\x17.google.protobuf.StructB\x03\xe0A\x03\x12G\n\x10parent_relations\x18\x05 \x03(\x0b2-.google.home.enterprise.sdm.v1.ParentRelation:[\xeaAX\n+smartdevicemanagement.googleapis.com/Device\x12)enterprises/{enterprise}/devices/{device}"@\n\x0eParentRelation\x12\x13\n\x06parent\x18\x01 \x01(\tB\x03\xe0A\x03\x12\x19\n\x0cdisplay_name\x18\x02 \x01(\tB\x03\xe0A\x03B\xb2\x01\n!com.google.home.enterprise.sdm.v1P\x01Z@google.golang.org/genproto/googleapis/home/enterprise/sdm/v1;sdm\xa2\x02\x08GHENTSDM\xaa\x02\x1dGoogle.Home.Enterprise.Sdm.V1\xca\x02\x1dGoogle\\Home\\Enterprise\\Sdm\\V1b\x06proto3')
_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'google.home.enterprise.sdm.v1.device_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
    _globals['DESCRIPTOR']._loaded_options = None
    _globals['DESCRIPTOR']._serialized_options = b'\n!com.google.home.enterprise.sdm.v1P\x01Z@google.golang.org/genproto/googleapis/home/enterprise/sdm/v1;sdm\xa2\x02\x08GHENTSDM\xaa\x02\x1dGoogle.Home.Enterprise.Sdm.V1\xca\x02\x1dGoogle\\Home\\Enterprise\\Sdm\\V1'
    _globals['_DEVICE'].fields_by_name['type']._loaded_options = None
    _globals['_DEVICE'].fields_by_name['type']._serialized_options = b'\xe0A\x03'
    _globals['_DEVICE'].fields_by_name['traits']._loaded_options = None
    _globals['_DEVICE'].fields_by_name['traits']._serialized_options = b'\xe0A\x03'
    _globals['_DEVICE']._loaded_options = None
    _globals['_DEVICE']._serialized_options = b'\xeaAX\n+smartdevicemanagement.googleapis.com/Device\x12)enterprises/{enterprise}/devices/{device}'
    _globals['_PARENTRELATION'].fields_by_name['parent']._loaded_options = None
    _globals['_PARENTRELATION'].fields_by_name['parent']._serialized_options = b'\xe0A\x03'
    _globals['_PARENTRELATION'].fields_by_name['display_name']._loaded_options = None
    _globals['_PARENTRELATION'].fields_by_name['display_name']._serialized_options = b'\xe0A\x03'
    _globals['_DEVICE']._serialized_start = 168
    _globals['_DEVICE']._serialized_end = 421
    _globals['_PARENTRELATION']._serialized_start = 423
    _globals['_PARENTRELATION']._serialized_end = 487