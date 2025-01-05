"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_runtime_version.ValidateProtobufRuntimeVersion(_runtime_version.Domain.PUBLIC, 5, 28, 1, '', 'sentinel/oracle/v1/events.proto')
_sym_db = _symbol_database.Default()
from ....gogoproto import gogo_pb2 as gogoproto_dot_gogo__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x1fsentinel/oracle/v1/events.proto\x12\x12sentinel.oracle.v1\x1a\x14gogoproto/gogo.proto"c\n\x0bEventCreate\x12\r\n\x05denom\x18\x02 \x01(\t\x12\x10\n\x08decimals\x18\x03 \x01(\x03\x12\x18\n\x10base_asset_denom\x18\x04 \x01(\t\x12\x19\n\x11quote_asset_denom\x18\x05 \x01(\t"\x1c\n\x0bEventDelete\x12\r\n\x05denom\x18\x02 \x01(\t"c\n\x0bEventUpdate\x12\r\n\x05denom\x18\x02 \x01(\t\x12\x10\n\x08decimals\x18\x03 \x01(\x03\x12\x18\n\x10base_asset_denom\x18\x04 \x01(\t\x12\x19\n\x11quote_asset_denom\x18\x05 \x01(\tB@Z6github.com/sentinel-official/hub/v12/x/oracle/types/v1\xc8\xe1\x1e\x00\xa8\xe2\x1e\x00b\x06proto3')
_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'sentinel.oracle.v1.events_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
    _globals['DESCRIPTOR']._loaded_options = None
    _globals['DESCRIPTOR']._serialized_options = b'Z6github.com/sentinel-official/hub/v12/x/oracle/types/v1\xc8\xe1\x1e\x00\xa8\xe2\x1e\x00'
    _globals['_EVENTCREATE']._serialized_start = 77
    _globals['_EVENTCREATE']._serialized_end = 176
    _globals['_EVENTDELETE']._serialized_start = 178
    _globals['_EVENTDELETE']._serialized_end = 206
    _globals['_EVENTUPDATE']._serialized_start = 208
    _globals['_EVENTUPDATE']._serialized_end = 307