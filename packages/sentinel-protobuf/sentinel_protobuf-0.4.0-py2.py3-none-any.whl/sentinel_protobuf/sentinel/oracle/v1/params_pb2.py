
'Generated protocol buffer code.'
from google.protobuf.internal import builder as _builder
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
_sym_db = _symbol_database.Default()
from ....gogoproto import gogo_pb2 as gogoproto_dot_gogo__pb2
from google.protobuf import duration_pb2 as google_dot_protobuf_dot_duration__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x1fsentinel/oracle/v1/params.proto\x12\x12sentinel.oracle.v1\x1a\x14gogoproto/gogo.proto\x1a\x1egoogle/protobuf/duration.proto"\x96\x01\n\x06Params\x12\x16\n\x0eblock_interval\x18\x01 \x01(\x03\x12!\n\nchannel_id\x18\x02 \x01(\tB\r\xe2\xde\x1f\tChannelID\x12\x1b\n\x07port_id\x18\x03 \x01(\tB\n\xe2\xde\x1f\x06PortID\x124\n\x07timeout\x18\x04 \x01(\x0b2\x19.google.protobuf.DurationB\x08\xc8\xde\x1f\x00\x98\xdf\x1f\x01B@Z6github.com/sentinel-official/hub/v12/x/oracle/types/v1\xa8\xe2\x1e\x00\xc8\xe1\x1e\x00b\x06proto3')
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, globals())
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'sentinel.oracle.v1.params_pb2', globals())
if (_descriptor._USE_C_DESCRIPTORS == False):
    DESCRIPTOR._options = None
    DESCRIPTOR._serialized_options = b'Z6github.com/sentinel-official/hub/v12/x/oracle/types/v1\xa8\xe2\x1e\x00\xc8\xe1\x1e\x00'
    _PARAMS.fields_by_name['channel_id']._options = None
    _PARAMS.fields_by_name['channel_id']._serialized_options = b'\xe2\xde\x1f\tChannelID'
    _PARAMS.fields_by_name['port_id']._options = None
    _PARAMS.fields_by_name['port_id']._serialized_options = b'\xe2\xde\x1f\x06PortID'
    _PARAMS.fields_by_name['timeout']._options = None
    _PARAMS.fields_by_name['timeout']._serialized_options = b'\xc8\xde\x1f\x00\x98\xdf\x1f\x01'
    _PARAMS._serialized_start = 110
    _PARAMS._serialized_end = 260
