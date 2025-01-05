"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_runtime_version.ValidateProtobufRuntimeVersion(_runtime_version.Domain.PUBLIC, 5, 28, 1, '', 'google/analytics/admin/v1alpha/audience.proto')
_sym_db = _symbol_database.Default()
from .....google.api import field_behavior_pb2 as google_dot_api_dot_field__behavior__pb2
from .....google.api import resource_pb2 as google_dot_api_dot_resource__pb2
from google.protobuf import duration_pb2 as google_dot_protobuf_dot_duration__pb2
from google.protobuf import timestamp_pb2 as google_dot_protobuf_dot_timestamp__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n-google/analytics/admin/v1alpha/audience.proto\x12\x1egoogle.analytics.admin.v1alpha\x1a\x1fgoogle/api/field_behavior.proto\x1a\x19google/api/resource.proto\x1a\x1egoogle/protobuf/duration.proto\x1a\x1fgoogle/protobuf/timestamp.proto"\xfc\x0b\n\x1fAudienceDimensionOrMetricFilter\x12e\n\rstring_filter\x18\x02 \x01(\x0b2L.google.analytics.admin.v1alpha.AudienceDimensionOrMetricFilter.StringFilterH\x00\x12f\n\x0ein_list_filter\x18\x03 \x01(\x0b2L.google.analytics.admin.v1alpha.AudienceDimensionOrMetricFilter.InListFilterH\x00\x12g\n\x0enumeric_filter\x18\x04 \x01(\x0b2M.google.analytics.admin.v1alpha.AudienceDimensionOrMetricFilter.NumericFilterH\x00\x12g\n\x0ebetween_filter\x18\x05 \x01(\x0b2M.google.analytics.admin.v1alpha.AudienceDimensionOrMetricFilter.BetweenFilterH\x00\x12\x1a\n\nfield_name\x18\x01 \x01(\tB\x06\xe0A\x02\xe0A\x05\x12!\n\x14at_any_point_in_time\x18\x06 \x01(\x08B\x03\xe0A\x01\x12 \n\x13in_any_n_day_period\x18\x07 \x01(\x05B\x03\xe0A\x01\x1a\xa3\x02\n\x0cStringFilter\x12o\n\nmatch_type\x18\x01 \x01(\x0e2V.google.analytics.admin.v1alpha.AudienceDimensionOrMetricFilter.StringFilter.MatchTypeB\x03\xe0A\x02\x12\x12\n\x05value\x18\x02 \x01(\tB\x03\xe0A\x02\x12\x1b\n\x0ecase_sensitive\x18\x03 \x01(\x08B\x03\xe0A\x01"q\n\tMatchType\x12\x1a\n\x16MATCH_TYPE_UNSPECIFIED\x10\x00\x12\t\n\x05EXACT\x10\x01\x12\x0f\n\x0bBEGINS_WITH\x10\x02\x12\r\n\tENDS_WITH\x10\x03\x12\x0c\n\x08CONTAINS\x10\x04\x12\x0f\n\x0bFULL_REGEXP\x10\x05\x1a@\n\x0cInListFilter\x12\x13\n\x06values\x18\x01 \x03(\tB\x03\xe0A\x02\x12\x1b\n\x0ecase_sensitive\x18\x02 \x01(\x08B\x03\xe0A\x01\x1aJ\n\x0cNumericValue\x12\x15\n\x0bint64_value\x18\x01 \x01(\x03H\x00\x12\x16\n\x0cdouble_value\x18\x02 \x01(\x01H\x00B\x0b\n\tone_value\x1a\xb6\x02\n\rNumericFilter\x12o\n\toperation\x18\x01 \x01(\x0e2W.google.analytics.admin.v1alpha.AudienceDimensionOrMetricFilter.NumericFilter.OperationB\x03\xe0A\x02\x12`\n\x05value\x18\x02 \x01(\x0b2L.google.analytics.admin.v1alpha.AudienceDimensionOrMetricFilter.NumericValueB\x03\xe0A\x02"R\n\tOperation\x12\x19\n\x15OPERATION_UNSPECIFIED\x10\x00\x12\t\n\x05EQUAL\x10\x01\x12\r\n\tLESS_THAN\x10\x02\x12\x10\n\x0cGREATER_THAN\x10\x04\x1a\xdb\x01\n\rBetweenFilter\x12e\n\nfrom_value\x18\x01 \x01(\x0b2L.google.analytics.admin.v1alpha.AudienceDimensionOrMetricFilter.NumericValueB\x03\xe0A\x02\x12c\n\x08to_value\x18\x02 \x01(\x0b2L.google.analytics.admin.v1alpha.AudienceDimensionOrMetricFilter.NumericValueB\x03\xe0A\x02B\x0c\n\none_filter"\x9b\x01\n\x13AudienceEventFilter\x12\x1a\n\nevent_name\x18\x01 \x01(\tB\x06\xe0A\x02\xe0A\x05\x12h\n!event_parameter_filter_expression\x18\x02 \x01(\x0b28.google.analytics.admin.v1alpha.AudienceFilterExpressionB\x03\xe0A\x01"\xcf\x03\n\x18AudienceFilterExpression\x12Q\n\tand_group\x18\x01 \x01(\x0b2<.google.analytics.admin.v1alpha.AudienceFilterExpressionListH\x00\x12P\n\x08or_group\x18\x02 \x01(\x0b2<.google.analytics.admin.v1alpha.AudienceFilterExpressionListH\x00\x12R\n\x0enot_expression\x18\x03 \x01(\x0b28.google.analytics.admin.v1alpha.AudienceFilterExpressionH\x00\x12e\n\x1adimension_or_metric_filter\x18\x04 \x01(\x0b2?.google.analytics.admin.v1alpha.AudienceDimensionOrMetricFilterH\x00\x12K\n\x0cevent_filter\x18\x05 \x01(\x0b23.google.analytics.admin.v1alpha.AudienceEventFilterH\x00B\x06\n\x04expr"t\n\x1cAudienceFilterExpressionList\x12T\n\x12filter_expressions\x18\x01 \x03(\x0b28.google.analytics.admin.v1alpha.AudienceFilterExpression"\xbf\x01\n\x14AudienceSimpleFilter\x12J\n\x05scope\x18\x01 \x01(\x0e23.google.analytics.admin.v1alpha.AudienceFilterScopeB\x06\xe0A\x02\xe0A\x05\x12[\n\x11filter_expression\x18\x02 \x01(\x0b28.google.analytics.admin.v1alpha.AudienceFilterExpressionB\x06\xe0A\x02\xe0A\x05"\xb2\x04\n\x16AudienceSequenceFilter\x12J\n\x05scope\x18\x01 \x01(\x0e23.google.analytics.admin.v1alpha.AudienceFilterScopeB\x06\xe0A\x02\xe0A\x05\x12A\n\x19sequence_maximum_duration\x18\x02 \x01(\x0b2\x19.google.protobuf.DurationB\x03\xe0A\x01\x12h\n\x0esequence_steps\x18\x03 \x03(\x0b2K.google.analytics.admin.v1alpha.AudienceSequenceFilter.AudienceSequenceStepB\x03\xe0A\x02\x1a\x9e\x02\n\x14AudienceSequenceStep\x12J\n\x05scope\x18\x01 \x01(\x0e23.google.analytics.admin.v1alpha.AudienceFilterScopeB\x06\xe0A\x02\xe0A\x05\x12 \n\x13immediately_follows\x18\x02 \x01(\x08B\x03\xe0A\x01\x12;\n\x13constraint_duration\x18\x03 \x01(\x0b2\x19.google.protobuf.DurationB\x03\xe0A\x01\x12[\n\x11filter_expression\x18\x04 \x01(\x0b28.google.analytics.admin.v1alpha.AudienceFilterExpressionB\x06\xe0A\x02\xe0A\x05"\xfb\x02\n\x14AudienceFilterClause\x12M\n\rsimple_filter\x18\x02 \x01(\x0b24.google.analytics.admin.v1alpha.AudienceSimpleFilterH\x00\x12Q\n\x0fsequence_filter\x18\x03 \x01(\x0b26.google.analytics.admin.v1alpha.AudienceSequenceFilterH\x00\x12a\n\x0bclause_type\x18\x01 \x01(\x0e2G.google.analytics.admin.v1alpha.AudienceFilterClause.AudienceClauseTypeB\x03\xe0A\x02"T\n\x12AudienceClauseType\x12$\n AUDIENCE_CLAUSE_TYPE_UNSPECIFIED\x10\x00\x12\x0b\n\x07INCLUDE\x10\x01\x12\x0b\n\x07EXCLUDE\x10\x02B\x08\n\x06filter"\xf3\x01\n\x14AudienceEventTrigger\x12\x17\n\nevent_name\x18\x01 \x01(\tB\x03\xe0A\x02\x12]\n\rlog_condition\x18\x02 \x01(\x0e2A.google.analytics.admin.v1alpha.AudienceEventTrigger.LogConditionB\x03\xe0A\x02"c\n\x0cLogCondition\x12\x1d\n\x19LOG_CONDITION_UNSPECIFIED\x10\x00\x12\x13\n\x0fAUDIENCE_JOINED\x10\x01\x12\x1f\n\x1bAUDIENCE_MEMBERSHIP_RENEWED\x10\x02"\xd4\x05\n\x08Audience\x12\x11\n\x04name\x18\x01 \x01(\tB\x03\xe0A\x03\x12\x19\n\x0cdisplay_name\x18\x02 \x01(\tB\x03\xe0A\x02\x12\x18\n\x0bdescription\x18\x03 \x01(\tB\x03\xe0A\x02\x12(\n\x18membership_duration_days\x18\x04 \x01(\x05B\x06\xe0A\x02\xe0A\x05\x12(\n\x1bads_personalization_enabled\x18\x05 \x01(\x08B\x03\xe0A\x03\x12P\n\revent_trigger\x18\x06 \x01(\x0b24.google.analytics.admin.v1alpha.AudienceEventTriggerB\x03\xe0A\x01\x12l\n\x17exclusion_duration_mode\x18\x07 \x01(\x0e2F.google.analytics.admin.v1alpha.Audience.AudienceExclusionDurationModeB\x03\xe0A\x05\x12W\n\x0efilter_clauses\x18\x08 \x03(\x0b24.google.analytics.admin.v1alpha.AudienceFilterClauseB\t\xe0A\x05\xe0A\x02\xe0A\x06\x124\n\x0bcreate_time\x18\t \x01(\x0b2\x1a.google.protobuf.TimestampB\x03\xe0A\x03"\x83\x01\n\x1dAudienceExclusionDurationMode\x120\n,AUDIENCE_EXCLUSION_DURATION_MODE_UNSPECIFIED\x10\x00\x12\x17\n\x13EXCLUDE_TEMPORARILY\x10\x01\x12\x17\n\x13EXCLUDE_PERMANENTLY\x10\x02:W\xeaAT\n&analyticsadmin.googleapis.com/Audience\x12*properties/{property}/audiences/{audience}*\xc7\x01\n\x13AudienceFilterScope\x12%\n!AUDIENCE_FILTER_SCOPE_UNSPECIFIED\x10\x00\x12+\n\'AUDIENCE_FILTER_SCOPE_WITHIN_SAME_EVENT\x10\x01\x12-\n)AUDIENCE_FILTER_SCOPE_WITHIN_SAME_SESSION\x10\x02\x12-\n)AUDIENCE_FILTER_SCOPE_ACROSS_ALL_SESSIONS\x10\x03Bu\n"com.google.analytics.admin.v1alphaB\rAudienceProtoP\x01Z>cloud.google.com/go/analytics/admin/apiv1alpha/adminpb;adminpbb\x06proto3')
_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'google.analytics.admin.v1alpha.audience_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
    _globals['DESCRIPTOR']._loaded_options = None
    _globals['DESCRIPTOR']._serialized_options = b'\n"com.google.analytics.admin.v1alphaB\rAudienceProtoP\x01Z>cloud.google.com/go/analytics/admin/apiv1alpha/adminpb;adminpb'
    _globals['_AUDIENCEDIMENSIONORMETRICFILTER_STRINGFILTER'].fields_by_name['match_type']._loaded_options = None
    _globals['_AUDIENCEDIMENSIONORMETRICFILTER_STRINGFILTER'].fields_by_name['match_type']._serialized_options = b'\xe0A\x02'
    _globals['_AUDIENCEDIMENSIONORMETRICFILTER_STRINGFILTER'].fields_by_name['value']._loaded_options = None
    _globals['_AUDIENCEDIMENSIONORMETRICFILTER_STRINGFILTER'].fields_by_name['value']._serialized_options = b'\xe0A\x02'
    _globals['_AUDIENCEDIMENSIONORMETRICFILTER_STRINGFILTER'].fields_by_name['case_sensitive']._loaded_options = None
    _globals['_AUDIENCEDIMENSIONORMETRICFILTER_STRINGFILTER'].fields_by_name['case_sensitive']._serialized_options = b'\xe0A\x01'
    _globals['_AUDIENCEDIMENSIONORMETRICFILTER_INLISTFILTER'].fields_by_name['values']._loaded_options = None
    _globals['_AUDIENCEDIMENSIONORMETRICFILTER_INLISTFILTER'].fields_by_name['values']._serialized_options = b'\xe0A\x02'
    _globals['_AUDIENCEDIMENSIONORMETRICFILTER_INLISTFILTER'].fields_by_name['case_sensitive']._loaded_options = None
    _globals['_AUDIENCEDIMENSIONORMETRICFILTER_INLISTFILTER'].fields_by_name['case_sensitive']._serialized_options = b'\xe0A\x01'
    _globals['_AUDIENCEDIMENSIONORMETRICFILTER_NUMERICFILTER'].fields_by_name['operation']._loaded_options = None
    _globals['_AUDIENCEDIMENSIONORMETRICFILTER_NUMERICFILTER'].fields_by_name['operation']._serialized_options = b'\xe0A\x02'
    _globals['_AUDIENCEDIMENSIONORMETRICFILTER_NUMERICFILTER'].fields_by_name['value']._loaded_options = None
    _globals['_AUDIENCEDIMENSIONORMETRICFILTER_NUMERICFILTER'].fields_by_name['value']._serialized_options = b'\xe0A\x02'
    _globals['_AUDIENCEDIMENSIONORMETRICFILTER_BETWEENFILTER'].fields_by_name['from_value']._loaded_options = None
    _globals['_AUDIENCEDIMENSIONORMETRICFILTER_BETWEENFILTER'].fields_by_name['from_value']._serialized_options = b'\xe0A\x02'
    _globals['_AUDIENCEDIMENSIONORMETRICFILTER_BETWEENFILTER'].fields_by_name['to_value']._loaded_options = None
    _globals['_AUDIENCEDIMENSIONORMETRICFILTER_BETWEENFILTER'].fields_by_name['to_value']._serialized_options = b'\xe0A\x02'
    _globals['_AUDIENCEDIMENSIONORMETRICFILTER'].fields_by_name['field_name']._loaded_options = None
    _globals['_AUDIENCEDIMENSIONORMETRICFILTER'].fields_by_name['field_name']._serialized_options = b'\xe0A\x02\xe0A\x05'
    _globals['_AUDIENCEDIMENSIONORMETRICFILTER'].fields_by_name['at_any_point_in_time']._loaded_options = None
    _globals['_AUDIENCEDIMENSIONORMETRICFILTER'].fields_by_name['at_any_point_in_time']._serialized_options = b'\xe0A\x01'
    _globals['_AUDIENCEDIMENSIONORMETRICFILTER'].fields_by_name['in_any_n_day_period']._loaded_options = None
    _globals['_AUDIENCEDIMENSIONORMETRICFILTER'].fields_by_name['in_any_n_day_period']._serialized_options = b'\xe0A\x01'
    _globals['_AUDIENCEEVENTFILTER'].fields_by_name['event_name']._loaded_options = None
    _globals['_AUDIENCEEVENTFILTER'].fields_by_name['event_name']._serialized_options = b'\xe0A\x02\xe0A\x05'
    _globals['_AUDIENCEEVENTFILTER'].fields_by_name['event_parameter_filter_expression']._loaded_options = None
    _globals['_AUDIENCEEVENTFILTER'].fields_by_name['event_parameter_filter_expression']._serialized_options = b'\xe0A\x01'
    _globals['_AUDIENCESIMPLEFILTER'].fields_by_name['scope']._loaded_options = None
    _globals['_AUDIENCESIMPLEFILTER'].fields_by_name['scope']._serialized_options = b'\xe0A\x02\xe0A\x05'
    _globals['_AUDIENCESIMPLEFILTER'].fields_by_name['filter_expression']._loaded_options = None
    _globals['_AUDIENCESIMPLEFILTER'].fields_by_name['filter_expression']._serialized_options = b'\xe0A\x02\xe0A\x05'
    _globals['_AUDIENCESEQUENCEFILTER_AUDIENCESEQUENCESTEP'].fields_by_name['scope']._loaded_options = None
    _globals['_AUDIENCESEQUENCEFILTER_AUDIENCESEQUENCESTEP'].fields_by_name['scope']._serialized_options = b'\xe0A\x02\xe0A\x05'
    _globals['_AUDIENCESEQUENCEFILTER_AUDIENCESEQUENCESTEP'].fields_by_name['immediately_follows']._loaded_options = None
    _globals['_AUDIENCESEQUENCEFILTER_AUDIENCESEQUENCESTEP'].fields_by_name['immediately_follows']._serialized_options = b'\xe0A\x01'
    _globals['_AUDIENCESEQUENCEFILTER_AUDIENCESEQUENCESTEP'].fields_by_name['constraint_duration']._loaded_options = None
    _globals['_AUDIENCESEQUENCEFILTER_AUDIENCESEQUENCESTEP'].fields_by_name['constraint_duration']._serialized_options = b'\xe0A\x01'
    _globals['_AUDIENCESEQUENCEFILTER_AUDIENCESEQUENCESTEP'].fields_by_name['filter_expression']._loaded_options = None
    _globals['_AUDIENCESEQUENCEFILTER_AUDIENCESEQUENCESTEP'].fields_by_name['filter_expression']._serialized_options = b'\xe0A\x02\xe0A\x05'
    _globals['_AUDIENCESEQUENCEFILTER'].fields_by_name['scope']._loaded_options = None
    _globals['_AUDIENCESEQUENCEFILTER'].fields_by_name['scope']._serialized_options = b'\xe0A\x02\xe0A\x05'
    _globals['_AUDIENCESEQUENCEFILTER'].fields_by_name['sequence_maximum_duration']._loaded_options = None
    _globals['_AUDIENCESEQUENCEFILTER'].fields_by_name['sequence_maximum_duration']._serialized_options = b'\xe0A\x01'
    _globals['_AUDIENCESEQUENCEFILTER'].fields_by_name['sequence_steps']._loaded_options = None
    _globals['_AUDIENCESEQUENCEFILTER'].fields_by_name['sequence_steps']._serialized_options = b'\xe0A\x02'
    _globals['_AUDIENCEFILTERCLAUSE'].fields_by_name['clause_type']._loaded_options = None
    _globals['_AUDIENCEFILTERCLAUSE'].fields_by_name['clause_type']._serialized_options = b'\xe0A\x02'
    _globals['_AUDIENCEEVENTTRIGGER'].fields_by_name['event_name']._loaded_options = None
    _globals['_AUDIENCEEVENTTRIGGER'].fields_by_name['event_name']._serialized_options = b'\xe0A\x02'
    _globals['_AUDIENCEEVENTTRIGGER'].fields_by_name['log_condition']._loaded_options = None
    _globals['_AUDIENCEEVENTTRIGGER'].fields_by_name['log_condition']._serialized_options = b'\xe0A\x02'
    _globals['_AUDIENCE'].fields_by_name['name']._loaded_options = None
    _globals['_AUDIENCE'].fields_by_name['name']._serialized_options = b'\xe0A\x03'
    _globals['_AUDIENCE'].fields_by_name['display_name']._loaded_options = None
    _globals['_AUDIENCE'].fields_by_name['display_name']._serialized_options = b'\xe0A\x02'
    _globals['_AUDIENCE'].fields_by_name['description']._loaded_options = None
    _globals['_AUDIENCE'].fields_by_name['description']._serialized_options = b'\xe0A\x02'
    _globals['_AUDIENCE'].fields_by_name['membership_duration_days']._loaded_options = None
    _globals['_AUDIENCE'].fields_by_name['membership_duration_days']._serialized_options = b'\xe0A\x02\xe0A\x05'
    _globals['_AUDIENCE'].fields_by_name['ads_personalization_enabled']._loaded_options = None
    _globals['_AUDIENCE'].fields_by_name['ads_personalization_enabled']._serialized_options = b'\xe0A\x03'
    _globals['_AUDIENCE'].fields_by_name['event_trigger']._loaded_options = None
    _globals['_AUDIENCE'].fields_by_name['event_trigger']._serialized_options = b'\xe0A\x01'
    _globals['_AUDIENCE'].fields_by_name['exclusion_duration_mode']._loaded_options = None
    _globals['_AUDIENCE'].fields_by_name['exclusion_duration_mode']._serialized_options = b'\xe0A\x05'
    _globals['_AUDIENCE'].fields_by_name['filter_clauses']._loaded_options = None
    _globals['_AUDIENCE'].fields_by_name['filter_clauses']._serialized_options = b'\xe0A\x05\xe0A\x02\xe0A\x06'
    _globals['_AUDIENCE'].fields_by_name['create_time']._loaded_options = None
    _globals['_AUDIENCE'].fields_by_name['create_time']._serialized_options = b'\xe0A\x03'
    _globals['_AUDIENCE']._loaded_options = None
    _globals['_AUDIENCE']._serialized_options = b'\xeaAT\n&analyticsadmin.googleapis.com/Audience\x12*properties/{property}/audiences/{audience}'
    _globals['_AUDIENCEFILTERSCOPE']._serialized_start = 4598
    _globals['_AUDIENCEFILTERSCOPE']._serialized_end = 4797
    _globals['_AUDIENCEDIMENSIONORMETRICFILTER']._serialized_start = 207
    _globals['_AUDIENCEDIMENSIONORMETRICFILTER']._serialized_end = 1739
    _globals['_AUDIENCEDIMENSIONORMETRICFILTER_STRINGFILTER']._serialized_start = 757
    _globals['_AUDIENCEDIMENSIONORMETRICFILTER_STRINGFILTER']._serialized_end = 1048
    _globals['_AUDIENCEDIMENSIONORMETRICFILTER_STRINGFILTER_MATCHTYPE']._serialized_start = 935
    _globals['_AUDIENCEDIMENSIONORMETRICFILTER_STRINGFILTER_MATCHTYPE']._serialized_end = 1048
    _globals['_AUDIENCEDIMENSIONORMETRICFILTER_INLISTFILTER']._serialized_start = 1050
    _globals['_AUDIENCEDIMENSIONORMETRICFILTER_INLISTFILTER']._serialized_end = 1114
    _globals['_AUDIENCEDIMENSIONORMETRICFILTER_NUMERICVALUE']._serialized_start = 1116
    _globals['_AUDIENCEDIMENSIONORMETRICFILTER_NUMERICVALUE']._serialized_end = 1190
    _globals['_AUDIENCEDIMENSIONORMETRICFILTER_NUMERICFILTER']._serialized_start = 1193
    _globals['_AUDIENCEDIMENSIONORMETRICFILTER_NUMERICFILTER']._serialized_end = 1503
    _globals['_AUDIENCEDIMENSIONORMETRICFILTER_NUMERICFILTER_OPERATION']._serialized_start = 1421
    _globals['_AUDIENCEDIMENSIONORMETRICFILTER_NUMERICFILTER_OPERATION']._serialized_end = 1503
    _globals['_AUDIENCEDIMENSIONORMETRICFILTER_BETWEENFILTER']._serialized_start = 1506
    _globals['_AUDIENCEDIMENSIONORMETRICFILTER_BETWEENFILTER']._serialized_end = 1725
    _globals['_AUDIENCEEVENTFILTER']._serialized_start = 1742
    _globals['_AUDIENCEEVENTFILTER']._serialized_end = 1897
    _globals['_AUDIENCEFILTEREXPRESSION']._serialized_start = 1900
    _globals['_AUDIENCEFILTEREXPRESSION']._serialized_end = 2363
    _globals['_AUDIENCEFILTEREXPRESSIONLIST']._serialized_start = 2365
    _globals['_AUDIENCEFILTEREXPRESSIONLIST']._serialized_end = 2481
    _globals['_AUDIENCESIMPLEFILTER']._serialized_start = 2484
    _globals['_AUDIENCESIMPLEFILTER']._serialized_end = 2675
    _globals['_AUDIENCESEQUENCEFILTER']._serialized_start = 2678
    _globals['_AUDIENCESEQUENCEFILTER']._serialized_end = 3240
    _globals['_AUDIENCESEQUENCEFILTER_AUDIENCESEQUENCESTEP']._serialized_start = 2954
    _globals['_AUDIENCESEQUENCEFILTER_AUDIENCESEQUENCESTEP']._serialized_end = 3240
    _globals['_AUDIENCEFILTERCLAUSE']._serialized_start = 3243
    _globals['_AUDIENCEFILTERCLAUSE']._serialized_end = 3622
    _globals['_AUDIENCEFILTERCLAUSE_AUDIENCECLAUSETYPE']._serialized_start = 3528
    _globals['_AUDIENCEFILTERCLAUSE_AUDIENCECLAUSETYPE']._serialized_end = 3612
    _globals['_AUDIENCEEVENTTRIGGER']._serialized_start = 3625
    _globals['_AUDIENCEEVENTTRIGGER']._serialized_end = 3868
    _globals['_AUDIENCEEVENTTRIGGER_LOGCONDITION']._serialized_start = 3769
    _globals['_AUDIENCEEVENTTRIGGER_LOGCONDITION']._serialized_end = 3868
    _globals['_AUDIENCE']._serialized_start = 3871
    _globals['_AUDIENCE']._serialized_end = 4595
    _globals['_AUDIENCE_AUDIENCEEXCLUSIONDURATIONMODE']._serialized_start = 4375
    _globals['_AUDIENCE_AUDIENCEEXCLUSIONDURATIONMODE']._serialized_end = 4506