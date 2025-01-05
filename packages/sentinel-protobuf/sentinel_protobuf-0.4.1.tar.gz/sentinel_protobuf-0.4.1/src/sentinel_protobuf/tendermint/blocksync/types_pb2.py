"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_runtime_version.ValidateProtobufRuntimeVersion(_runtime_version.Domain.PUBLIC, 5, 28, 1, '', 'tendermint/blocksync/types.proto')
_sym_db = _symbol_database.Default()
from ...tendermint.types import block_pb2 as tendermint_dot_types_dot_block__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n tendermint/blocksync/types.proto\x12\x14tendermint.blocksync\x1a\x1ctendermint/types/block.proto"\x1e\n\x0cBlockRequest\x12\x0e\n\x06height\x18\x01 \x01(\x03"!\n\x0fNoBlockResponse\x12\x0e\n\x06height\x18\x01 \x01(\x03"7\n\rBlockResponse\x12&\n\x05block\x18\x01 \x01(\x0b2\x17.tendermint.types.Block"\x0f\n\rStatusRequest".\n\x0eStatusResponse\x12\x0e\n\x06height\x18\x01 \x01(\x03\x12\x0c\n\x04base\x18\x02 \x01(\x03"\xd0\x02\n\x07Message\x12;\n\rblock_request\x18\x01 \x01(\x0b2".tendermint.blocksync.BlockRequestH\x00\x12B\n\x11no_block_response\x18\x02 \x01(\x0b2%.tendermint.blocksync.NoBlockResponseH\x00\x12=\n\x0eblock_response\x18\x03 \x01(\x0b2#.tendermint.blocksync.BlockResponseH\x00\x12=\n\x0estatus_request\x18\x04 \x01(\x0b2#.tendermint.blocksync.StatusRequestH\x00\x12?\n\x0fstatus_response\x18\x05 \x01(\x0b2$.tendermint.blocksync.StatusResponseH\x00B\x05\n\x03sumB9Z7github.com/cometbft/cometbft/proto/tendermint/blocksyncb\x06proto3')
_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'tendermint.blocksync.types_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
    _globals['DESCRIPTOR']._loaded_options = None
    _globals['DESCRIPTOR']._serialized_options = b'Z7github.com/cometbft/cometbft/proto/tendermint/blocksync'
    _globals['_BLOCKREQUEST']._serialized_start = 88
    _globals['_BLOCKREQUEST']._serialized_end = 118
    _globals['_NOBLOCKRESPONSE']._serialized_start = 120
    _globals['_NOBLOCKRESPONSE']._serialized_end = 153
    _globals['_BLOCKRESPONSE']._serialized_start = 155
    _globals['_BLOCKRESPONSE']._serialized_end = 210
    _globals['_STATUSREQUEST']._serialized_start = 212
    _globals['_STATUSREQUEST']._serialized_end = 227
    _globals['_STATUSRESPONSE']._serialized_start = 229
    _globals['_STATUSRESPONSE']._serialized_end = 275
    _globals['_MESSAGE']._serialized_start = 278
    _globals['_MESSAGE']._serialized_end = 614