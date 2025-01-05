"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_runtime_version.ValidateProtobufRuntimeVersion(_runtime_version.Domain.PUBLIC, 5, 28, 1, '', 'sentinel/mint/v1/inflation.proto')
_sym_db = _symbol_database.Default()
from ....gogoproto import gogo_pb2 as gogoproto_dot_gogo__pb2
from google.protobuf import timestamp_pb2 as google_dot_protobuf_dot_timestamp__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n sentinel/mint/v1/inflation.proto\x12\x10sentinel.mint.v1\x1a\x14gogoproto/gogo.proto\x1a\x1fgoogle/protobuf/timestamp.proto"\xa8\x02\n\tInflation\x12>\n\x03max\x18\x01 \x01(\tB1\xc8\xde\x1f\x00\xda\xde\x1f\x1bcosmossdk.io/math.LegacyDec\xf2\xde\x1f\nyaml:"max"\x12>\n\x03min\x18\x02 \x01(\tB1\xc8\xde\x1f\x00\xda\xde\x1f\x1bcosmossdk.io/math.LegacyDec\xf2\xde\x1f\nyaml:"min"\x12N\n\x0brate_change\x18\x03 \x01(\tB9\xc8\xde\x1f\x00\xda\xde\x1f\x1bcosmossdk.io/math.LegacyDec\xf2\xde\x1f\x12yaml:"rate_change"\x12K\n\ttimestamp\x18\x04 \x01(\x0b2\x1a.google.protobuf.TimestampB\x1c\xc8\xde\x1f\x00\xf2\xde\x1f\x10yaml:"timestamp"\x90\xdf\x1f\x01B>Z4github.com/sentinel-official/hub/v12/x/mint/types/v1\xc8\xe1\x1e\x00\xa8\xe2\x1e\x00b\x06proto3')
_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'sentinel.mint.v1.inflation_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
    _globals['DESCRIPTOR']._loaded_options = None
    _globals['DESCRIPTOR']._serialized_options = b'Z4github.com/sentinel-official/hub/v12/x/mint/types/v1\xc8\xe1\x1e\x00\xa8\xe2\x1e\x00'
    _globals['_INFLATION'].fields_by_name['max']._loaded_options = None
    _globals['_INFLATION'].fields_by_name['max']._serialized_options = b'\xc8\xde\x1f\x00\xda\xde\x1f\x1bcosmossdk.io/math.LegacyDec\xf2\xde\x1f\nyaml:"max"'
    _globals['_INFLATION'].fields_by_name['min']._loaded_options = None
    _globals['_INFLATION'].fields_by_name['min']._serialized_options = b'\xc8\xde\x1f\x00\xda\xde\x1f\x1bcosmossdk.io/math.LegacyDec\xf2\xde\x1f\nyaml:"min"'
    _globals['_INFLATION'].fields_by_name['rate_change']._loaded_options = None
    _globals['_INFLATION'].fields_by_name['rate_change']._serialized_options = b'\xc8\xde\x1f\x00\xda\xde\x1f\x1bcosmossdk.io/math.LegacyDec\xf2\xde\x1f\x12yaml:"rate_change"'
    _globals['_INFLATION'].fields_by_name['timestamp']._loaded_options = None
    _globals['_INFLATION'].fields_by_name['timestamp']._serialized_options = b'\xc8\xde\x1f\x00\xf2\xde\x1f\x10yaml:"timestamp"\x90\xdf\x1f\x01'
    _globals['_INFLATION']._serialized_start = 110
    _globals['_INFLATION']._serialized_end = 406