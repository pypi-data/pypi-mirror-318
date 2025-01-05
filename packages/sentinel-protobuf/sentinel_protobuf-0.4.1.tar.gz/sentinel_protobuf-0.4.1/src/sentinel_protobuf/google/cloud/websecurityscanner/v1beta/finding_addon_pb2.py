"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_runtime_version.ValidateProtobufRuntimeVersion(_runtime_version.Domain.PUBLIC, 5, 28, 1, '', 'google/cloud/websecurityscanner/v1beta/finding_addon.proto')
_sym_db = _symbol_database.Default()
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n:google/cloud/websecurityscanner/v1beta/finding_addon.proto\x12&google.cloud.websecurityscanner.v1beta"*\n\x04Form\x12\x12\n\naction_uri\x18\x01 \x01(\t\x12\x0e\n\x06fields\x18\x02 \x03(\t"Q\n\x0fOutdatedLibrary\x12\x14\n\x0clibrary_name\x18\x01 \x01(\t\x12\x0f\n\x07version\x18\x02 \x01(\t\x12\x17\n\x0flearn_more_urls\x18\x03 \x03(\t"?\n\x11ViolatingResource\x12\x14\n\x0ccontent_type\x18\x01 \x01(\t\x12\x14\n\x0cresource_url\x18\x02 \x01(\t"/\n\x14VulnerableParameters\x12\x17\n\x0fparameter_names\x18\x01 \x03(\t"\xe8\x01\n\x11VulnerableHeaders\x12Q\n\x07headers\x18\x01 \x03(\x0b2@.google.cloud.websecurityscanner.v1beta.VulnerableHeaders.Header\x12Y\n\x0fmissing_headers\x18\x02 \x03(\x0b2@.google.cloud.websecurityscanner.v1beta.VulnerableHeaders.Header\x1a%\n\x06Header\x12\x0c\n\x04name\x18\x01 \x01(\t\x12\r\n\x05value\x18\x02 \x01(\t"2\n\x03Xss\x12\x14\n\x0cstack_traces\x18\x01 \x03(\t\x12\x15\n\rerror_message\x18\x02 \x01(\tB\x9b\x02\n*com.google.cloud.websecurityscanner.v1betaB\x11FindingAddonProtoP\x01ZZcloud.google.com/go/websecurityscanner/apiv1beta/websecurityscannerpb;websecurityscannerpb\xaa\x02&Google.Cloud.WebSecurityScanner.V1Beta\xca\x02&Google\\Cloud\\WebSecurityScanner\\V1beta\xea\x02)Google::Cloud::WebSecurityScanner::V1betab\x06proto3')
_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'google.cloud.websecurityscanner.v1beta.finding_addon_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
    _globals['DESCRIPTOR']._loaded_options = None
    _globals['DESCRIPTOR']._serialized_options = b'\n*com.google.cloud.websecurityscanner.v1betaB\x11FindingAddonProtoP\x01ZZcloud.google.com/go/websecurityscanner/apiv1beta/websecurityscannerpb;websecurityscannerpb\xaa\x02&Google.Cloud.WebSecurityScanner.V1Beta\xca\x02&Google\\Cloud\\WebSecurityScanner\\V1beta\xea\x02)Google::Cloud::WebSecurityScanner::V1beta'
    _globals['_FORM']._serialized_start = 102
    _globals['_FORM']._serialized_end = 144
    _globals['_OUTDATEDLIBRARY']._serialized_start = 146
    _globals['_OUTDATEDLIBRARY']._serialized_end = 227
    _globals['_VIOLATINGRESOURCE']._serialized_start = 229
    _globals['_VIOLATINGRESOURCE']._serialized_end = 292
    _globals['_VULNERABLEPARAMETERS']._serialized_start = 294
    _globals['_VULNERABLEPARAMETERS']._serialized_end = 341
    _globals['_VULNERABLEHEADERS']._serialized_start = 344
    _globals['_VULNERABLEHEADERS']._serialized_end = 576
    _globals['_VULNERABLEHEADERS_HEADER']._serialized_start = 539
    _globals['_VULNERABLEHEADERS_HEADER']._serialized_end = 576
    _globals['_XSS']._serialized_start = 578
    _globals['_XSS']._serialized_end = 628