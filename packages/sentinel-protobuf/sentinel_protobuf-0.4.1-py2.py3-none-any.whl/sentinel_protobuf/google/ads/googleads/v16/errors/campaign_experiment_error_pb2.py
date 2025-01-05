"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_runtime_version.ValidateProtobufRuntimeVersion(_runtime_version.Domain.PUBLIC, 5, 28, 1, '', 'google/ads/googleads/v16/errors/campaign_experiment_error.proto')
_sym_db = _symbol_database.Default()
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n?google/ads/googleads/v16/errors/campaign_experiment_error.proto\x12\x1fgoogle.ads.googleads.v16.errors"\x80\x04\n\x1bCampaignExperimentErrorEnum"\xe0\x03\n\x17CampaignExperimentError\x12\x0f\n\x0bUNSPECIFIED\x10\x00\x12\x0b\n\x07UNKNOWN\x10\x01\x12\x12\n\x0eDUPLICATE_NAME\x10\x02\x12\x16\n\x12INVALID_TRANSITION\x10\x03\x12/\n+CANNOT_CREATE_EXPERIMENT_WITH_SHARED_BUDGET\x10\x04\x126\n2CANNOT_CREATE_EXPERIMENT_FOR_REMOVED_BASE_CAMPAIGN\x10\x05\x123\n/CANNOT_CREATE_EXPERIMENT_FOR_NON_PROPOSED_DRAFT\x10\x06\x12%\n!CUSTOMER_CANNOT_CREATE_EXPERIMENT\x10\x07\x12%\n!CAMPAIGN_CANNOT_CREATE_EXPERIMENT\x10\x08\x12)\n%EXPERIMENT_DURATIONS_MUST_NOT_OVERLAP\x10\t\x128\n4EXPERIMENT_DURATION_MUST_BE_WITHIN_CAMPAIGN_DURATION\x10\n\x12*\n&CANNOT_MUTATE_EXPERIMENT_DUE_TO_STATUS\x10\x0bB\xfc\x01\n#com.google.ads.googleads.v16.errorsB\x1cCampaignExperimentErrorProtoP\x01ZEgoogle.golang.org/genproto/googleapis/ads/googleads/v16/errors;errors\xa2\x02\x03GAA\xaa\x02\x1fGoogle.Ads.GoogleAds.V16.Errors\xca\x02\x1fGoogle\\Ads\\GoogleAds\\V16\\Errors\xea\x02#Google::Ads::GoogleAds::V16::Errorsb\x06proto3')
_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'google.ads.googleads.v16.errors.campaign_experiment_error_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
    _globals['DESCRIPTOR']._loaded_options = None
    _globals['DESCRIPTOR']._serialized_options = b'\n#com.google.ads.googleads.v16.errorsB\x1cCampaignExperimentErrorProtoP\x01ZEgoogle.golang.org/genproto/googleapis/ads/googleads/v16/errors;errors\xa2\x02\x03GAA\xaa\x02\x1fGoogle.Ads.GoogleAds.V16.Errors\xca\x02\x1fGoogle\\Ads\\GoogleAds\\V16\\Errors\xea\x02#Google::Ads::GoogleAds::V16::Errors'
    _globals['_CAMPAIGNEXPERIMENTERRORENUM']._serialized_start = 101
    _globals['_CAMPAIGNEXPERIMENTERRORENUM']._serialized_end = 613
    _globals['_CAMPAIGNEXPERIMENTERRORENUM_CAMPAIGNEXPERIMENTERROR']._serialized_start = 133
    _globals['_CAMPAIGNEXPERIMENTERRORENUM_CAMPAIGNEXPERIMENTERROR']._serialized_end = 613