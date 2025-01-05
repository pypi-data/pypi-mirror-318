"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_runtime_version.ValidateProtobufRuntimeVersion(_runtime_version.Domain.PUBLIC, 5, 28, 1, '', 'google/ads/googleads/v18/resources/offline_conversion_upload_conversion_action_summary.proto')
_sym_db = _symbol_database.Default()
from ......google.ads.googleads.v18.enums import offline_conversion_diagnostic_status_enum_pb2 as google_dot_ads_dot_googleads_dot_v18_dot_enums_dot_offline__conversion__diagnostic__status__enum__pb2
from ......google.ads.googleads.v18.enums import offline_event_upload_client_enum_pb2 as google_dot_ads_dot_googleads_dot_v18_dot_enums_dot_offline__event__upload__client__enum__pb2
from ......google.ads.googleads.v18.resources import offline_conversion_upload_client_summary_pb2 as google_dot_ads_dot_googleads_dot_v18_dot_resources_dot_offline__conversion__upload__client__summary__pb2
from ......google.api import field_behavior_pb2 as google_dot_api_dot_field__behavior__pb2
from ......google.api import resource_pb2 as google_dot_api_dot_resource__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\\google/ads/googleads/v18/resources/offline_conversion_upload_conversion_action_summary.proto\x12"google.ads.googleads.v18.resources\x1aNgoogle/ads/googleads/v18/enums/offline_conversion_diagnostic_status_enum.proto\x1aEgoogle/ads/googleads/v18/enums/offline_event_upload_client_enum.proto\x1aQgoogle/ads/googleads/v18/resources/offline_conversion_upload_client_summary.proto\x1a\x1fgoogle/api/field_behavior.proto\x1a\x19google/api/resource.proto"\x94\x08\n.OfflineConversionUploadConversionActionSummary\x12f\n\rresource_name\x18\x01 \x01(\tBO\xe0A\x03\xfaAI\nGgoogleads.googleapis.com/OfflineConversionUploadConversionActionSummary\x12j\n\x06client\x18\x02 \x01(\x0e2U.google.ads.googleads.v18.enums.OfflineEventUploadClientEnum.OfflineEventUploadClientB\x03\xe0A\x03\x12!\n\x14conversion_action_id\x18\x03 \x01(\x03B\x03\xe0A\x03\x12#\n\x16conversion_action_name\x18\x04 \x01(\tB\x03\xe0A\x03\x12|\n\x06status\x18\x05 \x01(\x0e2g.google.ads.googleads.v18.enums.OfflineConversionDiagnosticStatusEnum.OfflineConversionDiagnosticStatusB\x03\xe0A\x03\x12\x1e\n\x11total_event_count\x18\x06 \x01(\x03B\x03\xe0A\x03\x12#\n\x16successful_event_count\x18\x07 \x01(\x03B\x03\xe0A\x03\x12 \n\x13pending_event_count\x18\x08 \x01(\x03B\x03\xe0A\x03\x12"\n\x15last_upload_date_time\x18\t \x01(\tB\x03\xe0A\x03\x12Z\n\x0fdaily_summaries\x18\n \x03(\x0b2<.google.ads.googleads.v18.resources.OfflineConversionSummaryB\x03\xe0A\x03\x12X\n\rjob_summaries\x18\x0b \x03(\x0b2<.google.ads.googleads.v18.resources.OfflineConversionSummaryB\x03\xe0A\x03\x12O\n\x06alerts\x18\x0c \x03(\x0b2:.google.ads.googleads.v18.resources.OfflineConversionAlertB\x03\xe0A\x03:\xb5\x01\xeaA\xb1\x01\nGgoogleads.googleapis.com/OfflineConversionUploadConversionActionSummary\x12fcustomers/{customer_id}/offlineConversionUploadConversionActionSummaries/{conversion_type_id}~{client}B\xa5\x02\n&com.google.ads.googleads.v18.resourcesB3OfflineConversionUploadConversionActionSummaryProtoP\x01ZKgoogle.golang.org/genproto/googleapis/ads/googleads/v18/resources;resources\xa2\x02\x03GAA\xaa\x02"Google.Ads.GoogleAds.V18.Resources\xca\x02"Google\\Ads\\GoogleAds\\V18\\Resources\xea\x02&Google::Ads::GoogleAds::V18::Resourcesb\x06proto3')
_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'google.ads.googleads.v18.resources.offline_conversion_upload_conversion_action_summary_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
    _globals['DESCRIPTOR']._loaded_options = None
    _globals['DESCRIPTOR']._serialized_options = b'\n&com.google.ads.googleads.v18.resourcesB3OfflineConversionUploadConversionActionSummaryProtoP\x01ZKgoogle.golang.org/genproto/googleapis/ads/googleads/v18/resources;resources\xa2\x02\x03GAA\xaa\x02"Google.Ads.GoogleAds.V18.Resources\xca\x02"Google\\Ads\\GoogleAds\\V18\\Resources\xea\x02&Google::Ads::GoogleAds::V18::Resources'
    _globals['_OFFLINECONVERSIONUPLOADCONVERSIONACTIONSUMMARY'].fields_by_name['resource_name']._loaded_options = None
    _globals['_OFFLINECONVERSIONUPLOADCONVERSIONACTIONSUMMARY'].fields_by_name['resource_name']._serialized_options = b'\xe0A\x03\xfaAI\nGgoogleads.googleapis.com/OfflineConversionUploadConversionActionSummary'
    _globals['_OFFLINECONVERSIONUPLOADCONVERSIONACTIONSUMMARY'].fields_by_name['client']._loaded_options = None
    _globals['_OFFLINECONVERSIONUPLOADCONVERSIONACTIONSUMMARY'].fields_by_name['client']._serialized_options = b'\xe0A\x03'
    _globals['_OFFLINECONVERSIONUPLOADCONVERSIONACTIONSUMMARY'].fields_by_name['conversion_action_id']._loaded_options = None
    _globals['_OFFLINECONVERSIONUPLOADCONVERSIONACTIONSUMMARY'].fields_by_name['conversion_action_id']._serialized_options = b'\xe0A\x03'
    _globals['_OFFLINECONVERSIONUPLOADCONVERSIONACTIONSUMMARY'].fields_by_name['conversion_action_name']._loaded_options = None
    _globals['_OFFLINECONVERSIONUPLOADCONVERSIONACTIONSUMMARY'].fields_by_name['conversion_action_name']._serialized_options = b'\xe0A\x03'
    _globals['_OFFLINECONVERSIONUPLOADCONVERSIONACTIONSUMMARY'].fields_by_name['status']._loaded_options = None
    _globals['_OFFLINECONVERSIONUPLOADCONVERSIONACTIONSUMMARY'].fields_by_name['status']._serialized_options = b'\xe0A\x03'
    _globals['_OFFLINECONVERSIONUPLOADCONVERSIONACTIONSUMMARY'].fields_by_name['total_event_count']._loaded_options = None
    _globals['_OFFLINECONVERSIONUPLOADCONVERSIONACTIONSUMMARY'].fields_by_name['total_event_count']._serialized_options = b'\xe0A\x03'
    _globals['_OFFLINECONVERSIONUPLOADCONVERSIONACTIONSUMMARY'].fields_by_name['successful_event_count']._loaded_options = None
    _globals['_OFFLINECONVERSIONUPLOADCONVERSIONACTIONSUMMARY'].fields_by_name['successful_event_count']._serialized_options = b'\xe0A\x03'
    _globals['_OFFLINECONVERSIONUPLOADCONVERSIONACTIONSUMMARY'].fields_by_name['pending_event_count']._loaded_options = None
    _globals['_OFFLINECONVERSIONUPLOADCONVERSIONACTIONSUMMARY'].fields_by_name['pending_event_count']._serialized_options = b'\xe0A\x03'
    _globals['_OFFLINECONVERSIONUPLOADCONVERSIONACTIONSUMMARY'].fields_by_name['last_upload_date_time']._loaded_options = None
    _globals['_OFFLINECONVERSIONUPLOADCONVERSIONACTIONSUMMARY'].fields_by_name['last_upload_date_time']._serialized_options = b'\xe0A\x03'
    _globals['_OFFLINECONVERSIONUPLOADCONVERSIONACTIONSUMMARY'].fields_by_name['daily_summaries']._loaded_options = None
    _globals['_OFFLINECONVERSIONUPLOADCONVERSIONACTIONSUMMARY'].fields_by_name['daily_summaries']._serialized_options = b'\xe0A\x03'
    _globals['_OFFLINECONVERSIONUPLOADCONVERSIONACTIONSUMMARY'].fields_by_name['job_summaries']._loaded_options = None
    _globals['_OFFLINECONVERSIONUPLOADCONVERSIONACTIONSUMMARY'].fields_by_name['job_summaries']._serialized_options = b'\xe0A\x03'
    _globals['_OFFLINECONVERSIONUPLOADCONVERSIONACTIONSUMMARY'].fields_by_name['alerts']._loaded_options = None
    _globals['_OFFLINECONVERSIONUPLOADCONVERSIONACTIONSUMMARY'].fields_by_name['alerts']._serialized_options = b'\xe0A\x03'
    _globals['_OFFLINECONVERSIONUPLOADCONVERSIONACTIONSUMMARY']._loaded_options = None
    _globals['_OFFLINECONVERSIONUPLOADCONVERSIONACTIONSUMMARY']._serialized_options = b'\xeaA\xb1\x01\nGgoogleads.googleapis.com/OfflineConversionUploadConversionActionSummary\x12fcustomers/{customer_id}/offlineConversionUploadConversionActionSummaries/{conversion_type_id}~{client}'
    _globals['_OFFLINECONVERSIONUPLOADCONVERSIONACTIONSUMMARY']._serialized_start = 427
    _globals['_OFFLINECONVERSIONUPLOADCONVERSIONACTIONSUMMARY']._serialized_end = 1471