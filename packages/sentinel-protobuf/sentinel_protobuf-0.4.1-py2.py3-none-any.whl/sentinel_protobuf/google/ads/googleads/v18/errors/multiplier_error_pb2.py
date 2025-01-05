"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_runtime_version.ValidateProtobufRuntimeVersion(_runtime_version.Domain.PUBLIC, 5, 28, 1, '', 'google/ads/googleads/v18/errors/multiplier_error.proto')
_sym_db = _symbol_database.Default()
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n6google/ads/googleads/v18/errors/multiplier_error.proto\x12\x1fgoogle.ads.googleads.v18.errors"\xcf\x04\n\x13MultiplierErrorEnum"\xb7\x04\n\x0fMultiplierError\x12\x0f\n\x0bUNSPECIFIED\x10\x00\x12\x0b\n\x07UNKNOWN\x10\x01\x12\x17\n\x13MULTIPLIER_TOO_HIGH\x10\x02\x12\x16\n\x12MULTIPLIER_TOO_LOW\x10\x03\x12\x1e\n\x1aTOO_MANY_FRACTIONAL_DIGITS\x10\x04\x12/\n+MULTIPLIER_NOT_ALLOWED_FOR_BIDDING_STRATEGY\x10\x05\x123\n/MULTIPLIER_NOT_ALLOWED_WHEN_BASE_BID_IS_MISSING\x10\x06\x12\x1b\n\x17NO_MULTIPLIER_SPECIFIED\x10\x07\x120\n,MULTIPLIER_CAUSES_BID_TO_EXCEED_DAILY_BUDGET\x10\x08\x122\n.MULTIPLIER_CAUSES_BID_TO_EXCEED_MONTHLY_BUDGET\x10\t\x121\n-MULTIPLIER_CAUSES_BID_TO_EXCEED_CUSTOM_BUDGET\x10\n\x123\n/MULTIPLIER_CAUSES_BID_TO_EXCEED_MAX_ALLOWED_BID\x10\x0b\x121\n-BID_LESS_THAN_MIN_ALLOWED_BID_WITH_MULTIPLIER\x10\x0c\x121\n-MULTIPLIER_AND_BIDDING_STRATEGY_TYPE_MISMATCH\x10\rB\xf4\x01\n#com.google.ads.googleads.v18.errorsB\x14MultiplierErrorProtoP\x01ZEgoogle.golang.org/genproto/googleapis/ads/googleads/v18/errors;errors\xa2\x02\x03GAA\xaa\x02\x1fGoogle.Ads.GoogleAds.V18.Errors\xca\x02\x1fGoogle\\Ads\\GoogleAds\\V18\\Errors\xea\x02#Google::Ads::GoogleAds::V18::Errorsb\x06proto3')
_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'google.ads.googleads.v18.errors.multiplier_error_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
    _globals['DESCRIPTOR']._loaded_options = None
    _globals['DESCRIPTOR']._serialized_options = b'\n#com.google.ads.googleads.v18.errorsB\x14MultiplierErrorProtoP\x01ZEgoogle.golang.org/genproto/googleapis/ads/googleads/v18/errors;errors\xa2\x02\x03GAA\xaa\x02\x1fGoogle.Ads.GoogleAds.V18.Errors\xca\x02\x1fGoogle\\Ads\\GoogleAds\\V18\\Errors\xea\x02#Google::Ads::GoogleAds::V18::Errors'
    _globals['_MULTIPLIERERRORENUM']._serialized_start = 92
    _globals['_MULTIPLIERERRORENUM']._serialized_end = 683
    _globals['_MULTIPLIERERRORENUM_MULTIPLIERERROR']._serialized_start = 116
    _globals['_MULTIPLIERERRORENUM_MULTIPLIERERROR']._serialized_end = 683