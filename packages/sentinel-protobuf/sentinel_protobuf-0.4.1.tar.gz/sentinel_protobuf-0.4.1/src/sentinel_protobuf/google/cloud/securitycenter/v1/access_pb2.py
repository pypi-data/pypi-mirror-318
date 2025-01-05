"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_runtime_version.ValidateProtobufRuntimeVersion(_runtime_version.Domain.PUBLIC, 5, 28, 1, '', 'google/cloud/securitycenter/v1/access.proto')
_sym_db = _symbol_database.Default()
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n+google/cloud/securitycenter/v1/access.proto\x12\x1egoogle.cloud.securitycenter.v1"\x89\x03\n\x06Access\x12\x17\n\x0fprincipal_email\x18\x01 \x01(\t\x12\x11\n\tcaller_ip\x18\x02 \x01(\t\x12B\n\rcaller_ip_geo\x18\x03 \x01(\x0b2+.google.cloud.securitycenter.v1.Geolocation\x12\x19\n\x11user_agent_family\x18\x04 \x01(\t\x12\x12\n\nuser_agent\x18\x0c \x01(\t\x12\x14\n\x0cservice_name\x18\x05 \x01(\t\x12\x13\n\x0bmethod_name\x18\x06 \x01(\t\x12\x19\n\x11principal_subject\x18\x07 \x01(\t\x12 \n\x18service_account_key_name\x18\x08 \x01(\t\x12e\n\x1fservice_account_delegation_info\x18\t \x03(\x0b2<.google.cloud.securitycenter.v1.ServiceAccountDelegationInfo\x12\x11\n\tuser_name\x18\x0b \x01(\t"R\n\x1cServiceAccountDelegationInfo\x12\x17\n\x0fprincipal_email\x18\x01 \x01(\t\x12\x19\n\x11principal_subject\x18\x02 \x01(\t""\n\x0bGeolocation\x12\x13\n\x0bregion_code\x18\x01 \x01(\tB\xe5\x01\n"com.google.cloud.securitycenter.v1B\x0bAccessProtoP\x01ZJcloud.google.com/go/securitycenter/apiv1/securitycenterpb;securitycenterpb\xaa\x02\x1eGoogle.Cloud.SecurityCenter.V1\xca\x02\x1eGoogle\\Cloud\\SecurityCenter\\V1\xea\x02!Google::Cloud::SecurityCenter::V1b\x06proto3')
_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'google.cloud.securitycenter.v1.access_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
    _globals['DESCRIPTOR']._loaded_options = None
    _globals['DESCRIPTOR']._serialized_options = b'\n"com.google.cloud.securitycenter.v1B\x0bAccessProtoP\x01ZJcloud.google.com/go/securitycenter/apiv1/securitycenterpb;securitycenterpb\xaa\x02\x1eGoogle.Cloud.SecurityCenter.V1\xca\x02\x1eGoogle\\Cloud\\SecurityCenter\\V1\xea\x02!Google::Cloud::SecurityCenter::V1'
    _globals['_ACCESS']._serialized_start = 80
    _globals['_ACCESS']._serialized_end = 473
    _globals['_SERVICEACCOUNTDELEGATIONINFO']._serialized_start = 475
    _globals['_SERVICEACCOUNTDELEGATIONINFO']._serialized_end = 557
    _globals['_GEOLOCATION']._serialized_start = 559
    _globals['_GEOLOCATION']._serialized_end = 593