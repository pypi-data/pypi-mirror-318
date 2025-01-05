"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_runtime_version.ValidateProtobufRuntimeVersion(_runtime_version.Domain.PUBLIC, 5, 28, 1, '', 'google/cloud/securitycenter/v2/cloud_armor.proto')
_sym_db = _symbol_database.Default()
from google.protobuf import duration_pb2 as google_dot_protobuf_dot_duration__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n0google/cloud/securitycenter/v2/cloud_armor.proto\x12\x1egoogle.cloud.securitycenter.v2\x1a\x1egoogle/protobuf/duration.proto"\xde\x02\n\nCloudArmor\x12G\n\x0fsecurity_policy\x18\x01 \x01(\x0b2..google.cloud.securitycenter.v2.SecurityPolicy\x12:\n\x08requests\x18\x02 \x01(\x0b2(.google.cloud.securitycenter.v2.Requests\x12O\n\x13adaptive_protection\x18\x03 \x01(\x0b22.google.cloud.securitycenter.v2.AdaptiveProtection\x126\n\x06attack\x18\x04 \x01(\x0b2&.google.cloud.securitycenter.v2.Attack\x12\x15\n\rthreat_vector\x18\x05 \x01(\t\x12+\n\x08duration\x18\x06 \x01(\x0b2\x19.google.protobuf.Duration"=\n\x0eSecurityPolicy\x12\x0c\n\x04name\x18\x01 \x01(\t\x12\x0c\n\x04type\x18\x02 \x01(\t\x12\x0f\n\x07preview\x18\x03 \x01(\x08"j\n\x08Requests\x12\r\n\x05ratio\x18\x01 \x01(\x01\x12\x1a\n\x12short_term_allowed\x18\x02 \x01(\x05\x12\x19\n\x11long_term_allowed\x18\x03 \x01(\x05\x12\x18\n\x10long_term_denied\x18\x04 \x01(\x05"(\n\x12AdaptiveProtection\x12\x12\n\nconfidence\x18\x01 \x01(\x01"H\n\x06Attack\x12\x12\n\nvolume_pps\x18\x01 \x01(\x05\x12\x12\n\nvolume_bps\x18\x02 \x01(\x05\x12\x16\n\x0eclassification\x18\x03 \x01(\tB\xe9\x01\n"com.google.cloud.securitycenter.v2B\x0fCloudArmorProtoP\x01ZJcloud.google.com/go/securitycenter/apiv2/securitycenterpb;securitycenterpb\xaa\x02\x1eGoogle.Cloud.SecurityCenter.V2\xca\x02\x1eGoogle\\Cloud\\SecurityCenter\\V2\xea\x02!Google::Cloud::SecurityCenter::V2b\x06proto3')
_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'google.cloud.securitycenter.v2.cloud_armor_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
    _globals['DESCRIPTOR']._loaded_options = None
    _globals['DESCRIPTOR']._serialized_options = b'\n"com.google.cloud.securitycenter.v2B\x0fCloudArmorProtoP\x01ZJcloud.google.com/go/securitycenter/apiv2/securitycenterpb;securitycenterpb\xaa\x02\x1eGoogle.Cloud.SecurityCenter.V2\xca\x02\x1eGoogle\\Cloud\\SecurityCenter\\V2\xea\x02!Google::Cloud::SecurityCenter::V2'
    _globals['_CLOUDARMOR']._serialized_start = 117
    _globals['_CLOUDARMOR']._serialized_end = 467
    _globals['_SECURITYPOLICY']._serialized_start = 469
    _globals['_SECURITYPOLICY']._serialized_end = 530
    _globals['_REQUESTS']._serialized_start = 532
    _globals['_REQUESTS']._serialized_end = 638
    _globals['_ADAPTIVEPROTECTION']._serialized_start = 640
    _globals['_ADAPTIVEPROTECTION']._serialized_end = 680
    _globals['_ATTACK']._serialized_start = 682
    _globals['_ATTACK']._serialized_end = 754