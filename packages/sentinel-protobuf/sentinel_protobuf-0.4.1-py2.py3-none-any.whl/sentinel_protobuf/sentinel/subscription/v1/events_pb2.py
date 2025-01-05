"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_runtime_version.ValidateProtobufRuntimeVersion(_runtime_version.Domain.PUBLIC, 5, 28, 1, '', 'sentinel/subscription/v1/events.proto')
_sym_db = _symbol_database.Default()
from ....gogoproto import gogo_pb2 as gogoproto_dot_gogo__pb2
from ....sentinel.types.v1 import status_pb2 as sentinel_dot_types_dot_v1_dot_status__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n%sentinel/subscription/v1/events.proto\x12\x18sentinel.subscription.v1\x1a\x14gogoproto/gogo.proto\x1a\x1esentinel/types/v1/status.proto"O\n\rEventAddQuota\x12\x19\n\x02id\x18\x01 \x01(\x04B\r\xf2\xde\x1f\tyaml:"id"\x12#\n\x07address\x18\x02 \x01(\tB\x12\xf2\xde\x1f\x0eyaml:"address""i\n\x0eEventSetStatus\x12\x19\n\x02id\x18\x01 \x01(\x04B\r\xf2\xde\x1f\tyaml:"id"\x12<\n\x06status\x18\x02 \x01(\x0e2\x19.sentinel.types.v1.StatusB\x11\xf2\xde\x1f\ryaml:"status""i\n\x0eEventSubscribe\x12\x19\n\x02id\x18\x01 \x01(\x04B\r\xf2\xde\x1f\tyaml:"id"\x12\x1d\n\x04node\x18\x02 \x01(\tB\x0f\xf2\xde\x1f\x0byaml:"node"\x12\x1d\n\x04plan\x18\x03 \x01(\x04B\x0f\xf2\xde\x1f\x0byaml:"plan""R\n\x10EventUpdateQuota\x12\x19\n\x02id\x18\x01 \x01(\x04B\r\xf2\xde\x1f\tyaml:"id"\x12#\n\x07address\x18\x02 \x01(\tB\x12\xf2\xde\x1f\x0eyaml:"address"BFZ<github.com/sentinel-official/hub/v12/x/subscription/types/v1\xc8\xe1\x1e\x00\xa8\xe2\x1e\x00b\x06proto3')
_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'sentinel.subscription.v1.events_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
    _globals['DESCRIPTOR']._loaded_options = None
    _globals['DESCRIPTOR']._serialized_options = b'Z<github.com/sentinel-official/hub/v12/x/subscription/types/v1\xc8\xe1\x1e\x00\xa8\xe2\x1e\x00'
    _globals['_EVENTADDQUOTA'].fields_by_name['id']._loaded_options = None
    _globals['_EVENTADDQUOTA'].fields_by_name['id']._serialized_options = b'\xf2\xde\x1f\tyaml:"id"'
    _globals['_EVENTADDQUOTA'].fields_by_name['address']._loaded_options = None
    _globals['_EVENTADDQUOTA'].fields_by_name['address']._serialized_options = b'\xf2\xde\x1f\x0eyaml:"address"'
    _globals['_EVENTSETSTATUS'].fields_by_name['id']._loaded_options = None
    _globals['_EVENTSETSTATUS'].fields_by_name['id']._serialized_options = b'\xf2\xde\x1f\tyaml:"id"'
    _globals['_EVENTSETSTATUS'].fields_by_name['status']._loaded_options = None
    _globals['_EVENTSETSTATUS'].fields_by_name['status']._serialized_options = b'\xf2\xde\x1f\ryaml:"status"'
    _globals['_EVENTSUBSCRIBE'].fields_by_name['id']._loaded_options = None
    _globals['_EVENTSUBSCRIBE'].fields_by_name['id']._serialized_options = b'\xf2\xde\x1f\tyaml:"id"'
    _globals['_EVENTSUBSCRIBE'].fields_by_name['node']._loaded_options = None
    _globals['_EVENTSUBSCRIBE'].fields_by_name['node']._serialized_options = b'\xf2\xde\x1f\x0byaml:"node"'
    _globals['_EVENTSUBSCRIBE'].fields_by_name['plan']._loaded_options = None
    _globals['_EVENTSUBSCRIBE'].fields_by_name['plan']._serialized_options = b'\xf2\xde\x1f\x0byaml:"plan"'
    _globals['_EVENTUPDATEQUOTA'].fields_by_name['id']._loaded_options = None
    _globals['_EVENTUPDATEQUOTA'].fields_by_name['id']._serialized_options = b'\xf2\xde\x1f\tyaml:"id"'
    _globals['_EVENTUPDATEQUOTA'].fields_by_name['address']._loaded_options = None
    _globals['_EVENTUPDATEQUOTA'].fields_by_name['address']._serialized_options = b'\xf2\xde\x1f\x0eyaml:"address"'
    _globals['_EVENTADDQUOTA']._serialized_start = 121
    _globals['_EVENTADDQUOTA']._serialized_end = 200
    _globals['_EVENTSETSTATUS']._serialized_start = 202
    _globals['_EVENTSETSTATUS']._serialized_end = 307
    _globals['_EVENTSUBSCRIBE']._serialized_start = 309
    _globals['_EVENTSUBSCRIBE']._serialized_end = 414
    _globals['_EVENTUPDATEQUOTA']._serialized_start = 416
    _globals['_EVENTUPDATEQUOTA']._serialized_end = 498