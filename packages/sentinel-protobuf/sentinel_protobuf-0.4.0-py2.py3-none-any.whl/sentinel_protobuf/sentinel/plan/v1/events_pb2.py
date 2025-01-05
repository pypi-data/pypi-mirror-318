
'Generated protocol buffer code.'
from google.protobuf.internal import builder as _builder
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
_sym_db = _symbol_database.Default()
from ....gogoproto import gogo_pb2 as gogoproto_dot_gogo__pb2
from ....sentinel.types.v1 import status_pb2 as sentinel_dot_types_dot_v1_dot_status__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x1dsentinel/plan/v1/events.proto\x12\x10sentinel.plan.v1\x1a\x14gogoproto/gogo.proto\x1a\x1esentinel/types/v1/status.proto"L\n\x08EventAdd\x12\x19\n\x02id\x18\x01 \x01(\x04B\r\xf2\xde\x1f\tyaml:"id"\x12%\n\x08provider\x18\x02 \x01(\tB\x13\xf2\xde\x1f\x0fyaml:"provider""o\n\x0cEventAddNode\x12\x19\n\x02id\x18\x01 \x01(\x04B\r\xf2\xde\x1f\tyaml:"id"\x12\x1d\n\x04node\x18\x02 \x01(\tB\x0f\xf2\xde\x1f\x0byaml:"node"\x12%\n\x08provider\x18\x03 \x01(\tB\x13\xf2\xde\x1f\x0fyaml:"provider""r\n\x0fEventRemoveNode\x12\x19\n\x02id\x18\x01 \x01(\x04B\r\xf2\xde\x1f\tyaml:"id"\x12\x1d\n\x04node\x18\x02 \x01(\tB\x0f\xf2\xde\x1f\x0byaml:"node"\x12%\n\x08provider\x18\x03 \x01(\tB\x13\xf2\xde\x1f\x0fyaml:"provider""\x90\x01\n\x0eEventSetStatus\x12\x19\n\x02id\x18\x01 \x01(\x04B\r\xf2\xde\x1f\tyaml:"id"\x12%\n\x08provider\x18\x02 \x01(\tB\x13\xf2\xde\x1f\x0fyaml:"provider"\x12<\n\x06status\x18\x03 \x01(\x0e2\x19.sentinel.types.v1.StatusB\x11\xf2\xde\x1f\ryaml:"status"B>Z4github.com/sentinel-official/hub/v12/x/plan/types/v1\xa8\xe2\x1e\x00\xc8\xe1\x1e\x00b\x06proto3')
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, globals())
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'sentinel.plan.v1.events_pb2', globals())
if (_descriptor._USE_C_DESCRIPTORS == False):
    DESCRIPTOR._options = None
    DESCRIPTOR._serialized_options = b'Z4github.com/sentinel-official/hub/v12/x/plan/types/v1\xa8\xe2\x1e\x00\xc8\xe1\x1e\x00'
    _EVENTADD.fields_by_name['id']._options = None
    _EVENTADD.fields_by_name['id']._serialized_options = b'\xf2\xde\x1f\tyaml:"id"'
    _EVENTADD.fields_by_name['provider']._options = None
    _EVENTADD.fields_by_name['provider']._serialized_options = b'\xf2\xde\x1f\x0fyaml:"provider"'
    _EVENTADDNODE.fields_by_name['id']._options = None
    _EVENTADDNODE.fields_by_name['id']._serialized_options = b'\xf2\xde\x1f\tyaml:"id"'
    _EVENTADDNODE.fields_by_name['node']._options = None
    _EVENTADDNODE.fields_by_name['node']._serialized_options = b'\xf2\xde\x1f\x0byaml:"node"'
    _EVENTADDNODE.fields_by_name['provider']._options = None
    _EVENTADDNODE.fields_by_name['provider']._serialized_options = b'\xf2\xde\x1f\x0fyaml:"provider"'
    _EVENTREMOVENODE.fields_by_name['id']._options = None
    _EVENTREMOVENODE.fields_by_name['id']._serialized_options = b'\xf2\xde\x1f\tyaml:"id"'
    _EVENTREMOVENODE.fields_by_name['node']._options = None
    _EVENTREMOVENODE.fields_by_name['node']._serialized_options = b'\xf2\xde\x1f\x0byaml:"node"'
    _EVENTREMOVENODE.fields_by_name['provider']._options = None
    _EVENTREMOVENODE.fields_by_name['provider']._serialized_options = b'\xf2\xde\x1f\x0fyaml:"provider"'
    _EVENTSETSTATUS.fields_by_name['id']._options = None
    _EVENTSETSTATUS.fields_by_name['id']._serialized_options = b'\xf2\xde\x1f\tyaml:"id"'
    _EVENTSETSTATUS.fields_by_name['provider']._options = None
    _EVENTSETSTATUS.fields_by_name['provider']._serialized_options = b'\xf2\xde\x1f\x0fyaml:"provider"'
    _EVENTSETSTATUS.fields_by_name['status']._options = None
    _EVENTSETSTATUS.fields_by_name['status']._serialized_options = b'\xf2\xde\x1f\ryaml:"status"'
    _EVENTADD._serialized_start = 105
    _EVENTADD._serialized_end = 181
    _EVENTADDNODE._serialized_start = 183
    _EVENTADDNODE._serialized_end = 294
    _EVENTREMOVENODE._serialized_start = 296
    _EVENTREMOVENODE._serialized_end = 410
    _EVENTSETSTATUS._serialized_start = 413
    _EVENTSETSTATUS._serialized_end = 557
