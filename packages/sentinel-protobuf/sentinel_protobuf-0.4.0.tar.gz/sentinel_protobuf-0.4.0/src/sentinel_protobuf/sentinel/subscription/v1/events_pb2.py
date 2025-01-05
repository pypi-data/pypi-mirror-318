
'Generated protocol buffer code.'
from google.protobuf.internal import builder as _builder
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
_sym_db = _symbol_database.Default()
from ....gogoproto import gogo_pb2 as gogoproto_dot_gogo__pb2
from ....sentinel.types.v1 import status_pb2 as sentinel_dot_types_dot_v1_dot_status__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n%sentinel/subscription/v1/events.proto\x12\x18sentinel.subscription.v1\x1a\x14gogoproto/gogo.proto\x1a\x1esentinel/types/v1/status.proto"O\n\rEventAddQuota\x12\x19\n\x02id\x18\x01 \x01(\x04B\r\xf2\xde\x1f\tyaml:"id"\x12#\n\x07address\x18\x02 \x01(\tB\x12\xf2\xde\x1f\x0eyaml:"address""i\n\x0eEventSetStatus\x12\x19\n\x02id\x18\x01 \x01(\x04B\r\xf2\xde\x1f\tyaml:"id"\x12<\n\x06status\x18\x02 \x01(\x0e2\x19.sentinel.types.v1.StatusB\x11\xf2\xde\x1f\ryaml:"status""i\n\x0eEventSubscribe\x12\x19\n\x02id\x18\x01 \x01(\x04B\r\xf2\xde\x1f\tyaml:"id"\x12\x1d\n\x04node\x18\x02 \x01(\tB\x0f\xf2\xde\x1f\x0byaml:"node"\x12\x1d\n\x04plan\x18\x03 \x01(\x04B\x0f\xf2\xde\x1f\x0byaml:"plan""R\n\x10EventUpdateQuota\x12\x19\n\x02id\x18\x01 \x01(\x04B\r\xf2\xde\x1f\tyaml:"id"\x12#\n\x07address\x18\x02 \x01(\tB\x12\xf2\xde\x1f\x0eyaml:"address"BFZ<github.com/sentinel-official/hub/v12/x/subscription/types/v1\xa8\xe2\x1e\x00\xc8\xe1\x1e\x00b\x06proto3')
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, globals())
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'sentinel.subscription.v1.events_pb2', globals())
if (_descriptor._USE_C_DESCRIPTORS == False):
    DESCRIPTOR._options = None
    DESCRIPTOR._serialized_options = b'Z<github.com/sentinel-official/hub/v12/x/subscription/types/v1\xa8\xe2\x1e\x00\xc8\xe1\x1e\x00'
    _EVENTADDQUOTA.fields_by_name['id']._options = None
    _EVENTADDQUOTA.fields_by_name['id']._serialized_options = b'\xf2\xde\x1f\tyaml:"id"'
    _EVENTADDQUOTA.fields_by_name['address']._options = None
    _EVENTADDQUOTA.fields_by_name['address']._serialized_options = b'\xf2\xde\x1f\x0eyaml:"address"'
    _EVENTSETSTATUS.fields_by_name['id']._options = None
    _EVENTSETSTATUS.fields_by_name['id']._serialized_options = b'\xf2\xde\x1f\tyaml:"id"'
    _EVENTSETSTATUS.fields_by_name['status']._options = None
    _EVENTSETSTATUS.fields_by_name['status']._serialized_options = b'\xf2\xde\x1f\ryaml:"status"'
    _EVENTSUBSCRIBE.fields_by_name['id']._options = None
    _EVENTSUBSCRIBE.fields_by_name['id']._serialized_options = b'\xf2\xde\x1f\tyaml:"id"'
    _EVENTSUBSCRIBE.fields_by_name['node']._options = None
    _EVENTSUBSCRIBE.fields_by_name['node']._serialized_options = b'\xf2\xde\x1f\x0byaml:"node"'
    _EVENTSUBSCRIBE.fields_by_name['plan']._options = None
    _EVENTSUBSCRIBE.fields_by_name['plan']._serialized_options = b'\xf2\xde\x1f\x0byaml:"plan"'
    _EVENTUPDATEQUOTA.fields_by_name['id']._options = None
    _EVENTUPDATEQUOTA.fields_by_name['id']._serialized_options = b'\xf2\xde\x1f\tyaml:"id"'
    _EVENTUPDATEQUOTA.fields_by_name['address']._options = None
    _EVENTUPDATEQUOTA.fields_by_name['address']._serialized_options = b'\xf2\xde\x1f\x0eyaml:"address"'
    _EVENTADDQUOTA._serialized_start = 121
    _EVENTADDQUOTA._serialized_end = 200
    _EVENTSETSTATUS._serialized_start = 202
    _EVENTSETSTATUS._serialized_end = 307
    _EVENTSUBSCRIBE._serialized_start = 309
    _EVENTSUBSCRIBE._serialized_end = 414
    _EVENTUPDATEQUOTA._serialized_start = 416
    _EVENTUPDATEQUOTA._serialized_end = 498
