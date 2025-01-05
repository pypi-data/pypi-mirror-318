"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_runtime_version.ValidateProtobufRuntimeVersion(_runtime_version.Domain.PUBLIC, 5, 28, 1, '', 'google/cloud/websecurityscanner/v1/finding_addon.proto')
_sym_db = _symbol_database.Default()
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n6google/cloud/websecurityscanner/v1/finding_addon.proto\x12"google.cloud.websecurityscanner.v1"*\n\x04Form\x12\x12\n\naction_uri\x18\x01 \x01(\t\x12\x0e\n\x06fields\x18\x02 \x03(\t"Q\n\x0fOutdatedLibrary\x12\x14\n\x0clibrary_name\x18\x01 \x01(\t\x12\x0f\n\x07version\x18\x02 \x01(\t\x12\x17\n\x0flearn_more_urls\x18\x03 \x03(\t"?\n\x11ViolatingResource\x12\x14\n\x0ccontent_type\x18\x01 \x01(\t\x12\x14\n\x0cresource_url\x18\x02 \x01(\t"/\n\x14VulnerableParameters\x12\x17\n\x0fparameter_names\x18\x01 \x03(\t"\xe0\x01\n\x11VulnerableHeaders\x12M\n\x07headers\x18\x01 \x03(\x0b2<.google.cloud.websecurityscanner.v1.VulnerableHeaders.Header\x12U\n\x0fmissing_headers\x18\x02 \x03(\x0b2<.google.cloud.websecurityscanner.v1.VulnerableHeaders.Header\x1a%\n\x06Header\x12\x0c\n\x04name\x18\x01 \x01(\t\x12\r\n\x05value\x18\x02 \x01(\t"\xdb\x03\n\x03Xss\x12\x14\n\x0cstack_traces\x18\x01 \x03(\t\x12\x15\n\rerror_message\x18\x02 \x01(\t\x12K\n\rattack_vector\x18\x03 \x01(\x0e24.google.cloud.websecurityscanner.v1.Xss.AttackVector\x12\x1e\n\x16stored_xss_seeding_url\x18\x04 \x01(\t"\xb9\x02\n\x0cAttackVector\x12\x1d\n\x19ATTACK_VECTOR_UNSPECIFIED\x10\x00\x12\x11\n\rLOCAL_STORAGE\x10\x01\x12\x13\n\x0fSESSION_STORAGE\x10\x02\x12\x0f\n\x0bWINDOW_NAME\x10\x03\x12\x0c\n\x08REFERRER\x10\x04\x12\x0e\n\nFORM_INPUT\x10\x05\x12\n\n\x06COOKIE\x10\x06\x12\x10\n\x0cPOST_MESSAGE\x10\x07\x12\x12\n\x0eGET_PARAMETERS\x10\x08\x12\x10\n\x0cURL_FRAGMENT\x10\t\x12\x10\n\x0cHTML_COMMENT\x10\n\x12\x13\n\x0fPOST_PARAMETERS\x10\x0b\x12\x0c\n\x08PROTOCOL\x10\x0c\x12\x0e\n\nSTORED_XSS\x10\r\x12\x0f\n\x0bSAME_ORIGIN\x10\x0e\x12\x19\n\x15USER_CONTROLLABLE_URL\x10\x0f"\xa9\x01\n\x03Xxe\x12\x15\n\rpayload_value\x18\x01 \x01(\t\x12J\n\x10payload_location\x18\x02 \x01(\x0e20.google.cloud.websecurityscanner.v1.Xxe.Location"?\n\x08Location\x12\x18\n\x14LOCATION_UNSPECIFIED\x10\x00\x12\x19\n\x15COMPLETE_REQUEST_BODY\x10\x01B\x87\x02\n&com.google.cloud.websecurityscanner.v1B\x11FindingAddonProtoP\x01ZVcloud.google.com/go/websecurityscanner/apiv1/websecurityscannerpb;websecurityscannerpb\xaa\x02"Google.Cloud.WebSecurityScanner.V1\xca\x02"Google\\Cloud\\WebSecurityScanner\\V1\xea\x02%Google::Cloud::WebSecurityScanner::V1b\x06proto3')
_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'google.cloud.websecurityscanner.v1.finding_addon_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
    _globals['DESCRIPTOR']._loaded_options = None
    _globals['DESCRIPTOR']._serialized_options = b'\n&com.google.cloud.websecurityscanner.v1B\x11FindingAddonProtoP\x01ZVcloud.google.com/go/websecurityscanner/apiv1/websecurityscannerpb;websecurityscannerpb\xaa\x02"Google.Cloud.WebSecurityScanner.V1\xca\x02"Google\\Cloud\\WebSecurityScanner\\V1\xea\x02%Google::Cloud::WebSecurityScanner::V1'
    _globals['_FORM']._serialized_start = 94
    _globals['_FORM']._serialized_end = 136
    _globals['_OUTDATEDLIBRARY']._serialized_start = 138
    _globals['_OUTDATEDLIBRARY']._serialized_end = 219
    _globals['_VIOLATINGRESOURCE']._serialized_start = 221
    _globals['_VIOLATINGRESOURCE']._serialized_end = 284
    _globals['_VULNERABLEPARAMETERS']._serialized_start = 286
    _globals['_VULNERABLEPARAMETERS']._serialized_end = 333
    _globals['_VULNERABLEHEADERS']._serialized_start = 336
    _globals['_VULNERABLEHEADERS']._serialized_end = 560
    _globals['_VULNERABLEHEADERS_HEADER']._serialized_start = 523
    _globals['_VULNERABLEHEADERS_HEADER']._serialized_end = 560
    _globals['_XSS']._serialized_start = 563
    _globals['_XSS']._serialized_end = 1038
    _globals['_XSS_ATTACKVECTOR']._serialized_start = 725
    _globals['_XSS_ATTACKVECTOR']._serialized_end = 1038
    _globals['_XXE']._serialized_start = 1041
    _globals['_XXE']._serialized_end = 1210
    _globals['_XXE_LOCATION']._serialized_start = 1147
    _globals['_XXE_LOCATION']._serialized_end = 1210