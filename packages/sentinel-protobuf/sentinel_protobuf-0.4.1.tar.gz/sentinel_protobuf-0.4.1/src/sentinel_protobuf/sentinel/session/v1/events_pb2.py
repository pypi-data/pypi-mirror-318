"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_runtime_version.ValidateProtobufRuntimeVersion(_runtime_version.Domain.PUBLIC, 5, 28, 1, '', 'sentinel/session/v1/events.proto')
_sym_db = _symbol_database.Default()
from ....cosmos.base.v1beta1 import coin_pb2 as cosmos_dot_base_dot_v1beta1_dot_coin__pb2
from ....gogoproto import gogo_pb2 as gogoproto_dot_gogo__pb2
from ....sentinel.types.v1 import status_pb2 as sentinel_dot_types_dot_v1_dot_status__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n sentinel/session/v1/events.proto\x12\x13sentinel.session.v1\x1a\x1ecosmos/base/v1beta1/coin.proto\x1a\x14gogoproto/gogo.proto\x1a\x1esentinel/types/v1/status.proto"\xb5\x01\n\x08EventPay\x12\x19\n\x02id\x18\x01 \x01(\x04B\r\xf2\xde\x1f\tyaml:"id"\x12\x1d\n\x04node\x18\x02 \x01(\tB\x0f\xf2\xde\x1f\x0byaml:"node"\x12-\n\x0csubscription\x18\x03 \x01(\x04B\x17\xf2\xde\x1f\x13yaml:"subscription"\x12@\n\x06amount\x18\x04 \x01(\x0b2\x19.cosmos.base.v1beta1.CoinB\x15\xc8\xde\x1f\x00\xf2\xde\x1f\ryaml:"amount""u\n\nEventStart\x12\x19\n\x02id\x18\x01 \x01(\x04B\r\xf2\xde\x1f\tyaml:"id"\x12\x1d\n\x04node\x18\x02 \x01(\tB\x0f\xf2\xde\x1f\x0byaml:"node"\x12-\n\x0csubscription\x18\x03 \x01(\x04B\x17\xf2\xde\x1f\x13yaml:"subscription""\xb7\x01\n\x0eEventSetStatus\x12\x19\n\x02id\x18\x01 \x01(\x04B\r\xf2\xde\x1f\tyaml:"id"\x12\x1d\n\x04node\x18\x02 \x01(\tB\x0f\xf2\xde\x1f\x0byaml:"node"\x12-\n\x0csubscription\x18\x03 \x01(\x04B\x17\xf2\xde\x1f\x13yaml:"subscription"\x12<\n\x06status\x18\x04 \x01(\x0e2\x19.sentinel.types.v1.StatusB\x11\xf2\xde\x1f\ryaml:"status""v\n\x0bEventUpdate\x12\x19\n\x02id\x18\x01 \x01(\x04B\r\xf2\xde\x1f\tyaml:"id"\x12\x1d\n\x04node\x18\x02 \x01(\tB\x0f\xf2\xde\x1f\x0byaml:"node"\x12-\n\x0csubscription\x18\x03 \x01(\x04B\x17\xf2\xde\x1f\x13yaml:"subscription"BAZ7github.com/sentinel-official/hub/v12/x/session/types/v1\xc8\xe1\x1e\x00\xa8\xe2\x1e\x00b\x06proto3')
_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'sentinel.session.v1.events_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
    _globals['DESCRIPTOR']._loaded_options = None
    _globals['DESCRIPTOR']._serialized_options = b'Z7github.com/sentinel-official/hub/v12/x/session/types/v1\xc8\xe1\x1e\x00\xa8\xe2\x1e\x00'
    _globals['_EVENTPAY'].fields_by_name['id']._loaded_options = None
    _globals['_EVENTPAY'].fields_by_name['id']._serialized_options = b'\xf2\xde\x1f\tyaml:"id"'
    _globals['_EVENTPAY'].fields_by_name['node']._loaded_options = None
    _globals['_EVENTPAY'].fields_by_name['node']._serialized_options = b'\xf2\xde\x1f\x0byaml:"node"'
    _globals['_EVENTPAY'].fields_by_name['subscription']._loaded_options = None
    _globals['_EVENTPAY'].fields_by_name['subscription']._serialized_options = b'\xf2\xde\x1f\x13yaml:"subscription"'
    _globals['_EVENTPAY'].fields_by_name['amount']._loaded_options = None
    _globals['_EVENTPAY'].fields_by_name['amount']._serialized_options = b'\xc8\xde\x1f\x00\xf2\xde\x1f\ryaml:"amount"'
    _globals['_EVENTSTART'].fields_by_name['id']._loaded_options = None
    _globals['_EVENTSTART'].fields_by_name['id']._serialized_options = b'\xf2\xde\x1f\tyaml:"id"'
    _globals['_EVENTSTART'].fields_by_name['node']._loaded_options = None
    _globals['_EVENTSTART'].fields_by_name['node']._serialized_options = b'\xf2\xde\x1f\x0byaml:"node"'
    _globals['_EVENTSTART'].fields_by_name['subscription']._loaded_options = None
    _globals['_EVENTSTART'].fields_by_name['subscription']._serialized_options = b'\xf2\xde\x1f\x13yaml:"subscription"'
    _globals['_EVENTSETSTATUS'].fields_by_name['id']._loaded_options = None
    _globals['_EVENTSETSTATUS'].fields_by_name['id']._serialized_options = b'\xf2\xde\x1f\tyaml:"id"'
    _globals['_EVENTSETSTATUS'].fields_by_name['node']._loaded_options = None
    _globals['_EVENTSETSTATUS'].fields_by_name['node']._serialized_options = b'\xf2\xde\x1f\x0byaml:"node"'
    _globals['_EVENTSETSTATUS'].fields_by_name['subscription']._loaded_options = None
    _globals['_EVENTSETSTATUS'].fields_by_name['subscription']._serialized_options = b'\xf2\xde\x1f\x13yaml:"subscription"'
    _globals['_EVENTSETSTATUS'].fields_by_name['status']._loaded_options = None
    _globals['_EVENTSETSTATUS'].fields_by_name['status']._serialized_options = b'\xf2\xde\x1f\ryaml:"status"'
    _globals['_EVENTUPDATE'].fields_by_name['id']._loaded_options = None
    _globals['_EVENTUPDATE'].fields_by_name['id']._serialized_options = b'\xf2\xde\x1f\tyaml:"id"'
    _globals['_EVENTUPDATE'].fields_by_name['node']._loaded_options = None
    _globals['_EVENTUPDATE'].fields_by_name['node']._serialized_options = b'\xf2\xde\x1f\x0byaml:"node"'
    _globals['_EVENTUPDATE'].fields_by_name['subscription']._loaded_options = None
    _globals['_EVENTUPDATE'].fields_by_name['subscription']._serialized_options = b'\xf2\xde\x1f\x13yaml:"subscription"'
    _globals['_EVENTPAY']._serialized_start = 144
    _globals['_EVENTPAY']._serialized_end = 325
    _globals['_EVENTSTART']._serialized_start = 327
    _globals['_EVENTSTART']._serialized_end = 444
    _globals['_EVENTSETSTATUS']._serialized_start = 447
    _globals['_EVENTSETSTATUS']._serialized_end = 630
    _globals['_EVENTUPDATE']._serialized_start = 632
    _globals['_EVENTUPDATE']._serialized_end = 750