"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_runtime_version.ValidateProtobufRuntimeVersion(_runtime_version.Domain.PUBLIC, 5, 28, 1, '', 'google/ads/googleads/v18/errors/campaign_draft_error.proto')
_sym_db = _symbol_database.Default()
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n:google/ads/googleads/v18/errors/campaign_draft_error.proto\x12\x1fgoogle.ads.googleads.v18.errors"\xc8\x03\n\x16CampaignDraftErrorEnum"\xad\x03\n\x12CampaignDraftError\x12\x0f\n\x0bUNSPECIFIED\x10\x00\x12\x0b\n\x07UNKNOWN\x10\x01\x12\x18\n\x14DUPLICATE_DRAFT_NAME\x10\x02\x12*\n&INVALID_STATUS_TRANSITION_FROM_REMOVED\x10\x03\x12+\n\'INVALID_STATUS_TRANSITION_FROM_PROMOTED\x10\x04\x121\n-INVALID_STATUS_TRANSITION_FROM_PROMOTE_FAILED\x10\x05\x12 \n\x1cCUSTOMER_CANNOT_CREATE_DRAFT\x10\x06\x12 \n\x1cCAMPAIGN_CANNOT_CREATE_DRAFT\x10\x07\x12\x18\n\x14INVALID_DRAFT_CHANGE\x10\x08\x12\x1d\n\x19INVALID_STATUS_TRANSITION\x10\t\x12-\n)MAX_NUMBER_OF_DRAFTS_PER_CAMPAIGN_REACHED\x10\n\x12\'\n#LIST_ERRORS_FOR_PROMOTED_DRAFT_ONLY\x10\x0bB\xf7\x01\n#com.google.ads.googleads.v18.errorsB\x17CampaignDraftErrorProtoP\x01ZEgoogle.golang.org/genproto/googleapis/ads/googleads/v18/errors;errors\xa2\x02\x03GAA\xaa\x02\x1fGoogle.Ads.GoogleAds.V18.Errors\xca\x02\x1fGoogle\\Ads\\GoogleAds\\V18\\Errors\xea\x02#Google::Ads::GoogleAds::V18::Errorsb\x06proto3')
_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'google.ads.googleads.v18.errors.campaign_draft_error_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
    _globals['DESCRIPTOR']._loaded_options = None
    _globals['DESCRIPTOR']._serialized_options = b'\n#com.google.ads.googleads.v18.errorsB\x17CampaignDraftErrorProtoP\x01ZEgoogle.golang.org/genproto/googleapis/ads/googleads/v18/errors;errors\xa2\x02\x03GAA\xaa\x02\x1fGoogle.Ads.GoogleAds.V18.Errors\xca\x02\x1fGoogle\\Ads\\GoogleAds\\V18\\Errors\xea\x02#Google::Ads::GoogleAds::V18::Errors'
    _globals['_CAMPAIGNDRAFTERRORENUM']._serialized_start = 96
    _globals['_CAMPAIGNDRAFTERRORENUM']._serialized_end = 552
    _globals['_CAMPAIGNDRAFTERRORENUM_CAMPAIGNDRAFTERROR']._serialized_start = 123
    _globals['_CAMPAIGNDRAFTERRORENUM_CAMPAIGNDRAFTERROR']._serialized_end = 552