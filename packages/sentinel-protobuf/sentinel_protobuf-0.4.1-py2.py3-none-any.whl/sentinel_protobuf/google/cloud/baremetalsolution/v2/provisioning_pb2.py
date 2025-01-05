"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_runtime_version.ValidateProtobufRuntimeVersion(_runtime_version.Domain.PUBLIC, 5, 28, 1, '', 'google/cloud/baremetalsolution/v2/provisioning.proto')
_sym_db = _symbol_database.Default()
from .....google.api import field_behavior_pb2 as google_dot_api_dot_field__behavior__pb2
from .....google.api import resource_pb2 as google_dot_api_dot_resource__pb2
from .....google.cloud.baremetalsolution.v2 import common_pb2 as google_dot_cloud_dot_baremetalsolution_dot_v2_dot_common__pb2
from .....google.cloud.baremetalsolution.v2 import network_pb2 as google_dot_cloud_dot_baremetalsolution_dot_v2_dot_network__pb2
from google.protobuf import field_mask_pb2 as google_dot_protobuf_dot_field__mask__pb2
from google.protobuf import timestamp_pb2 as google_dot_protobuf_dot_timestamp__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n4google/cloud/baremetalsolution/v2/provisioning.proto\x12!google.cloud.baremetalsolution.v2\x1a\x1fgoogle/api/field_behavior.proto\x1a\x19google/api/resource.proto\x1a.google/cloud/baremetalsolution/v2/common.proto\x1a/google/cloud/baremetalsolution/v2/network.proto\x1a google/protobuf/field_mask.proto\x1a\x1fgoogle/protobuf/timestamp.proto"\xd8\x06\n\x12ProvisioningConfig\x12\x11\n\x04name\x18\x01 \x01(\tB\x03\xe0A\x03\x12D\n\tinstances\x18\x02 \x03(\x0b21.google.cloud.baremetalsolution.v2.InstanceConfig\x12B\n\x08networks\x18\x03 \x03(\x0b20.google.cloud.baremetalsolution.v2.NetworkConfig\x12@\n\x07volumes\x18\x04 \x03(\x0b2/.google.cloud.baremetalsolution.v2.VolumeConfig\x12\x11\n\tticket_id\x18\x05 \x01(\t\x12 \n\x18handover_service_account\x18\x06 \x01(\t\x12\x11\n\x05email\x18\x07 \x01(\tB\x02\x18\x01\x12O\n\x05state\x18\x08 \x01(\x0e2;.google.cloud.baremetalsolution.v2.ProvisioningConfig.StateB\x03\xe0A\x03\x12\x15\n\x08location\x18\t \x01(\tB\x03\xe0A\x01\x124\n\x0bupdate_time\x18\n \x01(\x0b2\x1a.google.protobuf.TimestampB\x03\xe0A\x03\x12\x1e\n\x11cloud_console_uri\x18\x0b \x01(\tB\x03\xe0A\x03\x12\x16\n\x0evpc_sc_enabled\x18\x0c \x01(\x08\x12\x16\n\x0estatus_message\x18\r \x01(\t\x12\x16\n\tcustom_id\x18\x0e \x01(\tB\x03\xe0A\x01"\x85\x01\n\x05State\x12\x15\n\x11STATE_UNSPECIFIED\x10\x00\x12\t\n\x05DRAFT\x10\x01\x12\r\n\tSUBMITTED\x10\x02\x12\x10\n\x0cPROVISIONING\x10\x03\x12\x0f\n\x0bPROVISIONED\x10\x04\x12\r\n\tVALIDATED\x10\x05\x12\r\n\tCANCELLED\x10\x06\x12\n\n\x06FAILED\x10\x07:\x8c\x01\xeaA\x88\x01\n3baremetalsolution.googleapis.com/ProvisioningConfig\x12Qprojects/{project}/locations/{location}/provisioningConfigs/{provisioning_config}"\xc9\x01\n\x1fSubmitProvisioningConfigRequest\x129\n\x06parent\x18\x01 \x01(\tB)\xe0A\x02\xfaA#\n!locations.googleapis.com/Location\x12W\n\x13provisioning_config\x18\x02 \x01(\x0b25.google.cloud.baremetalsolution.v2.ProvisioningConfigB\x03\xe0A\x02\x12\x12\n\x05email\x18\x03 \x01(\tB\x03\xe0A\x01"v\n SubmitProvisioningConfigResponse\x12R\n\x13provisioning_config\x18\x01 \x01(\x0b25.google.cloud.baremetalsolution.v2.ProvisioningConfig"\xe7\x04\n\x11ProvisioningQuota\x12\x11\n\x04name\x18\x01 \x01(\tB\x03\xe0A\x03\x12R\n\nasset_type\x18\x02 \x01(\x0e2>.google.cloud.baremetalsolution.v2.ProvisioningQuota.AssetType\x12\x13\n\x0bgcp_service\x18\x03 \x01(\t\x12\x10\n\x08location\x18\x04 \x01(\t\x12\x17\n\x0favailable_count\x18\x05 \x01(\x05\x12J\n\x0einstance_quota\x18\x06 \x01(\x0b20.google.cloud.baremetalsolution.v2.InstanceQuotaH\x00\x12\x16\n\x0cserver_count\x18\x07 \x01(\x03H\x01\x12\x1b\n\x11network_bandwidth\x18\x08 \x01(\x03H\x01\x12\x15\n\x0bstorage_gib\x18\t \x01(\x03H\x01"n\n\tAssetType\x12\x1a\n\x16ASSET_TYPE_UNSPECIFIED\x10\x00\x12\x15\n\x11ASSET_TYPE_SERVER\x10\x01\x12\x16\n\x12ASSET_TYPE_STORAGE\x10\x02\x12\x16\n\x12ASSET_TYPE_NETWORK\x10\x03:\x89\x01\xeaA\x85\x01\n2baremetalsolution.googleapis.com/ProvisioningQuota\x12Oprojects/{project}/locations/{location}/provisioningQuotas/{provisioning_quota}B\x07\n\x05quotaB\x0e\n\x0cavailability"\x81\x01\n\x1dListProvisioningQuotasRequest\x129\n\x06parent\x18\x01 \x01(\tB)\xe0A\x02\xfaA#\n!locations.googleapis.com/Location\x12\x11\n\tpage_size\x18\x02 \x01(\x05\x12\x12\n\npage_token\x18\x03 \x01(\t"\x8c\x01\n\x1eListProvisioningQuotasResponse\x12Q\n\x13provisioning_quotas\x18\x01 \x03(\x0b24.google.cloud.baremetalsolution.v2.ProvisioningQuota\x12\x17\n\x0fnext_page_token\x18\x02 \x01(\t"\xe3\x06\n\x0eInstanceConfig\x12\x11\n\x04name\x18\x01 \x01(\tB\x03\xe0A\x03\x12\n\n\x02id\x18\x02 \x01(\t\x12\x15\n\rinstance_type\x18\x03 \x01(\t\x12\x16\n\x0ehyperthreading\x18\x04 \x01(\x08\x12\x10\n\x08os_image\x18\x05 \x01(\t\x12\\\n\x0eclient_network\x18\x06 \x01(\x0b2@.google.cloud.baremetalsolution.v2.InstanceConfig.NetworkAddressB\x02\x18\x01\x12]\n\x0fprivate_network\x18\x07 \x01(\x0b2@.google.cloud.baremetalsolution.v2.InstanceConfig.NetworkAddressB\x02\x18\x01\x12\x11\n\tuser_note\x18\x08 \x01(\t\x12 \n\x18account_networks_enabled\x18\t \x01(\x08\x12W\n\x0enetwork_config\x18\n \x01(\x0e2?.google.cloud.baremetalsolution.v2.InstanceConfig.NetworkConfig\x12\x18\n\x10network_template\x18\x0b \x01(\t\x12O\n\x12logical_interfaces\x18\x0c \x03(\x0b23.google.cloud.baremetalsolution.v2.LogicalInterface\x12\x15\n\rssh_key_names\x18\r \x03(\t\x1aR\n\x0eNetworkAddress\x12\x12\n\nnetwork_id\x18\x01 \x01(\t\x12\x0f\n\x07address\x18\x02 \x01(\t\x12\x1b\n\x13existing_network_id\x18\x03 \x01(\t"O\n\rNetworkConfig\x12\x1d\n\x19NETWORKCONFIG_UNSPECIFIED\x10\x00\x12\x0f\n\x0bSINGLE_VLAN\x10\x01\x12\x0e\n\nMULTI_VLAN\x10\x02:\x7f\xeaA|\n/baremetalsolution.googleapis.com/InstanceConfig\x12Iprojects/{project}/locations/{location}/instanceConfigs/{instance_config}"\xf6\x08\n\x0cVolumeConfig\x12\x11\n\x04name\x18\x01 \x01(\tB\x03\xe0A\x03\x12\n\n\x02id\x18\x02 \x01(\t\x12\x19\n\x11snapshots_enabled\x18\x03 \x01(\x08\x12B\n\x04type\x18\x04 \x01(\x0e24.google.cloud.baremetalsolution.v2.VolumeConfig.Type\x12J\n\x08protocol\x18\x05 \x01(\x0e28.google.cloud.baremetalsolution.v2.VolumeConfig.Protocol\x12\x0f\n\x07size_gb\x18\x06 \x01(\x05\x12L\n\nlun_ranges\x18\x07 \x03(\x0b28.google.cloud.baremetalsolution.v2.VolumeConfig.LunRange\x12\x13\n\x0bmachine_ids\x18\x08 \x03(\t\x12N\n\x0bnfs_exports\x18\t \x03(\x0b29.google.cloud.baremetalsolution.v2.VolumeConfig.NfsExport\x12\x11\n\tuser_note\x18\n \x01(\t\x12\x13\n\x0bgcp_service\x18\x0b \x01(\t\x12R\n\x10performance_tier\x18\x0c \x01(\x0e28.google.cloud.baremetalsolution.v2.VolumePerformanceTier\x1a-\n\x08LunRange\x12\x10\n\x08quantity\x18\x01 \x01(\x05\x12\x0f\n\x07size_gb\x18\x02 \x01(\x05\x1a\xb5\x02\n\tNfsExport\x12\x12\n\nnetwork_id\x18\x01 \x01(\t\x12\x14\n\nmachine_id\x18\x02 \x01(\tH\x00\x12\x0e\n\x04cidr\x18\x03 \x01(\tH\x00\x12Z\n\x0bpermissions\x18\x04 \x01(\x0e2E.google.cloud.baremetalsolution.v2.VolumeConfig.NfsExport.Permissions\x12\x16\n\x0eno_root_squash\x18\x05 \x01(\x08\x12\x12\n\nallow_suid\x18\x06 \x01(\x08\x12\x11\n\tallow_dev\x18\x07 \x01(\x08"I\n\x0bPermissions\x12\x1b\n\x17PERMISSIONS_UNSPECIFIED\x10\x00\x12\r\n\tREAD_ONLY\x10\x01\x12\x0e\n\nREAD_WRITE\x10\x02B\x08\n\x06client"1\n\x04Type\x12\x14\n\x10TYPE_UNSPECIFIED\x10\x00\x12\t\n\x05FLASH\x10\x01\x12\x08\n\x04DISK\x10\x02"G\n\x08Protocol\x12\x18\n\x14PROTOCOL_UNSPECIFIED\x10\x00\x12\x0f\n\x0bPROTOCOL_FC\x10\x01\x12\x10\n\x0cPROTOCOL_NFS\x10\x02:y\xeaAv\n-baremetalsolution.googleapis.com/VolumeConfig\x12Eprojects/{project}/locations/{location}/volumeConfigs/{volume_config}"\x9b\x07\n\rNetworkConfig\x12\x11\n\x04name\x18\x01 \x01(\tB\x03\xe0A\x03\x12\n\n\x02id\x18\x02 \x01(\t\x12C\n\x04type\x18\x03 \x01(\x0e25.google.cloud.baremetalsolution.v2.NetworkConfig.Type\x12M\n\tbandwidth\x18\x04 \x01(\x0e2:.google.cloud.baremetalsolution.v2.NetworkConfig.Bandwidth\x12_\n\x10vlan_attachments\x18\x05 \x03(\x0b2E.google.cloud.baremetalsolution.v2.NetworkConfig.IntakeVlanAttachment\x12\x0c\n\x04cidr\x18\x06 \x01(\t\x12R\n\x0cservice_cidr\x18\x07 \x01(\x0e2<.google.cloud.baremetalsolution.v2.NetworkConfig.ServiceCidr\x12\x11\n\tuser_note\x18\x08 \x01(\t\x12\x13\n\x0bgcp_service\x18\t \x01(\t\x12\x19\n\x11vlan_same_project\x18\n \x01(\x08\x12\x1c\n\x14jumbo_frames_enabled\x18\x0b \x01(\x08\x1a7\n\x14IntakeVlanAttachment\x12\n\n\x02id\x18\x01 \x01(\t\x12\x13\n\x0bpairing_key\x18\x02 \x01(\t"5\n\x04Type\x12\x14\n\x10TYPE_UNSPECIFIED\x10\x00\x12\n\n\x06CLIENT\x10\x01\x12\x0b\n\x07PRIVATE\x10\x02"c\n\tBandwidth\x12\x19\n\x15BANDWIDTH_UNSPECIFIED\x10\x00\x12\r\n\tBW_1_GBPS\x10\x01\x12\r\n\tBW_2_GBPS\x10\x02\x12\r\n\tBW_5_GBPS\x10\x03\x12\x0e\n\nBW_10_GBPS\x10\x04"`\n\x0bServiceCidr\x12\x1c\n\x18SERVICE_CIDR_UNSPECIFIED\x10\x00\x12\x0c\n\x08DISABLED\x10\x01\x12\x0b\n\x07HIGH_26\x10\x02\x12\x0b\n\x07HIGH_27\x10\x03\x12\x0b\n\x07HIGH_28\x10\x04:|\xeaAy\n.baremetalsolution.googleapis.com/NetworkConfig\x12Gprojects/{project}/locations/{location}/networkConfigs/{network_config}"\x83\x02\n\rInstanceQuota\x12\x11\n\x04name\x18\x01 \x01(\tB\x03\xe0A\x03\x12\x19\n\rinstance_type\x18\x02 \x01(\tB\x02\x18\x01\x12\x13\n\x0bgcp_service\x18\x05 \x01(\t\x12\x10\n\x08location\x18\x03 \x01(\t\x12\x1f\n\x17available_machine_count\x18\x04 \x01(\x05:|\xeaAy\n.baremetalsolution.googleapis.com/InstanceQuota\x12Gprojects/{project}/locations/{location}/instanceQuotas/{instance_quota}"i\n\x1cGetProvisioningConfigRequest\x12I\n\x04name\x18\x01 \x01(\tB;\xe0A\x02\xfaA5\n3baremetalsolution.googleapis.com/ProvisioningConfig"\xc9\x01\n\x1fCreateProvisioningConfigRequest\x129\n\x06parent\x18\x01 \x01(\tB)\xe0A\x02\xfaA#\n!locations.googleapis.com/Location\x12W\n\x13provisioning_config\x18\x02 \x01(\x0b25.google.cloud.baremetalsolution.v2.ProvisioningConfigB\x03\xe0A\x02\x12\x12\n\x05email\x18\x03 \x01(\tB\x03\xe0A\x01"\xc4\x01\n\x1fUpdateProvisioningConfigRequest\x12W\n\x13provisioning_config\x18\x01 \x01(\x0b25.google.cloud.baremetalsolution.v2.ProvisioningConfigB\x03\xe0A\x02\x124\n\x0bupdate_mask\x18\x02 \x01(\x0b2\x1a.google.protobuf.FieldMaskB\x03\xe0A\x02\x12\x12\n\x05email\x18\x03 \x01(\tB\x03\xe0A\x01B\x80\x02\n%com.google.cloud.baremetalsolution.v2B\x11ProvisioningProtoP\x01ZScloud.google.com/go/baremetalsolution/apiv2/baremetalsolutionpb;baremetalsolutionpb\xaa\x02!Google.Cloud.BareMetalSolution.V2\xca\x02!Google\\Cloud\\BareMetalSolution\\V2\xea\x02$Google::Cloud::BareMetalSolution::V2b\x06proto3')
_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'google.cloud.baremetalsolution.v2.provisioning_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
    _globals['DESCRIPTOR']._loaded_options = None
    _globals['DESCRIPTOR']._serialized_options = b'\n%com.google.cloud.baremetalsolution.v2B\x11ProvisioningProtoP\x01ZScloud.google.com/go/baremetalsolution/apiv2/baremetalsolutionpb;baremetalsolutionpb\xaa\x02!Google.Cloud.BareMetalSolution.V2\xca\x02!Google\\Cloud\\BareMetalSolution\\V2\xea\x02$Google::Cloud::BareMetalSolution::V2'
    _globals['_PROVISIONINGCONFIG'].fields_by_name['name']._loaded_options = None
    _globals['_PROVISIONINGCONFIG'].fields_by_name['name']._serialized_options = b'\xe0A\x03'
    _globals['_PROVISIONINGCONFIG'].fields_by_name['email']._loaded_options = None
    _globals['_PROVISIONINGCONFIG'].fields_by_name['email']._serialized_options = b'\x18\x01'
    _globals['_PROVISIONINGCONFIG'].fields_by_name['state']._loaded_options = None
    _globals['_PROVISIONINGCONFIG'].fields_by_name['state']._serialized_options = b'\xe0A\x03'
    _globals['_PROVISIONINGCONFIG'].fields_by_name['location']._loaded_options = None
    _globals['_PROVISIONINGCONFIG'].fields_by_name['location']._serialized_options = b'\xe0A\x01'
    _globals['_PROVISIONINGCONFIG'].fields_by_name['update_time']._loaded_options = None
    _globals['_PROVISIONINGCONFIG'].fields_by_name['update_time']._serialized_options = b'\xe0A\x03'
    _globals['_PROVISIONINGCONFIG'].fields_by_name['cloud_console_uri']._loaded_options = None
    _globals['_PROVISIONINGCONFIG'].fields_by_name['cloud_console_uri']._serialized_options = b'\xe0A\x03'
    _globals['_PROVISIONINGCONFIG'].fields_by_name['custom_id']._loaded_options = None
    _globals['_PROVISIONINGCONFIG'].fields_by_name['custom_id']._serialized_options = b'\xe0A\x01'
    _globals['_PROVISIONINGCONFIG']._loaded_options = None
    _globals['_PROVISIONINGCONFIG']._serialized_options = b'\xeaA\x88\x01\n3baremetalsolution.googleapis.com/ProvisioningConfig\x12Qprojects/{project}/locations/{location}/provisioningConfigs/{provisioning_config}'
    _globals['_SUBMITPROVISIONINGCONFIGREQUEST'].fields_by_name['parent']._loaded_options = None
    _globals['_SUBMITPROVISIONINGCONFIGREQUEST'].fields_by_name['parent']._serialized_options = b'\xe0A\x02\xfaA#\n!locations.googleapis.com/Location'
    _globals['_SUBMITPROVISIONINGCONFIGREQUEST'].fields_by_name['provisioning_config']._loaded_options = None
    _globals['_SUBMITPROVISIONINGCONFIGREQUEST'].fields_by_name['provisioning_config']._serialized_options = b'\xe0A\x02'
    _globals['_SUBMITPROVISIONINGCONFIGREQUEST'].fields_by_name['email']._loaded_options = None
    _globals['_SUBMITPROVISIONINGCONFIGREQUEST'].fields_by_name['email']._serialized_options = b'\xe0A\x01'
    _globals['_PROVISIONINGQUOTA'].fields_by_name['name']._loaded_options = None
    _globals['_PROVISIONINGQUOTA'].fields_by_name['name']._serialized_options = b'\xe0A\x03'
    _globals['_PROVISIONINGQUOTA']._loaded_options = None
    _globals['_PROVISIONINGQUOTA']._serialized_options = b'\xeaA\x85\x01\n2baremetalsolution.googleapis.com/ProvisioningQuota\x12Oprojects/{project}/locations/{location}/provisioningQuotas/{provisioning_quota}'
    _globals['_LISTPROVISIONINGQUOTASREQUEST'].fields_by_name['parent']._loaded_options = None
    _globals['_LISTPROVISIONINGQUOTASREQUEST'].fields_by_name['parent']._serialized_options = b'\xe0A\x02\xfaA#\n!locations.googleapis.com/Location'
    _globals['_INSTANCECONFIG'].fields_by_name['name']._loaded_options = None
    _globals['_INSTANCECONFIG'].fields_by_name['name']._serialized_options = b'\xe0A\x03'
    _globals['_INSTANCECONFIG'].fields_by_name['client_network']._loaded_options = None
    _globals['_INSTANCECONFIG'].fields_by_name['client_network']._serialized_options = b'\x18\x01'
    _globals['_INSTANCECONFIG'].fields_by_name['private_network']._loaded_options = None
    _globals['_INSTANCECONFIG'].fields_by_name['private_network']._serialized_options = b'\x18\x01'
    _globals['_INSTANCECONFIG']._loaded_options = None
    _globals['_INSTANCECONFIG']._serialized_options = b'\xeaA|\n/baremetalsolution.googleapis.com/InstanceConfig\x12Iprojects/{project}/locations/{location}/instanceConfigs/{instance_config}'
    _globals['_VOLUMECONFIG'].fields_by_name['name']._loaded_options = None
    _globals['_VOLUMECONFIG'].fields_by_name['name']._serialized_options = b'\xe0A\x03'
    _globals['_VOLUMECONFIG']._loaded_options = None
    _globals['_VOLUMECONFIG']._serialized_options = b'\xeaAv\n-baremetalsolution.googleapis.com/VolumeConfig\x12Eprojects/{project}/locations/{location}/volumeConfigs/{volume_config}'
    _globals['_NETWORKCONFIG'].fields_by_name['name']._loaded_options = None
    _globals['_NETWORKCONFIG'].fields_by_name['name']._serialized_options = b'\xe0A\x03'
    _globals['_NETWORKCONFIG']._loaded_options = None
    _globals['_NETWORKCONFIG']._serialized_options = b'\xeaAy\n.baremetalsolution.googleapis.com/NetworkConfig\x12Gprojects/{project}/locations/{location}/networkConfigs/{network_config}'
    _globals['_INSTANCEQUOTA'].fields_by_name['name']._loaded_options = None
    _globals['_INSTANCEQUOTA'].fields_by_name['name']._serialized_options = b'\xe0A\x03'
    _globals['_INSTANCEQUOTA'].fields_by_name['instance_type']._loaded_options = None
    _globals['_INSTANCEQUOTA'].fields_by_name['instance_type']._serialized_options = b'\x18\x01'
    _globals['_INSTANCEQUOTA']._loaded_options = None
    _globals['_INSTANCEQUOTA']._serialized_options = b'\xeaAy\n.baremetalsolution.googleapis.com/InstanceQuota\x12Gprojects/{project}/locations/{location}/instanceQuotas/{instance_quota}'
    _globals['_GETPROVISIONINGCONFIGREQUEST'].fields_by_name['name']._loaded_options = None
    _globals['_GETPROVISIONINGCONFIGREQUEST'].fields_by_name['name']._serialized_options = b'\xe0A\x02\xfaA5\n3baremetalsolution.googleapis.com/ProvisioningConfig'
    _globals['_CREATEPROVISIONINGCONFIGREQUEST'].fields_by_name['parent']._loaded_options = None
    _globals['_CREATEPROVISIONINGCONFIGREQUEST'].fields_by_name['parent']._serialized_options = b'\xe0A\x02\xfaA#\n!locations.googleapis.com/Location'
    _globals['_CREATEPROVISIONINGCONFIGREQUEST'].fields_by_name['provisioning_config']._loaded_options = None
    _globals['_CREATEPROVISIONINGCONFIGREQUEST'].fields_by_name['provisioning_config']._serialized_options = b'\xe0A\x02'
    _globals['_CREATEPROVISIONINGCONFIGREQUEST'].fields_by_name['email']._loaded_options = None
    _globals['_CREATEPROVISIONINGCONFIGREQUEST'].fields_by_name['email']._serialized_options = b'\xe0A\x01'
    _globals['_UPDATEPROVISIONINGCONFIGREQUEST'].fields_by_name['provisioning_config']._loaded_options = None
    _globals['_UPDATEPROVISIONINGCONFIGREQUEST'].fields_by_name['provisioning_config']._serialized_options = b'\xe0A\x02'
    _globals['_UPDATEPROVISIONINGCONFIGREQUEST'].fields_by_name['update_mask']._loaded_options = None
    _globals['_UPDATEPROVISIONINGCONFIGREQUEST'].fields_by_name['update_mask']._serialized_options = b'\xe0A\x02'
    _globals['_UPDATEPROVISIONINGCONFIGREQUEST'].fields_by_name['email']._loaded_options = None
    _globals['_UPDATEPROVISIONINGCONFIGREQUEST'].fields_by_name['email']._serialized_options = b'\xe0A\x01'
    _globals['_PROVISIONINGCONFIG']._serialized_start = 316
    _globals['_PROVISIONINGCONFIG']._serialized_end = 1172
    _globals['_PROVISIONINGCONFIG_STATE']._serialized_start = 896
    _globals['_PROVISIONINGCONFIG_STATE']._serialized_end = 1029
    _globals['_SUBMITPROVISIONINGCONFIGREQUEST']._serialized_start = 1175
    _globals['_SUBMITPROVISIONINGCONFIGREQUEST']._serialized_end = 1376
    _globals['_SUBMITPROVISIONINGCONFIGRESPONSE']._serialized_start = 1378
    _globals['_SUBMITPROVISIONINGCONFIGRESPONSE']._serialized_end = 1496
    _globals['_PROVISIONINGQUOTA']._serialized_start = 1499
    _globals['_PROVISIONINGQUOTA']._serialized_end = 2114
    _globals['_PROVISIONINGQUOTA_ASSETTYPE']._serialized_start = 1839
    _globals['_PROVISIONINGQUOTA_ASSETTYPE']._serialized_end = 1949
    _globals['_LISTPROVISIONINGQUOTASREQUEST']._serialized_start = 2117
    _globals['_LISTPROVISIONINGQUOTASREQUEST']._serialized_end = 2246
    _globals['_LISTPROVISIONINGQUOTASRESPONSE']._serialized_start = 2249
    _globals['_LISTPROVISIONINGQUOTASRESPONSE']._serialized_end = 2389
    _globals['_INSTANCECONFIG']._serialized_start = 2392
    _globals['_INSTANCECONFIG']._serialized_end = 3259
    _globals['_INSTANCECONFIG_NETWORKADDRESS']._serialized_start = 2967
    _globals['_INSTANCECONFIG_NETWORKADDRESS']._serialized_end = 3049
    _globals['_INSTANCECONFIG_NETWORKCONFIG']._serialized_start = 3051
    _globals['_INSTANCECONFIG_NETWORKCONFIG']._serialized_end = 3130
    _globals['_VOLUMECONFIG']._serialized_start = 3262
    _globals['_VOLUMECONFIG']._serialized_end = 4404
    _globals['_VOLUMECONFIG_LUNRANGE']._serialized_start = 3800
    _globals['_VOLUMECONFIG_LUNRANGE']._serialized_end = 3845
    _globals['_VOLUMECONFIG_NFSEXPORT']._serialized_start = 3848
    _globals['_VOLUMECONFIG_NFSEXPORT']._serialized_end = 4157
    _globals['_VOLUMECONFIG_NFSEXPORT_PERMISSIONS']._serialized_start = 4074
    _globals['_VOLUMECONFIG_NFSEXPORT_PERMISSIONS']._serialized_end = 4147
    _globals['_VOLUMECONFIG_TYPE']._serialized_start = 4159
    _globals['_VOLUMECONFIG_TYPE']._serialized_end = 4208
    _globals['_VOLUMECONFIG_PROTOCOL']._serialized_start = 4210
    _globals['_VOLUMECONFIG_PROTOCOL']._serialized_end = 4281
    _globals['_NETWORKCONFIG']._serialized_start = 4407
    _globals['_NETWORKCONFIG']._serialized_end = 5330
    _globals['_NETWORKCONFIG_INTAKEVLANATTACHMENT']._serialized_start = 4895
    _globals['_NETWORKCONFIG_INTAKEVLANATTACHMENT']._serialized_end = 4950
    _globals['_NETWORKCONFIG_TYPE']._serialized_start = 4952
    _globals['_NETWORKCONFIG_TYPE']._serialized_end = 5005
    _globals['_NETWORKCONFIG_BANDWIDTH']._serialized_start = 5007
    _globals['_NETWORKCONFIG_BANDWIDTH']._serialized_end = 5106
    _globals['_NETWORKCONFIG_SERVICECIDR']._serialized_start = 5108
    _globals['_NETWORKCONFIG_SERVICECIDR']._serialized_end = 5204
    _globals['_INSTANCEQUOTA']._serialized_start = 5333
    _globals['_INSTANCEQUOTA']._serialized_end = 5592
    _globals['_GETPROVISIONINGCONFIGREQUEST']._serialized_start = 5594
    _globals['_GETPROVISIONINGCONFIGREQUEST']._serialized_end = 5699
    _globals['_CREATEPROVISIONINGCONFIGREQUEST']._serialized_start = 5702
    _globals['_CREATEPROVISIONINGCONFIGREQUEST']._serialized_end = 5903
    _globals['_UPDATEPROVISIONINGCONFIGREQUEST']._serialized_start = 5906
    _globals['_UPDATEPROVISIONINGCONFIGREQUEST']._serialized_end = 6102