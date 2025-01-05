"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_runtime_version.ValidateProtobufRuntimeVersion(_runtime_version.Domain.PUBLIC, 5, 28, 1, '', 'google/cloud/securitycenter/v1/indicator.proto')
_sym_db = _symbol_database.Default()
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n.google/cloud/securitycenter/v1/indicator.proto\x12\x1egoogle.cloud.securitycenter.v1"\xd9\x06\n\tIndicator\x12\x14\n\x0cip_addresses\x18\x01 \x03(\t\x12\x0f\n\x07domains\x18\x02 \x03(\t\x12N\n\nsignatures\x18\x03 \x03(\x0b2:.google.cloud.securitycenter.v1.Indicator.ProcessSignature\x12\x0c\n\x04uris\x18\x04 \x03(\t\x1a\xc6\x05\n\x10ProcessSignature\x12o\n\x15memory_hash_signature\x18\x06 \x01(\x0b2N.google.cloud.securitycenter.v1.Indicator.ProcessSignature.MemoryHashSignatureH\x00\x12k\n\x13yara_rule_signature\x18\x07 \x01(\x0b2L.google.cloud.securitycenter.v1.Indicator.ProcessSignature.YaraRuleSignatureH\x00\x12`\n\x0esignature_type\x18\x08 \x01(\x0e2H.google.cloud.securitycenter.v1.Indicator.ProcessSignature.SignatureType\x1a\xd6\x01\n\x13MemoryHashSignature\x12\x15\n\rbinary_family\x18\x01 \x01(\t\x12l\n\ndetections\x18\x04 \x03(\x0b2X.google.cloud.securitycenter.v1.Indicator.ProcessSignature.MemoryHashSignature.Detection\x1a:\n\tDetection\x12\x0e\n\x06binary\x18\x02 \x01(\t\x12\x1d\n\x15percent_pages_matched\x18\x03 \x01(\x01\x1a&\n\x11YaraRuleSignature\x12\x11\n\tyara_rule\x18\x05 \x01(\t"d\n\rSignatureType\x12\x1e\n\x1aSIGNATURE_TYPE_UNSPECIFIED\x10\x00\x12\x1a\n\x16SIGNATURE_TYPE_PROCESS\x10\x01\x12\x17\n\x13SIGNATURE_TYPE_FILE\x10\x02B\x0b\n\tsignatureB\xe8\x01\n"com.google.cloud.securitycenter.v1B\x0eIndicatorProtoP\x01ZJcloud.google.com/go/securitycenter/apiv1/securitycenterpb;securitycenterpb\xaa\x02\x1eGoogle.Cloud.SecurityCenter.V1\xca\x02\x1eGoogle\\Cloud\\SecurityCenter\\V1\xea\x02!Google::Cloud::SecurityCenter::V1b\x06proto3')
_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'google.cloud.securitycenter.v1.indicator_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
    _globals['DESCRIPTOR']._loaded_options = None
    _globals['DESCRIPTOR']._serialized_options = b'\n"com.google.cloud.securitycenter.v1B\x0eIndicatorProtoP\x01ZJcloud.google.com/go/securitycenter/apiv1/securitycenterpb;securitycenterpb\xaa\x02\x1eGoogle.Cloud.SecurityCenter.V1\xca\x02\x1eGoogle\\Cloud\\SecurityCenter\\V1\xea\x02!Google::Cloud::SecurityCenter::V1'
    _globals['_INDICATOR']._serialized_start = 83
    _globals['_INDICATOR']._serialized_end = 940
    _globals['_INDICATOR_PROCESSSIGNATURE']._serialized_start = 230
    _globals['_INDICATOR_PROCESSSIGNATURE']._serialized_end = 940
    _globals['_INDICATOR_PROCESSSIGNATURE_MEMORYHASHSIGNATURE']._serialized_start = 571
    _globals['_INDICATOR_PROCESSSIGNATURE_MEMORYHASHSIGNATURE']._serialized_end = 785
    _globals['_INDICATOR_PROCESSSIGNATURE_MEMORYHASHSIGNATURE_DETECTION']._serialized_start = 727
    _globals['_INDICATOR_PROCESSSIGNATURE_MEMORYHASHSIGNATURE_DETECTION']._serialized_end = 785
    _globals['_INDICATOR_PROCESSSIGNATURE_YARARULESIGNATURE']._serialized_start = 787
    _globals['_INDICATOR_PROCESSSIGNATURE_YARARULESIGNATURE']._serialized_end = 825
    _globals['_INDICATOR_PROCESSSIGNATURE_SIGNATURETYPE']._serialized_start = 827
    _globals['_INDICATOR_PROCESSSIGNATURE_SIGNATURETYPE']._serialized_end = 927