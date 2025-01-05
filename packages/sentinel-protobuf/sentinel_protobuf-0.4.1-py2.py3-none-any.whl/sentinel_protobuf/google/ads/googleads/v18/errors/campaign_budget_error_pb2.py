"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_runtime_version.ValidateProtobufRuntimeVersion(_runtime_version.Domain.PUBLIC, 5, 28, 1, '', 'google/ads/googleads/v18/errors/campaign_budget_error.proto')
_sym_db = _symbol_database.Default()
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n;google/ads/googleads/v18/errors/campaign_budget_error.proto\x12\x1fgoogle.ads.googleads.v18.errors"\x97\x07\n\x17CampaignBudgetErrorEnum"\xfb\x06\n\x13CampaignBudgetError\x12\x0f\n\x0bUNSPECIFIED\x10\x00\x12\x0b\n\x07UNKNOWN\x10\x01\x12$\n CAMPAIGN_BUDGET_CANNOT_BE_SHARED\x10\x11\x12\x1b\n\x17CAMPAIGN_BUDGET_REMOVED\x10\x02\x12\x1a\n\x16CAMPAIGN_BUDGET_IN_USE\x10\x03\x12(\n$CAMPAIGN_BUDGET_PERIOD_NOT_AVAILABLE\x10\x04\x12<\n8CANNOT_MODIFY_FIELD_OF_IMPLICITLY_SHARED_CAMPAIGN_BUDGET\x10\x06\x126\n2CANNOT_UPDATE_CAMPAIGN_BUDGET_TO_IMPLICITLY_SHARED\x10\x07\x12C\n?CANNOT_UPDATE_CAMPAIGN_BUDGET_TO_EXPLICITLY_SHARED_WITHOUT_NAME\x10\x08\x126\n2CANNOT_UPDATE_CAMPAIGN_BUDGET_TO_EXPLICITLY_SHARED\x10\t\x12H\nDCANNOT_USE_IMPLICITLY_SHARED_CAMPAIGN_BUDGET_WITH_MULTIPLE_CAMPAIGNS\x10\n\x12\x12\n\x0eDUPLICATE_NAME\x10\x0b\x12"\n\x1eMONEY_AMOUNT_IN_WRONG_CURRENCY\x10\x0c\x12/\n+MONEY_AMOUNT_LESS_THAN_CURRENCY_MINIMUM_CPC\x10\r\x12\x1a\n\x16MONEY_AMOUNT_TOO_LARGE\x10\x0e\x12\x19\n\x15NEGATIVE_MONEY_AMOUNT\x10\x0f\x12)\n%NON_MULTIPLE_OF_MINIMUM_CURRENCY_UNIT\x10\x10\x12=\n9TOTAL_BUDGET_AMOUNT_MUST_BE_UNSET_FOR_BUDGET_PERIOD_DAILY\x10\x12\x12\x12\n\x0eINVALID_PERIOD\x10\x13\x12(\n$CANNOT_USE_ACCELERATED_DELIVERY_MODE\x10\x14\x128\n4BUDGET_AMOUNT_MUST_BE_UNSET_FOR_CUSTOM_BUDGET_PERIOD\x10\x15B\xf8\x01\n#com.google.ads.googleads.v18.errorsB\x18CampaignBudgetErrorProtoP\x01ZEgoogle.golang.org/genproto/googleapis/ads/googleads/v18/errors;errors\xa2\x02\x03GAA\xaa\x02\x1fGoogle.Ads.GoogleAds.V18.Errors\xca\x02\x1fGoogle\\Ads\\GoogleAds\\V18\\Errors\xea\x02#Google::Ads::GoogleAds::V18::Errorsb\x06proto3')
_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'google.ads.googleads.v18.errors.campaign_budget_error_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
    _globals['DESCRIPTOR']._loaded_options = None
    _globals['DESCRIPTOR']._serialized_options = b'\n#com.google.ads.googleads.v18.errorsB\x18CampaignBudgetErrorProtoP\x01ZEgoogle.golang.org/genproto/googleapis/ads/googleads/v18/errors;errors\xa2\x02\x03GAA\xaa\x02\x1fGoogle.Ads.GoogleAds.V18.Errors\xca\x02\x1fGoogle\\Ads\\GoogleAds\\V18\\Errors\xea\x02#Google::Ads::GoogleAds::V18::Errors'
    _globals['_CAMPAIGNBUDGETERRORENUM']._serialized_start = 97
    _globals['_CAMPAIGNBUDGETERRORENUM']._serialized_end = 1016
    _globals['_CAMPAIGNBUDGETERRORENUM_CAMPAIGNBUDGETERROR']._serialized_start = 125
    _globals['_CAMPAIGNBUDGETERRORENUM_CAMPAIGNBUDGETERROR']._serialized_end = 1016