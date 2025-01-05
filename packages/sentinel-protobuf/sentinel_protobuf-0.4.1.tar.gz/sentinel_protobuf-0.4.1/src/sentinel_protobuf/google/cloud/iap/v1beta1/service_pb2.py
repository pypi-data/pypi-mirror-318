"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_runtime_version.ValidateProtobufRuntimeVersion(_runtime_version.Domain.PUBLIC, 5, 28, 1, '', 'google/cloud/iap/v1beta1/service.proto')
_sym_db = _symbol_database.Default()
from .....google.api import annotations_pb2 as google_dot_api_dot_annotations__pb2
from .....google.api import client_pb2 as google_dot_api_dot_client__pb2
from .....google.iam.v1 import iam_policy_pb2 as google_dot_iam_dot_v1_dot_iam__policy__pb2
from .....google.iam.v1 import policy_pb2 as google_dot_iam_dot_v1_dot_policy__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n&google/cloud/iap/v1beta1/service.proto\x12\x18google.cloud.iap.v1beta1\x1a\x1cgoogle/api/annotations.proto\x1a\x17google/api/client.proto\x1a\x1egoogle/iam/v1/iam_policy.proto\x1a\x1agoogle/iam/v1/policy.proto2\x80\x04\n\x1eIdentityAwareProxyAdminV1Beta1\x12y\n\x0cSetIamPolicy\x12".google.iam.v1.SetIamPolicyRequest\x1a\x15.google.iam.v1.Policy".\x82\xd3\xe4\x93\x02("#/v1beta1/{resource=**}:setIamPolicy:\x01*\x12y\n\x0cGetIamPolicy\x12".google.iam.v1.GetIamPolicyRequest\x1a\x15.google.iam.v1.Policy".\x82\xd3\xe4\x93\x02("#/v1beta1/{resource=**}:getIamPolicy:\x01*\x12\x9f\x01\n\x12TestIamPermissions\x12(.google.iam.v1.TestIamPermissionsRequest\x1a).google.iam.v1.TestIamPermissionsResponse"4\x82\xd3\xe4\x93\x02.")/v1beta1/{resource=**}:testIamPermissions:\x01*\x1aF\xcaA\x12iap.googleapis.com\xd2A.https://www.googleapis.com/auth/cloud-platformBP\n\x1ccom.google.cloud.iap.v1beta1P\x01Z.cloud.google.com/go/iap/apiv1beta1/iappb;iappbb\x06proto3')
_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'google.cloud.iap.v1beta1.service_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
    _globals['DESCRIPTOR']._loaded_options = None
    _globals['DESCRIPTOR']._serialized_options = b'\n\x1ccom.google.cloud.iap.v1beta1P\x01Z.cloud.google.com/go/iap/apiv1beta1/iappb;iappb'
    _globals['_IDENTITYAWAREPROXYADMINV1BETA1']._loaded_options = None
    _globals['_IDENTITYAWAREPROXYADMINV1BETA1']._serialized_options = b'\xcaA\x12iap.googleapis.com\xd2A.https://www.googleapis.com/auth/cloud-platform'
    _globals['_IDENTITYAWAREPROXYADMINV1BETA1'].methods_by_name['SetIamPolicy']._loaded_options = None
    _globals['_IDENTITYAWAREPROXYADMINV1BETA1'].methods_by_name['SetIamPolicy']._serialized_options = b'\x82\xd3\xe4\x93\x02("#/v1beta1/{resource=**}:setIamPolicy:\x01*'
    _globals['_IDENTITYAWAREPROXYADMINV1BETA1'].methods_by_name['GetIamPolicy']._loaded_options = None
    _globals['_IDENTITYAWAREPROXYADMINV1BETA1'].methods_by_name['GetIamPolicy']._serialized_options = b'\x82\xd3\xe4\x93\x02("#/v1beta1/{resource=**}:getIamPolicy:\x01*'
    _globals['_IDENTITYAWAREPROXYADMINV1BETA1'].methods_by_name['TestIamPermissions']._loaded_options = None
    _globals['_IDENTITYAWAREPROXYADMINV1BETA1'].methods_by_name['TestIamPermissions']._serialized_options = b'\x82\xd3\xe4\x93\x02.")/v1beta1/{resource=**}:testIamPermissions:\x01*'
    _globals['_IDENTITYAWAREPROXYADMINV1BETA1']._serialized_start = 184
    _globals['_IDENTITYAWAREPROXYADMINV1BETA1']._serialized_end = 696