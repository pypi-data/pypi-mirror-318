"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_runtime_version.ValidateProtobufRuntimeVersion(_runtime_version.Domain.PUBLIC, 5, 28, 1, '', 'google/ads/googleads/v16/errors/account_budget_proposal_error.proto')
_sym_db = _symbol_database.Default()
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\nCgoogle/ads/googleads/v16/errors/account_budget_proposal_error.proto\x12\x1fgoogle.ads.googleads.v16.errors"\xda\x07\n\x1eAccountBudgetProposalErrorEnum"\xb7\x07\n\x1aAccountBudgetProposalError\x12\x0f\n\x0bUNSPECIFIED\x10\x00\x12\x0b\n\x07UNKNOWN\x10\x01\x12\x1a\n\x16FIELD_MASK_NOT_ALLOWED\x10\x02\x12\x13\n\x0fIMMUTABLE_FIELD\x10\x03\x12\x1a\n\x16REQUIRED_FIELD_MISSING\x10\x04\x12#\n\x1fCANNOT_CANCEL_APPROVED_PROPOSAL\x10\x05\x12#\n\x1fCANNOT_REMOVE_UNAPPROVED_BUDGET\x10\x06\x12 \n\x1cCANNOT_REMOVE_RUNNING_BUDGET\x10\x07\x12 \n\x1cCANNOT_END_UNAPPROVED_BUDGET\x10\x08\x12\x1e\n\x1aCANNOT_END_INACTIVE_BUDGET\x10\t\x12\x18\n\x14BUDGET_NAME_REQUIRED\x10\n\x12\x1c\n\x18CANNOT_UPDATE_OLD_BUDGET\x10\x0b\x12\x16\n\x12CANNOT_END_IN_PAST\x10\x0c\x12\x1a\n\x16CANNOT_EXTEND_END_TIME\x10\r\x12"\n\x1ePURCHASE_ORDER_NUMBER_REQUIRED\x10\x0e\x12"\n\x1ePENDING_UPDATE_PROPOSAL_EXISTS\x10\x0f\x12=\n9MULTIPLE_BUDGETS_NOT_ALLOWED_FOR_UNAPPROVED_BILLING_SETUP\x10\x10\x12/\n+CANNOT_UPDATE_START_TIME_FOR_STARTED_BUDGET\x10\x11\x126\n2SPENDING_LIMIT_LOWER_THAN_ACCRUED_COST_NOT_ALLOWED\x10\x12\x12\x13\n\x0fUPDATE_IS_NO_OP\x10\x13\x12#\n\x1fEND_TIME_MUST_FOLLOW_START_TIME\x10\x14\x125\n1BUDGET_DATE_RANGE_INCOMPATIBLE_WITH_BILLING_SETUP\x10\x15\x12\x12\n\x0eNOT_AUTHORIZED\x10\x16\x12\x19\n\x15INVALID_BILLING_SETUP\x10\x17\x12\x1c\n\x18OVERLAPS_EXISTING_BUDGET\x10\x18\x12$\n CANNOT_CREATE_BUDGET_THROUGH_API\x10\x19\x12$\n INVALID_MASTER_SERVICE_AGREEMENT\x10\x1a\x12\x1a\n\x16CANCELED_BILLING_SETUP\x10\x1bB\xff\x01\n#com.google.ads.googleads.v16.errorsB\x1fAccountBudgetProposalErrorProtoP\x01ZEgoogle.golang.org/genproto/googleapis/ads/googleads/v16/errors;errors\xa2\x02\x03GAA\xaa\x02\x1fGoogle.Ads.GoogleAds.V16.Errors\xca\x02\x1fGoogle\\Ads\\GoogleAds\\V16\\Errors\xea\x02#Google::Ads::GoogleAds::V16::Errorsb\x06proto3')
_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'google.ads.googleads.v16.errors.account_budget_proposal_error_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
    _globals['DESCRIPTOR']._loaded_options = None
    _globals['DESCRIPTOR']._serialized_options = b'\n#com.google.ads.googleads.v16.errorsB\x1fAccountBudgetProposalErrorProtoP\x01ZEgoogle.golang.org/genproto/googleapis/ads/googleads/v16/errors;errors\xa2\x02\x03GAA\xaa\x02\x1fGoogle.Ads.GoogleAds.V16.Errors\xca\x02\x1fGoogle\\Ads\\GoogleAds\\V16\\Errors\xea\x02#Google::Ads::GoogleAds::V16::Errors'
    _globals['_ACCOUNTBUDGETPROPOSALERRORENUM']._serialized_start = 105
    _globals['_ACCOUNTBUDGETPROPOSALERRORENUM']._serialized_end = 1091
    _globals['_ACCOUNTBUDGETPROPOSALERRORENUM_ACCOUNTBUDGETPROPOSALERROR']._serialized_start = 140
    _globals['_ACCOUNTBUDGETPROPOSALERRORENUM_ACCOUNTBUDGETPROPOSALERROR']._serialized_end = 1091