"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_runtime_version.ValidateProtobufRuntimeVersion(_runtime_version.Domain.PUBLIC, 5, 28, 1, '', 'google/cloud/talent/v4beta1/filters.proto')
_sym_db = _symbol_database.Default()
from .....google.api import field_behavior_pb2 as google_dot_api_dot_field__behavior__pb2
from .....google.cloud.talent.v4beta1 import common_pb2 as google_dot_cloud_dot_talent_dot_v4beta1_dot_common__pb2
from google.protobuf import duration_pb2 as google_dot_protobuf_dot_duration__pb2
from .....google.type import latlng_pb2 as google_dot_type_dot_latlng__pb2
from .....google.type import timeofday_pb2 as google_dot_type_dot_timeofday__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n)google/cloud/talent/v4beta1/filters.proto\x12\x1bgoogle.cloud.talent.v4beta1\x1a\x1fgoogle/api/field_behavior.proto\x1a(google/cloud/talent/v4beta1/common.proto\x1a\x1egoogle/protobuf/duration.proto\x1a\x18google/type/latlng.proto\x1a\x1bgoogle/type/timeofday.proto"\x80\x05\n\x08JobQuery\x12\r\n\x05query\x18\x01 \x01(\t\x12\x1b\n\x13query_language_code\x18\x0e \x01(\t\x12\x11\n\tcompanies\x18\x02 \x03(\t\x12E\n\x10location_filters\x18\x03 \x03(\x0b2+.google.cloud.talent.v4beta1.LocationFilter\x12@\n\x0ejob_categories\x18\x04 \x03(\x0e2(.google.cloud.talent.v4beta1.JobCategory\x12B\n\x0ecommute_filter\x18\x05 \x01(\x0b2*.google.cloud.talent.v4beta1.CommuteFilter\x12\x1d\n\x15company_display_names\x18\x06 \x03(\t\x12L\n\x13compensation_filter\x18\x07 \x01(\x0b2/.google.cloud.talent.v4beta1.CompensationFilter\x12\x1f\n\x17custom_attribute_filter\x18\x08 \x01(\t\x12\x1b\n\x13disable_spell_check\x18\t \x01(\x08\x12E\n\x10employment_types\x18\n \x03(\x0e2+.google.cloud.talent.v4beta1.EmploymentType\x12\x16\n\x0elanguage_codes\x18\x0b \x03(\t\x12G\n\x12publish_time_range\x18\x0c \x01(\x0b2+.google.cloud.talent.v4beta1.TimestampRange\x12\x15\n\rexcluded_jobs\x18\r \x03(\t"\x83\x03\n\x0eLocationFilter\x12\x0f\n\x07address\x18\x01 \x01(\t\x12\x13\n\x0bregion_code\x18\x02 \x01(\t\x12$\n\x07lat_lng\x18\x03 \x01(\x0b2\x13.google.type.LatLng\x12\x19\n\x11distance_in_miles\x18\x04 \x01(\x01\x12a\n\x16telecommute_preference\x18\x05 \x01(\x0e2A.google.cloud.talent.v4beta1.LocationFilter.TelecommutePreference\x12\x0f\n\x07negated\x18\x06 \x01(\x08"\x95\x01\n\x15TelecommutePreference\x12&\n"TELECOMMUTE_PREFERENCE_UNSPECIFIED\x10\x00\x12\x1c\n\x14TELECOMMUTE_EXCLUDED\x10\x01\x1a\x02\x08\x01\x12\x17\n\x13TELECOMMUTE_ALLOWED\x10\x02\x12\x1d\n\x19TELECOMMUTE_JOBS_EXCLUDED\x10\x03"\xca\x03\n\x12CompensationFilter\x12M\n\x04type\x18\x01 \x01(\x0e2:.google.cloud.talent.v4beta1.CompensationFilter.FilterTypeB\x03\xe0A\x02\x12R\n\x05units\x18\x02 \x03(\x0e2>.google.cloud.talent.v4beta1.CompensationInfo.CompensationUnitB\x03\xe0A\x02\x12N\n\x05range\x18\x03 \x01(\x0b2?.google.cloud.talent.v4beta1.CompensationInfo.CompensationRange\x128\n0include_jobs_with_unspecified_compensation_range\x18\x04 \x01(\x08"\x86\x01\n\nFilterType\x12\x1b\n\x17FILTER_TYPE_UNSPECIFIED\x10\x00\x12\r\n\tUNIT_ONLY\x10\x01\x12\x13\n\x0fUNIT_AND_AMOUNT\x10\x02\x12\x1a\n\x16ANNUALIZED_BASE_AMOUNT\x10\x03\x12\x1b\n\x17ANNUALIZED_TOTAL_AMOUNT\x10\x04"\xcb\x03\n\rCommuteFilter\x12G\n\x0ecommute_method\x18\x01 \x01(\x0e2*.google.cloud.talent.v4beta1.CommuteMethodB\x03\xe0A\x02\x123\n\x11start_coordinates\x18\x02 \x01(\x0b2\x13.google.type.LatLngB\x03\xe0A\x02\x127\n\x0ftravel_duration\x18\x03 \x01(\x0b2\x19.google.protobuf.DurationB\x03\xe0A\x02\x12!\n\x19allow_imprecise_addresses\x18\x04 \x01(\x08\x12N\n\x0croad_traffic\x18\x05 \x01(\x0e26.google.cloud.talent.v4beta1.CommuteFilter.RoadTrafficH\x00\x120\n\x0edeparture_time\x18\x06 \x01(\x0b2\x16.google.type.TimeOfDayH\x00"L\n\x0bRoadTraffic\x12\x1c\n\x18ROAD_TRAFFIC_UNSPECIFIED\x10\x00\x12\x10\n\x0cTRAFFIC_FREE\x10\x01\x12\r\n\tBUSY_HOUR\x10\x02B\x10\n\x0etraffic_optionBp\n\x1fcom.google.cloud.talent.v4beta1B\x0cFiltersProtoP\x01Z7cloud.google.com/go/talent/apiv4beta1/talentpb;talentpb\xa2\x02\x03CTSb\x06proto3')
_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'google.cloud.talent.v4beta1.filters_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
    _globals['DESCRIPTOR']._loaded_options = None
    _globals['DESCRIPTOR']._serialized_options = b'\n\x1fcom.google.cloud.talent.v4beta1B\x0cFiltersProtoP\x01Z7cloud.google.com/go/talent/apiv4beta1/talentpb;talentpb\xa2\x02\x03CTS'
    _globals['_LOCATIONFILTER_TELECOMMUTEPREFERENCE'].values_by_name['TELECOMMUTE_EXCLUDED']._loaded_options = None
    _globals['_LOCATIONFILTER_TELECOMMUTEPREFERENCE'].values_by_name['TELECOMMUTE_EXCLUDED']._serialized_options = b'\x08\x01'
    _globals['_COMPENSATIONFILTER'].fields_by_name['type']._loaded_options = None
    _globals['_COMPENSATIONFILTER'].fields_by_name['type']._serialized_options = b'\xe0A\x02'
    _globals['_COMPENSATIONFILTER'].fields_by_name['units']._loaded_options = None
    _globals['_COMPENSATIONFILTER'].fields_by_name['units']._serialized_options = b'\xe0A\x02'
    _globals['_COMMUTEFILTER'].fields_by_name['commute_method']._loaded_options = None
    _globals['_COMMUTEFILTER'].fields_by_name['commute_method']._serialized_options = b'\xe0A\x02'
    _globals['_COMMUTEFILTER'].fields_by_name['start_coordinates']._loaded_options = None
    _globals['_COMMUTEFILTER'].fields_by_name['start_coordinates']._serialized_options = b'\xe0A\x02'
    _globals['_COMMUTEFILTER'].fields_by_name['travel_duration']._loaded_options = None
    _globals['_COMMUTEFILTER'].fields_by_name['travel_duration']._serialized_options = b'\xe0A\x02'
    _globals['_JOBQUERY']._serialized_start = 237
    _globals['_JOBQUERY']._serialized_end = 877
    _globals['_LOCATIONFILTER']._serialized_start = 880
    _globals['_LOCATIONFILTER']._serialized_end = 1267
    _globals['_LOCATIONFILTER_TELECOMMUTEPREFERENCE']._serialized_start = 1118
    _globals['_LOCATIONFILTER_TELECOMMUTEPREFERENCE']._serialized_end = 1267
    _globals['_COMPENSATIONFILTER']._serialized_start = 1270
    _globals['_COMPENSATIONFILTER']._serialized_end = 1728
    _globals['_COMPENSATIONFILTER_FILTERTYPE']._serialized_start = 1594
    _globals['_COMPENSATIONFILTER_FILTERTYPE']._serialized_end = 1728
    _globals['_COMMUTEFILTER']._serialized_start = 1731
    _globals['_COMMUTEFILTER']._serialized_end = 2190
    _globals['_COMMUTEFILTER_ROADTRAFFIC']._serialized_start = 2096
    _globals['_COMMUTEFILTER_ROADTRAFFIC']._serialized_end = 2172