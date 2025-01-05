"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_runtime_version.ValidateProtobufRuntimeVersion(_runtime_version.Domain.PUBLIC, 5, 28, 1, '', 'google/cloud/policytroubleshooter/v1/checker.proto')
_sym_db = _symbol_database.Default()
from .....google.cloud.policytroubleshooter.v1 import explanations_pb2 as google_dot_cloud_dot_policytroubleshooter_dot_v1_dot_explanations__pb2
from .....google.api import annotations_pb2 as google_dot_api_dot_annotations__pb2
from .....google.api import client_pb2 as google_dot_api_dot_client__pb2
from .....google.rpc import status_pb2 as google_dot_rpc_dot_status__pb2
from ....google.cloud.policytroubleshooter.v1.explanations_pb2 import *
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n2google/cloud/policytroubleshooter/v1/checker.proto\x12$google.cloud.policytroubleshooter.v1\x1a7google/cloud/policytroubleshooter/v1/explanations.proto\x1a\x1cgoogle/api/annotations.proto\x1a\x17google/api/client.proto\x1a\x17google/rpc/status.proto"g\n\x1cTroubleshootIamPolicyRequest\x12G\n\x0caccess_tuple\x18\x01 \x01(\x0b21.google.cloud.policytroubleshooter.v1.AccessTuple"\xd9\x01\n\x1dTroubleshootIamPolicyResponse\x12A\n\x06access\x18\x01 \x01(\x0e21.google.cloud.policytroubleshooter.v1.AccessState\x12Q\n\x12explained_policies\x18\x02 \x03(\x0b25.google.cloud.policytroubleshooter.v1.ExplainedPolicy\x12"\n\x06errors\x18\x03 \x03(\x0b2\x12.google.rpc.Status2\xa9\x02\n\nIamChecker\x12\xc1\x01\n\x15TroubleshootIamPolicy\x12B.google.cloud.policytroubleshooter.v1.TroubleshootIamPolicyRequest\x1aC.google.cloud.policytroubleshooter.v1.TroubleshootIamPolicyResponse"\x1f\x82\xd3\xe4\x93\x02\x19"\x14/v1/iam:troubleshoot:\x01*\x1aW\xcaA#policytroubleshooter.googleapis.com\xd2A.https://www.googleapis.com/auth/cloud-platformB\x96\x02\n(com.google.cloud.policytroubleshooter.v1B\x0fIAMCheckerProtoP\x01Z\\cloud.google.com/go/policytroubleshooter/apiv1/policytroubleshooterpb;policytroubleshooterpb\xf8\x01\x01\xaa\x02$Google.Cloud.PolicyTroubleshooter.V1\xca\x02$Google\\Cloud\\PolicyTroubleshooter\\V1\xea\x02\'Google::Cloud::PolicyTroubleshooter::V1P\x00b\x06proto3')
_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'google.cloud.policytroubleshooter.v1.checker_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
    _globals['DESCRIPTOR']._loaded_options = None
    _globals['DESCRIPTOR']._serialized_options = b"\n(com.google.cloud.policytroubleshooter.v1B\x0fIAMCheckerProtoP\x01Z\\cloud.google.com/go/policytroubleshooter/apiv1/policytroubleshooterpb;policytroubleshooterpb\xf8\x01\x01\xaa\x02$Google.Cloud.PolicyTroubleshooter.V1\xca\x02$Google\\Cloud\\PolicyTroubleshooter\\V1\xea\x02'Google::Cloud::PolicyTroubleshooter::V1"
    _globals['_IAMCHECKER']._loaded_options = None
    _globals['_IAMCHECKER']._serialized_options = b'\xcaA#policytroubleshooter.googleapis.com\xd2A.https://www.googleapis.com/auth/cloud-platform'
    _globals['_IAMCHECKER'].methods_by_name['TroubleshootIamPolicy']._loaded_options = None
    _globals['_IAMCHECKER'].methods_by_name['TroubleshootIamPolicy']._serialized_options = b'\x82\xd3\xe4\x93\x02\x19"\x14/v1/iam:troubleshoot:\x01*'
    _globals['_TROUBLESHOOTIAMPOLICYREQUEST']._serialized_start = 229
    _globals['_TROUBLESHOOTIAMPOLICYREQUEST']._serialized_end = 332
    _globals['_TROUBLESHOOTIAMPOLICYRESPONSE']._serialized_start = 335
    _globals['_TROUBLESHOOTIAMPOLICYRESPONSE']._serialized_end = 552
    _globals['_IAMCHECKER']._serialized_start = 555
    _globals['_IAMCHECKER']._serialized_end = 852