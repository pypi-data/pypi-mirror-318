"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_runtime_version.ValidateProtobufRuntimeVersion(_runtime_version.Domain.PUBLIC, 5, 28, 1, '', 'google/cloud/paymentgateway/issuerswitch/v1/resolutions.proto')
_sym_db = _symbol_database.Default()
from ......google.api import annotations_pb2 as google_dot_api_dot_annotations__pb2
from ......google.api import client_pb2 as google_dot_api_dot_client__pb2
from ......google.api import field_behavior_pb2 as google_dot_api_dot_field__behavior__pb2
from ......google.api import resource_pb2 as google_dot_api_dot_resource__pb2
from ......google.cloud.paymentgateway.issuerswitch.v1 import common_fields_pb2 as google_dot_cloud_dot_paymentgateway_dot_issuerswitch_dot_v1_dot_common__fields__pb2
from ......google.longrunning import operations_pb2 as google_dot_longrunning_dot_operations__pb2
from google.protobuf import timestamp_pb2 as google_dot_protobuf_dot_timestamp__pb2
from ......google.type import money_pb2 as google_dot_type_dot_money__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n=google/cloud/paymentgateway/issuerswitch/v1/resolutions.proto\x12+google.cloud.paymentgateway.issuerswitch.v1\x1a\x1cgoogle/api/annotations.proto\x1a\x17google/api/client.proto\x1a\x1fgoogle/api/field_behavior.proto\x1a\x19google/api/resource.proto\x1a?google/cloud/paymentgateway/issuerswitch/v1/common_fields.proto\x1a#google/longrunning/operations.proto\x1a\x1fgoogle/protobuf/timestamp.proto\x1a\x17google/type/money.proto"\xec\x03\n\tComplaint\x12\x0c\n\x04name\x18\x01 \x01(\t\x12i\n\x1araise_complaint_adjustment\x18\x02 \x01(\x0b2E.google.cloud.paymentgateway.issuerswitch.v1.RaiseComplaintAdjustment\x12N\n\x07details\x18\x04 \x01(\x0b28.google.cloud.paymentgateway.issuerswitch.v1.CaseDetailsB\x03\xe0A\x02\x12P\n\x08response\x18\x05 \x01(\x0b29.google.cloud.paymentgateway.issuerswitch.v1.CaseResponseB\x03\xe0A\x03\x12m\n\x1cresolve_complaint_adjustment\x18\x06 \x01(\x0b2G.google.cloud.paymentgateway.issuerswitch.v1.ResolveComplaintAdjustment:U\xeaAR\n%issuerswitch.googleapis.com/Complaint\x12)projects/{project}/complaints/{complaint}"\xa7\x01\n\x16CreateComplaintRequest\x12=\n\x06parent\x18\x01 \x01(\tB-\xe0A\x02\xfaA\'\x12%issuerswitch.googleapis.com/Complaint\x12N\n\tcomplaint\x18\x02 \x01(\x0b26.google.cloud.paymentgateway.issuerswitch.v1.ComplaintB\x03\xe0A\x02"i\n\x17ResolveComplaintRequest\x12N\n\tcomplaint\x18\x01 \x01(\x0b26.google.cloud.paymentgateway.issuerswitch.v1.ComplaintB\x03\xe0A\x02"\xdc\x03\n\x07Dispute\x12\x0c\n\x04name\x18\x01 \x01(\t\x12e\n\x18raise_dispute_adjustment\x18\x02 \x01(\x0b2C.google.cloud.paymentgateway.issuerswitch.v1.RaiseDisputeAdjustment\x12N\n\x07details\x18\x04 \x01(\x0b28.google.cloud.paymentgateway.issuerswitch.v1.CaseDetailsB\x03\xe0A\x02\x12P\n\x08response\x18\x05 \x01(\x0b29.google.cloud.paymentgateway.issuerswitch.v1.CaseResponseB\x03\xe0A\x03\x12i\n\x1aresolve_dispute_adjustment\x18\x06 \x01(\x0b2E.google.cloud.paymentgateway.issuerswitch.v1.ResolveDisputeAdjustment:O\xeaAL\n#issuerswitch.googleapis.com/Dispute\x12%projects/{project}/disputes/{dispute}"\x9f\x01\n\x14CreateDisputeRequest\x12;\n\x06parent\x18\x01 \x01(\tB+\xe0A\x02\xfaA%\x12#issuerswitch.googleapis.com/Dispute\x12J\n\x07dispute\x18\x02 \x01(\x0b24.google.cloud.paymentgateway.issuerswitch.v1.DisputeB\x03\xe0A\x02"c\n\x15ResolveDisputeRequest\x12J\n\x07dispute\x18\x01 \x01(\x0b24.google.cloud.paymentgateway.issuerswitch.v1.DisputeB\x03\xe0A\x02"\x8d\x01\n\x13OriginalTransaction\x12\x1b\n\x0etransaction_id\x18\x01 \x01(\tB\x03\xe0A\x02\x12\'\n\x1aretrieval_reference_number\x18\x02 \x01(\tB\x03\xe0A\x02\x120\n\x0crequest_time\x18\x03 \x01(\x0b2\x1a.google.protobuf.Timestamp"\xc6\x02\n\x0bCaseDetails\x12c\n\x14original_transaction\x18\x01 \x01(\x0b2@.google.cloud.paymentgateway.issuerswitch.v1.OriginalTransactionB\x03\xe0A\x02\x12b\n\x14transaction_sub_type\x18\x02 \x01(\x0e2?.google.cloud.paymentgateway.issuerswitch.v1.TransactionSubTypeB\x03\xe0A\x02\x12\'\n\x06amount\x18\x03 \x01(\x0b2\x12.google.type.MoneyB\x03\xe0A\x02\x12)\n!original_settlement_response_code\x18\x04 \x01(\t\x12\x1a\n\rcurrent_cycle\x18\x05 \x01(\x08B\x03\xe0A\x02"\xde\x04\n\x0cCaseResponse\x12"\n\x1acomplaint_reference_number\x18\x01 \x01(\t\x12"\n\x06amount\x18\x02 \x01(\x0b2\x12.google.type.Money\x12\x17\n\x0fadjustment_flag\x18\x03 \x01(\t\x12\x17\n\x0fadjustment_code\x18\x04 \x01(\t\x12\x1f\n\x17adjustment_reference_id\x18\x05 \x01(\t\x12\x1a\n\x12adjustment_remarks\x18\x06 \x01(\t\x12\x17\n\x0fapproval_number\x18\x07 \x01(\t\x12\x16\n\x0eprocess_status\x18\x08 \x01(\t\x123\n\x0fadjustment_time\x18\t \x01(\x0b2\x1a.google.protobuf.Timestamp\x12I\n\x05payer\x18\n \x01(\x0b28.google.cloud.paymentgateway.issuerswitch.v1.ParticipantH\x00\x12I\n\x05payee\x18\x0b \x01(\x0b28.google.cloud.paymentgateway.issuerswitch.v1.ParticipantH\x00\x12P\n\x06result\x18\x0c \x01(\x0e2@.google.cloud.paymentgateway.issuerswitch.v1.CaseResponse.Result":\n\x06Result\x12\x16\n\x12RESULT_UNSPECIFIED\x10\x00\x12\x0b\n\x07SUCCESS\x10\x01\x12\x0b\n\x07FAILURE\x10\x02B\r\n\x0bparticipant"\xe8\x04\n\x18RaiseComplaintAdjustment\x12r\n\x0fadjustment_flag\x18\x01 \x01(\x0e2T.google.cloud.paymentgateway.issuerswitch.v1.RaiseComplaintAdjustment.AdjustmentFlagB\x03\xe0A\x02\x12n\n\x0fadjustment_code\x18\x02 \x01(\x0e2P.google.cloud.paymentgateway.issuerswitch.v1.RaiseComplaintAdjustment.ReasonCodeB\x03\xe0A\x02"<\n\x0eAdjustmentFlag\x12\x1f\n\x1bADJUSTMENT_FLAG_UNSPECIFIED\x10\x00\x12\t\n\x05RAISE\x10\x01"\xa9\x02\n\nReasonCode\x12\x1b\n\x17REASON_CODE_UNSPECIFIED\x10\x00\x12!\n\x1dCUSTOMER_ACCOUNT_NOT_REVERSED\x10\x01\x12\x1f\n\x1bGOODS_SERVICES_NOT_PROVIDED\x10\x02\x12&\n"CUSTOMER_ACCOUNT_NOT_CREDITED_BACK\x10\x03\x12$\n BENEFICIARY_ACCOUNT_NOT_CREDITED\x10\x04\x12\'\n#GOODS_SERVICES_CREDIT_NOT_PROCESSED\x10\x05\x12&\n"MERCHANT_NOT_RECEIVED_CONFIRMATION\x10\x06\x12\x1b\n\x17PAID_BY_ALTERNATE_MEANS\x10\x07"\xf4\x06\n\x1aResolveComplaintAdjustment\x12t\n\x0fadjustment_flag\x18\x01 \x01(\x0e2V.google.cloud.paymentgateway.issuerswitch.v1.ResolveComplaintAdjustment.AdjustmentFlagB\x03\xe0A\x02\x12p\n\x0fadjustment_code\x18\x02 \x01(\x0e2R.google.cloud.paymentgateway.issuerswitch.v1.ResolveComplaintAdjustment.ReasonCodeB\x03\xe0A\x02"\xa5\x01\n\x0eAdjustmentFlag\x12\x1f\n\x1bADJUSTMENT_FLAG_UNSPECIFIED\x10\x00\x12\x1f\n\x1bDEBIT_REVERSAL_CONFIRMATION\x10\x01\x12\n\n\x06RETURN\x10\x02\x12 \n\x1cREFUND_REVERSAL_CONFIRMATION\x10\x03\x12#\n\x1fTRANSACTION_CREDIT_CONFIRMATION\x10\x04"\xc5\x03\n\nReasonCode\x12\x1b\n\x17REASON_CODE_UNSPECIFIED\x10\x00\x12\x1d\n\x19COMPLAINT_RESOLVED_ONLINE\x10\x01\x12&\n"COMPLAINT_RESOLVED_NOW_OR_MANUALLY\x10\x02\x12!\n\x1dORIGINAL_TRANSACTION_NOT_DONE\x10\x03\x12\x16\n\x12RET_ACCOUNT_CLOSED\x10\x04\x12\x1e\n\x1aRET_ACCOUNT_DOES_NOT_EXIST\x10\x05\x12\x1a\n\x16RET_PARTY_INSTRUCTIONS\x10\x06\x12\x13\n\x0fRET_NRI_ACCOUNT\x10\x07\x12\x16\n\x12RET_CREDIT_FREEZED\x10\x08\x12#\n\x1fRET_INVALID_BENEFICIARY_DETAILS\x10\t\x12\x18\n\x14RET_ANY_OTHER_REASON\x10\n\x12!\n\x1dRET_BENEFICIARY_CANNOT_CREDIT\x10\x0b\x12*\n&RET_MERCHANT_NOT_RECEIVED_CONFIRMATION\x10\x0c\x12!\n\x1dRRC_CUSTOMER_ACCOUNT_CREDITED\x10\r"\x98\n\n\x16RaiseDisputeAdjustment\x12p\n\x0fadjustment_flag\x18\x01 \x01(\x0e2R.google.cloud.paymentgateway.issuerswitch.v1.RaiseDisputeAdjustment.AdjustmentFlagB\x03\xe0A\x02\x12l\n\x0fadjustment_code\x18\x02 \x01(\x0e2N.google.cloud.paymentgateway.issuerswitch.v1.RaiseDisputeAdjustment.ReasonCodeB\x03\xe0A\x02"\x9b\x02\n\x0eAdjustmentFlag\x12\x1f\n\x1bADJUSTMENT_FLAG_UNSPECIFIED\x10\x00\x12\x14\n\x10CHARGEBACK_RAISE\x10\x01\x12\x1a\n\x16FRAUD_CHARGEBACK_RAISE\x10\x02\x12!\n\x1dWRONG_CREDIT_CHARGEBACK_RAISE\x10\x03\x12\x1d\n\x19DEFERRED_CHARGEBACK_RAISE\x10\x04\x12\x19\n\x15PRE_ARBITRATION_RAISE\x10\x05\x12"\n\x1eDEFERRED_PRE_ARBITRATION_RAISE\x10\x06\x12\x15\n\x11ARBITRATION_RAISE\x10\x07\x12\x1e\n\x1aDEFERRED_ARBITRATION_RAISE\x10\x08"\xff\x05\n\nReasonCode\x12\x1b\n\x17REASON_CODE_UNSPECIFIED\x10\x00\x12>\n:CHARGEBACK_RAISE_REMITTER_DEBITED_BENEFICIARY_NOT_CREDITED\x10\x01\x122\n.PRE_ARBITRATION_RAISE_BENEFICIARY_NOT_CREDITED\x10\x02\x126\n2DEFERRED_CHARGEBACK_RAISE_BENEFICIARY_NOT_CREDITED\x10\x03\x12;\n7DEFERRED_PRE_ARBITRATION_RAISE_BENEFICIARY_NOT_CREDITED\x10\x04\x12K\nGDEFERRED_ARBITRATION_RAISE_DEFERRED_CHARGEBACK_PRE_ARBITRATION_REJECTED\x10\x05\x12\x17\n\x13CHARGEBACK_ON_FRAUD\x10\x06\x12\'\n#GOODS_SERVICES_CREDIT_NOT_PROCESSED\x10\x07\x12\x1c\n\x18GOODS_SERVICES_DEFECTIVE\x10\x08\x12\x1b\n\x17PAID_BY_ALTERNATE_MEANS\x10\t\x12\x1f\n\x1bGOODS_SERVICES_NOT_RECEIVED\x10\n\x12&\n"MERCHANT_NOT_RECEIVED_CONFIRMATION\x10\x0b\x12\x1b\n\x17TRANSACTION_NOT_STEELED\x10\x0c\x12\x19\n\x15DUPLICATE_TRANSACTION\x10\r\x12\'\n#CHARGEBACK_CARD_HOLDER_CHARGED_MORE\x10\x0e\x122\n.CUSTOMER_CLAIMING_GOODS_SERVICES_NOT_DELIVERED\x10\x0f\x12\x12\n\x0ePARTIES_DENIED\x10\x10\x12/\n+FUNDS_TRANSFERRED_TO_UNINTENDED_BENEFICIARY\x10\x11"\xb5\x17\n\x18ResolveDisputeAdjustment\x12r\n\x0fadjustment_flag\x18\x01 \x01(\x0e2T.google.cloud.paymentgateway.issuerswitch.v1.ResolveDisputeAdjustment.AdjustmentFlagB\x03\xe0A\x02\x12n\n\x0fadjustment_code\x18\x02 \x01(\x0e2P.google.cloud.paymentgateway.issuerswitch.v1.ResolveDisputeAdjustment.ReasonCodeB\x03\xe0A\x02"\xe0\x04\n\x0eAdjustmentFlag\x12\x1f\n\x1bADJUSTMENT_FLAG_UNSPECIFIED\x10\x00\x12\x18\n\x14RE_PRESENTMENT_RAISE\x10\x01\x12!\n\x1dDEFERRED_RE_PRESENTMENT_RAISE\x10\x02\x12\x19\n\x15CHARGEBACK_ACCEPTANCE\x10\x03\x12"\n\x1eDEFERRED_CHARGEBACK_ACCEPTANCE\x10\x04\x12\x1e\n\x1aPRE_ARBITRATION_ACCEPTANCE\x10\x05\x12\'\n#DEFERRED_PRE_ARBITRATION_ACCEPTANCE\x10\x06\x12\x1c\n\x18PRE_ARBITRATION_DECLINED\x10\x07\x12%\n!DEFERRED_PRE_ARBITRATION_DECLINED\x10\x08\x12\x1a\n\x16ARBITRATION_ACCEPTANCE\x10\t\x12\x1c\n\x18ARBITRATION_CONTINUATION\x10\n\x12\x19\n\x15ARBITRATION_WITHDRAWN\x10\x0b\x12\x17\n\x13ARBITRATION_VERDICT\x10\x0c\x12\x15\n\x11CREDIT_ADJUSTMENT\x10\r\x12"\n\x1eFRAUD_CHARGEBACK_REPRESENTMENT\x10\x0e\x12\x1b\n\x17FRAUD_CHARGEBACK_ACCEPT\x10\x0f\x12\x1e\n\x1aWRONG_CREDIT_REPRESENTMENT\x10\x10\x12&\n"WRONG_CREDIT_CHARGEBACK_ACCEPTANCE\x10\x11\x12\x15\n\x11MANUAL_ADJUSTMENT\x10\x12"\xd1\x10\n\nReasonCode\x12\x1b\n\x17REASON_CODE_UNSPECIFIED\x10\x00\x12M\nICHARGEBACK_BENEFICIARY_CANNOT_CREDIT_OR_PRE_ARBITRATION_DUPLICATE_PROCESS\x10\x01\x128\n4PRE_ARBITRATION_DECLINED_BENEFICIARY_CREDITED_ONLINE\x10\x03\x12:\n6PRE_ARBITRATION_DECLINED_BENEFICIARY_CREDITED_MANUALLY\x10\x04\x12B\n>DEFERRED_CHARGEBACK_ACCEPTANCE_ACCOUNT_NOT_CREDITED_TCC_RAISED\x10\x05\x12=\n9DEFERRED_RE_PRESENTMENT_RAISE_ACCOUNT_CREDITED_TCC_RAISED\x10\x06\x12<\n8DEFERRED_PRE_ARBITRATION_ACCEPTANCE_ACCOUNT_NOT_CREDITED\x10\x07\x126\n2DEFERRED_PRE_ARBITRATION_DECLINED_ACCOUNT_CREDITED\x10\x08\x12D\n@FRAUD_CHARGEBACK_ACCEPT_AMOUNT_RECOVERED_FROM_FRAUDULENT_ACCOUNT\x10\t\x12C\n?FRAUD_CHARGEBACK_REPRESENTMENT_LIEN_MARKED_INSUFFICIENT_BALANCE\x10\n\x123\n/FRAUD_CHARGEBACK_REPRESENTMENT_FIR_NOT_PROVIDED\x10\x0b\x120\n,FRAUD_CHARGEBACK_REPRESENTMENT_REASON_OTHERS\x10\x0c\x124\n0RE_PRESENTMENT_RAISE_BENEFICIARY_CREDITED_ONLINE\x10\r\x126\n2RE_PRESENTMENT_RAISE_BENEFICIARY_CREDITED_MANUALLY\x10\x0e\x129\n5CREDIT_ADJUSTMENT_GOODS_SERVICES_CREDIT_NOT_PROCESSED\x10\x0f\x12.\n*CREDIT_ADJUSTMENT_GOODS_SERVICES_DEFECTIVE\x10\x10\x12-\n)CREDIT_ADJUSTMENT_PAID_BY_ALTERNATE_MEANS\x10\x11\x121\n-CREDIT_ADJUSTMENT_GOODS_SERVICES_NOT_RECEIVED\x10\x12\x128\n4CREDIT_ADJUSTMENT_MERCHANT_NOT_RECEIVED_CONFIRMATION\x10\x13\x12+\n\'CREDIT_ADJUSTMENT_DUPLICATE_TRANSACTION\x10\x14\x12#\n\x1fCREDIT_ADJUSTMENT_REASON_OTHERS\x10\x15\x121\n-CREDIT_ADJUSTMENT_NON_MATCHING_ACCOUNT_NUMBER\x10\x16\x12.\n*CREDIT_ADJUSTMENT_CARD_HOLDER_CHARGED_MORE\x10\x17\x12*\n&CREDIT_ADJUSTMENT_CREDIT_NOT_PROCESSED\x10\x18\x12/\n+CREDIT_ADJUSTMENT_BENEFICIARY_CANNOT_CREDIT\x10\x19\x129\n5CHARGEBACK_ACCEPTANCE_MERCHANT_CANNOT_PROVIDE_SERVICE\x10\x1a\x120\n,RE_PRESENTMENT_RAISE_GOODS_SERVICES_PROVIDED\x10\x1b\x124\n0PRE_ARBITRATION_DECLINED_SERVICES_PROVIDED_LATER\x10\x1c\x12@\n<PRE_ARBITRATION_ACCEPTANCE_SERVICES_NOT_PROVIDED_BY_MERCHANT\x10\x1d\x12/\n+ARBITRATION_ACCEPTANCE_ILLEGIBLE_FULFILMENT\x10\x1e\x12@\n<ARBITRATION_CONTINUATION_CUSTOMER_STILL_NOT_RECEIVED_SERVICE\x10\x1f\x129\n5ARBITRATION_WITHDRAWN_CUSTOMER_RECEIVED_SERVICE_LATER\x10 \x12%\n!ARBITRATION_VERDICT_PANEL_VERDICT\x10!\x12\x1c\n\x18MANUAL_ADJUSTMENT_REASON\x10"\x12\x18\n\x14ATTRIBUTING_CUSTOMER\x10#\x12\x1f\n\x1bATTRIBUTING_TECHNICAL_ISSUE\x10$\x127\n3WRONG_CREDIT_CHARGEBACK_ACCEPTANCE_AMOUNT_RECOVERED\x10%\x12?\n;WRONG_CREDIT_REPRESENTMENT_LIEN_MARKED_INSUFFICIENT_BALANCE\x10&\x124\n0WRONG_CREDIT_REPRESENTMENT_CUSTOMER_INACCESSIBLE\x10\'\x12,\n(WRONG_CREDIT_REPRESENTMENT_REASON_OTHERS\x10("\x19\n\x17CreateComplaintMetadata"\x1a\n\x18ResolveComplaintMetadata"\x17\n\x15CreateDisputeMetadata"\x18\n\x16ResolveDisputeMetadata*\x83\x01\n\x12TransactionSubType\x12$\n TRANSACTION_SUB_TYPE_UNSPECIFIED\x10\x00\x12$\n TRANSACTION_SUB_TYPE_BENEFICIARY\x10\x01\x12!\n\x1dTRANSACTION_SUB_TYPE_REMITTER\x10\x022\x8c\x08\n\x17IssuerSwitchResolutions\x12\xe6\x01\n\x0fCreateComplaint\x12C.google.cloud.paymentgateway.issuerswitch.v1.CreateComplaintRequest\x1a\x1d.google.longrunning.Operation"o\xcaA$\n\tComplaint\x12\x17CreateComplaintMetadata\xdaA\x10parent,complaint\x82\xd3\xe4\x93\x02/""/v1/{parent=projects/*}/complaints:\tcomplaint\x12\xf4\x01\n\x10ResolveComplaint\x12D.google.cloud.paymentgateway.issuerswitch.v1.ResolveComplaintRequest\x1a\x1d.google.longrunning.Operation"{\xcaA%\n\tComplaint\x12\x18ResolveComplaintMetadata\xdaA\tcomplaint\x82\xd3\xe4\x93\x02A"4/v1/{complaint.name=projects/*/complaints/*}:resolve:\tcomplaint\x12\xd8\x01\n\rCreateDispute\x12A.google.cloud.paymentgateway.issuerswitch.v1.CreateDisputeRequest\x1a\x1d.google.longrunning.Operation"e\xcaA \n\x07Dispute\x12\x15CreateDisputeMetadata\xdaA\x0eparent,dispute\x82\xd3\xe4\x93\x02+" /v1/{parent=projects/*}/disputes:\x07dispute\x12\xe4\x01\n\x0eResolveDispute\x12B.google.cloud.paymentgateway.issuerswitch.v1.ResolveDisputeRequest\x1a\x1d.google.longrunning.Operation"o\xcaA!\n\x07Dispute\x12\x16ResolveDisputeMetadata\xdaA\x07dispute\x82\xd3\xe4\x93\x02;"0/v1/{dispute.name=projects/*/disputes/*}:resolve:\x07dispute\x1aO\xcaA\x1bissuerswitch.googleapis.com\xd2A.https://www.googleapis.com/auth/cloud-platformB\xa8\x02\n/com.google.cloud.paymentgateway.issuerswitch.v1B\x10ResolutionsProtoP\x01ZScloud.google.com/go/paymentgateway/issuerswitch/apiv1/issuerswitchpb;issuerswitchpb\xaa\x02+Google.Cloud.PaymentGateway.IssuerSwitch.V1\xca\x02+Google\\Cloud\\PaymentGateway\\IssuerSwitch\\V1\xea\x02/Google::Cloud::PaymentGateway::IssuerSwitch::V1b\x06proto3')
_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'google.cloud.paymentgateway.issuerswitch.v1.resolutions_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
    _globals['DESCRIPTOR']._loaded_options = None
    _globals['DESCRIPTOR']._serialized_options = b'\n/com.google.cloud.paymentgateway.issuerswitch.v1B\x10ResolutionsProtoP\x01ZScloud.google.com/go/paymentgateway/issuerswitch/apiv1/issuerswitchpb;issuerswitchpb\xaa\x02+Google.Cloud.PaymentGateway.IssuerSwitch.V1\xca\x02+Google\\Cloud\\PaymentGateway\\IssuerSwitch\\V1\xea\x02/Google::Cloud::PaymentGateway::IssuerSwitch::V1'
    _globals['_COMPLAINT'].fields_by_name['details']._loaded_options = None
    _globals['_COMPLAINT'].fields_by_name['details']._serialized_options = b'\xe0A\x02'
    _globals['_COMPLAINT'].fields_by_name['response']._loaded_options = None
    _globals['_COMPLAINT'].fields_by_name['response']._serialized_options = b'\xe0A\x03'
    _globals['_COMPLAINT']._loaded_options = None
    _globals['_COMPLAINT']._serialized_options = b'\xeaAR\n%issuerswitch.googleapis.com/Complaint\x12)projects/{project}/complaints/{complaint}'
    _globals['_CREATECOMPLAINTREQUEST'].fields_by_name['parent']._loaded_options = None
    _globals['_CREATECOMPLAINTREQUEST'].fields_by_name['parent']._serialized_options = b"\xe0A\x02\xfaA'\x12%issuerswitch.googleapis.com/Complaint"
    _globals['_CREATECOMPLAINTREQUEST'].fields_by_name['complaint']._loaded_options = None
    _globals['_CREATECOMPLAINTREQUEST'].fields_by_name['complaint']._serialized_options = b'\xe0A\x02'
    _globals['_RESOLVECOMPLAINTREQUEST'].fields_by_name['complaint']._loaded_options = None
    _globals['_RESOLVECOMPLAINTREQUEST'].fields_by_name['complaint']._serialized_options = b'\xe0A\x02'
    _globals['_DISPUTE'].fields_by_name['details']._loaded_options = None
    _globals['_DISPUTE'].fields_by_name['details']._serialized_options = b'\xe0A\x02'
    _globals['_DISPUTE'].fields_by_name['response']._loaded_options = None
    _globals['_DISPUTE'].fields_by_name['response']._serialized_options = b'\xe0A\x03'
    _globals['_DISPUTE']._loaded_options = None
    _globals['_DISPUTE']._serialized_options = b'\xeaAL\n#issuerswitch.googleapis.com/Dispute\x12%projects/{project}/disputes/{dispute}'
    _globals['_CREATEDISPUTEREQUEST'].fields_by_name['parent']._loaded_options = None
    _globals['_CREATEDISPUTEREQUEST'].fields_by_name['parent']._serialized_options = b'\xe0A\x02\xfaA%\x12#issuerswitch.googleapis.com/Dispute'
    _globals['_CREATEDISPUTEREQUEST'].fields_by_name['dispute']._loaded_options = None
    _globals['_CREATEDISPUTEREQUEST'].fields_by_name['dispute']._serialized_options = b'\xe0A\x02'
    _globals['_RESOLVEDISPUTEREQUEST'].fields_by_name['dispute']._loaded_options = None
    _globals['_RESOLVEDISPUTEREQUEST'].fields_by_name['dispute']._serialized_options = b'\xe0A\x02'
    _globals['_ORIGINALTRANSACTION'].fields_by_name['transaction_id']._loaded_options = None
    _globals['_ORIGINALTRANSACTION'].fields_by_name['transaction_id']._serialized_options = b'\xe0A\x02'
    _globals['_ORIGINALTRANSACTION'].fields_by_name['retrieval_reference_number']._loaded_options = None
    _globals['_ORIGINALTRANSACTION'].fields_by_name['retrieval_reference_number']._serialized_options = b'\xe0A\x02'
    _globals['_CASEDETAILS'].fields_by_name['original_transaction']._loaded_options = None
    _globals['_CASEDETAILS'].fields_by_name['original_transaction']._serialized_options = b'\xe0A\x02'
    _globals['_CASEDETAILS'].fields_by_name['transaction_sub_type']._loaded_options = None
    _globals['_CASEDETAILS'].fields_by_name['transaction_sub_type']._serialized_options = b'\xe0A\x02'
    _globals['_CASEDETAILS'].fields_by_name['amount']._loaded_options = None
    _globals['_CASEDETAILS'].fields_by_name['amount']._serialized_options = b'\xe0A\x02'
    _globals['_CASEDETAILS'].fields_by_name['current_cycle']._loaded_options = None
    _globals['_CASEDETAILS'].fields_by_name['current_cycle']._serialized_options = b'\xe0A\x02'
    _globals['_RAISECOMPLAINTADJUSTMENT'].fields_by_name['adjustment_flag']._loaded_options = None
    _globals['_RAISECOMPLAINTADJUSTMENT'].fields_by_name['adjustment_flag']._serialized_options = b'\xe0A\x02'
    _globals['_RAISECOMPLAINTADJUSTMENT'].fields_by_name['adjustment_code']._loaded_options = None
    _globals['_RAISECOMPLAINTADJUSTMENT'].fields_by_name['adjustment_code']._serialized_options = b'\xe0A\x02'
    _globals['_RESOLVECOMPLAINTADJUSTMENT'].fields_by_name['adjustment_flag']._loaded_options = None
    _globals['_RESOLVECOMPLAINTADJUSTMENT'].fields_by_name['adjustment_flag']._serialized_options = b'\xe0A\x02'
    _globals['_RESOLVECOMPLAINTADJUSTMENT'].fields_by_name['adjustment_code']._loaded_options = None
    _globals['_RESOLVECOMPLAINTADJUSTMENT'].fields_by_name['adjustment_code']._serialized_options = b'\xe0A\x02'
    _globals['_RAISEDISPUTEADJUSTMENT'].fields_by_name['adjustment_flag']._loaded_options = None
    _globals['_RAISEDISPUTEADJUSTMENT'].fields_by_name['adjustment_flag']._serialized_options = b'\xe0A\x02'
    _globals['_RAISEDISPUTEADJUSTMENT'].fields_by_name['adjustment_code']._loaded_options = None
    _globals['_RAISEDISPUTEADJUSTMENT'].fields_by_name['adjustment_code']._serialized_options = b'\xe0A\x02'
    _globals['_RESOLVEDISPUTEADJUSTMENT'].fields_by_name['adjustment_flag']._loaded_options = None
    _globals['_RESOLVEDISPUTEADJUSTMENT'].fields_by_name['adjustment_flag']._serialized_options = b'\xe0A\x02'
    _globals['_RESOLVEDISPUTEADJUSTMENT'].fields_by_name['adjustment_code']._loaded_options = None
    _globals['_RESOLVEDISPUTEADJUSTMENT'].fields_by_name['adjustment_code']._serialized_options = b'\xe0A\x02'
    _globals['_ISSUERSWITCHRESOLUTIONS']._loaded_options = None
    _globals['_ISSUERSWITCHRESOLUTIONS']._serialized_options = b'\xcaA\x1bissuerswitch.googleapis.com\xd2A.https://www.googleapis.com/auth/cloud-platform'
    _globals['_ISSUERSWITCHRESOLUTIONS'].methods_by_name['CreateComplaint']._loaded_options = None
    _globals['_ISSUERSWITCHRESOLUTIONS'].methods_by_name['CreateComplaint']._serialized_options = b'\xcaA$\n\tComplaint\x12\x17CreateComplaintMetadata\xdaA\x10parent,complaint\x82\xd3\xe4\x93\x02/""/v1/{parent=projects/*}/complaints:\tcomplaint'
    _globals['_ISSUERSWITCHRESOLUTIONS'].methods_by_name['ResolveComplaint']._loaded_options = None
    _globals['_ISSUERSWITCHRESOLUTIONS'].methods_by_name['ResolveComplaint']._serialized_options = b'\xcaA%\n\tComplaint\x12\x18ResolveComplaintMetadata\xdaA\tcomplaint\x82\xd3\xe4\x93\x02A"4/v1/{complaint.name=projects/*/complaints/*}:resolve:\tcomplaint'
    _globals['_ISSUERSWITCHRESOLUTIONS'].methods_by_name['CreateDispute']._loaded_options = None
    _globals['_ISSUERSWITCHRESOLUTIONS'].methods_by_name['CreateDispute']._serialized_options = b'\xcaA \n\x07Dispute\x12\x15CreateDisputeMetadata\xdaA\x0eparent,dispute\x82\xd3\xe4\x93\x02+" /v1/{parent=projects/*}/disputes:\x07dispute'
    _globals['_ISSUERSWITCHRESOLUTIONS'].methods_by_name['ResolveDispute']._loaded_options = None
    _globals['_ISSUERSWITCHRESOLUTIONS'].methods_by_name['ResolveDispute']._serialized_options = b'\xcaA!\n\x07Dispute\x12\x16ResolveDisputeMetadata\xdaA\x07dispute\x82\xd3\xe4\x93\x02;"0/v1/{dispute.name=projects/*/disputes/*}:resolve:\x07dispute'
    _globals['_TRANSACTIONSUBTYPE']._serialized_start = 8901
    _globals['_TRANSACTIONSUBTYPE']._serialized_end = 9032
    _globals['_COMPLAINT']._serialized_start = 386
    _globals['_COMPLAINT']._serialized_end = 878
    _globals['_CREATECOMPLAINTREQUEST']._serialized_start = 881
    _globals['_CREATECOMPLAINTREQUEST']._serialized_end = 1048
    _globals['_RESOLVECOMPLAINTREQUEST']._serialized_start = 1050
    _globals['_RESOLVECOMPLAINTREQUEST']._serialized_end = 1155
    _globals['_DISPUTE']._serialized_start = 1158
    _globals['_DISPUTE']._serialized_end = 1634
    _globals['_CREATEDISPUTEREQUEST']._serialized_start = 1637
    _globals['_CREATEDISPUTEREQUEST']._serialized_end = 1796
    _globals['_RESOLVEDISPUTEREQUEST']._serialized_start = 1798
    _globals['_RESOLVEDISPUTEREQUEST']._serialized_end = 1897
    _globals['_ORIGINALTRANSACTION']._serialized_start = 1900
    _globals['_ORIGINALTRANSACTION']._serialized_end = 2041
    _globals['_CASEDETAILS']._serialized_start = 2044
    _globals['_CASEDETAILS']._serialized_end = 2370
    _globals['_CASERESPONSE']._serialized_start = 2373
    _globals['_CASERESPONSE']._serialized_end = 2979
    _globals['_CASERESPONSE_RESULT']._serialized_start = 2906
    _globals['_CASERESPONSE_RESULT']._serialized_end = 2964
    _globals['_RAISECOMPLAINTADJUSTMENT']._serialized_start = 2982
    _globals['_RAISECOMPLAINTADJUSTMENT']._serialized_end = 3598
    _globals['_RAISECOMPLAINTADJUSTMENT_ADJUSTMENTFLAG']._serialized_start = 3238
    _globals['_RAISECOMPLAINTADJUSTMENT_ADJUSTMENTFLAG']._serialized_end = 3298
    _globals['_RAISECOMPLAINTADJUSTMENT_REASONCODE']._serialized_start = 3301
    _globals['_RAISECOMPLAINTADJUSTMENT_REASONCODE']._serialized_end = 3598
    _globals['_RESOLVECOMPLAINTADJUSTMENT']._serialized_start = 3601
    _globals['_RESOLVECOMPLAINTADJUSTMENT']._serialized_end = 4485
    _globals['_RESOLVECOMPLAINTADJUSTMENT_ADJUSTMENTFLAG']._serialized_start = 3864
    _globals['_RESOLVECOMPLAINTADJUSTMENT_ADJUSTMENTFLAG']._serialized_end = 4029
    _globals['_RESOLVECOMPLAINTADJUSTMENT_REASONCODE']._serialized_start = 4032
    _globals['_RESOLVECOMPLAINTADJUSTMENT_REASONCODE']._serialized_end = 4485
    _globals['_RAISEDISPUTEADJUSTMENT']._serialized_start = 4488
    _globals['_RAISEDISPUTEADJUSTMENT']._serialized_end = 5792
    _globals['_RAISEDISPUTEADJUSTMENT_ADJUSTMENTFLAG']._serialized_start = 4739
    _globals['_RAISEDISPUTEADJUSTMENT_ADJUSTMENTFLAG']._serialized_end = 5022
    _globals['_RAISEDISPUTEADJUSTMENT_REASONCODE']._serialized_start = 5025
    _globals['_RAISEDISPUTEADJUSTMENT_REASONCODE']._serialized_end = 5792
    _globals['_RESOLVEDISPUTEADJUSTMENT']._serialized_start = 5795
    _globals['_RESOLVEDISPUTEADJUSTMENT']._serialized_end = 8792
    _globals['_RESOLVEDISPUTEADJUSTMENT_ADJUSTMENTFLAG']._serialized_start = 6052
    _globals['_RESOLVEDISPUTEADJUSTMENT_ADJUSTMENTFLAG']._serialized_end = 6660
    _globals['_RESOLVEDISPUTEADJUSTMENT_REASONCODE']._serialized_start = 6663
    _globals['_RESOLVEDISPUTEADJUSTMENT_REASONCODE']._serialized_end = 8792
    _globals['_CREATECOMPLAINTMETADATA']._serialized_start = 8794
    _globals['_CREATECOMPLAINTMETADATA']._serialized_end = 8819
    _globals['_RESOLVECOMPLAINTMETADATA']._serialized_start = 8821
    _globals['_RESOLVECOMPLAINTMETADATA']._serialized_end = 8847
    _globals['_CREATEDISPUTEMETADATA']._serialized_start = 8849
    _globals['_CREATEDISPUTEMETADATA']._serialized_end = 8872
    _globals['_RESOLVEDISPUTEMETADATA']._serialized_start = 8874
    _globals['_RESOLVEDISPUTEMETADATA']._serialized_end = 8898
    _globals['_ISSUERSWITCHRESOLUTIONS']._serialized_start = 9035
    _globals['_ISSUERSWITCHRESOLUTIONS']._serialized_end = 10071