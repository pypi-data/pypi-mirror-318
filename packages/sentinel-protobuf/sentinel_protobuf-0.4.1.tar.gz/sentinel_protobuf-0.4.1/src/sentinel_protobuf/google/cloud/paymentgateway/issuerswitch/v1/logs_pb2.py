"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_runtime_version.ValidateProtobufRuntimeVersion(_runtime_version.Domain.PUBLIC, 5, 28, 1, '', 'google/cloud/paymentgateway/issuerswitch/v1/logs.proto')
_sym_db = _symbol_database.Default()
from ......google.cloud.paymentgateway.issuerswitch.v1 import common_fields_pb2 as google_dot_cloud_dot_paymentgateway_dot_issuerswitch_dot_v1_dot_common__fields__pb2
from ......google.cloud.paymentgateway.issuerswitch.v1 import transactions_pb2 as google_dot_cloud_dot_paymentgateway_dot_issuerswitch_dot_v1_dot_transactions__pb2
from ......google.logging.type import log_severity_pb2 as google_dot_logging_dot_type_dot_log__severity__pb2
from google.protobuf import timestamp_pb2 as google_dot_protobuf_dot_timestamp__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n6google/cloud/paymentgateway/issuerswitch/v1/logs.proto\x12+google.cloud.paymentgateway.issuerswitch.v1\x1a?google/cloud/paymentgateway/issuerswitch/v1/common_fields.proto\x1a>google/cloud/paymentgateway/issuerswitch/v1/transactions.proto\x1a&google/logging/type/log_severity.proto\x1a\x1fgoogle/protobuf/timestamp.proto"\xb4\x05\n\x0eUpiTransaction\x12\x0f\n\x07message\x18\x01 \x01(\t\x122\n\x08severity\x18\x02 \x01(\x0e2 .google.logging.type.LogSeverity\x12F\n\x08api_type\x18\x03 \x01(\x0e24.google.cloud.paymentgateway.issuerswitch.v1.ApiType\x12M\n\x0cxml_api_type\x18\x04 \x01(\x0e27.google.cloud.paymentgateway.issuerswitch.v1.XmlApiType\x12V\n\x10transaction_type\x18\x05 \x01(\x0e2<.google.cloud.paymentgateway.issuerswitch.v1.TransactionType\x12\x16\n\x0etransaction_id\x18\x06 \x01(\t\x12\x12\n\nmessage_id\x18\x07 \x01(\t\x12\x0b\n\x03rrn\x18\x08 \x01(\t\x128\n\x14payload_receipt_time\x18\t \x01(\x0b2\x1a.google.protobuf.Timestamp\x125\n\x11payload_sent_time\x18\n \x01(\x0b2\x1a.google.protobuf.Timestamp\x12R\n\x06status\x18\x0b \x01(\x0e2B.google.cloud.paymentgateway.issuerswitch.v1.TransactionInfo.State\x12\x12\n\nerror_code\x18\x0c \x01(\t\x12\x16\n\x0eupi_error_code\x18\r \x01(\t\x12\x15\n\rerror_message\x18\x0e \x01(\t\x12\x0e\n\x04sent\x18\x0f \x01(\tH\x00\x12\x12\n\x08received\x18\x10 \x01(\tH\x00B\t\n\x07payloadB\xa1\x02\n/com.google.cloud.paymentgateway.issuerswitch.v1B\tLogsProtoP\x01ZScloud.google.com/go/paymentgateway/issuerswitch/apiv1/issuerswitchpb;issuerswitchpb\xaa\x02+Google.Cloud.PaymentGateway.IssuerSwitch.V1\xca\x02+Google\\Cloud\\PaymentGateway\\IssuerSwitch\\V1\xea\x02/Google::Cloud::PaymentGateway::IssuerSwitch::V1b\x06proto3')
_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'google.cloud.paymentgateway.issuerswitch.v1.logs_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
    _globals['DESCRIPTOR']._loaded_options = None
    _globals['DESCRIPTOR']._serialized_options = b'\n/com.google.cloud.paymentgateway.issuerswitch.v1B\tLogsProtoP\x01ZScloud.google.com/go/paymentgateway/issuerswitch/apiv1/issuerswitchpb;issuerswitchpb\xaa\x02+Google.Cloud.PaymentGateway.IssuerSwitch.V1\xca\x02+Google\\Cloud\\PaymentGateway\\IssuerSwitch\\V1\xea\x02/Google::Cloud::PaymentGateway::IssuerSwitch::V1'
    _globals['_UPITRANSACTION']._serialized_start = 306
    _globals['_UPITRANSACTION']._serialized_end = 998