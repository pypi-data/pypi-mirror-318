"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_runtime_version.ValidateProtobufRuntimeVersion(_runtime_version.Domain.PUBLIC, 5, 28, 1, '', 'sentinel/deposit/v1/events.proto')
_sym_db = _symbol_database.Default()
from ....gogoproto import gogo_pb2 as gogoproto_dot_gogo__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n sentinel/deposit/v1/events.proto\x12\x13sentinel.deposit.v1\x1a\x14gogoproto/gogo.proto"P\n\x08EventAdd\x12#\n\x07address\x18\x01 \x01(\tB\x12\xf2\xde\x1f\x0eyaml:"address"\x12\x1f\n\x05coins\x18\x02 \x01(\tB\x10\xf2\xde\x1f\x0cyaml:"coins""U\n\rEventSubtract\x12#\n\x07address\x18\x01 \x01(\tB\x12\xf2\xde\x1f\x0eyaml:"address"\x12\x1f\n\x05coins\x18\x02 \x01(\tB\x10\xf2\xde\x1f\x0cyaml:"coins"BAZ7github.com/sentinel-official/hub/v12/x/deposit/types/v1\xc8\xe1\x1e\x00\xa8\xe2\x1e\x00b\x06proto3')
_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'sentinel.deposit.v1.events_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
    _globals['DESCRIPTOR']._loaded_options = None
    _globals['DESCRIPTOR']._serialized_options = b'Z7github.com/sentinel-official/hub/v12/x/deposit/types/v1\xc8\xe1\x1e\x00\xa8\xe2\x1e\x00'
    _globals['_EVENTADD'].fields_by_name['address']._loaded_options = None
    _globals['_EVENTADD'].fields_by_name['address']._serialized_options = b'\xf2\xde\x1f\x0eyaml:"address"'
    _globals['_EVENTADD'].fields_by_name['coins']._loaded_options = None
    _globals['_EVENTADD'].fields_by_name['coins']._serialized_options = b'\xf2\xde\x1f\x0cyaml:"coins"'
    _globals['_EVENTSUBTRACT'].fields_by_name['address']._loaded_options = None
    _globals['_EVENTSUBTRACT'].fields_by_name['address']._serialized_options = b'\xf2\xde\x1f\x0eyaml:"address"'
    _globals['_EVENTSUBTRACT'].fields_by_name['coins']._loaded_options = None
    _globals['_EVENTSUBTRACT'].fields_by_name['coins']._serialized_options = b'\xf2\xde\x1f\x0cyaml:"coins"'
    _globals['_EVENTADD']._serialized_start = 79
    _globals['_EVENTADD']._serialized_end = 159
    _globals['_EVENTSUBTRACT']._serialized_start = 161
    _globals['_EVENTSUBTRACT']._serialized_end = 246