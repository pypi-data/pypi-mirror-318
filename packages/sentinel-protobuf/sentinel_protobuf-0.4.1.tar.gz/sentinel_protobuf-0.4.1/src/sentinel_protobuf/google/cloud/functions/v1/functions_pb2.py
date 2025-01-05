"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_runtime_version.ValidateProtobufRuntimeVersion(_runtime_version.Domain.PUBLIC, 5, 28, 1, '', 'google/cloud/functions/v1/functions.proto')
_sym_db = _symbol_database.Default()
from .....google.api import annotations_pb2 as google_dot_api_dot_annotations__pb2
from .....google.api import client_pb2 as google_dot_api_dot_client__pb2
from .....google.api import field_behavior_pb2 as google_dot_api_dot_field__behavior__pb2
from .....google.api import resource_pb2 as google_dot_api_dot_resource__pb2
from .....google.cloud.functions.v1 import operations_pb2 as google_dot_cloud_dot_functions_dot_v1_dot_operations__pb2
from .....google.iam.v1 import iam_policy_pb2 as google_dot_iam_dot_v1_dot_iam__policy__pb2
from .....google.iam.v1 import policy_pb2 as google_dot_iam_dot_v1_dot_policy__pb2
from .....google.longrunning import operations_pb2 as google_dot_longrunning_dot_operations__pb2
from google.protobuf import duration_pb2 as google_dot_protobuf_dot_duration__pb2
from google.protobuf import empty_pb2 as google_dot_protobuf_dot_empty__pb2
from google.protobuf import field_mask_pb2 as google_dot_protobuf_dot_field__mask__pb2
from google.protobuf import timestamp_pb2 as google_dot_protobuf_dot_timestamp__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n)google/cloud/functions/v1/functions.proto\x12\x19google.cloud.functions.v1\x1a\x1cgoogle/api/annotations.proto\x1a\x17google/api/client.proto\x1a\x1fgoogle/api/field_behavior.proto\x1a\x19google/api/resource.proto\x1a*google/cloud/functions/v1/operations.proto\x1a\x1egoogle/iam/v1/iam_policy.proto\x1a\x1agoogle/iam/v1/policy.proto\x1a#google/longrunning/operations.proto\x1a\x1egoogle/protobuf/duration.proto\x1a\x1bgoogle/protobuf/empty.proto\x1a google/protobuf/field_mask.proto\x1a\x1fgoogle/protobuf/timestamp.proto"\xb7\x14\n\rCloudFunction\x12\x0c\n\x04name\x18\x01 \x01(\t\x12\x13\n\x0bdescription\x18\x02 \x01(\t\x12\x1c\n\x12source_archive_url\x18\x03 \x01(\tH\x00\x12H\n\x11source_repository\x18\x04 \x01(\x0b2+.google.cloud.functions.v1.SourceRepositoryH\x00\x12\x1b\n\x11source_upload_url\x18\x10 \x01(\tH\x00\x12@\n\rhttps_trigger\x18\x05 \x01(\x0b2\'.google.cloud.functions.v1.HttpsTriggerH\x01\x12@\n\revent_trigger\x18\x06 \x01(\x0b2\'.google.cloud.functions.v1.EventTriggerH\x01\x12C\n\x06status\x18\x07 \x01(\x0e2..google.cloud.functions.v1.CloudFunctionStatusB\x03\xe0A\x03\x12\x13\n\x0bentry_point\x18\x08 \x01(\t\x12\x0f\n\x07runtime\x18\x13 \x01(\t\x12*\n\x07timeout\x18\t \x01(\x0b2\x19.google.protobuf.Duration\x12\x1b\n\x13available_memory_mb\x18\n \x01(\x05\x12\x1d\n\x15service_account_email\x18\x0b \x01(\t\x124\n\x0bupdate_time\x18\x0c \x01(\x0b2\x1a.google.protobuf.TimestampB\x03\xe0A\x03\x12\x17\n\nversion_id\x18\x0e \x01(\x03B\x03\xe0A\x03\x12D\n\x06labels\x18\x0f \x03(\x0b24.google.cloud.functions.v1.CloudFunction.LabelsEntry\x12a\n\x15environment_variables\x18\x11 \x03(\x0b2B.google.cloud.functions.v1.CloudFunction.EnvironmentVariablesEntry\x12l\n\x1bbuild_environment_variables\x18\x1c \x03(\x0b2G.google.cloud.functions.v1.CloudFunction.BuildEnvironmentVariablesEntry\x12\x13\n\x07network\x18\x12 \x01(\tB\x02\x18\x01\x12\x15\n\rmax_instances\x18\x14 \x01(\x05\x12\x15\n\rmin_instances\x18  \x01(\x05\x12\x15\n\rvpc_connector\x18\x16 \x01(\t\x12j\n\x1dvpc_connector_egress_settings\x18\x17 \x01(\x0e2C.google.cloud.functions.v1.CloudFunction.VpcConnectorEgressSettings\x12R\n\x10ingress_settings\x18\x18 \x01(\x0e28.google.cloud.functions.v1.CloudFunction.IngressSettings\x12<\n\x0ckms_key_name\x18\x19 \x01(\tB&\xfaA#\n!cloudkms.googleapis.com/CryptoKey\x12\x19\n\x11build_worker_pool\x18\x1a \x01(\t\x12\x15\n\x08build_id\x18\x1b \x01(\tB\x03\xe0A\x03\x12\x17\n\nbuild_name\x18! \x01(\tB\x03\xe0A\x03\x12M\n\x1csecret_environment_variables\x18\x1d \x03(\x0b2\'.google.cloud.functions.v1.SecretEnvVar\x12?\n\x0esecret_volumes\x18\x1e \x03(\x0b2\'.google.cloud.functions.v1.SecretVolume\x12\x19\n\x0csource_token\x18\x1f \x01(\tB\x03\xe0A\x04\x12J\n\x11docker_repository\x18" \x01(\tB/\xfaA,\n*artifactregistry.googleapis.com/Repository\x12P\n\x0fdocker_registry\x18# \x01(\x0e27.google.cloud.functions.v1.CloudFunction.DockerRegistry\x12a\n\x17automatic_update_policy\x18( \x01(\x0b2>.google.cloud.functions.v1.CloudFunction.AutomaticUpdatePolicyH\x02\x12`\n\x17on_deploy_update_policy\x18) \x01(\x0b2=.google.cloud.functions.v1.CloudFunction.OnDeployUpdatePolicyH\x02\x12\x1d\n\x15build_service_account\x18+ \x01(\t\x1a\x17\n\x15AutomaticUpdatePolicy\x1a4\n\x14OnDeployUpdatePolicy\x12\x1c\n\x0fruntime_version\x18\x01 \x01(\tB\x03\xe0A\x03\x1a-\n\x0bLabelsEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\r\n\x05value\x18\x02 \x01(\t:\x028\x01\x1a;\n\x19EnvironmentVariablesEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\r\n\x05value\x18\x02 \x01(\t:\x028\x01\x1a@\n\x1eBuildEnvironmentVariablesEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\r\n\x05value\x18\x02 \x01(\t:\x028\x01"u\n\x1aVpcConnectorEgressSettings\x12-\n)VPC_CONNECTOR_EGRESS_SETTINGS_UNSPECIFIED\x10\x00\x12\x17\n\x13PRIVATE_RANGES_ONLY\x10\x01\x12\x0f\n\x0bALL_TRAFFIC\x10\x02"x\n\x0fIngressSettings\x12 \n\x1cINGRESS_SETTINGS_UNSPECIFIED\x10\x00\x12\r\n\tALLOW_ALL\x10\x01\x12\x17\n\x13ALLOW_INTERNAL_ONLY\x10\x02\x12\x1b\n\x17ALLOW_INTERNAL_AND_GCLB\x10\x03"`\n\x0eDockerRegistry\x12\x1f\n\x1bDOCKER_REGISTRY_UNSPECIFIED\x10\x00\x12\x16\n\x12CONTAINER_REGISTRY\x10\x01\x12\x15\n\x11ARTIFACT_REGISTRY\x10\x02:n\xeaAk\n+cloudfunctions.googleapis.com/CloudFunction\x12<projects/{project}/locations/{location}/functions/{function}B\r\n\x0bsource_codeB\t\n\x07triggerB\x17\n\x15runtime_update_policy":\n\x10SourceRepository\x12\x0b\n\x03url\x18\x01 \x01(\t\x12\x19\n\x0cdeployed_url\x18\x02 \x01(\tB\x03\xe0A\x03"\xc8\x01\n\x0cHttpsTrigger\x12\x10\n\x03url\x18\x01 \x01(\tB\x03\xe0A\x03\x12M\n\x0esecurity_level\x18\x02 \x01(\x0e25.google.cloud.functions.v1.HttpsTrigger.SecurityLevel"W\n\rSecurityLevel\x12\x1e\n\x1aSECURITY_LEVEL_UNSPECIFIED\x10\x00\x12\x11\n\rSECURE_ALWAYS\x10\x01\x12\x13\n\x0fSECURE_OPTIONAL\x10\x02"\x87\x01\n\x0cEventTrigger\x12\x12\n\nevent_type\x18\x01 \x01(\t\x12\x10\n\x08resource\x18\x02 \x01(\t\x12\x0f\n\x07service\x18\x03 \x01(\t\x12@\n\x0efailure_policy\x18\x05 \x01(\x0b2(.google.cloud.functions.v1.FailurePolicy"c\n\rFailurePolicy\x12?\n\x05retry\x18\x01 \x01(\x0b2..google.cloud.functions.v1.FailurePolicy.RetryH\x00\x1a\x07\n\x05RetryB\x08\n\x06action"P\n\x0cSecretEnvVar\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\x12\n\nproject_id\x18\x02 \x01(\t\x12\x0e\n\x06secret\x18\x03 \x01(\t\x12\x0f\n\x07version\x18\x04 \x01(\t"\xbf\x01\n\x0cSecretVolume\x12\x12\n\nmount_path\x18\x01 \x01(\t\x12\x12\n\nproject_id\x18\x02 \x01(\t\x12\x0e\n\x06secret\x18\x03 \x01(\t\x12G\n\x08versions\x18\x04 \x03(\x0b25.google.cloud.functions.v1.SecretVolume.SecretVersion\x1a.\n\rSecretVersion\x12\x0f\n\x07version\x18\x01 \x01(\t\x12\x0c\n\x04path\x18\x02 \x01(\t"\x95\x01\n\x15CreateFunctionRequest\x12;\n\x08location\x18\x01 \x01(\tB)\xe0A\x02\xfaA#\n!locations.googleapis.com/Location\x12?\n\x08function\x18\x02 \x01(\x0b2(.google.cloud.functions.v1.CloudFunctionB\x03\xe0A\x02"\x89\x01\n\x15UpdateFunctionRequest\x12?\n\x08function\x18\x01 \x01(\x0b2(.google.cloud.functions.v1.CloudFunctionB\x03\xe0A\x02\x12/\n\x0bupdate_mask\x18\x02 \x01(\x0b2\x1a.google.protobuf.FieldMask"p\n\x12GetFunctionRequest\x12A\n\x04name\x18\x01 \x01(\tB3\xe0A\x02\xfaA-\n+cloudfunctions.googleapis.com/CloudFunction\x12\x17\n\nversion_id\x18\x02 \x01(\x03B\x03\xe0A\x01"u\n\x14ListFunctionsRequest\x126\n\x06parent\x18\x01 \x01(\tB&\xfaA#\n!locations.googleapis.com/Location\x12\x11\n\tpage_size\x18\x02 \x01(\x05\x12\x12\n\npage_token\x18\x03 \x01(\t"\x82\x01\n\x15ListFunctionsResponse\x12;\n\tfunctions\x18\x01 \x03(\x0b2(.google.cloud.functions.v1.CloudFunction\x12\x17\n\x0fnext_page_token\x18\x02 \x01(\t\x12\x13\n\x0bunreachable\x18\x03 \x03(\t"Z\n\x15DeleteFunctionRequest\x12A\n\x04name\x18\x01 \x01(\tB3\xe0A\x02\xfaA-\n+cloudfunctions.googleapis.com/CloudFunction"k\n\x13CallFunctionRequest\x12A\n\x04name\x18\x01 \x01(\tB3\xe0A\x02\xfaA-\n+cloudfunctions.googleapis.com/CloudFunction\x12\x11\n\x04data\x18\x02 \x01(\tB\x03\xe0A\x02"K\n\x14CallFunctionResponse\x12\x14\n\x0cexecution_id\x18\x01 \x01(\t\x12\x0e\n\x06result\x18\x02 \x01(\t\x12\r\n\x05error\x18\x03 \x01(\t"h\n\x18GenerateUploadUrlRequest\x12\x0e\n\x06parent\x18\x01 \x01(\t\x12<\n\x0ckms_key_name\x18\x02 \x01(\tB&\xfaA#\n!cloudkms.googleapis.com/CryptoKey"/\n\x19GenerateUploadUrlResponse\x12\x12\n\nupload_url\x18\x01 \x01(\t">\n\x1aGenerateDownloadUrlRequest\x12\x0c\n\x04name\x18\x01 \x01(\t\x12\x12\n\nversion_id\x18\x02 \x01(\x04"3\n\x1bGenerateDownloadUrlResponse\x12\x14\n\x0cdownload_url\x18\x01 \x01(\t*\x92\x01\n\x13CloudFunctionStatus\x12%\n!CLOUD_FUNCTION_STATUS_UNSPECIFIED\x10\x00\x12\n\n\x06ACTIVE\x10\x01\x12\x0b\n\x07OFFLINE\x10\x02\x12\x16\n\x12DEPLOY_IN_PROGRESS\x10\x03\x12\x16\n\x12DELETE_IN_PROGRESS\x10\x04\x12\x0b\n\x07UNKNOWN\x10\x052\x97\x11\n\x15CloudFunctionsService\x12\xa9\x01\n\rListFunctions\x12/.google.cloud.functions.v1.ListFunctionsRequest\x1a0.google.cloud.functions.v1.ListFunctionsResponse"5\x82\xd3\xe4\x93\x02/\x12-/v1/{parent=projects/*/locations/*}/functions\x12\xa4\x01\n\x0bGetFunction\x12-.google.cloud.functions.v1.GetFunctionRequest\x1a(.google.cloud.functions.v1.CloudFunction"<\xdaA\x04name\x82\xd3\xe4\x93\x02/\x12-/v1/{name=projects/*/locations/*/functions/*}\x12\xdf\x01\n\x0eCreateFunction\x120.google.cloud.functions.v1.CreateFunctionRequest\x1a\x1d.google.longrunning.Operation"|\xcaA$\n\rCloudFunction\x12\x13OperationMetadataV1\xdaA\x11location,function\x82\xd3\xe4\x93\x02;"//v1/{location=projects/*/locations/*}/functions:\x08function\x12\xdd\x01\n\x0eUpdateFunction\x120.google.cloud.functions.v1.UpdateFunctionRequest\x1a\x1d.google.longrunning.Operation"z\xcaA$\n\rCloudFunction\x12\x13OperationMetadataV1\xdaA\x08function\x82\xd3\xe4\x93\x02B26/v1/{function.name=projects/*/locations/*/functions/*}:\x08function\x12\xce\x01\n\x0eDeleteFunction\x120.google.cloud.functions.v1.DeleteFunctionRequest\x1a\x1d.google.longrunning.Operation"k\xcaA,\n\x15google.protobuf.Empty\x12\x13OperationMetadataV1\xdaA\x04name\x82\xd3\xe4\x93\x02/*-/v1/{name=projects/*/locations/*/functions/*}\x12\xba\x01\n\x0cCallFunction\x12..google.cloud.functions.v1.CallFunctionRequest\x1a/.google.cloud.functions.v1.CallFunctionResponse"I\xdaA\tname,data\x82\xd3\xe4\x93\x027"2/v1/{name=projects/*/locations/*/functions/*}:call:\x01*\x12\xca\x01\n\x11GenerateUploadUrl\x123.google.cloud.functions.v1.GenerateUploadUrlRequest\x1a4.google.cloud.functions.v1.GenerateUploadUrlResponse"J\x82\xd3\xe4\x93\x02D"?/v1/{parent=projects/*/locations/*}/functions:generateUploadUrl:\x01*\x12\xd2\x01\n\x13GenerateDownloadUrl\x125.google.cloud.functions.v1.GenerateDownloadUrlRequest\x1a6.google.cloud.functions.v1.GenerateDownloadUrlResponse"L\x82\xd3\xe4\x93\x02F"A/v1/{name=projects/*/locations/*/functions/*}:generateDownloadUrl:\x01*\x12\x94\x01\n\x0cSetIamPolicy\x12".google.iam.v1.SetIamPolicyRequest\x1a\x15.google.iam.v1.Policy"I\x82\xd3\xe4\x93\x02C">/v1/{resource=projects/*/locations/*/functions/*}:setIamPolicy:\x01*\x12\x91\x01\n\x0cGetIamPolicy\x12".google.iam.v1.GetIamPolicyRequest\x1a\x15.google.iam.v1.Policy"F\x82\xd3\xe4\x93\x02@\x12>/v1/{resource=projects/*/locations/*/functions/*}:getIamPolicy\x12\xba\x01\n\x12TestIamPermissions\x12(.google.iam.v1.TestIamPermissionsRequest\x1a).google.iam.v1.TestIamPermissionsResponse"O\x82\xd3\xe4\x93\x02I"D/v1/{resource=projects/*/locations/*/functions/*}:testIamPermissions:\x01*\x1aQ\xcaA\x1dcloudfunctions.googleapis.com\xd2A.https://www.googleapis.com/auth/cloud-platformB\xe1\x02\n\x1dcom.google.cloud.functions.v1B\x0eFunctionsProtoP\x01Z;cloud.google.com/go/functions/apiv1/functionspb;functionspb\xa2\x02\x03GCF\xeaAo\n*artifactregistry.googleapis.com/Repository\x12Aprojects/{project}/locations/{location}/repositories/{repository}\xeaAx\n!cloudkms.googleapis.com/CryptoKey\x12Sprojects/{project}/locations/{location}/keyRings/{key_ring}/cryptoKeys/{crypto_key}b\x06proto3')
_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'google.cloud.functions.v1.functions_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
    _globals['DESCRIPTOR']._loaded_options = None
    _globals['DESCRIPTOR']._serialized_options = b'\n\x1dcom.google.cloud.functions.v1B\x0eFunctionsProtoP\x01Z;cloud.google.com/go/functions/apiv1/functionspb;functionspb\xa2\x02\x03GCF\xeaAo\n*artifactregistry.googleapis.com/Repository\x12Aprojects/{project}/locations/{location}/repositories/{repository}\xeaAx\n!cloudkms.googleapis.com/CryptoKey\x12Sprojects/{project}/locations/{location}/keyRings/{key_ring}/cryptoKeys/{crypto_key}'
    _globals['_CLOUDFUNCTION_ONDEPLOYUPDATEPOLICY'].fields_by_name['runtime_version']._loaded_options = None
    _globals['_CLOUDFUNCTION_ONDEPLOYUPDATEPOLICY'].fields_by_name['runtime_version']._serialized_options = b'\xe0A\x03'
    _globals['_CLOUDFUNCTION_LABELSENTRY']._loaded_options = None
    _globals['_CLOUDFUNCTION_LABELSENTRY']._serialized_options = b'8\x01'
    _globals['_CLOUDFUNCTION_ENVIRONMENTVARIABLESENTRY']._loaded_options = None
    _globals['_CLOUDFUNCTION_ENVIRONMENTVARIABLESENTRY']._serialized_options = b'8\x01'
    _globals['_CLOUDFUNCTION_BUILDENVIRONMENTVARIABLESENTRY']._loaded_options = None
    _globals['_CLOUDFUNCTION_BUILDENVIRONMENTVARIABLESENTRY']._serialized_options = b'8\x01'
    _globals['_CLOUDFUNCTION'].fields_by_name['status']._loaded_options = None
    _globals['_CLOUDFUNCTION'].fields_by_name['status']._serialized_options = b'\xe0A\x03'
    _globals['_CLOUDFUNCTION'].fields_by_name['update_time']._loaded_options = None
    _globals['_CLOUDFUNCTION'].fields_by_name['update_time']._serialized_options = b'\xe0A\x03'
    _globals['_CLOUDFUNCTION'].fields_by_name['version_id']._loaded_options = None
    _globals['_CLOUDFUNCTION'].fields_by_name['version_id']._serialized_options = b'\xe0A\x03'
    _globals['_CLOUDFUNCTION'].fields_by_name['network']._loaded_options = None
    _globals['_CLOUDFUNCTION'].fields_by_name['network']._serialized_options = b'\x18\x01'
    _globals['_CLOUDFUNCTION'].fields_by_name['kms_key_name']._loaded_options = None
    _globals['_CLOUDFUNCTION'].fields_by_name['kms_key_name']._serialized_options = b'\xfaA#\n!cloudkms.googleapis.com/CryptoKey'
    _globals['_CLOUDFUNCTION'].fields_by_name['build_id']._loaded_options = None
    _globals['_CLOUDFUNCTION'].fields_by_name['build_id']._serialized_options = b'\xe0A\x03'
    _globals['_CLOUDFUNCTION'].fields_by_name['build_name']._loaded_options = None
    _globals['_CLOUDFUNCTION'].fields_by_name['build_name']._serialized_options = b'\xe0A\x03'
    _globals['_CLOUDFUNCTION'].fields_by_name['source_token']._loaded_options = None
    _globals['_CLOUDFUNCTION'].fields_by_name['source_token']._serialized_options = b'\xe0A\x04'
    _globals['_CLOUDFUNCTION'].fields_by_name['docker_repository']._loaded_options = None
    _globals['_CLOUDFUNCTION'].fields_by_name['docker_repository']._serialized_options = b'\xfaA,\n*artifactregistry.googleapis.com/Repository'
    _globals['_CLOUDFUNCTION']._loaded_options = None
    _globals['_CLOUDFUNCTION']._serialized_options = b'\xeaAk\n+cloudfunctions.googleapis.com/CloudFunction\x12<projects/{project}/locations/{location}/functions/{function}'
    _globals['_SOURCEREPOSITORY'].fields_by_name['deployed_url']._loaded_options = None
    _globals['_SOURCEREPOSITORY'].fields_by_name['deployed_url']._serialized_options = b'\xe0A\x03'
    _globals['_HTTPSTRIGGER'].fields_by_name['url']._loaded_options = None
    _globals['_HTTPSTRIGGER'].fields_by_name['url']._serialized_options = b'\xe0A\x03'
    _globals['_CREATEFUNCTIONREQUEST'].fields_by_name['location']._loaded_options = None
    _globals['_CREATEFUNCTIONREQUEST'].fields_by_name['location']._serialized_options = b'\xe0A\x02\xfaA#\n!locations.googleapis.com/Location'
    _globals['_CREATEFUNCTIONREQUEST'].fields_by_name['function']._loaded_options = None
    _globals['_CREATEFUNCTIONREQUEST'].fields_by_name['function']._serialized_options = b'\xe0A\x02'
    _globals['_UPDATEFUNCTIONREQUEST'].fields_by_name['function']._loaded_options = None
    _globals['_UPDATEFUNCTIONREQUEST'].fields_by_name['function']._serialized_options = b'\xe0A\x02'
    _globals['_GETFUNCTIONREQUEST'].fields_by_name['name']._loaded_options = None
    _globals['_GETFUNCTIONREQUEST'].fields_by_name['name']._serialized_options = b'\xe0A\x02\xfaA-\n+cloudfunctions.googleapis.com/CloudFunction'
    _globals['_GETFUNCTIONREQUEST'].fields_by_name['version_id']._loaded_options = None
    _globals['_GETFUNCTIONREQUEST'].fields_by_name['version_id']._serialized_options = b'\xe0A\x01'
    _globals['_LISTFUNCTIONSREQUEST'].fields_by_name['parent']._loaded_options = None
    _globals['_LISTFUNCTIONSREQUEST'].fields_by_name['parent']._serialized_options = b'\xfaA#\n!locations.googleapis.com/Location'
    _globals['_DELETEFUNCTIONREQUEST'].fields_by_name['name']._loaded_options = None
    _globals['_DELETEFUNCTIONREQUEST'].fields_by_name['name']._serialized_options = b'\xe0A\x02\xfaA-\n+cloudfunctions.googleapis.com/CloudFunction'
    _globals['_CALLFUNCTIONREQUEST'].fields_by_name['name']._loaded_options = None
    _globals['_CALLFUNCTIONREQUEST'].fields_by_name['name']._serialized_options = b'\xe0A\x02\xfaA-\n+cloudfunctions.googleapis.com/CloudFunction'
    _globals['_CALLFUNCTIONREQUEST'].fields_by_name['data']._loaded_options = None
    _globals['_CALLFUNCTIONREQUEST'].fields_by_name['data']._serialized_options = b'\xe0A\x02'
    _globals['_GENERATEUPLOADURLREQUEST'].fields_by_name['kms_key_name']._loaded_options = None
    _globals['_GENERATEUPLOADURLREQUEST'].fields_by_name['kms_key_name']._serialized_options = b'\xfaA#\n!cloudkms.googleapis.com/CryptoKey'
    _globals['_CLOUDFUNCTIONSSERVICE']._loaded_options = None
    _globals['_CLOUDFUNCTIONSSERVICE']._serialized_options = b'\xcaA\x1dcloudfunctions.googleapis.com\xd2A.https://www.googleapis.com/auth/cloud-platform'
    _globals['_CLOUDFUNCTIONSSERVICE'].methods_by_name['ListFunctions']._loaded_options = None
    _globals['_CLOUDFUNCTIONSSERVICE'].methods_by_name['ListFunctions']._serialized_options = b'\x82\xd3\xe4\x93\x02/\x12-/v1/{parent=projects/*/locations/*}/functions'
    _globals['_CLOUDFUNCTIONSSERVICE'].methods_by_name['GetFunction']._loaded_options = None
    _globals['_CLOUDFUNCTIONSSERVICE'].methods_by_name['GetFunction']._serialized_options = b'\xdaA\x04name\x82\xd3\xe4\x93\x02/\x12-/v1/{name=projects/*/locations/*/functions/*}'
    _globals['_CLOUDFUNCTIONSSERVICE'].methods_by_name['CreateFunction']._loaded_options = None
    _globals['_CLOUDFUNCTIONSSERVICE'].methods_by_name['CreateFunction']._serialized_options = b'\xcaA$\n\rCloudFunction\x12\x13OperationMetadataV1\xdaA\x11location,function\x82\xd3\xe4\x93\x02;"//v1/{location=projects/*/locations/*}/functions:\x08function'
    _globals['_CLOUDFUNCTIONSSERVICE'].methods_by_name['UpdateFunction']._loaded_options = None
    _globals['_CLOUDFUNCTIONSSERVICE'].methods_by_name['UpdateFunction']._serialized_options = b'\xcaA$\n\rCloudFunction\x12\x13OperationMetadataV1\xdaA\x08function\x82\xd3\xe4\x93\x02B26/v1/{function.name=projects/*/locations/*/functions/*}:\x08function'
    _globals['_CLOUDFUNCTIONSSERVICE'].methods_by_name['DeleteFunction']._loaded_options = None
    _globals['_CLOUDFUNCTIONSSERVICE'].methods_by_name['DeleteFunction']._serialized_options = b'\xcaA,\n\x15google.protobuf.Empty\x12\x13OperationMetadataV1\xdaA\x04name\x82\xd3\xe4\x93\x02/*-/v1/{name=projects/*/locations/*/functions/*}'
    _globals['_CLOUDFUNCTIONSSERVICE'].methods_by_name['CallFunction']._loaded_options = None
    _globals['_CLOUDFUNCTIONSSERVICE'].methods_by_name['CallFunction']._serialized_options = b'\xdaA\tname,data\x82\xd3\xe4\x93\x027"2/v1/{name=projects/*/locations/*/functions/*}:call:\x01*'
    _globals['_CLOUDFUNCTIONSSERVICE'].methods_by_name['GenerateUploadUrl']._loaded_options = None
    _globals['_CLOUDFUNCTIONSSERVICE'].methods_by_name['GenerateUploadUrl']._serialized_options = b'\x82\xd3\xe4\x93\x02D"?/v1/{parent=projects/*/locations/*}/functions:generateUploadUrl:\x01*'
    _globals['_CLOUDFUNCTIONSSERVICE'].methods_by_name['GenerateDownloadUrl']._loaded_options = None
    _globals['_CLOUDFUNCTIONSSERVICE'].methods_by_name['GenerateDownloadUrl']._serialized_options = b'\x82\xd3\xe4\x93\x02F"A/v1/{name=projects/*/locations/*/functions/*}:generateDownloadUrl:\x01*'
    _globals['_CLOUDFUNCTIONSSERVICE'].methods_by_name['SetIamPolicy']._loaded_options = None
    _globals['_CLOUDFUNCTIONSSERVICE'].methods_by_name['SetIamPolicy']._serialized_options = b'\x82\xd3\xe4\x93\x02C">/v1/{resource=projects/*/locations/*/functions/*}:setIamPolicy:\x01*'
    _globals['_CLOUDFUNCTIONSSERVICE'].methods_by_name['GetIamPolicy']._loaded_options = None
    _globals['_CLOUDFUNCTIONSSERVICE'].methods_by_name['GetIamPolicy']._serialized_options = b'\x82\xd3\xe4\x93\x02@\x12>/v1/{resource=projects/*/locations/*/functions/*}:getIamPolicy'
    _globals['_CLOUDFUNCTIONSSERVICE'].methods_by_name['TestIamPermissions']._loaded_options = None
    _globals['_CLOUDFUNCTIONSSERVICE'].methods_by_name['TestIamPermissions']._serialized_options = b'\x82\xd3\xe4\x93\x02I"D/v1/{resource=projects/*/locations/*/functions/*}:testIamPermissions:\x01*'
    _globals['_CLOUDFUNCTIONSTATUS']._serialized_start = 5061
    _globals['_CLOUDFUNCTIONSTATUS']._serialized_end = 5207
    _globals['_CLOUDFUNCTION']._serialized_start = 457
    _globals['_CLOUDFUNCTION']._serialized_end = 3072
    _globals['_CLOUDFUNCTION_AUTOMATICUPDATEPOLICY']._serialized_start = 2319
    _globals['_CLOUDFUNCTION_AUTOMATICUPDATEPOLICY']._serialized_end = 2342
    _globals['_CLOUDFUNCTION_ONDEPLOYUPDATEPOLICY']._serialized_start = 2344
    _globals['_CLOUDFUNCTION_ONDEPLOYUPDATEPOLICY']._serialized_end = 2396
    _globals['_CLOUDFUNCTION_LABELSENTRY']._serialized_start = 2398
    _globals['_CLOUDFUNCTION_LABELSENTRY']._serialized_end = 2443
    _globals['_CLOUDFUNCTION_ENVIRONMENTVARIABLESENTRY']._serialized_start = 2445
    _globals['_CLOUDFUNCTION_ENVIRONMENTVARIABLESENTRY']._serialized_end = 2504
    _globals['_CLOUDFUNCTION_BUILDENVIRONMENTVARIABLESENTRY']._serialized_start = 2506
    _globals['_CLOUDFUNCTION_BUILDENVIRONMENTVARIABLESENTRY']._serialized_end = 2570
    _globals['_CLOUDFUNCTION_VPCCONNECTOREGRESSSETTINGS']._serialized_start = 2572
    _globals['_CLOUDFUNCTION_VPCCONNECTOREGRESSSETTINGS']._serialized_end = 2689
    _globals['_CLOUDFUNCTION_INGRESSSETTINGS']._serialized_start = 2691
    _globals['_CLOUDFUNCTION_INGRESSSETTINGS']._serialized_end = 2811
    _globals['_CLOUDFUNCTION_DOCKERREGISTRY']._serialized_start = 2813
    _globals['_CLOUDFUNCTION_DOCKERREGISTRY']._serialized_end = 2909
    _globals['_SOURCEREPOSITORY']._serialized_start = 3074
    _globals['_SOURCEREPOSITORY']._serialized_end = 3132
    _globals['_HTTPSTRIGGER']._serialized_start = 3135
    _globals['_HTTPSTRIGGER']._serialized_end = 3335
    _globals['_HTTPSTRIGGER_SECURITYLEVEL']._serialized_start = 3248
    _globals['_HTTPSTRIGGER_SECURITYLEVEL']._serialized_end = 3335
    _globals['_EVENTTRIGGER']._serialized_start = 3338
    _globals['_EVENTTRIGGER']._serialized_end = 3473
    _globals['_FAILUREPOLICY']._serialized_start = 3475
    _globals['_FAILUREPOLICY']._serialized_end = 3574
    _globals['_FAILUREPOLICY_RETRY']._serialized_start = 3557
    _globals['_FAILUREPOLICY_RETRY']._serialized_end = 3564
    _globals['_SECRETENVVAR']._serialized_start = 3576
    _globals['_SECRETENVVAR']._serialized_end = 3656
    _globals['_SECRETVOLUME']._serialized_start = 3659
    _globals['_SECRETVOLUME']._serialized_end = 3850
    _globals['_SECRETVOLUME_SECRETVERSION']._serialized_start = 3804
    _globals['_SECRETVOLUME_SECRETVERSION']._serialized_end = 3850
    _globals['_CREATEFUNCTIONREQUEST']._serialized_start = 3853
    _globals['_CREATEFUNCTIONREQUEST']._serialized_end = 4002
    _globals['_UPDATEFUNCTIONREQUEST']._serialized_start = 4005
    _globals['_UPDATEFUNCTIONREQUEST']._serialized_end = 4142
    _globals['_GETFUNCTIONREQUEST']._serialized_start = 4144
    _globals['_GETFUNCTIONREQUEST']._serialized_end = 4256
    _globals['_LISTFUNCTIONSREQUEST']._serialized_start = 4258
    _globals['_LISTFUNCTIONSREQUEST']._serialized_end = 4375
    _globals['_LISTFUNCTIONSRESPONSE']._serialized_start = 4378
    _globals['_LISTFUNCTIONSRESPONSE']._serialized_end = 4508
    _globals['_DELETEFUNCTIONREQUEST']._serialized_start = 4510
    _globals['_DELETEFUNCTIONREQUEST']._serialized_end = 4600
    _globals['_CALLFUNCTIONREQUEST']._serialized_start = 4602
    _globals['_CALLFUNCTIONREQUEST']._serialized_end = 4709
    _globals['_CALLFUNCTIONRESPONSE']._serialized_start = 4711
    _globals['_CALLFUNCTIONRESPONSE']._serialized_end = 4786
    _globals['_GENERATEUPLOADURLREQUEST']._serialized_start = 4788
    _globals['_GENERATEUPLOADURLREQUEST']._serialized_end = 4892
    _globals['_GENERATEUPLOADURLRESPONSE']._serialized_start = 4894
    _globals['_GENERATEUPLOADURLRESPONSE']._serialized_end = 4941
    _globals['_GENERATEDOWNLOADURLREQUEST']._serialized_start = 4943
    _globals['_GENERATEDOWNLOADURLREQUEST']._serialized_end = 5005
    _globals['_GENERATEDOWNLOADURLRESPONSE']._serialized_start = 5007
    _globals['_GENERATEDOWNLOADURLRESPONSE']._serialized_end = 5058
    _globals['_CLOUDFUNCTIONSSERVICE']._serialized_start = 5210
    _globals['_CLOUDFUNCTIONSSERVICE']._serialized_end = 7409