"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_runtime_version.ValidateProtobufRuntimeVersion(_runtime_version.Domain.PUBLIC, 5, 28, 1, '', 'google/cloud/osconfig/v1/osconfig_service.proto')
_sym_db = _symbol_database.Default()
from .....google.api import client_pb2 as google_dot_api_dot_client__pb2
from .....google.api import resource_pb2 as google_dot_api_dot_resource__pb2
from .....google.cloud.osconfig.v1 import patch_deployments_pb2 as google_dot_cloud_dot_osconfig_dot_v1_dot_patch__deployments__pb2
from .....google.cloud.osconfig.v1 import patch_jobs_pb2 as google_dot_cloud_dot_osconfig_dot_v1_dot_patch__jobs__pb2
from google.protobuf import empty_pb2 as google_dot_protobuf_dot_empty__pb2
from .....google.api import annotations_pb2 as google_dot_api_dot_annotations__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n/google/cloud/osconfig/v1/osconfig_service.proto\x12\x18google.cloud.osconfig.v1\x1a\x17google/api/client.proto\x1a\x19google/api/resource.proto\x1a0google/cloud/osconfig/v1/patch_deployments.proto\x1a)google/cloud/osconfig/v1/patch_jobs.proto\x1a\x1bgoogle/protobuf/empty.proto\x1a\x1cgoogle/api/annotations.proto2\xac\x12\n\x0fOsConfigService\x12\x9d\x01\n\x0fExecutePatchJob\x120.google.cloud.osconfig.v1.ExecutePatchJobRequest\x1a".google.cloud.osconfig.v1.PatchJob"4\x82\xd3\xe4\x93\x02.")/v1/{parent=projects/*}/patchJobs:execute:\x01*\x12\x91\x01\n\x0bGetPatchJob\x12,.google.cloud.osconfig.v1.GetPatchJobRequest\x1a".google.cloud.osconfig.v1.PatchJob"0\xdaA\x04name\x82\xd3\xe4\x93\x02#\x12!/v1/{name=projects/*/patchJobs/*}\x12\x9a\x01\n\x0eCancelPatchJob\x12/.google.cloud.osconfig.v1.CancelPatchJobRequest\x1a".google.cloud.osconfig.v1.PatchJob"3\x82\xd3\xe4\x93\x02-"(/v1/{name=projects/*/patchJobs/*}:cancel:\x01*\x12\xa4\x01\n\rListPatchJobs\x12..google.cloud.osconfig.v1.ListPatchJobsRequest\x1a/.google.cloud.osconfig.v1.ListPatchJobsResponse"2\xdaA\x06parent\x82\xd3\xe4\x93\x02#\x12!/v1/{parent=projects/*}/patchJobs\x12\xe0\x01\n\x1bListPatchJobInstanceDetails\x12<.google.cloud.osconfig.v1.ListPatchJobInstanceDetailsRequest\x1a=.google.cloud.osconfig.v1.ListPatchJobInstanceDetailsResponse"D\xdaA\x06parent\x82\xd3\xe4\x93\x025\x123/v1/{parent=projects/*/patchJobs/*}/instanceDetails\x12\xec\x01\n\x15CreatePatchDeployment\x126.google.cloud.osconfig.v1.CreatePatchDeploymentRequest\x1a).google.cloud.osconfig.v1.PatchDeployment"p\xdaA+parent,patch_deployment,patch_deployment_id\x82\xd3\xe4\x93\x02<"(/v1/{parent=projects/*}/patchDeployments:\x10patch_deployment\x12\xad\x01\n\x12GetPatchDeployment\x123.google.cloud.osconfig.v1.GetPatchDeploymentRequest\x1a).google.cloud.osconfig.v1.PatchDeployment"7\xdaA\x04name\x82\xd3\xe4\x93\x02*\x12(/v1/{name=projects/*/patchDeployments/*}\x12\xc0\x01\n\x14ListPatchDeployments\x125.google.cloud.osconfig.v1.ListPatchDeploymentsRequest\x1a6.google.cloud.osconfig.v1.ListPatchDeploymentsResponse"9\xdaA\x06parent\x82\xd3\xe4\x93\x02*\x12(/v1/{parent=projects/*}/patchDeployments\x12\xa0\x01\n\x15DeletePatchDeployment\x126.google.cloud.osconfig.v1.DeletePatchDeploymentRequest\x1a\x16.google.protobuf.Empty"7\xdaA\x04name\x82\xd3\xe4\x93\x02**(/v1/{name=projects/*/patchDeployments/*}\x12\xee\x01\n\x15UpdatePatchDeployment\x126.google.cloud.osconfig.v1.UpdatePatchDeploymentRequest\x1a).google.cloud.osconfig.v1.PatchDeployment"r\xdaA\x1cpatch_deployment,update_mask\x82\xd3\xe4\x93\x02M29/v1/{patch_deployment.name=projects/*/patchDeployments/*}:\x10patch_deployment\x12\xba\x01\n\x14PausePatchDeployment\x125.google.cloud.osconfig.v1.PausePatchDeploymentRequest\x1a).google.cloud.osconfig.v1.PatchDeployment"@\xdaA\x04name\x82\xd3\xe4\x93\x023"./v1/{name=projects/*/patchDeployments/*}:pause:\x01*\x12\xbd\x01\n\x15ResumePatchDeployment\x126.google.cloud.osconfig.v1.ResumePatchDeploymentRequest\x1a).google.cloud.osconfig.v1.PatchDeployment"A\xdaA\x04name\x82\xd3\xe4\x93\x024"//v1/{name=projects/*/patchDeployments/*}:resume:\x01*\x1aK\xcaA\x17osconfig.googleapis.com\xd2A.https://www.googleapis.com/auth/cloud-platformB\xd4\x02\n\x1ccom.google.cloud.osconfig.v1B\rOsConfigProtoZ8cloud.google.com/go/osconfig/apiv1/osconfigpb;osconfigpb\xaa\x02\x18Google.Cloud.OsConfig.V1\xca\x02\x18Google\\Cloud\\OsConfig\\V1\xea\x02\x1bGoogle::Cloud::OsConfig::V1\xeaA\x95\x01\n\x1fcompute.googleapis.com/Instance\x124projects/{project}/zones/{zone}/instances/{instance}\x12<projects/{project}/locations/{location}/instances/{instance}b\x06proto3')
_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'google.cloud.osconfig.v1.osconfig_service_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
    _globals['DESCRIPTOR']._loaded_options = None
    _globals['DESCRIPTOR']._serialized_options = b'\n\x1ccom.google.cloud.osconfig.v1B\rOsConfigProtoZ8cloud.google.com/go/osconfig/apiv1/osconfigpb;osconfigpb\xaa\x02\x18Google.Cloud.OsConfig.V1\xca\x02\x18Google\\Cloud\\OsConfig\\V1\xea\x02\x1bGoogle::Cloud::OsConfig::V1\xeaA\x95\x01\n\x1fcompute.googleapis.com/Instance\x124projects/{project}/zones/{zone}/instances/{instance}\x12<projects/{project}/locations/{location}/instances/{instance}'
    _globals['_OSCONFIGSERVICE']._loaded_options = None
    _globals['_OSCONFIGSERVICE']._serialized_options = b'\xcaA\x17osconfig.googleapis.com\xd2A.https://www.googleapis.com/auth/cloud-platform'
    _globals['_OSCONFIGSERVICE'].methods_by_name['ExecutePatchJob']._loaded_options = None
    _globals['_OSCONFIGSERVICE'].methods_by_name['ExecutePatchJob']._serialized_options = b'\x82\xd3\xe4\x93\x02.")/v1/{parent=projects/*}/patchJobs:execute:\x01*'
    _globals['_OSCONFIGSERVICE'].methods_by_name['GetPatchJob']._loaded_options = None
    _globals['_OSCONFIGSERVICE'].methods_by_name['GetPatchJob']._serialized_options = b'\xdaA\x04name\x82\xd3\xe4\x93\x02#\x12!/v1/{name=projects/*/patchJobs/*}'
    _globals['_OSCONFIGSERVICE'].methods_by_name['CancelPatchJob']._loaded_options = None
    _globals['_OSCONFIGSERVICE'].methods_by_name['CancelPatchJob']._serialized_options = b'\x82\xd3\xe4\x93\x02-"(/v1/{name=projects/*/patchJobs/*}:cancel:\x01*'
    _globals['_OSCONFIGSERVICE'].methods_by_name['ListPatchJobs']._loaded_options = None
    _globals['_OSCONFIGSERVICE'].methods_by_name['ListPatchJobs']._serialized_options = b'\xdaA\x06parent\x82\xd3\xe4\x93\x02#\x12!/v1/{parent=projects/*}/patchJobs'
    _globals['_OSCONFIGSERVICE'].methods_by_name['ListPatchJobInstanceDetails']._loaded_options = None
    _globals['_OSCONFIGSERVICE'].methods_by_name['ListPatchJobInstanceDetails']._serialized_options = b'\xdaA\x06parent\x82\xd3\xe4\x93\x025\x123/v1/{parent=projects/*/patchJobs/*}/instanceDetails'
    _globals['_OSCONFIGSERVICE'].methods_by_name['CreatePatchDeployment']._loaded_options = None
    _globals['_OSCONFIGSERVICE'].methods_by_name['CreatePatchDeployment']._serialized_options = b'\xdaA+parent,patch_deployment,patch_deployment_id\x82\xd3\xe4\x93\x02<"(/v1/{parent=projects/*}/patchDeployments:\x10patch_deployment'
    _globals['_OSCONFIGSERVICE'].methods_by_name['GetPatchDeployment']._loaded_options = None
    _globals['_OSCONFIGSERVICE'].methods_by_name['GetPatchDeployment']._serialized_options = b'\xdaA\x04name\x82\xd3\xe4\x93\x02*\x12(/v1/{name=projects/*/patchDeployments/*}'
    _globals['_OSCONFIGSERVICE'].methods_by_name['ListPatchDeployments']._loaded_options = None
    _globals['_OSCONFIGSERVICE'].methods_by_name['ListPatchDeployments']._serialized_options = b'\xdaA\x06parent\x82\xd3\xe4\x93\x02*\x12(/v1/{parent=projects/*}/patchDeployments'
    _globals['_OSCONFIGSERVICE'].methods_by_name['DeletePatchDeployment']._loaded_options = None
    _globals['_OSCONFIGSERVICE'].methods_by_name['DeletePatchDeployment']._serialized_options = b'\xdaA\x04name\x82\xd3\xe4\x93\x02**(/v1/{name=projects/*/patchDeployments/*}'
    _globals['_OSCONFIGSERVICE'].methods_by_name['UpdatePatchDeployment']._loaded_options = None
    _globals['_OSCONFIGSERVICE'].methods_by_name['UpdatePatchDeployment']._serialized_options = b'\xdaA\x1cpatch_deployment,update_mask\x82\xd3\xe4\x93\x02M29/v1/{patch_deployment.name=projects/*/patchDeployments/*}:\x10patch_deployment'
    _globals['_OSCONFIGSERVICE'].methods_by_name['PausePatchDeployment']._loaded_options = None
    _globals['_OSCONFIGSERVICE'].methods_by_name['PausePatchDeployment']._serialized_options = b'\xdaA\x04name\x82\xd3\xe4\x93\x023"./v1/{name=projects/*/patchDeployments/*}:pause:\x01*'
    _globals['_OSCONFIGSERVICE'].methods_by_name['ResumePatchDeployment']._loaded_options = None
    _globals['_OSCONFIGSERVICE'].methods_by_name['ResumePatchDeployment']._serialized_options = b'\xdaA\x04name\x82\xd3\xe4\x93\x024"//v1/{name=projects/*/patchDeployments/*}:resume:\x01*'
    _globals['_OSCONFIGSERVICE']._serialized_start = 282
    _globals['_OSCONFIGSERVICE']._serialized_end = 2630