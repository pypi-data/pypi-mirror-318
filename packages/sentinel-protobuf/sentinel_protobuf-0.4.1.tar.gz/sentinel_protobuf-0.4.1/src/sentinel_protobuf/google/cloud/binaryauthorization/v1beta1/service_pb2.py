"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_runtime_version.ValidateProtobufRuntimeVersion(_runtime_version.Domain.PUBLIC, 5, 28, 1, '', 'google/cloud/binaryauthorization/v1beta1/service.proto')
_sym_db = _symbol_database.Default()
from .....google.api import annotations_pb2 as google_dot_api_dot_annotations__pb2
from .....google.api import client_pb2 as google_dot_api_dot_client__pb2
from .....google.api import field_behavior_pb2 as google_dot_api_dot_field__behavior__pb2
from .....google.api import resource_pb2 as google_dot_api_dot_resource__pb2
from .....google.cloud.binaryauthorization.v1beta1 import resources_pb2 as google_dot_cloud_dot_binaryauthorization_dot_v1beta1_dot_resources__pb2
from google.protobuf import empty_pb2 as google_dot_protobuf_dot_empty__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n6google/cloud/binaryauthorization/v1beta1/service.proto\x12(google.cloud.binaryauthorization.v1beta1\x1a\x1cgoogle/api/annotations.proto\x1a\x17google/api/client.proto\x1a\x1fgoogle/api/field_behavior.proto\x1a\x19google/api/resource.proto\x1a8google/cloud/binaryauthorization/v1beta1/resources.proto\x1a\x1bgoogle/protobuf/empty.proto"S\n\x10GetPolicyRequest\x12?\n\x04name\x18\x01 \x01(\tB1\xe0A\x02\xfaA+\n)binaryauthorization.googleapis.com/Policy"\\\n\x13UpdatePolicyRequest\x12E\n\x06policy\x18\x01 \x01(\x0b20.google.cloud.binaryauthorization.v1beta1.PolicyB\x03\xe0A\x02"\xc1\x01\n\x15CreateAttestorRequest\x12C\n\x06parent\x18\x01 \x01(\tB3\xe0A\x02\xfaA-\n+cloudresourcemanager.googleapis.com/Project\x12\x18\n\x0battestor_id\x18\x02 \x01(\tB\x03\xe0A\x02\x12I\n\x08attestor\x18\x03 \x01(\x0b22.google.cloud.binaryauthorization.v1beta1.AttestorB\x03\xe0A\x02"W\n\x12GetAttestorRequest\x12A\n\x04name\x18\x01 \x01(\tB3\xe0A\x02\xfaA-\n+binaryauthorization.googleapis.com/Attestor"b\n\x15UpdateAttestorRequest\x12I\n\x08attestor\x18\x01 \x01(\x0b22.google.cloud.binaryauthorization.v1beta1.AttestorB\x03\xe0A\x02"\x82\x01\n\x14ListAttestorsRequest\x12C\n\x06parent\x18\x01 \x01(\tB3\xe0A\x02\xfaA-\n+cloudresourcemanager.googleapis.com/Project\x12\x11\n\tpage_size\x18\x02 \x01(\x05\x12\x12\n\npage_token\x18\x03 \x01(\t"w\n\x15ListAttestorsResponse\x12E\n\tattestors\x18\x01 \x03(\x0b22.google.cloud.binaryauthorization.v1beta1.Attestor\x12\x17\n\x0fnext_page_token\x18\x02 \x01(\t"Z\n\x15DeleteAttestorRequest\x12A\n\x04name\x18\x01 \x01(\tB3\xe0A\x02\xfaA-\n+binaryauthorization.googleapis.com/Attestor"Y\n\x16GetSystemPolicyRequest\x12?\n\x04name\x18\x01 \x01(\tB1\xe0A\x02\xfaA+\n)binaryauthorization.googleapis.com/Policy2\xcb\x0b\n BinauthzManagementServiceV1Beta1\x12\xab\x01\n\tGetPolicy\x12:.google.cloud.binaryauthorization.v1beta1.GetPolicyRequest\x1a0.google.cloud.binaryauthorization.v1beta1.Policy"0\xdaA\x04name\x82\xd3\xe4\x93\x02#\x12!/v1beta1/{name=projects/*/policy}\x12\xc2\x01\n\x0cUpdatePolicy\x12=.google.cloud.binaryauthorization.v1beta1.UpdatePolicyRequest\x1a0.google.cloud.binaryauthorization.v1beta1.Policy"A\xdaA\x06policy\x82\xd3\xe4\x93\x022\x1a(/v1beta1/{policy.name=projects/*/policy}:\x06policy\x12\xdd\x01\n\x0eCreateAttestor\x12?.google.cloud.binaryauthorization.v1beta1.CreateAttestorRequest\x1a2.google.cloud.binaryauthorization.v1beta1.Attestor"V\xdaA\x1bparent,attestor_id,attestor\x82\xd3\xe4\x93\x022"&/v1beta1/{parent=projects/*}/attestors:\x08attestor\x12\xb6\x01\n\x0bGetAttestor\x12<.google.cloud.binaryauthorization.v1beta1.GetAttestorRequest\x1a2.google.cloud.binaryauthorization.v1beta1.Attestor"5\xdaA\x04name\x82\xd3\xe4\x93\x02(\x12&/v1beta1/{name=projects/*/attestors/*}\x12\xd3\x01\n\x0eUpdateAttestor\x12?.google.cloud.binaryauthorization.v1beta1.UpdateAttestorRequest\x1a2.google.cloud.binaryauthorization.v1beta1.Attestor"L\xdaA\x08attestor\x82\xd3\xe4\x93\x02;\x1a//v1beta1/{attestor.name=projects/*/attestors/*}:\x08attestor\x12\xc9\x01\n\rListAttestors\x12>.google.cloud.binaryauthorization.v1beta1.ListAttestorsRequest\x1a?.google.cloud.binaryauthorization.v1beta1.ListAttestorsResponse"7\xdaA\x06parent\x82\xd3\xe4\x93\x02(\x12&/v1beta1/{parent=projects/*}/attestors\x12\xa0\x01\n\x0eDeleteAttestor\x12?.google.cloud.binaryauthorization.v1beta1.DeleteAttestorRequest\x1a\x16.google.protobuf.Empty"5\xdaA\x04name\x82\xd3\xe4\x93\x02(*&/v1beta1/{name=projects/*/attestors/*}\x1aV\xcaA"binaryauthorization.googleapis.com\xd2A.https://www.googleapis.com/auth/cloud-platform2\xa8\x02\n\x13SystemPolicyV1Beta1\x12\xb8\x01\n\x0fGetSystemPolicy\x12@.google.cloud.binaryauthorization.v1beta1.GetSystemPolicyRequest\x1a0.google.cloud.binaryauthorization.v1beta1.Policy"1\xdaA\x04name\x82\xd3\xe4\x93\x02$\x12"/v1beta1/{name=locations/*/policy}\x1aV\xcaA"binaryauthorization.googleapis.com\xd2A.https://www.googleapis.com/auth/cloud-platformB\xb8\x02\n,com.google.cloud.binaryauthorization.v1beta1B\x1fBinaryAuthorizationServiceProtoP\x01Z^cloud.google.com/go/binaryauthorization/apiv1beta1/binaryauthorizationpb;binaryauthorizationpb\xf8\x01\x01\xaa\x02(Google.Cloud.BinaryAuthorization.V1Beta1\xca\x02(Google\\Cloud\\BinaryAuthorization\\V1beta1\xea\x02+Google::Cloud::BinaryAuthorization::V1beta1b\x06proto3')
_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'google.cloud.binaryauthorization.v1beta1.service_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
    _globals['DESCRIPTOR']._loaded_options = None
    _globals['DESCRIPTOR']._serialized_options = b'\n,com.google.cloud.binaryauthorization.v1beta1B\x1fBinaryAuthorizationServiceProtoP\x01Z^cloud.google.com/go/binaryauthorization/apiv1beta1/binaryauthorizationpb;binaryauthorizationpb\xf8\x01\x01\xaa\x02(Google.Cloud.BinaryAuthorization.V1Beta1\xca\x02(Google\\Cloud\\BinaryAuthorization\\V1beta1\xea\x02+Google::Cloud::BinaryAuthorization::V1beta1'
    _globals['_GETPOLICYREQUEST'].fields_by_name['name']._loaded_options = None
    _globals['_GETPOLICYREQUEST'].fields_by_name['name']._serialized_options = b'\xe0A\x02\xfaA+\n)binaryauthorization.googleapis.com/Policy'
    _globals['_UPDATEPOLICYREQUEST'].fields_by_name['policy']._loaded_options = None
    _globals['_UPDATEPOLICYREQUEST'].fields_by_name['policy']._serialized_options = b'\xe0A\x02'
    _globals['_CREATEATTESTORREQUEST'].fields_by_name['parent']._loaded_options = None
    _globals['_CREATEATTESTORREQUEST'].fields_by_name['parent']._serialized_options = b'\xe0A\x02\xfaA-\n+cloudresourcemanager.googleapis.com/Project'
    _globals['_CREATEATTESTORREQUEST'].fields_by_name['attestor_id']._loaded_options = None
    _globals['_CREATEATTESTORREQUEST'].fields_by_name['attestor_id']._serialized_options = b'\xe0A\x02'
    _globals['_CREATEATTESTORREQUEST'].fields_by_name['attestor']._loaded_options = None
    _globals['_CREATEATTESTORREQUEST'].fields_by_name['attestor']._serialized_options = b'\xe0A\x02'
    _globals['_GETATTESTORREQUEST'].fields_by_name['name']._loaded_options = None
    _globals['_GETATTESTORREQUEST'].fields_by_name['name']._serialized_options = b'\xe0A\x02\xfaA-\n+binaryauthorization.googleapis.com/Attestor'
    _globals['_UPDATEATTESTORREQUEST'].fields_by_name['attestor']._loaded_options = None
    _globals['_UPDATEATTESTORREQUEST'].fields_by_name['attestor']._serialized_options = b'\xe0A\x02'
    _globals['_LISTATTESTORSREQUEST'].fields_by_name['parent']._loaded_options = None
    _globals['_LISTATTESTORSREQUEST'].fields_by_name['parent']._serialized_options = b'\xe0A\x02\xfaA-\n+cloudresourcemanager.googleapis.com/Project'
    _globals['_DELETEATTESTORREQUEST'].fields_by_name['name']._loaded_options = None
    _globals['_DELETEATTESTORREQUEST'].fields_by_name['name']._serialized_options = b'\xe0A\x02\xfaA-\n+binaryauthorization.googleapis.com/Attestor'
    _globals['_GETSYSTEMPOLICYREQUEST'].fields_by_name['name']._loaded_options = None
    _globals['_GETSYSTEMPOLICYREQUEST'].fields_by_name['name']._serialized_options = b'\xe0A\x02\xfaA+\n)binaryauthorization.googleapis.com/Policy'
    _globals['_BINAUTHZMANAGEMENTSERVICEV1BETA1']._loaded_options = None
    _globals['_BINAUTHZMANAGEMENTSERVICEV1BETA1']._serialized_options = b'\xcaA"binaryauthorization.googleapis.com\xd2A.https://www.googleapis.com/auth/cloud-platform'
    _globals['_BINAUTHZMANAGEMENTSERVICEV1BETA1'].methods_by_name['GetPolicy']._loaded_options = None
    _globals['_BINAUTHZMANAGEMENTSERVICEV1BETA1'].methods_by_name['GetPolicy']._serialized_options = b'\xdaA\x04name\x82\xd3\xe4\x93\x02#\x12!/v1beta1/{name=projects/*/policy}'
    _globals['_BINAUTHZMANAGEMENTSERVICEV1BETA1'].methods_by_name['UpdatePolicy']._loaded_options = None
    _globals['_BINAUTHZMANAGEMENTSERVICEV1BETA1'].methods_by_name['UpdatePolicy']._serialized_options = b'\xdaA\x06policy\x82\xd3\xe4\x93\x022\x1a(/v1beta1/{policy.name=projects/*/policy}:\x06policy'
    _globals['_BINAUTHZMANAGEMENTSERVICEV1BETA1'].methods_by_name['CreateAttestor']._loaded_options = None
    _globals['_BINAUTHZMANAGEMENTSERVICEV1BETA1'].methods_by_name['CreateAttestor']._serialized_options = b'\xdaA\x1bparent,attestor_id,attestor\x82\xd3\xe4\x93\x022"&/v1beta1/{parent=projects/*}/attestors:\x08attestor'
    _globals['_BINAUTHZMANAGEMENTSERVICEV1BETA1'].methods_by_name['GetAttestor']._loaded_options = None
    _globals['_BINAUTHZMANAGEMENTSERVICEV1BETA1'].methods_by_name['GetAttestor']._serialized_options = b'\xdaA\x04name\x82\xd3\xe4\x93\x02(\x12&/v1beta1/{name=projects/*/attestors/*}'
    _globals['_BINAUTHZMANAGEMENTSERVICEV1BETA1'].methods_by_name['UpdateAttestor']._loaded_options = None
    _globals['_BINAUTHZMANAGEMENTSERVICEV1BETA1'].methods_by_name['UpdateAttestor']._serialized_options = b'\xdaA\x08attestor\x82\xd3\xe4\x93\x02;\x1a//v1beta1/{attestor.name=projects/*/attestors/*}:\x08attestor'
    _globals['_BINAUTHZMANAGEMENTSERVICEV1BETA1'].methods_by_name['ListAttestors']._loaded_options = None
    _globals['_BINAUTHZMANAGEMENTSERVICEV1BETA1'].methods_by_name['ListAttestors']._serialized_options = b'\xdaA\x06parent\x82\xd3\xe4\x93\x02(\x12&/v1beta1/{parent=projects/*}/attestors'
    _globals['_BINAUTHZMANAGEMENTSERVICEV1BETA1'].methods_by_name['DeleteAttestor']._loaded_options = None
    _globals['_BINAUTHZMANAGEMENTSERVICEV1BETA1'].methods_by_name['DeleteAttestor']._serialized_options = b'\xdaA\x04name\x82\xd3\xe4\x93\x02(*&/v1beta1/{name=projects/*/attestors/*}'
    _globals['_SYSTEMPOLICYV1BETA1']._loaded_options = None
    _globals['_SYSTEMPOLICYV1BETA1']._serialized_options = b'\xcaA"binaryauthorization.googleapis.com\xd2A.https://www.googleapis.com/auth/cloud-platform'
    _globals['_SYSTEMPOLICYV1BETA1'].methods_by_name['GetSystemPolicy']._loaded_options = None
    _globals['_SYSTEMPOLICYV1BETA1'].methods_by_name['GetSystemPolicy']._serialized_options = b'\xdaA\x04name\x82\xd3\xe4\x93\x02$\x12"/v1beta1/{name=locations/*/policy}'
    _globals['_GETPOLICYREQUEST']._serialized_start = 302
    _globals['_GETPOLICYREQUEST']._serialized_end = 385
    _globals['_UPDATEPOLICYREQUEST']._serialized_start = 387
    _globals['_UPDATEPOLICYREQUEST']._serialized_end = 479
    _globals['_CREATEATTESTORREQUEST']._serialized_start = 482
    _globals['_CREATEATTESTORREQUEST']._serialized_end = 675
    _globals['_GETATTESTORREQUEST']._serialized_start = 677
    _globals['_GETATTESTORREQUEST']._serialized_end = 764
    _globals['_UPDATEATTESTORREQUEST']._serialized_start = 766
    _globals['_UPDATEATTESTORREQUEST']._serialized_end = 864
    _globals['_LISTATTESTORSREQUEST']._serialized_start = 867
    _globals['_LISTATTESTORSREQUEST']._serialized_end = 997
    _globals['_LISTATTESTORSRESPONSE']._serialized_start = 999
    _globals['_LISTATTESTORSRESPONSE']._serialized_end = 1118
    _globals['_DELETEATTESTORREQUEST']._serialized_start = 1120
    _globals['_DELETEATTESTORREQUEST']._serialized_end = 1210
    _globals['_GETSYSTEMPOLICYREQUEST']._serialized_start = 1212
    _globals['_GETSYSTEMPOLICYREQUEST']._serialized_end = 1301
    _globals['_BINAUTHZMANAGEMENTSERVICEV1BETA1']._serialized_start = 1304
    _globals['_BINAUTHZMANAGEMENTSERVICEV1BETA1']._serialized_end = 2787
    _globals['_SYSTEMPOLICYV1BETA1']._serialized_start = 2790
    _globals['_SYSTEMPOLICYV1BETA1']._serialized_end = 3086