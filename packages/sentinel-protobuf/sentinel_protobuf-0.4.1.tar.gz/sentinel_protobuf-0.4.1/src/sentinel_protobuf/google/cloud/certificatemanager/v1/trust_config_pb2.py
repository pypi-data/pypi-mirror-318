"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_runtime_version.ValidateProtobufRuntimeVersion(_runtime_version.Domain.PUBLIC, 5, 28, 1, '', 'google/cloud/certificatemanager/v1/trust_config.proto')
_sym_db = _symbol_database.Default()
from .....google.api import field_behavior_pb2 as google_dot_api_dot_field__behavior__pb2
from .....google.api import resource_pb2 as google_dot_api_dot_resource__pb2
from google.protobuf import field_mask_pb2 as google_dot_protobuf_dot_field__mask__pb2
from google.protobuf import timestamp_pb2 as google_dot_protobuf_dot_timestamp__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n5google/cloud/certificatemanager/v1/trust_config.proto\x12"google.cloud.certificatemanager.v1\x1a\x1fgoogle/api/field_behavior.proto\x1a\x19google/api/resource.proto\x1a google/protobuf/field_mask.proto\x1a\x1fgoogle/protobuf/timestamp.proto"\x9d\x01\n\x17ListTrustConfigsRequest\x129\n\x06parent\x18\x01 \x01(\tB)\xe0A\x02\xfaA#\n!locations.googleapis.com/Location\x12\x11\n\tpage_size\x18\x02 \x01(\x05\x12\x12\n\npage_token\x18\x03 \x01(\t\x12\x0e\n\x06filter\x18\x04 \x01(\t\x12\x10\n\x08order_by\x18\x05 \x01(\t"\x90\x01\n\x18ListTrustConfigsResponse\x12F\n\rtrust_configs\x18\x01 \x03(\x0b2/.google.cloud.certificatemanager.v1.TrustConfig\x12\x17\n\x0fnext_page_token\x18\x02 \x01(\t\x12\x13\n\x0bunreachable\x18\x03 \x03(\t"\\\n\x15GetTrustConfigRequest\x12C\n\x04name\x18\x01 \x01(\tB5\xe0A\x02\xfaA/\n-certificatemanager.googleapis.com/TrustConfig"\xbf\x01\n\x18CreateTrustConfigRequest\x129\n\x06parent\x18\x01 \x01(\tB)\xe0A\x02\xfaA#\n!locations.googleapis.com/Location\x12\x1c\n\x0ftrust_config_id\x18\x02 \x01(\tB\x03\xe0A\x02\x12J\n\x0ctrust_config\x18\x03 \x01(\x0b2/.google.cloud.certificatemanager.v1.TrustConfigB\x03\xe0A\x02"\x9c\x01\n\x18UpdateTrustConfigRequest\x12J\n\x0ctrust_config\x18\x01 \x01(\x0b2/.google.cloud.certificatemanager.v1.TrustConfigB\x03\xe0A\x02\x124\n\x0bupdate_mask\x18\x02 \x01(\x0b2\x1a.google.protobuf.FieldMaskB\x03\xe0A\x02"m\n\x18DeleteTrustConfigRequest\x12C\n\x04name\x18\x01 \x01(\tB5\xe0A\x02\xfaA/\n-certificatemanager.googleapis.com/TrustConfig\x12\x0c\n\x04etag\x18\x02 \x01(\t"\x95\x06\n\x0bTrustConfig\x12\x0c\n\x04name\x18\x01 \x01(\t\x124\n\x0bcreate_time\x18\x02 \x01(\x0b2\x1a.google.protobuf.TimestampB\x03\xe0A\x03\x124\n\x0bupdate_time\x18\x03 \x01(\x0b2\x1a.google.protobuf.TimestampB\x03\xe0A\x03\x12K\n\x06labels\x18\x04 \x03(\x0b2;.google.cloud.certificatemanager.v1.TrustConfig.LabelsEntry\x12\x13\n\x0bdescription\x18\x05 \x01(\t\x12\x0c\n\x04etag\x18\x06 \x01(\t\x12P\n\x0ctrust_stores\x18\x08 \x03(\x0b2:.google.cloud.certificatemanager.v1.TrustConfig.TrustStore\x1a0\n\x0bTrustAnchor\x12\x19\n\x0fpem_certificate\x18\x01 \x01(\tH\x00B\x06\n\x04kind\x1a3\n\x0eIntermediateCA\x12\x19\n\x0fpem_certificate\x18\x01 \x01(\tH\x00B\x06\n\x04kind\x1a\xba\x01\n\nTrustStore\x12R\n\rtrust_anchors\x18\x01 \x03(\x0b2;.google.cloud.certificatemanager.v1.TrustConfig.TrustAnchor\x12X\n\x10intermediate_cas\x18\x02 \x03(\x0b2>.google.cloud.certificatemanager.v1.TrustConfig.IntermediateCA\x1a-\n\x0bLabelsEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\r\n\x05value\x18\x02 \x01(\t:\x028\x01:w\xeaAt\n-certificatemanager.googleapis.com/TrustConfig\x12Cprojects/{project}/locations/{location}/trustConfigs/{trust_config}B\x86\x02\n&com.google.cloud.certificatemanager.v1B\x10TrustConifgProtoP\x01ZVcloud.google.com/go/certificatemanager/apiv1/certificatemanagerpb;certificatemanagerpb\xaa\x02"Google.Cloud.CertificateManager.V1\xca\x02"Google\\Cloud\\CertificateManager\\V1\xea\x02%Google::Cloud::CertificateManager::V1b\x06proto3')
_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'google.cloud.certificatemanager.v1.trust_config_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
    _globals['DESCRIPTOR']._loaded_options = None
    _globals['DESCRIPTOR']._serialized_options = b'\n&com.google.cloud.certificatemanager.v1B\x10TrustConifgProtoP\x01ZVcloud.google.com/go/certificatemanager/apiv1/certificatemanagerpb;certificatemanagerpb\xaa\x02"Google.Cloud.CertificateManager.V1\xca\x02"Google\\Cloud\\CertificateManager\\V1\xea\x02%Google::Cloud::CertificateManager::V1'
    _globals['_LISTTRUSTCONFIGSREQUEST'].fields_by_name['parent']._loaded_options = None
    _globals['_LISTTRUSTCONFIGSREQUEST'].fields_by_name['parent']._serialized_options = b'\xe0A\x02\xfaA#\n!locations.googleapis.com/Location'
    _globals['_GETTRUSTCONFIGREQUEST'].fields_by_name['name']._loaded_options = None
    _globals['_GETTRUSTCONFIGREQUEST'].fields_by_name['name']._serialized_options = b'\xe0A\x02\xfaA/\n-certificatemanager.googleapis.com/TrustConfig'
    _globals['_CREATETRUSTCONFIGREQUEST'].fields_by_name['parent']._loaded_options = None
    _globals['_CREATETRUSTCONFIGREQUEST'].fields_by_name['parent']._serialized_options = b'\xe0A\x02\xfaA#\n!locations.googleapis.com/Location'
    _globals['_CREATETRUSTCONFIGREQUEST'].fields_by_name['trust_config_id']._loaded_options = None
    _globals['_CREATETRUSTCONFIGREQUEST'].fields_by_name['trust_config_id']._serialized_options = b'\xe0A\x02'
    _globals['_CREATETRUSTCONFIGREQUEST'].fields_by_name['trust_config']._loaded_options = None
    _globals['_CREATETRUSTCONFIGREQUEST'].fields_by_name['trust_config']._serialized_options = b'\xe0A\x02'
    _globals['_UPDATETRUSTCONFIGREQUEST'].fields_by_name['trust_config']._loaded_options = None
    _globals['_UPDATETRUSTCONFIGREQUEST'].fields_by_name['trust_config']._serialized_options = b'\xe0A\x02'
    _globals['_UPDATETRUSTCONFIGREQUEST'].fields_by_name['update_mask']._loaded_options = None
    _globals['_UPDATETRUSTCONFIGREQUEST'].fields_by_name['update_mask']._serialized_options = b'\xe0A\x02'
    _globals['_DELETETRUSTCONFIGREQUEST'].fields_by_name['name']._loaded_options = None
    _globals['_DELETETRUSTCONFIGREQUEST'].fields_by_name['name']._serialized_options = b'\xe0A\x02\xfaA/\n-certificatemanager.googleapis.com/TrustConfig'
    _globals['_TRUSTCONFIG_LABELSENTRY']._loaded_options = None
    _globals['_TRUSTCONFIG_LABELSENTRY']._serialized_options = b'8\x01'
    _globals['_TRUSTCONFIG'].fields_by_name['create_time']._loaded_options = None
    _globals['_TRUSTCONFIG'].fields_by_name['create_time']._serialized_options = b'\xe0A\x03'
    _globals['_TRUSTCONFIG'].fields_by_name['update_time']._loaded_options = None
    _globals['_TRUSTCONFIG'].fields_by_name['update_time']._serialized_options = b'\xe0A\x03'
    _globals['_TRUSTCONFIG']._loaded_options = None
    _globals['_TRUSTCONFIG']._serialized_options = b'\xeaAt\n-certificatemanager.googleapis.com/TrustConfig\x12Cprojects/{project}/locations/{location}/trustConfigs/{trust_config}'
    _globals['_LISTTRUSTCONFIGSREQUEST']._serialized_start = 221
    _globals['_LISTTRUSTCONFIGSREQUEST']._serialized_end = 378
    _globals['_LISTTRUSTCONFIGSRESPONSE']._serialized_start = 381
    _globals['_LISTTRUSTCONFIGSRESPONSE']._serialized_end = 525
    _globals['_GETTRUSTCONFIGREQUEST']._serialized_start = 527
    _globals['_GETTRUSTCONFIGREQUEST']._serialized_end = 619
    _globals['_CREATETRUSTCONFIGREQUEST']._serialized_start = 622
    _globals['_CREATETRUSTCONFIGREQUEST']._serialized_end = 813
    _globals['_UPDATETRUSTCONFIGREQUEST']._serialized_start = 816
    _globals['_UPDATETRUSTCONFIGREQUEST']._serialized_end = 972
    _globals['_DELETETRUSTCONFIGREQUEST']._serialized_start = 974
    _globals['_DELETETRUSTCONFIGREQUEST']._serialized_end = 1083
    _globals['_TRUSTCONFIG']._serialized_start = 1086
    _globals['_TRUSTCONFIG']._serialized_end = 1875
    _globals['_TRUSTCONFIG_TRUSTANCHOR']._serialized_start = 1417
    _globals['_TRUSTCONFIG_TRUSTANCHOR']._serialized_end = 1465
    _globals['_TRUSTCONFIG_INTERMEDIATECA']._serialized_start = 1467
    _globals['_TRUSTCONFIG_INTERMEDIATECA']._serialized_end = 1518
    _globals['_TRUSTCONFIG_TRUSTSTORE']._serialized_start = 1521
    _globals['_TRUSTCONFIG_TRUSTSTORE']._serialized_end = 1707
    _globals['_TRUSTCONFIG_LABELSENTRY']._serialized_start = 1709
    _globals['_TRUSTCONFIG_LABELSENTRY']._serialized_end = 1754