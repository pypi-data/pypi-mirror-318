"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_runtime_version.ValidateProtobufRuntimeVersion(_runtime_version.Domain.PUBLIC, 5, 28, 1, '', 'google/cloud/securitycenter/v2/resource.proto')
_sym_db = _symbol_database.Default()
from .....google.api import field_behavior_pb2 as google_dot_api_dot_field__behavior__pb2
from .....google.cloud.securitycenter.v2 import folder_pb2 as google_dot_cloud_dot_securitycenter_dot_v2_dot_folder__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n-google/cloud/securitycenter/v2/resource.proto\x12\x1egoogle.cloud.securitycenter.v2\x1a\x1fgoogle/api/field_behavior.proto\x1a+google/cloud/securitycenter/v2/folder.proto"\xf7\x03\n\x08Resource\x12\x0c\n\x04name\x18\x01 \x01(\t\x12\x14\n\x0cdisplay_name\x18\x02 \x01(\t\x12\x0c\n\x04type\x18\x03 \x01(\t\x12E\n\x0ecloud_provider\x18\x04 \x01(\x0e2-.google.cloud.securitycenter.v2.CloudProvider\x12\x0f\n\x07service\x18\x05 \x01(\t\x12\x10\n\x08location\x18\x06 \x01(\t\x12C\n\x0cgcp_metadata\x18\x07 \x01(\x0b2+.google.cloud.securitycenter.v2.GcpMetadataH\x00\x12C\n\x0caws_metadata\x18\x08 \x01(\x0b2+.google.cloud.securitycenter.v2.AwsMetadataH\x00\x12G\n\x0eazure_metadata\x18\t \x01(\x0b2-.google.cloud.securitycenter.v2.AzureMetadataH\x00\x12C\n\rresource_path\x18\n \x01(\x0b2,.google.cloud.securitycenter.v2.ResourcePath\x12\x1c\n\x14resource_path_string\x18\x0b \x01(\tB\x19\n\x17cloud_provider_metadata"\xbd\x01\n\x0bGcpMetadata\x12\x0f\n\x07project\x18\x01 \x01(\t\x12\x1c\n\x14project_display_name\x18\x02 \x01(\t\x12\x0e\n\x06parent\x18\x03 \x01(\t\x12\x1b\n\x13parent_display_name\x18\x04 \x01(\t\x12<\n\x07folders\x18\x05 \x03(\x0b2&.google.cloud.securitycenter.v2.FolderB\x03\xe0A\x03\x12\x14\n\x0corganization\x18\x06 \x01(\t"\x84\x03\n\x0bAwsMetadata\x12Q\n\x0corganization\x18\x01 \x01(\x0b2;.google.cloud.securitycenter.v2.AwsMetadata.AwsOrganization\x12_\n\x14organizational_units\x18\x02 \x03(\x0b2A.google.cloud.securitycenter.v2.AwsMetadata.AwsOrganizationalUnit\x12G\n\x07account\x18\x03 \x01(\x0b26.google.cloud.securitycenter.v2.AwsMetadata.AwsAccount\x1a\x1d\n\x0fAwsOrganization\x12\n\n\x02id\x18\x01 \x01(\t\x1a1\n\x15AwsOrganizationalUnit\x12\n\n\x02id\x18\x01 \x01(\t\x12\x0c\n\x04name\x18\x02 \x01(\t\x1a&\n\nAwsAccount\x12\n\n\x02id\x18\x01 \x01(\t\x12\x0c\n\x04name\x18\x02 \x01(\t"\xb4\x03\n\rAzureMetadata\x12]\n\x11management_groups\x18\x01 \x03(\x0b2B.google.cloud.securitycenter.v2.AzureMetadata.AzureManagementGroup\x12U\n\x0csubscription\x18\x02 \x01(\x0b2?.google.cloud.securitycenter.v2.AzureMetadata.AzureSubscription\x12X\n\x0eresource_group\x18\x03 \x01(\x0b2@.google.cloud.securitycenter.v2.AzureMetadata.AzureResourceGroup\x1a8\n\x14AzureManagementGroup\x12\n\n\x02id\x18\x01 \x01(\t\x12\x14\n\x0cdisplay_name\x18\x02 \x01(\t\x1a5\n\x11AzureSubscription\x12\n\n\x02id\x18\x01 \x01(\t\x12\x14\n\x0cdisplay_name\x18\x02 \x01(\t\x1a"\n\x12AzureResourceGroup\x12\x0c\n\x04name\x18\x01 \x01(\t"\xf4\x03\n\x0cResourcePath\x12L\n\x05nodes\x18\x01 \x03(\x0b2=.google.cloud.securitycenter.v2.ResourcePath.ResourcePathNode\x1a\x8a\x01\n\x10ResourcePathNode\x12T\n\tnode_type\x18\x01 \x01(\x0e2A.google.cloud.securitycenter.v2.ResourcePath.ResourcePathNodeType\x12\n\n\x02id\x18\x02 \x01(\t\x12\x14\n\x0cdisplay_name\x18\x03 \x01(\t"\x88\x02\n\x14ResourcePathNodeType\x12\'\n#RESOURCE_PATH_NODE_TYPE_UNSPECIFIED\x10\x00\x12\x14\n\x10GCP_ORGANIZATION\x10\x01\x12\x0e\n\nGCP_FOLDER\x10\x02\x12\x0f\n\x0bGCP_PROJECT\x10\x03\x12\x14\n\x10AWS_ORGANIZATION\x10\x04\x12\x1b\n\x17AWS_ORGANIZATIONAL_UNIT\x10\x05\x12\x0f\n\x0bAWS_ACCOUNT\x10\x06\x12\x1a\n\x16AZURE_MANAGEMENT_GROUP\x10\x07\x12\x16\n\x12AZURE_SUBSCRIPTION\x10\x08\x12\x18\n\x14AZURE_RESOURCE_GROUP\x10\t*x\n\rCloudProvider\x12\x1e\n\x1aCLOUD_PROVIDER_UNSPECIFIED\x10\x00\x12\x19\n\x15GOOGLE_CLOUD_PLATFORM\x10\x01\x12\x17\n\x13AMAZON_WEB_SERVICES\x10\x02\x12\x13\n\x0fMICROSOFT_AZURE\x10\x03B\xe7\x01\n"com.google.cloud.securitycenter.v2B\rResourceProtoP\x01ZJcloud.google.com/go/securitycenter/apiv2/securitycenterpb;securitycenterpb\xaa\x02\x1eGoogle.Cloud.SecurityCenter.V2\xca\x02\x1eGoogle\\Cloud\\SecurityCenter\\V2\xea\x02!Google::Cloud::SecurityCenter::V2b\x06proto3')
_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'google.cloud.securitycenter.v2.resource_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
    _globals['DESCRIPTOR']._loaded_options = None
    _globals['DESCRIPTOR']._serialized_options = b'\n"com.google.cloud.securitycenter.v2B\rResourceProtoP\x01ZJcloud.google.com/go/securitycenter/apiv2/securitycenterpb;securitycenterpb\xaa\x02\x1eGoogle.Cloud.SecurityCenter.V2\xca\x02\x1eGoogle\\Cloud\\SecurityCenter\\V2\xea\x02!Google::Cloud::SecurityCenter::V2'
    _globals['_GCPMETADATA'].fields_by_name['folders']._loaded_options = None
    _globals['_GCPMETADATA'].fields_by_name['folders']._serialized_options = b'\xe0A\x03'
    _globals['_CLOUDPROVIDER']._serialized_start = 2190
    _globals['_CLOUDPROVIDER']._serialized_end = 2310
    _globals['_RESOURCE']._serialized_start = 160
    _globals['_RESOURCE']._serialized_end = 663
    _globals['_GCPMETADATA']._serialized_start = 666
    _globals['_GCPMETADATA']._serialized_end = 855
    _globals['_AWSMETADATA']._serialized_start = 858
    _globals['_AWSMETADATA']._serialized_end = 1246
    _globals['_AWSMETADATA_AWSORGANIZATION']._serialized_start = 1126
    _globals['_AWSMETADATA_AWSORGANIZATION']._serialized_end = 1155
    _globals['_AWSMETADATA_AWSORGANIZATIONALUNIT']._serialized_start = 1157
    _globals['_AWSMETADATA_AWSORGANIZATIONALUNIT']._serialized_end = 1206
    _globals['_AWSMETADATA_AWSACCOUNT']._serialized_start = 1208
    _globals['_AWSMETADATA_AWSACCOUNT']._serialized_end = 1246
    _globals['_AZUREMETADATA']._serialized_start = 1249
    _globals['_AZUREMETADATA']._serialized_end = 1685
    _globals['_AZUREMETADATA_AZUREMANAGEMENTGROUP']._serialized_start = 1538
    _globals['_AZUREMETADATA_AZUREMANAGEMENTGROUP']._serialized_end = 1594
    _globals['_AZUREMETADATA_AZURESUBSCRIPTION']._serialized_start = 1596
    _globals['_AZUREMETADATA_AZURESUBSCRIPTION']._serialized_end = 1649
    _globals['_AZUREMETADATA_AZURERESOURCEGROUP']._serialized_start = 1651
    _globals['_AZUREMETADATA_AZURERESOURCEGROUP']._serialized_end = 1685
    _globals['_RESOURCEPATH']._serialized_start = 1688
    _globals['_RESOURCEPATH']._serialized_end = 2188
    _globals['_RESOURCEPATH_RESOURCEPATHNODE']._serialized_start = 1783
    _globals['_RESOURCEPATH_RESOURCEPATHNODE']._serialized_end = 1921
    _globals['_RESOURCEPATH_RESOURCEPATHNODETYPE']._serialized_start = 1924
    _globals['_RESOURCEPATH_RESOURCEPATHNODETYPE']._serialized_end = 2188