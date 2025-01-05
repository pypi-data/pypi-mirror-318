"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_runtime_version.ValidateProtobufRuntimeVersion(_runtime_version.Domain.PUBLIC, 5, 28, 1, '', 'google/analytics/admin/v1alpha/expanded_data_set.proto')
_sym_db = _symbol_database.Default()
from .....google.api import field_behavior_pb2 as google_dot_api_dot_field__behavior__pb2
from .....google.api import resource_pb2 as google_dot_api_dot_resource__pb2
from google.protobuf import timestamp_pb2 as google_dot_protobuf_dot_timestamp__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n6google/analytics/admin/v1alpha/expanded_data_set.proto\x12\x1egoogle.analytics.admin.v1alpha\x1a\x1fgoogle/api/field_behavior.proto\x1a\x19google/api/resource.proto\x1a\x1fgoogle/protobuf/timestamp.proto"\xa6\x04\n\x15ExpandedDataSetFilter\x12[\n\rstring_filter\x18\x02 \x01(\x0b2B.google.analytics.admin.v1alpha.ExpandedDataSetFilter.StringFilterH\x00\x12\\\n\x0ein_list_filter\x18\x03 \x01(\x0b2B.google.analytics.admin.v1alpha.ExpandedDataSetFilter.InListFilterH\x00\x12\x17\n\nfield_name\x18\x01 \x01(\tB\x03\xe0A\x02\x1a\xe8\x01\n\x0cStringFilter\x12e\n\nmatch_type\x18\x01 \x01(\x0e2L.google.analytics.admin.v1alpha.ExpandedDataSetFilter.StringFilter.MatchTypeB\x03\xe0A\x02\x12\x12\n\x05value\x18\x02 \x01(\tB\x03\xe0A\x02\x12\x1b\n\x0ecase_sensitive\x18\x03 \x01(\x08B\x03\xe0A\x01"@\n\tMatchType\x12\x1a\n\x16MATCH_TYPE_UNSPECIFIED\x10\x00\x12\t\n\x05EXACT\x10\x01\x12\x0c\n\x08CONTAINS\x10\x02\x1a@\n\x0cInListFilter\x12\x13\n\x06values\x18\x01 \x03(\tB\x03\xe0A\x02\x12\x1b\n\x0ecase_sensitive\x18\x02 \x01(\x08B\x03\xe0A\x01B\x0c\n\none_filter"\xa7\x02\n\x1fExpandedDataSetFilterExpression\x12X\n\tand_group\x18\x01 \x01(\x0b2C.google.analytics.admin.v1alpha.ExpandedDataSetFilterExpressionListH\x00\x12Y\n\x0enot_expression\x18\x02 \x01(\x0b2?.google.analytics.admin.v1alpha.ExpandedDataSetFilterExpressionH\x00\x12G\n\x06filter\x18\x03 \x01(\x0b25.google.analytics.admin.v1alpha.ExpandedDataSetFilterH\x00B\x06\n\x04expr"\x82\x01\n#ExpandedDataSetFilterExpressionList\x12[\n\x12filter_expressions\x18\x01 \x03(\x0b2?.google.analytics.admin.v1alpha.ExpandedDataSetFilterExpression"\xb2\x03\n\x0fExpandedDataSet\x12\x11\n\x04name\x18\x01 \x01(\tB\x03\xe0A\x03\x12\x19\n\x0cdisplay_name\x18\x02 \x01(\tB\x03\xe0A\x02\x12\x18\n\x0bdescription\x18\x03 \x01(\tB\x03\xe0A\x01\x12\x1c\n\x0fdimension_names\x18\x04 \x03(\tB\x03\xe0A\x05\x12\x19\n\x0cmetric_names\x18\x05 \x03(\tB\x03\xe0A\x05\x12i\n\x1bdimension_filter_expression\x18\x06 \x01(\x0b2?.google.analytics.admin.v1alpha.ExpandedDataSetFilterExpressionB\x03\xe0A\x05\x12C\n\x1adata_collection_start_time\x18\x07 \x01(\x0b2\x1a.google.protobuf.TimestampB\x03\xe0A\x03:n\xeaAk\n-analyticsadmin.googleapis.com/ExpandedDataSet\x12:properties/{property}/expandedDataSets/{expanded_data_set}B|\n"com.google.analytics.admin.v1alphaB\x14ExpandedDataSetProtoP\x01Z>cloud.google.com/go/analytics/admin/apiv1alpha/adminpb;adminpbb\x06proto3')
_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'google.analytics.admin.v1alpha.expanded_data_set_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
    _globals['DESCRIPTOR']._loaded_options = None
    _globals['DESCRIPTOR']._serialized_options = b'\n"com.google.analytics.admin.v1alphaB\x14ExpandedDataSetProtoP\x01Z>cloud.google.com/go/analytics/admin/apiv1alpha/adminpb;adminpb'
    _globals['_EXPANDEDDATASETFILTER_STRINGFILTER'].fields_by_name['match_type']._loaded_options = None
    _globals['_EXPANDEDDATASETFILTER_STRINGFILTER'].fields_by_name['match_type']._serialized_options = b'\xe0A\x02'
    _globals['_EXPANDEDDATASETFILTER_STRINGFILTER'].fields_by_name['value']._loaded_options = None
    _globals['_EXPANDEDDATASETFILTER_STRINGFILTER'].fields_by_name['value']._serialized_options = b'\xe0A\x02'
    _globals['_EXPANDEDDATASETFILTER_STRINGFILTER'].fields_by_name['case_sensitive']._loaded_options = None
    _globals['_EXPANDEDDATASETFILTER_STRINGFILTER'].fields_by_name['case_sensitive']._serialized_options = b'\xe0A\x01'
    _globals['_EXPANDEDDATASETFILTER_INLISTFILTER'].fields_by_name['values']._loaded_options = None
    _globals['_EXPANDEDDATASETFILTER_INLISTFILTER'].fields_by_name['values']._serialized_options = b'\xe0A\x02'
    _globals['_EXPANDEDDATASETFILTER_INLISTFILTER'].fields_by_name['case_sensitive']._loaded_options = None
    _globals['_EXPANDEDDATASETFILTER_INLISTFILTER'].fields_by_name['case_sensitive']._serialized_options = b'\xe0A\x01'
    _globals['_EXPANDEDDATASETFILTER'].fields_by_name['field_name']._loaded_options = None
    _globals['_EXPANDEDDATASETFILTER'].fields_by_name['field_name']._serialized_options = b'\xe0A\x02'
    _globals['_EXPANDEDDATASET'].fields_by_name['name']._loaded_options = None
    _globals['_EXPANDEDDATASET'].fields_by_name['name']._serialized_options = b'\xe0A\x03'
    _globals['_EXPANDEDDATASET'].fields_by_name['display_name']._loaded_options = None
    _globals['_EXPANDEDDATASET'].fields_by_name['display_name']._serialized_options = b'\xe0A\x02'
    _globals['_EXPANDEDDATASET'].fields_by_name['description']._loaded_options = None
    _globals['_EXPANDEDDATASET'].fields_by_name['description']._serialized_options = b'\xe0A\x01'
    _globals['_EXPANDEDDATASET'].fields_by_name['dimension_names']._loaded_options = None
    _globals['_EXPANDEDDATASET'].fields_by_name['dimension_names']._serialized_options = b'\xe0A\x05'
    _globals['_EXPANDEDDATASET'].fields_by_name['metric_names']._loaded_options = None
    _globals['_EXPANDEDDATASET'].fields_by_name['metric_names']._serialized_options = b'\xe0A\x05'
    _globals['_EXPANDEDDATASET'].fields_by_name['dimension_filter_expression']._loaded_options = None
    _globals['_EXPANDEDDATASET'].fields_by_name['dimension_filter_expression']._serialized_options = b'\xe0A\x05'
    _globals['_EXPANDEDDATASET'].fields_by_name['data_collection_start_time']._loaded_options = None
    _globals['_EXPANDEDDATASET'].fields_by_name['data_collection_start_time']._serialized_options = b'\xe0A\x03'
    _globals['_EXPANDEDDATASET']._loaded_options = None
    _globals['_EXPANDEDDATASET']._serialized_options = b'\xeaAk\n-analyticsadmin.googleapis.com/ExpandedDataSet\x12:properties/{property}/expandedDataSets/{expanded_data_set}'
    _globals['_EXPANDEDDATASETFILTER']._serialized_start = 184
    _globals['_EXPANDEDDATASETFILTER']._serialized_end = 734
    _globals['_EXPANDEDDATASETFILTER_STRINGFILTER']._serialized_start = 422
    _globals['_EXPANDEDDATASETFILTER_STRINGFILTER']._serialized_end = 654
    _globals['_EXPANDEDDATASETFILTER_STRINGFILTER_MATCHTYPE']._serialized_start = 590
    _globals['_EXPANDEDDATASETFILTER_STRINGFILTER_MATCHTYPE']._serialized_end = 654
    _globals['_EXPANDEDDATASETFILTER_INLISTFILTER']._serialized_start = 656
    _globals['_EXPANDEDDATASETFILTER_INLISTFILTER']._serialized_end = 720
    _globals['_EXPANDEDDATASETFILTEREXPRESSION']._serialized_start = 737
    _globals['_EXPANDEDDATASETFILTEREXPRESSION']._serialized_end = 1032
    _globals['_EXPANDEDDATASETFILTEREXPRESSIONLIST']._serialized_start = 1035
    _globals['_EXPANDEDDATASETFILTEREXPRESSIONLIST']._serialized_end = 1165
    _globals['_EXPANDEDDATASET']._serialized_start = 1168
    _globals['_EXPANDEDDATASET']._serialized_end = 1602