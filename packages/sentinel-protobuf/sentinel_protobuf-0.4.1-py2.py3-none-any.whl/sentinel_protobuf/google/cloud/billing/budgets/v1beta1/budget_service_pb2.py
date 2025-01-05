"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_runtime_version.ValidateProtobufRuntimeVersion(_runtime_version.Domain.PUBLIC, 5, 28, 1, '', 'google/cloud/billing/budgets/v1beta1/budget_service.proto')
_sym_db = _symbol_database.Default()
from ......google.api import annotations_pb2 as google_dot_api_dot_annotations__pb2
from ......google.api import client_pb2 as google_dot_api_dot_client__pb2
from ......google.api import field_behavior_pb2 as google_dot_api_dot_field__behavior__pb2
from ......google.api import resource_pb2 as google_dot_api_dot_resource__pb2
from ......google.cloud.billing.budgets.v1beta1 import budget_model_pb2 as google_dot_cloud_dot_billing_dot_budgets_dot_v1beta1_dot_budget__model__pb2
from google.protobuf import empty_pb2 as google_dot_protobuf_dot_empty__pb2
from google.protobuf import field_mask_pb2 as google_dot_protobuf_dot_field__mask__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n9google/cloud/billing/budgets/v1beta1/budget_service.proto\x12$google.cloud.billing.budgets.v1beta1\x1a\x1cgoogle/api/annotations.proto\x1a\x17google/api/client.proto\x1a\x1fgoogle/api/field_behavior.proto\x1a\x19google/api/resource.proto\x1a7google/cloud/billing/budgets/v1beta1/budget_model.proto\x1a\x1bgoogle/protobuf/empty.proto\x1a google/protobuf/field_mask.proto"\x96\x01\n\x13CreateBudgetRequest\x12<\n\x06parent\x18\x01 \x01(\tB,\xe0A\x02\xfaA&\x12$billingbudgets.googleapis.com/Budget\x12A\n\x06budget\x18\x02 \x01(\x0b2,.google.cloud.billing.budgets.v1beta1.BudgetB\x03\xe0A\x02"\x8e\x01\n\x13UpdateBudgetRequest\x12A\n\x06budget\x18\x01 \x01(\x0b2,.google.cloud.billing.budgets.v1beta1.BudgetB\x03\xe0A\x02\x124\n\x0bupdate_mask\x18\x02 \x01(\x0b2\x1a.google.protobuf.FieldMaskB\x03\xe0A\x01"N\n\x10GetBudgetRequest\x12:\n\x04name\x18\x01 \x01(\tB,\xe0A\x02\xfaA&\n$billingbudgets.googleapis.com/Budget"\x97\x01\n\x12ListBudgetsRequest\x12<\n\x06parent\x18\x01 \x01(\tB,\xe0A\x02\xfaA&\x12$billingbudgets.googleapis.com/Budget\x12\x12\n\x05scope\x18\x04 \x01(\tB\x03\xe0A\x01\x12\x16\n\tpage_size\x18\x02 \x01(\x05B\x03\xe0A\x01\x12\x17\n\npage_token\x18\x03 \x01(\tB\x03\xe0A\x01"m\n\x13ListBudgetsResponse\x12=\n\x07budgets\x18\x01 \x03(\x0b2,.google.cloud.billing.budgets.v1beta1.Budget\x12\x17\n\x0fnext_page_token\x18\x02 \x01(\t"Q\n\x13DeleteBudgetRequest\x12:\n\x04name\x18\x01 \x01(\tB,\xe0A\x02\xfaA&\n$billingbudgets.googleapis.com/Budget2\xf7\x07\n\rBudgetService\x12\xaf\x01\n\x0cCreateBudget\x129.google.cloud.billing.budgets.v1beta1.CreateBudgetRequest\x1a,.google.cloud.billing.budgets.v1beta1.Budget"6\x82\xd3\xe4\x93\x020"+/v1beta1/{parent=billingAccounts/*}/budgets:\x01*\x12\xb6\x01\n\x0cUpdateBudget\x129.google.cloud.billing.budgets.v1beta1.UpdateBudgetRequest\x1a,.google.cloud.billing.budgets.v1beta1.Budget"=\x82\xd3\xe4\x93\x02722/v1beta1/{budget.name=billingAccounts/*/budgets/*}:\x01*\x12\xa6\x01\n\tGetBudget\x126.google.cloud.billing.budgets.v1beta1.GetBudgetRequest\x1a,.google.cloud.billing.budgets.v1beta1.Budget"3\x82\xd3\xe4\x93\x02-\x12+/v1beta1/{name=billingAccounts/*/budgets/*}\x12\xb7\x01\n\x0bListBudgets\x128.google.cloud.billing.budgets.v1beta1.ListBudgetsRequest\x1a9.google.cloud.billing.budgets.v1beta1.ListBudgetsResponse"3\x82\xd3\xe4\x93\x02-\x12+/v1beta1/{parent=billingAccounts/*}/budgets\x12\x96\x01\n\x0cDeleteBudget\x129.google.cloud.billing.budgets.v1beta1.DeleteBudgetRequest\x1a\x16.google.protobuf.Empty"3\x82\xd3\xe4\x93\x02-*+/v1beta1/{name=billingAccounts/*/budgets/*}\x1a\x7f\xcaA\x1dbillingbudgets.googleapis.com\xd2A\\https://www.googleapis.com/auth/cloud-billing,https://www.googleapis.com/auth/cloud-platformBp\n(com.google.cloud.billing.budgets.v1beta1P\x01ZBcloud.google.com/go/billing/budgets/apiv1beta1/budgetspb;budgetspbb\x06proto3')
_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'google.cloud.billing.budgets.v1beta1.budget_service_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
    _globals['DESCRIPTOR']._loaded_options = None
    _globals['DESCRIPTOR']._serialized_options = b'\n(com.google.cloud.billing.budgets.v1beta1P\x01ZBcloud.google.com/go/billing/budgets/apiv1beta1/budgetspb;budgetspb'
    _globals['_CREATEBUDGETREQUEST'].fields_by_name['parent']._loaded_options = None
    _globals['_CREATEBUDGETREQUEST'].fields_by_name['parent']._serialized_options = b'\xe0A\x02\xfaA&\x12$billingbudgets.googleapis.com/Budget'
    _globals['_CREATEBUDGETREQUEST'].fields_by_name['budget']._loaded_options = None
    _globals['_CREATEBUDGETREQUEST'].fields_by_name['budget']._serialized_options = b'\xe0A\x02'
    _globals['_UPDATEBUDGETREQUEST'].fields_by_name['budget']._loaded_options = None
    _globals['_UPDATEBUDGETREQUEST'].fields_by_name['budget']._serialized_options = b'\xe0A\x02'
    _globals['_UPDATEBUDGETREQUEST'].fields_by_name['update_mask']._loaded_options = None
    _globals['_UPDATEBUDGETREQUEST'].fields_by_name['update_mask']._serialized_options = b'\xe0A\x01'
    _globals['_GETBUDGETREQUEST'].fields_by_name['name']._loaded_options = None
    _globals['_GETBUDGETREQUEST'].fields_by_name['name']._serialized_options = b'\xe0A\x02\xfaA&\n$billingbudgets.googleapis.com/Budget'
    _globals['_LISTBUDGETSREQUEST'].fields_by_name['parent']._loaded_options = None
    _globals['_LISTBUDGETSREQUEST'].fields_by_name['parent']._serialized_options = b'\xe0A\x02\xfaA&\x12$billingbudgets.googleapis.com/Budget'
    _globals['_LISTBUDGETSREQUEST'].fields_by_name['scope']._loaded_options = None
    _globals['_LISTBUDGETSREQUEST'].fields_by_name['scope']._serialized_options = b'\xe0A\x01'
    _globals['_LISTBUDGETSREQUEST'].fields_by_name['page_size']._loaded_options = None
    _globals['_LISTBUDGETSREQUEST'].fields_by_name['page_size']._serialized_options = b'\xe0A\x01'
    _globals['_LISTBUDGETSREQUEST'].fields_by_name['page_token']._loaded_options = None
    _globals['_LISTBUDGETSREQUEST'].fields_by_name['page_token']._serialized_options = b'\xe0A\x01'
    _globals['_DELETEBUDGETREQUEST'].fields_by_name['name']._loaded_options = None
    _globals['_DELETEBUDGETREQUEST'].fields_by_name['name']._serialized_options = b'\xe0A\x02\xfaA&\n$billingbudgets.googleapis.com/Budget'
    _globals['_BUDGETSERVICE']._loaded_options = None
    _globals['_BUDGETSERVICE']._serialized_options = b'\xcaA\x1dbillingbudgets.googleapis.com\xd2A\\https://www.googleapis.com/auth/cloud-billing,https://www.googleapis.com/auth/cloud-platform'
    _globals['_BUDGETSERVICE'].methods_by_name['CreateBudget']._loaded_options = None
    _globals['_BUDGETSERVICE'].methods_by_name['CreateBudget']._serialized_options = b'\x82\xd3\xe4\x93\x020"+/v1beta1/{parent=billingAccounts/*}/budgets:\x01*'
    _globals['_BUDGETSERVICE'].methods_by_name['UpdateBudget']._loaded_options = None
    _globals['_BUDGETSERVICE'].methods_by_name['UpdateBudget']._serialized_options = b'\x82\xd3\xe4\x93\x02722/v1beta1/{budget.name=billingAccounts/*/budgets/*}:\x01*'
    _globals['_BUDGETSERVICE'].methods_by_name['GetBudget']._loaded_options = None
    _globals['_BUDGETSERVICE'].methods_by_name['GetBudget']._serialized_options = b'\x82\xd3\xe4\x93\x02-\x12+/v1beta1/{name=billingAccounts/*/budgets/*}'
    _globals['_BUDGETSERVICE'].methods_by_name['ListBudgets']._loaded_options = None
    _globals['_BUDGETSERVICE'].methods_by_name['ListBudgets']._serialized_options = b'\x82\xd3\xe4\x93\x02-\x12+/v1beta1/{parent=billingAccounts/*}/budgets'
    _globals['_BUDGETSERVICE'].methods_by_name['DeleteBudget']._loaded_options = None
    _globals['_BUDGETSERVICE'].methods_by_name['DeleteBudget']._serialized_options = b'\x82\xd3\xe4\x93\x02-*+/v1beta1/{name=billingAccounts/*/budgets/*}'
    _globals['_CREATEBUDGETREQUEST']._serialized_start = 335
    _globals['_CREATEBUDGETREQUEST']._serialized_end = 485
    _globals['_UPDATEBUDGETREQUEST']._serialized_start = 488
    _globals['_UPDATEBUDGETREQUEST']._serialized_end = 630
    _globals['_GETBUDGETREQUEST']._serialized_start = 632
    _globals['_GETBUDGETREQUEST']._serialized_end = 710
    _globals['_LISTBUDGETSREQUEST']._serialized_start = 713
    _globals['_LISTBUDGETSREQUEST']._serialized_end = 864
    _globals['_LISTBUDGETSRESPONSE']._serialized_start = 866
    _globals['_LISTBUDGETSRESPONSE']._serialized_end = 975
    _globals['_DELETEBUDGETREQUEST']._serialized_start = 977
    _globals['_DELETEBUDGETREQUEST']._serialized_end = 1058
    _globals['_BUDGETSERVICE']._serialized_start = 1061
    _globals['_BUDGETSERVICE']._serialized_end = 2076