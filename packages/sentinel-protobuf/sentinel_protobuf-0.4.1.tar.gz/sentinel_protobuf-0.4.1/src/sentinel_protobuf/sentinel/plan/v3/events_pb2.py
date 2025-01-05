"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_runtime_version.ValidateProtobufRuntimeVersion(_runtime_version.Domain.PUBLIC, 5, 28, 1, '', 'sentinel/plan/v3/events.proto')
_sym_db = _symbol_database.Default()
from ....gogoproto import gogo_pb2 as gogoproto_dot_gogo__pb2
from ....sentinel.types.v1 import status_pb2 as sentinel_dot_types_dot_v1_dot_status__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x1dsentinel/plan/v3/events.proto\x12\x10sentinel.plan.v3\x1a\x14gogoproto/gogo.proto\x1a\x1esentinel/types/v1/status.proto"z\n\x0bEventCreate\x12\x12\n\x02id\x18\x01 \x01(\x04B\x06\xe2\xde\x1f\x02ID\x12\x14\n\x0cprov_address\x18\x02 \x01(\t\x12\x11\n\tgigabytes\x18\x03 \x01(\x03\x12\r\n\x05hours\x18\x04 \x01(\x03\x12\x0e\n\x06prices\x18\x05 \x01(\t\x12\x0f\n\x07private\x18\x06 \x01(\x08"O\n\rEventLinkNode\x12\x12\n\x02id\x18\x01 \x01(\x04B\x06\xe2\xde\x1f\x02ID\x12\x14\n\x0cprov_address\x18\x02 \x01(\t\x12\x14\n\x0cnode_address\x18\x03 \x01(\t"Q\n\x0fEventUnlinkNode\x12\x12\n\x02id\x18\x01 \x01(\x04B\x06\xe2\xde\x1f\x02ID\x12\x14\n\x0cprov_address\x18\x02 \x01(\t\x12\x14\n\x0cnode_address\x18\x03 \x01(\t"b\n\x0bEventUpdate\x12\x12\n\x02id\x18\x01 \x01(\x04B\x06\xe2\xde\x1f\x02ID\x12\x14\n\x0cprov_address\x18\x02 \x01(\t\x12)\n\x06status\x18\x03 \x01(\x0e2\x19.sentinel.types.v1.StatusB>Z4github.com/sentinel-official/hub/v12/x/plan/types/v3\xc8\xe1\x1e\x00\xa8\xe2\x1e\x00b\x06proto3')
_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'sentinel.plan.v3.events_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
    _globals['DESCRIPTOR']._loaded_options = None
    _globals['DESCRIPTOR']._serialized_options = b'Z4github.com/sentinel-official/hub/v12/x/plan/types/v3\xc8\xe1\x1e\x00\xa8\xe2\x1e\x00'
    _globals['_EVENTCREATE'].fields_by_name['id']._loaded_options = None
    _globals['_EVENTCREATE'].fields_by_name['id']._serialized_options = b'\xe2\xde\x1f\x02ID'
    _globals['_EVENTLINKNODE'].fields_by_name['id']._loaded_options = None
    _globals['_EVENTLINKNODE'].fields_by_name['id']._serialized_options = b'\xe2\xde\x1f\x02ID'
    _globals['_EVENTUNLINKNODE'].fields_by_name['id']._loaded_options = None
    _globals['_EVENTUNLINKNODE'].fields_by_name['id']._serialized_options = b'\xe2\xde\x1f\x02ID'
    _globals['_EVENTUPDATE'].fields_by_name['id']._loaded_options = None
    _globals['_EVENTUPDATE'].fields_by_name['id']._serialized_options = b'\xe2\xde\x1f\x02ID'
    _globals['_EVENTCREATE']._serialized_start = 105
    _globals['_EVENTCREATE']._serialized_end = 227
    _globals['_EVENTLINKNODE']._serialized_start = 229
    _globals['_EVENTLINKNODE']._serialized_end = 308
    _globals['_EVENTUNLINKNODE']._serialized_start = 310
    _globals['_EVENTUNLINKNODE']._serialized_end = 391
    _globals['_EVENTUPDATE']._serialized_start = 393
    _globals['_EVENTUPDATE']._serialized_end = 491