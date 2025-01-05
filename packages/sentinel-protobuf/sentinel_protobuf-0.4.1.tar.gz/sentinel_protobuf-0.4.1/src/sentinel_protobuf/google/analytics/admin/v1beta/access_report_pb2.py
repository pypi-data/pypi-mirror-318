"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_runtime_version.ValidateProtobufRuntimeVersion(_runtime_version.Domain.PUBLIC, 5, 28, 1, '', 'google/analytics/admin/v1beta/access_report.proto')
_sym_db = _symbol_database.Default()
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n1google/analytics/admin/v1beta/access_report.proto\x12\x1dgoogle.analytics.admin.v1beta")\n\x0fAccessDimension\x12\x16\n\x0edimension_name\x18\x01 \x01(\t"#\n\x0cAccessMetric\x12\x13\n\x0bmetric_name\x18\x01 \x01(\t"7\n\x0fAccessDateRange\x12\x12\n\nstart_date\x18\x01 \x01(\t\x12\x10\n\x08end_date\x18\x02 \x01(\t"\xe0\x02\n\x16AccessFilterExpression\x12N\n\tand_group\x18\x01 \x01(\x0b29.google.analytics.admin.v1beta.AccessFilterExpressionListH\x00\x12M\n\x08or_group\x18\x02 \x01(\x0b29.google.analytics.admin.v1beta.AccessFilterExpressionListH\x00\x12O\n\x0enot_expression\x18\x03 \x01(\x0b25.google.analytics.admin.v1beta.AccessFilterExpressionH\x00\x12D\n\raccess_filter\x18\x04 \x01(\x0b2+.google.analytics.admin.v1beta.AccessFilterH\x00B\x10\n\x0eone_expression"h\n\x1aAccessFilterExpressionList\x12J\n\x0bexpressions\x18\x01 \x03(\x0b25.google.analytics.admin.v1beta.AccessFilterExpression"\xe5\x02\n\x0cAccessFilter\x12J\n\rstring_filter\x18\x02 \x01(\x0b21.google.analytics.admin.v1beta.AccessStringFilterH\x00\x12K\n\x0ein_list_filter\x18\x03 \x01(\x0b21.google.analytics.admin.v1beta.AccessInListFilterH\x00\x12L\n\x0enumeric_filter\x18\x04 \x01(\x0b22.google.analytics.admin.v1beta.AccessNumericFilterH\x00\x12L\n\x0ebetween_filter\x18\x05 \x01(\x0b22.google.analytics.admin.v1beta.AccessBetweenFilterH\x00\x12\x12\n\nfield_name\x18\x01 \x01(\tB\x0c\n\none_filter"\x94\x02\n\x12AccessStringFilter\x12O\n\nmatch_type\x18\x01 \x01(\x0e2;.google.analytics.admin.v1beta.AccessStringFilter.MatchType\x12\r\n\x05value\x18\x02 \x01(\t\x12\x16\n\x0ecase_sensitive\x18\x03 \x01(\x08"\x85\x01\n\tMatchType\x12\x1a\n\x16MATCH_TYPE_UNSPECIFIED\x10\x00\x12\t\n\x05EXACT\x10\x01\x12\x0f\n\x0bBEGINS_WITH\x10\x02\x12\r\n\tENDS_WITH\x10\x03\x12\x0c\n\x08CONTAINS\x10\x04\x12\x0f\n\x0bFULL_REGEXP\x10\x05\x12\x12\n\x0ePARTIAL_REGEXP\x10\x06"<\n\x12AccessInListFilter\x12\x0e\n\x06values\x18\x01 \x03(\t\x12\x16\n\x0ecase_sensitive\x18\x02 \x01(\x08"\xaa\x02\n\x13AccessNumericFilter\x12O\n\toperation\x18\x01 \x01(\x0e2<.google.analytics.admin.v1beta.AccessNumericFilter.Operation\x12:\n\x05value\x18\x02 \x01(\x0b2+.google.analytics.admin.v1beta.NumericValue"\x85\x01\n\tOperation\x12\x19\n\x15OPERATION_UNSPECIFIED\x10\x00\x12\t\n\x05EQUAL\x10\x01\x12\r\n\tLESS_THAN\x10\x02\x12\x16\n\x12LESS_THAN_OR_EQUAL\x10\x03\x12\x10\n\x0cGREATER_THAN\x10\x04\x12\x19\n\x15GREATER_THAN_OR_EQUAL\x10\x05"\x95\x01\n\x13AccessBetweenFilter\x12?\n\nfrom_value\x18\x01 \x01(\x0b2+.google.analytics.admin.v1beta.NumericValue\x12=\n\x08to_value\x18\x02 \x01(\x0b2+.google.analytics.admin.v1beta.NumericValue"J\n\x0cNumericValue\x12\x15\n\x0bint64_value\x18\x01 \x01(\x03H\x00\x12\x16\n\x0cdouble_value\x18\x02 \x01(\x01H\x00B\x0b\n\tone_value"\xea\x03\n\rAccessOrderBy\x12L\n\x06metric\x18\x01 \x01(\x0b2:.google.analytics.admin.v1beta.AccessOrderBy.MetricOrderByH\x00\x12R\n\tdimension\x18\x02 \x01(\x0b2=.google.analytics.admin.v1beta.AccessOrderBy.DimensionOrderByH\x00\x12\x0c\n\x04desc\x18\x03 \x01(\x08\x1a$\n\rMetricOrderBy\x12\x13\n\x0bmetric_name\x18\x01 \x01(\t\x1a\xf2\x01\n\x10DimensionOrderBy\x12\x16\n\x0edimension_name\x18\x01 \x01(\t\x12[\n\norder_type\x18\x02 \x01(\x0e2G.google.analytics.admin.v1beta.AccessOrderBy.DimensionOrderBy.OrderType"i\n\tOrderType\x12\x1a\n\x16ORDER_TYPE_UNSPECIFIED\x10\x00\x12\x10\n\x0cALPHANUMERIC\x10\x01\x12!\n\x1dCASE_INSENSITIVE_ALPHANUMERIC\x10\x02\x12\x0b\n\x07NUMERIC\x10\x03B\x0e\n\x0cone_order_by"/\n\x15AccessDimensionHeader\x12\x16\n\x0edimension_name\x18\x01 \x01(\t")\n\x12AccessMetricHeader\x12\x13\n\x0bmetric_name\x18\x01 \x01(\t"\xa3\x01\n\tAccessRow\x12M\n\x10dimension_values\x18\x01 \x03(\x0b23.google.analytics.admin.v1beta.AccessDimensionValue\x12G\n\rmetric_values\x18\x02 \x03(\x0b20.google.analytics.admin.v1beta.AccessMetricValue"%\n\x14AccessDimensionValue\x12\r\n\x05value\x18\x01 \x01(\t""\n\x11AccessMetricValue\x12\r\n\x05value\x18\x01 \x01(\t"\xa6\x03\n\x0bAccessQuota\x12H\n\x0etokens_per_day\x18\x01 \x01(\x0b20.google.analytics.admin.v1beta.AccessQuotaStatus\x12I\n\x0ftokens_per_hour\x18\x02 \x01(\x0b20.google.analytics.admin.v1beta.AccessQuotaStatus\x12M\n\x13concurrent_requests\x18\x03 \x01(\x0b20.google.analytics.admin.v1beta.AccessQuotaStatus\x12\\\n"server_errors_per_project_per_hour\x18\x04 \x01(\x0b20.google.analytics.admin.v1beta.AccessQuotaStatus\x12U\n\x1btokens_per_project_per_hour\x18\x05 \x01(\x0b20.google.analytics.admin.v1beta.AccessQuotaStatus"8\n\x11AccessQuotaStatus\x12\x10\n\x08consumed\x18\x01 \x01(\x05\x12\x11\n\tremaining\x18\x02 \x01(\x05Bw\n!com.google.analytics.admin.v1betaB\x11AccessReportProtoP\x01Z=cloud.google.com/go/analytics/admin/apiv1beta/adminpb;adminpbb\x06proto3')
_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'google.analytics.admin.v1beta.access_report_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
    _globals['DESCRIPTOR']._loaded_options = None
    _globals['DESCRIPTOR']._serialized_options = b'\n!com.google.analytics.admin.v1betaB\x11AccessReportProtoP\x01Z=cloud.google.com/go/analytics/admin/apiv1beta/adminpb;adminpb'
    _globals['_ACCESSDIMENSION']._serialized_start = 84
    _globals['_ACCESSDIMENSION']._serialized_end = 125
    _globals['_ACCESSMETRIC']._serialized_start = 127
    _globals['_ACCESSMETRIC']._serialized_end = 162
    _globals['_ACCESSDATERANGE']._serialized_start = 164
    _globals['_ACCESSDATERANGE']._serialized_end = 219
    _globals['_ACCESSFILTEREXPRESSION']._serialized_start = 222
    _globals['_ACCESSFILTEREXPRESSION']._serialized_end = 574
    _globals['_ACCESSFILTEREXPRESSIONLIST']._serialized_start = 576
    _globals['_ACCESSFILTEREXPRESSIONLIST']._serialized_end = 680
    _globals['_ACCESSFILTER']._serialized_start = 683
    _globals['_ACCESSFILTER']._serialized_end = 1040
    _globals['_ACCESSSTRINGFILTER']._serialized_start = 1043
    _globals['_ACCESSSTRINGFILTER']._serialized_end = 1319
    _globals['_ACCESSSTRINGFILTER_MATCHTYPE']._serialized_start = 1186
    _globals['_ACCESSSTRINGFILTER_MATCHTYPE']._serialized_end = 1319
    _globals['_ACCESSINLISTFILTER']._serialized_start = 1321
    _globals['_ACCESSINLISTFILTER']._serialized_end = 1381
    _globals['_ACCESSNUMERICFILTER']._serialized_start = 1384
    _globals['_ACCESSNUMERICFILTER']._serialized_end = 1682
    _globals['_ACCESSNUMERICFILTER_OPERATION']._serialized_start = 1549
    _globals['_ACCESSNUMERICFILTER_OPERATION']._serialized_end = 1682
    _globals['_ACCESSBETWEENFILTER']._serialized_start = 1685
    _globals['_ACCESSBETWEENFILTER']._serialized_end = 1834
    _globals['_NUMERICVALUE']._serialized_start = 1836
    _globals['_NUMERICVALUE']._serialized_end = 1910
    _globals['_ACCESSORDERBY']._serialized_start = 1913
    _globals['_ACCESSORDERBY']._serialized_end = 2403
    _globals['_ACCESSORDERBY_METRICORDERBY']._serialized_start = 2106
    _globals['_ACCESSORDERBY_METRICORDERBY']._serialized_end = 2142
    _globals['_ACCESSORDERBY_DIMENSIONORDERBY']._serialized_start = 2145
    _globals['_ACCESSORDERBY_DIMENSIONORDERBY']._serialized_end = 2387
    _globals['_ACCESSORDERBY_DIMENSIONORDERBY_ORDERTYPE']._serialized_start = 2282
    _globals['_ACCESSORDERBY_DIMENSIONORDERBY_ORDERTYPE']._serialized_end = 2387
    _globals['_ACCESSDIMENSIONHEADER']._serialized_start = 2405
    _globals['_ACCESSDIMENSIONHEADER']._serialized_end = 2452
    _globals['_ACCESSMETRICHEADER']._serialized_start = 2454
    _globals['_ACCESSMETRICHEADER']._serialized_end = 2495
    _globals['_ACCESSROW']._serialized_start = 2498
    _globals['_ACCESSROW']._serialized_end = 2661
    _globals['_ACCESSDIMENSIONVALUE']._serialized_start = 2663
    _globals['_ACCESSDIMENSIONVALUE']._serialized_end = 2700
    _globals['_ACCESSMETRICVALUE']._serialized_start = 2702
    _globals['_ACCESSMETRICVALUE']._serialized_end = 2736
    _globals['_ACCESSQUOTA']._serialized_start = 2739
    _globals['_ACCESSQUOTA']._serialized_end = 3161
    _globals['_ACCESSQUOTASTATUS']._serialized_start = 3163
    _globals['_ACCESSQUOTASTATUS']._serialized_end = 3219