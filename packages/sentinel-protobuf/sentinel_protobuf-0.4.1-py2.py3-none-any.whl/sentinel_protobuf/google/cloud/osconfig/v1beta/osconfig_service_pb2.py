"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_runtime_version.ValidateProtobufRuntimeVersion(_runtime_version.Domain.PUBLIC, 5, 28, 1, '', 'google/cloud/osconfig/v1beta/osconfig_service.proto')
_sym_db = _symbol_database.Default()
from .....google.api import annotations_pb2 as google_dot_api_dot_annotations__pb2
from .....google.api import client_pb2 as google_dot_api_dot_client__pb2
from .....google.cloud.osconfig.v1beta import guest_policies_pb2 as google_dot_cloud_dot_osconfig_dot_v1beta_dot_guest__policies__pb2
from .....google.cloud.osconfig.v1beta import patch_deployments_pb2 as google_dot_cloud_dot_osconfig_dot_v1beta_dot_patch__deployments__pb2
from .....google.cloud.osconfig.v1beta import patch_jobs_pb2 as google_dot_cloud_dot_osconfig_dot_v1beta_dot_patch__jobs__pb2
from google.protobuf import empty_pb2 as google_dot_protobuf_dot_empty__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n3google/cloud/osconfig/v1beta/osconfig_service.proto\x12\x1cgoogle.cloud.osconfig.v1beta\x1a\x1cgoogle/api/annotations.proto\x1a\x17google/api/client.proto\x1a1google/cloud/osconfig/v1beta/guest_policies.proto\x1a4google/cloud/osconfig/v1beta/patch_deployments.proto\x1a-google/cloud/osconfig/v1beta/patch_jobs.proto\x1a\x1bgoogle/protobuf/empty.proto2\x93\x1c\n\x0fOsConfigService\x12\xa9\x01\n\x0fExecutePatchJob\x124.google.cloud.osconfig.v1beta.ExecutePatchJobRequest\x1a&.google.cloud.osconfig.v1beta.PatchJob"8\x82\xd3\xe4\x93\x022"-/v1beta/{parent=projects/*}/patchJobs:execute:\x01*\x12\x96\x01\n\x0bGetPatchJob\x120.google.cloud.osconfig.v1beta.GetPatchJobRequest\x1a&.google.cloud.osconfig.v1beta.PatchJob"-\x82\xd3\xe4\x93\x02\'\x12%/v1beta/{name=projects/*/patchJobs/*}\x12\xa6\x01\n\x0eCancelPatchJob\x123.google.cloud.osconfig.v1beta.CancelPatchJobRequest\x1a&.google.cloud.osconfig.v1beta.PatchJob"7\x82\xd3\xe4\x93\x021",/v1beta/{name=projects/*/patchJobs/*}:cancel:\x01*\x12\xa7\x01\n\rListPatchJobs\x122.google.cloud.osconfig.v1beta.ListPatchJobsRequest\x1a3.google.cloud.osconfig.v1beta.ListPatchJobsResponse"-\x82\xd3\xe4\x93\x02\'\x12%/v1beta/{parent=projects/*}/patchJobs\x12\xec\x01\n\x1bListPatchJobInstanceDetails\x12@.google.cloud.osconfig.v1beta.ListPatchJobInstanceDetailsRequest\x1aA.google.cloud.osconfig.v1beta.ListPatchJobInstanceDetailsResponse"H\xdaA\x06parent\x82\xd3\xe4\x93\x029\x127/v1beta/{parent=projects/*/patchJobs/*}/instanceDetails\x12\xca\x01\n\x15CreatePatchDeployment\x12:.google.cloud.osconfig.v1beta.CreatePatchDeploymentRequest\x1a-.google.cloud.osconfig.v1beta.PatchDeployment"F\x82\xd3\xe4\x93\x02@",/v1beta/{parent=projects/*}/patchDeployments:\x10patch_deployment\x12\xb2\x01\n\x12GetPatchDeployment\x127.google.cloud.osconfig.v1beta.GetPatchDeploymentRequest\x1a-.google.cloud.osconfig.v1beta.PatchDeployment"4\x82\xd3\xe4\x93\x02.\x12,/v1beta/{name=projects/*/patchDeployments/*}\x12\xc3\x01\n\x14ListPatchDeployments\x129.google.cloud.osconfig.v1beta.ListPatchDeploymentsRequest\x1a:.google.cloud.osconfig.v1beta.ListPatchDeploymentsResponse"4\x82\xd3\xe4\x93\x02.\x12,/v1beta/{parent=projects/*}/patchDeployments\x12\xa1\x01\n\x15DeletePatchDeployment\x12:.google.cloud.osconfig.v1beta.DeletePatchDeploymentRequest\x1a\x16.google.protobuf.Empty"4\x82\xd3\xe4\x93\x02.*,/v1beta/{name=projects/*/patchDeployments/*}\x12\xfa\x01\n\x15UpdatePatchDeployment\x12:.google.cloud.osconfig.v1beta.UpdatePatchDeploymentRequest\x1a-.google.cloud.osconfig.v1beta.PatchDeployment"v\xdaA\x1cpatch_deployment,update_mask\x82\xd3\xe4\x93\x02Q2=/v1beta/{patch_deployment.name=projects/*/patchDeployments/*}:\x10patch_deployment\x12\xc6\x01\n\x14PausePatchDeployment\x129.google.cloud.osconfig.v1beta.PausePatchDeploymentRequest\x1a-.google.cloud.osconfig.v1beta.PatchDeployment"D\xdaA\x04name\x82\xd3\xe4\x93\x027"2/v1beta/{name=projects/*/patchDeployments/*}:pause:\x01*\x12\xc9\x01\n\x15ResumePatchDeployment\x12:.google.cloud.osconfig.v1beta.ResumePatchDeploymentRequest\x1a-.google.cloud.osconfig.v1beta.PatchDeployment"E\xdaA\x04name\x82\xd3\xe4\x93\x028"3/v1beta/{name=projects/*/patchDeployments/*}:resume:\x01*\x12\xce\x01\n\x11CreateGuestPolicy\x126.google.cloud.osconfig.v1beta.CreateGuestPolicyRequest\x1a).google.cloud.osconfig.v1beta.GuestPolicy"V\xdaA\x14parent, guest_policy\x82\xd3\xe4\x93\x029")/v1beta/{parent=projects/*}/guestPolicies:\x0cguest_policy\x12\xaa\x01\n\x0eGetGuestPolicy\x123.google.cloud.osconfig.v1beta.GetGuestPolicyRequest\x1a).google.cloud.osconfig.v1beta.GuestPolicy"8\xdaA\x04name\x82\xd3\xe4\x93\x02+\x12)/v1beta/{name=projects/*/guestPolicies/*}\x12\xc0\x01\n\x11ListGuestPolicies\x126.google.cloud.osconfig.v1beta.ListGuestPoliciesRequest\x1a7.google.cloud.osconfig.v1beta.ListGuestPoliciesResponse":\xdaA\x06parent\x82\xd3\xe4\x93\x02+\x12)/v1beta/{parent=projects/*}/guestPolicies\x12\xdf\x01\n\x11UpdateGuestPolicy\x126.google.cloud.osconfig.v1beta.UpdateGuestPolicyRequest\x1a).google.cloud.osconfig.v1beta.GuestPolicy"g\xdaA\x18guest_policy,update_mask\x82\xd3\xe4\x93\x02F26/v1beta/{guest_policy.name=projects/*/guestPolicies/*}:\x0cguest_policy\x12\x9d\x01\n\x11DeleteGuestPolicy\x126.google.cloud.osconfig.v1beta.DeleteGuestPolicyRequest\x1a\x16.google.protobuf.Empty"8\xdaA\x04name\x82\xd3\xe4\x93\x02+*)/v1beta/{name=projects/*/guestPolicies/*}\x12\xea\x01\n\x1aLookupEffectiveGuestPolicy\x12?.google.cloud.osconfig.v1beta.LookupEffectiveGuestPolicyRequest\x1a2.google.cloud.osconfig.v1beta.EffectiveGuestPolicy"W\x82\xd3\xe4\x93\x02Q"L/v1beta/{instance=projects/*/zones/*/instances/*}:lookupEffectiveGuestPolicy:\x01*\x1aK\xcaA\x17osconfig.googleapis.com\xd2A.https://www.googleapis.com/auth/cloud-platformBo\n com.google.cloud.osconfig.v1betaB\rOsConfigProtoZ<cloud.google.com/go/osconfig/apiv1beta/osconfigpb;osconfigpbb\x06proto3')
_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'google.cloud.osconfig.v1beta.osconfig_service_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
    _globals['DESCRIPTOR']._loaded_options = None
    _globals['DESCRIPTOR']._serialized_options = b'\n com.google.cloud.osconfig.v1betaB\rOsConfigProtoZ<cloud.google.com/go/osconfig/apiv1beta/osconfigpb;osconfigpb'
    _globals['_OSCONFIGSERVICE']._loaded_options = None
    _globals['_OSCONFIGSERVICE']._serialized_options = b'\xcaA\x17osconfig.googleapis.com\xd2A.https://www.googleapis.com/auth/cloud-platform'
    _globals['_OSCONFIGSERVICE'].methods_by_name['ExecutePatchJob']._loaded_options = None
    _globals['_OSCONFIGSERVICE'].methods_by_name['ExecutePatchJob']._serialized_options = b'\x82\xd3\xe4\x93\x022"-/v1beta/{parent=projects/*}/patchJobs:execute:\x01*'
    _globals['_OSCONFIGSERVICE'].methods_by_name['GetPatchJob']._loaded_options = None
    _globals['_OSCONFIGSERVICE'].methods_by_name['GetPatchJob']._serialized_options = b"\x82\xd3\xe4\x93\x02'\x12%/v1beta/{name=projects/*/patchJobs/*}"
    _globals['_OSCONFIGSERVICE'].methods_by_name['CancelPatchJob']._loaded_options = None
    _globals['_OSCONFIGSERVICE'].methods_by_name['CancelPatchJob']._serialized_options = b'\x82\xd3\xe4\x93\x021",/v1beta/{name=projects/*/patchJobs/*}:cancel:\x01*'
    _globals['_OSCONFIGSERVICE'].methods_by_name['ListPatchJobs']._loaded_options = None
    _globals['_OSCONFIGSERVICE'].methods_by_name['ListPatchJobs']._serialized_options = b"\x82\xd3\xe4\x93\x02'\x12%/v1beta/{parent=projects/*}/patchJobs"
    _globals['_OSCONFIGSERVICE'].methods_by_name['ListPatchJobInstanceDetails']._loaded_options = None
    _globals['_OSCONFIGSERVICE'].methods_by_name['ListPatchJobInstanceDetails']._serialized_options = b'\xdaA\x06parent\x82\xd3\xe4\x93\x029\x127/v1beta/{parent=projects/*/patchJobs/*}/instanceDetails'
    _globals['_OSCONFIGSERVICE'].methods_by_name['CreatePatchDeployment']._loaded_options = None
    _globals['_OSCONFIGSERVICE'].methods_by_name['CreatePatchDeployment']._serialized_options = b'\x82\xd3\xe4\x93\x02@",/v1beta/{parent=projects/*}/patchDeployments:\x10patch_deployment'
    _globals['_OSCONFIGSERVICE'].methods_by_name['GetPatchDeployment']._loaded_options = None
    _globals['_OSCONFIGSERVICE'].methods_by_name['GetPatchDeployment']._serialized_options = b'\x82\xd3\xe4\x93\x02.\x12,/v1beta/{name=projects/*/patchDeployments/*}'
    _globals['_OSCONFIGSERVICE'].methods_by_name['ListPatchDeployments']._loaded_options = None
    _globals['_OSCONFIGSERVICE'].methods_by_name['ListPatchDeployments']._serialized_options = b'\x82\xd3\xe4\x93\x02.\x12,/v1beta/{parent=projects/*}/patchDeployments'
    _globals['_OSCONFIGSERVICE'].methods_by_name['DeletePatchDeployment']._loaded_options = None
    _globals['_OSCONFIGSERVICE'].methods_by_name['DeletePatchDeployment']._serialized_options = b'\x82\xd3\xe4\x93\x02.*,/v1beta/{name=projects/*/patchDeployments/*}'
    _globals['_OSCONFIGSERVICE'].methods_by_name['UpdatePatchDeployment']._loaded_options = None
    _globals['_OSCONFIGSERVICE'].methods_by_name['UpdatePatchDeployment']._serialized_options = b'\xdaA\x1cpatch_deployment,update_mask\x82\xd3\xe4\x93\x02Q2=/v1beta/{patch_deployment.name=projects/*/patchDeployments/*}:\x10patch_deployment'
    _globals['_OSCONFIGSERVICE'].methods_by_name['PausePatchDeployment']._loaded_options = None
    _globals['_OSCONFIGSERVICE'].methods_by_name['PausePatchDeployment']._serialized_options = b'\xdaA\x04name\x82\xd3\xe4\x93\x027"2/v1beta/{name=projects/*/patchDeployments/*}:pause:\x01*'
    _globals['_OSCONFIGSERVICE'].methods_by_name['ResumePatchDeployment']._loaded_options = None
    _globals['_OSCONFIGSERVICE'].methods_by_name['ResumePatchDeployment']._serialized_options = b'\xdaA\x04name\x82\xd3\xe4\x93\x028"3/v1beta/{name=projects/*/patchDeployments/*}:resume:\x01*'
    _globals['_OSCONFIGSERVICE'].methods_by_name['CreateGuestPolicy']._loaded_options = None
    _globals['_OSCONFIGSERVICE'].methods_by_name['CreateGuestPolicy']._serialized_options = b'\xdaA\x14parent, guest_policy\x82\xd3\xe4\x93\x029")/v1beta/{parent=projects/*}/guestPolicies:\x0cguest_policy'
    _globals['_OSCONFIGSERVICE'].methods_by_name['GetGuestPolicy']._loaded_options = None
    _globals['_OSCONFIGSERVICE'].methods_by_name['GetGuestPolicy']._serialized_options = b'\xdaA\x04name\x82\xd3\xe4\x93\x02+\x12)/v1beta/{name=projects/*/guestPolicies/*}'
    _globals['_OSCONFIGSERVICE'].methods_by_name['ListGuestPolicies']._loaded_options = None
    _globals['_OSCONFIGSERVICE'].methods_by_name['ListGuestPolicies']._serialized_options = b'\xdaA\x06parent\x82\xd3\xe4\x93\x02+\x12)/v1beta/{parent=projects/*}/guestPolicies'
    _globals['_OSCONFIGSERVICE'].methods_by_name['UpdateGuestPolicy']._loaded_options = None
    _globals['_OSCONFIGSERVICE'].methods_by_name['UpdateGuestPolicy']._serialized_options = b'\xdaA\x18guest_policy,update_mask\x82\xd3\xe4\x93\x02F26/v1beta/{guest_policy.name=projects/*/guestPolicies/*}:\x0cguest_policy'
    _globals['_OSCONFIGSERVICE'].methods_by_name['DeleteGuestPolicy']._loaded_options = None
    _globals['_OSCONFIGSERVICE'].methods_by_name['DeleteGuestPolicy']._serialized_options = b'\xdaA\x04name\x82\xd3\xe4\x93\x02+*)/v1beta/{name=projects/*/guestPolicies/*}'
    _globals['_OSCONFIGSERVICE'].methods_by_name['LookupEffectiveGuestPolicy']._loaded_options = None
    _globals['_OSCONFIGSERVICE'].methods_by_name['LookupEffectiveGuestPolicy']._serialized_options = b'\x82\xd3\xe4\x93\x02Q"L/v1beta/{instance=projects/*/zones/*/instances/*}:lookupEffectiveGuestPolicy:\x01*'
    _globals['_OSCONFIGSERVICE']._serialized_start = 322
    _globals['_OSCONFIGSERVICE']._serialized_end = 3925