"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_runtime_version.ValidateProtobufRuntimeVersion(_runtime_version.Domain.PUBLIC, 5, 28, 1, '', 'google/ads/googleads/v16/resources/lead_form_submission_data.proto')
_sym_db = _symbol_database.Default()
from ......google.ads.googleads.v16.enums import lead_form_field_user_input_type_pb2 as google_dot_ads_dot_googleads_dot_v16_dot_enums_dot_lead__form__field__user__input__type__pb2
from ......google.api import field_behavior_pb2 as google_dot_api_dot_field__behavior__pb2
from ......google.api import resource_pb2 as google_dot_api_dot_resource__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\nBgoogle/ads/googleads/v16/resources/lead_form_submission_data.proto\x12"google.ads.googleads.v16.resources\x1aDgoogle/ads/googleads/v16/enums/lead_form_field_user_input_type.proto\x1a\x1fgoogle/api/field_behavior.proto\x1a\x19google/api/resource.proto"\x83\x06\n\x16LeadFormSubmissionData\x12N\n\rresource_name\x18\x01 \x01(\tB7\xe0A\x03\xfaA1\n/googleads.googleapis.com/LeadFormSubmissionData\x12\x0f\n\x02id\x18\x02 \x01(\tB\x03\xe0A\x03\x125\n\x05asset\x18\x03 \x01(\tB&\xe0A\x03\xfaA \n\x1egoogleads.googleapis.com/Asset\x12;\n\x08campaign\x18\x04 \x01(\tB)\xe0A\x03\xfaA#\n!googleads.googleapis.com/Campaign\x12e\n\x1blead_form_submission_fields\x18\x05 \x03(\x0b2;.google.ads.googleads.v16.resources.LeadFormSubmissionFieldB\x03\xe0A\x03\x12r\n"custom_lead_form_submission_fields\x18\n \x03(\x0b2A.google.ads.googleads.v16.resources.CustomLeadFormSubmissionFieldB\x03\xe0A\x03\x12:\n\x08ad_group\x18\x06 \x01(\tB(\xe0A\x03\xfaA"\n googleads.googleapis.com/AdGroup\x12?\n\x0bad_group_ad\x18\x07 \x01(\tB*\xe0A\x03\xfaA$\n"googleads.googleapis.com/AdGroupAd\x12\x12\n\x05gclid\x18\x08 \x01(\tB\x03\xe0A\x03\x12!\n\x14submission_date_time\x18\t \x01(\tB\x03\xe0A\x03:\x84\x01\xeaA\x80\x01\n/googleads.googleapis.com/LeadFormSubmissionData\x12Mcustomers/{customer_id}/leadFormSubmissionData/{lead_form_user_submission_id}"\xa7\x01\n\x17LeadFormSubmissionField\x12r\n\nfield_type\x18\x01 \x01(\x0e2Y.google.ads.googleads.v16.enums.LeadFormFieldUserInputTypeEnum.LeadFormFieldUserInputTypeB\x03\xe0A\x03\x12\x18\n\x0bfield_value\x18\x02 \x01(\tB\x03\xe0A\x03"U\n\x1dCustomLeadFormSubmissionField\x12\x1a\n\rquestion_text\x18\x01 \x01(\tB\x03\xe0A\x03\x12\x18\n\x0bfield_value\x18\x02 \x01(\tB\x03\xe0A\x03B\x8d\x02\n&com.google.ads.googleads.v16.resourcesB\x1bLeadFormSubmissionDataProtoP\x01ZKgoogle.golang.org/genproto/googleapis/ads/googleads/v16/resources;resources\xa2\x02\x03GAA\xaa\x02"Google.Ads.GoogleAds.V16.Resources\xca\x02"Google\\Ads\\GoogleAds\\V16\\Resources\xea\x02&Google::Ads::GoogleAds::V16::Resourcesb\x06proto3')
_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'google.ads.googleads.v16.resources.lead_form_submission_data_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
    _globals['DESCRIPTOR']._loaded_options = None
    _globals['DESCRIPTOR']._serialized_options = b'\n&com.google.ads.googleads.v16.resourcesB\x1bLeadFormSubmissionDataProtoP\x01ZKgoogle.golang.org/genproto/googleapis/ads/googleads/v16/resources;resources\xa2\x02\x03GAA\xaa\x02"Google.Ads.GoogleAds.V16.Resources\xca\x02"Google\\Ads\\GoogleAds\\V16\\Resources\xea\x02&Google::Ads::GoogleAds::V16::Resources'
    _globals['_LEADFORMSUBMISSIONDATA'].fields_by_name['resource_name']._loaded_options = None
    _globals['_LEADFORMSUBMISSIONDATA'].fields_by_name['resource_name']._serialized_options = b'\xe0A\x03\xfaA1\n/googleads.googleapis.com/LeadFormSubmissionData'
    _globals['_LEADFORMSUBMISSIONDATA'].fields_by_name['id']._loaded_options = None
    _globals['_LEADFORMSUBMISSIONDATA'].fields_by_name['id']._serialized_options = b'\xe0A\x03'
    _globals['_LEADFORMSUBMISSIONDATA'].fields_by_name['asset']._loaded_options = None
    _globals['_LEADFORMSUBMISSIONDATA'].fields_by_name['asset']._serialized_options = b'\xe0A\x03\xfaA \n\x1egoogleads.googleapis.com/Asset'
    _globals['_LEADFORMSUBMISSIONDATA'].fields_by_name['campaign']._loaded_options = None
    _globals['_LEADFORMSUBMISSIONDATA'].fields_by_name['campaign']._serialized_options = b'\xe0A\x03\xfaA#\n!googleads.googleapis.com/Campaign'
    _globals['_LEADFORMSUBMISSIONDATA'].fields_by_name['lead_form_submission_fields']._loaded_options = None
    _globals['_LEADFORMSUBMISSIONDATA'].fields_by_name['lead_form_submission_fields']._serialized_options = b'\xe0A\x03'
    _globals['_LEADFORMSUBMISSIONDATA'].fields_by_name['custom_lead_form_submission_fields']._loaded_options = None
    _globals['_LEADFORMSUBMISSIONDATA'].fields_by_name['custom_lead_form_submission_fields']._serialized_options = b'\xe0A\x03'
    _globals['_LEADFORMSUBMISSIONDATA'].fields_by_name['ad_group']._loaded_options = None
    _globals['_LEADFORMSUBMISSIONDATA'].fields_by_name['ad_group']._serialized_options = b'\xe0A\x03\xfaA"\n googleads.googleapis.com/AdGroup'
    _globals['_LEADFORMSUBMISSIONDATA'].fields_by_name['ad_group_ad']._loaded_options = None
    _globals['_LEADFORMSUBMISSIONDATA'].fields_by_name['ad_group_ad']._serialized_options = b'\xe0A\x03\xfaA$\n"googleads.googleapis.com/AdGroupAd'
    _globals['_LEADFORMSUBMISSIONDATA'].fields_by_name['gclid']._loaded_options = None
    _globals['_LEADFORMSUBMISSIONDATA'].fields_by_name['gclid']._serialized_options = b'\xe0A\x03'
    _globals['_LEADFORMSUBMISSIONDATA'].fields_by_name['submission_date_time']._loaded_options = None
    _globals['_LEADFORMSUBMISSIONDATA'].fields_by_name['submission_date_time']._serialized_options = b'\xe0A\x03'
    _globals['_LEADFORMSUBMISSIONDATA']._loaded_options = None
    _globals['_LEADFORMSUBMISSIONDATA']._serialized_options = b'\xeaA\x80\x01\n/googleads.googleapis.com/LeadFormSubmissionData\x12Mcustomers/{customer_id}/leadFormSubmissionData/{lead_form_user_submission_id}'
    _globals['_LEADFORMSUBMISSIONFIELD'].fields_by_name['field_type']._loaded_options = None
    _globals['_LEADFORMSUBMISSIONFIELD'].fields_by_name['field_type']._serialized_options = b'\xe0A\x03'
    _globals['_LEADFORMSUBMISSIONFIELD'].fields_by_name['field_value']._loaded_options = None
    _globals['_LEADFORMSUBMISSIONFIELD'].fields_by_name['field_value']._serialized_options = b'\xe0A\x03'
    _globals['_CUSTOMLEADFORMSUBMISSIONFIELD'].fields_by_name['question_text']._loaded_options = None
    _globals['_CUSTOMLEADFORMSUBMISSIONFIELD'].fields_by_name['question_text']._serialized_options = b'\xe0A\x03'
    _globals['_CUSTOMLEADFORMSUBMISSIONFIELD'].fields_by_name['field_value']._loaded_options = None
    _globals['_CUSTOMLEADFORMSUBMISSIONFIELD'].fields_by_name['field_value']._serialized_options = b'\xe0A\x03'
    _globals['_LEADFORMSUBMISSIONDATA']._serialized_start = 237
    _globals['_LEADFORMSUBMISSIONDATA']._serialized_end = 1008
    _globals['_LEADFORMSUBMISSIONFIELD']._serialized_start = 1011
    _globals['_LEADFORMSUBMISSIONFIELD']._serialized_end = 1178
    _globals['_CUSTOMLEADFORMSUBMISSIONFIELD']._serialized_start = 1180
    _globals['_CUSTOMLEADFORMSUBMISSIONFIELD']._serialized_end = 1265