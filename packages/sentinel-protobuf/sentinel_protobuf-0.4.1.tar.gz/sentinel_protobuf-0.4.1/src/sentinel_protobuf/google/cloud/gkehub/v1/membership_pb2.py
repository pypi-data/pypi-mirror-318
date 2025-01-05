"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_runtime_version.ValidateProtobufRuntimeVersion(_runtime_version.Domain.PUBLIC, 5, 28, 1, '', 'google/cloud/gkehub/v1/membership.proto')
_sym_db = _symbol_database.Default()
from .....google.api import field_behavior_pb2 as google_dot_api_dot_field__behavior__pb2
from .....google.api import resource_pb2 as google_dot_api_dot_resource__pb2
from google.protobuf import timestamp_pb2 as google_dot_protobuf_dot_timestamp__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\'google/cloud/gkehub/v1/membership.proto\x12\x16google.cloud.gkehub.v1\x1a\x1fgoogle/api/field_behavior.proto\x1a\x19google/api/resource.proto\x1a\x1fgoogle/protobuf/timestamp.proto"\xb8\x06\n\nMembership\x12C\n\x08endpoint\x18\x04 \x01(\x0b2*.google.cloud.gkehub.v1.MembershipEndpointB\x03\xe0A\x01H\x00\x12\x11\n\x04name\x18\x01 \x01(\tB\x03\xe0A\x03\x12C\n\x06labels\x18\x02 \x03(\x0b2..google.cloud.gkehub.v1.Membership.LabelsEntryB\x03\xe0A\x01\x12\x18\n\x0bdescription\x18\x03 \x01(\tB\x03\xe0A\x03\x12;\n\x05state\x18\x05 \x01(\x0b2\'.google.cloud.gkehub.v1.MembershipStateB\x03\xe0A\x03\x124\n\x0bcreate_time\x18\x06 \x01(\x0b2\x1a.google.protobuf.TimestampB\x03\xe0A\x03\x124\n\x0bupdate_time\x18\x07 \x01(\x0b2\x1a.google.protobuf.TimestampB\x03\xe0A\x03\x124\n\x0bdelete_time\x18\x08 \x01(\x0b2\x1a.google.protobuf.TimestampB\x03\xe0A\x03\x12\x18\n\x0bexternal_id\x18\t \x01(\tB\x03\xe0A\x01\x12=\n\x14last_connection_time\x18\n \x01(\x0b2\x1a.google.protobuf.TimestampB\x03\xe0A\x03\x12\x16\n\tunique_id\x18\x0b \x01(\tB\x03\xe0A\x03\x129\n\tauthority\x18\x0c \x01(\x0b2!.google.cloud.gkehub.v1.AuthorityB\x03\xe0A\x01\x12H\n\x11monitoring_config\x18\x0e \x01(\x0b2(.google.cloud.gkehub.v1.MonitoringConfigB\x03\xe0A\x01\x1a-\n\x0bLabelsEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\r\n\x05value\x18\x02 \x01(\t:\x028\x01:g\xeaAd\n gkehub.googleapis.com/Membership\x12@projects/{project}/locations/{location}/memberships/{membership}B\x06\n\x04type"\x8b\x02\n\x12MembershipEndpoint\x12<\n\x0bgke_cluster\x18\x01 \x01(\x0b2".google.cloud.gkehub.v1.GkeClusterB\x03\xe0A\x01\x12L\n\x13kubernetes_metadata\x18\x02 \x01(\x0b2*.google.cloud.gkehub.v1.KubernetesMetadataB\x03\xe0A\x03\x12L\n\x13kubernetes_resource\x18\x03 \x01(\x0b2*.google.cloud.gkehub.v1.KubernetesResourceB\x03\xe0A\x01\x12\x1b\n\x0egoogle_managed\x18\x08 \x01(\x08B\x03\xe0A\x03"\x98\x02\n\x12KubernetesResource\x12#\n\x16membership_cr_manifest\x18\x01 \x01(\tB\x03\xe0A\x04\x12K\n\x14membership_resources\x18\x02 \x03(\x0b2(.google.cloud.gkehub.v1.ResourceManifestB\x03\xe0A\x03\x12H\n\x11connect_resources\x18\x03 \x03(\x0b2(.google.cloud.gkehub.v1.ResourceManifestB\x03\xe0A\x03\x12F\n\x10resource_options\x18\x04 \x01(\x0b2\'.google.cloud.gkehub.v1.ResourceOptionsB\x03\xe0A\x01"c\n\x0fResourceOptions\x12\x1c\n\x0fconnect_version\x18\x01 \x01(\tB\x03\xe0A\x01\x12\x18\n\x0bv1beta1_crd\x18\x02 \x01(\x08B\x03\xe0A\x01\x12\x18\n\x0bk8s_version\x18\x03 \x01(\tB\x03\xe0A\x01"<\n\x10ResourceManifest\x12\x10\n\x08manifest\x18\x01 \x01(\t\x12\x16\n\x0ecluster_scoped\x18\x02 \x01(\x08"F\n\nGkeCluster\x12\x1a\n\rresource_link\x18\x01 \x01(\tB\x03\xe0A\x05\x12\x1c\n\x0fcluster_missing\x18\x02 \x01(\x08B\x03\xe0A\x03"\xdf\x01\n\x12KubernetesMetadata\x12*\n\x1dkubernetes_api_server_version\x18\x01 \x01(\tB\x03\xe0A\x03\x12\x1d\n\x10node_provider_id\x18\x02 \x01(\tB\x03\xe0A\x03\x12\x17\n\nnode_count\x18\x03 \x01(\x05B\x03\xe0A\x03\x12\x17\n\nvcpu_count\x18\x04 \x01(\x05B\x03\xe0A\x03\x12\x16\n\tmemory_mb\x18\x05 \x01(\x05B\x03\xe0A\x03\x124\n\x0bupdate_time\x18d \x01(\x0b2\x1a.google.protobuf.TimestampB\x03\xe0A\x03"\x96\x01\n\x10MonitoringConfig\x12\x17\n\nproject_id\x18\x01 \x01(\tB\x03\xe0A\x05\x12\x15\n\x08location\x18\x02 \x01(\tB\x03\xe0A\x05\x12\x14\n\x07cluster\x18\x03 \x01(\tB\x03\xe0A\x05\x12!\n\x19kubernetes_metrics_prefix\x18\x04 \x01(\t\x12\x19\n\x0ccluster_hash\x18\x05 \x01(\tB\x03\xe0A\x05"\xbb\x01\n\x0fMembershipState\x12?\n\x04code\x18\x01 \x01(\x0e2,.google.cloud.gkehub.v1.MembershipState.CodeB\x03\xe0A\x03"g\n\x04Code\x12\x14\n\x10CODE_UNSPECIFIED\x10\x00\x12\x0c\n\x08CREATING\x10\x01\x12\t\n\x05READY\x10\x02\x12\x0c\n\x08DELETING\x10\x03\x12\x0c\n\x08UPDATING\x10\x04\x12\x14\n\x10SERVICE_UPDATING\x10\x05"}\n\tAuthority\x12\x13\n\x06issuer\x18\x01 \x01(\tB\x03\xe0A\x01\x12#\n\x16workload_identity_pool\x18\x02 \x01(\tB\x03\xe0A\x03\x12\x1e\n\x11identity_provider\x18\x03 \x01(\tB\x03\xe0A\x03\x12\x16\n\toidc_jwks\x18\x04 \x01(\x0cB\x03\xe0A\x01B\xb1\x01\n\x1acom.google.cloud.gkehub.v1B\x0fMembershipProtoP\x01Z2cloud.google.com/go/gkehub/apiv1/gkehubpb;gkehubpb\xaa\x02\x16Google.Cloud.GkeHub.V1\xca\x02\x16Google\\Cloud\\GkeHub\\V1\xea\x02\x19Google::Cloud::GkeHub::V1b\x06proto3')
_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'google.cloud.gkehub.v1.membership_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
    _globals['DESCRIPTOR']._loaded_options = None
    _globals['DESCRIPTOR']._serialized_options = b'\n\x1acom.google.cloud.gkehub.v1B\x0fMembershipProtoP\x01Z2cloud.google.com/go/gkehub/apiv1/gkehubpb;gkehubpb\xaa\x02\x16Google.Cloud.GkeHub.V1\xca\x02\x16Google\\Cloud\\GkeHub\\V1\xea\x02\x19Google::Cloud::GkeHub::V1'
    _globals['_MEMBERSHIP_LABELSENTRY']._loaded_options = None
    _globals['_MEMBERSHIP_LABELSENTRY']._serialized_options = b'8\x01'
    _globals['_MEMBERSHIP'].fields_by_name['endpoint']._loaded_options = None
    _globals['_MEMBERSHIP'].fields_by_name['endpoint']._serialized_options = b'\xe0A\x01'
    _globals['_MEMBERSHIP'].fields_by_name['name']._loaded_options = None
    _globals['_MEMBERSHIP'].fields_by_name['name']._serialized_options = b'\xe0A\x03'
    _globals['_MEMBERSHIP'].fields_by_name['labels']._loaded_options = None
    _globals['_MEMBERSHIP'].fields_by_name['labels']._serialized_options = b'\xe0A\x01'
    _globals['_MEMBERSHIP'].fields_by_name['description']._loaded_options = None
    _globals['_MEMBERSHIP'].fields_by_name['description']._serialized_options = b'\xe0A\x03'
    _globals['_MEMBERSHIP'].fields_by_name['state']._loaded_options = None
    _globals['_MEMBERSHIP'].fields_by_name['state']._serialized_options = b'\xe0A\x03'
    _globals['_MEMBERSHIP'].fields_by_name['create_time']._loaded_options = None
    _globals['_MEMBERSHIP'].fields_by_name['create_time']._serialized_options = b'\xe0A\x03'
    _globals['_MEMBERSHIP'].fields_by_name['update_time']._loaded_options = None
    _globals['_MEMBERSHIP'].fields_by_name['update_time']._serialized_options = b'\xe0A\x03'
    _globals['_MEMBERSHIP'].fields_by_name['delete_time']._loaded_options = None
    _globals['_MEMBERSHIP'].fields_by_name['delete_time']._serialized_options = b'\xe0A\x03'
    _globals['_MEMBERSHIP'].fields_by_name['external_id']._loaded_options = None
    _globals['_MEMBERSHIP'].fields_by_name['external_id']._serialized_options = b'\xe0A\x01'
    _globals['_MEMBERSHIP'].fields_by_name['last_connection_time']._loaded_options = None
    _globals['_MEMBERSHIP'].fields_by_name['last_connection_time']._serialized_options = b'\xe0A\x03'
    _globals['_MEMBERSHIP'].fields_by_name['unique_id']._loaded_options = None
    _globals['_MEMBERSHIP'].fields_by_name['unique_id']._serialized_options = b'\xe0A\x03'
    _globals['_MEMBERSHIP'].fields_by_name['authority']._loaded_options = None
    _globals['_MEMBERSHIP'].fields_by_name['authority']._serialized_options = b'\xe0A\x01'
    _globals['_MEMBERSHIP'].fields_by_name['monitoring_config']._loaded_options = None
    _globals['_MEMBERSHIP'].fields_by_name['monitoring_config']._serialized_options = b'\xe0A\x01'
    _globals['_MEMBERSHIP']._loaded_options = None
    _globals['_MEMBERSHIP']._serialized_options = b'\xeaAd\n gkehub.googleapis.com/Membership\x12@projects/{project}/locations/{location}/memberships/{membership}'
    _globals['_MEMBERSHIPENDPOINT'].fields_by_name['gke_cluster']._loaded_options = None
    _globals['_MEMBERSHIPENDPOINT'].fields_by_name['gke_cluster']._serialized_options = b'\xe0A\x01'
    _globals['_MEMBERSHIPENDPOINT'].fields_by_name['kubernetes_metadata']._loaded_options = None
    _globals['_MEMBERSHIPENDPOINT'].fields_by_name['kubernetes_metadata']._serialized_options = b'\xe0A\x03'
    _globals['_MEMBERSHIPENDPOINT'].fields_by_name['kubernetes_resource']._loaded_options = None
    _globals['_MEMBERSHIPENDPOINT'].fields_by_name['kubernetes_resource']._serialized_options = b'\xe0A\x01'
    _globals['_MEMBERSHIPENDPOINT'].fields_by_name['google_managed']._loaded_options = None
    _globals['_MEMBERSHIPENDPOINT'].fields_by_name['google_managed']._serialized_options = b'\xe0A\x03'
    _globals['_KUBERNETESRESOURCE'].fields_by_name['membership_cr_manifest']._loaded_options = None
    _globals['_KUBERNETESRESOURCE'].fields_by_name['membership_cr_manifest']._serialized_options = b'\xe0A\x04'
    _globals['_KUBERNETESRESOURCE'].fields_by_name['membership_resources']._loaded_options = None
    _globals['_KUBERNETESRESOURCE'].fields_by_name['membership_resources']._serialized_options = b'\xe0A\x03'
    _globals['_KUBERNETESRESOURCE'].fields_by_name['connect_resources']._loaded_options = None
    _globals['_KUBERNETESRESOURCE'].fields_by_name['connect_resources']._serialized_options = b'\xe0A\x03'
    _globals['_KUBERNETESRESOURCE'].fields_by_name['resource_options']._loaded_options = None
    _globals['_KUBERNETESRESOURCE'].fields_by_name['resource_options']._serialized_options = b'\xe0A\x01'
    _globals['_RESOURCEOPTIONS'].fields_by_name['connect_version']._loaded_options = None
    _globals['_RESOURCEOPTIONS'].fields_by_name['connect_version']._serialized_options = b'\xe0A\x01'
    _globals['_RESOURCEOPTIONS'].fields_by_name['v1beta1_crd']._loaded_options = None
    _globals['_RESOURCEOPTIONS'].fields_by_name['v1beta1_crd']._serialized_options = b'\xe0A\x01'
    _globals['_RESOURCEOPTIONS'].fields_by_name['k8s_version']._loaded_options = None
    _globals['_RESOURCEOPTIONS'].fields_by_name['k8s_version']._serialized_options = b'\xe0A\x01'
    _globals['_GKECLUSTER'].fields_by_name['resource_link']._loaded_options = None
    _globals['_GKECLUSTER'].fields_by_name['resource_link']._serialized_options = b'\xe0A\x05'
    _globals['_GKECLUSTER'].fields_by_name['cluster_missing']._loaded_options = None
    _globals['_GKECLUSTER'].fields_by_name['cluster_missing']._serialized_options = b'\xe0A\x03'
    _globals['_KUBERNETESMETADATA'].fields_by_name['kubernetes_api_server_version']._loaded_options = None
    _globals['_KUBERNETESMETADATA'].fields_by_name['kubernetes_api_server_version']._serialized_options = b'\xe0A\x03'
    _globals['_KUBERNETESMETADATA'].fields_by_name['node_provider_id']._loaded_options = None
    _globals['_KUBERNETESMETADATA'].fields_by_name['node_provider_id']._serialized_options = b'\xe0A\x03'
    _globals['_KUBERNETESMETADATA'].fields_by_name['node_count']._loaded_options = None
    _globals['_KUBERNETESMETADATA'].fields_by_name['node_count']._serialized_options = b'\xe0A\x03'
    _globals['_KUBERNETESMETADATA'].fields_by_name['vcpu_count']._loaded_options = None
    _globals['_KUBERNETESMETADATA'].fields_by_name['vcpu_count']._serialized_options = b'\xe0A\x03'
    _globals['_KUBERNETESMETADATA'].fields_by_name['memory_mb']._loaded_options = None
    _globals['_KUBERNETESMETADATA'].fields_by_name['memory_mb']._serialized_options = b'\xe0A\x03'
    _globals['_KUBERNETESMETADATA'].fields_by_name['update_time']._loaded_options = None
    _globals['_KUBERNETESMETADATA'].fields_by_name['update_time']._serialized_options = b'\xe0A\x03'
    _globals['_MONITORINGCONFIG'].fields_by_name['project_id']._loaded_options = None
    _globals['_MONITORINGCONFIG'].fields_by_name['project_id']._serialized_options = b'\xe0A\x05'
    _globals['_MONITORINGCONFIG'].fields_by_name['location']._loaded_options = None
    _globals['_MONITORINGCONFIG'].fields_by_name['location']._serialized_options = b'\xe0A\x05'
    _globals['_MONITORINGCONFIG'].fields_by_name['cluster']._loaded_options = None
    _globals['_MONITORINGCONFIG'].fields_by_name['cluster']._serialized_options = b'\xe0A\x05'
    _globals['_MONITORINGCONFIG'].fields_by_name['cluster_hash']._loaded_options = None
    _globals['_MONITORINGCONFIG'].fields_by_name['cluster_hash']._serialized_options = b'\xe0A\x05'
    _globals['_MEMBERSHIPSTATE'].fields_by_name['code']._loaded_options = None
    _globals['_MEMBERSHIPSTATE'].fields_by_name['code']._serialized_options = b'\xe0A\x03'
    _globals['_AUTHORITY'].fields_by_name['issuer']._loaded_options = None
    _globals['_AUTHORITY'].fields_by_name['issuer']._serialized_options = b'\xe0A\x01'
    _globals['_AUTHORITY'].fields_by_name['workload_identity_pool']._loaded_options = None
    _globals['_AUTHORITY'].fields_by_name['workload_identity_pool']._serialized_options = b'\xe0A\x03'
    _globals['_AUTHORITY'].fields_by_name['identity_provider']._loaded_options = None
    _globals['_AUTHORITY'].fields_by_name['identity_provider']._serialized_options = b'\xe0A\x03'
    _globals['_AUTHORITY'].fields_by_name['oidc_jwks']._loaded_options = None
    _globals['_AUTHORITY'].fields_by_name['oidc_jwks']._serialized_options = b'\xe0A\x01'
    _globals['_MEMBERSHIP']._serialized_start = 161
    _globals['_MEMBERSHIP']._serialized_end = 985
    _globals['_MEMBERSHIP_LABELSENTRY']._serialized_start = 827
    _globals['_MEMBERSHIP_LABELSENTRY']._serialized_end = 872
    _globals['_MEMBERSHIPENDPOINT']._serialized_start = 988
    _globals['_MEMBERSHIPENDPOINT']._serialized_end = 1255
    _globals['_KUBERNETESRESOURCE']._serialized_start = 1258
    _globals['_KUBERNETESRESOURCE']._serialized_end = 1538
    _globals['_RESOURCEOPTIONS']._serialized_start = 1540
    _globals['_RESOURCEOPTIONS']._serialized_end = 1639
    _globals['_RESOURCEMANIFEST']._serialized_start = 1641
    _globals['_RESOURCEMANIFEST']._serialized_end = 1701
    _globals['_GKECLUSTER']._serialized_start = 1703
    _globals['_GKECLUSTER']._serialized_end = 1773
    _globals['_KUBERNETESMETADATA']._serialized_start = 1776
    _globals['_KUBERNETESMETADATA']._serialized_end = 1999
    _globals['_MONITORINGCONFIG']._serialized_start = 2002
    _globals['_MONITORINGCONFIG']._serialized_end = 2152
    _globals['_MEMBERSHIPSTATE']._serialized_start = 2155
    _globals['_MEMBERSHIPSTATE']._serialized_end = 2342
    _globals['_MEMBERSHIPSTATE_CODE']._serialized_start = 2239
    _globals['_MEMBERSHIPSTATE_CODE']._serialized_end = 2342
    _globals['_AUTHORITY']._serialized_start = 2344
    _globals['_AUTHORITY']._serialized_end = 2469