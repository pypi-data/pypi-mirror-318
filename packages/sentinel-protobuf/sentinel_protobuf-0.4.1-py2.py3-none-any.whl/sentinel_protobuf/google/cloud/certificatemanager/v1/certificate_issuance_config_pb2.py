"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_runtime_version.ValidateProtobufRuntimeVersion(_runtime_version.Domain.PUBLIC, 5, 28, 1, '', 'google/cloud/certificatemanager/v1/certificate_issuance_config.proto')
_sym_db = _symbol_database.Default()
from .....google.api import field_behavior_pb2 as google_dot_api_dot_field__behavior__pb2
from .....google.api import resource_pb2 as google_dot_api_dot_resource__pb2
from google.protobuf import duration_pb2 as google_dot_protobuf_dot_duration__pb2
from google.protobuf import timestamp_pb2 as google_dot_protobuf_dot_timestamp__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\nDgoogle/cloud/certificatemanager/v1/certificate_issuance_config.proto\x12"google.cloud.certificatemanager.v1\x1a\x1fgoogle/api/field_behavior.proto\x1a\x19google/api/resource.proto\x1a\x1egoogle/protobuf/duration.proto\x1a\x1fgoogle/protobuf/timestamp.proto"\xab\x01\n%ListCertificateIssuanceConfigsRequest\x129\n\x06parent\x18\x01 \x01(\tB)\xe0A\x02\xfaA#\n!locations.googleapis.com/Location\x12\x11\n\tpage_size\x18\x02 \x01(\x05\x12\x12\n\npage_token\x18\x03 \x01(\t\x12\x0e\n\x06filter\x18\x04 \x01(\t\x12\x10\n\x08order_by\x18\x05 \x01(\t"\xbb\x01\n&ListCertificateIssuanceConfigsResponse\x12c\n\x1ccertificate_issuance_configs\x18\x01 \x03(\x0b2=.google.cloud.certificatemanager.v1.CertificateIssuanceConfig\x12\x17\n\x0fnext_page_token\x18\x02 \x01(\t\x12\x13\n\x0bunreachable\x18\x03 \x03(\t"x\n#GetCertificateIssuanceConfigRequest\x12Q\n\x04name\x18\x01 \x01(\tBC\xe0A\x02\xfaA=\n;certificatemanager.googleapis.com/CertificateIssuanceConfig"\xf9\x01\n&CreateCertificateIssuanceConfigRequest\x129\n\x06parent\x18\x01 \x01(\tB)\xe0A\x02\xfaA#\n!locations.googleapis.com/Location\x12+\n\x1ecertificate_issuance_config_id\x18\x02 \x01(\tB\x03\xe0A\x02\x12g\n\x1bcertificate_issuance_config\x18\x03 \x01(\x0b2=.google.cloud.certificatemanager.v1.CertificateIssuanceConfigB\x03\xe0A\x02"{\n&DeleteCertificateIssuanceConfigRequest\x12Q\n\x04name\x18\x01 \x01(\tBC\xe0A\x02\xfaA=\n;certificatemanager.googleapis.com/CertificateIssuanceConfig"\xa3\t\n\x19CertificateIssuanceConfig\x12\x0c\n\x04name\x18\x01 \x01(\t\x124\n\x0bcreate_time\x18\x02 \x01(\x0b2\x1a.google.protobuf.TimestampB\x03\xe0A\x03\x124\n\x0bupdate_time\x18\x03 \x01(\x0b2\x1a.google.protobuf.TimestampB\x03\xe0A\x03\x12Y\n\x06labels\x18\x04 \x03(\x0b2I.google.cloud.certificatemanager.v1.CertificateIssuanceConfig.LabelsEntry\x12\x13\n\x0bdescription\x18\x05 \x01(\t\x12\x83\x01\n\x1ccertificate_authority_config\x18\x06 \x01(\x0b2X.google.cloud.certificatemanager.v1.CertificateIssuanceConfig.CertificateAuthorityConfigB\x03\xe0A\x02\x120\n\x08lifetime\x18\x07 \x01(\x0b2\x19.google.protobuf.DurationB\x03\xe0A\x02\x12\'\n\x1arotation_window_percentage\x18\x08 \x01(\x05B\x03\xe0A\x02\x12f\n\rkey_algorithm\x18\t \x01(\x0e2J.google.cloud.certificatemanager.v1.CertificateIssuanceConfig.KeyAlgorithmB\x03\xe0A\x02\x1a\xb0\x02\n\x1aCertificateAuthorityConfig\x12\xaa\x01\n$certificate_authority_service_config\x18\x01 \x01(\x0b2z.google.cloud.certificatemanager.v1.CertificateIssuanceConfig.CertificateAuthorityConfig.CertificateAuthorityServiceConfigH\x00\x1a]\n!CertificateAuthorityServiceConfig\x128\n\x07ca_pool\x18\x01 \x01(\tB\'\xe0A\x02\xfaA!\n\x1fprivateca.googleapis.com/CaPoolB\x06\n\x04kind\x1a-\n\x0bLabelsEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\r\n\x05value\x18\x02 \x01(\t:\x028\x01"K\n\x0cKeyAlgorithm\x12\x1d\n\x19KEY_ALGORITHM_UNSPECIFIED\x10\x00\x12\x0c\n\x08RSA_2048\x10\x01\x12\x0e\n\nECDSA_P256\x10\x04:\xa3\x01\xeaA\x9f\x01\n;certificatemanager.googleapis.com/CertificateIssuanceConfig\x12`projects/{project}/locations/{location}/certificateIssuanceConfigs/{certificate_issuance_config}B\xf3\x02\n&com.google.cloud.certificatemanager.v1B\x1eCertificateIssuanceConfigProtoP\x01ZVcloud.google.com/go/certificatemanager/apiv1/certificatemanagerpb;certificatemanagerpb\xaa\x02"Google.Cloud.CertificateManager.V1\xca\x02"Google\\Cloud\\CertificateManager\\V1\xea\x02%Google::Cloud::CertificateManager::V1\xeaA\\\n\x1fprivateca.googleapis.com/CaPool\x129projects/{project}/locations/{location}/caPools/{ca_pool}b\x06proto3')
_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'google.cloud.certificatemanager.v1.certificate_issuance_config_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
    _globals['DESCRIPTOR']._loaded_options = None
    _globals['DESCRIPTOR']._serialized_options = b'\n&com.google.cloud.certificatemanager.v1B\x1eCertificateIssuanceConfigProtoP\x01ZVcloud.google.com/go/certificatemanager/apiv1/certificatemanagerpb;certificatemanagerpb\xaa\x02"Google.Cloud.CertificateManager.V1\xca\x02"Google\\Cloud\\CertificateManager\\V1\xea\x02%Google::Cloud::CertificateManager::V1\xeaA\\\n\x1fprivateca.googleapis.com/CaPool\x129projects/{project}/locations/{location}/caPools/{ca_pool}'
    _globals['_LISTCERTIFICATEISSUANCECONFIGSREQUEST'].fields_by_name['parent']._loaded_options = None
    _globals['_LISTCERTIFICATEISSUANCECONFIGSREQUEST'].fields_by_name['parent']._serialized_options = b'\xe0A\x02\xfaA#\n!locations.googleapis.com/Location'
    _globals['_GETCERTIFICATEISSUANCECONFIGREQUEST'].fields_by_name['name']._loaded_options = None
    _globals['_GETCERTIFICATEISSUANCECONFIGREQUEST'].fields_by_name['name']._serialized_options = b'\xe0A\x02\xfaA=\n;certificatemanager.googleapis.com/CertificateIssuanceConfig'
    _globals['_CREATECERTIFICATEISSUANCECONFIGREQUEST'].fields_by_name['parent']._loaded_options = None
    _globals['_CREATECERTIFICATEISSUANCECONFIGREQUEST'].fields_by_name['parent']._serialized_options = b'\xe0A\x02\xfaA#\n!locations.googleapis.com/Location'
    _globals['_CREATECERTIFICATEISSUANCECONFIGREQUEST'].fields_by_name['certificate_issuance_config_id']._loaded_options = None
    _globals['_CREATECERTIFICATEISSUANCECONFIGREQUEST'].fields_by_name['certificate_issuance_config_id']._serialized_options = b'\xe0A\x02'
    _globals['_CREATECERTIFICATEISSUANCECONFIGREQUEST'].fields_by_name['certificate_issuance_config']._loaded_options = None
    _globals['_CREATECERTIFICATEISSUANCECONFIGREQUEST'].fields_by_name['certificate_issuance_config']._serialized_options = b'\xe0A\x02'
    _globals['_DELETECERTIFICATEISSUANCECONFIGREQUEST'].fields_by_name['name']._loaded_options = None
    _globals['_DELETECERTIFICATEISSUANCECONFIGREQUEST'].fields_by_name['name']._serialized_options = b'\xe0A\x02\xfaA=\n;certificatemanager.googleapis.com/CertificateIssuanceConfig'
    _globals['_CERTIFICATEISSUANCECONFIG_CERTIFICATEAUTHORITYCONFIG_CERTIFICATEAUTHORITYSERVICECONFIG'].fields_by_name['ca_pool']._loaded_options = None
    _globals['_CERTIFICATEISSUANCECONFIG_CERTIFICATEAUTHORITYCONFIG_CERTIFICATEAUTHORITYSERVICECONFIG'].fields_by_name['ca_pool']._serialized_options = b'\xe0A\x02\xfaA!\n\x1fprivateca.googleapis.com/CaPool'
    _globals['_CERTIFICATEISSUANCECONFIG_LABELSENTRY']._loaded_options = None
    _globals['_CERTIFICATEISSUANCECONFIG_LABELSENTRY']._serialized_options = b'8\x01'
    _globals['_CERTIFICATEISSUANCECONFIG'].fields_by_name['create_time']._loaded_options = None
    _globals['_CERTIFICATEISSUANCECONFIG'].fields_by_name['create_time']._serialized_options = b'\xe0A\x03'
    _globals['_CERTIFICATEISSUANCECONFIG'].fields_by_name['update_time']._loaded_options = None
    _globals['_CERTIFICATEISSUANCECONFIG'].fields_by_name['update_time']._serialized_options = b'\xe0A\x03'
    _globals['_CERTIFICATEISSUANCECONFIG'].fields_by_name['certificate_authority_config']._loaded_options = None
    _globals['_CERTIFICATEISSUANCECONFIG'].fields_by_name['certificate_authority_config']._serialized_options = b'\xe0A\x02'
    _globals['_CERTIFICATEISSUANCECONFIG'].fields_by_name['lifetime']._loaded_options = None
    _globals['_CERTIFICATEISSUANCECONFIG'].fields_by_name['lifetime']._serialized_options = b'\xe0A\x02'
    _globals['_CERTIFICATEISSUANCECONFIG'].fields_by_name['rotation_window_percentage']._loaded_options = None
    _globals['_CERTIFICATEISSUANCECONFIG'].fields_by_name['rotation_window_percentage']._serialized_options = b'\xe0A\x02'
    _globals['_CERTIFICATEISSUANCECONFIG'].fields_by_name['key_algorithm']._loaded_options = None
    _globals['_CERTIFICATEISSUANCECONFIG'].fields_by_name['key_algorithm']._serialized_options = b'\xe0A\x02'
    _globals['_CERTIFICATEISSUANCECONFIG']._loaded_options = None
    _globals['_CERTIFICATEISSUANCECONFIG']._serialized_options = b'\xeaA\x9f\x01\n;certificatemanager.googleapis.com/CertificateIssuanceConfig\x12`projects/{project}/locations/{location}/certificateIssuanceConfigs/{certificate_issuance_config}'
    _globals['_LISTCERTIFICATEISSUANCECONFIGSREQUEST']._serialized_start = 234
    _globals['_LISTCERTIFICATEISSUANCECONFIGSREQUEST']._serialized_end = 405
    _globals['_LISTCERTIFICATEISSUANCECONFIGSRESPONSE']._serialized_start = 408
    _globals['_LISTCERTIFICATEISSUANCECONFIGSRESPONSE']._serialized_end = 595
    _globals['_GETCERTIFICATEISSUANCECONFIGREQUEST']._serialized_start = 597
    _globals['_GETCERTIFICATEISSUANCECONFIGREQUEST']._serialized_end = 717
    _globals['_CREATECERTIFICATEISSUANCECONFIGREQUEST']._serialized_start = 720
    _globals['_CREATECERTIFICATEISSUANCECONFIGREQUEST']._serialized_end = 969
    _globals['_DELETECERTIFICATEISSUANCECONFIGREQUEST']._serialized_start = 971
    _globals['_DELETECERTIFICATEISSUANCECONFIGREQUEST']._serialized_end = 1094
    _globals['_CERTIFICATEISSUANCECONFIG']._serialized_start = 1097
    _globals['_CERTIFICATEISSUANCECONFIG']._serialized_end = 2284
    _globals['_CERTIFICATEISSUANCECONFIG_CERTIFICATEAUTHORITYCONFIG']._serialized_start = 1690
    _globals['_CERTIFICATEISSUANCECONFIG_CERTIFICATEAUTHORITYCONFIG']._serialized_end = 1994
    _globals['_CERTIFICATEISSUANCECONFIG_CERTIFICATEAUTHORITYCONFIG_CERTIFICATEAUTHORITYSERVICECONFIG']._serialized_start = 1893
    _globals['_CERTIFICATEISSUANCECONFIG_CERTIFICATEAUTHORITYCONFIG_CERTIFICATEAUTHORITYSERVICECONFIG']._serialized_end = 1986
    _globals['_CERTIFICATEISSUANCECONFIG_LABELSENTRY']._serialized_start = 1996
    _globals['_CERTIFICATEISSUANCECONFIG_LABELSENTRY']._serialized_end = 2041
    _globals['_CERTIFICATEISSUANCECONFIG_KEYALGORITHM']._serialized_start = 2043
    _globals['_CERTIFICATEISSUANCECONFIG_KEYALGORITHM']._serialized_end = 2118