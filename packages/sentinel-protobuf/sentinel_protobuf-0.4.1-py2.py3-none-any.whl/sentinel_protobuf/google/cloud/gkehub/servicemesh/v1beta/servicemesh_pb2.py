"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_runtime_version.ValidateProtobufRuntimeVersion(_runtime_version.Domain.PUBLIC, 5, 28, 1, '', 'google/cloud/gkehub/servicemesh/v1beta/servicemesh.proto')
_sym_db = _symbol_database.Default()
from ......google.api import field_behavior_pb2 as google_dot_api_dot_field__behavior__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n8google/cloud/gkehub/servicemesh/v1beta/servicemesh.proto\x12&google.cloud.gkehub.servicemesh.v1beta\x1a\x1fgoogle/api/field_behavior.proto"\x8b\x03\n\x0eMembershipSpec\x12h\n\rcontrol_plane\x18\x01 \x01(\x0e2M.google.cloud.gkehub.servicemesh.v1beta.MembershipSpec.ControlPlaneManagementB\x02\x18\x01\x12U\n\nmanagement\x18\x04 \x01(\x0e2A.google.cloud.gkehub.servicemesh.v1beta.MembershipSpec.Management"]\n\x16ControlPlaneManagement\x12(\n$CONTROL_PLANE_MANAGEMENT_UNSPECIFIED\x10\x00\x12\r\n\tAUTOMATIC\x10\x01\x12\n\n\x06MANUAL\x10\x02"Y\n\nManagement\x12\x1a\n\x16MANAGEMENT_UNSPECIFIED\x10\x00\x12\x18\n\x14MANAGEMENT_AUTOMATIC\x10\x01\x12\x15\n\x11MANAGEMENT_MANUAL\x10\x02"\xac\x12\n\x0fMembershipState\x12u\n\x18control_plane_management\x18\x02 \x01(\x0b2N.google.cloud.gkehub.servicemesh.v1beta.MembershipState.ControlPlaneManagementB\x03\xe0A\x03\x12o\n\x15data_plane_management\x18\x04 \x01(\x0b2K.google.cloud.gkehub.servicemesh.v1beta.MembershipState.DataPlaneManagementB\x03\xe0A\x03\x12Z\n\nconditions\x18\x08 \x03(\x0b2A.google.cloud.gkehub.servicemesh.v1beta.MembershipState.ConditionB\x03\xe0A\x03\x1a\x95\x03\n\x16ControlPlaneManagement\x12F\n\x07details\x18\x02 \x03(\x0b25.google.cloud.gkehub.servicemesh.v1beta.StatusDetails\x12U\n\x05state\x18\x03 \x01(\x0e2F.google.cloud.gkehub.servicemesh.v1beta.MembershipState.LifecycleState\x12z\n\x0eimplementation\x18\x04 \x01(\x0e2].google.cloud.gkehub.servicemesh.v1beta.MembershipState.ControlPlaneManagement.ImplementationB\x03\xe0A\x03"`\n\x0eImplementation\x12\x1e\n\x1aIMPLEMENTATION_UNSPECIFIED\x10\x00\x12\n\n\x06ISTIOD\x10\x01\x12\x14\n\x10TRAFFIC_DIRECTOR\x10\x02\x12\x0c\n\x08UPDATING\x10\x03\x1a\xb4\x01\n\x13DataPlaneManagement\x12U\n\x05state\x18\x01 \x01(\x0e2F.google.cloud.gkehub.servicemesh.v1beta.MembershipState.LifecycleState\x12F\n\x07details\x18\x02 \x03(\x0b25.google.cloud.gkehub.servicemesh.v1beta.StatusDetails\x1a\xdc\t\n\tCondition\x12T\n\x04code\x18\x01 \x01(\x0e2F.google.cloud.gkehub.servicemesh.v1beta.MembershipState.Condition.Code\x12\x1a\n\x12documentation_link\x18\x02 \x01(\t\x12\x0f\n\x07details\x18\x03 \x01(\t\x12\\\n\x08severity\x18\x04 \x01(\x0e2J.google.cloud.gkehub.servicemesh.v1beta.MembershipState.Condition.Severity"\xa5\x07\n\x04Code\x12\x14\n\x10CODE_UNSPECIFIED\x10\x00\x12\x1e\n\x1aMESH_IAM_PERMISSION_DENIED\x10d\x12\x1b\n\x16CNI_CONFIG_UNSUPPORTED\x10\xc9\x01\x12\x1c\n\x17GKE_SANDBOX_UNSUPPORTED\x10\xca\x01\x123\n.NODEPOOL_WORKLOAD_IDENTITY_FEDERATION_REQUIRED\x10\xcb\x01\x12\x1c\n\x17CNI_INSTALLATION_FAILED\x10\xcc\x01\x12\x1a\n\x15CNI_POD_UNSCHEDULABLE\x10\xcd\x01\x12(\n#UNSUPPORTED_MULTIPLE_CONTROL_PLANES\x10\xad\x02\x12\x17\n\x12VPCSC_GA_SUPPORTED\x10\xae\x02\x12 \n\x1bCONFIG_APPLY_INTERNAL_ERROR\x10\x91\x03\x12\x1c\n\x17CONFIG_VALIDATION_ERROR\x10\x92\x03\x12\x1e\n\x19CONFIG_VALIDATION_WARNING\x10\x93\x03\x12$\n\x1fQUOTA_EXCEEDED_BACKEND_SERVICES\x10\x94\x03\x12!\n\x1cQUOTA_EXCEEDED_HEALTH_CHECKS\x10\x95\x03\x12\x1f\n\x1aQUOTA_EXCEEDED_HTTP_ROUTES\x10\x96\x03\x12\x1e\n\x19QUOTA_EXCEEDED_TCP_ROUTES\x10\x97\x03\x12\x1e\n\x19QUOTA_EXCEEDED_TLS_ROUTES\x10\x98\x03\x12$\n\x1fQUOTA_EXCEEDED_TRAFFIC_POLICIES\x10\x99\x03\x12%\n QUOTA_EXCEEDED_ENDPOINT_POLICIES\x10\x9a\x03\x12\x1c\n\x17QUOTA_EXCEEDED_GATEWAYS\x10\x9b\x03\x12\x1a\n\x15QUOTA_EXCEEDED_MESHES\x10\x9c\x03\x12\'\n"QUOTA_EXCEEDED_SERVER_TLS_POLICIES\x10\x9d\x03\x12\'\n"QUOTA_EXCEEDED_CLIENT_TLS_POLICIES\x10\x9e\x03\x12\'\n"QUOTA_EXCEEDED_SERVICE_LB_POLICIES\x10\x9f\x03\x12 \n\x1bQUOTA_EXCEEDED_HTTP_FILTERS\x10\xa0\x03\x12\x1f\n\x1aQUOTA_EXCEEDED_TCP_FILTERS\x10\xa1\x03\x12+\n&QUOTA_EXCEEDED_NETWORK_ENDPOINT_GROUPS\x10\xa2\x03"F\n\x08Severity\x12\x18\n\x14SEVERITY_UNSPECIFIED\x10\x00\x12\t\n\x05ERROR\x10\x01\x12\x0b\n\x07WARNING\x10\x02\x12\x08\n\x04INFO\x10\x03"\xa6\x01\n\x0eLifecycleState\x12\x1f\n\x1bLIFECYCLE_STATE_UNSPECIFIED\x10\x00\x12\x0c\n\x08DISABLED\x10\x01\x12\x17\n\x13FAILED_PRECONDITION\x10\x02\x12\x10\n\x0cPROVISIONING\x10\x03\x12\n\n\x06ACTIVE\x10\x04\x12\x0b\n\x07STALLED\x10\x05\x12\x13\n\x0fNEEDS_ATTENTION\x10\x06\x12\x0c\n\x08DEGRADED\x10\x07".\n\rStatusDetails\x12\x0c\n\x04code\x18\x01 \x01(\t\x12\x0f\n\x07details\x18\x02 \x01(\tB\x8d\x02\n*com.google.cloud.gkehub.servicemesh.v1betaB\x10ServiceMeshProtoP\x01ZLcloud.google.com/go/gkehub/servicemesh/apiv1beta/servicemeshpb;servicemeshpb\xaa\x02&Google.Cloud.GkeHub.ServiceMesh.V1Beta\xca\x02&Google\\Cloud\\GkeHub\\ServiceMesh\\V1beta\xea\x02*Google::Cloud::GkeHub::ServiceMesh::V1betab\x06proto3')
_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'google.cloud.gkehub.servicemesh.v1beta.servicemesh_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
    _globals['DESCRIPTOR']._loaded_options = None
    _globals['DESCRIPTOR']._serialized_options = b'\n*com.google.cloud.gkehub.servicemesh.v1betaB\x10ServiceMeshProtoP\x01ZLcloud.google.com/go/gkehub/servicemesh/apiv1beta/servicemeshpb;servicemeshpb\xaa\x02&Google.Cloud.GkeHub.ServiceMesh.V1Beta\xca\x02&Google\\Cloud\\GkeHub\\ServiceMesh\\V1beta\xea\x02*Google::Cloud::GkeHub::ServiceMesh::V1beta'
    _globals['_MEMBERSHIPSPEC'].fields_by_name['control_plane']._loaded_options = None
    _globals['_MEMBERSHIPSPEC'].fields_by_name['control_plane']._serialized_options = b'\x18\x01'
    _globals['_MEMBERSHIPSTATE_CONTROLPLANEMANAGEMENT'].fields_by_name['implementation']._loaded_options = None
    _globals['_MEMBERSHIPSTATE_CONTROLPLANEMANAGEMENT'].fields_by_name['implementation']._serialized_options = b'\xe0A\x03'
    _globals['_MEMBERSHIPSTATE'].fields_by_name['control_plane_management']._loaded_options = None
    _globals['_MEMBERSHIPSTATE'].fields_by_name['control_plane_management']._serialized_options = b'\xe0A\x03'
    _globals['_MEMBERSHIPSTATE'].fields_by_name['data_plane_management']._loaded_options = None
    _globals['_MEMBERSHIPSTATE'].fields_by_name['data_plane_management']._serialized_options = b'\xe0A\x03'
    _globals['_MEMBERSHIPSTATE'].fields_by_name['conditions']._loaded_options = None
    _globals['_MEMBERSHIPSTATE'].fields_by_name['conditions']._serialized_options = b'\xe0A\x03'
    _globals['_MEMBERSHIPSPEC']._serialized_start = 134
    _globals['_MEMBERSHIPSPEC']._serialized_end = 529
    _globals['_MEMBERSHIPSPEC_CONTROLPLANEMANAGEMENT']._serialized_start = 345
    _globals['_MEMBERSHIPSPEC_CONTROLPLANEMANAGEMENT']._serialized_end = 438
    _globals['_MEMBERSHIPSPEC_MANAGEMENT']._serialized_start = 440
    _globals['_MEMBERSHIPSPEC_MANAGEMENT']._serialized_end = 529
    _globals['_MEMBERSHIPSTATE']._serialized_start = 532
    _globals['_MEMBERSHIPSTATE']._serialized_end = 2880
    _globals['_MEMBERSHIPSTATE_CONTROLPLANEMANAGEMENT']._serialized_start = 876
    _globals['_MEMBERSHIPSTATE_CONTROLPLANEMANAGEMENT']._serialized_end = 1281
    _globals['_MEMBERSHIPSTATE_CONTROLPLANEMANAGEMENT_IMPLEMENTATION']._serialized_start = 1185
    _globals['_MEMBERSHIPSTATE_CONTROLPLANEMANAGEMENT_IMPLEMENTATION']._serialized_end = 1281
    _globals['_MEMBERSHIPSTATE_DATAPLANEMANAGEMENT']._serialized_start = 1284
    _globals['_MEMBERSHIPSTATE_DATAPLANEMANAGEMENT']._serialized_end = 1464
    _globals['_MEMBERSHIPSTATE_CONDITION']._serialized_start = 1467
    _globals['_MEMBERSHIPSTATE_CONDITION']._serialized_end = 2711
    _globals['_MEMBERSHIPSTATE_CONDITION_CODE']._serialized_start = 1706
    _globals['_MEMBERSHIPSTATE_CONDITION_CODE']._serialized_end = 2639
    _globals['_MEMBERSHIPSTATE_CONDITION_SEVERITY']._serialized_start = 2641
    _globals['_MEMBERSHIPSTATE_CONDITION_SEVERITY']._serialized_end = 2711
    _globals['_MEMBERSHIPSTATE_LIFECYCLESTATE']._serialized_start = 2714
    _globals['_MEMBERSHIPSTATE_LIFECYCLESTATE']._serialized_end = 2880
    _globals['_STATUSDETAILS']._serialized_start = 2882
    _globals['_STATUSDETAILS']._serialized_end = 2928