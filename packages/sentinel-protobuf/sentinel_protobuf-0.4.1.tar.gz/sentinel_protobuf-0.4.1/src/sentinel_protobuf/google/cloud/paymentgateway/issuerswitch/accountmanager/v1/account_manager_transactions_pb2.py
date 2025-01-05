"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_runtime_version.ValidateProtobufRuntimeVersion(_runtime_version.Domain.PUBLIC, 5, 28, 1, '', 'google/cloud/paymentgateway/issuerswitch/accountmanager/v1/account_manager_transactions.proto')
_sym_db = _symbol_database.Default()
from .......google.api import annotations_pb2 as google_dot_api_dot_annotations__pb2
from .......google.api import client_pb2 as google_dot_api_dot_client__pb2
from .......google.api import field_behavior_pb2 as google_dot_api_dot_field__behavior__pb2
from .......google.api import resource_pb2 as google_dot_api_dot_resource__pb2
from .......google.cloud.paymentgateway.issuerswitch.v1 import common_fields_pb2 as google_dot_cloud_dot_paymentgateway_dot_issuerswitch_dot_v1_dot_common__fields__pb2
from .......google.longrunning import operations_pb2 as google_dot_longrunning_dot_operations__pb2
from google.protobuf import timestamp_pb2 as google_dot_protobuf_dot_timestamp__pb2
from .......google.type import money_pb2 as google_dot_type_dot_money__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n]google/cloud/paymentgateway/issuerswitch/accountmanager/v1/account_manager_transactions.proto\x12:google.cloud.paymentgateway.issuerswitch.accountmanager.v1\x1a\x1cgoogle/api/annotations.proto\x1a\x17google/api/client.proto\x1a\x1fgoogle/api/field_behavior.proto\x1a\x19google/api/resource.proto\x1a?google/cloud/paymentgateway/issuerswitch/v1/common_fields.proto\x1a#google/longrunning/operations.proto\x1a\x1fgoogle/protobuf/timestamp.proto\x1a\x17google/type/money.proto"\xf7\x05\n\x19AccountManagerTransaction\x12\x0c\n\x04name\x18\x01 \x01(\t\x12\x12\n\naccount_id\x18\x02 \x01(\t\x12g\n\x04info\x18\x03 \x01(\x0b2Y.google.cloud.paymentgateway.issuerswitch.accountmanager.v1.AccountManagerTransactionInfo\x12n\n\x05payer\x18\x04 \x01(\x0b2_.google.cloud.paymentgateway.issuerswitch.accountmanager.v1.AccountManagerSettlementParticipant\x12n\n\x05payee\x18\x05 \x01(\x0b2_.google.cloud.paymentgateway.issuerswitch.accountmanager.v1.AccountManagerSettlementParticipant\x12\x84\x01\n\x13reconciliation_info\x18\x06 \x01(\x0b2g.google.cloud.paymentgateway.issuerswitch.accountmanager.v1.AccountManagerTransactionReconciliationInfo\x12"\n\x06amount\x18\x07 \x01(\x0b2\x12.google.type.Money:\xc3\x01\xeaA\xbf\x01\n5issuerswitch.googleapis.com/AccountManagerTransaction\x12Oprojects/{project}/accountManagers/{account_manager}/transactions/{transaction}*\x1aaccountManagerTransactions2\x19accountManagerTransaction"\xf7\x07\n\x1dAccountManagerTransactionInfo\x12\n\n\x02id\x18\x01 \x01(\t\x12s\n\x10transaction_type\x18\x03 \x01(\x0e2Y.google.cloud.paymentgateway.issuerswitch.accountmanager.v1.AccountManagerTransactionType\x12s\n\x05state\x18\x05 \x01(\x0e2_.google.cloud.paymentgateway.issuerswitch.accountmanager.v1.AccountManagerTransactionInfo.StateB\x03\xe0A\x03\x12\x8d\x01\n\x08metadata\x18\x06 \x01(\x0b2{.google.cloud.paymentgateway.issuerswitch.accountmanager.v1.AccountManagerTransactionInfo.AccountManagerTransactionMetadata\x12\x9b\x01\n\rerror_details\x18\x07 \x01(\x0b2\x7f.google.cloud.paymentgateway.issuerswitch.accountmanager.v1.AccountManagerTransactionInfo.AccountManagerTransactionErrorDetailsB\x03\xe0A\x03\x1a\x98\x02\n!AccountManagerTransactionMetadata\x124\n\x10transaction_time\x18\x01 \x01(\x0b2\x1a.google.protobuf.Timestamp\x124\n\x0bcreate_time\x18\x02 \x01(\x0b2\x1a.google.protobuf.TimestampB\x03\xe0A\x03\x124\n\x0bupdate_time\x18\x03 \x01(\x0b2\x1a.google.protobuf.TimestampB\x03\xe0A\x03\x12"\n\x1aretrieval_reference_number\x18\x04 \x01(\t\x12\x17\n\x0finitiation_mode\x18\x05 \x01(\t\x12\x14\n\x0cpurpose_code\x18\x06 \x01(\t\x1a\\\n%AccountManagerTransactionErrorDetails\x12\x17\n\nerror_code\x18\x01 \x01(\tB\x03\xe0A\x03\x12\x1a\n\rerror_message\x18\x02 \x01(\tB\x03\xe0A\x03"9\n\x05State\x12\x15\n\x11STATE_UNSPECIFIED\x10\x00\x12\r\n\tSUCCEEDED\x10\x01\x12\n\n\x06FAILED\x10\x02"\x80\x02\n#AccountManagerSettlementParticipant\x12j\n\x0bparticipant\x18\x01 \x01(\x0b2U.google.cloud.paymentgateway.issuerswitch.accountmanager.v1.AccountManagerParticipant\x12m\n\rmerchant_info\x18\x02 \x01(\x0b2V.google.cloud.paymentgateway.issuerswitch.accountmanager.v1.AccountManagerMerchantInfo"\xb0\x02\n\x19AccountManagerParticipant\x12\x17\n\x0fpayment_address\x18\x01 \x01(\t\x12n\n\x07persona\x18\x02 \x01(\x0e2].google.cloud.paymentgateway.issuerswitch.accountmanager.v1.AccountManagerParticipant.Persona\x12N\n\x07account\x18\x03 \x01(\x0b2=.google.cloud.paymentgateway.issuerswitch.v1.AccountReference":\n\x07Persona\x12\x17\n\x13PERSONA_UNSPECIFIED\x10\x00\x12\n\n\x06ENTITY\x10\x01\x12\n\n\x06PERSON\x10\x02"?\n\x1aAccountManagerMerchantInfo\x12\x15\n\rcategory_code\x18\x01 \x01(\t\x12\n\n\x02id\x18\x02 \x01(\t"\xd0\x02\n+AccountManagerTransactionReconciliationInfo\x12\x8f\x01\n\x05state\x18\x01 \x01(\x0e2{.google.cloud.paymentgateway.issuerswitch.accountmanager.v1.AccountManagerTransactionReconciliationInfo.ReconciliationStateB\x03\xe0A\x03\x127\n\x13reconciliation_time\x18\x02 \x01(\x0b2\x1a.google.protobuf.Timestamp"V\n\x13ReconciliationState\x12$\n RECONCILIATION_STATE_UNSPECIFIED\x10\x00\x12\r\n\tSUCCEEDED\x10\x01\x12\n\n\x06FAILED\x10\x02"\xa0\x02\n\'ExportAccountManagerTransactionsRequest\x12\x13\n\x06parent\x18\x01 \x01(\tB\x03\xe0A\x02\x12x\n\x10transaction_type\x18\x03 \x01(\x0e2Y.google.cloud.paymentgateway.issuerswitch.accountmanager.v1.AccountManagerTransactionTypeB\x03\xe0A\x01\x123\n\nstart_time\x18\x04 \x01(\x0b2\x1a.google.protobuf.TimestampB\x03\xe0A\x01\x121\n\x08end_time\x18\x05 \x01(\x0b2\x1a.google.protobuf.TimestampB\x03\xe0A\x01"\xbc\x01\n%ListAccountManagerTransactionsRequest\x12M\n\x06parent\x18\x01 \x01(\tB=\xe0A\x02\xfaA7\x125issuerswitch.googleapis.com/AccountManagerTransaction\x12\x16\n\tpage_size\x18\x03 \x01(\x05B\x03\xe0A\x01\x12\x17\n\npage_token\x18\x04 \x01(\tB\x03\xe0A\x01\x12\x13\n\x06filter\x18\x05 \x01(\tB\x03\xe0A\x01"\xbe\x01\n&ListAccountManagerTransactionsResponse\x12{\n\x1caccount_manager_transactions\x18\x01 \x03(\x0b2U.google.cloud.paymentgateway.issuerswitch.accountmanager.v1.AccountManagerTransaction\x12\x17\n\x0fnext_page_token\x18\x02 \x01(\t"\x9d\x01\n*ReconcileAccountManagerTransactionsRequest\x12o\n\x0btransaction\x18\x01 \x01(\x0b2U.google.cloud.paymentgateway.issuerswitch.accountmanager.v1.AccountManagerTransactionB\x03\xe0A\x02"\xc5\x01\n/BatchReconcileAccountManagerTransactionsRequest\x12\x13\n\x06parent\x18\x01 \x01(\tB\x03\xe0A\x02\x12}\n\x08requests\x18\x02 \x03(\x0b2f.google.cloud.paymentgateway.issuerswitch.accountmanager.v1.ReconcileAccountManagerTransactionsRequestB\x03\xe0A\x02"\xaf\x01\n0BatchReconcileAccountManagerTransactionsResponse\x12{\n\x1caccount_manager_transactions\x18\x01 \x03(\x0b2U.google.cloud.paymentgateway.issuerswitch.accountmanager.v1.AccountManagerTransaction*\x91\x01\n\x1dAccountManagerTransactionType\x120\n,ACCOUNT_MANAGER_TRANSACTION_TYPE_UNSPECIFIED\x10\x00\x12\n\n\x06CREDIT\x10\x01\x12\x13\n\x0fCREDIT_REVERSAL\x10\x02\x12\t\n\x05DEBIT\x10\x03\x12\x12\n\x0eDEBIT_REVERSAL\x10\x042\xd7\x08\n\x1aAccountManagerTransactions\x12\xc8\x02\n ExportAccountManagerTransactions\x12c.google.cloud.paymentgateway.issuerswitch.accountmanager.v1.ExportAccountManagerTransactionsRequest\x1a\x1d.google.longrunning.Operation"\x9f\x01\xcaAT\n(ExportAccountManagerTransactionsResponse\x12(ExportAccountManagerTransactionsMetadata\x82\xd3\xe4\x93\x02B"=/v1/{parent=projects/*/accountManagers/*}/transactions:export:\x01*\x12\xb0\x02\n\x1eListAccountManagerTransactions\x12a.google.cloud.paymentgateway.issuerswitch.accountmanager.v1.ListAccountManagerTransactionsRequest\x1ab.google.cloud.paymentgateway.issuerswitch.accountmanager.v1.ListAccountManagerTransactionsResponse"G\xdaA\x06parent\x82\xd3\xe4\x93\x028\x126/v1/{parent=projects/*/accountManagers/*}/transactions\x12\xe9\x02\n(BatchReconcileAccountManagerTransactions\x12k.google.cloud.paymentgateway.issuerswitch.accountmanager.v1.BatchReconcileAccountManagerTransactionsRequest\x1al.google.cloud.paymentgateway.issuerswitch.accountmanager.v1.BatchReconcileAccountManagerTransactionsResponse"b\xdaA\x0fparent,requests\x82\xd3\xe4\x93\x02J"E/v1/{parent=projects/*/accountManagers/*}/transactions:batchReconcile:\x01*\x1aO\xcaA\x1bissuerswitch.googleapis.com\xd2A.https://www.googleapis.com/auth/cloud-platformB\x87\x03\n>com.google.cloud.paymentgateway.issuerswitch.accountmanager.v1B\x1fAccountManagerTransactionsProtoP\x01Zfcloud.google.com/go/paymentgateway/issuerswitch/accountmanager/apiv1/accountmanagerpb;accountmanagerpb\xaa\x02:Google.Cloud.PaymentGateway.IssuerSwitch.AccountManager.V1\xca\x02:Google\\Cloud\\PaymentGateway\\IssuerSwitch\\AccountManager\\V1\xea\x02?Google::Cloud::PaymentGateway::IssuerSwitch::AccountManager::V1b\x06proto3')
_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'google.cloud.paymentgateway.issuerswitch.accountmanager.v1.account_manager_transactions_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
    _globals['DESCRIPTOR']._loaded_options = None
    _globals['DESCRIPTOR']._serialized_options = b'\n>com.google.cloud.paymentgateway.issuerswitch.accountmanager.v1B\x1fAccountManagerTransactionsProtoP\x01Zfcloud.google.com/go/paymentgateway/issuerswitch/accountmanager/apiv1/accountmanagerpb;accountmanagerpb\xaa\x02:Google.Cloud.PaymentGateway.IssuerSwitch.AccountManager.V1\xca\x02:Google\\Cloud\\PaymentGateway\\IssuerSwitch\\AccountManager\\V1\xea\x02?Google::Cloud::PaymentGateway::IssuerSwitch::AccountManager::V1'
    _globals['_ACCOUNTMANAGERTRANSACTION']._loaded_options = None
    _globals['_ACCOUNTMANAGERTRANSACTION']._serialized_options = b'\xeaA\xbf\x01\n5issuerswitch.googleapis.com/AccountManagerTransaction\x12Oprojects/{project}/accountManagers/{account_manager}/transactions/{transaction}*\x1aaccountManagerTransactions2\x19accountManagerTransaction'
    _globals['_ACCOUNTMANAGERTRANSACTIONINFO_ACCOUNTMANAGERTRANSACTIONMETADATA'].fields_by_name['create_time']._loaded_options = None
    _globals['_ACCOUNTMANAGERTRANSACTIONINFO_ACCOUNTMANAGERTRANSACTIONMETADATA'].fields_by_name['create_time']._serialized_options = b'\xe0A\x03'
    _globals['_ACCOUNTMANAGERTRANSACTIONINFO_ACCOUNTMANAGERTRANSACTIONMETADATA'].fields_by_name['update_time']._loaded_options = None
    _globals['_ACCOUNTMANAGERTRANSACTIONINFO_ACCOUNTMANAGERTRANSACTIONMETADATA'].fields_by_name['update_time']._serialized_options = b'\xe0A\x03'
    _globals['_ACCOUNTMANAGERTRANSACTIONINFO_ACCOUNTMANAGERTRANSACTIONERRORDETAILS'].fields_by_name['error_code']._loaded_options = None
    _globals['_ACCOUNTMANAGERTRANSACTIONINFO_ACCOUNTMANAGERTRANSACTIONERRORDETAILS'].fields_by_name['error_code']._serialized_options = b'\xe0A\x03'
    _globals['_ACCOUNTMANAGERTRANSACTIONINFO_ACCOUNTMANAGERTRANSACTIONERRORDETAILS'].fields_by_name['error_message']._loaded_options = None
    _globals['_ACCOUNTMANAGERTRANSACTIONINFO_ACCOUNTMANAGERTRANSACTIONERRORDETAILS'].fields_by_name['error_message']._serialized_options = b'\xe0A\x03'
    _globals['_ACCOUNTMANAGERTRANSACTIONINFO'].fields_by_name['state']._loaded_options = None
    _globals['_ACCOUNTMANAGERTRANSACTIONINFO'].fields_by_name['state']._serialized_options = b'\xe0A\x03'
    _globals['_ACCOUNTMANAGERTRANSACTIONINFO'].fields_by_name['error_details']._loaded_options = None
    _globals['_ACCOUNTMANAGERTRANSACTIONINFO'].fields_by_name['error_details']._serialized_options = b'\xe0A\x03'
    _globals['_ACCOUNTMANAGERTRANSACTIONRECONCILIATIONINFO'].fields_by_name['state']._loaded_options = None
    _globals['_ACCOUNTMANAGERTRANSACTIONRECONCILIATIONINFO'].fields_by_name['state']._serialized_options = b'\xe0A\x03'
    _globals['_EXPORTACCOUNTMANAGERTRANSACTIONSREQUEST'].fields_by_name['parent']._loaded_options = None
    _globals['_EXPORTACCOUNTMANAGERTRANSACTIONSREQUEST'].fields_by_name['parent']._serialized_options = b'\xe0A\x02'
    _globals['_EXPORTACCOUNTMANAGERTRANSACTIONSREQUEST'].fields_by_name['transaction_type']._loaded_options = None
    _globals['_EXPORTACCOUNTMANAGERTRANSACTIONSREQUEST'].fields_by_name['transaction_type']._serialized_options = b'\xe0A\x01'
    _globals['_EXPORTACCOUNTMANAGERTRANSACTIONSREQUEST'].fields_by_name['start_time']._loaded_options = None
    _globals['_EXPORTACCOUNTMANAGERTRANSACTIONSREQUEST'].fields_by_name['start_time']._serialized_options = b'\xe0A\x01'
    _globals['_EXPORTACCOUNTMANAGERTRANSACTIONSREQUEST'].fields_by_name['end_time']._loaded_options = None
    _globals['_EXPORTACCOUNTMANAGERTRANSACTIONSREQUEST'].fields_by_name['end_time']._serialized_options = b'\xe0A\x01'
    _globals['_LISTACCOUNTMANAGERTRANSACTIONSREQUEST'].fields_by_name['parent']._loaded_options = None
    _globals['_LISTACCOUNTMANAGERTRANSACTIONSREQUEST'].fields_by_name['parent']._serialized_options = b'\xe0A\x02\xfaA7\x125issuerswitch.googleapis.com/AccountManagerTransaction'
    _globals['_LISTACCOUNTMANAGERTRANSACTIONSREQUEST'].fields_by_name['page_size']._loaded_options = None
    _globals['_LISTACCOUNTMANAGERTRANSACTIONSREQUEST'].fields_by_name['page_size']._serialized_options = b'\xe0A\x01'
    _globals['_LISTACCOUNTMANAGERTRANSACTIONSREQUEST'].fields_by_name['page_token']._loaded_options = None
    _globals['_LISTACCOUNTMANAGERTRANSACTIONSREQUEST'].fields_by_name['page_token']._serialized_options = b'\xe0A\x01'
    _globals['_LISTACCOUNTMANAGERTRANSACTIONSREQUEST'].fields_by_name['filter']._loaded_options = None
    _globals['_LISTACCOUNTMANAGERTRANSACTIONSREQUEST'].fields_by_name['filter']._serialized_options = b'\xe0A\x01'
    _globals['_RECONCILEACCOUNTMANAGERTRANSACTIONSREQUEST'].fields_by_name['transaction']._loaded_options = None
    _globals['_RECONCILEACCOUNTMANAGERTRANSACTIONSREQUEST'].fields_by_name['transaction']._serialized_options = b'\xe0A\x02'
    _globals['_BATCHRECONCILEACCOUNTMANAGERTRANSACTIONSREQUEST'].fields_by_name['parent']._loaded_options = None
    _globals['_BATCHRECONCILEACCOUNTMANAGERTRANSACTIONSREQUEST'].fields_by_name['parent']._serialized_options = b'\xe0A\x02'
    _globals['_BATCHRECONCILEACCOUNTMANAGERTRANSACTIONSREQUEST'].fields_by_name['requests']._loaded_options = None
    _globals['_BATCHRECONCILEACCOUNTMANAGERTRANSACTIONSREQUEST'].fields_by_name['requests']._serialized_options = b'\xe0A\x02'
    _globals['_ACCOUNTMANAGERTRANSACTIONS']._loaded_options = None
    _globals['_ACCOUNTMANAGERTRANSACTIONS']._serialized_options = b'\xcaA\x1bissuerswitch.googleapis.com\xd2A.https://www.googleapis.com/auth/cloud-platform'
    _globals['_ACCOUNTMANAGERTRANSACTIONS'].methods_by_name['ExportAccountManagerTransactions']._loaded_options = None
    _globals['_ACCOUNTMANAGERTRANSACTIONS'].methods_by_name['ExportAccountManagerTransactions']._serialized_options = b'\xcaAT\n(ExportAccountManagerTransactionsResponse\x12(ExportAccountManagerTransactionsMetadata\x82\xd3\xe4\x93\x02B"=/v1/{parent=projects/*/accountManagers/*}/transactions:export:\x01*'
    _globals['_ACCOUNTMANAGERTRANSACTIONS'].methods_by_name['ListAccountManagerTransactions']._loaded_options = None
    _globals['_ACCOUNTMANAGERTRANSACTIONS'].methods_by_name['ListAccountManagerTransactions']._serialized_options = b'\xdaA\x06parent\x82\xd3\xe4\x93\x028\x126/v1/{parent=projects/*/accountManagers/*}/transactions'
    _globals['_ACCOUNTMANAGERTRANSACTIONS'].methods_by_name['BatchReconcileAccountManagerTransactions']._loaded_options = None
    _globals['_ACCOUNTMANAGERTRANSACTIONS'].methods_by_name['BatchReconcileAccountManagerTransactions']._serialized_options = b'\xdaA\x0fparent,requests\x82\xd3\xe4\x93\x02J"E/v1/{parent=projects/*/accountManagers/*}/transactions:batchReconcile:\x01*'
    _globals['_ACCOUNTMANAGERTRANSACTIONTYPE']._serialized_start = 4396
    _globals['_ACCOUNTMANAGERTRANSACTIONTYPE']._serialized_end = 4541
    _globals['_ACCOUNTMANAGERTRANSACTION']._serialized_start = 433
    _globals['_ACCOUNTMANAGERTRANSACTION']._serialized_end = 1192
    _globals['_ACCOUNTMANAGERTRANSACTIONINFO']._serialized_start = 1195
    _globals['_ACCOUNTMANAGERTRANSACTIONINFO']._serialized_end = 2210
    _globals['_ACCOUNTMANAGERTRANSACTIONINFO_ACCOUNTMANAGERTRANSACTIONMETADATA']._serialized_start = 1777
    _globals['_ACCOUNTMANAGERTRANSACTIONINFO_ACCOUNTMANAGERTRANSACTIONMETADATA']._serialized_end = 2057
    _globals['_ACCOUNTMANAGERTRANSACTIONINFO_ACCOUNTMANAGERTRANSACTIONERRORDETAILS']._serialized_start = 2059
    _globals['_ACCOUNTMANAGERTRANSACTIONINFO_ACCOUNTMANAGERTRANSACTIONERRORDETAILS']._serialized_end = 2151
    _globals['_ACCOUNTMANAGERTRANSACTIONINFO_STATE']._serialized_start = 2153
    _globals['_ACCOUNTMANAGERTRANSACTIONINFO_STATE']._serialized_end = 2210
    _globals['_ACCOUNTMANAGERSETTLEMENTPARTICIPANT']._serialized_start = 2213
    _globals['_ACCOUNTMANAGERSETTLEMENTPARTICIPANT']._serialized_end = 2469
    _globals['_ACCOUNTMANAGERPARTICIPANT']._serialized_start = 2472
    _globals['_ACCOUNTMANAGERPARTICIPANT']._serialized_end = 2776
    _globals['_ACCOUNTMANAGERPARTICIPANT_PERSONA']._serialized_start = 2718
    _globals['_ACCOUNTMANAGERPARTICIPANT_PERSONA']._serialized_end = 2776
    _globals['_ACCOUNTMANAGERMERCHANTINFO']._serialized_start = 2778
    _globals['_ACCOUNTMANAGERMERCHANTINFO']._serialized_end = 2841
    _globals['_ACCOUNTMANAGERTRANSACTIONRECONCILIATIONINFO']._serialized_start = 2844
    _globals['_ACCOUNTMANAGERTRANSACTIONRECONCILIATIONINFO']._serialized_end = 3180
    _globals['_ACCOUNTMANAGERTRANSACTIONRECONCILIATIONINFO_RECONCILIATIONSTATE']._serialized_start = 3094
    _globals['_ACCOUNTMANAGERTRANSACTIONRECONCILIATIONINFO_RECONCILIATIONSTATE']._serialized_end = 3180
    _globals['_EXPORTACCOUNTMANAGERTRANSACTIONSREQUEST']._serialized_start = 3183
    _globals['_EXPORTACCOUNTMANAGERTRANSACTIONSREQUEST']._serialized_end = 3471
    _globals['_LISTACCOUNTMANAGERTRANSACTIONSREQUEST']._serialized_start = 3474
    _globals['_LISTACCOUNTMANAGERTRANSACTIONSREQUEST']._serialized_end = 3662
    _globals['_LISTACCOUNTMANAGERTRANSACTIONSRESPONSE']._serialized_start = 3665
    _globals['_LISTACCOUNTMANAGERTRANSACTIONSRESPONSE']._serialized_end = 3855
    _globals['_RECONCILEACCOUNTMANAGERTRANSACTIONSREQUEST']._serialized_start = 3858
    _globals['_RECONCILEACCOUNTMANAGERTRANSACTIONSREQUEST']._serialized_end = 4015
    _globals['_BATCHRECONCILEACCOUNTMANAGERTRANSACTIONSREQUEST']._serialized_start = 4018
    _globals['_BATCHRECONCILEACCOUNTMANAGERTRANSACTIONSREQUEST']._serialized_end = 4215
    _globals['_BATCHRECONCILEACCOUNTMANAGERTRANSACTIONSRESPONSE']._serialized_start = 4218
    _globals['_BATCHRECONCILEACCOUNTMANAGERTRANSACTIONSRESPONSE']._serialized_end = 4393
    _globals['_ACCOUNTMANAGERTRANSACTIONS']._serialized_start = 4544
    _globals['_ACCOUNTMANAGERTRANSACTIONS']._serialized_end = 5655