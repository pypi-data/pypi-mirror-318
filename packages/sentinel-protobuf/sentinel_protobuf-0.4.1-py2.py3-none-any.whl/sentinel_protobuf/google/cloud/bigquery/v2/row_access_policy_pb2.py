"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_runtime_version.ValidateProtobufRuntimeVersion(_runtime_version.Domain.PUBLIC, 5, 28, 1, '', 'google/cloud/bigquery/v2/row_access_policy.proto')
_sym_db = _symbol_database.Default()
from .....google.api import annotations_pb2 as google_dot_api_dot_annotations__pb2
from .....google.api import client_pb2 as google_dot_api_dot_client__pb2
from .....google.api import field_behavior_pb2 as google_dot_api_dot_field__behavior__pb2
from .....google.cloud.bigquery.v2 import row_access_policy_reference_pb2 as google_dot_cloud_dot_bigquery_dot_v2_dot_row__access__policy__reference__pb2
from google.protobuf import timestamp_pb2 as google_dot_protobuf_dot_timestamp__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n0google/cloud/bigquery/v2/row_access_policy.proto\x12\x18google.cloud.bigquery.v2\x1a\x1cgoogle/api/annotations.proto\x1a\x17google/api/client.proto\x1a\x1fgoogle/api/field_behavior.proto\x1a:google/cloud/bigquery/v2/row_access_policy_reference.proto\x1a\x1fgoogle/protobuf/timestamp.proto"\x8e\x01\n\x1cListRowAccessPoliciesRequest\x12\x17\n\nproject_id\x18\x01 \x01(\tB\x03\xe0A\x02\x12\x17\n\ndataset_id\x18\x02 \x01(\tB\x03\xe0A\x02\x12\x15\n\x08table_id\x18\x03 \x01(\tB\x03\xe0A\x02\x12\x12\n\npage_token\x18\x04 \x01(\t\x12\x11\n\tpage_size\x18\x05 \x01(\x05"\x80\x01\n\x1dListRowAccessPoliciesResponse\x12F\n\x13row_access_policies\x18\x01 \x03(\x0b2).google.cloud.bigquery.v2.RowAccessPolicy\x12\x17\n\x0fnext_page_token\x18\x02 \x01(\t"\x96\x02\n\x0fRowAccessPolicy\x12\x11\n\x04etag\x18\x01 \x01(\tB\x03\xe0A\x03\x12\\\n\x1brow_access_policy_reference\x18\x02 \x01(\x0b22.google.cloud.bigquery.v2.RowAccessPolicyReferenceB\x03\xe0A\x02\x12\x1d\n\x10filter_predicate\x18\x03 \x01(\tB\x03\xe0A\x02\x126\n\rcreation_time\x18\x04 \x01(\x0b2\x1a.google.protobuf.TimestampB\x03\xe0A\x03\x12;\n\x12last_modified_time\x18\x05 \x01(\x0b2\x1a.google.protobuf.TimestampB\x03\xe0A\x032\xc0\x03\n\x16RowAccessPolicyService\x12\xf4\x01\n\x15ListRowAccessPolicies\x126.google.cloud.bigquery.v2.ListRowAccessPoliciesRequest\x1a7.google.cloud.bigquery.v2.ListRowAccessPoliciesResponse"j\x82\xd3\xe4\x93\x02d\x12b/bigquery/v2/projects/{project_id=*}/datasets/{dataset_id=*}/tables/{table_id=*}/rowAccessPolicies\x1a\xae\x01\xcaA\x17bigquery.googleapis.com\xd2A\x90\x01https://www.googleapis.com/auth/bigquery,https://www.googleapis.com/auth/cloud-platform,https://www.googleapis.com/auth/cloud-platform.read-onlyBp\n\x1ccom.google.cloud.bigquery.v2B\x14RowAccessPolicyProtoP\x01Z8cloud.google.com/go/bigquery/apiv2/bigquerypb;bigquerypbb\x06proto3')
_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'google.cloud.bigquery.v2.row_access_policy_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
    _globals['DESCRIPTOR']._loaded_options = None
    _globals['DESCRIPTOR']._serialized_options = b'\n\x1ccom.google.cloud.bigquery.v2B\x14RowAccessPolicyProtoP\x01Z8cloud.google.com/go/bigquery/apiv2/bigquerypb;bigquerypb'
    _globals['_LISTROWACCESSPOLICIESREQUEST'].fields_by_name['project_id']._loaded_options = None
    _globals['_LISTROWACCESSPOLICIESREQUEST'].fields_by_name['project_id']._serialized_options = b'\xe0A\x02'
    _globals['_LISTROWACCESSPOLICIESREQUEST'].fields_by_name['dataset_id']._loaded_options = None
    _globals['_LISTROWACCESSPOLICIESREQUEST'].fields_by_name['dataset_id']._serialized_options = b'\xe0A\x02'
    _globals['_LISTROWACCESSPOLICIESREQUEST'].fields_by_name['table_id']._loaded_options = None
    _globals['_LISTROWACCESSPOLICIESREQUEST'].fields_by_name['table_id']._serialized_options = b'\xe0A\x02'
    _globals['_ROWACCESSPOLICY'].fields_by_name['etag']._loaded_options = None
    _globals['_ROWACCESSPOLICY'].fields_by_name['etag']._serialized_options = b'\xe0A\x03'
    _globals['_ROWACCESSPOLICY'].fields_by_name['row_access_policy_reference']._loaded_options = None
    _globals['_ROWACCESSPOLICY'].fields_by_name['row_access_policy_reference']._serialized_options = b'\xe0A\x02'
    _globals['_ROWACCESSPOLICY'].fields_by_name['filter_predicate']._loaded_options = None
    _globals['_ROWACCESSPOLICY'].fields_by_name['filter_predicate']._serialized_options = b'\xe0A\x02'
    _globals['_ROWACCESSPOLICY'].fields_by_name['creation_time']._loaded_options = None
    _globals['_ROWACCESSPOLICY'].fields_by_name['creation_time']._serialized_options = b'\xe0A\x03'
    _globals['_ROWACCESSPOLICY'].fields_by_name['last_modified_time']._loaded_options = None
    _globals['_ROWACCESSPOLICY'].fields_by_name['last_modified_time']._serialized_options = b'\xe0A\x03'
    _globals['_ROWACCESSPOLICYSERVICE']._loaded_options = None
    _globals['_ROWACCESSPOLICYSERVICE']._serialized_options = b'\xcaA\x17bigquery.googleapis.com\xd2A\x90\x01https://www.googleapis.com/auth/bigquery,https://www.googleapis.com/auth/cloud-platform,https://www.googleapis.com/auth/cloud-platform.read-only'
    _globals['_ROWACCESSPOLICYSERVICE'].methods_by_name['ListRowAccessPolicies']._loaded_options = None
    _globals['_ROWACCESSPOLICYSERVICE'].methods_by_name['ListRowAccessPolicies']._serialized_options = b'\x82\xd3\xe4\x93\x02d\x12b/bigquery/v2/projects/{project_id=*}/datasets/{dataset_id=*}/tables/{table_id=*}/rowAccessPolicies'
    _globals['_LISTROWACCESSPOLICIESREQUEST']._serialized_start = 260
    _globals['_LISTROWACCESSPOLICIESREQUEST']._serialized_end = 402
    _globals['_LISTROWACCESSPOLICIESRESPONSE']._serialized_start = 405
    _globals['_LISTROWACCESSPOLICIESRESPONSE']._serialized_end = 533
    _globals['_ROWACCESSPOLICY']._serialized_start = 536
    _globals['_ROWACCESSPOLICY']._serialized_end = 814
    _globals['_ROWACCESSPOLICYSERVICE']._serialized_start = 817
    _globals['_ROWACCESSPOLICYSERVICE']._serialized_end = 1265