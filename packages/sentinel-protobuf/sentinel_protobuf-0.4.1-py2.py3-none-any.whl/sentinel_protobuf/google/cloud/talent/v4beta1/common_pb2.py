"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_runtime_version.ValidateProtobufRuntimeVersion(_runtime_version.Domain.PUBLIC, 5, 28, 1, '', 'google/cloud/talent/v4beta1/common.proto')
_sym_db = _symbol_database.Default()
from .....google.api import field_behavior_pb2 as google_dot_api_dot_field__behavior__pb2
from google.protobuf import timestamp_pb2 as google_dot_protobuf_dot_timestamp__pb2
from google.protobuf import wrappers_pb2 as google_dot_protobuf_dot_wrappers__pb2
from .....google.type import latlng_pb2 as google_dot_type_dot_latlng__pb2
from .....google.type import money_pb2 as google_dot_type_dot_money__pb2
from .....google.type import postal_address_pb2 as google_dot_type_dot_postal__address__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n(google/cloud/talent/v4beta1/common.proto\x12\x1bgoogle.cloud.talent.v4beta1\x1a\x1fgoogle/api/field_behavior.proto\x1a\x1fgoogle/protobuf/timestamp.proto\x1a\x1egoogle/protobuf/wrappers.proto\x1a\x18google/type/latlng.proto\x1a\x17google/type/money.proto\x1a google/type/postal_address.proto"n\n\x0eTimestampRange\x12.\n\nstart_time\x18\x01 \x01(\x0b2\x1a.google.protobuf.Timestamp\x12,\n\x08end_time\x18\x02 \x01(\x0b2\x1a.google.protobuf.Timestamp"\xb7\x03\n\x08Location\x12I\n\rlocation_type\x18\x01 \x01(\x0e22.google.cloud.talent.v4beta1.Location.LocationType\x122\n\x0epostal_address\x18\x02 \x01(\x0b2\x1a.google.type.PostalAddress\x12$\n\x07lat_lng\x18\x03 \x01(\x0b2\x13.google.type.LatLng\x12\x14\n\x0cradius_miles\x18\x04 \x01(\x01"\xef\x01\n\x0cLocationType\x12\x1d\n\x19LOCATION_TYPE_UNSPECIFIED\x10\x00\x12\x0b\n\x07COUNTRY\x10\x01\x12\x17\n\x13ADMINISTRATIVE_AREA\x10\x02\x12\x1b\n\x17SUB_ADMINISTRATIVE_AREA\x10\x03\x12\x0c\n\x08LOCALITY\x10\x04\x12\x0f\n\x0bPOSTAL_CODE\x10\x05\x12\x10\n\x0cSUB_LOCALITY\x10\x06\x12\x12\n\x0eSUB_LOCALITY_1\x10\x07\x12\x12\n\x0eSUB_LOCALITY_2\x10\x08\x12\x10\n\x0cNEIGHBORHOOD\x10\t\x12\x12\n\x0eSTREET_ADDRESS\x10\n"\x9f\x01\n\x0fRequestMetadata\x12\x0e\n\x06domain\x18\x01 \x01(\t\x12\x12\n\nsession_id\x18\x02 \x01(\t\x12\x0f\n\x07user_id\x18\x03 \x01(\t\x12\x19\n\x11allow_missing_ids\x18\x04 \x01(\x08\x12<\n\x0bdevice_info\x18\x05 \x01(\x0b2\'.google.cloud.talent.v4beta1.DeviceInfo"&\n\x10ResponseMetadata\x12\x12\n\nrequest_id\x18\x01 \x01(\t"\xcf\x01\n\nDeviceInfo\x12G\n\x0bdevice_type\x18\x01 \x01(\x0e22.google.cloud.talent.v4beta1.DeviceInfo.DeviceType\x12\n\n\x02id\x18\x02 \x01(\t"l\n\nDeviceType\x12\x1b\n\x17DEVICE_TYPE_UNSPECIFIED\x10\x00\x12\x07\n\x03WEB\x10\x01\x12\x0e\n\nMOBILE_WEB\x10\x02\x12\x0b\n\x07ANDROID\x10\x03\x12\x07\n\x03IOS\x10\x04\x12\x07\n\x03BOT\x10\x05\x12\t\n\x05OTHER\x10\x06"m\n\x0fCustomAttribute\x12\x15\n\rstring_values\x18\x01 \x03(\t\x12\x13\n\x0blong_values\x18\x02 \x03(\x03\x12\x12\n\nfilterable\x18\x03 \x01(\x08\x12\x1a\n\x12keyword_searchable\x18\x04 \x01(\x08"W\n\x12SpellingCorrection\x12\x11\n\tcorrected\x18\x01 \x01(\x08\x12\x16\n\x0ecorrected_text\x18\x02 \x01(\t\x12\x16\n\x0ecorrected_html\x18\x03 \x01(\t"\xa6\t\n\x10CompensationInfo\x12P\n\x07entries\x18\x01 \x03(\x0b2?.google.cloud.talent.v4beta1.CompensationInfo.CompensationEntry\x12p\n"annualized_base_compensation_range\x18\x02 \x01(\x0b2?.google.cloud.talent.v4beta1.CompensationInfo.CompensationRangeB\x03\xe0A\x03\x12q\n#annualized_total_compensation_range\x18\x03 \x01(\x0b2?.google.cloud.talent.v4beta1.CompensationInfo.CompensationRangeB\x03\xe0A\x03\x1a\x92\x03\n\x11CompensationEntry\x12L\n\x04type\x18\x01 \x01(\x0e2>.google.cloud.talent.v4beta1.CompensationInfo.CompensationType\x12L\n\x04unit\x18\x02 \x01(\x0e2>.google.cloud.talent.v4beta1.CompensationInfo.CompensationUnit\x12$\n\x06amount\x18\x03 \x01(\x0b2\x12.google.type.MoneyH\x00\x12P\n\x05range\x18\x04 \x01(\x0b2?.google.cloud.talent.v4beta1.CompensationInfo.CompensationRangeH\x00\x12\x13\n\x0bdescription\x18\x05 \x01(\t\x12=\n\x17expected_units_per_year\x18\x06 \x01(\x0b2\x1c.google.protobuf.DoubleValueB\x15\n\x13compensation_amount\x1ao\n\x11CompensationRange\x12,\n\x10max_compensation\x18\x02 \x01(\x0b2\x12.google.type.Money\x12,\n\x10min_compensation\x18\x01 \x01(\x0b2\x12.google.type.Money"\xb5\x01\n\x10CompensationType\x12!\n\x1dCOMPENSATION_TYPE_UNSPECIFIED\x10\x00\x12\x08\n\x04BASE\x10\x01\x12\t\n\x05BONUS\x10\x02\x12\x11\n\rSIGNING_BONUS\x10\x03\x12\n\n\x06EQUITY\x10\x04\x12\x12\n\x0ePROFIT_SHARING\x10\x05\x12\x0f\n\x0bCOMMISSIONS\x10\x06\x12\x08\n\x04TIPS\x10\x07\x12\x1b\n\x17OTHER_COMPENSATION_TYPE\x10\x08"\x9c\x01\n\x10CompensationUnit\x12!\n\x1dCOMPENSATION_UNIT_UNSPECIFIED\x10\x00\x12\n\n\x06HOURLY\x10\x01\x12\t\n\x05DAILY\x10\x02\x12\n\n\x06WEEKLY\x10\x03\x12\x0b\n\x07MONTHLY\x10\x04\x12\n\n\x06YEARLY\x10\x05\x12\x0c\n\x08ONE_TIME\x10\x06\x12\x1b\n\x17OTHER_COMPENSATION_UNIT\x10\x07"\xcc\x03\n\x16BatchOperationMetadata\x12H\n\x05state\x18\x01 \x01(\x0e29.google.cloud.talent.v4beta1.BatchOperationMetadata.State\x12\x19\n\x11state_description\x18\x02 \x01(\t\x12\x15\n\rsuccess_count\x18\x03 \x01(\x05\x12\x15\n\rfailure_count\x18\x04 \x01(\x05\x12\x13\n\x0btotal_count\x18\x05 \x01(\x05\x12/\n\x0bcreate_time\x18\x06 \x01(\x0b2\x1a.google.protobuf.Timestamp\x12/\n\x0bupdate_time\x18\x07 \x01(\x0b2\x1a.google.protobuf.Timestamp\x12,\n\x08end_time\x18\x08 \x01(\x0b2\x1a.google.protobuf.Timestamp"z\n\x05State\x12\x15\n\x11STATE_UNSPECIFIED\x10\x00\x12\x10\n\x0cINITIALIZING\x10\x01\x12\x0e\n\nPROCESSING\x10\x02\x12\r\n\tSUCCEEDED\x10\x03\x12\n\n\x06FAILED\x10\x04\x12\x0e\n\nCANCELLING\x10\x05\x12\r\n\tCANCELLED\x10\x06*y\n\x0bCompanySize\x12\x1c\n\x18COMPANY_SIZE_UNSPECIFIED\x10\x00\x12\x08\n\x04MINI\x10\x01\x12\t\n\x05SMALL\x10\x02\x12\x0b\n\x07SMEDIUM\x10\x03\x12\n\n\x06MEDIUM\x10\x04\x12\x07\n\x03BIG\x10\x05\x12\n\n\x06BIGGER\x10\x06\x12\t\n\x05GIANT\x10\x07*\xe2\x01\n\nJobBenefit\x12\x1b\n\x17JOB_BENEFIT_UNSPECIFIED\x10\x00\x12\x0e\n\nCHILD_CARE\x10\x01\x12\n\n\x06DENTAL\x10\x02\x12\x14\n\x10DOMESTIC_PARTNER\x10\x03\x12\x12\n\x0eFLEXIBLE_HOURS\x10\x04\x12\x0b\n\x07MEDICAL\x10\x05\x12\x12\n\x0eLIFE_INSURANCE\x10\x06\x12\x12\n\x0ePARENTAL_LEAVE\x10\x07\x12\x13\n\x0fRETIREMENT_PLAN\x10\x08\x12\r\n\tSICK_DAYS\x10\t\x12\x0c\n\x08VACATION\x10\n\x12\n\n\x06VISION\x10\x0b*\x8e\x02\n\nDegreeType\x12\x1b\n\x17DEGREE_TYPE_UNSPECIFIED\x10\x00\x12\x15\n\x11PRIMARY_EDUCATION\x10\x01\x12\x1d\n\x19LOWER_SECONDARY_EDUCATION\x10\x02\x12\x1d\n\x19UPPER_SECONDARY_EDUCATION\x10\x03\x12\x1c\n\x18ADULT_REMEDIAL_EDUCATION\x10\x04\x12\x1c\n\x18ASSOCIATES_OR_EQUIVALENT\x10\x05\x12\x1b\n\x17BACHELORS_OR_EQUIVALENT\x10\x06\x12\x19\n\x15MASTERS_OR_EQUIVALENT\x10\x07\x12\x1a\n\x16DOCTORAL_OR_EQUIVALENT\x10\x08*\xdc\x01\n\x0eEmploymentType\x12\x1f\n\x1bEMPLOYMENT_TYPE_UNSPECIFIED\x10\x00\x12\r\n\tFULL_TIME\x10\x01\x12\r\n\tPART_TIME\x10\x02\x12\x0e\n\nCONTRACTOR\x10\x03\x12\x14\n\x10CONTRACT_TO_HIRE\x10\x04\x12\r\n\tTEMPORARY\x10\x05\x12\n\n\x06INTERN\x10\x06\x12\r\n\tVOLUNTEER\x10\x07\x12\x0c\n\x08PER_DIEM\x10\x08\x12\x12\n\x0eFLY_IN_FLY_OUT\x10\t\x12\x19\n\x15OTHER_EMPLOYMENT_TYPE\x10\n*q\n\x08JobLevel\x12\x19\n\x15JOB_LEVEL_UNSPECIFIED\x10\x00\x12\x0f\n\x0bENTRY_LEVEL\x10\x01\x12\x0f\n\x0bEXPERIENCED\x10\x02\x12\x0b\n\x07MANAGER\x10\x03\x12\x0c\n\x08DIRECTOR\x10\x04\x12\r\n\tEXECUTIVE\x10\x05*\xba\x06\n\x0bJobCategory\x12\x1c\n\x18JOB_CATEGORY_UNSPECIFIED\x10\x00\x12\x1a\n\x16ACCOUNTING_AND_FINANCE\x10\x01\x12\x1d\n\x19ADMINISTRATIVE_AND_OFFICE\x10\x02\x12\x1d\n\x19ADVERTISING_AND_MARKETING\x10\x03\x12\x0f\n\x0bANIMAL_CARE\x10\x04\x12\x1a\n\x16ART_FASHION_AND_DESIGN\x10\x05\x12\x17\n\x13BUSINESS_OPERATIONS\x10\x06\x12\x1b\n\x17CLEANING_AND_FACILITIES\x10\x07\x12\x13\n\x0fCOMPUTER_AND_IT\x10\x08\x12\x10\n\x0cCONSTRUCTION\x10\t\x12\x14\n\x10CUSTOMER_SERVICE\x10\n\x12\r\n\tEDUCATION\x10\x0b\x12\x1c\n\x18ENTERTAINMENT_AND_TRAVEL\x10\x0c\x12\x18\n\x14FARMING_AND_OUTDOORS\x10\r\x12\x0e\n\nHEALTHCARE\x10\x0e\x12\x13\n\x0fHUMAN_RESOURCES\x10\x0f\x12\'\n#INSTALLATION_MAINTENANCE_AND_REPAIR\x10\x10\x12\t\n\x05LEGAL\x10\x11\x12\x0e\n\nMANAGEMENT\x10\x12\x12\x1f\n\x1bMANUFACTURING_AND_WAREHOUSE\x10\x13\x12$\n MEDIA_COMMUNICATIONS_AND_WRITING\x10\x14\x12\x16\n\x12OIL_GAS_AND_MINING\x10\x15\x12\x1e\n\x1aPERSONAL_CARE_AND_SERVICES\x10\x16\x12\x17\n\x13PROTECTIVE_SERVICES\x10\x17\x12\x0f\n\x0bREAL_ESTATE\x10\x18\x12\x1e\n\x1aRESTAURANT_AND_HOSPITALITY\x10\x19\x12\x14\n\x10SALES_AND_RETAIL\x10\x1a\x12\x1b\n\x17SCIENCE_AND_ENGINEERING\x10\x1b\x12"\n\x1eSOCIAL_SERVICES_AND_NON_PROFIT\x10\x1c\x12!\n\x1dSPORTS_FITNESS_AND_RECREATION\x10\x1d\x12 \n\x1cTRANSPORTATION_AND_LOGISTICS\x10\x1e*e\n\rPostingRegion\x12\x1e\n\x1aPOSTING_REGION_UNSPECIFIED\x10\x00\x12\x17\n\x13ADMINISTRATIVE_AREA\x10\x01\x12\n\n\x06NATION\x10\x02\x12\x0f\n\x0bTELECOMMUTE\x10\x03*n\n\nVisibility\x12\x1a\n\x16VISIBILITY_UNSPECIFIED\x10\x00\x12\x10\n\x0cACCOUNT_ONLY\x10\x01\x12\x16\n\x12SHARED_WITH_GOOGLE\x10\x02\x12\x16\n\x12SHARED_WITH_PUBLIC\x10\x03\x1a\x02\x18\x01*q\n\x10HtmlSanitization\x12!\n\x1dHTML_SANITIZATION_UNSPECIFIED\x10\x00\x12\x1e\n\x1aHTML_SANITIZATION_DISABLED\x10\x01\x12\x1a\n\x16SIMPLE_FORMATTING_ONLY\x10\x02*c\n\rCommuteMethod\x12\x1e\n\x1aCOMMUTE_METHOD_UNSPECIFIED\x10\x00\x12\x0b\n\x07DRIVING\x10\x01\x12\x0b\n\x07TRANSIT\x10\x02\x12\x0b\n\x07WALKING\x10\x03\x12\x0b\n\x07CYCLING\x10\x04Bo\n\x1fcom.google.cloud.talent.v4beta1B\x0bCommonProtoP\x01Z7cloud.google.com/go/talent/apiv4beta1/talentpb;talentpb\xa2\x02\x03CTSb\x06proto3')
_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'google.cloud.talent.v4beta1.common_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
    _globals['DESCRIPTOR']._loaded_options = None
    _globals['DESCRIPTOR']._serialized_options = b'\n\x1fcom.google.cloud.talent.v4beta1B\x0bCommonProtoP\x01Z7cloud.google.com/go/talent/apiv4beta1/talentpb;talentpb\xa2\x02\x03CTS'
    _globals['_VISIBILITY']._loaded_options = None
    _globals['_VISIBILITY']._serialized_options = b'\x18\x01'
    _globals['_COMPENSATIONINFO'].fields_by_name['annualized_base_compensation_range']._loaded_options = None
    _globals['_COMPENSATIONINFO'].fields_by_name['annualized_base_compensation_range']._serialized_options = b'\xe0A\x03'
    _globals['_COMPENSATIONINFO'].fields_by_name['annualized_total_compensation_range']._loaded_options = None
    _globals['_COMPENSATIONINFO'].fields_by_name['annualized_total_compensation_range']._serialized_options = b'\xe0A\x03'
    _globals['_COMPANYSIZE']._serialized_start = 3078
    _globals['_COMPANYSIZE']._serialized_end = 3199
    _globals['_JOBBENEFIT']._serialized_start = 3202
    _globals['_JOBBENEFIT']._serialized_end = 3428
    _globals['_DEGREETYPE']._serialized_start = 3431
    _globals['_DEGREETYPE']._serialized_end = 3701
    _globals['_EMPLOYMENTTYPE']._serialized_start = 3704
    _globals['_EMPLOYMENTTYPE']._serialized_end = 3924
    _globals['_JOBLEVEL']._serialized_start = 3926
    _globals['_JOBLEVEL']._serialized_end = 4039
    _globals['_JOBCATEGORY']._serialized_start = 4042
    _globals['_JOBCATEGORY']._serialized_end = 4868
    _globals['_POSTINGREGION']._serialized_start = 4870
    _globals['_POSTINGREGION']._serialized_end = 4971
    _globals['_VISIBILITY']._serialized_start = 4973
    _globals['_VISIBILITY']._serialized_end = 5083
    _globals['_HTMLSANITIZATION']._serialized_start = 5085
    _globals['_HTMLSANITIZATION']._serialized_end = 5198
    _globals['_COMMUTEMETHOD']._serialized_start = 5200
    _globals['_COMMUTEMETHOD']._serialized_end = 5299
    _globals['_TIMESTAMPRANGE']._serialized_start = 256
    _globals['_TIMESTAMPRANGE']._serialized_end = 366
    _globals['_LOCATION']._serialized_start = 369
    _globals['_LOCATION']._serialized_end = 808
    _globals['_LOCATION_LOCATIONTYPE']._serialized_start = 569
    _globals['_LOCATION_LOCATIONTYPE']._serialized_end = 808
    _globals['_REQUESTMETADATA']._serialized_start = 811
    _globals['_REQUESTMETADATA']._serialized_end = 970
    _globals['_RESPONSEMETADATA']._serialized_start = 972
    _globals['_RESPONSEMETADATA']._serialized_end = 1010
    _globals['_DEVICEINFO']._serialized_start = 1013
    _globals['_DEVICEINFO']._serialized_end = 1220
    _globals['_DEVICEINFO_DEVICETYPE']._serialized_start = 1112
    _globals['_DEVICEINFO_DEVICETYPE']._serialized_end = 1220
    _globals['_CUSTOMATTRIBUTE']._serialized_start = 1222
    _globals['_CUSTOMATTRIBUTE']._serialized_end = 1331
    _globals['_SPELLINGCORRECTION']._serialized_start = 1333
    _globals['_SPELLINGCORRECTION']._serialized_end = 1420
    _globals['_COMPENSATIONINFO']._serialized_start = 1423
    _globals['_COMPENSATIONINFO']._serialized_end = 2613
    _globals['_COMPENSATIONINFO_COMPENSATIONENTRY']._serialized_start = 1755
    _globals['_COMPENSATIONINFO_COMPENSATIONENTRY']._serialized_end = 2157
    _globals['_COMPENSATIONINFO_COMPENSATIONRANGE']._serialized_start = 2159
    _globals['_COMPENSATIONINFO_COMPENSATIONRANGE']._serialized_end = 2270
    _globals['_COMPENSATIONINFO_COMPENSATIONTYPE']._serialized_start = 2273
    _globals['_COMPENSATIONINFO_COMPENSATIONTYPE']._serialized_end = 2454
    _globals['_COMPENSATIONINFO_COMPENSATIONUNIT']._serialized_start = 2457
    _globals['_COMPENSATIONINFO_COMPENSATIONUNIT']._serialized_end = 2613
    _globals['_BATCHOPERATIONMETADATA']._serialized_start = 2616
    _globals['_BATCHOPERATIONMETADATA']._serialized_end = 3076
    _globals['_BATCHOPERATIONMETADATA_STATE']._serialized_start = 2954
    _globals['_BATCHOPERATIONMETADATA_STATE']._serialized_end = 3076