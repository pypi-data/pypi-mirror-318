
'Generated protocol buffer code.'
from google.protobuf.internal import builder as _builder
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
_sym_db = _symbol_database.Default()
from ....gogoproto import gogo_pb2 as gogoproto_dot_gogo__pb2
from ....sentinel.types.v1 import status_pb2 as sentinel_dot_types_dot_v1_dot_status__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x1dsentinel/plan/v3/events.proto\x12\x10sentinel.plan.v3\x1a\x14gogoproto/gogo.proto\x1a\x1esentinel/types/v1/status.proto"z\n\x0bEventCreate\x12\x12\n\x02id\x18\x01 \x01(\x04B\x06\xe2\xde\x1f\x02ID\x12\x14\n\x0cprov_address\x18\x02 \x01(\t\x12\x11\n\tgigabytes\x18\x03 \x01(\x03\x12\r\n\x05hours\x18\x04 \x01(\x03\x12\x0e\n\x06prices\x18\x05 \x01(\t\x12\x0f\n\x07private\x18\x06 \x01(\x08"O\n\rEventLinkNode\x12\x12\n\x02id\x18\x01 \x01(\x04B\x06\xe2\xde\x1f\x02ID\x12\x14\n\x0cprov_address\x18\x02 \x01(\t\x12\x14\n\x0cnode_address\x18\x03 \x01(\t"Q\n\x0fEventUnlinkNode\x12\x12\n\x02id\x18\x01 \x01(\x04B\x06\xe2\xde\x1f\x02ID\x12\x14\n\x0cprov_address\x18\x02 \x01(\t\x12\x14\n\x0cnode_address\x18\x03 \x01(\t"b\n\x0bEventUpdate\x12\x12\n\x02id\x18\x01 \x01(\x04B\x06\xe2\xde\x1f\x02ID\x12\x14\n\x0cprov_address\x18\x02 \x01(\t\x12)\n\x06status\x18\x03 \x01(\x0e2\x19.sentinel.types.v1.StatusB>Z4github.com/sentinel-official/hub/v12/x/plan/types/v3\xa8\xe2\x1e\x00\xc8\xe1\x1e\x00b\x06proto3')
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, globals())
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'sentinel.plan.v3.events_pb2', globals())
if (_descriptor._USE_C_DESCRIPTORS == False):
    DESCRIPTOR._options = None
    DESCRIPTOR._serialized_options = b'Z4github.com/sentinel-official/hub/v12/x/plan/types/v3\xa8\xe2\x1e\x00\xc8\xe1\x1e\x00'
    _EVENTCREATE.fields_by_name['id']._options = None
    _EVENTCREATE.fields_by_name['id']._serialized_options = b'\xe2\xde\x1f\x02ID'
    _EVENTLINKNODE.fields_by_name['id']._options = None
    _EVENTLINKNODE.fields_by_name['id']._serialized_options = b'\xe2\xde\x1f\x02ID'
    _EVENTUNLINKNODE.fields_by_name['id']._options = None
    _EVENTUNLINKNODE.fields_by_name['id']._serialized_options = b'\xe2\xde\x1f\x02ID'
    _EVENTUPDATE.fields_by_name['id']._options = None
    _EVENTUPDATE.fields_by_name['id']._serialized_options = b'\xe2\xde\x1f\x02ID'
    _EVENTCREATE._serialized_start = 105
    _EVENTCREATE._serialized_end = 227
    _EVENTLINKNODE._serialized_start = 229
    _EVENTLINKNODE._serialized_end = 308
    _EVENTUNLINKNODE._serialized_start = 310
    _EVENTUNLINKNODE._serialized_end = 391
    _EVENTUPDATE._serialized_start = 393
    _EVENTUPDATE._serialized_end = 491
