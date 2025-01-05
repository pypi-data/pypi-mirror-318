"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_runtime_version.ValidateProtobufRuntimeVersion(_runtime_version.Domain.PUBLIC, 5, 28, 1, '', 'google/ads/googleads/v18/resources/offline_conversion_upload_client_summary.proto')
_sym_db = _symbol_database.Default()
from ......google.ads.googleads.v18.enums import offline_conversion_diagnostic_status_enum_pb2 as google_dot_ads_dot_googleads_dot_v18_dot_enums_dot_offline__conversion__diagnostic__status__enum__pb2
from ......google.ads.googleads.v18.enums import offline_event_upload_client_enum_pb2 as google_dot_ads_dot_googleads_dot_v18_dot_enums_dot_offline__event__upload__client__enum__pb2
from ......google.ads.googleads.v18.errors import collection_size_error_pb2 as google_dot_ads_dot_googleads_dot_v18_dot_errors_dot_collection__size__error__pb2
from ......google.ads.googleads.v18.errors import conversion_adjustment_upload_error_pb2 as google_dot_ads_dot_googleads_dot_v18_dot_errors_dot_conversion__adjustment__upload__error__pb2
from ......google.ads.googleads.v18.errors import conversion_upload_error_pb2 as google_dot_ads_dot_googleads_dot_v18_dot_errors_dot_conversion__upload__error__pb2
from ......google.ads.googleads.v18.errors import date_error_pb2 as google_dot_ads_dot_googleads_dot_v18_dot_errors_dot_date__error__pb2
from ......google.ads.googleads.v18.errors import distinct_error_pb2 as google_dot_ads_dot_googleads_dot_v18_dot_errors_dot_distinct__error__pb2
from ......google.ads.googleads.v18.errors import field_error_pb2 as google_dot_ads_dot_googleads_dot_v18_dot_errors_dot_field__error__pb2
from ......google.ads.googleads.v18.errors import mutate_error_pb2 as google_dot_ads_dot_googleads_dot_v18_dot_errors_dot_mutate__error__pb2
from ......google.ads.googleads.v18.errors import not_allowlisted_error_pb2 as google_dot_ads_dot_googleads_dot_v18_dot_errors_dot_not__allowlisted__error__pb2
from ......google.ads.googleads.v18.errors import string_format_error_pb2 as google_dot_ads_dot_googleads_dot_v18_dot_errors_dot_string__format__error__pb2
from ......google.ads.googleads.v18.errors import string_length_error_pb2 as google_dot_ads_dot_googleads_dot_v18_dot_errors_dot_string__length__error__pb2
from ......google.api import field_behavior_pb2 as google_dot_api_dot_field__behavior__pb2
from ......google.api import resource_pb2 as google_dot_api_dot_resource__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\nQgoogle/ads/googleads/v18/resources/offline_conversion_upload_client_summary.proto\x12"google.ads.googleads.v18.resources\x1aNgoogle/ads/googleads/v18/enums/offline_conversion_diagnostic_status_enum.proto\x1aEgoogle/ads/googleads/v18/enums/offline_event_upload_client_enum.proto\x1a;google/ads/googleads/v18/errors/collection_size_error.proto\x1aHgoogle/ads/googleads/v18/errors/conversion_adjustment_upload_error.proto\x1a=google/ads/googleads/v18/errors/conversion_upload_error.proto\x1a0google/ads/googleads/v18/errors/date_error.proto\x1a4google/ads/googleads/v18/errors/distinct_error.proto\x1a1google/ads/googleads/v18/errors/field_error.proto\x1a2google/ads/googleads/v18/errors/mutate_error.proto\x1a;google/ads/googleads/v18/errors/not_allowlisted_error.proto\x1a9google/ads/googleads/v18/errors/string_format_error.proto\x1a9google/ads/googleads/v18/errors/string_length_error.proto\x1a\x1fgoogle/api/field_behavior.proto\x1a\x19google/api/resource.proto"\xc5\x07\n$OfflineConversionUploadClientSummary\x12\\\n\rresource_name\x18\x01 \x01(\tBE\xe0A\x03\xfaA?\n=googleads.googleapis.com/OfflineConversionUploadClientSummary\x12j\n\x06client\x18\x02 \x01(\x0e2U.google.ads.googleads.v18.enums.OfflineEventUploadClientEnum.OfflineEventUploadClientB\x03\xe0A\x03\x12|\n\x06status\x18\x03 \x01(\x0e2g.google.ads.googleads.v18.enums.OfflineConversionDiagnosticStatusEnum.OfflineConversionDiagnosticStatusB\x03\xe0A\x03\x12\x1e\n\x11total_event_count\x18\x04 \x01(\x03B\x03\xe0A\x03\x12#\n\x16successful_event_count\x18\x05 \x01(\x03B\x03\xe0A\x03\x12\x19\n\x0csuccess_rate\x18\x06 \x01(\x01B\x03\xe0A\x03\x12 \n\x13pending_event_count\x18\x0b \x01(\x03B\x03\xe0A\x03\x12\x19\n\x0cpending_rate\x18\x0c \x01(\x01B\x03\xe0A\x03\x12"\n\x15last_upload_date_time\x18\x07 \x01(\tB\x03\xe0A\x03\x12Z\n\x0fdaily_summaries\x18\x08 \x03(\x0b2<.google.ads.googleads.v18.resources.OfflineConversionSummaryB\x03\xe0A\x03\x12X\n\rjob_summaries\x18\t \x03(\x0b2<.google.ads.googleads.v18.resources.OfflineConversionSummaryB\x03\xe0A\x03\x12O\n\x06alerts\x18\n \x03(\x0b2:.google.ads.googleads.v18.resources.OfflineConversionAlertB\x03\xe0A\x03:\x8c\x01\xeaA\x88\x01\n=googleads.googleapis.com/OfflineConversionUploadClientSummary\x12Gcustomers/{customer_id}/offlineConversionUploadClientSummaries/{client}"\xb4\x01\n\x18OfflineConversionSummary\x12\x1d\n\x10successful_count\x18\x03 \x01(\x03B\x03\xe0A\x03\x12\x19\n\x0cfailed_count\x18\x04 \x01(\x03B\x03\xe0A\x03\x12\x1a\n\rpending_count\x18\x05 \x01(\x03B\x03\xe0A\x03\x12\x15\n\x06job_id\x18\x01 \x01(\x03B\x03\xe0A\x03H\x00\x12\x1a\n\x0bupload_date\x18\x02 \x01(\tB\x03\xe0A\x03H\x00B\x0f\n\rdimension_key"\x87\x01\n\x16OfflineConversionAlert\x12N\n\x05error\x18\x01 \x01(\x0b2:.google.ads.googleads.v18.resources.OfflineConversionErrorB\x03\xe0A\x03\x12\x1d\n\x10error_percentage\x18\x02 \x01(\x01B\x03\xe0A\x03"\xe7\x08\n\x16OfflineConversionError\x12r\n\x15collection_size_error\x18\x01 \x01(\x0e2L.google.ads.googleads.v18.errors.CollectionSizeErrorEnum.CollectionSizeErrorB\x03\xe0A\x03H\x00\x12\x97\x01\n"conversion_adjustment_upload_error\x18\x02 \x01(\x0e2d.google.ads.googleads.v18.errors.ConversionAdjustmentUploadErrorEnum.ConversionAdjustmentUploadErrorB\x03\xe0A\x03H\x00\x12x\n\x17conversion_upload_error\x18\x03 \x01(\x0e2P.google.ads.googleads.v18.errors.ConversionUploadErrorEnum.ConversionUploadErrorB\x03\xe0A\x03H\x00\x12S\n\ndate_error\x18\x04 \x01(\x0e28.google.ads.googleads.v18.errors.DateErrorEnum.DateErrorB\x03\xe0A\x03H\x00\x12_\n\x0edistinct_error\x18\x05 \x01(\x0e2@.google.ads.googleads.v18.errors.DistinctErrorEnum.DistinctErrorB\x03\xe0A\x03H\x00\x12V\n\x0bfield_error\x18\x06 \x01(\x0e2:.google.ads.googleads.v18.errors.FieldErrorEnum.FieldErrorB\x03\xe0A\x03H\x00\x12Y\n\x0cmutate_error\x18\x07 \x01(\x0e2<.google.ads.googleads.v18.errors.MutateErrorEnum.MutateErrorB\x03\xe0A\x03H\x00\x12r\n\x15not_allowlisted_error\x18\x08 \x01(\x0e2L.google.ads.googleads.v18.errors.NotAllowlistedErrorEnum.NotAllowlistedErrorB\x03\xe0A\x03H\x00\x12l\n\x13string_format_error\x18\t \x01(\x0e2H.google.ads.googleads.v18.errors.StringFormatErrorEnum.StringFormatErrorB\x03\xe0A\x03H\x00\x12l\n\x13string_length_error\x18\n \x01(\x0e2H.google.ads.googleads.v18.errors.StringLengthErrorEnum.StringLengthErrorB\x03\xe0A\x03H\x00B\x0c\n\nerror_codeB\x9b\x02\n&com.google.ads.googleads.v18.resourcesB)OfflineConversionUploadClientSummaryProtoP\x01ZKgoogle.golang.org/genproto/googleapis/ads/googleads/v18/resources;resources\xa2\x02\x03GAA\xaa\x02"Google.Ads.GoogleAds.V18.Resources\xca\x02"Google\\Ads\\GoogleAds\\V18\\Resources\xea\x02&Google::Ads::GoogleAds::V18::Resourcesb\x06proto3')
_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'google.ads.googleads.v18.resources.offline_conversion_upload_client_summary_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
    _globals['DESCRIPTOR']._loaded_options = None
    _globals['DESCRIPTOR']._serialized_options = b'\n&com.google.ads.googleads.v18.resourcesB)OfflineConversionUploadClientSummaryProtoP\x01ZKgoogle.golang.org/genproto/googleapis/ads/googleads/v18/resources;resources\xa2\x02\x03GAA\xaa\x02"Google.Ads.GoogleAds.V18.Resources\xca\x02"Google\\Ads\\GoogleAds\\V18\\Resources\xea\x02&Google::Ads::GoogleAds::V18::Resources'
    _globals['_OFFLINECONVERSIONUPLOADCLIENTSUMMARY'].fields_by_name['resource_name']._loaded_options = None
    _globals['_OFFLINECONVERSIONUPLOADCLIENTSUMMARY'].fields_by_name['resource_name']._serialized_options = b'\xe0A\x03\xfaA?\n=googleads.googleapis.com/OfflineConversionUploadClientSummary'
    _globals['_OFFLINECONVERSIONUPLOADCLIENTSUMMARY'].fields_by_name['client']._loaded_options = None
    _globals['_OFFLINECONVERSIONUPLOADCLIENTSUMMARY'].fields_by_name['client']._serialized_options = b'\xe0A\x03'
    _globals['_OFFLINECONVERSIONUPLOADCLIENTSUMMARY'].fields_by_name['status']._loaded_options = None
    _globals['_OFFLINECONVERSIONUPLOADCLIENTSUMMARY'].fields_by_name['status']._serialized_options = b'\xe0A\x03'
    _globals['_OFFLINECONVERSIONUPLOADCLIENTSUMMARY'].fields_by_name['total_event_count']._loaded_options = None
    _globals['_OFFLINECONVERSIONUPLOADCLIENTSUMMARY'].fields_by_name['total_event_count']._serialized_options = b'\xe0A\x03'
    _globals['_OFFLINECONVERSIONUPLOADCLIENTSUMMARY'].fields_by_name['successful_event_count']._loaded_options = None
    _globals['_OFFLINECONVERSIONUPLOADCLIENTSUMMARY'].fields_by_name['successful_event_count']._serialized_options = b'\xe0A\x03'
    _globals['_OFFLINECONVERSIONUPLOADCLIENTSUMMARY'].fields_by_name['success_rate']._loaded_options = None
    _globals['_OFFLINECONVERSIONUPLOADCLIENTSUMMARY'].fields_by_name['success_rate']._serialized_options = b'\xe0A\x03'
    _globals['_OFFLINECONVERSIONUPLOADCLIENTSUMMARY'].fields_by_name['pending_event_count']._loaded_options = None
    _globals['_OFFLINECONVERSIONUPLOADCLIENTSUMMARY'].fields_by_name['pending_event_count']._serialized_options = b'\xe0A\x03'
    _globals['_OFFLINECONVERSIONUPLOADCLIENTSUMMARY'].fields_by_name['pending_rate']._loaded_options = None
    _globals['_OFFLINECONVERSIONUPLOADCLIENTSUMMARY'].fields_by_name['pending_rate']._serialized_options = b'\xe0A\x03'
    _globals['_OFFLINECONVERSIONUPLOADCLIENTSUMMARY'].fields_by_name['last_upload_date_time']._loaded_options = None
    _globals['_OFFLINECONVERSIONUPLOADCLIENTSUMMARY'].fields_by_name['last_upload_date_time']._serialized_options = b'\xe0A\x03'
    _globals['_OFFLINECONVERSIONUPLOADCLIENTSUMMARY'].fields_by_name['daily_summaries']._loaded_options = None
    _globals['_OFFLINECONVERSIONUPLOADCLIENTSUMMARY'].fields_by_name['daily_summaries']._serialized_options = b'\xe0A\x03'
    _globals['_OFFLINECONVERSIONUPLOADCLIENTSUMMARY'].fields_by_name['job_summaries']._loaded_options = None
    _globals['_OFFLINECONVERSIONUPLOADCLIENTSUMMARY'].fields_by_name['job_summaries']._serialized_options = b'\xe0A\x03'
    _globals['_OFFLINECONVERSIONUPLOADCLIENTSUMMARY'].fields_by_name['alerts']._loaded_options = None
    _globals['_OFFLINECONVERSIONUPLOADCLIENTSUMMARY'].fields_by_name['alerts']._serialized_options = b'\xe0A\x03'
    _globals['_OFFLINECONVERSIONUPLOADCLIENTSUMMARY']._loaded_options = None
    _globals['_OFFLINECONVERSIONUPLOADCLIENTSUMMARY']._serialized_options = b'\xeaA\x88\x01\n=googleads.googleapis.com/OfflineConversionUploadClientSummary\x12Gcustomers/{customer_id}/offlineConversionUploadClientSummaries/{client}'
    _globals['_OFFLINECONVERSIONSUMMARY'].fields_by_name['successful_count']._loaded_options = None
    _globals['_OFFLINECONVERSIONSUMMARY'].fields_by_name['successful_count']._serialized_options = b'\xe0A\x03'
    _globals['_OFFLINECONVERSIONSUMMARY'].fields_by_name['failed_count']._loaded_options = None
    _globals['_OFFLINECONVERSIONSUMMARY'].fields_by_name['failed_count']._serialized_options = b'\xe0A\x03'
    _globals['_OFFLINECONVERSIONSUMMARY'].fields_by_name['pending_count']._loaded_options = None
    _globals['_OFFLINECONVERSIONSUMMARY'].fields_by_name['pending_count']._serialized_options = b'\xe0A\x03'
    _globals['_OFFLINECONVERSIONSUMMARY'].fields_by_name['job_id']._loaded_options = None
    _globals['_OFFLINECONVERSIONSUMMARY'].fields_by_name['job_id']._serialized_options = b'\xe0A\x03'
    _globals['_OFFLINECONVERSIONSUMMARY'].fields_by_name['upload_date']._loaded_options = None
    _globals['_OFFLINECONVERSIONSUMMARY'].fields_by_name['upload_date']._serialized_options = b'\xe0A\x03'
    _globals['_OFFLINECONVERSIONALERT'].fields_by_name['error']._loaded_options = None
    _globals['_OFFLINECONVERSIONALERT'].fields_by_name['error']._serialized_options = b'\xe0A\x03'
    _globals['_OFFLINECONVERSIONALERT'].fields_by_name['error_percentage']._loaded_options = None
    _globals['_OFFLINECONVERSIONALERT'].fields_by_name['error_percentage']._serialized_options = b'\xe0A\x03'
    _globals['_OFFLINECONVERSIONERROR'].fields_by_name['collection_size_error']._loaded_options = None
    _globals['_OFFLINECONVERSIONERROR'].fields_by_name['collection_size_error']._serialized_options = b'\xe0A\x03'
    _globals['_OFFLINECONVERSIONERROR'].fields_by_name['conversion_adjustment_upload_error']._loaded_options = None
    _globals['_OFFLINECONVERSIONERROR'].fields_by_name['conversion_adjustment_upload_error']._serialized_options = b'\xe0A\x03'
    _globals['_OFFLINECONVERSIONERROR'].fields_by_name['conversion_upload_error']._loaded_options = None
    _globals['_OFFLINECONVERSIONERROR'].fields_by_name['conversion_upload_error']._serialized_options = b'\xe0A\x03'
    _globals['_OFFLINECONVERSIONERROR'].fields_by_name['date_error']._loaded_options = None
    _globals['_OFFLINECONVERSIONERROR'].fields_by_name['date_error']._serialized_options = b'\xe0A\x03'
    _globals['_OFFLINECONVERSIONERROR'].fields_by_name['distinct_error']._loaded_options = None
    _globals['_OFFLINECONVERSIONERROR'].fields_by_name['distinct_error']._serialized_options = b'\xe0A\x03'
    _globals['_OFFLINECONVERSIONERROR'].fields_by_name['field_error']._loaded_options = None
    _globals['_OFFLINECONVERSIONERROR'].fields_by_name['field_error']._serialized_options = b'\xe0A\x03'
    _globals['_OFFLINECONVERSIONERROR'].fields_by_name['mutate_error']._loaded_options = None
    _globals['_OFFLINECONVERSIONERROR'].fields_by_name['mutate_error']._serialized_options = b'\xe0A\x03'
    _globals['_OFFLINECONVERSIONERROR'].fields_by_name['not_allowlisted_error']._loaded_options = None
    _globals['_OFFLINECONVERSIONERROR'].fields_by_name['not_allowlisted_error']._serialized_options = b'\xe0A\x03'
    _globals['_OFFLINECONVERSIONERROR'].fields_by_name['string_format_error']._loaded_options = None
    _globals['_OFFLINECONVERSIONERROR'].fields_by_name['string_format_error']._serialized_options = b'\xe0A\x03'
    _globals['_OFFLINECONVERSIONERROR'].fields_by_name['string_length_error']._loaded_options = None
    _globals['_OFFLINECONVERSIONERROR'].fields_by_name['string_length_error']._serialized_options = b'\xe0A\x03'
    _globals['_OFFLINECONVERSIONUPLOADCLIENTSUMMARY']._serialized_start = 917
    _globals['_OFFLINECONVERSIONUPLOADCLIENTSUMMARY']._serialized_end = 1882
    _globals['_OFFLINECONVERSIONSUMMARY']._serialized_start = 1885
    _globals['_OFFLINECONVERSIONSUMMARY']._serialized_end = 2065
    _globals['_OFFLINECONVERSIONALERT']._serialized_start = 2068
    _globals['_OFFLINECONVERSIONALERT']._serialized_end = 2203
    _globals['_OFFLINECONVERSIONERROR']._serialized_start = 2206
    _globals['_OFFLINECONVERSIONERROR']._serialized_end = 3333