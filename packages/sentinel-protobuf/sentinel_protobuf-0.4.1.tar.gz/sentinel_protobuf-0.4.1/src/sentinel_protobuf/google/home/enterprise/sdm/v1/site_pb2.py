"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_runtime_version.ValidateProtobufRuntimeVersion(_runtime_version.Domain.PUBLIC, 5, 28, 1, '', 'google/home/enterprise/sdm/v1/site.proto')
_sym_db = _symbol_database.Default()
from ......google.api import field_behavior_pb2 as google_dot_api_dot_field__behavior__pb2
from ......google.api import resource_pb2 as google_dot_api_dot_resource__pb2
from google.protobuf import struct_pb2 as google_dot_protobuf_dot_struct__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n(google/home/enterprise/sdm/v1/site.proto\x12\x1dgoogle.home.enterprise.sdm.v1\x1a\x1fgoogle/api/field_behavior.proto\x1a\x19google/api/resource.proto\x1a\x1cgoogle/protobuf/struct.proto"\xad\x01\n\tStructure\x12\x11\n\x04name\x18\x01 \x01(\tB\x03\xe0A\x03\x12\'\n\x06traits\x18\x02 \x01(\x0b2\x17.google.protobuf.Struct:d\xeaAa\n.smartdevicemanagement.googleapis.com/Structure\x12/enterprises/{enterprise}/structures/{structure}"\xb0\x01\n\x04Room\x12\x11\n\x04name\x18\x01 \x01(\tB\x03\xe0A\x03\x12\'\n\x06traits\x18\x02 \x01(\x0b2\x17.google.protobuf.Struct:l\xeaAi\n)smartdevicemanagement.googleapis.com/Room\x12<enterprises/{enterprise}/structures/{structure}/rooms/{room}B\xb2\x01\n!com.google.home.enterprise.sdm.v1P\x01Z@google.golang.org/genproto/googleapis/home/enterprise/sdm/v1;sdm\xa2\x02\x08GHENTSDM\xaa\x02\x1dGoogle.Home.Enterprise.Sdm.V1\xca\x02\x1dGoogle\\Home\\Enterprise\\Sdm\\V1b\x06proto3')
_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'google.home.enterprise.sdm.v1.site_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
    _globals['DESCRIPTOR']._loaded_options = None
    _globals['DESCRIPTOR']._serialized_options = b'\n!com.google.home.enterprise.sdm.v1P\x01Z@google.golang.org/genproto/googleapis/home/enterprise/sdm/v1;sdm\xa2\x02\x08GHENTSDM\xaa\x02\x1dGoogle.Home.Enterprise.Sdm.V1\xca\x02\x1dGoogle\\Home\\Enterprise\\Sdm\\V1'
    _globals['_STRUCTURE'].fields_by_name['name']._loaded_options = None
    _globals['_STRUCTURE'].fields_by_name['name']._serialized_options = b'\xe0A\x03'
    _globals['_STRUCTURE']._loaded_options = None
    _globals['_STRUCTURE']._serialized_options = b'\xeaAa\n.smartdevicemanagement.googleapis.com/Structure\x12/enterprises/{enterprise}/structures/{structure}'
    _globals['_ROOM'].fields_by_name['name']._loaded_options = None
    _globals['_ROOM'].fields_by_name['name']._serialized_options = b'\xe0A\x03'
    _globals['_ROOM']._loaded_options = None
    _globals['_ROOM']._serialized_options = b'\xeaAi\n)smartdevicemanagement.googleapis.com/Room\x12<enterprises/{enterprise}/structures/{structure}/rooms/{room}'
    _globals['_STRUCTURE']._serialized_start = 166
    _globals['_STRUCTURE']._serialized_end = 339
    _globals['_ROOM']._serialized_start = 342
    _globals['_ROOM']._serialized_end = 518