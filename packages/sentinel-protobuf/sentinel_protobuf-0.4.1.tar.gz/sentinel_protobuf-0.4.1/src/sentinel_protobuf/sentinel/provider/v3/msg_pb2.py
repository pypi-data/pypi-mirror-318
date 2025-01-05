"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_runtime_version.ValidateProtobufRuntimeVersion(_runtime_version.Domain.PUBLIC, 5, 28, 1, '', 'sentinel/provider/v3/msg.proto')
_sym_db = _symbol_database.Default()
from ....gogoproto import gogo_pb2 as gogoproto_dot_gogo__pb2
from ....sentinel.provider.v2 import params_pb2 as sentinel_dot_provider_dot_v2_dot_params__pb2
from ....sentinel.types.v1 import status_pb2 as sentinel_dot_types_dot_v1_dot_status__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x1esentinel/provider/v3/msg.proto\x12\x14sentinel.provider.v3\x1a\x14gogoproto/gogo.proto\x1a!sentinel/provider/v2/params.proto\x1a\x1esentinel/types/v1/status.proto"p\n\x1aMsgRegisterProviderRequest\x12\x0c\n\x04from\x18\x01 \x01(\t\x12\x0c\n\x04name\x18\x02 \x01(\t\x12\x10\n\x08identity\x18\x03 \x01(\t\x12\x0f\n\x07website\x18\x04 \x01(\t\x12\x13\n\x0bdescription\x18\x05 \x01(\t"u\n\x1fMsgUpdateProviderDetailsRequest\x12\x0c\n\x04from\x18\x01 \x01(\t\x12\x0c\n\x04name\x18\x02 \x01(\t\x12\x10\n\x08identity\x18\x03 \x01(\t\x12\x0f\n\x07website\x18\x04 \x01(\t\x12\x13\n\x0bdescription\x18\x05 \x01(\t"Y\n\x1eMsgUpdateProviderStatusRequest\x12\x0c\n\x04from\x18\x01 \x01(\t\x12)\n\x06status\x18\x02 \x01(\x0e2\x19.sentinel.types.v1.Status"Z\n\x16MsgUpdateParamsRequest\x12\x0c\n\x04from\x18\x01 \x01(\t\x122\n\x06params\x18\x02 \x01(\x0b2\x1c.sentinel.provider.v2.ParamsB\x04\xc8\xde\x1f\x00"\x1d\n\x1bMsgRegisterProviderResponse""\n MsgUpdateProviderDetailsResponse"!\n\x1fMsgUpdateProviderStatusResponse"\x19\n\x17MsgUpdateParamsResponse2\x8d\x04\n\nMsgService\x12z\n\x13MsgRegisterProvider\x120.sentinel.provider.v3.MsgRegisterProviderRequest\x1a1.sentinel.provider.v3.MsgRegisterProviderResponse\x12\x89\x01\n\x18MsgUpdateProviderDetails\x125.sentinel.provider.v3.MsgUpdateProviderDetailsRequest\x1a6.sentinel.provider.v3.MsgUpdateProviderDetailsResponse\x12\x86\x01\n\x17MsgUpdateProviderStatus\x124.sentinel.provider.v3.MsgUpdateProviderStatusRequest\x1a5.sentinel.provider.v3.MsgUpdateProviderStatusResponse\x12n\n\x0fMsgUpdateParams\x12,.sentinel.provider.v3.MsgUpdateParamsRequest\x1a-.sentinel.provider.v3.MsgUpdateParamsResponseBBZ8github.com/sentinel-official/hub/v12/x/provider/types/v3\xc8\xe1\x1e\x00\xa8\xe2\x1e\x00b\x06proto3')
_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'sentinel.provider.v3.msg_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
    _globals['DESCRIPTOR']._loaded_options = None
    _globals['DESCRIPTOR']._serialized_options = b'Z8github.com/sentinel-official/hub/v12/x/provider/types/v3\xc8\xe1\x1e\x00\xa8\xe2\x1e\x00'
    _globals['_MSGUPDATEPARAMSREQUEST'].fields_by_name['params']._loaded_options = None
    _globals['_MSGUPDATEPARAMSREQUEST'].fields_by_name['params']._serialized_options = b'\xc8\xde\x1f\x00'
    _globals['_MSGREGISTERPROVIDERREQUEST']._serialized_start = 145
    _globals['_MSGREGISTERPROVIDERREQUEST']._serialized_end = 257
    _globals['_MSGUPDATEPROVIDERDETAILSREQUEST']._serialized_start = 259
    _globals['_MSGUPDATEPROVIDERDETAILSREQUEST']._serialized_end = 376
    _globals['_MSGUPDATEPROVIDERSTATUSREQUEST']._serialized_start = 378
    _globals['_MSGUPDATEPROVIDERSTATUSREQUEST']._serialized_end = 467
    _globals['_MSGUPDATEPARAMSREQUEST']._serialized_start = 469
    _globals['_MSGUPDATEPARAMSREQUEST']._serialized_end = 559
    _globals['_MSGREGISTERPROVIDERRESPONSE']._serialized_start = 561
    _globals['_MSGREGISTERPROVIDERRESPONSE']._serialized_end = 590
    _globals['_MSGUPDATEPROVIDERDETAILSRESPONSE']._serialized_start = 592
    _globals['_MSGUPDATEPROVIDERDETAILSRESPONSE']._serialized_end = 626
    _globals['_MSGUPDATEPROVIDERSTATUSRESPONSE']._serialized_start = 628
    _globals['_MSGUPDATEPROVIDERSTATUSRESPONSE']._serialized_end = 661
    _globals['_MSGUPDATEPARAMSRESPONSE']._serialized_start = 663
    _globals['_MSGUPDATEPARAMSRESPONSE']._serialized_end = 688
    _globals['_MSGSERVICE']._serialized_start = 691
    _globals['_MSGSERVICE']._serialized_end = 1216