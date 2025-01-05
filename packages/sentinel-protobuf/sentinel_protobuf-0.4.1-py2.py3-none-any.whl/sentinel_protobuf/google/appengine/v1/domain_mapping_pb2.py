"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_runtime_version.ValidateProtobufRuntimeVersion(_runtime_version.Domain.PUBLIC, 5, 28, 1, '', 'google/appengine/v1/domain_mapping.proto')
_sym_db = _symbol_database.Default()
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n(google/appengine/v1/domain_mapping.proto\x12\x13google.appengine.v1"\xa0\x01\n\rDomainMapping\x12\x0c\n\x04name\x18\x01 \x01(\t\x12\n\n\x02id\x18\x02 \x01(\t\x126\n\x0cssl_settings\x18\x03 \x01(\x0b2 .google.appengine.v1.SslSettings\x12=\n\x10resource_records\x18\x04 \x03(\x0b2#.google.appengine.v1.ResourceRecord"\xf3\x01\n\x0bSslSettings\x12\x16\n\x0ecertificate_id\x18\x01 \x01(\t\x12O\n\x13ssl_management_type\x18\x03 \x01(\x0e22.google.appengine.v1.SslSettings.SslManagementType\x12&\n\x1epending_managed_certificate_id\x18\x04 \x01(\t"S\n\x11SslManagementType\x12#\n\x1fSSL_MANAGEMENT_TYPE_UNSPECIFIED\x10\x00\x12\r\n\tAUTOMATIC\x10\x01\x12\n\n\x06MANUAL\x10\x02"\xb3\x01\n\x0eResourceRecord\x12\x0c\n\x04name\x18\x01 \x01(\t\x12\x0e\n\x06rrdata\x18\x02 \x01(\t\x12<\n\x04type\x18\x03 \x01(\x0e2..google.appengine.v1.ResourceRecord.RecordType"E\n\nRecordType\x12\x1b\n\x17RECORD_TYPE_UNSPECIFIED\x10\x00\x12\x05\n\x01A\x10\x01\x12\x08\n\x04AAAA\x10\x02\x12\t\n\x05CNAME\x10\x03B\xc3\x01\n\x17com.google.appengine.v1B\x12DomainMappingProtoP\x01Z;cloud.google.com/go/appengine/apiv1/appenginepb;appenginepb\xaa\x02\x19Google.Cloud.AppEngine.V1\xca\x02\x19Google\\Cloud\\AppEngine\\V1\xea\x02\x1cGoogle::Cloud::AppEngine::V1b\x06proto3')
_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'google.appengine.v1.domain_mapping_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
    _globals['DESCRIPTOR']._loaded_options = None
    _globals['DESCRIPTOR']._serialized_options = b'\n\x17com.google.appengine.v1B\x12DomainMappingProtoP\x01Z;cloud.google.com/go/appengine/apiv1/appenginepb;appenginepb\xaa\x02\x19Google.Cloud.AppEngine.V1\xca\x02\x19Google\\Cloud\\AppEngine\\V1\xea\x02\x1cGoogle::Cloud::AppEngine::V1'
    _globals['_DOMAINMAPPING']._serialized_start = 66
    _globals['_DOMAINMAPPING']._serialized_end = 226
    _globals['_SSLSETTINGS']._serialized_start = 229
    _globals['_SSLSETTINGS']._serialized_end = 472
    _globals['_SSLSETTINGS_SSLMANAGEMENTTYPE']._serialized_start = 389
    _globals['_SSLSETTINGS_SSLMANAGEMENTTYPE']._serialized_end = 472
    _globals['_RESOURCERECORD']._serialized_start = 475
    _globals['_RESOURCERECORD']._serialized_end = 654
    _globals['_RESOURCERECORD_RECORDTYPE']._serialized_start = 585
    _globals['_RESOURCERECORD_RECORDTYPE']._serialized_end = 654