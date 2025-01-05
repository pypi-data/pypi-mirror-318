
'Generated protocol buffer code.'
from google.protobuf.internal import builder as _builder
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
_sym_db = _symbol_database.Default()
from ....gogoproto import gogo_pb2 as gogoproto_dot_gogo__pb2
from ....sentinel.types.v1 import status_pb2 as sentinel_dot_types_dot_v1_dot_status__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n!sentinel/provider/v3/events.proto\x12\x14sentinel.provider.v3\x1a\x14gogoproto/gogo.proto\x1a\x1esentinel/types/v1/status.proto"i\n\x0bEventCreate\x12\x14\n\x0cprov_address\x18\x01 \x01(\t\x12\x0c\n\x04name\x18\x02 \x01(\t\x12\x10\n\x08identity\x18\x03 \x01(\t\x12\x0f\n\x07website\x18\x04 \x01(\t\x12\x13\n\x0bdescription\x18\x05 \x01(\t"p\n\x12EventUpdateDetails\x12\x14\n\x0cprov_address\x18\x01 \x01(\t\x12\x0c\n\x04name\x18\x02 \x01(\t\x12\x10\n\x08identity\x18\x03 \x01(\t\x12\x0f\n\x07website\x18\x04 \x01(\t\x12\x13\n\x0bdescription\x18\x05 \x01(\t"T\n\x11EventUpdateStatus\x12\x14\n\x0cprov_address\x18\x01 \x01(\t\x12)\n\x06status\x18\x02 \x01(\x0e2\x19.sentinel.types.v1.StatusBBZ8github.com/sentinel-official/hub/v12/x/provider/types/v3\xa8\xe2\x1e\x00\xc8\xe1\x1e\x00b\x06proto3')
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, globals())
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'sentinel.provider.v3.events_pb2', globals())
if (_descriptor._USE_C_DESCRIPTORS == False):
    DESCRIPTOR._options = None
    DESCRIPTOR._serialized_options = b'Z8github.com/sentinel-official/hub/v12/x/provider/types/v3\xa8\xe2\x1e\x00\xc8\xe1\x1e\x00'
    _EVENTCREATE._serialized_start = 113
    _EVENTCREATE._serialized_end = 218
    _EVENTUPDATEDETAILS._serialized_start = 220
    _EVENTUPDATEDETAILS._serialized_end = 332
    _EVENTUPDATESTATUS._serialized_start = 334
    _EVENTUPDATESTATUS._serialized_end = 418
