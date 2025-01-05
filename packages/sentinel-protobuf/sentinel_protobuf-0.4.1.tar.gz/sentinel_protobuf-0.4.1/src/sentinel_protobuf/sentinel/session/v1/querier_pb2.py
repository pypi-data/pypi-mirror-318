"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_runtime_version.ValidateProtobufRuntimeVersion(_runtime_version.Domain.PUBLIC, 5, 28, 1, '', 'sentinel/session/v1/querier.proto')
_sym_db = _symbol_database.Default()
from ....cosmos.base.query.v1beta1 import pagination_pb2 as cosmos_dot_base_dot_query_dot_v1beta1_dot_pagination__pb2
from ....gogoproto import gogo_pb2 as gogoproto_dot_gogo__pb2
from ....google.api import annotations_pb2 as google_dot_api_dot_annotations__pb2
from ....sentinel.session.v1 import params_pb2 as sentinel_dot_session_dot_v1_dot_params__pb2
from ....sentinel.session.v1 import session_pb2 as sentinel_dot_session_dot_v1_dot_session__pb2
from ....sentinel.types.v1 import status_pb2 as sentinel_dot_types_dot_v1_dot_status__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n!sentinel/session/v1/querier.proto\x12\x13sentinel.session.v1\x1a*cosmos/base/query/v1beta1/pagination.proto\x1a\x14gogoproto/gogo.proto\x1a\x1cgoogle/api/annotations.proto\x1a sentinel/session/v1/params.proto\x1a!sentinel/session/v1/session.proto\x1a\x1esentinel/types/v1/status.proto"R\n\x14QuerySessionsRequest\x12:\n\npagination\x18\x01 \x01(\x0b2&.cosmos.base.query.v1beta1.PageRequest"\x98\x01\n\x1eQuerySessionsForAddressRequest\x12\x0f\n\x07address\x18\x01 \x01(\t\x12)\n\x06status\x18\x02 \x01(\x0e2\x19.sentinel.types.v1.Status\x12:\n\npagination\x18\x03 \x01(\x0b2&.cosmos.base.query.v1beta1.PageRequest"!\n\x13QuerySessionRequest\x12\n\n\x02id\x18\x01 \x01(\x04"\x14\n\x12QueryParamsRequest"\x8a\x01\n\x15QuerySessionsResponse\x124\n\x08sessions\x18\x01 \x03(\x0b2\x1c.sentinel.session.v1.SessionB\x04\xc8\xde\x1f\x00\x12;\n\npagination\x18\x02 \x01(\x0b2\'.cosmos.base.query.v1beta1.PageResponse"\x94\x01\n\x1fQuerySessionsForAddressResponse\x124\n\x08sessions\x18\x01 \x03(\x0b2\x1c.sentinel.session.v1.SessionB\x04\xc8\xde\x1f\x00\x12;\n\npagination\x18\x02 \x01(\x0b2\'.cosmos.base.query.v1beta1.PageResponse"K\n\x14QuerySessionResponse\x123\n\x07session\x18\x01 \x01(\x0b2\x1c.sentinel.session.v1.SessionB\x04\xc8\xde\x1f\x00"H\n\x13QueryParamsResponse\x121\n\x06params\x18\x01 \x01(\x0b2\x1b.sentinel.session.v1.ParamsB\x04\xc8\xde\x1f\x002\xf9\x04\n\x0cQueryService\x12\x8d\x01\n\rQuerySessions\x12).sentinel.session.v1.QuerySessionsRequest\x1a*.sentinel.session.v1.QuerySessionsResponse"%\x82\xd3\xe4\x93\x02\x1f\x12\x1d/sentinel/session/v1/sessions\x12\xbe\x01\n\x17QuerySessionsForAddress\x123.sentinel.session.v1.QuerySessionsForAddressRequest\x1a4.sentinel.session.v1.QuerySessionsForAddressResponse"8\x82\xd3\xe4\x93\x022\x120/sentinel/session/v1/accounts/{address}/sessions\x12\x8f\x01\n\x0cQuerySession\x12(.sentinel.session.v1.QuerySessionRequest\x1a).sentinel.session.v1.QuerySessionResponse"*\x82\xd3\xe4\x93\x02$\x12"/sentinel/session/v1/sessions/{id}\x12\x85\x01\n\x0bQueryParams\x12\'.sentinel.session.v1.QueryParamsRequest\x1a(.sentinel.session.v1.QueryParamsResponse"#\x82\xd3\xe4\x93\x02\x1d\x12\x1b/sentinel/session/v1/paramsBAZ7github.com/sentinel-official/hub/v12/x/session/types/v1\xc8\xe1\x1e\x00\xa8\xe2\x1e\x00b\x06proto3')
_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'sentinel.session.v1.querier_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
    _globals['DESCRIPTOR']._loaded_options = None
    _globals['DESCRIPTOR']._serialized_options = b'Z7github.com/sentinel-official/hub/v12/x/session/types/v1\xc8\xe1\x1e\x00\xa8\xe2\x1e\x00'
    _globals['_QUERYSESSIONSRESPONSE'].fields_by_name['sessions']._loaded_options = None
    _globals['_QUERYSESSIONSRESPONSE'].fields_by_name['sessions']._serialized_options = b'\xc8\xde\x1f\x00'
    _globals['_QUERYSESSIONSFORADDRESSRESPONSE'].fields_by_name['sessions']._loaded_options = None
    _globals['_QUERYSESSIONSFORADDRESSRESPONSE'].fields_by_name['sessions']._serialized_options = b'\xc8\xde\x1f\x00'
    _globals['_QUERYSESSIONRESPONSE'].fields_by_name['session']._loaded_options = None
    _globals['_QUERYSESSIONRESPONSE'].fields_by_name['session']._serialized_options = b'\xc8\xde\x1f\x00'
    _globals['_QUERYPARAMSRESPONSE'].fields_by_name['params']._loaded_options = None
    _globals['_QUERYPARAMSRESPONSE'].fields_by_name['params']._serialized_options = b'\xc8\xde\x1f\x00'
    _globals['_QUERYSERVICE'].methods_by_name['QuerySessions']._loaded_options = None
    _globals['_QUERYSERVICE'].methods_by_name['QuerySessions']._serialized_options = b'\x82\xd3\xe4\x93\x02\x1f\x12\x1d/sentinel/session/v1/sessions'
    _globals['_QUERYSERVICE'].methods_by_name['QuerySessionsForAddress']._loaded_options = None
    _globals['_QUERYSERVICE'].methods_by_name['QuerySessionsForAddress']._serialized_options = b'\x82\xd3\xe4\x93\x022\x120/sentinel/session/v1/accounts/{address}/sessions'
    _globals['_QUERYSERVICE'].methods_by_name['QuerySession']._loaded_options = None
    _globals['_QUERYSERVICE'].methods_by_name['QuerySession']._serialized_options = b'\x82\xd3\xe4\x93\x02$\x12"/sentinel/session/v1/sessions/{id}'
    _globals['_QUERYSERVICE'].methods_by_name['QueryParams']._loaded_options = None
    _globals['_QUERYSERVICE'].methods_by_name['QueryParams']._serialized_options = b'\x82\xd3\xe4\x93\x02\x1d\x12\x1b/sentinel/session/v1/params'
    _globals['_QUERYSESSIONSREQUEST']._serialized_start = 255
    _globals['_QUERYSESSIONSREQUEST']._serialized_end = 337
    _globals['_QUERYSESSIONSFORADDRESSREQUEST']._serialized_start = 340
    _globals['_QUERYSESSIONSFORADDRESSREQUEST']._serialized_end = 492
    _globals['_QUERYSESSIONREQUEST']._serialized_start = 494
    _globals['_QUERYSESSIONREQUEST']._serialized_end = 527
    _globals['_QUERYPARAMSREQUEST']._serialized_start = 529
    _globals['_QUERYPARAMSREQUEST']._serialized_end = 549
    _globals['_QUERYSESSIONSRESPONSE']._serialized_start = 552
    _globals['_QUERYSESSIONSRESPONSE']._serialized_end = 690
    _globals['_QUERYSESSIONSFORADDRESSRESPONSE']._serialized_start = 693
    _globals['_QUERYSESSIONSFORADDRESSRESPONSE']._serialized_end = 841
    _globals['_QUERYSESSIONRESPONSE']._serialized_start = 843
    _globals['_QUERYSESSIONRESPONSE']._serialized_end = 918
    _globals['_QUERYPARAMSRESPONSE']._serialized_start = 920
    _globals['_QUERYPARAMSRESPONSE']._serialized_end = 992
    _globals['_QUERYSERVICE']._serialized_start = 995
    _globals['_QUERYSERVICE']._serialized_end = 1628