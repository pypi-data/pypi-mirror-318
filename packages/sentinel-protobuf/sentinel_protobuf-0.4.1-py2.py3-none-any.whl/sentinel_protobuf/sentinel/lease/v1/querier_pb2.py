"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_runtime_version.ValidateProtobufRuntimeVersion(_runtime_version.Domain.PUBLIC, 5, 28, 1, '', 'sentinel/lease/v1/querier.proto')
_sym_db = _symbol_database.Default()
from ....cosmos.base.query.v1beta1 import pagination_pb2 as cosmos_dot_base_dot_query_dot_v1beta1_dot_pagination__pb2
from ....gogoproto import gogo_pb2 as gogoproto_dot_gogo__pb2
from ....google.api import annotations_pb2 as google_dot_api_dot_annotations__pb2
from ....sentinel.lease.v1 import lease_pb2 as sentinel_dot_lease_dot_v1_dot_lease__pb2
from ....sentinel.lease.v1 import params_pb2 as sentinel_dot_lease_dot_v1_dot_params__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x1fsentinel/lease/v1/querier.proto\x12\x11sentinel.lease.v1\x1a*cosmos/base/query/v1beta1/pagination.proto\x1a\x14gogoproto/gogo.proto\x1a\x1cgoogle/api/annotations.proto\x1a\x1dsentinel/lease/v1/lease.proto\x1a\x1esentinel/lease/v1/params.proto"P\n\x12QueryLeasesRequest\x12:\n\npagination\x18\x01 \x01(\x0b2&.cosmos.base.query.v1beta1.PageRequest"h\n\x19QueryLeasesForNodeRequest\x12\x0f\n\x07address\x18\x01 \x01(\t\x12:\n\npagination\x18\x02 \x01(\x0b2&.cosmos.base.query.v1beta1.PageRequest"l\n\x1dQueryLeasesForProviderRequest\x12\x0f\n\x07address\x18\x01 \x01(\t\x12:\n\npagination\x18\x02 \x01(\x0b2&.cosmos.base.query.v1beta1.PageRequest"\x1f\n\x11QueryLeaseRequest\x12\n\n\x02id\x18\x01 \x01(\x04"\x14\n\x12QueryParamsRequest"\x82\x01\n\x13QueryLeasesResponse\x12.\n\x06leases\x18\x01 \x03(\x0b2\x18.sentinel.lease.v1.LeaseB\x04\xc8\xde\x1f\x00\x12;\n\npagination\x18\x02 \x01(\x0b2\'.cosmos.base.query.v1beta1.PageResponse"\x89\x01\n\x1aQueryLeasesForNodeResponse\x12.\n\x06leases\x18\x01 \x03(\x0b2\x18.sentinel.lease.v1.LeaseB\x04\xc8\xde\x1f\x00\x12;\n\npagination\x18\x02 \x01(\x0b2\'.cosmos.base.query.v1beta1.PageResponse"\x8d\x01\n\x1eQueryLeasesForProviderResponse\x12.\n\x06leases\x18\x01 \x03(\x0b2\x18.sentinel.lease.v1.LeaseB\x04\xc8\xde\x1f\x00\x12;\n\npagination\x18\x02 \x01(\x0b2\'.cosmos.base.query.v1beta1.PageResponse"C\n\x12QueryLeaseResponse\x12-\n\x05lease\x18\x01 \x01(\x0b2\x18.sentinel.lease.v1.LeaseB\x04\xc8\xde\x1f\x00"F\n\x13QueryParamsResponse\x12/\n\x06params\x18\x01 \x01(\x0b2\x19.sentinel.lease.v1.ParamsB\x04\xc8\xde\x1f\x002\xf2\x05\n\x0cQueryService\x12\x7f\n\x0bQueryLeases\x12%.sentinel.lease.v1.QueryLeasesRequest\x1a&.sentinel.lease.v1.QueryLeasesResponse"!\x82\xd3\xe4\x93\x02\x1b\x12\x19/sentinel/lease/v1/leases\x12\xb4\x01\n\x16QueryLeasesForProvider\x120.sentinel.lease.v1.QueryLeasesForProviderRequest\x1a1.sentinel.lease.v1.QueryLeasesForProviderResponse"5\x82\xd3\xe4\x93\x02/\x12-/sentinel/lease/v1/providers/{address}/leases\x12\xa4\x01\n\x12QueryLeasesForNode\x12,.sentinel.lease.v1.QueryLeasesForNodeRequest\x1a-.sentinel.lease.v1.QueryLeasesForNodeResponse"1\x82\xd3\xe4\x93\x02+\x12)/sentinel/lease/v1/nodes/{address}/leases\x12\x81\x01\n\nQueryLease\x12$.sentinel.lease.v1.QueryLeaseRequest\x1a%.sentinel.lease.v1.QueryLeaseResponse"&\x82\xd3\xe4\x93\x02 \x12\x1e/sentinel/lease/v1/leases/{id}\x12\x7f\n\x0bQueryParams\x12%.sentinel.lease.v1.QueryParamsRequest\x1a&.sentinel.lease.v1.QueryParamsResponse"!\x82\xd3\xe4\x93\x02\x1b\x12\x19/sentinel/lease/v1/paramsB?Z5github.com/sentinel-official/hub/v12/x/lease/types/v1\xc8\xe1\x1e\x00\xa8\xe2\x1e\x00b\x06proto3')
_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'sentinel.lease.v1.querier_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
    _globals['DESCRIPTOR']._loaded_options = None
    _globals['DESCRIPTOR']._serialized_options = b'Z5github.com/sentinel-official/hub/v12/x/lease/types/v1\xc8\xe1\x1e\x00\xa8\xe2\x1e\x00'
    _globals['_QUERYLEASESRESPONSE'].fields_by_name['leases']._loaded_options = None
    _globals['_QUERYLEASESRESPONSE'].fields_by_name['leases']._serialized_options = b'\xc8\xde\x1f\x00'
    _globals['_QUERYLEASESFORNODERESPONSE'].fields_by_name['leases']._loaded_options = None
    _globals['_QUERYLEASESFORNODERESPONSE'].fields_by_name['leases']._serialized_options = b'\xc8\xde\x1f\x00'
    _globals['_QUERYLEASESFORPROVIDERRESPONSE'].fields_by_name['leases']._loaded_options = None
    _globals['_QUERYLEASESFORPROVIDERRESPONSE'].fields_by_name['leases']._serialized_options = b'\xc8\xde\x1f\x00'
    _globals['_QUERYLEASERESPONSE'].fields_by_name['lease']._loaded_options = None
    _globals['_QUERYLEASERESPONSE'].fields_by_name['lease']._serialized_options = b'\xc8\xde\x1f\x00'
    _globals['_QUERYPARAMSRESPONSE'].fields_by_name['params']._loaded_options = None
    _globals['_QUERYPARAMSRESPONSE'].fields_by_name['params']._serialized_options = b'\xc8\xde\x1f\x00'
    _globals['_QUERYSERVICE'].methods_by_name['QueryLeases']._loaded_options = None
    _globals['_QUERYSERVICE'].methods_by_name['QueryLeases']._serialized_options = b'\x82\xd3\xe4\x93\x02\x1b\x12\x19/sentinel/lease/v1/leases'
    _globals['_QUERYSERVICE'].methods_by_name['QueryLeasesForProvider']._loaded_options = None
    _globals['_QUERYSERVICE'].methods_by_name['QueryLeasesForProvider']._serialized_options = b'\x82\xd3\xe4\x93\x02/\x12-/sentinel/lease/v1/providers/{address}/leases'
    _globals['_QUERYSERVICE'].methods_by_name['QueryLeasesForNode']._loaded_options = None
    _globals['_QUERYSERVICE'].methods_by_name['QueryLeasesForNode']._serialized_options = b'\x82\xd3\xe4\x93\x02+\x12)/sentinel/lease/v1/nodes/{address}/leases'
    _globals['_QUERYSERVICE'].methods_by_name['QueryLease']._loaded_options = None
    _globals['_QUERYSERVICE'].methods_by_name['QueryLease']._serialized_options = b'\x82\xd3\xe4\x93\x02 \x12\x1e/sentinel/lease/v1/leases/{id}'
    _globals['_QUERYSERVICE'].methods_by_name['QueryParams']._loaded_options = None
    _globals['_QUERYSERVICE'].methods_by_name['QueryParams']._serialized_options = b'\x82\xd3\xe4\x93\x02\x1b\x12\x19/sentinel/lease/v1/params'
    _globals['_QUERYLEASESREQUEST']._serialized_start = 213
    _globals['_QUERYLEASESREQUEST']._serialized_end = 293
    _globals['_QUERYLEASESFORNODEREQUEST']._serialized_start = 295
    _globals['_QUERYLEASESFORNODEREQUEST']._serialized_end = 399
    _globals['_QUERYLEASESFORPROVIDERREQUEST']._serialized_start = 401
    _globals['_QUERYLEASESFORPROVIDERREQUEST']._serialized_end = 509
    _globals['_QUERYLEASEREQUEST']._serialized_start = 511
    _globals['_QUERYLEASEREQUEST']._serialized_end = 542
    _globals['_QUERYPARAMSREQUEST']._serialized_start = 544
    _globals['_QUERYPARAMSREQUEST']._serialized_end = 564
    _globals['_QUERYLEASESRESPONSE']._serialized_start = 567
    _globals['_QUERYLEASESRESPONSE']._serialized_end = 697
    _globals['_QUERYLEASESFORNODERESPONSE']._serialized_start = 700
    _globals['_QUERYLEASESFORNODERESPONSE']._serialized_end = 837
    _globals['_QUERYLEASESFORPROVIDERRESPONSE']._serialized_start = 840
    _globals['_QUERYLEASESFORPROVIDERRESPONSE']._serialized_end = 981
    _globals['_QUERYLEASERESPONSE']._serialized_start = 983
    _globals['_QUERYLEASERESPONSE']._serialized_end = 1050
    _globals['_QUERYPARAMSRESPONSE']._serialized_start = 1052
    _globals['_QUERYPARAMSRESPONSE']._serialized_end = 1122
    _globals['_QUERYSERVICE']._serialized_start = 1125
    _globals['_QUERYSERVICE']._serialized_end = 1879