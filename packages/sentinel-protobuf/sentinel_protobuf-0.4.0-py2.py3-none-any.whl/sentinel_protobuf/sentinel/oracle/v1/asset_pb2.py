
'Generated protocol buffer code.'
from google.protobuf.internal import builder as _builder
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
_sym_db = _symbol_database.Default()
from ....gogoproto import gogo_pb2 as gogoproto_dot_gogo__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x1esentinel/oracle/v1/asset.proto\x12\x12sentinel.oracle.v1\x1a\x14gogoproto/gogo.proto"\x9b\x01\n\x05Asset\x12\r\n\x05denom\x18\x01 \x01(\t\x12\x10\n\x08decimals\x18\x02 \x01(\x03\x12\x18\n\x10base_asset_denom\x18\x03 \x01(\t\x12\x19\n\x11quote_asset_denom\x18\x04 \x01(\t\x12,\n\x05price\x18\x05 \x01(\tB\x1d\xda\xde\x1f\x15cosmossdk.io/math.Int\xc8\xde\x1f\x00\x12\x0e\n\x06height\x18\x06 \x01(\x03B@Z6github.com/sentinel-official/hub/v12/x/oracle/types/v1\xa8\xe2\x1e\x00\xc8\xe1\x1e\x00b\x06proto3')
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, globals())
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'sentinel.oracle.v1.asset_pb2', globals())
if (_descriptor._USE_C_DESCRIPTORS == False):
    DESCRIPTOR._options = None
    DESCRIPTOR._serialized_options = b'Z6github.com/sentinel-official/hub/v12/x/oracle/types/v1\xa8\xe2\x1e\x00\xc8\xe1\x1e\x00'
    _ASSET.fields_by_name['price']._options = None
    _ASSET.fields_by_name['price']._serialized_options = b'\xda\xde\x1f\x15cosmossdk.io/math.Int\xc8\xde\x1f\x00'
    _ASSET._serialized_start = 77
    _ASSET._serialized_end = 232
