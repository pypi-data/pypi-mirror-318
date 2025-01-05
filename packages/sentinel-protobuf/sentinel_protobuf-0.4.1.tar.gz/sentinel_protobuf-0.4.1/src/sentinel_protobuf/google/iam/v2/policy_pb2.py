"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_runtime_version.ValidateProtobufRuntimeVersion(_runtime_version.Domain.PUBLIC, 5, 28, 1, '', 'google/iam/v2/policy.proto')
_sym_db = _symbol_database.Default()
from ....google.api import annotations_pb2 as google_dot_api_dot_annotations__pb2
from ....google.api import client_pb2 as google_dot_api_dot_client__pb2
from ....google.api import field_behavior_pb2 as google_dot_api_dot_field__behavior__pb2
from ....google.iam.v2 import deny_pb2 as google_dot_iam_dot_v2_dot_deny__pb2
from ....google.longrunning import operations_pb2 as google_dot_longrunning_dot_operations__pb2
from google.protobuf import timestamp_pb2 as google_dot_protobuf_dot_timestamp__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x1agoogle/iam/v2/policy.proto\x12\rgoogle.iam.v2\x1a\x1cgoogle/api/annotations.proto\x1a\x17google/api/client.proto\x1a\x1fgoogle/api/field_behavior.proto\x1a\x18google/iam/v2/deny.proto\x1a#google/longrunning/operations.proto\x1a\x1fgoogle/protobuf/timestamp.proto"\xc2\x03\n\x06Policy\x12\x11\n\x04name\x18\x01 \x01(\tB\x03\xe0A\x05\x12\x10\n\x03uid\x18\x02 \x01(\tB\x03\xe0A\x05\x12\x11\n\x04kind\x18\x03 \x01(\tB\x03\xe0A\x03\x12\x14\n\x0cdisplay_name\x18\x04 \x01(\t\x12;\n\x0bannotations\x18\x05 \x03(\x0b2&.google.iam.v2.Policy.AnnotationsEntry\x12\x0c\n\x04etag\x18\x06 \x01(\t\x124\n\x0bcreate_time\x18\x07 \x01(\x0b2\x1a.google.protobuf.TimestampB\x03\xe0A\x03\x124\n\x0bupdate_time\x18\x08 \x01(\x0b2\x1a.google.protobuf.TimestampB\x03\xe0A\x03\x124\n\x0bdelete_time\x18\t \x01(\x0b2\x1a.google.protobuf.TimestampB\x03\xe0A\x03\x12(\n\x05rules\x18\n \x03(\x0b2\x19.google.iam.v2.PolicyRule\x12\x1f\n\x12managing_authority\x18\x0b \x01(\tB\x03\xe0A\x05\x1a2\n\x10AnnotationsEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\r\n\x05value\x18\x02 \x01(\t:\x028\x01"W\n\nPolicyRule\x12,\n\tdeny_rule\x18\x02 \x01(\x0b2\x17.google.iam.v2.DenyRuleH\x00\x12\x13\n\x0bdescription\x18\x01 \x01(\tB\x06\n\x04kind"Q\n\x13ListPoliciesRequest\x12\x13\n\x06parent\x18\x01 \x01(\tB\x03\xe0A\x02\x12\x11\n\tpage_size\x18\x02 \x01(\x05\x12\x12\n\npage_token\x18\x03 \x01(\t"X\n\x14ListPoliciesResponse\x12\'\n\x08policies\x18\x01 \x03(\x0b2\x15.google.iam.v2.Policy\x12\x17\n\x0fnext_page_token\x18\x02 \x01(\t"%\n\x10GetPolicyRequest\x12\x11\n\x04name\x18\x01 \x01(\tB\x03\xe0A\x02"i\n\x13CreatePolicyRequest\x12\x13\n\x06parent\x18\x01 \x01(\tB\x03\xe0A\x02\x12*\n\x06policy\x18\x02 \x01(\x0b2\x15.google.iam.v2.PolicyB\x03\xe0A\x02\x12\x11\n\tpolicy_id\x18\x03 \x01(\t"A\n\x13UpdatePolicyRequest\x12*\n\x06policy\x18\x01 \x01(\x0b2\x15.google.iam.v2.PolicyB\x03\xe0A\x02";\n\x13DeletePolicyRequest\x12\x11\n\x04name\x18\x01 \x01(\tB\x03\xe0A\x02\x12\x11\n\x04etag\x18\x02 \x01(\tB\x03\xe0A\x01"J\n\x17PolicyOperationMetadata\x12/\n\x0bcreate_time\x18\x01 \x01(\x0b2\x1a.google.protobuf.Timestamp2\xd0\x06\n\x08Policies\x12\x83\x01\n\x0cListPolicies\x12".google.iam.v2.ListPoliciesRequest\x1a#.google.iam.v2.ListPoliciesResponse"*\xdaA\x06parent\x82\xd3\xe4\x93\x02\x1b\x12\x19/v2/{parent=policies/*/*}\x12m\n\tGetPolicy\x12\x1f.google.iam.v2.GetPolicyRequest\x1a\x15.google.iam.v2.Policy"(\xdaA\x04name\x82\xd3\xe4\x93\x02\x1b\x12\x19/v2/{name=policies/*/*/*}\x12\xba\x01\n\x0cCreatePolicy\x12".google.iam.v2.CreatePolicyRequest\x1a\x1d.google.longrunning.Operation"g\xcaA!\n\x06Policy\x12\x17PolicyOperationMetadata\xdaA\x17parent,policy,policy_id\x82\xd3\xe4\x93\x02#"\x19/v2/{parent=policies/*/*}:\x06policy\x12\xa7\x01\n\x0cUpdatePolicy\x12".google.iam.v2.UpdatePolicyRequest\x1a\x1d.google.longrunning.Operation"T\xcaA!\n\x06Policy\x12\x17PolicyOperationMetadata\x82\xd3\xe4\x93\x02*\x1a /v2/{policy.name=policies/*/*/*}:\x06policy\x12\x9f\x01\n\x0cDeletePolicy\x12".google.iam.v2.DeletePolicyRequest\x1a\x1d.google.longrunning.Operation"L\xcaA!\n\x06Policy\x12\x17PolicyOperationMetadata\xdaA\x04name\x82\xd3\xe4\x93\x02\x1b*\x19/v2/{name=policies/*/*/*}\x1aF\xcaA\x12iam.googleapis.com\xd2A.https://www.googleapis.com/auth/cloud-platformBy\n\x11com.google.iam.v2B\x0bPolicyProtoP\x01Z)cloud.google.com/go/iam/apiv2/iampb;iampb\xaa\x02\x13Google.Cloud.Iam.V2\xca\x02\x13Google\\Cloud\\Iam\\V2b\x06proto3')
_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'google.iam.v2.policy_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
    _globals['DESCRIPTOR']._loaded_options = None
    _globals['DESCRIPTOR']._serialized_options = b'\n\x11com.google.iam.v2B\x0bPolicyProtoP\x01Z)cloud.google.com/go/iam/apiv2/iampb;iampb\xaa\x02\x13Google.Cloud.Iam.V2\xca\x02\x13Google\\Cloud\\Iam\\V2'
    _globals['_POLICY_ANNOTATIONSENTRY']._loaded_options = None
    _globals['_POLICY_ANNOTATIONSENTRY']._serialized_options = b'8\x01'
    _globals['_POLICY'].fields_by_name['name']._loaded_options = None
    _globals['_POLICY'].fields_by_name['name']._serialized_options = b'\xe0A\x05'
    _globals['_POLICY'].fields_by_name['uid']._loaded_options = None
    _globals['_POLICY'].fields_by_name['uid']._serialized_options = b'\xe0A\x05'
    _globals['_POLICY'].fields_by_name['kind']._loaded_options = None
    _globals['_POLICY'].fields_by_name['kind']._serialized_options = b'\xe0A\x03'
    _globals['_POLICY'].fields_by_name['create_time']._loaded_options = None
    _globals['_POLICY'].fields_by_name['create_time']._serialized_options = b'\xe0A\x03'
    _globals['_POLICY'].fields_by_name['update_time']._loaded_options = None
    _globals['_POLICY'].fields_by_name['update_time']._serialized_options = b'\xe0A\x03'
    _globals['_POLICY'].fields_by_name['delete_time']._loaded_options = None
    _globals['_POLICY'].fields_by_name['delete_time']._serialized_options = b'\xe0A\x03'
    _globals['_POLICY'].fields_by_name['managing_authority']._loaded_options = None
    _globals['_POLICY'].fields_by_name['managing_authority']._serialized_options = b'\xe0A\x05'
    _globals['_LISTPOLICIESREQUEST'].fields_by_name['parent']._loaded_options = None
    _globals['_LISTPOLICIESREQUEST'].fields_by_name['parent']._serialized_options = b'\xe0A\x02'
    _globals['_GETPOLICYREQUEST'].fields_by_name['name']._loaded_options = None
    _globals['_GETPOLICYREQUEST'].fields_by_name['name']._serialized_options = b'\xe0A\x02'
    _globals['_CREATEPOLICYREQUEST'].fields_by_name['parent']._loaded_options = None
    _globals['_CREATEPOLICYREQUEST'].fields_by_name['parent']._serialized_options = b'\xe0A\x02'
    _globals['_CREATEPOLICYREQUEST'].fields_by_name['policy']._loaded_options = None
    _globals['_CREATEPOLICYREQUEST'].fields_by_name['policy']._serialized_options = b'\xe0A\x02'
    _globals['_UPDATEPOLICYREQUEST'].fields_by_name['policy']._loaded_options = None
    _globals['_UPDATEPOLICYREQUEST'].fields_by_name['policy']._serialized_options = b'\xe0A\x02'
    _globals['_DELETEPOLICYREQUEST'].fields_by_name['name']._loaded_options = None
    _globals['_DELETEPOLICYREQUEST'].fields_by_name['name']._serialized_options = b'\xe0A\x02'
    _globals['_DELETEPOLICYREQUEST'].fields_by_name['etag']._loaded_options = None
    _globals['_DELETEPOLICYREQUEST'].fields_by_name['etag']._serialized_options = b'\xe0A\x01'
    _globals['_POLICIES']._loaded_options = None
    _globals['_POLICIES']._serialized_options = b'\xcaA\x12iam.googleapis.com\xd2A.https://www.googleapis.com/auth/cloud-platform'
    _globals['_POLICIES'].methods_by_name['ListPolicies']._loaded_options = None
    _globals['_POLICIES'].methods_by_name['ListPolicies']._serialized_options = b'\xdaA\x06parent\x82\xd3\xe4\x93\x02\x1b\x12\x19/v2/{parent=policies/*/*}'
    _globals['_POLICIES'].methods_by_name['GetPolicy']._loaded_options = None
    _globals['_POLICIES'].methods_by_name['GetPolicy']._serialized_options = b'\xdaA\x04name\x82\xd3\xe4\x93\x02\x1b\x12\x19/v2/{name=policies/*/*/*}'
    _globals['_POLICIES'].methods_by_name['CreatePolicy']._loaded_options = None
    _globals['_POLICIES'].methods_by_name['CreatePolicy']._serialized_options = b'\xcaA!\n\x06Policy\x12\x17PolicyOperationMetadata\xdaA\x17parent,policy,policy_id\x82\xd3\xe4\x93\x02#"\x19/v2/{parent=policies/*/*}:\x06policy'
    _globals['_POLICIES'].methods_by_name['UpdatePolicy']._loaded_options = None
    _globals['_POLICIES'].methods_by_name['UpdatePolicy']._serialized_options = b'\xcaA!\n\x06Policy\x12\x17PolicyOperationMetadata\x82\xd3\xe4\x93\x02*\x1a /v2/{policy.name=policies/*/*/*}:\x06policy'
    _globals['_POLICIES'].methods_by_name['DeletePolicy']._loaded_options = None
    _globals['_POLICIES'].methods_by_name['DeletePolicy']._serialized_options = b'\xcaA!\n\x06Policy\x12\x17PolicyOperationMetadata\xdaA\x04name\x82\xd3\xe4\x93\x02\x1b*\x19/v2/{name=policies/*/*/*}'
    _globals['_POLICY']._serialized_start = 230
    _globals['_POLICY']._serialized_end = 680
    _globals['_POLICY_ANNOTATIONSENTRY']._serialized_start = 630
    _globals['_POLICY_ANNOTATIONSENTRY']._serialized_end = 680
    _globals['_POLICYRULE']._serialized_start = 682
    _globals['_POLICYRULE']._serialized_end = 769
    _globals['_LISTPOLICIESREQUEST']._serialized_start = 771
    _globals['_LISTPOLICIESREQUEST']._serialized_end = 852
    _globals['_LISTPOLICIESRESPONSE']._serialized_start = 854
    _globals['_LISTPOLICIESRESPONSE']._serialized_end = 942
    _globals['_GETPOLICYREQUEST']._serialized_start = 944
    _globals['_GETPOLICYREQUEST']._serialized_end = 981
    _globals['_CREATEPOLICYREQUEST']._serialized_start = 983
    _globals['_CREATEPOLICYREQUEST']._serialized_end = 1088
    _globals['_UPDATEPOLICYREQUEST']._serialized_start = 1090
    _globals['_UPDATEPOLICYREQUEST']._serialized_end = 1155
    _globals['_DELETEPOLICYREQUEST']._serialized_start = 1157
    _globals['_DELETEPOLICYREQUEST']._serialized_end = 1216
    _globals['_POLICYOPERATIONMETADATA']._serialized_start = 1218
    _globals['_POLICYOPERATIONMETADATA']._serialized_end = 1292
    _globals['_POLICIES']._serialized_start = 1295
    _globals['_POLICIES']._serialized_end = 2143