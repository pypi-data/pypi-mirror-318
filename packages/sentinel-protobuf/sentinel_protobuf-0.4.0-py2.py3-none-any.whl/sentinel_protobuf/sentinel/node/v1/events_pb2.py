
'Generated protocol buffer code.'
from google.protobuf.internal import builder as _builder
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
_sym_db = _symbol_database.Default()
from ....gogoproto import gogo_pb2 as gogoproto_dot_gogo__pb2
from ....sentinel.types.v1 import status_pb2 as sentinel_dot_types_dot_v1_dot_status__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x1dsentinel/node/v1/events.proto\x12\x10sentinel.node.v1\x1a\x14gogoproto/gogo.proto\x1a\x1esentinel/types/v1/status.proto"[\n\rEventRegister\x12#\n\x07address\x18\x01 \x01(\tB\x12\xf2\xde\x1f\x0eyaml:"address"\x12%\n\x08provider\x18\x02 \x01(\tB\x13\xf2\xde\x1f\x0fyaml:"provider""s\n\x0eEventSetStatus\x12#\n\x07address\x18\x01 \x01(\tB\x12\xf2\xde\x1f\x0eyaml:"address"\x12<\n\x06status\x18\x02 \x01(\x0e2\x19.sentinel.types.v1.StatusB\x11\xf2\xde\x1f\ryaml:"status""Y\n\x0bEventUpdate\x12#\n\x07address\x18\x01 \x01(\tB\x12\xf2\xde\x1f\x0eyaml:"address"\x12%\n\x08provider\x18\x02 \x01(\tB\x13\xf2\xde\x1f\x0fyaml:"provider"B>Z4github.com/sentinel-official/hub/v12/x/node/types/v1\xa8\xe2\x1e\x00\xc8\xe1\x1e\x00b\x06proto3')
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, globals())
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'sentinel.node.v1.events_pb2', globals())
if (_descriptor._USE_C_DESCRIPTORS == False):
    DESCRIPTOR._options = None
    DESCRIPTOR._serialized_options = b'Z4github.com/sentinel-official/hub/v12/x/node/types/v1\xa8\xe2\x1e\x00\xc8\xe1\x1e\x00'
    _EVENTREGISTER.fields_by_name['address']._options = None
    _EVENTREGISTER.fields_by_name['address']._serialized_options = b'\xf2\xde\x1f\x0eyaml:"address"'
    _EVENTREGISTER.fields_by_name['provider']._options = None
    _EVENTREGISTER.fields_by_name['provider']._serialized_options = b'\xf2\xde\x1f\x0fyaml:"provider"'
    _EVENTSETSTATUS.fields_by_name['address']._options = None
    _EVENTSETSTATUS.fields_by_name['address']._serialized_options = b'\xf2\xde\x1f\x0eyaml:"address"'
    _EVENTSETSTATUS.fields_by_name['status']._options = None
    _EVENTSETSTATUS.fields_by_name['status']._serialized_options = b'\xf2\xde\x1f\ryaml:"status"'
    _EVENTUPDATE.fields_by_name['address']._options = None
    _EVENTUPDATE.fields_by_name['address']._serialized_options = b'\xf2\xde\x1f\x0eyaml:"address"'
    _EVENTUPDATE.fields_by_name['provider']._options = None
    _EVENTUPDATE.fields_by_name['provider']._serialized_options = b'\xf2\xde\x1f\x0fyaml:"provider"'
    _EVENTREGISTER._serialized_start = 105
    _EVENTREGISTER._serialized_end = 196
    _EVENTSETSTATUS._serialized_start = 198
    _EVENTSETSTATUS._serialized_end = 313
    _EVENTUPDATE._serialized_start = 315
    _EVENTUPDATE._serialized_end = 404
