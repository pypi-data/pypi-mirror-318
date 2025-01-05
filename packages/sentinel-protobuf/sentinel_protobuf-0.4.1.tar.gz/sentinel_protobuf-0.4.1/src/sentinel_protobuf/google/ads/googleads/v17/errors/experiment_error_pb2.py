"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_runtime_version.ValidateProtobufRuntimeVersion(_runtime_version.Domain.PUBLIC, 5, 28, 1, '', 'google/ads/googleads/v17/errors/experiment_error.proto')
_sym_db = _symbol_database.Default()
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n6google/ads/googleads/v17/errors/experiment_error.proto\x12\x1fgoogle.ads.googleads.v17.errors"\xa8\t\n\x13ExperimentErrorEnum"\x90\t\n\x0fExperimentError\x12\x0f\n\x0bUNSPECIFIED\x10\x00\x12\x0b\n\x07UNKNOWN\x10\x01\x12!\n\x1dCANNOT_SET_START_DATE_IN_PAST\x10\x02\x12\x1e\n\x1aEND_DATE_BEFORE_START_DATE\x10\x03\x12 \n\x1cSTART_DATE_TOO_FAR_IN_FUTURE\x10\x04\x12\x1d\n\x19DUPLICATE_EXPERIMENT_NAME\x10\x05\x12$\n CANNOT_MODIFY_REMOVED_EXPERIMENT\x10\x06\x12\x1d\n\x19START_DATE_ALREADY_PASSED\x10\x07\x12\x1f\n\x1bCANNOT_SET_END_DATE_IN_PAST\x10\x08\x12 \n\x1cCANNOT_SET_STATUS_TO_REMOVED\x10\t\x12\x1f\n\x1bCANNOT_MODIFY_PAST_END_DATE\x10\n\x12\x12\n\x0eINVALID_STATUS\x10\x0b\x12!\n\x1dINVALID_CAMPAIGN_CHANNEL_TYPE\x10\x0c\x12&\n"OVERLAPPING_MEMBERS_AND_DATE_RANGE\x10\r\x12#\n\x1fINVALID_TRIAL_ARM_TRAFFIC_SPLIT\x10\x0e\x12\x1d\n\x19TRAFFIC_SPLIT_OVERLAPPING\x10\x0f\x12E\nASUM_TRIAL_ARM_TRAFFIC_UNEQUALS_TO_TRIAL_TRAFFIC_SPLIT_DENOMINATOR\x10\x10\x12+\n\'CANNOT_MODIFY_TRAFFIC_SPLIT_AFTER_START\x10\x11\x12\x18\n\x14EXPERIMENT_NOT_FOUND\x10\x12\x12\x1e\n\x1aEXPERIMENT_NOT_YET_STARTED\x10\x13\x12%\n!CANNOT_HAVE_MULTIPLE_CONTROL_ARMS\x10\x14\x12\x1f\n\x1bIN_DESIGN_CAMPAIGNS_NOT_SET\x10\x15\x12"\n\x1eCANNOT_SET_STATUS_TO_GRADUATED\x10\x16\x128\n4CANNOT_CREATE_EXPERIMENT_CAMPAIGN_WITH_SHARED_BUDGET\x10\x17\x128\n4CANNOT_CREATE_EXPERIMENT_CAMPAIGN_WITH_CUSTOM_BUDGET\x10\x18\x12\x1d\n\x19STATUS_TRANSITION_INVALID\x10\x19\x12&\n"DUPLICATE_EXPERIMENT_CAMPAIGN_NAME\x10\x1a\x12(\n$CANNOT_REMOVE_IN_CREATION_EXPERIMENT\x10\x1b\x120\n,CANNOT_ADD_CAMPAIGN_WITH_DEPRECATED_AD_TYPES\x10\x1c\x126\n2CANNOT_ENABLE_SYNC_FOR_UNSUPPORTED_EXPERIMENT_TYPE\x10\x1d\x12&\n"INVALID_DURATION_FOR_AN_EXPERIMENT\x10\x1eB\xf4\x01\n#com.google.ads.googleads.v17.errorsB\x14ExperimentErrorProtoP\x01ZEgoogle.golang.org/genproto/googleapis/ads/googleads/v17/errors;errors\xa2\x02\x03GAA\xaa\x02\x1fGoogle.Ads.GoogleAds.V17.Errors\xca\x02\x1fGoogle\\Ads\\GoogleAds\\V17\\Errors\xea\x02#Google::Ads::GoogleAds::V17::Errorsb\x06proto3')
_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'google.ads.googleads.v17.errors.experiment_error_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
    _globals['DESCRIPTOR']._loaded_options = None
    _globals['DESCRIPTOR']._serialized_options = b'\n#com.google.ads.googleads.v17.errorsB\x14ExperimentErrorProtoP\x01ZEgoogle.golang.org/genproto/googleapis/ads/googleads/v17/errors;errors\xa2\x02\x03GAA\xaa\x02\x1fGoogle.Ads.GoogleAds.V17.Errors\xca\x02\x1fGoogle\\Ads\\GoogleAds\\V17\\Errors\xea\x02#Google::Ads::GoogleAds::V17::Errors'
    _globals['_EXPERIMENTERRORENUM']._serialized_start = 92
    _globals['_EXPERIMENTERRORENUM']._serialized_end = 1284
    _globals['_EXPERIMENTERRORENUM_EXPERIMENTERROR']._serialized_start = 116
    _globals['_EXPERIMENTERRORENUM_EXPERIMENTERROR']._serialized_end = 1284