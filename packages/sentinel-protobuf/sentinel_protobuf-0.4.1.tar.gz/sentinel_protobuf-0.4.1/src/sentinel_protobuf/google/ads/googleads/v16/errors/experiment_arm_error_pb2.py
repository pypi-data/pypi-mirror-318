"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_runtime_version.ValidateProtobufRuntimeVersion(_runtime_version.Domain.PUBLIC, 5, 28, 1, '', 'google/ads/googleads/v16/errors/experiment_arm_error.proto')
_sym_db = _symbol_database.Default()
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n:google/ads/googleads/v16/errors/experiment_arm_error.proto\x12\x1fgoogle.ads.googleads.v16.errors"\xb1\x05\n\x16ExperimentArmErrorEnum"\x96\x05\n\x12ExperimentArmError\x12\x0f\n\x0bUNSPECIFIED\x10\x00\x12\x0b\n\x07UNKNOWN\x10\x01\x12\'\n#EXPERIMENT_ARM_COUNT_LIMIT_EXCEEDED\x10\x02\x12\x1b\n\x17INVALID_CAMPAIGN_STATUS\x10\x03\x12!\n\x1dDUPLICATE_EXPERIMENT_ARM_NAME\x10\x04\x12%\n!CANNOT_SET_TREATMENT_ARM_CAMPAIGN\x10\x05\x12\x1e\n\x1aCANNOT_MODIFY_CAMPAIGN_IDS\x10\x06\x12-\n)CANNOT_MODIFY_CAMPAIGN_WITHOUT_SUFFIX_SET\x10\x07\x12+\n\'CANNOT_MUTATE_TRAFFIC_SPLIT_AFTER_START\x10\x08\x12*\n&CANNOT_ADD_CAMPAIGN_WITH_SHARED_BUDGET\x10\t\x12*\n&CANNOT_ADD_CAMPAIGN_WITH_CUSTOM_BUDGET\x10\n\x124\n0CANNOT_ADD_CAMPAIGNS_WITH_DYNAMIC_ASSETS_ENABLED\x10\x0b\x125\n1UNSUPPORTED_CAMPAIGN_ADVERTISING_CHANNEL_SUB_TYPE\x10\x0c\x12,\n(CANNOT_ADD_BASE_CAMPAIGN_WITH_DATE_RANGE\x10\r\x121\n-BIDDING_STRATEGY_NOT_SUPPORTED_IN_EXPERIMENTS\x10\x0e\x120\n,TRAFFIC_SPLIT_NOT_SUPPORTED_FOR_CHANNEL_TYPE\x10\x0fB\xf7\x01\n#com.google.ads.googleads.v16.errorsB\x17ExperimentArmErrorProtoP\x01ZEgoogle.golang.org/genproto/googleapis/ads/googleads/v16/errors;errors\xa2\x02\x03GAA\xaa\x02\x1fGoogle.Ads.GoogleAds.V16.Errors\xca\x02\x1fGoogle\\Ads\\GoogleAds\\V16\\Errors\xea\x02#Google::Ads::GoogleAds::V16::Errorsb\x06proto3')
_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'google.ads.googleads.v16.errors.experiment_arm_error_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
    _globals['DESCRIPTOR']._loaded_options = None
    _globals['DESCRIPTOR']._serialized_options = b'\n#com.google.ads.googleads.v16.errorsB\x17ExperimentArmErrorProtoP\x01ZEgoogle.golang.org/genproto/googleapis/ads/googleads/v16/errors;errors\xa2\x02\x03GAA\xaa\x02\x1fGoogle.Ads.GoogleAds.V16.Errors\xca\x02\x1fGoogle\\Ads\\GoogleAds\\V16\\Errors\xea\x02#Google::Ads::GoogleAds::V16::Errors'
    _globals['_EXPERIMENTARMERRORENUM']._serialized_start = 96
    _globals['_EXPERIMENTARMERRORENUM']._serialized_end = 785
    _globals['_EXPERIMENTARMERRORENUM_EXPERIMENTARMERROR']._serialized_start = 123
    _globals['_EXPERIMENTARMERRORENUM_EXPERIMENTARMERROR']._serialized_end = 785