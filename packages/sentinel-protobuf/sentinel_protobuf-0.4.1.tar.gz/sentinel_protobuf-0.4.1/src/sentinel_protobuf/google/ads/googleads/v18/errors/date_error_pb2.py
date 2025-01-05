"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_runtime_version.ValidateProtobufRuntimeVersion(_runtime_version.Domain.PUBLIC, 5, 28, 1, '', 'google/ads/googleads/v18/errors/date_error.proto')
_sym_db = _symbol_database.Default()
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n0google/ads/googleads/v18/errors/date_error.proto\x12\x1fgoogle.ads.googleads.v18.errors"\xbf\x03\n\rDateErrorEnum"\xad\x03\n\tDateError\x12\x0f\n\x0bUNSPECIFIED\x10\x00\x12\x0b\n\x07UNKNOWN\x10\x01\x12 \n\x1cINVALID_FIELD_VALUES_IN_DATE\x10\x02\x12%\n!INVALID_FIELD_VALUES_IN_DATE_TIME\x10\x03\x12\x17\n\x13INVALID_STRING_DATE\x10\x04\x12#\n\x1fINVALID_STRING_DATE_TIME_MICROS\x10\x06\x12$\n INVALID_STRING_DATE_TIME_SECONDS\x10\x0b\x120\n,INVALID_STRING_DATE_TIME_SECONDS_WITH_OFFSET\x10\x0c\x12\x1d\n\x19EARLIER_THAN_MINIMUM_DATE\x10\x07\x12\x1b\n\x17LATER_THAN_MAXIMUM_DATE\x10\x08\x123\n/DATE_RANGE_MINIMUM_DATE_LATER_THAN_MAXIMUM_DATE\x10\t\x122\n.DATE_RANGE_MINIMUM_AND_MAXIMUM_DATES_BOTH_NULL\x10\nB\xee\x01\n#com.google.ads.googleads.v18.errorsB\x0eDateErrorProtoP\x01ZEgoogle.golang.org/genproto/googleapis/ads/googleads/v18/errors;errors\xa2\x02\x03GAA\xaa\x02\x1fGoogle.Ads.GoogleAds.V18.Errors\xca\x02\x1fGoogle\\Ads\\GoogleAds\\V18\\Errors\xea\x02#Google::Ads::GoogleAds::V18::Errorsb\x06proto3')
_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'google.ads.googleads.v18.errors.date_error_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
    _globals['DESCRIPTOR']._loaded_options = None
    _globals['DESCRIPTOR']._serialized_options = b'\n#com.google.ads.googleads.v18.errorsB\x0eDateErrorProtoP\x01ZEgoogle.golang.org/genproto/googleapis/ads/googleads/v18/errors;errors\xa2\x02\x03GAA\xaa\x02\x1fGoogle.Ads.GoogleAds.V18.Errors\xca\x02\x1fGoogle\\Ads\\GoogleAds\\V18\\Errors\xea\x02#Google::Ads::GoogleAds::V18::Errors'
    _globals['_DATEERRORENUM']._serialized_start = 86
    _globals['_DATEERRORENUM']._serialized_end = 533
    _globals['_DATEERRORENUM_DATEERROR']._serialized_start = 104
    _globals['_DATEERRORENUM_DATEERROR']._serialized_end = 533