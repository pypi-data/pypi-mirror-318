"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_runtime_version.ValidateProtobufRuntimeVersion(_runtime_version.Domain.PUBLIC, 5, 28, 1, '', 'google/cloud/billing/budgets/v1beta1/budget_model.proto')
_sym_db = _symbol_database.Default()
from ......google.api import field_behavior_pb2 as google_dot_api_dot_field__behavior__pb2
from ......google.api import resource_pb2 as google_dot_api_dot_resource__pb2
from google.protobuf import struct_pb2 as google_dot_protobuf_dot_struct__pb2
from ......google.type import date_pb2 as google_dot_type_dot_date__pb2
from ......google.type import money_pb2 as google_dot_type_dot_money__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n7google/cloud/billing/budgets/v1beta1/budget_model.proto\x12$google.cloud.billing.budgets.v1beta1\x1a\x1fgoogle/api/field_behavior.proto\x1a\x19google/api/resource.proto\x1a\x1cgoogle/protobuf/struct.proto\x1a\x16google/type/date.proto\x1a\x17google/type/money.proto"\xde\x03\n\x06Budget\x12\x11\n\x04name\x18\x01 \x01(\tB\x03\xe0A\x03\x12\x14\n\x0cdisplay_name\x18\x02 \x01(\t\x12H\n\rbudget_filter\x18\x03 \x01(\x0b2,.google.cloud.billing.budgets.v1beta1.FilterB\x03\xe0A\x01\x12G\n\x06amount\x18\x04 \x01(\x0b22.google.cloud.billing.budgets.v1beta1.BudgetAmountB\x03\xe0A\x02\x12Q\n\x0fthreshold_rules\x18\x05 \x03(\x0b23.google.cloud.billing.budgets.v1beta1.ThresholdRuleB\x03\xe0A\x01\x12S\n\x10all_updates_rule\x18\x06 \x01(\x0b24.google.cloud.billing.budgets.v1beta1.AllUpdatesRuleB\x03\xe0A\x01\x12\x11\n\x04etag\x18\x07 \x01(\tB\x03\xe0A\x01:]\xeaAZ\n$billingbudgets.googleapis.com/Budget\x122billingAccounts/{billing_account}/budgets/{budget}"\xa5\x01\n\x0cBudgetAmount\x12.\n\x10specified_amount\x18\x01 \x01(\x0b2\x12.google.type.MoneyH\x00\x12T\n\x12last_period_amount\x18\x02 \x01(\x0b26.google.cloud.billing.budgets.v1beta1.LastPeriodAmountH\x00B\x0f\n\rbudget_amount"\x12\n\x10LastPeriodAmount"\xcd\x01\n\rThresholdRule\x12\x1e\n\x11threshold_percent\x18\x01 \x01(\x01B\x03\xe0A\x02\x12S\n\x0bspend_basis\x18\x02 \x01(\x0e29.google.cloud.billing.budgets.v1beta1.ThresholdRule.BasisB\x03\xe0A\x01"G\n\x05Basis\x12\x15\n\x11BASIS_UNSPECIFIED\x10\x00\x12\x11\n\rCURRENT_SPEND\x10\x01\x12\x14\n\x10FORECASTED_SPEND\x10\x02"\xd2\x01\n\x0eAllUpdatesRule\x12\x19\n\x0cpubsub_topic\x18\x01 \x01(\tB\x03\xe0A\x01\x12\x1b\n\x0eschema_version\x18\x02 \x01(\tB\x03\xe0A\x01\x12-\n monitoring_notification_channels\x18\x03 \x03(\tB\x03\xe0A\x01\x12+\n\x1edisable_default_iam_recipients\x18\x04 \x01(\x08B\x03\xe0A\x01\x12,\n\x1fenable_project_level_recipients\x18\x05 \x01(\x08B\x03\xe0A\x01"\xd8\x05\n\x06Filter\x12\x15\n\x08projects\x18\x01 \x03(\tB\x03\xe0A\x01\x12\x1f\n\x12resource_ancestors\x18\x02 \x03(\tB\x03\xe0A\x01\x12\x19\n\x0ccredit_types\x18\x07 \x03(\tB\x03\xe0A\x01\x12f\n\x16credit_types_treatment\x18\x04 \x01(\x0e2A.google.cloud.billing.budgets.v1beta1.Filter.CreditTypesTreatmentB\x03\xe0A\x01\x12\x15\n\x08services\x18\x03 \x03(\tB\x03\xe0A\x01\x12\x18\n\x0bsubaccounts\x18\x05 \x03(\tB\x03\xe0A\x01\x12M\n\x06labels\x18\x06 \x03(\x0b28.google.cloud.billing.budgets.v1beta1.Filter.LabelsEntryB\x03\xe0A\x01\x12T\n\x0fcalendar_period\x18\x08 \x01(\x0e24.google.cloud.billing.budgets.v1beta1.CalendarPeriodB\x03\xe0A\x01H\x00\x12P\n\rcustom_period\x18\t \x01(\x0b22.google.cloud.billing.budgets.v1beta1.CustomPeriodB\x03\xe0A\x01H\x00\x1aI\n\x0bLabelsEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12)\n\x05value\x18\x02 \x01(\x0b2\x1a.google.protobuf.ListValue:\x028\x01"\x8f\x01\n\x14CreditTypesTreatment\x12&\n"CREDIT_TYPES_TREATMENT_UNSPECIFIED\x10\x00\x12\x17\n\x13INCLUDE_ALL_CREDITS\x10\x01\x12\x17\n\x13EXCLUDE_ALL_CREDITS\x10\x02\x12\x1d\n\x19INCLUDE_SPECIFIED_CREDITS\x10\x03B\x0e\n\x0cusage_period"d\n\x0cCustomPeriod\x12*\n\nstart_date\x18\x01 \x01(\x0b2\x11.google.type.DateB\x03\xe0A\x02\x12(\n\x08end_date\x18\x02 \x01(\x0b2\x11.google.type.DateB\x03\xe0A\x01*S\n\x0eCalendarPeriod\x12\x1f\n\x1bCALENDAR_PERIOD_UNSPECIFIED\x10\x00\x12\t\n\x05MONTH\x10\x01\x12\x0b\n\x07QUARTER\x10\x02\x12\x08\n\x04YEAR\x10\x03Bp\n(com.google.cloud.billing.budgets.v1beta1P\x01ZBcloud.google.com/go/billing/budgets/apiv1beta1/budgetspb;budgetspbb\x06proto3')
_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'google.cloud.billing.budgets.v1beta1.budget_model_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
    _globals['DESCRIPTOR']._loaded_options = None
    _globals['DESCRIPTOR']._serialized_options = b'\n(com.google.cloud.billing.budgets.v1beta1P\x01ZBcloud.google.com/go/billing/budgets/apiv1beta1/budgetspb;budgetspb'
    _globals['_BUDGET'].fields_by_name['name']._loaded_options = None
    _globals['_BUDGET'].fields_by_name['name']._serialized_options = b'\xe0A\x03'
    _globals['_BUDGET'].fields_by_name['budget_filter']._loaded_options = None
    _globals['_BUDGET'].fields_by_name['budget_filter']._serialized_options = b'\xe0A\x01'
    _globals['_BUDGET'].fields_by_name['amount']._loaded_options = None
    _globals['_BUDGET'].fields_by_name['amount']._serialized_options = b'\xe0A\x02'
    _globals['_BUDGET'].fields_by_name['threshold_rules']._loaded_options = None
    _globals['_BUDGET'].fields_by_name['threshold_rules']._serialized_options = b'\xe0A\x01'
    _globals['_BUDGET'].fields_by_name['all_updates_rule']._loaded_options = None
    _globals['_BUDGET'].fields_by_name['all_updates_rule']._serialized_options = b'\xe0A\x01'
    _globals['_BUDGET'].fields_by_name['etag']._loaded_options = None
    _globals['_BUDGET'].fields_by_name['etag']._serialized_options = b'\xe0A\x01'
    _globals['_BUDGET']._loaded_options = None
    _globals['_BUDGET']._serialized_options = b'\xeaAZ\n$billingbudgets.googleapis.com/Budget\x122billingAccounts/{billing_account}/budgets/{budget}'
    _globals['_THRESHOLDRULE'].fields_by_name['threshold_percent']._loaded_options = None
    _globals['_THRESHOLDRULE'].fields_by_name['threshold_percent']._serialized_options = b'\xe0A\x02'
    _globals['_THRESHOLDRULE'].fields_by_name['spend_basis']._loaded_options = None
    _globals['_THRESHOLDRULE'].fields_by_name['spend_basis']._serialized_options = b'\xe0A\x01'
    _globals['_ALLUPDATESRULE'].fields_by_name['pubsub_topic']._loaded_options = None
    _globals['_ALLUPDATESRULE'].fields_by_name['pubsub_topic']._serialized_options = b'\xe0A\x01'
    _globals['_ALLUPDATESRULE'].fields_by_name['schema_version']._loaded_options = None
    _globals['_ALLUPDATESRULE'].fields_by_name['schema_version']._serialized_options = b'\xe0A\x01'
    _globals['_ALLUPDATESRULE'].fields_by_name['monitoring_notification_channels']._loaded_options = None
    _globals['_ALLUPDATESRULE'].fields_by_name['monitoring_notification_channels']._serialized_options = b'\xe0A\x01'
    _globals['_ALLUPDATESRULE'].fields_by_name['disable_default_iam_recipients']._loaded_options = None
    _globals['_ALLUPDATESRULE'].fields_by_name['disable_default_iam_recipients']._serialized_options = b'\xe0A\x01'
    _globals['_ALLUPDATESRULE'].fields_by_name['enable_project_level_recipients']._loaded_options = None
    _globals['_ALLUPDATESRULE'].fields_by_name['enable_project_level_recipients']._serialized_options = b'\xe0A\x01'
    _globals['_FILTER_LABELSENTRY']._loaded_options = None
    _globals['_FILTER_LABELSENTRY']._serialized_options = b'8\x01'
    _globals['_FILTER'].fields_by_name['projects']._loaded_options = None
    _globals['_FILTER'].fields_by_name['projects']._serialized_options = b'\xe0A\x01'
    _globals['_FILTER'].fields_by_name['resource_ancestors']._loaded_options = None
    _globals['_FILTER'].fields_by_name['resource_ancestors']._serialized_options = b'\xe0A\x01'
    _globals['_FILTER'].fields_by_name['credit_types']._loaded_options = None
    _globals['_FILTER'].fields_by_name['credit_types']._serialized_options = b'\xe0A\x01'
    _globals['_FILTER'].fields_by_name['credit_types_treatment']._loaded_options = None
    _globals['_FILTER'].fields_by_name['credit_types_treatment']._serialized_options = b'\xe0A\x01'
    _globals['_FILTER'].fields_by_name['services']._loaded_options = None
    _globals['_FILTER'].fields_by_name['services']._serialized_options = b'\xe0A\x01'
    _globals['_FILTER'].fields_by_name['subaccounts']._loaded_options = None
    _globals['_FILTER'].fields_by_name['subaccounts']._serialized_options = b'\xe0A\x01'
    _globals['_FILTER'].fields_by_name['labels']._loaded_options = None
    _globals['_FILTER'].fields_by_name['labels']._serialized_options = b'\xe0A\x01'
    _globals['_FILTER'].fields_by_name['calendar_period']._loaded_options = None
    _globals['_FILTER'].fields_by_name['calendar_period']._serialized_options = b'\xe0A\x01'
    _globals['_FILTER'].fields_by_name['custom_period']._loaded_options = None
    _globals['_FILTER'].fields_by_name['custom_period']._serialized_options = b'\xe0A\x01'
    _globals['_CUSTOMPERIOD'].fields_by_name['start_date']._loaded_options = None
    _globals['_CUSTOMPERIOD'].fields_by_name['start_date']._serialized_options = b'\xe0A\x02'
    _globals['_CUSTOMPERIOD'].fields_by_name['end_date']._loaded_options = None
    _globals['_CUSTOMPERIOD'].fields_by_name['end_date']._serialized_options = b'\xe0A\x01'
    _globals['_CALENDARPERIOD']._serialized_start = 2159
    _globals['_CALENDARPERIOD']._serialized_end = 2242
    _globals['_BUDGET']._serialized_start = 237
    _globals['_BUDGET']._serialized_end = 715
    _globals['_BUDGETAMOUNT']._serialized_start = 718
    _globals['_BUDGETAMOUNT']._serialized_end = 883
    _globals['_LASTPERIODAMOUNT']._serialized_start = 885
    _globals['_LASTPERIODAMOUNT']._serialized_end = 903
    _globals['_THRESHOLDRULE']._serialized_start = 906
    _globals['_THRESHOLDRULE']._serialized_end = 1111
    _globals['_THRESHOLDRULE_BASIS']._serialized_start = 1040
    _globals['_THRESHOLDRULE_BASIS']._serialized_end = 1111
    _globals['_ALLUPDATESRULE']._serialized_start = 1114
    _globals['_ALLUPDATESRULE']._serialized_end = 1324
    _globals['_FILTER']._serialized_start = 1327
    _globals['_FILTER']._serialized_end = 2055
    _globals['_FILTER_LABELSENTRY']._serialized_start = 1820
    _globals['_FILTER_LABELSENTRY']._serialized_end = 1893
    _globals['_FILTER_CREDITTYPESTREATMENT']._serialized_start = 1896
    _globals['_FILTER_CREDITTYPESTREATMENT']._serialized_end = 2039
    _globals['_CUSTOMPERIOD']._serialized_start = 2057
    _globals['_CUSTOMPERIOD']._serialized_end = 2157