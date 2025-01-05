"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_runtime_version.ValidateProtobufRuntimeVersion(_runtime_version.Domain.PUBLIC, 5, 28, 1, '', 'google/cloud/secrets/v1beta1/service.proto')
_sym_db = _symbol_database.Default()
from .....google.api import annotations_pb2 as google_dot_api_dot_annotations__pb2
from .....google.api import client_pb2 as google_dot_api_dot_client__pb2
from .....google.api import field_behavior_pb2 as google_dot_api_dot_field__behavior__pb2
from .....google.api import resource_pb2 as google_dot_api_dot_resource__pb2
from .....google.cloud.secrets.v1beta1 import resources_pb2 as google_dot_cloud_dot_secrets_dot_v1beta1_dot_resources__pb2
from .....google.iam.v1 import iam_policy_pb2 as google_dot_iam_dot_v1_dot_iam__policy__pb2
from .....google.iam.v1 import policy_pb2 as google_dot_iam_dot_v1_dot_policy__pb2
from google.protobuf import empty_pb2 as google_dot_protobuf_dot_empty__pb2
from google.protobuf import field_mask_pb2 as google_dot_protobuf_dot_field__mask__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n*google/cloud/secrets/v1beta1/service.proto\x12\x1cgoogle.cloud.secrets.v1beta1\x1a\x1cgoogle/api/annotations.proto\x1a\x17google/api/client.proto\x1a\x1fgoogle/api/field_behavior.proto\x1a\x19google/api/resource.proto\x1a,google/cloud/secrets/v1beta1/resources.proto\x1a\x1egoogle/iam/v1/iam_policy.proto\x1a\x1agoogle/iam/v1/policy.proto\x1a\x1bgoogle/protobuf/empty.proto\x1a google/protobuf/field_mask.proto"\x8a\x01\n\x12ListSecretsRequest\x12C\n\x06parent\x18\x01 \x01(\tB3\xe0A\x02\xfaA-\n+cloudresourcemanager.googleapis.com/Project\x12\x16\n\tpage_size\x18\x02 \x01(\x05B\x03\xe0A\x01\x12\x17\n\npage_token\x18\x03 \x01(\tB\x03\xe0A\x01"y\n\x13ListSecretsResponse\x125\n\x07secrets\x18\x01 \x03(\x0b2$.google.cloud.secrets.v1beta1.Secret\x12\x17\n\x0fnext_page_token\x18\x02 \x01(\t\x12\x12\n\ntotal_size\x18\x03 \x01(\x05"\xad\x01\n\x13CreateSecretRequest\x12C\n\x06parent\x18\x01 \x01(\tB3\xe0A\x02\xfaA-\n+cloudresourcemanager.googleapis.com/Project\x12\x16\n\tsecret_id\x18\x02 \x01(\tB\x03\xe0A\x02\x129\n\x06secret\x18\x03 \x01(\x0b2$.google.cloud.secrets.v1beta1.SecretB\x03\xe0A\x02"\x99\x01\n\x17AddSecretVersionRequest\x12;\n\x06parent\x18\x01 \x01(\tB+\xe0A\x02\xfaA%\n#secretmanager.googleapis.com/Secret\x12A\n\x07payload\x18\x02 \x01(\x0b2+.google.cloud.secrets.v1beta1.SecretPayloadB\x03\xe0A\x02"M\n\x10GetSecretRequest\x129\n\x04name\x18\x01 \x01(\tB+\xe0A\x02\xfaA%\n#secretmanager.googleapis.com/Secret"\x89\x01\n\x19ListSecretVersionsRequest\x12;\n\x06parent\x18\x01 \x01(\tB+\xe0A\x02\xfaA%\n#secretmanager.googleapis.com/Secret\x12\x16\n\tpage_size\x18\x02 \x01(\x05B\x03\xe0A\x01\x12\x17\n\npage_token\x18\x03 \x01(\tB\x03\xe0A\x01"\x88\x01\n\x1aListSecretVersionsResponse\x12=\n\x08versions\x18\x01 \x03(\x0b2+.google.cloud.secrets.v1beta1.SecretVersion\x12\x17\n\x0fnext_page_token\x18\x02 \x01(\t\x12\x12\n\ntotal_size\x18\x03 \x01(\x05"[\n\x17GetSecretVersionRequest\x12@\n\x04name\x18\x01 \x01(\tB2\xe0A\x02\xfaA,\n*secretmanager.googleapis.com/SecretVersion"\x86\x01\n\x13UpdateSecretRequest\x129\n\x06secret\x18\x01 \x01(\x0b2$.google.cloud.secrets.v1beta1.SecretB\x03\xe0A\x02\x124\n\x0bupdate_mask\x18\x02 \x01(\x0b2\x1a.google.protobuf.FieldMaskB\x03\xe0A\x02"^\n\x1aAccessSecretVersionRequest\x12@\n\x04name\x18\x01 \x01(\tB2\xe0A\x02\xfaA,\n*secretmanager.googleapis.com/SecretVersion"\x9a\x01\n\x1bAccessSecretVersionResponse\x12=\n\x04name\x18\x01 \x01(\tB/\xfaA,\n*secretmanager.googleapis.com/SecretVersion\x12<\n\x07payload\x18\x02 \x01(\x0b2+.google.cloud.secrets.v1beta1.SecretPayload"P\n\x13DeleteSecretRequest\x129\n\x04name\x18\x01 \x01(\tB+\xe0A\x02\xfaA%\n#secretmanager.googleapis.com/Secret"_\n\x1bDisableSecretVersionRequest\x12@\n\x04name\x18\x01 \x01(\tB2\xe0A\x02\xfaA,\n*secretmanager.googleapis.com/SecretVersion"^\n\x1aEnableSecretVersionRequest\x12@\n\x04name\x18\x01 \x01(\tB2\xe0A\x02\xfaA,\n*secretmanager.googleapis.com/SecretVersion"_\n\x1bDestroySecretVersionRequest\x12@\n\x04name\x18\x01 \x01(\tB2\xe0A\x02\xfaA,\n*secretmanager.googleapis.com/SecretVersion2\x83\x16\n\x14SecretManagerService\x12\xa9\x01\n\x0bListSecrets\x120.google.cloud.secrets.v1beta1.ListSecretsRequest\x1a1.google.cloud.secrets.v1beta1.ListSecretsResponse"5\xdaA\x06parent\x82\xd3\xe4\x93\x02&\x12$/v1beta1/{parent=projects/*}/secrets\x12\xb7\x01\n\x0cCreateSecret\x121.google.cloud.secrets.v1beta1.CreateSecretRequest\x1a$.google.cloud.secrets.v1beta1.Secret"N\xdaA\x17parent,secret_id,secret\x82\xd3\xe4\x93\x02."$/v1beta1/{parent=projects/*}/secrets:\x06secret\x12\xc5\x01\n\x10AddSecretVersion\x125.google.cloud.secrets.v1beta1.AddSecretVersionRequest\x1a+.google.cloud.secrets.v1beta1.SecretVersion"M\xdaA\x0eparent,payload\x82\xd3\xe4\x93\x026"1/v1beta1/{parent=projects/*/secrets/*}:addVersion:\x01*\x12\x96\x01\n\tGetSecret\x12..google.cloud.secrets.v1beta1.GetSecretRequest\x1a$.google.cloud.secrets.v1beta1.Secret"3\xdaA\x04name\x82\xd3\xe4\x93\x02&\x12$/v1beta1/{name=projects/*/secrets/*}\x12\xb9\x01\n\x0cUpdateSecret\x121.google.cloud.secrets.v1beta1.UpdateSecretRequest\x1a$.google.cloud.secrets.v1beta1.Secret"P\xdaA\x12secret,update_mask\x82\xd3\xe4\x93\x0252+/v1beta1/{secret.name=projects/*/secrets/*}:\x06secret\x12\x8e\x01\n\x0cDeleteSecret\x121.google.cloud.secrets.v1beta1.DeleteSecretRequest\x1a\x16.google.protobuf.Empty"3\xdaA\x04name\x82\xd3\xe4\x93\x02&*$/v1beta1/{name=projects/*/secrets/*}\x12\xc9\x01\n\x12ListSecretVersions\x127.google.cloud.secrets.v1beta1.ListSecretVersionsRequest\x1a8.google.cloud.secrets.v1beta1.ListSecretVersionsResponse"@\xdaA\x06parent\x82\xd3\xe4\x93\x021\x12//v1beta1/{parent=projects/*/secrets/*}/versions\x12\xb6\x01\n\x10GetSecretVersion\x125.google.cloud.secrets.v1beta1.GetSecretVersionRequest\x1a+.google.cloud.secrets.v1beta1.SecretVersion">\xdaA\x04name\x82\xd3\xe4\x93\x021\x12//v1beta1/{name=projects/*/secrets/*/versions/*}\x12\xd1\x01\n\x13AccessSecretVersion\x128.google.cloud.secrets.v1beta1.AccessSecretVersionRequest\x1a9.google.cloud.secrets.v1beta1.AccessSecretVersionResponse"E\xdaA\x04name\x82\xd3\xe4\x93\x028\x126/v1beta1/{name=projects/*/secrets/*/versions/*}:access\x12\xc9\x01\n\x14DisableSecretVersion\x129.google.cloud.secrets.v1beta1.DisableSecretVersionRequest\x1a+.google.cloud.secrets.v1beta1.SecretVersion"I\xdaA\x04name\x82\xd3\xe4\x93\x02<"7/v1beta1/{name=projects/*/secrets/*/versions/*}:disable:\x01*\x12\xc6\x01\n\x13EnableSecretVersion\x128.google.cloud.secrets.v1beta1.EnableSecretVersionRequest\x1a+.google.cloud.secrets.v1beta1.SecretVersion"H\xdaA\x04name\x82\xd3\xe4\x93\x02;"6/v1beta1/{name=projects/*/secrets/*/versions/*}:enable:\x01*\x12\xc9\x01\n\x14DestroySecretVersion\x129.google.cloud.secrets.v1beta1.DestroySecretVersionRequest\x1a+.google.cloud.secrets.v1beta1.SecretVersion"I\xdaA\x04name\x82\xd3\xe4\x93\x02<"7/v1beta1/{name=projects/*/secrets/*/versions/*}:destroy:\x01*\x12\x8b\x01\n\x0cSetIamPolicy\x12".google.iam.v1.SetIamPolicyRequest\x1a\x15.google.iam.v1.Policy"@\x82\xd3\xe4\x93\x02:"5/v1beta1/{resource=projects/*/secrets/*}:setIamPolicy:\x01*\x12\x88\x01\n\x0cGetIamPolicy\x12".google.iam.v1.GetIamPolicyRequest\x1a\x15.google.iam.v1.Policy"=\x82\xd3\xe4\x93\x027\x125/v1beta1/{resource=projects/*/secrets/*}:getIamPolicy\x12\xb1\x01\n\x12TestIamPermissions\x12(.google.iam.v1.TestIamPermissionsRequest\x1a).google.iam.v1.TestIamPermissionsResponse"F\x82\xd3\xe4\x93\x02@";/v1beta1/{resource=projects/*/secrets/*}:testIamPermissions:\x01*\x1aP\xcaA\x1csecretmanager.googleapis.com\xd2A.https://www.googleapis.com/auth/cloud-platformB\xef\x01\n&com.google.cloud.secretmanager.v1beta1B\x0cServiceProtoP\x01Z:cloud.google.com/go/secrets/apiv1beta1/secretspb;secretspb\xf8\x01\x01\xa2\x02\x03GSM\xaa\x02"Google.Cloud.SecretManager.V1Beta1\xca\x02"Google\\Cloud\\SecretManager\\V1beta1\xea\x02%Google::Cloud::SecretManager::V1beta1b\x06proto3')
_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'google.cloud.secrets.v1beta1.service_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
    _globals['DESCRIPTOR']._loaded_options = None
    _globals['DESCRIPTOR']._serialized_options = b'\n&com.google.cloud.secretmanager.v1beta1B\x0cServiceProtoP\x01Z:cloud.google.com/go/secrets/apiv1beta1/secretspb;secretspb\xf8\x01\x01\xa2\x02\x03GSM\xaa\x02"Google.Cloud.SecretManager.V1Beta1\xca\x02"Google\\Cloud\\SecretManager\\V1beta1\xea\x02%Google::Cloud::SecretManager::V1beta1'
    _globals['_LISTSECRETSREQUEST'].fields_by_name['parent']._loaded_options = None
    _globals['_LISTSECRETSREQUEST'].fields_by_name['parent']._serialized_options = b'\xe0A\x02\xfaA-\n+cloudresourcemanager.googleapis.com/Project'
    _globals['_LISTSECRETSREQUEST'].fields_by_name['page_size']._loaded_options = None
    _globals['_LISTSECRETSREQUEST'].fields_by_name['page_size']._serialized_options = b'\xe0A\x01'
    _globals['_LISTSECRETSREQUEST'].fields_by_name['page_token']._loaded_options = None
    _globals['_LISTSECRETSREQUEST'].fields_by_name['page_token']._serialized_options = b'\xe0A\x01'
    _globals['_CREATESECRETREQUEST'].fields_by_name['parent']._loaded_options = None
    _globals['_CREATESECRETREQUEST'].fields_by_name['parent']._serialized_options = b'\xe0A\x02\xfaA-\n+cloudresourcemanager.googleapis.com/Project'
    _globals['_CREATESECRETREQUEST'].fields_by_name['secret_id']._loaded_options = None
    _globals['_CREATESECRETREQUEST'].fields_by_name['secret_id']._serialized_options = b'\xe0A\x02'
    _globals['_CREATESECRETREQUEST'].fields_by_name['secret']._loaded_options = None
    _globals['_CREATESECRETREQUEST'].fields_by_name['secret']._serialized_options = b'\xe0A\x02'
    _globals['_ADDSECRETVERSIONREQUEST'].fields_by_name['parent']._loaded_options = None
    _globals['_ADDSECRETVERSIONREQUEST'].fields_by_name['parent']._serialized_options = b'\xe0A\x02\xfaA%\n#secretmanager.googleapis.com/Secret'
    _globals['_ADDSECRETVERSIONREQUEST'].fields_by_name['payload']._loaded_options = None
    _globals['_ADDSECRETVERSIONREQUEST'].fields_by_name['payload']._serialized_options = b'\xe0A\x02'
    _globals['_GETSECRETREQUEST'].fields_by_name['name']._loaded_options = None
    _globals['_GETSECRETREQUEST'].fields_by_name['name']._serialized_options = b'\xe0A\x02\xfaA%\n#secretmanager.googleapis.com/Secret'
    _globals['_LISTSECRETVERSIONSREQUEST'].fields_by_name['parent']._loaded_options = None
    _globals['_LISTSECRETVERSIONSREQUEST'].fields_by_name['parent']._serialized_options = b'\xe0A\x02\xfaA%\n#secretmanager.googleapis.com/Secret'
    _globals['_LISTSECRETVERSIONSREQUEST'].fields_by_name['page_size']._loaded_options = None
    _globals['_LISTSECRETVERSIONSREQUEST'].fields_by_name['page_size']._serialized_options = b'\xe0A\x01'
    _globals['_LISTSECRETVERSIONSREQUEST'].fields_by_name['page_token']._loaded_options = None
    _globals['_LISTSECRETVERSIONSREQUEST'].fields_by_name['page_token']._serialized_options = b'\xe0A\x01'
    _globals['_GETSECRETVERSIONREQUEST'].fields_by_name['name']._loaded_options = None
    _globals['_GETSECRETVERSIONREQUEST'].fields_by_name['name']._serialized_options = b'\xe0A\x02\xfaA,\n*secretmanager.googleapis.com/SecretVersion'
    _globals['_UPDATESECRETREQUEST'].fields_by_name['secret']._loaded_options = None
    _globals['_UPDATESECRETREQUEST'].fields_by_name['secret']._serialized_options = b'\xe0A\x02'
    _globals['_UPDATESECRETREQUEST'].fields_by_name['update_mask']._loaded_options = None
    _globals['_UPDATESECRETREQUEST'].fields_by_name['update_mask']._serialized_options = b'\xe0A\x02'
    _globals['_ACCESSSECRETVERSIONREQUEST'].fields_by_name['name']._loaded_options = None
    _globals['_ACCESSSECRETVERSIONREQUEST'].fields_by_name['name']._serialized_options = b'\xe0A\x02\xfaA,\n*secretmanager.googleapis.com/SecretVersion'
    _globals['_ACCESSSECRETVERSIONRESPONSE'].fields_by_name['name']._loaded_options = None
    _globals['_ACCESSSECRETVERSIONRESPONSE'].fields_by_name['name']._serialized_options = b'\xfaA,\n*secretmanager.googleapis.com/SecretVersion'
    _globals['_DELETESECRETREQUEST'].fields_by_name['name']._loaded_options = None
    _globals['_DELETESECRETREQUEST'].fields_by_name['name']._serialized_options = b'\xe0A\x02\xfaA%\n#secretmanager.googleapis.com/Secret'
    _globals['_DISABLESECRETVERSIONREQUEST'].fields_by_name['name']._loaded_options = None
    _globals['_DISABLESECRETVERSIONREQUEST'].fields_by_name['name']._serialized_options = b'\xe0A\x02\xfaA,\n*secretmanager.googleapis.com/SecretVersion'
    _globals['_ENABLESECRETVERSIONREQUEST'].fields_by_name['name']._loaded_options = None
    _globals['_ENABLESECRETVERSIONREQUEST'].fields_by_name['name']._serialized_options = b'\xe0A\x02\xfaA,\n*secretmanager.googleapis.com/SecretVersion'
    _globals['_DESTROYSECRETVERSIONREQUEST'].fields_by_name['name']._loaded_options = None
    _globals['_DESTROYSECRETVERSIONREQUEST'].fields_by_name['name']._serialized_options = b'\xe0A\x02\xfaA,\n*secretmanager.googleapis.com/SecretVersion'
    _globals['_SECRETMANAGERSERVICE']._loaded_options = None
    _globals['_SECRETMANAGERSERVICE']._serialized_options = b'\xcaA\x1csecretmanager.googleapis.com\xd2A.https://www.googleapis.com/auth/cloud-platform'
    _globals['_SECRETMANAGERSERVICE'].methods_by_name['ListSecrets']._loaded_options = None
    _globals['_SECRETMANAGERSERVICE'].methods_by_name['ListSecrets']._serialized_options = b'\xdaA\x06parent\x82\xd3\xe4\x93\x02&\x12$/v1beta1/{parent=projects/*}/secrets'
    _globals['_SECRETMANAGERSERVICE'].methods_by_name['CreateSecret']._loaded_options = None
    _globals['_SECRETMANAGERSERVICE'].methods_by_name['CreateSecret']._serialized_options = b'\xdaA\x17parent,secret_id,secret\x82\xd3\xe4\x93\x02."$/v1beta1/{parent=projects/*}/secrets:\x06secret'
    _globals['_SECRETMANAGERSERVICE'].methods_by_name['AddSecretVersion']._loaded_options = None
    _globals['_SECRETMANAGERSERVICE'].methods_by_name['AddSecretVersion']._serialized_options = b'\xdaA\x0eparent,payload\x82\xd3\xe4\x93\x026"1/v1beta1/{parent=projects/*/secrets/*}:addVersion:\x01*'
    _globals['_SECRETMANAGERSERVICE'].methods_by_name['GetSecret']._loaded_options = None
    _globals['_SECRETMANAGERSERVICE'].methods_by_name['GetSecret']._serialized_options = b'\xdaA\x04name\x82\xd3\xe4\x93\x02&\x12$/v1beta1/{name=projects/*/secrets/*}'
    _globals['_SECRETMANAGERSERVICE'].methods_by_name['UpdateSecret']._loaded_options = None
    _globals['_SECRETMANAGERSERVICE'].methods_by_name['UpdateSecret']._serialized_options = b'\xdaA\x12secret,update_mask\x82\xd3\xe4\x93\x0252+/v1beta1/{secret.name=projects/*/secrets/*}:\x06secret'
    _globals['_SECRETMANAGERSERVICE'].methods_by_name['DeleteSecret']._loaded_options = None
    _globals['_SECRETMANAGERSERVICE'].methods_by_name['DeleteSecret']._serialized_options = b'\xdaA\x04name\x82\xd3\xe4\x93\x02&*$/v1beta1/{name=projects/*/secrets/*}'
    _globals['_SECRETMANAGERSERVICE'].methods_by_name['ListSecretVersions']._loaded_options = None
    _globals['_SECRETMANAGERSERVICE'].methods_by_name['ListSecretVersions']._serialized_options = b'\xdaA\x06parent\x82\xd3\xe4\x93\x021\x12//v1beta1/{parent=projects/*/secrets/*}/versions'
    _globals['_SECRETMANAGERSERVICE'].methods_by_name['GetSecretVersion']._loaded_options = None
    _globals['_SECRETMANAGERSERVICE'].methods_by_name['GetSecretVersion']._serialized_options = b'\xdaA\x04name\x82\xd3\xe4\x93\x021\x12//v1beta1/{name=projects/*/secrets/*/versions/*}'
    _globals['_SECRETMANAGERSERVICE'].methods_by_name['AccessSecretVersion']._loaded_options = None
    _globals['_SECRETMANAGERSERVICE'].methods_by_name['AccessSecretVersion']._serialized_options = b'\xdaA\x04name\x82\xd3\xe4\x93\x028\x126/v1beta1/{name=projects/*/secrets/*/versions/*}:access'
    _globals['_SECRETMANAGERSERVICE'].methods_by_name['DisableSecretVersion']._loaded_options = None
    _globals['_SECRETMANAGERSERVICE'].methods_by_name['DisableSecretVersion']._serialized_options = b'\xdaA\x04name\x82\xd3\xe4\x93\x02<"7/v1beta1/{name=projects/*/secrets/*/versions/*}:disable:\x01*'
    _globals['_SECRETMANAGERSERVICE'].methods_by_name['EnableSecretVersion']._loaded_options = None
    _globals['_SECRETMANAGERSERVICE'].methods_by_name['EnableSecretVersion']._serialized_options = b'\xdaA\x04name\x82\xd3\xe4\x93\x02;"6/v1beta1/{name=projects/*/secrets/*/versions/*}:enable:\x01*'
    _globals['_SECRETMANAGERSERVICE'].methods_by_name['DestroySecretVersion']._loaded_options = None
    _globals['_SECRETMANAGERSERVICE'].methods_by_name['DestroySecretVersion']._serialized_options = b'\xdaA\x04name\x82\xd3\xe4\x93\x02<"7/v1beta1/{name=projects/*/secrets/*/versions/*}:destroy:\x01*'
    _globals['_SECRETMANAGERSERVICE'].methods_by_name['SetIamPolicy']._loaded_options = None
    _globals['_SECRETMANAGERSERVICE'].methods_by_name['SetIamPolicy']._serialized_options = b'\x82\xd3\xe4\x93\x02:"5/v1beta1/{resource=projects/*/secrets/*}:setIamPolicy:\x01*'
    _globals['_SECRETMANAGERSERVICE'].methods_by_name['GetIamPolicy']._loaded_options = None
    _globals['_SECRETMANAGERSERVICE'].methods_by_name['GetIamPolicy']._serialized_options = b'\x82\xd3\xe4\x93\x027\x125/v1beta1/{resource=projects/*/secrets/*}:getIamPolicy'
    _globals['_SECRETMANAGERSERVICE'].methods_by_name['TestIamPermissions']._loaded_options = None
    _globals['_SECRETMANAGERSERVICE'].methods_by_name['TestIamPermissions']._serialized_options = b'\x82\xd3\xe4\x93\x02@";/v1beta1/{resource=projects/*/secrets/*}:testIamPermissions:\x01*'
    _globals['_LISTSECRETSREQUEST']._serialized_start = 361
    _globals['_LISTSECRETSREQUEST']._serialized_end = 499
    _globals['_LISTSECRETSRESPONSE']._serialized_start = 501
    _globals['_LISTSECRETSRESPONSE']._serialized_end = 622
    _globals['_CREATESECRETREQUEST']._serialized_start = 625
    _globals['_CREATESECRETREQUEST']._serialized_end = 798
    _globals['_ADDSECRETVERSIONREQUEST']._serialized_start = 801
    _globals['_ADDSECRETVERSIONREQUEST']._serialized_end = 954
    _globals['_GETSECRETREQUEST']._serialized_start = 956
    _globals['_GETSECRETREQUEST']._serialized_end = 1033
    _globals['_LISTSECRETVERSIONSREQUEST']._serialized_start = 1036
    _globals['_LISTSECRETVERSIONSREQUEST']._serialized_end = 1173
    _globals['_LISTSECRETVERSIONSRESPONSE']._serialized_start = 1176
    _globals['_LISTSECRETVERSIONSRESPONSE']._serialized_end = 1312
    _globals['_GETSECRETVERSIONREQUEST']._serialized_start = 1314
    _globals['_GETSECRETVERSIONREQUEST']._serialized_end = 1405
    _globals['_UPDATESECRETREQUEST']._serialized_start = 1408
    _globals['_UPDATESECRETREQUEST']._serialized_end = 1542
    _globals['_ACCESSSECRETVERSIONREQUEST']._serialized_start = 1544
    _globals['_ACCESSSECRETVERSIONREQUEST']._serialized_end = 1638
    _globals['_ACCESSSECRETVERSIONRESPONSE']._serialized_start = 1641
    _globals['_ACCESSSECRETVERSIONRESPONSE']._serialized_end = 1795
    _globals['_DELETESECRETREQUEST']._serialized_start = 1797
    _globals['_DELETESECRETREQUEST']._serialized_end = 1877
    _globals['_DISABLESECRETVERSIONREQUEST']._serialized_start = 1879
    _globals['_DISABLESECRETVERSIONREQUEST']._serialized_end = 1974
    _globals['_ENABLESECRETVERSIONREQUEST']._serialized_start = 1976
    _globals['_ENABLESECRETVERSIONREQUEST']._serialized_end = 2070
    _globals['_DESTROYSECRETVERSIONREQUEST']._serialized_start = 2072
    _globals['_DESTROYSECRETVERSIONREQUEST']._serialized_end = 2167
    _globals['_SECRETMANAGERSERVICE']._serialized_start = 2170
    _globals['_SECRETMANAGERSERVICE']._serialized_end = 4989