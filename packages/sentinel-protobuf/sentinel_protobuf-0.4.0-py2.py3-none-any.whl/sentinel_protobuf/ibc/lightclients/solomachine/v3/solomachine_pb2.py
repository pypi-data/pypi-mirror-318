
'Generated protocol buffer code.'
from google.protobuf.internal import builder as _builder
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
_sym_db = _symbol_database.Default()
from .....gogoproto import gogo_pb2 as gogoproto_dot_gogo__pb2
from google.protobuf import any_pb2 as google_dot_protobuf_dot_any__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n1ibc/lightclients/solomachine/v3/solomachine.proto\x12\x1fibc.lightclients.solomachine.v3\x1a\x14gogoproto/gogo.proto\x1a\x19google/protobuf/any.proto"\xb4\x01\n\x0bClientState\x12\x10\n\x08sequence\x18\x01 \x01(\x04\x12\'\n\tis_frozen\x18\x02 \x01(\x08B\x14\xf2\xde\x1f\x10yaml:"is_frozen"\x12d\n\x0fconsensus_state\x18\x03 \x01(\x0b2/.ibc.lightclients.solomachine.v3.ConsensusStateB\x1a\xf2\xde\x1f\x16yaml:"consensus_state":\x04\x88\xa0\x1f\x00"\x7f\n\x0eConsensusState\x12?\n\npublic_key\x18\x01 \x01(\x0b2\x14.google.protobuf.AnyB\x15\xf2\xde\x1f\x11yaml:"public_key"\x12\x13\n\x0bdiversifier\x18\x02 \x01(\t\x12\x11\n\ttimestamp\x18\x03 \x01(\x04:\x04\x88\xa0\x1f\x00"\xb2\x01\n\x06Header\x12\x11\n\ttimestamp\x18\x01 \x01(\x04\x12\x11\n\tsignature\x18\x02 \x01(\x0c\x12G\n\x0enew_public_key\x18\x03 \x01(\x0b2\x14.google.protobuf.AnyB\x19\xf2\xde\x1f\x15yaml:"new_public_key"\x123\n\x0fnew_diversifier\x18\x04 \x01(\tB\x1a\xf2\xde\x1f\x16yaml:"new_diversifier":\x04\x88\xa0\x1f\x00"\xee\x01\n\x0cMisbehaviour\x12\x10\n\x08sequence\x18\x01 \x01(\x04\x12b\n\rsignature_one\x18\x02 \x01(\x0b21.ibc.lightclients.solomachine.v3.SignatureAndDataB\x18\xf2\xde\x1f\x14yaml:"signature_one"\x12b\n\rsignature_two\x18\x03 \x01(\x0b21.ibc.lightclients.solomachine.v3.SignatureAndDataB\x18\xf2\xde\x1f\x14yaml:"signature_two":\x04\x88\xa0\x1f\x00"Z\n\x10SignatureAndData\x12\x11\n\tsignature\x18\x01 \x01(\x0c\x12\x0c\n\x04path\x18\x02 \x01(\x0c\x12\x0c\n\x04data\x18\x03 \x01(\x0c\x12\x11\n\ttimestamp\x18\x04 \x01(\x04:\x04\x88\xa0\x1f\x00"f\n\x18TimestampedSignatureData\x121\n\x0esignature_data\x18\x01 \x01(\x0cB\x19\xf2\xde\x1f\x15yaml:"signature_data"\x12\x11\n\ttimestamp\x18\x02 \x01(\x04:\x04\x88\xa0\x1f\x00"g\n\tSignBytes\x12\x10\n\x08sequence\x18\x01 \x01(\x04\x12\x11\n\ttimestamp\x18\x02 \x01(\x04\x12\x13\n\x0bdiversifier\x18\x03 \x01(\t\x12\x0c\n\x04path\x18\x04 \x01(\x0c\x12\x0c\n\x04data\x18\x05 \x01(\x0c:\x04\x88\xa0\x1f\x00"\x8a\x01\n\nHeaderData\x12A\n\x0bnew_pub_key\x18\x01 \x01(\x0b2\x14.google.protobuf.AnyB\x16\xf2\xde\x1f\x12yaml:"new_pub_key"\x123\n\x0fnew_diversifier\x18\x02 \x01(\tB\x1a\xf2\xde\x1f\x16yaml:"new_diversifier":\x04\x88\xa0\x1f\x00BNZLgithub.com/cosmos/ibc-go/v7/modules/light-clients/06-solomachine;solomachineb\x06proto3')
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, globals())
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'ibc.lightclients.solomachine.v3.solomachine_pb2', globals())
if (_descriptor._USE_C_DESCRIPTORS == False):
    DESCRIPTOR._options = None
    DESCRIPTOR._serialized_options = b'ZLgithub.com/cosmos/ibc-go/v7/modules/light-clients/06-solomachine;solomachine'
    _CLIENTSTATE.fields_by_name['is_frozen']._options = None
    _CLIENTSTATE.fields_by_name['is_frozen']._serialized_options = b'\xf2\xde\x1f\x10yaml:"is_frozen"'
    _CLIENTSTATE.fields_by_name['consensus_state']._options = None
    _CLIENTSTATE.fields_by_name['consensus_state']._serialized_options = b'\xf2\xde\x1f\x16yaml:"consensus_state"'
    _CLIENTSTATE._options = None
    _CLIENTSTATE._serialized_options = b'\x88\xa0\x1f\x00'
    _CONSENSUSSTATE.fields_by_name['public_key']._options = None
    _CONSENSUSSTATE.fields_by_name['public_key']._serialized_options = b'\xf2\xde\x1f\x11yaml:"public_key"'
    _CONSENSUSSTATE._options = None
    _CONSENSUSSTATE._serialized_options = b'\x88\xa0\x1f\x00'
    _HEADER.fields_by_name['new_public_key']._options = None
    _HEADER.fields_by_name['new_public_key']._serialized_options = b'\xf2\xde\x1f\x15yaml:"new_public_key"'
    _HEADER.fields_by_name['new_diversifier']._options = None
    _HEADER.fields_by_name['new_diversifier']._serialized_options = b'\xf2\xde\x1f\x16yaml:"new_diversifier"'
    _HEADER._options = None
    _HEADER._serialized_options = b'\x88\xa0\x1f\x00'
    _MISBEHAVIOUR.fields_by_name['signature_one']._options = None
    _MISBEHAVIOUR.fields_by_name['signature_one']._serialized_options = b'\xf2\xde\x1f\x14yaml:"signature_one"'
    _MISBEHAVIOUR.fields_by_name['signature_two']._options = None
    _MISBEHAVIOUR.fields_by_name['signature_two']._serialized_options = b'\xf2\xde\x1f\x14yaml:"signature_two"'
    _MISBEHAVIOUR._options = None
    _MISBEHAVIOUR._serialized_options = b'\x88\xa0\x1f\x00'
    _SIGNATUREANDDATA._options = None
    _SIGNATUREANDDATA._serialized_options = b'\x88\xa0\x1f\x00'
    _TIMESTAMPEDSIGNATUREDATA.fields_by_name['signature_data']._options = None
    _TIMESTAMPEDSIGNATUREDATA.fields_by_name['signature_data']._serialized_options = b'\xf2\xde\x1f\x15yaml:"signature_data"'
    _TIMESTAMPEDSIGNATUREDATA._options = None
    _TIMESTAMPEDSIGNATUREDATA._serialized_options = b'\x88\xa0\x1f\x00'
    _SIGNBYTES._options = None
    _SIGNBYTES._serialized_options = b'\x88\xa0\x1f\x00'
    _HEADERDATA.fields_by_name['new_pub_key']._options = None
    _HEADERDATA.fields_by_name['new_pub_key']._serialized_options = b'\xf2\xde\x1f\x12yaml:"new_pub_key"'
    _HEADERDATA.fields_by_name['new_diversifier']._options = None
    _HEADERDATA.fields_by_name['new_diversifier']._serialized_options = b'\xf2\xde\x1f\x16yaml:"new_diversifier"'
    _HEADERDATA._options = None
    _HEADERDATA._serialized_options = b'\x88\xa0\x1f\x00'
    _CLIENTSTATE._serialized_start = 136
    _CLIENTSTATE._serialized_end = 316
    _CONSENSUSSTATE._serialized_start = 318
    _CONSENSUSSTATE._serialized_end = 445
    _HEADER._serialized_start = 448
    _HEADER._serialized_end = 626
    _MISBEHAVIOUR._serialized_start = 629
    _MISBEHAVIOUR._serialized_end = 867
    _SIGNATUREANDDATA._serialized_start = 869
    _SIGNATUREANDDATA._serialized_end = 959
    _TIMESTAMPEDSIGNATUREDATA._serialized_start = 961
    _TIMESTAMPEDSIGNATUREDATA._serialized_end = 1063
    _SIGNBYTES._serialized_start = 1065
    _SIGNBYTES._serialized_end = 1168
    _HEADERDATA._serialized_start = 1171
    _HEADERDATA._serialized_end = 1309
