"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_runtime_version.ValidateProtobufRuntimeVersion(_runtime_version.Domain.PUBLIC, 5, 28, 1, '', 'google/cloud/securitycenter/v1/security_posture.proto')
_sym_db = _symbol_database.Default()
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n5google/cloud/securitycenter/v1/security_posture.proto\x12\x1egoogle.cloud.securitycenter.v1"\xe8\x02\n\x0fSecurityPosture\x12\x0c\n\x04name\x18\x01 \x01(\t\x12\x13\n\x0brevision_id\x18\x02 \x01(\t\x12#\n\x1bposture_deployment_resource\x18\x03 \x01(\t\x12\x1a\n\x12posture_deployment\x18\x04 \x01(\t\x12\x16\n\x0echanged_policy\x18\x05 \x01(\t\x12\x12\n\npolicy_set\x18\x06 \x01(\t\x12\x0e\n\x06policy\x18\x07 \x01(\t\x12`\n\x14policy_drift_details\x18\x08 \x03(\x0b2B.google.cloud.securitycenter.v1.SecurityPosture.PolicyDriftDetails\x1aS\n\x12PolicyDriftDetails\x12\r\n\x05field\x18\x01 \x01(\t\x12\x16\n\x0eexpected_value\x18\x02 \x01(\t\x12\x16\n\x0edetected_value\x18\x03 \x01(\tB\xee\x01\n"com.google.cloud.securitycenter.v1B\x14SecurityPostureProtoP\x01ZJcloud.google.com/go/securitycenter/apiv1/securitycenterpb;securitycenterpb\xaa\x02\x1eGoogle.Cloud.SecurityCenter.V1\xca\x02\x1eGoogle\\Cloud\\SecurityCenter\\V1\xea\x02!Google::Cloud::SecurityCenter::V1b\x06proto3')
_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'google.cloud.securitycenter.v1.security_posture_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
    _globals['DESCRIPTOR']._loaded_options = None
    _globals['DESCRIPTOR']._serialized_options = b'\n"com.google.cloud.securitycenter.v1B\x14SecurityPostureProtoP\x01ZJcloud.google.com/go/securitycenter/apiv1/securitycenterpb;securitycenterpb\xaa\x02\x1eGoogle.Cloud.SecurityCenter.V1\xca\x02\x1eGoogle\\Cloud\\SecurityCenter\\V1\xea\x02!Google::Cloud::SecurityCenter::V1'
    _globals['_SECURITYPOSTURE']._serialized_start = 90
    _globals['_SECURITYPOSTURE']._serialized_end = 450
    _globals['_SECURITYPOSTURE_POLICYDRIFTDETAILS']._serialized_start = 367
    _globals['_SECURITYPOSTURE_POLICYDRIFTDETAILS']._serialized_end = 450