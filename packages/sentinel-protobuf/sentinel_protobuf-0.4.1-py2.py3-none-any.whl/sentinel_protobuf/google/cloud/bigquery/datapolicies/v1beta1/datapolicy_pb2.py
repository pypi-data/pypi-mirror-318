"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_runtime_version.ValidateProtobufRuntimeVersion(_runtime_version.Domain.PUBLIC, 5, 28, 1, '', 'google/cloud/bigquery/datapolicies/v1beta1/datapolicy.proto')
_sym_db = _symbol_database.Default()
from ......google.api import annotations_pb2 as google_dot_api_dot_annotations__pb2
from ......google.api import client_pb2 as google_dot_api_dot_client__pb2
from ......google.api import field_behavior_pb2 as google_dot_api_dot_field__behavior__pb2
from ......google.api import resource_pb2 as google_dot_api_dot_resource__pb2
from ......google.iam.v1 import iam_policy_pb2 as google_dot_iam_dot_v1_dot_iam__policy__pb2
from ......google.iam.v1 import policy_pb2 as google_dot_iam_dot_v1_dot_policy__pb2
from google.protobuf import empty_pb2 as google_dot_protobuf_dot_empty__pb2
from google.protobuf import field_mask_pb2 as google_dot_protobuf_dot_field__mask__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n;google/cloud/bigquery/datapolicies/v1beta1/datapolicy.proto\x12*google.cloud.bigquery.datapolicies.v1beta1\x1a\x1cgoogle/api/annotations.proto\x1a\x17google/api/client.proto\x1a\x1fgoogle/api/field_behavior.proto\x1a\x19google/api/resource.proto\x1a\x1egoogle/iam/v1/iam_policy.proto\x1a\x1agoogle/iam/v1/policy.proto\x1a\x1bgoogle/protobuf/empty.proto\x1a google/protobuf/field_mask.proto"\xb1\x01\n\x17CreateDataPolicyRequest\x12D\n\x06parent\x18\x01 \x01(\tB4\xe0A\x02\xfaA.\x12,bigquerydatapolicy.googleapis.com/DataPolicy\x12P\n\x0bdata_policy\x18\x02 \x01(\x0b26.google.cloud.bigquery.datapolicies.v1beta1.DataPolicyB\x03\xe0A\x02"\x9c\x01\n\x17UpdateDataPolicyRequest\x12P\n\x0bdata_policy\x18\x01 \x01(\x0b26.google.cloud.bigquery.datapolicies.v1beta1.DataPolicyB\x03\xe0A\x02\x12/\n\x0bupdate_mask\x18\x02 \x01(\x0b2\x1a.google.protobuf.FieldMask"]\n\x17DeleteDataPolicyRequest\x12B\n\x04name\x18\x01 \x01(\tB4\xe0A\x02\xfaA.\n,bigquerydatapolicy.googleapis.com/DataPolicy"Z\n\x14GetDataPolicyRequest\x12B\n\x04name\x18\x01 \x01(\tB4\xe0A\x02\xfaA.\n,bigquerydatapolicy.googleapis.com/DataPolicy"\x86\x01\n\x17ListDataPoliciesRequest\x12D\n\x06parent\x18\x01 \x01(\tB4\xe0A\x02\xfaA.\x12,bigquerydatapolicy.googleapis.com/DataPolicy\x12\x11\n\tpage_size\x18\x02 \x01(\x05\x12\x12\n\npage_token\x18\x03 \x01(\t"\x82\x01\n\x18ListDataPoliciesResponse\x12M\n\rdata_policies\x18\x01 \x03(\x0b26.google.cloud.bigquery.datapolicies.v1beta1.DataPolicy\x12\x17\n\x0fnext_page_token\x18\x02 \x01(\t"\x8e\x04\n\nDataPolicy\x12\x14\n\npolicy_tag\x18\x04 \x01(\tH\x00\x12\\\n\x13data_masking_policy\x18\x05 \x01(\x0b2=.google.cloud.bigquery.datapolicies.v1beta1.DataMaskingPolicyH\x01\x12\x11\n\x04name\x18\x01 \x01(\tB\x03\xe0A\x03\x12_\n\x10data_policy_type\x18\x02 \x01(\x0e2E.google.cloud.bigquery.datapolicies.v1beta1.DataPolicy.DataPolicyType\x12\x16\n\x0edata_policy_id\x18\x03 \x01(\t"m\n\x0eDataPolicyType\x12 \n\x1cDATA_POLICY_TYPE_UNSPECIFIED\x10\x00\x12 \n\x1cCOLUMN_LEVEL_SECURITY_POLICY\x10\x03\x12\x17\n\x13DATA_MASKING_POLICY\x10\x02:u\xeaAr\n,bigquerydatapolicy.googleapis.com/DataPolicy\x12Bprojects/{project}/locations/{location}/dataPolicies/{data_policy}B\x10\n\x0ematching_labelB\x08\n\x06policy"\x95\x02\n\x11DataMaskingPolicy\x12s\n\x15predefined_expression\x18\x01 \x01(\x0e2R.google.cloud.bigquery.datapolicies.v1beta1.DataMaskingPolicy.PredefinedExpressionH\x00"u\n\x14PredefinedExpression\x12%\n!PREDEFINED_EXPRESSION_UNSPECIFIED\x10\x00\x12\n\n\x06SHA256\x10\x03\x12\x0f\n\x0bALWAYS_NULL\x10\x05\x12\x19\n\x15DEFAULT_MASKING_VALUE\x10\x07B\x14\n\x12masking_expression2\xff\r\n\x11DataPolicyService\x12\xf0\x01\n\x10CreateDataPolicy\x12C.google.cloud.bigquery.datapolicies.v1beta1.CreateDataPolicyRequest\x1a6.google.cloud.bigquery.datapolicies.v1beta1.DataPolicy"_\xdaA\x12parent,data_policy\x82\xd3\xe4\x93\x02D"5/v1beta1/{parent=projects/*/locations/*}/dataPolicies:\x0bdata_policy\x12\x81\x02\n\x10UpdateDataPolicy\x12C.google.cloud.bigquery.datapolicies.v1beta1.UpdateDataPolicyRequest\x1a6.google.cloud.bigquery.datapolicies.v1beta1.DataPolicy"p\xdaA\x17data_policy,update_mask\x82\xd3\xe4\x93\x02P2A/v1beta1/{data_policy.name=projects/*/locations/*/dataPolicies/*}:\x0bdata_policy\x12\xb5\x01\n\x10DeleteDataPolicy\x12C.google.cloud.bigquery.datapolicies.v1beta1.DeleteDataPolicyRequest\x1a\x16.google.protobuf.Empty"D\xdaA\x04name\x82\xd3\xe4\x93\x027*5/v1beta1/{name=projects/*/locations/*/dataPolicies/*}\x12\xcf\x01\n\rGetDataPolicy\x12@.google.cloud.bigquery.datapolicies.v1beta1.GetDataPolicyRequest\x1a6.google.cloud.bigquery.datapolicies.v1beta1.DataPolicy"D\xdaA\x04name\x82\xd3\xe4\x93\x027\x125/v1beta1/{name=projects/*/locations/*/dataPolicies/*}\x12\xe5\x01\n\x10ListDataPolicies\x12C.google.cloud.bigquery.datapolicies.v1beta1.ListDataPoliciesRequest\x1aD.google.cloud.bigquery.datapolicies.v1beta1.ListDataPoliciesResponse"F\xdaA\x06parent\x82\xd3\xe4\x93\x027\x125/v1beta1/{parent=projects/*/locations/*}/dataPolicies\x12\x9c\x01\n\x0cGetIamPolicy\x12".google.iam.v1.GetIamPolicyRequest\x1a\x15.google.iam.v1.Policy"Q\x82\xd3\xe4\x93\x02K"F/v1beta1/{resource=projects/*/locations/*/dataPolicies/*}:getIamPolicy:\x01*\x12\x9c\x01\n\x0cSetIamPolicy\x12".google.iam.v1.SetIamPolicyRequest\x1a\x15.google.iam.v1.Policy"Q\x82\xd3\xe4\x93\x02K"F/v1beta1/{resource=projects/*/locations/*/dataPolicies/*}:setIamPolicy:\x01*\x12\xc2\x01\n\x12TestIamPermissions\x12(.google.iam.v1.TestIamPermissionsRequest\x1a).google.iam.v1.TestIamPermissionsResponse"W\x82\xd3\xe4\x93\x02Q"L/v1beta1/{resource=projects/*/locations/*/dataPolicies/*}:testIamPermissions:\x01*\x1a~\xcaA!bigquerydatapolicy.googleapis.com\xd2AWhttps://www.googleapis.com/auth/bigquery,https://www.googleapis.com/auth/cloud-platformB\xa2\x02\n.com.google.cloud.bigquery.datapolicies.v1beta1B\x0fDataPolicyProtoP\x01ZRcloud.google.com/go/bigquery/datapolicies/apiv1beta1/datapoliciespb;datapoliciespb\xaa\x02*Google.Cloud.BigQuery.DataPolicies.V1Beta1\xca\x02*Google\\Cloud\\BigQuery\\DataPolicies\\V1beta1\xea\x02.Google::Cloud::Bigquery::DataPolicies::V1beta1b\x06proto3')
_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'google.cloud.bigquery.datapolicies.v1beta1.datapolicy_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
    _globals['DESCRIPTOR']._loaded_options = None
    _globals['DESCRIPTOR']._serialized_options = b'\n.com.google.cloud.bigquery.datapolicies.v1beta1B\x0fDataPolicyProtoP\x01ZRcloud.google.com/go/bigquery/datapolicies/apiv1beta1/datapoliciespb;datapoliciespb\xaa\x02*Google.Cloud.BigQuery.DataPolicies.V1Beta1\xca\x02*Google\\Cloud\\BigQuery\\DataPolicies\\V1beta1\xea\x02.Google::Cloud::Bigquery::DataPolicies::V1beta1'
    _globals['_CREATEDATAPOLICYREQUEST'].fields_by_name['parent']._loaded_options = None
    _globals['_CREATEDATAPOLICYREQUEST'].fields_by_name['parent']._serialized_options = b'\xe0A\x02\xfaA.\x12,bigquerydatapolicy.googleapis.com/DataPolicy'
    _globals['_CREATEDATAPOLICYREQUEST'].fields_by_name['data_policy']._loaded_options = None
    _globals['_CREATEDATAPOLICYREQUEST'].fields_by_name['data_policy']._serialized_options = b'\xe0A\x02'
    _globals['_UPDATEDATAPOLICYREQUEST'].fields_by_name['data_policy']._loaded_options = None
    _globals['_UPDATEDATAPOLICYREQUEST'].fields_by_name['data_policy']._serialized_options = b'\xe0A\x02'
    _globals['_DELETEDATAPOLICYREQUEST'].fields_by_name['name']._loaded_options = None
    _globals['_DELETEDATAPOLICYREQUEST'].fields_by_name['name']._serialized_options = b'\xe0A\x02\xfaA.\n,bigquerydatapolicy.googleapis.com/DataPolicy'
    _globals['_GETDATAPOLICYREQUEST'].fields_by_name['name']._loaded_options = None
    _globals['_GETDATAPOLICYREQUEST'].fields_by_name['name']._serialized_options = b'\xe0A\x02\xfaA.\n,bigquerydatapolicy.googleapis.com/DataPolicy'
    _globals['_LISTDATAPOLICIESREQUEST'].fields_by_name['parent']._loaded_options = None
    _globals['_LISTDATAPOLICIESREQUEST'].fields_by_name['parent']._serialized_options = b'\xe0A\x02\xfaA.\x12,bigquerydatapolicy.googleapis.com/DataPolicy'
    _globals['_DATAPOLICY'].fields_by_name['name']._loaded_options = None
    _globals['_DATAPOLICY'].fields_by_name['name']._serialized_options = b'\xe0A\x03'
    _globals['_DATAPOLICY']._loaded_options = None
    _globals['_DATAPOLICY']._serialized_options = b'\xeaAr\n,bigquerydatapolicy.googleapis.com/DataPolicy\x12Bprojects/{project}/locations/{location}/dataPolicies/{data_policy}'
    _globals['_DATAPOLICYSERVICE']._loaded_options = None
    _globals['_DATAPOLICYSERVICE']._serialized_options = b'\xcaA!bigquerydatapolicy.googleapis.com\xd2AWhttps://www.googleapis.com/auth/bigquery,https://www.googleapis.com/auth/cloud-platform'
    _globals['_DATAPOLICYSERVICE'].methods_by_name['CreateDataPolicy']._loaded_options = None
    _globals['_DATAPOLICYSERVICE'].methods_by_name['CreateDataPolicy']._serialized_options = b'\xdaA\x12parent,data_policy\x82\xd3\xe4\x93\x02D"5/v1beta1/{parent=projects/*/locations/*}/dataPolicies:\x0bdata_policy'
    _globals['_DATAPOLICYSERVICE'].methods_by_name['UpdateDataPolicy']._loaded_options = None
    _globals['_DATAPOLICYSERVICE'].methods_by_name['UpdateDataPolicy']._serialized_options = b'\xdaA\x17data_policy,update_mask\x82\xd3\xe4\x93\x02P2A/v1beta1/{data_policy.name=projects/*/locations/*/dataPolicies/*}:\x0bdata_policy'
    _globals['_DATAPOLICYSERVICE'].methods_by_name['DeleteDataPolicy']._loaded_options = None
    _globals['_DATAPOLICYSERVICE'].methods_by_name['DeleteDataPolicy']._serialized_options = b'\xdaA\x04name\x82\xd3\xe4\x93\x027*5/v1beta1/{name=projects/*/locations/*/dataPolicies/*}'
    _globals['_DATAPOLICYSERVICE'].methods_by_name['GetDataPolicy']._loaded_options = None
    _globals['_DATAPOLICYSERVICE'].methods_by_name['GetDataPolicy']._serialized_options = b'\xdaA\x04name\x82\xd3\xe4\x93\x027\x125/v1beta1/{name=projects/*/locations/*/dataPolicies/*}'
    _globals['_DATAPOLICYSERVICE'].methods_by_name['ListDataPolicies']._loaded_options = None
    _globals['_DATAPOLICYSERVICE'].methods_by_name['ListDataPolicies']._serialized_options = b'\xdaA\x06parent\x82\xd3\xe4\x93\x027\x125/v1beta1/{parent=projects/*/locations/*}/dataPolicies'
    _globals['_DATAPOLICYSERVICE'].methods_by_name['GetIamPolicy']._loaded_options = None
    _globals['_DATAPOLICYSERVICE'].methods_by_name['GetIamPolicy']._serialized_options = b'\x82\xd3\xe4\x93\x02K"F/v1beta1/{resource=projects/*/locations/*/dataPolicies/*}:getIamPolicy:\x01*'
    _globals['_DATAPOLICYSERVICE'].methods_by_name['SetIamPolicy']._loaded_options = None
    _globals['_DATAPOLICYSERVICE'].methods_by_name['SetIamPolicy']._serialized_options = b'\x82\xd3\xe4\x93\x02K"F/v1beta1/{resource=projects/*/locations/*/dataPolicies/*}:setIamPolicy:\x01*'
    _globals['_DATAPOLICYSERVICE'].methods_by_name['TestIamPermissions']._loaded_options = None
    _globals['_DATAPOLICYSERVICE'].methods_by_name['TestIamPermissions']._serialized_options = b'\x82\xd3\xe4\x93\x02Q"L/v1beta1/{resource=projects/*/locations/*/dataPolicies/*}:testIamPermissions:\x01*'
    _globals['_CREATEDATAPOLICYREQUEST']._serialized_start = 346
    _globals['_CREATEDATAPOLICYREQUEST']._serialized_end = 523
    _globals['_UPDATEDATAPOLICYREQUEST']._serialized_start = 526
    _globals['_UPDATEDATAPOLICYREQUEST']._serialized_end = 682
    _globals['_DELETEDATAPOLICYREQUEST']._serialized_start = 684
    _globals['_DELETEDATAPOLICYREQUEST']._serialized_end = 777
    _globals['_GETDATAPOLICYREQUEST']._serialized_start = 779
    _globals['_GETDATAPOLICYREQUEST']._serialized_end = 869
    _globals['_LISTDATAPOLICIESREQUEST']._serialized_start = 872
    _globals['_LISTDATAPOLICIESREQUEST']._serialized_end = 1006
    _globals['_LISTDATAPOLICIESRESPONSE']._serialized_start = 1009
    _globals['_LISTDATAPOLICIESRESPONSE']._serialized_end = 1139
    _globals['_DATAPOLICY']._serialized_start = 1142
    _globals['_DATAPOLICY']._serialized_end = 1668
    _globals['_DATAPOLICY_DATAPOLICYTYPE']._serialized_start = 1412
    _globals['_DATAPOLICY_DATAPOLICYTYPE']._serialized_end = 1521
    _globals['_DATAMASKINGPOLICY']._serialized_start = 1671
    _globals['_DATAMASKINGPOLICY']._serialized_end = 1948
    _globals['_DATAMASKINGPOLICY_PREDEFINEDEXPRESSION']._serialized_start = 1809
    _globals['_DATAMASKINGPOLICY_PREDEFINEDEXPRESSION']._serialized_end = 1926
    _globals['_DATAPOLICYSERVICE']._serialized_start = 1951
    _globals['_DATAPOLICYSERVICE']._serialized_end = 3742