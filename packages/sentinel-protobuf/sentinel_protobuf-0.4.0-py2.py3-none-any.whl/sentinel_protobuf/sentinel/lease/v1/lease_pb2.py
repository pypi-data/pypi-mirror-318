
'Generated protocol buffer code.'
from google.protobuf.internal import builder as _builder
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
_sym_db = _symbol_database.Default()
from ....gogoproto import gogo_pb2 as gogoproto_dot_gogo__pb2
from google.protobuf import timestamp_pb2 as google_dot_protobuf_dot_timestamp__pb2
from ....sentinel.types.v1 import price_pb2 as sentinel_dot_types_dot_v1_dot_price__pb2
from ....sentinel.types.v1 import renewal_pb2 as sentinel_dot_types_dot_v1_dot_renewal__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x1dsentinel/lease/v1/lease.proto\x12\x11sentinel.lease.v1\x1a\x14gogoproto/gogo.proto\x1a\x1fgoogle/protobuf/timestamp.proto\x1a\x1dsentinel/types/v1/price.proto\x1a\x1fsentinel/types/v1/renewal.proto"\xd1\x02\n\x05Lease\x12\x12\n\x02id\x18\x01 \x01(\x04B\x06\xe2\xde\x1f\x02ID\x12\x14\n\x0cprov_address\x18\x02 \x01(\t\x12\x14\n\x0cnode_address\x18\x03 \x01(\t\x12-\n\x05price\x18\x04 \x01(\x0b2\x18.sentinel.types.v1.PriceB\x04\xc8\xde\x1f\x00\x12\r\n\x05hours\x18\x05 \x01(\x03\x12\x11\n\tmax_hours\x18\x06 \x01(\x03\x12C\n\x14renewal_price_policy\x18\x07 \x01(\x0e2%.sentinel.types.v1.RenewalPricePolicy\x129\n\x0binactive_at\x18\x08 \x01(\x0b2\x1a.google.protobuf.TimestampB\x08\xc8\xde\x1f\x00\x90\xdf\x1f\x01\x127\n\tpayout_at\x18\t \x01(\x0b2\x1a.google.protobuf.TimestampB\x08\xc8\xde\x1f\x00\x90\xdf\x1f\x01B?Z5github.com/sentinel-official/hub/v12/x/lease/types/v1\xa8\xe2\x1e\x00\xc8\xe1\x1e\x00b\x06proto3')
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, globals())
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'sentinel.lease.v1.lease_pb2', globals())
if (_descriptor._USE_C_DESCRIPTORS == False):
    DESCRIPTOR._options = None
    DESCRIPTOR._serialized_options = b'Z5github.com/sentinel-official/hub/v12/x/lease/types/v1\xa8\xe2\x1e\x00\xc8\xe1\x1e\x00'
    _LEASE.fields_by_name['id']._options = None
    _LEASE.fields_by_name['id']._serialized_options = b'\xe2\xde\x1f\x02ID'
    _LEASE.fields_by_name['price']._options = None
    _LEASE.fields_by_name['price']._serialized_options = b'\xc8\xde\x1f\x00'
    _LEASE.fields_by_name['inactive_at']._options = None
    _LEASE.fields_by_name['inactive_at']._serialized_options = b'\xc8\xde\x1f\x00\x90\xdf\x1f\x01'
    _LEASE.fields_by_name['payout_at']._options = None
    _LEASE.fields_by_name['payout_at']._serialized_options = b'\xc8\xde\x1f\x00\x90\xdf\x1f\x01'
    _LEASE._serialized_start = 172
    _LEASE._serialized_end = 509
