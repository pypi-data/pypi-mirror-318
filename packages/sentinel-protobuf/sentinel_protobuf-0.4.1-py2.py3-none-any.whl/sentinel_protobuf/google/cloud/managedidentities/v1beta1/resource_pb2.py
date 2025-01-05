"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_runtime_version.ValidateProtobufRuntimeVersion(_runtime_version.Domain.PUBLIC, 5, 28, 1, '', 'google/cloud/managedidentities/v1beta1/resource.proto')
_sym_db = _symbol_database.Default()
from .....google.api import field_behavior_pb2 as google_dot_api_dot_field__behavior__pb2
from .....google.api import resource_pb2 as google_dot_api_dot_resource__pb2
from google.protobuf import timestamp_pb2 as google_dot_protobuf_dot_timestamp__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n5google/cloud/managedidentities/v1beta1/resource.proto\x12&google.cloud.managedidentities.v1beta1\x1a\x1fgoogle/api/field_behavior.proto\x1a\x19google/api/resource.proto\x1a\x1fgoogle/protobuf/timestamp.proto"\xad\x06\n\x06Domain\x12\x11\n\x04name\x18\x01 \x01(\tB\x03\xe0A\x03\x12O\n\x06labels\x18\x02 \x03(\x0b2:.google.cloud.managedidentities.v1beta1.Domain.LabelsEntryB\x03\xe0A\x01\x12 \n\x13authorized_networks\x18\x03 \x03(\tB\x03\xe0A\x01\x12\x1e\n\x11reserved_ip_range\x18\x04 \x01(\tB\x03\xe0A\x02\x12\x16\n\tlocations\x18\x05 \x03(\tB\x03\xe0A\x02\x12\x12\n\x05admin\x18\x06 \x01(\tB\x03\xe0A\x01\x12\x11\n\x04fqdn\x18\n \x01(\tB\x03\xe0A\x03\x124\n\x0bcreate_time\x18\x0b \x01(\x0b2\x1a.google.protobuf.TimestampB\x03\xe0A\x03\x124\n\x0bupdate_time\x18\x0c \x01(\x0b2\x1a.google.protobuf.TimestampB\x03\xe0A\x03\x12H\n\x05state\x18\r \x01(\x0e24.google.cloud.managedidentities.v1beta1.Domain.StateB\x03\xe0A\x03\x12\x1b\n\x0estatus_message\x18\x0e \x01(\tB\x03\xe0A\x03\x12B\n\x06trusts\x18\x0f \x03(\x0b2-.google.cloud.managedidentities.v1beta1.TrustB\x03\xe0A\x03\x1a-\n\x0bLabelsEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\r\n\x05value\x18\x02 \x01(\t:\x028\x01"\x8f\x01\n\x05State\x12\x15\n\x11STATE_UNSPECIFIED\x10\x00\x12\x0c\n\x08CREATING\x10\x01\x12\t\n\x05READY\x10\x02\x12\x0c\n\x08UPDATING\x10\x03\x12\x0c\n\x08DELETING\x10\x04\x12\r\n\tREPAIRING\x10\x05\x12\x1a\n\x16PERFORMING_MAINTENANCE\x10\x06\x12\x0f\n\x0bUNAVAILABLE\x10\x07:f\xeaAc\n\'managedidentities.googleapis.com/Domain\x128projects/{project}/locations/{location}/domains/{domain}"\xd7\x06\n\x05Trust\x12\x1a\n\x12target_domain_name\x18\x01 \x01(\t\x12K\n\ntrust_type\x18\x02 \x01(\x0e27.google.cloud.managedidentities.v1beta1.Trust.TrustType\x12U\n\x0ftrust_direction\x18\x03 \x01(\x0e2<.google.cloud.managedidentities.v1beta1.Trust.TrustDirection\x12 \n\x18selective_authentication\x18\x04 \x01(\x08\x12\x1f\n\x17target_dns_ip_addresses\x18\x05 \x03(\t\x12#\n\x16trust_handshake_secret\x18\x06 \x01(\tB\x03\xe0A\x04\x124\n\x0bcreate_time\x18\x07 \x01(\x0b2\x1a.google.protobuf.TimestampB\x03\xe0A\x03\x124\n\x0bupdate_time\x18\x08 \x01(\x0b2\x1a.google.protobuf.TimestampB\x03\xe0A\x03\x12G\n\x05state\x18\t \x01(\x0e23.google.cloud.managedidentities.v1beta1.Trust.StateB\x03\xe0A\x03\x12\x1e\n\x11state_description\x18\x0b \x01(\tB\x03\xe0A\x03\x12B\n\x19last_trust_heartbeat_time\x18\x0c \x01(\x0b2\x1a.google.protobuf.TimestampB\x03\xe0A\x03"i\n\x05State\x12\x15\n\x11STATE_UNSPECIFIED\x10\x00\x12\x0c\n\x08CREATING\x10\x01\x12\x0c\n\x08UPDATING\x10\x02\x12\x0c\n\x08DELETING\x10\x03\x12\r\n\tCONNECTED\x10\x04\x12\x10\n\x0cDISCONNECTED\x10\x05"A\n\tTrustType\x12\x1a\n\x16TRUST_TYPE_UNSPECIFIED\x10\x00\x12\n\n\x06FOREST\x10\x01\x12\x0c\n\x08EXTERNAL\x10\x02"_\n\x0eTrustDirection\x12\x1f\n\x1bTRUST_DIRECTION_UNSPECIFIED\x10\x00\x12\x0b\n\x07INBOUND\x10\x01\x12\x0c\n\x08OUTBOUND\x10\x02\x12\x11\n\rBIDIRECTIONAL\x10\x03B\x95\x02\n*com.google.cloud.managedidentities.v1beta1B\rResourceProtoP\x01ZXcloud.google.com/go/managedidentities/apiv1beta1/managedidentitiespb;managedidentitiespb\xaa\x02&Google.Cloud.ManagedIdentities.V1Beta1\xca\x02&Google\\Cloud\\ManagedIdentities\\V1beta1\xea\x02)Google::Cloud::ManagedIdentities::V1beta1b\x06proto3')
_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'google.cloud.managedidentities.v1beta1.resource_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
    _globals['DESCRIPTOR']._loaded_options = None
    _globals['DESCRIPTOR']._serialized_options = b'\n*com.google.cloud.managedidentities.v1beta1B\rResourceProtoP\x01ZXcloud.google.com/go/managedidentities/apiv1beta1/managedidentitiespb;managedidentitiespb\xaa\x02&Google.Cloud.ManagedIdentities.V1Beta1\xca\x02&Google\\Cloud\\ManagedIdentities\\V1beta1\xea\x02)Google::Cloud::ManagedIdentities::V1beta1'
    _globals['_DOMAIN_LABELSENTRY']._loaded_options = None
    _globals['_DOMAIN_LABELSENTRY']._serialized_options = b'8\x01'
    _globals['_DOMAIN'].fields_by_name['name']._loaded_options = None
    _globals['_DOMAIN'].fields_by_name['name']._serialized_options = b'\xe0A\x03'
    _globals['_DOMAIN'].fields_by_name['labels']._loaded_options = None
    _globals['_DOMAIN'].fields_by_name['labels']._serialized_options = b'\xe0A\x01'
    _globals['_DOMAIN'].fields_by_name['authorized_networks']._loaded_options = None
    _globals['_DOMAIN'].fields_by_name['authorized_networks']._serialized_options = b'\xe0A\x01'
    _globals['_DOMAIN'].fields_by_name['reserved_ip_range']._loaded_options = None
    _globals['_DOMAIN'].fields_by_name['reserved_ip_range']._serialized_options = b'\xe0A\x02'
    _globals['_DOMAIN'].fields_by_name['locations']._loaded_options = None
    _globals['_DOMAIN'].fields_by_name['locations']._serialized_options = b'\xe0A\x02'
    _globals['_DOMAIN'].fields_by_name['admin']._loaded_options = None
    _globals['_DOMAIN'].fields_by_name['admin']._serialized_options = b'\xe0A\x01'
    _globals['_DOMAIN'].fields_by_name['fqdn']._loaded_options = None
    _globals['_DOMAIN'].fields_by_name['fqdn']._serialized_options = b'\xe0A\x03'
    _globals['_DOMAIN'].fields_by_name['create_time']._loaded_options = None
    _globals['_DOMAIN'].fields_by_name['create_time']._serialized_options = b'\xe0A\x03'
    _globals['_DOMAIN'].fields_by_name['update_time']._loaded_options = None
    _globals['_DOMAIN'].fields_by_name['update_time']._serialized_options = b'\xe0A\x03'
    _globals['_DOMAIN'].fields_by_name['state']._loaded_options = None
    _globals['_DOMAIN'].fields_by_name['state']._serialized_options = b'\xe0A\x03'
    _globals['_DOMAIN'].fields_by_name['status_message']._loaded_options = None
    _globals['_DOMAIN'].fields_by_name['status_message']._serialized_options = b'\xe0A\x03'
    _globals['_DOMAIN'].fields_by_name['trusts']._loaded_options = None
    _globals['_DOMAIN'].fields_by_name['trusts']._serialized_options = b'\xe0A\x03'
    _globals['_DOMAIN']._loaded_options = None
    _globals['_DOMAIN']._serialized_options = b"\xeaAc\n'managedidentities.googleapis.com/Domain\x128projects/{project}/locations/{location}/domains/{domain}"
    _globals['_TRUST'].fields_by_name['trust_handshake_secret']._loaded_options = None
    _globals['_TRUST'].fields_by_name['trust_handshake_secret']._serialized_options = b'\xe0A\x04'
    _globals['_TRUST'].fields_by_name['create_time']._loaded_options = None
    _globals['_TRUST'].fields_by_name['create_time']._serialized_options = b'\xe0A\x03'
    _globals['_TRUST'].fields_by_name['update_time']._loaded_options = None
    _globals['_TRUST'].fields_by_name['update_time']._serialized_options = b'\xe0A\x03'
    _globals['_TRUST'].fields_by_name['state']._loaded_options = None
    _globals['_TRUST'].fields_by_name['state']._serialized_options = b'\xe0A\x03'
    _globals['_TRUST'].fields_by_name['state_description']._loaded_options = None
    _globals['_TRUST'].fields_by_name['state_description']._serialized_options = b'\xe0A\x03'
    _globals['_TRUST'].fields_by_name['last_trust_heartbeat_time']._loaded_options = None
    _globals['_TRUST'].fields_by_name['last_trust_heartbeat_time']._serialized_options = b'\xe0A\x03'
    _globals['_DOMAIN']._serialized_start = 191
    _globals['_DOMAIN']._serialized_end = 1004
    _globals['_DOMAIN_LABELSENTRY']._serialized_start = 709
    _globals['_DOMAIN_LABELSENTRY']._serialized_end = 754
    _globals['_DOMAIN_STATE']._serialized_start = 757
    _globals['_DOMAIN_STATE']._serialized_end = 900
    _globals['_TRUST']._serialized_start = 1007
    _globals['_TRUST']._serialized_end = 1862
    _globals['_TRUST_STATE']._serialized_start = 1593
    _globals['_TRUST_STATE']._serialized_end = 1698
    _globals['_TRUST_TRUSTTYPE']._serialized_start = 1700
    _globals['_TRUST_TRUSTTYPE']._serialized_end = 1765
    _globals['_TRUST_TRUSTDIRECTION']._serialized_start = 1767
    _globals['_TRUST_TRUSTDIRECTION']._serialized_end = 1862