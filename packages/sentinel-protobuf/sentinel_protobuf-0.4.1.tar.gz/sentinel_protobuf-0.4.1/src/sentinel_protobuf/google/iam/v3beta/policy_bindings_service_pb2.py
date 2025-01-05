"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_runtime_version.ValidateProtobufRuntimeVersion(_runtime_version.Domain.PUBLIC, 5, 28, 1, '', 'google/iam/v3beta/policy_bindings_service.proto')
_sym_db = _symbol_database.Default()
from ....google.api import annotations_pb2 as google_dot_api_dot_annotations__pb2
from ....google.api import client_pb2 as google_dot_api_dot_client__pb2
from ....google.api import field_behavior_pb2 as google_dot_api_dot_field__behavior__pb2
from ....google.api import resource_pb2 as google_dot_api_dot_resource__pb2
from ....google.iam.v3beta import operation_metadata_pb2 as google_dot_iam_dot_v3beta_dot_operation__metadata__pb2
from ....google.iam.v3beta import policy_binding_resources_pb2 as google_dot_iam_dot_v3beta_dot_policy__binding__resources__pb2
from ....google.longrunning import operations_pb2 as google_dot_longrunning_dot_operations__pb2
from google.protobuf import empty_pb2 as google_dot_protobuf_dot_empty__pb2
from google.protobuf import field_mask_pb2 as google_dot_protobuf_dot_field__mask__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n/google/iam/v3beta/policy_bindings_service.proto\x12\x11google.iam.v3beta\x1a\x1cgoogle/api/annotations.proto\x1a\x17google/api/client.proto\x1a\x1fgoogle/api/field_behavior.proto\x1a\x19google/api/resource.proto\x1a*google/iam/v3beta/operation_metadata.proto\x1a0google/iam/v3beta/policy_binding_resources.proto\x1a#google/longrunning/operations.proto\x1a\x1bgoogle/protobuf/empty.proto\x1a google/protobuf/field_mask.proto"\xd1\x01\n\x1aCreatePolicyBindingRequest\x128\n\x06parent\x18\x01 \x01(\tB(\xe0A\x02\xfaA"\x12 iam.googleapis.com/PolicyBinding\x12\x1e\n\x11policy_binding_id\x18\x02 \x01(\tB\x03\xe0A\x02\x12=\n\x0epolicy_binding\x18\x03 \x01(\x0b2 .google.iam.v3beta.PolicyBindingB\x03\xe0A\x02\x12\x1a\n\rvalidate_only\x18\x04 \x01(\x08B\x03\xe0A\x01"Q\n\x17GetPolicyBindingRequest\x126\n\x04name\x18\x01 \x01(\tB(\xe0A\x02\xfaA"\n iam.googleapis.com/PolicyBinding"\xad\x01\n\x1aUpdatePolicyBindingRequest\x12=\n\x0epolicy_binding\x18\x01 \x01(\x0b2 .google.iam.v3beta.PolicyBindingB\x03\xe0A\x02\x12\x1a\n\rvalidate_only\x18\x02 \x01(\x08B\x03\xe0A\x01\x124\n\x0bupdate_mask\x18\x03 \x01(\x0b2\x1a.google.protobuf.FieldMaskB\x03\xe0A\x01"\x83\x01\n\x1aDeletePolicyBindingRequest\x126\n\x04name\x18\x01 \x01(\tB(\xe0A\x02\xfaA"\n iam.googleapis.com/PolicyBinding\x12\x11\n\x04etag\x18\x02 \x01(\tB\x03\xe0A\x01\x12\x1a\n\rvalidate_only\x18\x03 \x01(\x08B\x03\xe0A\x01"\x9b\x01\n\x19ListPolicyBindingsRequest\x128\n\x06parent\x18\x01 \x01(\tB(\xe0A\x02\xfaA"\x12 iam.googleapis.com/PolicyBinding\x12\x16\n\tpage_size\x18\x02 \x01(\x05B\x03\xe0A\x01\x12\x17\n\npage_token\x18\x03 \x01(\tB\x03\xe0A\x01\x12\x13\n\x06filter\x18\x04 \x01(\tB\x03\xe0A\x01"u\n\x1aListPolicyBindingsResponse\x129\n\x0fpolicy_bindings\x18\x01 \x03(\x0b2 .google.iam.v3beta.PolicyBinding\x12\x1c\n\x0fnext_page_token\x18\x02 \x01(\tB\x03\xe0A\x01"\xa3\x01\n!SearchTargetPolicyBindingsRequest\x12\x13\n\x06target\x18\x01 \x01(\tB\x03\xe0A\x02\x12\x16\n\tpage_size\x18\x02 \x01(\x05B\x03\xe0A\x01\x12\x17\n\npage_token\x18\x03 \x01(\tB\x03\xe0A\x01\x128\n\x06parent\x18\x05 \x01(\tB(\xe0A\x02\xfaA"\x12 iam.googleapis.com/PolicyBinding"}\n"SearchTargetPolicyBindingsResponse\x129\n\x0fpolicy_bindings\x18\x01 \x03(\x0b2 .google.iam.v3beta.PolicyBinding\x12\x1c\n\x0fnext_page_token\x18\x02 \x01(\tB\x03\xe0A\x012\x8c\x12\n\x0ePolicyBindings\x12\x9c\x03\n\x13CreatePolicyBinding\x12-.google.iam.v3beta.CreatePolicyBindingRequest\x1a\x1d.google.longrunning.Operation"\xb6\x02\xcaA"\n\rPolicyBinding\x12\x11OperationMetadata\xdaA\'parent,policy_binding,policy_binding_id\x82\xd3\xe4\x93\x02\xe0\x01"6/v3beta/{parent=projects/*/locations/*}/policyBindings:\x0epolicy_bindingZG"5/v3beta/{parent=folders/*/locations/*}/policyBindings:\x0epolicy_bindingZM";/v3beta/{parent=organizations/*/locations/*}/policyBindings:\x0epolicy_binding\x12\xa1\x02\n\x10GetPolicyBinding\x12*.google.iam.v3beta.GetPolicyBindingRequest\x1a .google.iam.v3beta.PolicyBinding"\xbe\x01\xdaA\x04name\x82\xd3\xe4\x93\x02\xb0\x01\x126/v3beta/{name=projects/*/locations/*/policyBindings/*}Z7\x125/v3beta/{name=folders/*/locations/*/policyBindings/*}Z=\x12;/v3beta/{name=organizations/*/locations/*/policyBindings/*}\x12\xbc\x03\n\x13UpdatePolicyBinding\x12-.google.iam.v3beta.UpdatePolicyBindingRequest\x1a\x1d.google.longrunning.Operation"\xd6\x02\xcaA"\n\rPolicyBinding\x12\x11OperationMetadata\xdaA\x1apolicy_binding,update_mask\x82\xd3\xe4\x93\x02\x8d\x022E/v3beta/{policy_binding.name=projects/*/locations/*/policyBindings/*}:\x0epolicy_bindingZV2D/v3beta/{policy_binding.name=folders/*/locations/*/policyBindings/*}:\x0epolicy_bindingZ\\2J/v3beta/{policy_binding.name=organizations/*/locations/*/policyBindings/*}:\x0epolicy_binding\x12\xd1\x02\n\x13DeletePolicyBinding\x12-.google.iam.v3beta.DeletePolicyBindingRequest\x1a\x1d.google.longrunning.Operation"\xeb\x01\xcaA*\n\x15google.protobuf.Empty\x12\x11OperationMetadata\xdaA\x04name\x82\xd3\xe4\x93\x02\xb0\x01*6/v3beta/{name=projects/*/locations/*/policyBindings/*}Z7*5/v3beta/{name=folders/*/locations/*/policyBindings/*}Z=*;/v3beta/{name=organizations/*/locations/*/policyBindings/*}\x12\xb4\x02\n\x12ListPolicyBindings\x12,.google.iam.v3beta.ListPolicyBindingsRequest\x1a-.google.iam.v3beta.ListPolicyBindingsResponse"\xc0\x01\xdaA\x06parent\x82\xd3\xe4\x93\x02\xb0\x01\x126/v3beta/{parent=projects/*/locations/*}/policyBindingsZ7\x125/v3beta/{parent=folders/*/locations/*}/policyBindingsZ=\x12;/v3beta/{parent=organizations/*/locations/*}/policyBindings\x12\xa4\x03\n\x1aSearchTargetPolicyBindings\x124.google.iam.v3beta.SearchTargetPolicyBindingsRequest\x1a5.google.iam.v3beta.SearchTargetPolicyBindingsResponse"\x98\x02\xdaA\rparent,target\x82\xd3\xe4\x93\x02\x81\x02\x12Q/v3beta/{parent=projects/*/locations/*}/policyBindings:searchTargetPolicyBindingsZR\x12P/v3beta/{parent=folders/*/locations/*}/policyBindings:searchTargetPolicyBindingsZX\x12V/v3beta/{parent=organizations/*/locations/*}/policyBindings:searchTargetPolicyBindings\x1aF\xcaA\x12iam.googleapis.com\xd2A.https://www.googleapis.com/auth/cloud-platformB\xaa\x02\n\x15com.google.iam.v3betaB\x1aPolicyBindingsServiceProtoP\x01Z-cloud.google.com/go/iam/apiv3beta/iampb;iampb\xaa\x02\x17Google.Cloud.Iam.V3Beta\xeaA\\\n\'iam.googleapis.com/OrganizationLocation\x121organizations/{organization}/locations/{location}\xeaAJ\n!iam.googleapis.com/FolderLocation\x12%folders/{folder}/locations/{location}b\x06proto3')
_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'google.iam.v3beta.policy_bindings_service_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
    _globals['DESCRIPTOR']._loaded_options = None
    _globals['DESCRIPTOR']._serialized_options = b"\n\x15com.google.iam.v3betaB\x1aPolicyBindingsServiceProtoP\x01Z-cloud.google.com/go/iam/apiv3beta/iampb;iampb\xaa\x02\x17Google.Cloud.Iam.V3Beta\xeaA\\\n'iam.googleapis.com/OrganizationLocation\x121organizations/{organization}/locations/{location}\xeaAJ\n!iam.googleapis.com/FolderLocation\x12%folders/{folder}/locations/{location}"
    _globals['_CREATEPOLICYBINDINGREQUEST'].fields_by_name['parent']._loaded_options = None
    _globals['_CREATEPOLICYBINDINGREQUEST'].fields_by_name['parent']._serialized_options = b'\xe0A\x02\xfaA"\x12 iam.googleapis.com/PolicyBinding'
    _globals['_CREATEPOLICYBINDINGREQUEST'].fields_by_name['policy_binding_id']._loaded_options = None
    _globals['_CREATEPOLICYBINDINGREQUEST'].fields_by_name['policy_binding_id']._serialized_options = b'\xe0A\x02'
    _globals['_CREATEPOLICYBINDINGREQUEST'].fields_by_name['policy_binding']._loaded_options = None
    _globals['_CREATEPOLICYBINDINGREQUEST'].fields_by_name['policy_binding']._serialized_options = b'\xe0A\x02'
    _globals['_CREATEPOLICYBINDINGREQUEST'].fields_by_name['validate_only']._loaded_options = None
    _globals['_CREATEPOLICYBINDINGREQUEST'].fields_by_name['validate_only']._serialized_options = b'\xe0A\x01'
    _globals['_GETPOLICYBINDINGREQUEST'].fields_by_name['name']._loaded_options = None
    _globals['_GETPOLICYBINDINGREQUEST'].fields_by_name['name']._serialized_options = b'\xe0A\x02\xfaA"\n iam.googleapis.com/PolicyBinding'
    _globals['_UPDATEPOLICYBINDINGREQUEST'].fields_by_name['policy_binding']._loaded_options = None
    _globals['_UPDATEPOLICYBINDINGREQUEST'].fields_by_name['policy_binding']._serialized_options = b'\xe0A\x02'
    _globals['_UPDATEPOLICYBINDINGREQUEST'].fields_by_name['validate_only']._loaded_options = None
    _globals['_UPDATEPOLICYBINDINGREQUEST'].fields_by_name['validate_only']._serialized_options = b'\xe0A\x01'
    _globals['_UPDATEPOLICYBINDINGREQUEST'].fields_by_name['update_mask']._loaded_options = None
    _globals['_UPDATEPOLICYBINDINGREQUEST'].fields_by_name['update_mask']._serialized_options = b'\xe0A\x01'
    _globals['_DELETEPOLICYBINDINGREQUEST'].fields_by_name['name']._loaded_options = None
    _globals['_DELETEPOLICYBINDINGREQUEST'].fields_by_name['name']._serialized_options = b'\xe0A\x02\xfaA"\n iam.googleapis.com/PolicyBinding'
    _globals['_DELETEPOLICYBINDINGREQUEST'].fields_by_name['etag']._loaded_options = None
    _globals['_DELETEPOLICYBINDINGREQUEST'].fields_by_name['etag']._serialized_options = b'\xe0A\x01'
    _globals['_DELETEPOLICYBINDINGREQUEST'].fields_by_name['validate_only']._loaded_options = None
    _globals['_DELETEPOLICYBINDINGREQUEST'].fields_by_name['validate_only']._serialized_options = b'\xe0A\x01'
    _globals['_LISTPOLICYBINDINGSREQUEST'].fields_by_name['parent']._loaded_options = None
    _globals['_LISTPOLICYBINDINGSREQUEST'].fields_by_name['parent']._serialized_options = b'\xe0A\x02\xfaA"\x12 iam.googleapis.com/PolicyBinding'
    _globals['_LISTPOLICYBINDINGSREQUEST'].fields_by_name['page_size']._loaded_options = None
    _globals['_LISTPOLICYBINDINGSREQUEST'].fields_by_name['page_size']._serialized_options = b'\xe0A\x01'
    _globals['_LISTPOLICYBINDINGSREQUEST'].fields_by_name['page_token']._loaded_options = None
    _globals['_LISTPOLICYBINDINGSREQUEST'].fields_by_name['page_token']._serialized_options = b'\xe0A\x01'
    _globals['_LISTPOLICYBINDINGSREQUEST'].fields_by_name['filter']._loaded_options = None
    _globals['_LISTPOLICYBINDINGSREQUEST'].fields_by_name['filter']._serialized_options = b'\xe0A\x01'
    _globals['_LISTPOLICYBINDINGSRESPONSE'].fields_by_name['next_page_token']._loaded_options = None
    _globals['_LISTPOLICYBINDINGSRESPONSE'].fields_by_name['next_page_token']._serialized_options = b'\xe0A\x01'
    _globals['_SEARCHTARGETPOLICYBINDINGSREQUEST'].fields_by_name['target']._loaded_options = None
    _globals['_SEARCHTARGETPOLICYBINDINGSREQUEST'].fields_by_name['target']._serialized_options = b'\xe0A\x02'
    _globals['_SEARCHTARGETPOLICYBINDINGSREQUEST'].fields_by_name['page_size']._loaded_options = None
    _globals['_SEARCHTARGETPOLICYBINDINGSREQUEST'].fields_by_name['page_size']._serialized_options = b'\xe0A\x01'
    _globals['_SEARCHTARGETPOLICYBINDINGSREQUEST'].fields_by_name['page_token']._loaded_options = None
    _globals['_SEARCHTARGETPOLICYBINDINGSREQUEST'].fields_by_name['page_token']._serialized_options = b'\xe0A\x01'
    _globals['_SEARCHTARGETPOLICYBINDINGSREQUEST'].fields_by_name['parent']._loaded_options = None
    _globals['_SEARCHTARGETPOLICYBINDINGSREQUEST'].fields_by_name['parent']._serialized_options = b'\xe0A\x02\xfaA"\x12 iam.googleapis.com/PolicyBinding'
    _globals['_SEARCHTARGETPOLICYBINDINGSRESPONSE'].fields_by_name['next_page_token']._loaded_options = None
    _globals['_SEARCHTARGETPOLICYBINDINGSRESPONSE'].fields_by_name['next_page_token']._serialized_options = b'\xe0A\x01'
    _globals['_POLICYBINDINGS']._loaded_options = None
    _globals['_POLICYBINDINGS']._serialized_options = b'\xcaA\x12iam.googleapis.com\xd2A.https://www.googleapis.com/auth/cloud-platform'
    _globals['_POLICYBINDINGS'].methods_by_name['CreatePolicyBinding']._loaded_options = None
    _globals['_POLICYBINDINGS'].methods_by_name['CreatePolicyBinding']._serialized_options = b'\xcaA"\n\rPolicyBinding\x12\x11OperationMetadata\xdaA\'parent,policy_binding,policy_binding_id\x82\xd3\xe4\x93\x02\xe0\x01"6/v3beta/{parent=projects/*/locations/*}/policyBindings:\x0epolicy_bindingZG"5/v3beta/{parent=folders/*/locations/*}/policyBindings:\x0epolicy_bindingZM";/v3beta/{parent=organizations/*/locations/*}/policyBindings:\x0epolicy_binding'
    _globals['_POLICYBINDINGS'].methods_by_name['GetPolicyBinding']._loaded_options = None
    _globals['_POLICYBINDINGS'].methods_by_name['GetPolicyBinding']._serialized_options = b'\xdaA\x04name\x82\xd3\xe4\x93\x02\xb0\x01\x126/v3beta/{name=projects/*/locations/*/policyBindings/*}Z7\x125/v3beta/{name=folders/*/locations/*/policyBindings/*}Z=\x12;/v3beta/{name=organizations/*/locations/*/policyBindings/*}'
    _globals['_POLICYBINDINGS'].methods_by_name['UpdatePolicyBinding']._loaded_options = None
    _globals['_POLICYBINDINGS'].methods_by_name['UpdatePolicyBinding']._serialized_options = b'\xcaA"\n\rPolicyBinding\x12\x11OperationMetadata\xdaA\x1apolicy_binding,update_mask\x82\xd3\xe4\x93\x02\x8d\x022E/v3beta/{policy_binding.name=projects/*/locations/*/policyBindings/*}:\x0epolicy_bindingZV2D/v3beta/{policy_binding.name=folders/*/locations/*/policyBindings/*}:\x0epolicy_bindingZ\\2J/v3beta/{policy_binding.name=organizations/*/locations/*/policyBindings/*}:\x0epolicy_binding'
    _globals['_POLICYBINDINGS'].methods_by_name['DeletePolicyBinding']._loaded_options = None
    _globals['_POLICYBINDINGS'].methods_by_name['DeletePolicyBinding']._serialized_options = b'\xcaA*\n\x15google.protobuf.Empty\x12\x11OperationMetadata\xdaA\x04name\x82\xd3\xe4\x93\x02\xb0\x01*6/v3beta/{name=projects/*/locations/*/policyBindings/*}Z7*5/v3beta/{name=folders/*/locations/*/policyBindings/*}Z=*;/v3beta/{name=organizations/*/locations/*/policyBindings/*}'
    _globals['_POLICYBINDINGS'].methods_by_name['ListPolicyBindings']._loaded_options = None
    _globals['_POLICYBINDINGS'].methods_by_name['ListPolicyBindings']._serialized_options = b'\xdaA\x06parent\x82\xd3\xe4\x93\x02\xb0\x01\x126/v3beta/{parent=projects/*/locations/*}/policyBindingsZ7\x125/v3beta/{parent=folders/*/locations/*}/policyBindingsZ=\x12;/v3beta/{parent=organizations/*/locations/*}/policyBindings'
    _globals['_POLICYBINDINGS'].methods_by_name['SearchTargetPolicyBindings']._loaded_options = None
    _globals['_POLICYBINDINGS'].methods_by_name['SearchTargetPolicyBindings']._serialized_options = b'\xdaA\rparent,target\x82\xd3\xe4\x93\x02\x81\x02\x12Q/v3beta/{parent=projects/*/locations/*}/policyBindings:searchTargetPolicyBindingsZR\x12P/v3beta/{parent=folders/*/locations/*}/policyBindings:searchTargetPolicyBindingsZX\x12V/v3beta/{parent=organizations/*/locations/*}/policyBindings:searchTargetPolicyBindings'
    _globals['_CREATEPOLICYBINDINGREQUEST']._serialized_start = 380
    _globals['_CREATEPOLICYBINDINGREQUEST']._serialized_end = 589
    _globals['_GETPOLICYBINDINGREQUEST']._serialized_start = 591
    _globals['_GETPOLICYBINDINGREQUEST']._serialized_end = 672
    _globals['_UPDATEPOLICYBINDINGREQUEST']._serialized_start = 675
    _globals['_UPDATEPOLICYBINDINGREQUEST']._serialized_end = 848
    _globals['_DELETEPOLICYBINDINGREQUEST']._serialized_start = 851
    _globals['_DELETEPOLICYBINDINGREQUEST']._serialized_end = 982
    _globals['_LISTPOLICYBINDINGSREQUEST']._serialized_start = 985
    _globals['_LISTPOLICYBINDINGSREQUEST']._serialized_end = 1140
    _globals['_LISTPOLICYBINDINGSRESPONSE']._serialized_start = 1142
    _globals['_LISTPOLICYBINDINGSRESPONSE']._serialized_end = 1259
    _globals['_SEARCHTARGETPOLICYBINDINGSREQUEST']._serialized_start = 1262
    _globals['_SEARCHTARGETPOLICYBINDINGSREQUEST']._serialized_end = 1425
    _globals['_SEARCHTARGETPOLICYBINDINGSRESPONSE']._serialized_start = 1427
    _globals['_SEARCHTARGETPOLICYBINDINGSRESPONSE']._serialized_end = 1552
    _globals['_POLICYBINDINGS']._serialized_start = 1555
    _globals['_POLICYBINDINGS']._serialized_end = 3871