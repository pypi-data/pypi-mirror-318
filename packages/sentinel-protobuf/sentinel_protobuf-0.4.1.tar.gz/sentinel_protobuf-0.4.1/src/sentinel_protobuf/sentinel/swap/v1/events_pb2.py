"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_runtime_version.ValidateProtobufRuntimeVersion(_runtime_version.Domain.PUBLIC, 5, 28, 1, '', 'sentinel/swap/v1/events.proto')
_sym_db = _symbol_database.Default()
from ....gogoproto import gogo_pb2 as gogoproto_dot_gogo__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x1dsentinel/swap/v1/events.proto\x12\x10sentinel.swap.v1\x1a\x14gogoproto/gogo.proto"W\n\tEventSwap\x12#\n\x07tx_hash\x18\x01 \x01(\x0cB\x12\xf2\xde\x1f\x0eyaml:"tx_hash"\x12%\n\x08receiver\x18\x02 \x01(\tB\x13\xf2\xde\x1f\x0fyaml:"receiver"B>Z4github.com/sentinel-official/hub/v12/x/swap/types/v1\xc8\xe1\x1e\x00\xa8\xe2\x1e\x00b\x06proto3')
_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'sentinel.swap.v1.events_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
    _globals['DESCRIPTOR']._loaded_options = None
    _globals['DESCRIPTOR']._serialized_options = b'Z4github.com/sentinel-official/hub/v12/x/swap/types/v1\xc8\xe1\x1e\x00\xa8\xe2\x1e\x00'
    _globals['_EVENTSWAP'].fields_by_name['tx_hash']._loaded_options = None
    _globals['_EVENTSWAP'].fields_by_name['tx_hash']._serialized_options = b'\xf2\xde\x1f\x0eyaml:"tx_hash"'
    _globals['_EVENTSWAP'].fields_by_name['receiver']._loaded_options = None
    _globals['_EVENTSWAP'].fields_by_name['receiver']._serialized_options = b'\xf2\xde\x1f\x0fyaml:"receiver"'
    _globals['_EVENTSWAP']._serialized_start = 73
    _globals['_EVENTSWAP']._serialized_end = 160