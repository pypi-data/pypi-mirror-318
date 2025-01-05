"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_runtime_version.ValidateProtobufRuntimeVersion(_runtime_version.Domain.PUBLIC, 5, 28, 1, '', 'google/cloud/aiplatform/v1beta1/index_endpoint.proto')
_sym_db = _symbol_database.Default()
from .....google.api import field_behavior_pb2 as google_dot_api_dot_field__behavior__pb2
from .....google.api import resource_pb2 as google_dot_api_dot_resource__pb2
from .....google.cloud.aiplatform.v1beta1 import encryption_spec_pb2 as google_dot_cloud_dot_aiplatform_dot_v1beta1_dot_encryption__spec__pb2
from .....google.cloud.aiplatform.v1beta1 import machine_resources_pb2 as google_dot_cloud_dot_aiplatform_dot_v1beta1_dot_machine__resources__pb2
from .....google.cloud.aiplatform.v1beta1 import service_networking_pb2 as google_dot_cloud_dot_aiplatform_dot_v1beta1_dot_service__networking__pb2
from google.protobuf import timestamp_pb2 as google_dot_protobuf_dot_timestamp__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n4google/cloud/aiplatform/v1beta1/index_endpoint.proto\x12\x1fgoogle.cloud.aiplatform.v1beta1\x1a\x1fgoogle/api/field_behavior.proto\x1a\x19google/api/resource.proto\x1a5google/cloud/aiplatform/v1beta1/encryption_spec.proto\x1a7google/cloud/aiplatform/v1beta1/machine_resources.proto\x1a8google/cloud/aiplatform/v1beta1/service_networking.proto\x1a\x1fgoogle/protobuf/timestamp.proto"\x94\x07\n\rIndexEndpoint\x12\x11\n\x04name\x18\x01 \x01(\tB\x03\xe0A\x03\x12\x19\n\x0cdisplay_name\x18\x02 \x01(\tB\x03\xe0A\x02\x12\x13\n\x0bdescription\x18\x03 \x01(\t\x12M\n\x10deployed_indexes\x18\x04 \x03(\x0b2..google.cloud.aiplatform.v1beta1.DeployedIndexB\x03\xe0A\x03\x12\x0c\n\x04etag\x18\x05 \x01(\t\x12J\n\x06labels\x18\x06 \x03(\x0b2:.google.cloud.aiplatform.v1beta1.IndexEndpoint.LabelsEntry\x124\n\x0bcreate_time\x18\x07 \x01(\x0b2\x1a.google.protobuf.TimestampB\x03\xe0A\x03\x124\n\x0bupdate_time\x18\x08 \x01(\x0b2\x1a.google.protobuf.TimestampB\x03\xe0A\x03\x12\x14\n\x07network\x18\t \x01(\tB\x03\xe0A\x01\x12-\n\x1eenable_private_service_connect\x18\n \x01(\x08B\x05\x18\x01\xe0A\x01\x12i\n\x1eprivate_service_connect_config\x18\x0c \x01(\x0b2<.google.cloud.aiplatform.v1beta1.PrivateServiceConnectConfigB\x03\xe0A\x01\x12$\n\x17public_endpoint_enabled\x18\r \x01(\x08B\x03\xe0A\x01\x12(\n\x1bpublic_endpoint_domain_name\x18\x0e \x01(\tB\x03\xe0A\x03\x12M\n\x0fencryption_spec\x18\x0f \x01(\x0b2/.google.cloud.aiplatform.v1beta1.EncryptionSpecB\x03\xe0A\x05\x12\x1a\n\rsatisfies_pzs\x18\x11 \x01(\x08B\x03\xe0A\x03\x12\x1a\n\rsatisfies_pzi\x18\x12 \x01(\x08B\x03\xe0A\x03\x1a-\n\x0bLabelsEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\r\n\x05value\x18\x02 \x01(\t:\x028\x01:u\xeaAr\n\'aiplatform.googleapis.com/IndexEndpoint\x12Gprojects/{project}/locations/{location}/indexEndpoints/{index_endpoint}"\x86\x06\n\rDeployedIndex\x12\x0f\n\x02id\x18\x01 \x01(\tB\x03\xe0A\x02\x126\n\x05index\x18\x02 \x01(\tB\'\xe0A\x02\xfaA!\n\x1faiplatform.googleapis.com/Index\x12\x14\n\x0cdisplay_name\x18\x03 \x01(\t\x124\n\x0bcreate_time\x18\x04 \x01(\x0b2\x1a.google.protobuf.TimestampB\x03\xe0A\x03\x12V\n\x11private_endpoints\x18\x05 \x01(\x0b26.google.cloud.aiplatform.v1beta1.IndexPrivateEndpointsB\x03\xe0A\x03\x128\n\x0findex_sync_time\x18\x06 \x01(\x0b2\x1a.google.protobuf.TimestampB\x03\xe0A\x03\x12U\n\x13automatic_resources\x18\x07 \x01(\x0b23.google.cloud.aiplatform.v1beta1.AutomaticResourcesB\x03\xe0A\x01\x12U\n\x13dedicated_resources\x18\x10 \x01(\x0b23.google.cloud.aiplatform.v1beta1.DedicatedResourcesB\x03\xe0A\x01\x12"\n\x15enable_access_logging\x18\x08 \x01(\x08B\x03\xe0A\x01\x12a\n\x1adeployed_index_auth_config\x18\t \x01(\x0b28.google.cloud.aiplatform.v1beta1.DeployedIndexAuthConfigB\x03\xe0A\x01\x12\x1f\n\x12reserved_ip_ranges\x18\n \x03(\tB\x03\xe0A\x01\x12\x1d\n\x10deployment_group\x18\x0b \x01(\tB\x03\xe0A\x01\x12Y\n\x16psc_automation_configs\x18\x13 \x03(\x0b24.google.cloud.aiplatform.v1beta1.PSCAutomationConfigB\x03\xe0A\x01"\xb3\x01\n\x17DeployedIndexAuthConfig\x12\\\n\rauth_provider\x18\x01 \x01(\x0b2E.google.cloud.aiplatform.v1beta1.DeployedIndexAuthConfig.AuthProvider\x1a:\n\x0cAuthProvider\x12\x11\n\taudiences\x18\x01 \x03(\t\x12\x17\n\x0fallowed_issuers\x18\x02 \x03(\t"\xb7\x01\n\x15IndexPrivateEndpoints\x12\x1f\n\x12match_grpc_address\x18\x01 \x01(\tB\x03\xe0A\x03\x12\x1f\n\x12service_attachment\x18\x02 \x01(\tB\x03\xe0A\x03\x12\\\n\x17psc_automated_endpoints\x18\x03 \x03(\x0b26.google.cloud.aiplatform.v1beta1.PscAutomatedEndpointsB\x03\xe0A\x03B\xe9\x01\n#com.google.cloud.aiplatform.v1beta1B\x12IndexEndpointProtoP\x01ZCcloud.google.com/go/aiplatform/apiv1beta1/aiplatformpb;aiplatformpb\xaa\x02\x1fGoogle.Cloud.AIPlatform.V1Beta1\xca\x02\x1fGoogle\\Cloud\\AIPlatform\\V1beta1\xea\x02"Google::Cloud::AIPlatform::V1beta1b\x06proto3')
_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'google.cloud.aiplatform.v1beta1.index_endpoint_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
    _globals['DESCRIPTOR']._loaded_options = None
    _globals['DESCRIPTOR']._serialized_options = b'\n#com.google.cloud.aiplatform.v1beta1B\x12IndexEndpointProtoP\x01ZCcloud.google.com/go/aiplatform/apiv1beta1/aiplatformpb;aiplatformpb\xaa\x02\x1fGoogle.Cloud.AIPlatform.V1Beta1\xca\x02\x1fGoogle\\Cloud\\AIPlatform\\V1beta1\xea\x02"Google::Cloud::AIPlatform::V1beta1'
    _globals['_INDEXENDPOINT_LABELSENTRY']._loaded_options = None
    _globals['_INDEXENDPOINT_LABELSENTRY']._serialized_options = b'8\x01'
    _globals['_INDEXENDPOINT'].fields_by_name['name']._loaded_options = None
    _globals['_INDEXENDPOINT'].fields_by_name['name']._serialized_options = b'\xe0A\x03'
    _globals['_INDEXENDPOINT'].fields_by_name['display_name']._loaded_options = None
    _globals['_INDEXENDPOINT'].fields_by_name['display_name']._serialized_options = b'\xe0A\x02'
    _globals['_INDEXENDPOINT'].fields_by_name['deployed_indexes']._loaded_options = None
    _globals['_INDEXENDPOINT'].fields_by_name['deployed_indexes']._serialized_options = b'\xe0A\x03'
    _globals['_INDEXENDPOINT'].fields_by_name['create_time']._loaded_options = None
    _globals['_INDEXENDPOINT'].fields_by_name['create_time']._serialized_options = b'\xe0A\x03'
    _globals['_INDEXENDPOINT'].fields_by_name['update_time']._loaded_options = None
    _globals['_INDEXENDPOINT'].fields_by_name['update_time']._serialized_options = b'\xe0A\x03'
    _globals['_INDEXENDPOINT'].fields_by_name['network']._loaded_options = None
    _globals['_INDEXENDPOINT'].fields_by_name['network']._serialized_options = b'\xe0A\x01'
    _globals['_INDEXENDPOINT'].fields_by_name['enable_private_service_connect']._loaded_options = None
    _globals['_INDEXENDPOINT'].fields_by_name['enable_private_service_connect']._serialized_options = b'\x18\x01\xe0A\x01'
    _globals['_INDEXENDPOINT'].fields_by_name['private_service_connect_config']._loaded_options = None
    _globals['_INDEXENDPOINT'].fields_by_name['private_service_connect_config']._serialized_options = b'\xe0A\x01'
    _globals['_INDEXENDPOINT'].fields_by_name['public_endpoint_enabled']._loaded_options = None
    _globals['_INDEXENDPOINT'].fields_by_name['public_endpoint_enabled']._serialized_options = b'\xe0A\x01'
    _globals['_INDEXENDPOINT'].fields_by_name['public_endpoint_domain_name']._loaded_options = None
    _globals['_INDEXENDPOINT'].fields_by_name['public_endpoint_domain_name']._serialized_options = b'\xe0A\x03'
    _globals['_INDEXENDPOINT'].fields_by_name['encryption_spec']._loaded_options = None
    _globals['_INDEXENDPOINT'].fields_by_name['encryption_spec']._serialized_options = b'\xe0A\x05'
    _globals['_INDEXENDPOINT'].fields_by_name['satisfies_pzs']._loaded_options = None
    _globals['_INDEXENDPOINT'].fields_by_name['satisfies_pzs']._serialized_options = b'\xe0A\x03'
    _globals['_INDEXENDPOINT'].fields_by_name['satisfies_pzi']._loaded_options = None
    _globals['_INDEXENDPOINT'].fields_by_name['satisfies_pzi']._serialized_options = b'\xe0A\x03'
    _globals['_INDEXENDPOINT']._loaded_options = None
    _globals['_INDEXENDPOINT']._serialized_options = b"\xeaAr\n'aiplatform.googleapis.com/IndexEndpoint\x12Gprojects/{project}/locations/{location}/indexEndpoints/{index_endpoint}"
    _globals['_DEPLOYEDINDEX'].fields_by_name['id']._loaded_options = None
    _globals['_DEPLOYEDINDEX'].fields_by_name['id']._serialized_options = b'\xe0A\x02'
    _globals['_DEPLOYEDINDEX'].fields_by_name['index']._loaded_options = None
    _globals['_DEPLOYEDINDEX'].fields_by_name['index']._serialized_options = b'\xe0A\x02\xfaA!\n\x1faiplatform.googleapis.com/Index'
    _globals['_DEPLOYEDINDEX'].fields_by_name['create_time']._loaded_options = None
    _globals['_DEPLOYEDINDEX'].fields_by_name['create_time']._serialized_options = b'\xe0A\x03'
    _globals['_DEPLOYEDINDEX'].fields_by_name['private_endpoints']._loaded_options = None
    _globals['_DEPLOYEDINDEX'].fields_by_name['private_endpoints']._serialized_options = b'\xe0A\x03'
    _globals['_DEPLOYEDINDEX'].fields_by_name['index_sync_time']._loaded_options = None
    _globals['_DEPLOYEDINDEX'].fields_by_name['index_sync_time']._serialized_options = b'\xe0A\x03'
    _globals['_DEPLOYEDINDEX'].fields_by_name['automatic_resources']._loaded_options = None
    _globals['_DEPLOYEDINDEX'].fields_by_name['automatic_resources']._serialized_options = b'\xe0A\x01'
    _globals['_DEPLOYEDINDEX'].fields_by_name['dedicated_resources']._loaded_options = None
    _globals['_DEPLOYEDINDEX'].fields_by_name['dedicated_resources']._serialized_options = b'\xe0A\x01'
    _globals['_DEPLOYEDINDEX'].fields_by_name['enable_access_logging']._loaded_options = None
    _globals['_DEPLOYEDINDEX'].fields_by_name['enable_access_logging']._serialized_options = b'\xe0A\x01'
    _globals['_DEPLOYEDINDEX'].fields_by_name['deployed_index_auth_config']._loaded_options = None
    _globals['_DEPLOYEDINDEX'].fields_by_name['deployed_index_auth_config']._serialized_options = b'\xe0A\x01'
    _globals['_DEPLOYEDINDEX'].fields_by_name['reserved_ip_ranges']._loaded_options = None
    _globals['_DEPLOYEDINDEX'].fields_by_name['reserved_ip_ranges']._serialized_options = b'\xe0A\x01'
    _globals['_DEPLOYEDINDEX'].fields_by_name['deployment_group']._loaded_options = None
    _globals['_DEPLOYEDINDEX'].fields_by_name['deployment_group']._serialized_options = b'\xe0A\x01'
    _globals['_DEPLOYEDINDEX'].fields_by_name['psc_automation_configs']._loaded_options = None
    _globals['_DEPLOYEDINDEX'].fields_by_name['psc_automation_configs']._serialized_options = b'\xe0A\x01'
    _globals['_INDEXPRIVATEENDPOINTS'].fields_by_name['match_grpc_address']._loaded_options = None
    _globals['_INDEXPRIVATEENDPOINTS'].fields_by_name['match_grpc_address']._serialized_options = b'\xe0A\x03'
    _globals['_INDEXPRIVATEENDPOINTS'].fields_by_name['service_attachment']._loaded_options = None
    _globals['_INDEXPRIVATEENDPOINTS'].fields_by_name['service_attachment']._serialized_options = b'\xe0A\x03'
    _globals['_INDEXPRIVATEENDPOINTS'].fields_by_name['psc_automated_endpoints']._loaded_options = None
    _globals['_INDEXPRIVATEENDPOINTS'].fields_by_name['psc_automated_endpoints']._serialized_options = b'\xe0A\x03'
    _globals['_INDEXENDPOINT']._serialized_start = 353
    _globals['_INDEXENDPOINT']._serialized_end = 1269
    _globals['_INDEXENDPOINT_LABELSENTRY']._serialized_start = 1105
    _globals['_INDEXENDPOINT_LABELSENTRY']._serialized_end = 1150
    _globals['_DEPLOYEDINDEX']._serialized_start = 1272
    _globals['_DEPLOYEDINDEX']._serialized_end = 2046
    _globals['_DEPLOYEDINDEXAUTHCONFIG']._serialized_start = 2049
    _globals['_DEPLOYEDINDEXAUTHCONFIG']._serialized_end = 2228
    _globals['_DEPLOYEDINDEXAUTHCONFIG_AUTHPROVIDER']._serialized_start = 2170
    _globals['_DEPLOYEDINDEXAUTHCONFIG_AUTHPROVIDER']._serialized_end = 2228
    _globals['_INDEXPRIVATEENDPOINTS']._serialized_start = 2231
    _globals['_INDEXPRIVATEENDPOINTS']._serialized_end = 2414