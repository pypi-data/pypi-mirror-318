"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_runtime_version.ValidateProtobufRuntimeVersion(_runtime_version.Domain.PUBLIC, 5, 28, 1, '', 'google/ads/googleads/v18/errors/bidding_error.proto')
_sym_db = _symbol_database.Default()
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n3google/ads/googleads/v18/errors/bidding_error.proto\x12\x1fgoogle.ads.googleads.v18.errors"\xd3\t\n\x10BiddingErrorEnum"\xbe\t\n\x0cBiddingError\x12\x0f\n\x0bUNSPECIFIED\x10\x00\x12\x0b\n\x07UNKNOWN\x10\x01\x12+\n\'BIDDING_STRATEGY_TRANSITION_NOT_ALLOWED\x10\x02\x12.\n*CANNOT_ATTACH_BIDDING_STRATEGY_TO_CAMPAIGN\x10\x07\x12+\n\'INVALID_ANONYMOUS_BIDDING_STRATEGY_TYPE\x10\n\x12!\n\x1dINVALID_BIDDING_STRATEGY_TYPE\x10\x0e\x12\x0f\n\x0bINVALID_BID\x10\x11\x123\n/BIDDING_STRATEGY_NOT_AVAILABLE_FOR_ACCOUNT_TYPE\x10\x12\x120\n,CANNOT_CREATE_CAMPAIGN_WITH_BIDDING_STRATEGY\x10\x15\x12O\nKCANNOT_TARGET_CONTENT_NETWORK_ONLY_WITH_CAMPAIGN_LEVEL_POP_BIDDING_STRATEGY\x10\x17\x123\n/BIDDING_STRATEGY_NOT_SUPPORTED_WITH_AD_SCHEDULE\x10\x18\x121\n-PAY_PER_CONVERSION_NOT_AVAILABLE_FOR_CUSTOMER\x10\x19\x122\n.PAY_PER_CONVERSION_NOT_ALLOWED_WITH_TARGET_CPA\x10\x1a\x12:\n6BIDDING_STRATEGY_NOT_ALLOWED_FOR_SEARCH_ONLY_CAMPAIGNS\x10\x1b\x12;\n7BIDDING_STRATEGY_NOT_SUPPORTED_IN_DRAFTS_OR_EXPERIMENTS\x10\x1c\x12I\nEBIDDING_STRATEGY_TYPE_DOES_NOT_SUPPORT_PRODUCT_TYPE_ADGROUP_CRITERION\x10\x1d\x12\x11\n\rBID_TOO_SMALL\x10\x1e\x12\x0f\n\x0bBID_TOO_BIG\x10\x1f\x12"\n\x1eBID_TOO_MANY_FRACTIONAL_DIGITS\x10 \x12\x17\n\x13INVALID_DOMAIN_NAME\x10!\x12$\n NOT_COMPATIBLE_WITH_PAYMENT_MODE\x10"\x129\n5BIDDING_STRATEGY_TYPE_INCOMPATIBLE_WITH_SHARED_BUDGET\x10%\x12/\n+BIDDING_STRATEGY_AND_BUDGET_MUST_BE_ALIGNED\x10&\x12O\nKBIDDING_STRATEGY_AND_BUDGET_MUST_BE_ATTACHED_TO_THE_SAME_CAMPAIGNS_TO_ALIGN\x10\'\x128\n4BIDDING_STRATEGY_AND_BUDGET_MUST_BE_REMOVED_TOGETHER\x10(\x12<\n8CPC_BID_FLOOR_MICROS_GREATER_THAN_CPC_BID_CEILING_MICROS\x10)B\xf1\x01\n#com.google.ads.googleads.v18.errorsB\x11BiddingErrorProtoP\x01ZEgoogle.golang.org/genproto/googleapis/ads/googleads/v18/errors;errors\xa2\x02\x03GAA\xaa\x02\x1fGoogle.Ads.GoogleAds.V18.Errors\xca\x02\x1fGoogle\\Ads\\GoogleAds\\V18\\Errors\xea\x02#Google::Ads::GoogleAds::V18::Errorsb\x06proto3')
_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'google.ads.googleads.v18.errors.bidding_error_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
    _globals['DESCRIPTOR']._loaded_options = None
    _globals['DESCRIPTOR']._serialized_options = b'\n#com.google.ads.googleads.v18.errorsB\x11BiddingErrorProtoP\x01ZEgoogle.golang.org/genproto/googleapis/ads/googleads/v18/errors;errors\xa2\x02\x03GAA\xaa\x02\x1fGoogle.Ads.GoogleAds.V18.Errors\xca\x02\x1fGoogle\\Ads\\GoogleAds\\V18\\Errors\xea\x02#Google::Ads::GoogleAds::V18::Errors'
    _globals['_BIDDINGERRORENUM']._serialized_start = 89
    _globals['_BIDDINGERRORENUM']._serialized_end = 1324
    _globals['_BIDDINGERRORENUM_BIDDINGERROR']._serialized_start = 110
    _globals['_BIDDINGERRORENUM_BIDDINGERROR']._serialized_end = 1324