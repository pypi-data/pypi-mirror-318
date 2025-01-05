"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_runtime_version.ValidateProtobufRuntimeVersion(_runtime_version.Domain.PUBLIC, 5, 28, 1, '', 'google/analytics/admin/v1alpha/event_create_and_edit.proto')
_sym_db = _symbol_database.Default()
from .....google.api import field_behavior_pb2 as google_dot_api_dot_field__behavior__pb2
from .....google.api import resource_pb2 as google_dot_api_dot_resource__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n:google/analytics/admin/v1alpha/event_create_and_edit.proto\x12\x1egoogle.analytics.admin.v1alpha\x1a\x1fgoogle/api/field_behavior.proto\x1a\x19google/api/resource.proto"I\n\x11ParameterMutation\x12\x16\n\tparameter\x18\x01 \x01(\tB\x03\xe0A\x02\x12\x1c\n\x0fparameter_value\x18\x02 \x01(\tB\x03\xe0A\x02"\x92\x03\n\x0fEventCreateRule\x12\x11\n\x04name\x18\x01 \x01(\tB\x03\xe0A\x03\x12\x1e\n\x11destination_event\x18\x02 \x01(\tB\x03\xe0A\x02\x12P\n\x10event_conditions\x18\x03 \x03(\x0b21.google.analytics.admin.v1alpha.MatchingConditionB\x03\xe0A\x02\x12\x1e\n\x16source_copy_parameters\x18\x04 \x01(\x08\x12N\n\x13parameter_mutations\x18\x05 \x03(\x0b21.google.analytics.admin.v1alpha.ParameterMutation:\x89\x01\xeaA\x85\x01\n-analyticsadmin.googleapis.com/EventCreateRule\x12Tproperties/{property}/dataStreams/{data_stream}/eventCreateRules/{event_create_rule}"\xa8\x03\n\rEventEditRule\x12\x11\n\x04name\x18\x01 \x01(\tB\x03\xe0A\x08\x12\x19\n\x0cdisplay_name\x18\x02 \x01(\tB\x03\xe0A\x02\x12P\n\x10event_conditions\x18\x03 \x03(\x0b21.google.analytics.admin.v1alpha.MatchingConditionB\x03\xe0A\x02\x12S\n\x13parameter_mutations\x18\x04 \x03(\x0b21.google.analytics.admin.v1alpha.ParameterMutationB\x03\xe0A\x02\x12\x1d\n\x10processing_order\x18\x05 \x01(\x03B\x03\xe0A\x03:\xa2\x01\xeaA\x9e\x01\n+analyticsadmin.googleapis.com/EventEditRule\x12Pproperties/{property}/dataStreams/{data_stream}/eventEditRules/{event_edit_rule}*\x0eeventEditRules2\reventEditRule"\xad\x04\n\x11MatchingCondition\x12\x12\n\x05field\x18\x01 \x01(\tB\x03\xe0A\x02\x12^\n\x0fcomparison_type\x18\x02 \x01(\x0e2@.google.analytics.admin.v1alpha.MatchingCondition.ComparisonTypeB\x03\xe0A\x02\x12\x12\n\x05value\x18\x03 \x01(\tB\x03\xe0A\x02\x12\x0f\n\x07negated\x18\x04 \x01(\x08"\xfe\x02\n\x0eComparisonType\x12\x1f\n\x1bCOMPARISON_TYPE_UNSPECIFIED\x10\x00\x12\n\n\x06EQUALS\x10\x01\x12\x1b\n\x17EQUALS_CASE_INSENSITIVE\x10\x02\x12\x0c\n\x08CONTAINS\x10\x03\x12\x1d\n\x19CONTAINS_CASE_INSENSITIVE\x10\x04\x12\x0f\n\x0bSTARTS_WITH\x10\x05\x12 \n\x1cSTARTS_WITH_CASE_INSENSITIVE\x10\x06\x12\r\n\tENDS_WITH\x10\x07\x12\x1e\n\x1aENDS_WITH_CASE_INSENSITIVE\x10\x08\x12\x10\n\x0cGREATER_THAN\x10\t\x12\x19\n\x15GREATER_THAN_OR_EQUAL\x10\n\x12\r\n\tLESS_THAN\x10\x0b\x12\x16\n\x12LESS_THAN_OR_EQUAL\x10\x0c\x12\x16\n\x12REGULAR_EXPRESSION\x10\r\x12\'\n#REGULAR_EXPRESSION_CASE_INSENSITIVE\x10\x0eBf\n"com.google.analytics.admin.v1alphaP\x01Z>cloud.google.com/go/analytics/admin/apiv1alpha/adminpb;adminpbb\x06proto3')
_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'google.analytics.admin.v1alpha.event_create_and_edit_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
    _globals['DESCRIPTOR']._loaded_options = None
    _globals['DESCRIPTOR']._serialized_options = b'\n"com.google.analytics.admin.v1alphaP\x01Z>cloud.google.com/go/analytics/admin/apiv1alpha/adminpb;adminpb'
    _globals['_PARAMETERMUTATION'].fields_by_name['parameter']._loaded_options = None
    _globals['_PARAMETERMUTATION'].fields_by_name['parameter']._serialized_options = b'\xe0A\x02'
    _globals['_PARAMETERMUTATION'].fields_by_name['parameter_value']._loaded_options = None
    _globals['_PARAMETERMUTATION'].fields_by_name['parameter_value']._serialized_options = b'\xe0A\x02'
    _globals['_EVENTCREATERULE'].fields_by_name['name']._loaded_options = None
    _globals['_EVENTCREATERULE'].fields_by_name['name']._serialized_options = b'\xe0A\x03'
    _globals['_EVENTCREATERULE'].fields_by_name['destination_event']._loaded_options = None
    _globals['_EVENTCREATERULE'].fields_by_name['destination_event']._serialized_options = b'\xe0A\x02'
    _globals['_EVENTCREATERULE'].fields_by_name['event_conditions']._loaded_options = None
    _globals['_EVENTCREATERULE'].fields_by_name['event_conditions']._serialized_options = b'\xe0A\x02'
    _globals['_EVENTCREATERULE']._loaded_options = None
    _globals['_EVENTCREATERULE']._serialized_options = b'\xeaA\x85\x01\n-analyticsadmin.googleapis.com/EventCreateRule\x12Tproperties/{property}/dataStreams/{data_stream}/eventCreateRules/{event_create_rule}'
    _globals['_EVENTEDITRULE'].fields_by_name['name']._loaded_options = None
    _globals['_EVENTEDITRULE'].fields_by_name['name']._serialized_options = b'\xe0A\x08'
    _globals['_EVENTEDITRULE'].fields_by_name['display_name']._loaded_options = None
    _globals['_EVENTEDITRULE'].fields_by_name['display_name']._serialized_options = b'\xe0A\x02'
    _globals['_EVENTEDITRULE'].fields_by_name['event_conditions']._loaded_options = None
    _globals['_EVENTEDITRULE'].fields_by_name['event_conditions']._serialized_options = b'\xe0A\x02'
    _globals['_EVENTEDITRULE'].fields_by_name['parameter_mutations']._loaded_options = None
    _globals['_EVENTEDITRULE'].fields_by_name['parameter_mutations']._serialized_options = b'\xe0A\x02'
    _globals['_EVENTEDITRULE'].fields_by_name['processing_order']._loaded_options = None
    _globals['_EVENTEDITRULE'].fields_by_name['processing_order']._serialized_options = b'\xe0A\x03'
    _globals['_EVENTEDITRULE']._loaded_options = None
    _globals['_EVENTEDITRULE']._serialized_options = b'\xeaA\x9e\x01\n+analyticsadmin.googleapis.com/EventEditRule\x12Pproperties/{property}/dataStreams/{data_stream}/eventEditRules/{event_edit_rule}*\x0eeventEditRules2\reventEditRule'
    _globals['_MATCHINGCONDITION'].fields_by_name['field']._loaded_options = None
    _globals['_MATCHINGCONDITION'].fields_by_name['field']._serialized_options = b'\xe0A\x02'
    _globals['_MATCHINGCONDITION'].fields_by_name['comparison_type']._loaded_options = None
    _globals['_MATCHINGCONDITION'].fields_by_name['comparison_type']._serialized_options = b'\xe0A\x02'
    _globals['_MATCHINGCONDITION'].fields_by_name['value']._loaded_options = None
    _globals['_MATCHINGCONDITION'].fields_by_name['value']._serialized_options = b'\xe0A\x02'
    _globals['_PARAMETERMUTATION']._serialized_start = 154
    _globals['_PARAMETERMUTATION']._serialized_end = 227
    _globals['_EVENTCREATERULE']._serialized_start = 230
    _globals['_EVENTCREATERULE']._serialized_end = 632
    _globals['_EVENTEDITRULE']._serialized_start = 635
    _globals['_EVENTEDITRULE']._serialized_end = 1059
    _globals['_MATCHINGCONDITION']._serialized_start = 1062
    _globals['_MATCHINGCONDITION']._serialized_end = 1619
    _globals['_MATCHINGCONDITION_COMPARISONTYPE']._serialized_start = 1237
    _globals['_MATCHINGCONDITION_COMPARISONTYPE']._serialized_end = 1619