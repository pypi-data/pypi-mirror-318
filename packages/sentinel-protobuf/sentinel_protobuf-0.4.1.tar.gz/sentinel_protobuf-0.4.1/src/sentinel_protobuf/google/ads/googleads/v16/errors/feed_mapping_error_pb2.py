"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_runtime_version.ValidateProtobufRuntimeVersion(_runtime_version.Domain.PUBLIC, 5, 28, 1, '', 'google/ads/googleads/v16/errors/feed_mapping_error.proto')
_sym_db = _symbol_database.Default()
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n8google/ads/googleads/v16/errors/feed_mapping_error.proto\x12\x1fgoogle.ads.googleads.v16.errors"\xb2\x06\n\x14FeedMappingErrorEnum"\x99\x06\n\x10FeedMappingError\x12\x0f\n\x0bUNSPECIFIED\x10\x00\x12\x0b\n\x07UNKNOWN\x10\x01\x12\x1d\n\x19INVALID_PLACEHOLDER_FIELD\x10\x02\x12\x1b\n\x17INVALID_CRITERION_FIELD\x10\x03\x12\x1c\n\x18INVALID_PLACEHOLDER_TYPE\x10\x04\x12\x1a\n\x16INVALID_CRITERION_TYPE\x10\x05\x12\x1f\n\x1bNO_ATTRIBUTE_FIELD_MAPPINGS\x10\x07\x12 \n\x1cFEED_ATTRIBUTE_TYPE_MISMATCH\x10\x08\x128\n4CANNOT_OPERATE_ON_MAPPINGS_FOR_SYSTEM_GENERATED_FEED\x10\t\x12*\n&MULTIPLE_MAPPINGS_FOR_PLACEHOLDER_TYPE\x10\n\x12(\n$MULTIPLE_MAPPINGS_FOR_CRITERION_TYPE\x10\x0b\x12+\n\'MULTIPLE_MAPPINGS_FOR_PLACEHOLDER_FIELD\x10\x0c\x12)\n%MULTIPLE_MAPPINGS_FOR_CRITERION_FIELD\x10\r\x12\'\n#UNEXPECTED_ATTRIBUTE_FIELD_MAPPINGS\x10\x0e\x12.\n*LOCATION_PLACEHOLDER_ONLY_FOR_PLACES_FEEDS\x10\x0f\x12)\n%CANNOT_MODIFY_MAPPINGS_FOR_TYPED_FEED\x10\x10\x12:\n6INVALID_PLACEHOLDER_TYPE_FOR_NON_SYSTEM_GENERATED_FEED\x10\x11\x12;\n7INVALID_PLACEHOLDER_TYPE_FOR_SYSTEM_GENERATED_FEED_TYPE\x10\x12\x12)\n%ATTRIBUTE_FIELD_MAPPING_MISSING_FIELD\x10\x13\x12\x1e\n\x1aLEGACY_FEED_TYPE_READ_ONLY\x10\x14B\xf5\x01\n#com.google.ads.googleads.v16.errorsB\x15FeedMappingErrorProtoP\x01ZEgoogle.golang.org/genproto/googleapis/ads/googleads/v16/errors;errors\xa2\x02\x03GAA\xaa\x02\x1fGoogle.Ads.GoogleAds.V16.Errors\xca\x02\x1fGoogle\\Ads\\GoogleAds\\V16\\Errors\xea\x02#Google::Ads::GoogleAds::V16::Errorsb\x06proto3')
_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'google.ads.googleads.v16.errors.feed_mapping_error_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
    _globals['DESCRIPTOR']._loaded_options = None
    _globals['DESCRIPTOR']._serialized_options = b'\n#com.google.ads.googleads.v16.errorsB\x15FeedMappingErrorProtoP\x01ZEgoogle.golang.org/genproto/googleapis/ads/googleads/v16/errors;errors\xa2\x02\x03GAA\xaa\x02\x1fGoogle.Ads.GoogleAds.V16.Errors\xca\x02\x1fGoogle\\Ads\\GoogleAds\\V16\\Errors\xea\x02#Google::Ads::GoogleAds::V16::Errors'
    _globals['_FEEDMAPPINGERRORENUM']._serialized_start = 94
    _globals['_FEEDMAPPINGERRORENUM']._serialized_end = 912
    _globals['_FEEDMAPPINGERRORENUM_FEEDMAPPINGERROR']._serialized_start = 119
    _globals['_FEEDMAPPINGERRORENUM_FEEDMAPPINGERROR']._serialized_end = 912