"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_runtime_version.ValidateProtobufRuntimeVersion(_runtime_version.Domain.PUBLIC, 5, 28, 1, '', 'sentinel/session/v3/events.proto')
_sym_db = _symbol_database.Default()
from ....gogoproto import gogo_pb2 as gogoproto_dot_gogo__pb2
from google.protobuf import duration_pb2 as google_dot_protobuf_dot_duration__pb2
from ....sentinel.types.v1 import status_pb2 as sentinel_dot_types_dot_v1_dot_status__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n sentinel/session/v3/events.proto\x12\x13sentinel.session.v3\x1a\x14gogoproto/gogo.proto\x1a\x1egoogle/protobuf/duration.proto\x1a\x1esentinel/types/v1/status.proto"r\n\x08EventPay\x12\x12\n\x02id\x18\x01 \x01(\x04B\x06\xe2\xde\x1f\x02ID\x12\x13\n\x0bacc_address\x18\x02 \x01(\t\x12\x14\n\x0cnode_address\x18\x03 \x01(\t\x12\x0f\n\x07payment\x18\x04 \x01(\t\x12\x16\n\x0estaking_reward\x18\x05 \x01(\t"F\n\x0bEventRefund\x12\x12\n\x02id\x18\x01 \x01(\x04B\x06\xe2\xde\x1f\x02ID\x12\x13\n\x0bacc_address\x18\x02 \x01(\t\x12\x0e\n\x06amount\x18\x03 \x01(\t"\xb8\x01\n\x12EventUpdateDetails\x12\x12\n\x02id\x18\x01 \x01(\x04B\x06\xe2\xde\x1f\x02ID\x12\x13\n\x0bacc_address\x18\x02 \x01(\t\x12\x14\n\x0cnode_address\x18\x03 \x01(\t\x12\x16\n\x0edownload_bytes\x18\x04 \x01(\t\x12\x14\n\x0cupload_bytes\x18\x05 \x01(\t\x125\n\x08duration\x18\x06 \x01(\x0b2\x19.google.protobuf.DurationB\x08\xc8\xde\x1f\x00\x98\xdf\x1f\x01"\x90\x01\n\x11EventUpdateStatus\x12\x12\n\x02id\x18\x01 \x01(\x04B\x06\xe2\xde\x1f\x02ID\x12\x13\n\x0bacc_address\x18\x02 \x01(\t\x12\x14\n\x0cnode_address\x18\x03 \x01(\t\x12)\n\x06status\x18\x04 \x01(\x0e2\x19.sentinel.types.v1.Status\x12\x11\n\tstatus_at\x18\x05 \x01(\tBAZ7github.com/sentinel-official/hub/v12/x/session/types/v3\xc8\xe1\x1e\x00\xa8\xe2\x1e\x00b\x06proto3')
_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'sentinel.session.v3.events_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
    _globals['DESCRIPTOR']._loaded_options = None
    _globals['DESCRIPTOR']._serialized_options = b'Z7github.com/sentinel-official/hub/v12/x/session/types/v3\xc8\xe1\x1e\x00\xa8\xe2\x1e\x00'
    _globals['_EVENTPAY'].fields_by_name['id']._loaded_options = None
    _globals['_EVENTPAY'].fields_by_name['id']._serialized_options = b'\xe2\xde\x1f\x02ID'
    _globals['_EVENTREFUND'].fields_by_name['id']._loaded_options = None
    _globals['_EVENTREFUND'].fields_by_name['id']._serialized_options = b'\xe2\xde\x1f\x02ID'
    _globals['_EVENTUPDATEDETAILS'].fields_by_name['id']._loaded_options = None
    _globals['_EVENTUPDATEDETAILS'].fields_by_name['id']._serialized_options = b'\xe2\xde\x1f\x02ID'
    _globals['_EVENTUPDATEDETAILS'].fields_by_name['duration']._loaded_options = None
    _globals['_EVENTUPDATEDETAILS'].fields_by_name['duration']._serialized_options = b'\xc8\xde\x1f\x00\x98\xdf\x1f\x01'
    _globals['_EVENTUPDATESTATUS'].fields_by_name['id']._loaded_options = None
    _globals['_EVENTUPDATESTATUS'].fields_by_name['id']._serialized_options = b'\xe2\xde\x1f\x02ID'
    _globals['_EVENTPAY']._serialized_start = 143
    _globals['_EVENTPAY']._serialized_end = 257
    _globals['_EVENTREFUND']._serialized_start = 259
    _globals['_EVENTREFUND']._serialized_end = 329
    _globals['_EVENTUPDATEDETAILS']._serialized_start = 332
    _globals['_EVENTUPDATEDETAILS']._serialized_end = 516
    _globals['_EVENTUPDATESTATUS']._serialized_start = 519
    _globals['_EVENTUPDATESTATUS']._serialized_end = 663