"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_runtime_version.ValidateProtobufRuntimeVersion(_runtime_version.Domain.PUBLIC, 5, 28, 1, '', 'google/ads/googleads/v16/errors/setting_error.proto')
_sym_db = _symbol_database.Default()
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n3google/ads/googleads/v16/errors/setting_error.proto\x12\x1fgoogle.ads.googleads.v16.errors"\xb7\x06\n\x10SettingErrorEnum"\xa2\x06\n\x0cSettingError\x12\x0f\n\x0bUNSPECIFIED\x10\x00\x12\x0b\n\x07UNKNOWN\x10\x01\x12!\n\x1dSETTING_TYPE_IS_NOT_AVAILABLE\x10\x03\x120\n,SETTING_TYPE_IS_NOT_COMPATIBLE_WITH_CAMPAIGN\x10\x04\x12;\n7TARGETING_SETTING_CONTAINS_INVALID_CRITERION_TYPE_GROUP\x10\x05\x12Q\nMTARGETING_SETTING_DEMOGRAPHIC_CRITERION_TYPE_GROUPS_MUST_BE_SET_TO_TARGET_ALL\x10\x06\x12\\\nXTARGETING_SETTING_CANNOT_CHANGE_TARGET_ALL_TO_FALSE_FOR_DEMOGRAPHIC_CRITERION_TYPE_GROUP\x10\x07\x12C\n?DYNAMIC_SEARCH_ADS_SETTING_AT_LEAST_ONE_FEED_ID_MUST_BE_PRESENT\x10\x08\x12;\n7DYNAMIC_SEARCH_ADS_SETTING_CONTAINS_INVALID_DOMAIN_NAME\x10\t\x126\n2DYNAMIC_SEARCH_ADS_SETTING_CONTAINS_SUBDOMAIN_NAME\x10\n\x12=\n9DYNAMIC_SEARCH_ADS_SETTING_CONTAINS_INVALID_LANGUAGE_CODE\x10\x0b\x12>\n:TARGET_ALL_IS_NOT_ALLOWED_FOR_PLACEMENT_IN_SEARCH_CAMPAIGN\x10\x0c\x12.\n*SETTING_VALUE_NOT_COMPATIBLE_WITH_CAMPAIGN\x10\x14\x12H\nDBID_ONLY_IS_NOT_ALLOWED_TO_BE_MODIFIED_WITH_CUSTOMER_MATCH_TARGETING\x10\x15B\xf1\x01\n#com.google.ads.googleads.v16.errorsB\x11SettingErrorProtoP\x01ZEgoogle.golang.org/genproto/googleapis/ads/googleads/v16/errors;errors\xa2\x02\x03GAA\xaa\x02\x1fGoogle.Ads.GoogleAds.V16.Errors\xca\x02\x1fGoogle\\Ads\\GoogleAds\\V16\\Errors\xea\x02#Google::Ads::GoogleAds::V16::Errorsb\x06proto3')
_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'google.ads.googleads.v16.errors.setting_error_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
    _globals['DESCRIPTOR']._loaded_options = None
    _globals['DESCRIPTOR']._serialized_options = b'\n#com.google.ads.googleads.v16.errorsB\x11SettingErrorProtoP\x01ZEgoogle.golang.org/genproto/googleapis/ads/googleads/v16/errors;errors\xa2\x02\x03GAA\xaa\x02\x1fGoogle.Ads.GoogleAds.V16.Errors\xca\x02\x1fGoogle\\Ads\\GoogleAds\\V16\\Errors\xea\x02#Google::Ads::GoogleAds::V16::Errors'
    _globals['_SETTINGERRORENUM']._serialized_start = 89
    _globals['_SETTINGERRORENUM']._serialized_end = 912
    _globals['_SETTINGERRORENUM_SETTINGERROR']._serialized_start = 110
    _globals['_SETTINGERRORENUM_SETTINGERROR']._serialized_end = 912