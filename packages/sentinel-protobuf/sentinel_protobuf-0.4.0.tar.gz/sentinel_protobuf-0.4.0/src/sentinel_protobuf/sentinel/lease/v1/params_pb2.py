
'Generated protocol buffer code.'
from google.protobuf.internal import builder as _builder
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
_sym_db = _symbol_database.Default()
from ....gogoproto import gogo_pb2 as gogoproto_dot_gogo__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x1esentinel/lease/v1/params.proto\x12\x11sentinel.lease.v1\x1a\x14gogoproto/gogo.proto"v\n\x06Params\x12\x17\n\x0fmax_lease_hours\x18\x01 \x01(\x03\x12\x17\n\x0fmin_lease_hours\x18\x02 \x01(\x03\x12:\n\rstaking_share\x18\x03 \x01(\tB#\xda\xde\x1f\x1bcosmossdk.io/math.LegacyDec\xc8\xde\x1f\x00B?Z5github.com/sentinel-official/hub/v12/x/lease/types/v1\xa8\xe2\x1e\x00\xc8\xe1\x1e\x00b\x06proto3')
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, globals())
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'sentinel.lease.v1.params_pb2', globals())
if (_descriptor._USE_C_DESCRIPTORS == False):
    DESCRIPTOR._options = None
    DESCRIPTOR._serialized_options = b'Z5github.com/sentinel-official/hub/v12/x/lease/types/v1\xa8\xe2\x1e\x00\xc8\xe1\x1e\x00'
    _PARAMS.fields_by_name['staking_share']._options = None
    _PARAMS.fields_by_name['staking_share']._serialized_options = b'\xda\xde\x1f\x1bcosmossdk.io/math.LegacyDec\xc8\xde\x1f\x00'
    _PARAMS._serialized_start = 75
    _PARAMS._serialized_end = 193
