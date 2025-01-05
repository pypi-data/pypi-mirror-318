from google.cloud.paymentgateway.issuerswitch.v1 import common_fields_pb2 as _common_fields_pb2
from google.cloud.paymentgateway.issuerswitch.v1 import transactions_pb2 as _transactions_pb2
from google.logging.type import log_severity_pb2 as _log_severity_pb2
from google.protobuf import timestamp_pb2 as _timestamp_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Mapping as _Mapping, Optional as _Optional, Union as _Union
DESCRIPTOR: _descriptor.FileDescriptor

class UpiTransaction(_message.Message):
    __slots__ = ('message', 'severity', 'api_type', 'xml_api_type', 'transaction_type', 'transaction_id', 'message_id', 'rrn', 'payload_receipt_time', 'payload_sent_time', 'status', 'error_code', 'upi_error_code', 'error_message', 'sent', 'received')
    MESSAGE_FIELD_NUMBER: _ClassVar[int]
    SEVERITY_FIELD_NUMBER: _ClassVar[int]
    API_TYPE_FIELD_NUMBER: _ClassVar[int]
    XML_API_TYPE_FIELD_NUMBER: _ClassVar[int]
    TRANSACTION_TYPE_FIELD_NUMBER: _ClassVar[int]
    TRANSACTION_ID_FIELD_NUMBER: _ClassVar[int]
    MESSAGE_ID_FIELD_NUMBER: _ClassVar[int]
    RRN_FIELD_NUMBER: _ClassVar[int]
    PAYLOAD_RECEIPT_TIME_FIELD_NUMBER: _ClassVar[int]
    PAYLOAD_SENT_TIME_FIELD_NUMBER: _ClassVar[int]
    STATUS_FIELD_NUMBER: _ClassVar[int]
    ERROR_CODE_FIELD_NUMBER: _ClassVar[int]
    UPI_ERROR_CODE_FIELD_NUMBER: _ClassVar[int]
    ERROR_MESSAGE_FIELD_NUMBER: _ClassVar[int]
    SENT_FIELD_NUMBER: _ClassVar[int]
    RECEIVED_FIELD_NUMBER: _ClassVar[int]
    message: str
    severity: _log_severity_pb2.LogSeverity
    api_type: _common_fields_pb2.ApiType
    xml_api_type: _common_fields_pb2.XmlApiType
    transaction_type: _common_fields_pb2.TransactionType
    transaction_id: str
    message_id: str
    rrn: str
    payload_receipt_time: _timestamp_pb2.Timestamp
    payload_sent_time: _timestamp_pb2.Timestamp
    status: _transactions_pb2.TransactionInfo.State
    error_code: str
    upi_error_code: str
    error_message: str
    sent: str
    received: str

    def __init__(self, message: _Optional[str]=..., severity: _Optional[_Union[_log_severity_pb2.LogSeverity, str]]=..., api_type: _Optional[_Union[_common_fields_pb2.ApiType, str]]=..., xml_api_type: _Optional[_Union[_common_fields_pb2.XmlApiType, str]]=..., transaction_type: _Optional[_Union[_common_fields_pb2.TransactionType, str]]=..., transaction_id: _Optional[str]=..., message_id: _Optional[str]=..., rrn: _Optional[str]=..., payload_receipt_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]]=..., payload_sent_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]]=..., status: _Optional[_Union[_transactions_pb2.TransactionInfo.State, str]]=..., error_code: _Optional[str]=..., upi_error_code: _Optional[str]=..., error_message: _Optional[str]=..., sent: _Optional[str]=..., received: _Optional[str]=...) -> None:
        ...