"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_runtime_version.ValidateProtobufRuntimeVersion(_runtime_version.Domain.PUBLIC, 5, 28, 1, '', 'google/ads/admob/v1/admob_resources.proto')
_sym_db = _symbol_database.Default()
from .....google.api import field_behavior_pb2 as google_dot_api_dot_field__behavior__pb2
from .....google.api import resource_pb2 as google_dot_api_dot_resource__pb2
from .....google.type import date_pb2 as google_dot_type_dot_date__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n)google/ads/admob/v1/admob_resources.proto\x12\x13google.ads.admob.v1\x1a\x1fgoogle/api/field_behavior.proto\x1a\x19google/api/resource.proto\x1a\x16google/type/date.proto"\xac\x01\n\x10PublisherAccount\x12\x0c\n\x04name\x18\x01 \x01(\t\x12\x14\n\x0cpublisher_id\x18\x02 \x01(\t\x12\x1b\n\x13reporting_time_zone\x18\x03 \x01(\t\x12\x15\n\rcurrency_code\x18\x04 \x01(\t:@\xeaA=\n%admob.googleapis.com/PublisherAccount\x12\x14accounts/{publisher}"\xae\t\n\x11NetworkReportSpec\x122\n\ndate_range\x18\x01 \x01(\x0b2\x1e.google.ads.admob.v1.DateRange\x12D\n\ndimensions\x18\x02 \x03(\x0e20.google.ads.admob.v1.NetworkReportSpec.Dimension\x12>\n\x07metrics\x18\x03 \x03(\x0e2-.google.ads.admob.v1.NetworkReportSpec.Metric\x12Q\n\x11dimension_filters\x18\x04 \x03(\x0b26.google.ads.admob.v1.NetworkReportSpec.DimensionFilter\x12M\n\x0fsort_conditions\x18\x05 \x03(\x0b24.google.ads.admob.v1.NetworkReportSpec.SortCondition\x12H\n\x15localization_settings\x18\x06 \x01(\x0b2).google.ads.admob.v1.LocalizationSettings\x12\x17\n\x0fmax_report_rows\x18\x07 \x01(\x05\x12\x11\n\ttime_zone\x18\x08 \x01(\t\x1a\x9a\x01\n\x0fDimensionFilter\x126\n\x0bmatches_any\x18\x02 \x01(\x0b2\x1f.google.ads.admob.v1.StringListH\x00\x12C\n\tdimension\x18\x01 \x01(\x0e20.google.ads.admob.v1.NetworkReportSpec.DimensionB\n\n\x08operator\x1a\xd1\x01\n\rSortCondition\x12E\n\tdimension\x18\x01 \x01(\x0e20.google.ads.admob.v1.NetworkReportSpec.DimensionH\x00\x12?\n\x06metric\x18\x02 \x01(\x0e2-.google.ads.admob.v1.NetworkReportSpec.MetricH\x00\x12-\n\x05order\x18\x03 \x01(\x0e2\x1e.google.ads.admob.v1.SortOrderB\t\n\x07sort_on"\x8f\x01\n\tDimension\x12\x19\n\x15DIMENSION_UNSPECIFIED\x10\x00\x12\x08\n\x04DATE\x10\x01\x12\t\n\x05MONTH\x10\x02\x12\x08\n\x04WEEK\x10\x03\x12\x0b\n\x07AD_UNIT\x10\x04\x12\x07\n\x03APP\x10\x05\x12\x0b\n\x07AD_TYPE\x10\x06\x12\x0b\n\x07COUNTRY\x10\x07\x12\n\n\x06FORMAT\x10\x08\x12\x0c\n\x08PLATFORM\x10\t"\xc3\x01\n\x06Metric\x12\x16\n\x12METRIC_UNSPECIFIED\x10\x00\x12\x0f\n\x0bAD_REQUESTS\x10\x01\x12\n\n\x06CLICKS\x10\x02\x12\x16\n\x12ESTIMATED_EARNINGS\x10\x03\x12\x0f\n\x0bIMPRESSIONS\x10\x04\x12\x12\n\x0eIMPRESSION_CTR\x10\x05\x12\x12\n\x0eIMPRESSION_RPM\x10\x06\x12\x14\n\x10MATCHED_REQUESTS\x10\x07\x12\x0e\n\nMATCH_RATE\x10\x08\x12\r\n\tSHOW_RATE\x10\t"\xdd\t\n\x13MediationReportSpec\x122\n\ndate_range\x18\x01 \x01(\x0b2\x1e.google.ads.admob.v1.DateRange\x12F\n\ndimensions\x18\x02 \x03(\x0e22.google.ads.admob.v1.MediationReportSpec.Dimension\x12@\n\x07metrics\x18\x03 \x03(\x0e2/.google.ads.admob.v1.MediationReportSpec.Metric\x12S\n\x11dimension_filters\x18\x04 \x03(\x0b28.google.ads.admob.v1.MediationReportSpec.DimensionFilter\x12O\n\x0fsort_conditions\x18\x05 \x03(\x0b26.google.ads.admob.v1.MediationReportSpec.SortCondition\x12H\n\x15localization_settings\x18\x06 \x01(\x0b2).google.ads.admob.v1.LocalizationSettings\x12\x17\n\x0fmax_report_rows\x18\x07 \x01(\x05\x12\x11\n\ttime_zone\x18\x08 \x01(\t\x1a\x9c\x01\n\x0fDimensionFilter\x126\n\x0bmatches_any\x18\x02 \x01(\x0b2\x1f.google.ads.admob.v1.StringListH\x00\x12E\n\tdimension\x18\x01 \x01(\x0e22.google.ads.admob.v1.MediationReportSpec.DimensionB\n\n\x08operator\x1a\xd5\x01\n\rSortCondition\x12G\n\tdimension\x18\x01 \x01(\x0e22.google.ads.admob.v1.MediationReportSpec.DimensionH\x00\x12A\n\x06metric\x18\x02 \x01(\x0e2/.google.ads.admob.v1.MediationReportSpec.MetricH\x00\x12-\n\x05order\x18\x03 \x01(\x0e2\x1e.google.ads.admob.v1.SortOrderB\t\n\x07sort_on"\xbe\x01\n\tDimension\x12\x19\n\x15DIMENSION_UNSPECIFIED\x10\x00\x12\x08\n\x04DATE\x10\x01\x12\t\n\x05MONTH\x10\x02\x12\x08\n\x04WEEK\x10\x03\x12\r\n\tAD_SOURCE\x10\x04\x12\x16\n\x12AD_SOURCE_INSTANCE\x10\x05\x12\x0b\n\x07AD_UNIT\x10\x06\x12\x07\n\x03APP\x10\x07\x12\x13\n\x0fMEDIATION_GROUP\x10\x0b\x12\x0b\n\x07COUNTRY\x10\x08\x12\n\n\x06FORMAT\x10\t\x12\x0c\n\x08PLATFORM\x10\n"\xb3\x01\n\x06Metric\x12\x16\n\x12METRIC_UNSPECIFIED\x10\x00\x12\x0f\n\x0bAD_REQUESTS\x10\x01\x12\n\n\x06CLICKS\x10\x02\x12\x16\n\x12ESTIMATED_EARNINGS\x10\x03\x12\x0f\n\x0bIMPRESSIONS\x10\x04\x12\x12\n\x0eIMPRESSION_CTR\x10\x05\x12\x14\n\x10MATCHED_REQUESTS\x10\x06\x12\x0e\n\nMATCH_RATE\x10\x07\x12\x11\n\rOBSERVED_ECPM\x10\x08"\x84\x04\n\tReportRow\x12M\n\x10dimension_values\x18\x01 \x03(\x0b23.google.ads.admob.v1.ReportRow.DimensionValuesEntry\x12G\n\rmetric_values\x18\x02 \x03(\x0b20.google.ads.admob.v1.ReportRow.MetricValuesEntry\x1a6\n\x0eDimensionValue\x12\r\n\x05value\x18\x01 \x01(\t\x12\x15\n\rdisplay_label\x18\x02 \x01(\t\x1a_\n\x0bMetricValue\x12\x17\n\rinteger_value\x18\x01 \x01(\x03H\x00\x12\x16\n\x0cdouble_value\x18\x02 \x01(\x01H\x00\x12\x16\n\x0cmicros_value\x18\x03 \x01(\x03H\x00B\x07\n\x05value\x1ae\n\x14DimensionValuesEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12<\n\x05value\x18\x02 \x01(\x0b2-.google.ads.admob.v1.ReportRow.DimensionValue:\x028\x01\x1a_\n\x11MetricValuesEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x129\n\x05value\x18\x02 \x01(\x0b2*.google.ads.admob.v1.ReportRow.MetricValue:\x028\x01"\xea\x01\n\rReportWarning\x125\n\x04type\x18\x01 \x01(\x0e2\'.google.ads.admob.v1.ReportWarning.Type\x12\x13\n\x0bdescription\x18\x02 \x01(\t"\x8c\x01\n\x04Type\x12\x14\n\x10TYPE_UNSPECIFIED\x10\x00\x12\'\n#DATA_BEFORE_ACCOUNT_TIMEZONE_CHANGE\x10\x01\x12\x10\n\x0cDATA_DELAYED\x10\x02\x12\t\n\x05OTHER\x10\x03\x12(\n$REPORT_CURRENCY_NOT_ACCOUNT_CURRENCY\x10\x04"\xa9\x01\n\x0cReportHeader\x122\n\ndate_range\x18\x01 \x01(\x0b2\x1e.google.ads.admob.v1.DateRange\x12H\n\x15localization_settings\x18\x02 \x01(\x0b2).google.ads.admob.v1.LocalizationSettings\x12\x1b\n\x13reporting_time_zone\x18\x03 \x01(\t"`\n\x0cReportFooter\x124\n\x08warnings\x18\x01 \x03(\x0b2".google.ads.admob.v1.ReportWarning\x12\x1a\n\x12matching_row_count\x18\x02 \x01(\x03"W\n\tDateRange\x12%\n\nstart_date\x18\x01 \x01(\x0b2\x11.google.type.Date\x12#\n\x08end_date\x18\x02 \x01(\x0b2\x11.google.type.Date"D\n\x14LocalizationSettings\x12\x15\n\rcurrency_code\x18\x01 \x01(\t\x12\x15\n\rlanguage_code\x18\x02 \x01(\t"\x1c\n\nStringList\x12\x0e\n\x06values\x18\x01 \x03(\t*F\n\tSortOrder\x12\x1a\n\x16SORT_ORDER_UNSPECIFIED\x10\x00\x12\r\n\tASCENDING\x10\x01\x12\x0e\n\nDESCENDING\x10\x02Bh\n\x17com.google.ads.admob.v1B\x13AdMobResourcesProtoZ8google.golang.org/genproto/googleapis/ads/admob/v1;admobb\x06proto3')
_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'google.ads.admob.v1.admob_resources_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
    _globals['DESCRIPTOR']._loaded_options = None
    _globals['DESCRIPTOR']._serialized_options = b'\n\x17com.google.ads.admob.v1B\x13AdMobResourcesProtoZ8google.golang.org/genproto/googleapis/ads/admob/v1;admob'
    _globals['_PUBLISHERACCOUNT']._loaded_options = None
    _globals['_PUBLISHERACCOUNT']._serialized_options = b'\xeaA=\n%admob.googleapis.com/PublisherAccount\x12\x14accounts/{publisher}'
    _globals['_REPORTROW_DIMENSIONVALUESENTRY']._loaded_options = None
    _globals['_REPORTROW_DIMENSIONVALUESENTRY']._serialized_options = b'8\x01'
    _globals['_REPORTROW_METRICVALUESENTRY']._loaded_options = None
    _globals['_REPORTROW_METRICVALUESENTRY']._serialized_options = b'8\x01'
    _globals['_SORTORDER']._serialized_start = 3989
    _globals['_SORTORDER']._serialized_end = 4059
    _globals['_PUBLISHERACCOUNT']._serialized_start = 151
    _globals['_PUBLISHERACCOUNT']._serialized_end = 323
    _globals['_NETWORKREPORTSPEC']._serialized_start = 326
    _globals['_NETWORKREPORTSPEC']._serialized_end = 1524
    _globals['_NETWORKREPORTSPEC_DIMENSIONFILTER']._serialized_start = 814
    _globals['_NETWORKREPORTSPEC_DIMENSIONFILTER']._serialized_end = 968
    _globals['_NETWORKREPORTSPEC_SORTCONDITION']._serialized_start = 971
    _globals['_NETWORKREPORTSPEC_SORTCONDITION']._serialized_end = 1180
    _globals['_NETWORKREPORTSPEC_DIMENSION']._serialized_start = 1183
    _globals['_NETWORKREPORTSPEC_DIMENSION']._serialized_end = 1326
    _globals['_NETWORKREPORTSPEC_METRIC']._serialized_start = 1329
    _globals['_NETWORKREPORTSPEC_METRIC']._serialized_end = 1524
    _globals['_MEDIATIONREPORTSPEC']._serialized_start = 1527
    _globals['_MEDIATIONREPORTSPEC']._serialized_end = 2772
    _globals['_MEDIATIONREPORTSPEC_DIMENSIONFILTER']._serialized_start = 2025
    _globals['_MEDIATIONREPORTSPEC_DIMENSIONFILTER']._serialized_end = 2181
    _globals['_MEDIATIONREPORTSPEC_SORTCONDITION']._serialized_start = 2184
    _globals['_MEDIATIONREPORTSPEC_SORTCONDITION']._serialized_end = 2397
    _globals['_MEDIATIONREPORTSPEC_DIMENSION']._serialized_start = 2400
    _globals['_MEDIATIONREPORTSPEC_DIMENSION']._serialized_end = 2590
    _globals['_MEDIATIONREPORTSPEC_METRIC']._serialized_start = 2593
    _globals['_MEDIATIONREPORTSPEC_METRIC']._serialized_end = 2772
    _globals['_REPORTROW']._serialized_start = 2775
    _globals['_REPORTROW']._serialized_end = 3291
    _globals['_REPORTROW_DIMENSIONVALUE']._serialized_start = 2940
    _globals['_REPORTROW_DIMENSIONVALUE']._serialized_end = 2994
    _globals['_REPORTROW_METRICVALUE']._serialized_start = 2996
    _globals['_REPORTROW_METRICVALUE']._serialized_end = 3091
    _globals['_REPORTROW_DIMENSIONVALUESENTRY']._serialized_start = 3093
    _globals['_REPORTROW_DIMENSIONVALUESENTRY']._serialized_end = 3194
    _globals['_REPORTROW_METRICVALUESENTRY']._serialized_start = 3196
    _globals['_REPORTROW_METRICVALUESENTRY']._serialized_end = 3291
    _globals['_REPORTWARNING']._serialized_start = 3294
    _globals['_REPORTWARNING']._serialized_end = 3528
    _globals['_REPORTWARNING_TYPE']._serialized_start = 3388
    _globals['_REPORTWARNING_TYPE']._serialized_end = 3528
    _globals['_REPORTHEADER']._serialized_start = 3531
    _globals['_REPORTHEADER']._serialized_end = 3700
    _globals['_REPORTFOOTER']._serialized_start = 3702
    _globals['_REPORTFOOTER']._serialized_end = 3798
    _globals['_DATERANGE']._serialized_start = 3800
    _globals['_DATERANGE']._serialized_end = 3887
    _globals['_LOCALIZATIONSETTINGS']._serialized_start = 3889
    _globals['_LOCALIZATIONSETTINGS']._serialized_end = 3957
    _globals['_STRINGLIST']._serialized_start = 3959
    _globals['_STRINGLIST']._serialized_end = 3987