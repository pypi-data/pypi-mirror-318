"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_runtime_version.ValidateProtobufRuntimeVersion(_runtime_version.Domain.PUBLIC, 5, 28, 1, '', 'google/analytics/admin/v1alpha/access_report.proto')
_sym_db = _symbol_database.Default()
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n2google/analytics/admin/v1alpha/access_report.proto\x12\x1egoogle.analytics.admin.v1alpha")\n\x0fAccessDimension\x12\x16\n\x0edimension_name\x18\x01 \x01(\t"#\n\x0cAccessMetric\x12\x13\n\x0bmetric_name\x18\x01 \x01(\t"7\n\x0fAccessDateRange\x12\x12\n\nstart_date\x18\x01 \x01(\t\x12\x10\n\x08end_date\x18\x02 \x01(\t"\xe4\x02\n\x16AccessFilterExpression\x12O\n\tand_group\x18\x01 \x01(\x0b2:.google.analytics.admin.v1alpha.AccessFilterExpressionListH\x00\x12N\n\x08or_group\x18\x02 \x01(\x0b2:.google.analytics.admin.v1alpha.AccessFilterExpressionListH\x00\x12P\n\x0enot_expression\x18\x03 \x01(\x0b26.google.analytics.admin.v1alpha.AccessFilterExpressionH\x00\x12E\n\raccess_filter\x18\x04 \x01(\x0b2,.google.analytics.admin.v1alpha.AccessFilterH\x00B\x10\n\x0eone_expression"i\n\x1aAccessFilterExpressionList\x12K\n\x0bexpressions\x18\x01 \x03(\x0b26.google.analytics.admin.v1alpha.AccessFilterExpression"\xe9\x02\n\x0cAccessFilter\x12K\n\rstring_filter\x18\x02 \x01(\x0b22.google.analytics.admin.v1alpha.AccessStringFilterH\x00\x12L\n\x0ein_list_filter\x18\x03 \x01(\x0b22.google.analytics.admin.v1alpha.AccessInListFilterH\x00\x12M\n\x0enumeric_filter\x18\x04 \x01(\x0b23.google.analytics.admin.v1alpha.AccessNumericFilterH\x00\x12M\n\x0ebetween_filter\x18\x05 \x01(\x0b23.google.analytics.admin.v1alpha.AccessBetweenFilterH\x00\x12\x12\n\nfield_name\x18\x01 \x01(\tB\x0c\n\none_filter"\x95\x02\n\x12AccessStringFilter\x12P\n\nmatch_type\x18\x01 \x01(\x0e2<.google.analytics.admin.v1alpha.AccessStringFilter.MatchType\x12\r\n\x05value\x18\x02 \x01(\t\x12\x16\n\x0ecase_sensitive\x18\x03 \x01(\x08"\x85\x01\n\tMatchType\x12\x1a\n\x16MATCH_TYPE_UNSPECIFIED\x10\x00\x12\t\n\x05EXACT\x10\x01\x12\x0f\n\x0bBEGINS_WITH\x10\x02\x12\r\n\tENDS_WITH\x10\x03\x12\x0c\n\x08CONTAINS\x10\x04\x12\x0f\n\x0bFULL_REGEXP\x10\x05\x12\x12\n\x0ePARTIAL_REGEXP\x10\x06"<\n\x12AccessInListFilter\x12\x0e\n\x06values\x18\x01 \x03(\t\x12\x16\n\x0ecase_sensitive\x18\x02 \x01(\x08"\xac\x02\n\x13AccessNumericFilter\x12P\n\toperation\x18\x01 \x01(\x0e2=.google.analytics.admin.v1alpha.AccessNumericFilter.Operation\x12;\n\x05value\x18\x02 \x01(\x0b2,.google.analytics.admin.v1alpha.NumericValue"\x85\x01\n\tOperation\x12\x19\n\x15OPERATION_UNSPECIFIED\x10\x00\x12\t\n\x05EQUAL\x10\x01\x12\r\n\tLESS_THAN\x10\x02\x12\x16\n\x12LESS_THAN_OR_EQUAL\x10\x03\x12\x10\n\x0cGREATER_THAN\x10\x04\x12\x19\n\x15GREATER_THAN_OR_EQUAL\x10\x05"\x97\x01\n\x13AccessBetweenFilter\x12@\n\nfrom_value\x18\x01 \x01(\x0b2,.google.analytics.admin.v1alpha.NumericValue\x12>\n\x08to_value\x18\x02 \x01(\x0b2,.google.analytics.admin.v1alpha.NumericValue"J\n\x0cNumericValue\x12\x15\n\x0bint64_value\x18\x01 \x01(\x03H\x00\x12\x16\n\x0cdouble_value\x18\x02 \x01(\x01H\x00B\x0b\n\tone_value"\xed\x03\n\rAccessOrderBy\x12M\n\x06metric\x18\x01 \x01(\x0b2;.google.analytics.admin.v1alpha.AccessOrderBy.MetricOrderByH\x00\x12S\n\tdimension\x18\x02 \x01(\x0b2>.google.analytics.admin.v1alpha.AccessOrderBy.DimensionOrderByH\x00\x12\x0c\n\x04desc\x18\x03 \x01(\x08\x1a$\n\rMetricOrderBy\x12\x13\n\x0bmetric_name\x18\x01 \x01(\t\x1a\xf3\x01\n\x10DimensionOrderBy\x12\x16\n\x0edimension_name\x18\x01 \x01(\t\x12\\\n\norder_type\x18\x02 \x01(\x0e2H.google.analytics.admin.v1alpha.AccessOrderBy.DimensionOrderBy.OrderType"i\n\tOrderType\x12\x1a\n\x16ORDER_TYPE_UNSPECIFIED\x10\x00\x12\x10\n\x0cALPHANUMERIC\x10\x01\x12!\n\x1dCASE_INSENSITIVE_ALPHANUMERIC\x10\x02\x12\x0b\n\x07NUMERIC\x10\x03B\x0e\n\x0cone_order_by"/\n\x15AccessDimensionHeader\x12\x16\n\x0edimension_name\x18\x01 \x01(\t")\n\x12AccessMetricHeader\x12\x13\n\x0bmetric_name\x18\x01 \x01(\t"\xa5\x01\n\tAccessRow\x12N\n\x10dimension_values\x18\x01 \x03(\x0b24.google.analytics.admin.v1alpha.AccessDimensionValue\x12H\n\rmetric_values\x18\x02 \x03(\x0b21.google.analytics.admin.v1alpha.AccessMetricValue"%\n\x14AccessDimensionValue\x12\r\n\x05value\x18\x01 \x01(\t""\n\x11AccessMetricValue\x12\r\n\x05value\x18\x01 \x01(\t"\xab\x03\n\x0bAccessQuota\x12I\n\x0etokens_per_day\x18\x01 \x01(\x0b21.google.analytics.admin.v1alpha.AccessQuotaStatus\x12J\n\x0ftokens_per_hour\x18\x02 \x01(\x0b21.google.analytics.admin.v1alpha.AccessQuotaStatus\x12N\n\x13concurrent_requests\x18\x03 \x01(\x0b21.google.analytics.admin.v1alpha.AccessQuotaStatus\x12]\n"server_errors_per_project_per_hour\x18\x04 \x01(\x0b21.google.analytics.admin.v1alpha.AccessQuotaStatus\x12V\n\x1btokens_per_project_per_hour\x18\x05 \x01(\x0b21.google.analytics.admin.v1alpha.AccessQuotaStatus"8\n\x11AccessQuotaStatus\x12\x10\n\x08consumed\x18\x01 \x01(\x05\x12\x11\n\tremaining\x18\x02 \x01(\x05By\n"com.google.analytics.admin.v1alphaB\x11AccessReportProtoP\x01Z>cloud.google.com/go/analytics/admin/apiv1alpha/adminpb;adminpbb\x06proto3')
_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'google.analytics.admin.v1alpha.access_report_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
    _globals['DESCRIPTOR']._loaded_options = None
    _globals['DESCRIPTOR']._serialized_options = b'\n"com.google.analytics.admin.v1alphaB\x11AccessReportProtoP\x01Z>cloud.google.com/go/analytics/admin/apiv1alpha/adminpb;adminpb'
    _globals['_ACCESSDIMENSION']._serialized_start = 86
    _globals['_ACCESSDIMENSION']._serialized_end = 127
    _globals['_ACCESSMETRIC']._serialized_start = 129
    _globals['_ACCESSMETRIC']._serialized_end = 164
    _globals['_ACCESSDATERANGE']._serialized_start = 166
    _globals['_ACCESSDATERANGE']._serialized_end = 221
    _globals['_ACCESSFILTEREXPRESSION']._serialized_start = 224
    _globals['_ACCESSFILTEREXPRESSION']._serialized_end = 580
    _globals['_ACCESSFILTEREXPRESSIONLIST']._serialized_start = 582
    _globals['_ACCESSFILTEREXPRESSIONLIST']._serialized_end = 687
    _globals['_ACCESSFILTER']._serialized_start = 690
    _globals['_ACCESSFILTER']._serialized_end = 1051
    _globals['_ACCESSSTRINGFILTER']._serialized_start = 1054
    _globals['_ACCESSSTRINGFILTER']._serialized_end = 1331
    _globals['_ACCESSSTRINGFILTER_MATCHTYPE']._serialized_start = 1198
    _globals['_ACCESSSTRINGFILTER_MATCHTYPE']._serialized_end = 1331
    _globals['_ACCESSINLISTFILTER']._serialized_start = 1333
    _globals['_ACCESSINLISTFILTER']._serialized_end = 1393
    _globals['_ACCESSNUMERICFILTER']._serialized_start = 1396
    _globals['_ACCESSNUMERICFILTER']._serialized_end = 1696
    _globals['_ACCESSNUMERICFILTER_OPERATION']._serialized_start = 1563
    _globals['_ACCESSNUMERICFILTER_OPERATION']._serialized_end = 1696
    _globals['_ACCESSBETWEENFILTER']._serialized_start = 1699
    _globals['_ACCESSBETWEENFILTER']._serialized_end = 1850
    _globals['_NUMERICVALUE']._serialized_start = 1852
    _globals['_NUMERICVALUE']._serialized_end = 1926
    _globals['_ACCESSORDERBY']._serialized_start = 1929
    _globals['_ACCESSORDERBY']._serialized_end = 2422
    _globals['_ACCESSORDERBY_METRICORDERBY']._serialized_start = 2124
    _globals['_ACCESSORDERBY_METRICORDERBY']._serialized_end = 2160
    _globals['_ACCESSORDERBY_DIMENSIONORDERBY']._serialized_start = 2163
    _globals['_ACCESSORDERBY_DIMENSIONORDERBY']._serialized_end = 2406
    _globals['_ACCESSORDERBY_DIMENSIONORDERBY_ORDERTYPE']._serialized_start = 2301
    _globals['_ACCESSORDERBY_DIMENSIONORDERBY_ORDERTYPE']._serialized_end = 2406
    _globals['_ACCESSDIMENSIONHEADER']._serialized_start = 2424
    _globals['_ACCESSDIMENSIONHEADER']._serialized_end = 2471
    _globals['_ACCESSMETRICHEADER']._serialized_start = 2473
    _globals['_ACCESSMETRICHEADER']._serialized_end = 2514
    _globals['_ACCESSROW']._serialized_start = 2517
    _globals['_ACCESSROW']._serialized_end = 2682
    _globals['_ACCESSDIMENSIONVALUE']._serialized_start = 2684
    _globals['_ACCESSDIMENSIONVALUE']._serialized_end = 2721
    _globals['_ACCESSMETRICVALUE']._serialized_start = 2723
    _globals['_ACCESSMETRICVALUE']._serialized_end = 2757
    _globals['_ACCESSQUOTA']._serialized_start = 2760
    _globals['_ACCESSQUOTA']._serialized_end = 3187
    _globals['_ACCESSQUOTASTATUS']._serialized_start = 3189
    _globals['_ACCESSQUOTASTATUS']._serialized_end = 3245