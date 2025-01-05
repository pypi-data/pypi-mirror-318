"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_runtime_version.ValidateProtobufRuntimeVersion(_runtime_version.Domain.PUBLIC, 5, 28, 1, '', 'google/ads/googleads/v16/errors/request_error.proto')
_sym_db = _symbol_database.Default()
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n3google/ads/googleads/v16/errors/request_error.proto\x12\x1fgoogle.ads.googleads.v16.errors"\x8e\x07\n\x10RequestErrorEnum"\xf9\x06\n\x0cRequestError\x12\x0f\n\x0bUNSPECIFIED\x10\x00\x12\x0b\n\x07UNKNOWN\x10\x01\x12\x19\n\x15RESOURCE_NAME_MISSING\x10\x03\x12\x1b\n\x17RESOURCE_NAME_MALFORMED\x10\x04\x12\x13\n\x0fBAD_RESOURCE_ID\x10\x11\x12\x17\n\x13INVALID_CUSTOMER_ID\x10\x10\x12\x16\n\x12OPERATION_REQUIRED\x10\x05\x12\x16\n\x12RESOURCE_NOT_FOUND\x10\x06\x12\x16\n\x12INVALID_PAGE_TOKEN\x10\x07\x12\x16\n\x12EXPIRED_PAGE_TOKEN\x10\x08\x12\x15\n\x11INVALID_PAGE_SIZE\x10\x16\x12\x1b\n\x17PAGE_SIZE_NOT_SUPPORTED\x10(\x12\x1a\n\x16REQUIRED_FIELD_MISSING\x10\t\x12\x13\n\x0fIMMUTABLE_FIELD\x10\x0b\x12\x1e\n\x1aTOO_MANY_MUTATE_OPERATIONS\x10\r\x12)\n%CANNOT_BE_EXECUTED_BY_MANAGER_ACCOUNT\x10\x0e\x12\x1f\n\x1bCANNOT_MODIFY_FOREIGN_FIELD\x10\x0f\x12\x16\n\x12INVALID_ENUM_VALUE\x10\x12\x12%\n!DEVELOPER_TOKEN_PARAMETER_MISSING\x10\x13\x12\'\n#LOGIN_CUSTOMER_ID_PARAMETER_MISSING\x10\x14\x12(\n$VALIDATE_ONLY_REQUEST_HAS_PAGE_TOKEN\x10\x15\x129\n5CANNOT_RETURN_SUMMARY_ROW_FOR_REQUEST_WITHOUT_METRICS\x10\x1d\x128\n4CANNOT_RETURN_SUMMARY_ROW_FOR_VALIDATE_ONLY_REQUESTS\x10\x1e\x12)\n%INCONSISTENT_RETURN_SUMMARY_ROW_VALUE\x10\x1f\x120\n,TOTAL_RESULTS_COUNT_NOT_ORIGINALLY_REQUESTED\x10 \x12\x1a\n\x16RPC_DEADLINE_TOO_SHORT\x10!\x12\x17\n\x13UNSUPPORTED_VERSION\x10&\x12\x1b\n\x17CLOUD_PROJECT_NOT_FOUND\x10\'B\xf1\x01\n#com.google.ads.googleads.v16.errorsB\x11RequestErrorProtoP\x01ZEgoogle.golang.org/genproto/googleapis/ads/googleads/v16/errors;errors\xa2\x02\x03GAA\xaa\x02\x1fGoogle.Ads.GoogleAds.V16.Errors\xca\x02\x1fGoogle\\Ads\\GoogleAds\\V16\\Errors\xea\x02#Google::Ads::GoogleAds::V16::Errorsb\x06proto3')
_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'google.ads.googleads.v16.errors.request_error_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
    _globals['DESCRIPTOR']._loaded_options = None
    _globals['DESCRIPTOR']._serialized_options = b'\n#com.google.ads.googleads.v16.errorsB\x11RequestErrorProtoP\x01ZEgoogle.golang.org/genproto/googleapis/ads/googleads/v16/errors;errors\xa2\x02\x03GAA\xaa\x02\x1fGoogle.Ads.GoogleAds.V16.Errors\xca\x02\x1fGoogle\\Ads\\GoogleAds\\V16\\Errors\xea\x02#Google::Ads::GoogleAds::V16::Errors'
    _globals['_REQUESTERRORENUM']._serialized_start = 89
    _globals['_REQUESTERRORENUM']._serialized_end = 999
    _globals['_REQUESTERRORENUM_REQUESTERROR']._serialized_start = 110
    _globals['_REQUESTERRORENUM_REQUESTERROR']._serialized_end = 999