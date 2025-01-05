from google.api import field_info_pb2 as _field_info_pb2
from google.protobuf import timestamp_pb2 as _timestamp_pb2
from google.rpc import status_pb2 as _status_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Mapping as _Mapping, Optional as _Optional, Union as _Union
DESCRIPTOR: _descriptor.FileDescriptor

class PipelineActivity(_message.Message):
    __slots__ = ('message_uid', 'attributes', 'activity_time', 'message_received', 'message_transformed', 'message_converted', 'message_request_dispatched', 'message_response_received')

    class PayloadFormat(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        PAYLOAD_FORMAT_UNSPECIFIED: _ClassVar[PipelineActivity.PayloadFormat]
        JSON: _ClassVar[PipelineActivity.PayloadFormat]
        PROTO: _ClassVar[PipelineActivity.PayloadFormat]
        AVRO: _ClassVar[PipelineActivity.PayloadFormat]
    PAYLOAD_FORMAT_UNSPECIFIED: PipelineActivity.PayloadFormat
    JSON: PipelineActivity.PayloadFormat
    PROTO: PipelineActivity.PayloadFormat
    AVRO: PipelineActivity.PayloadFormat

    class MessageReceived(_message.Message):
        __slots__ = ('details', 'input_payload_format', 'error')
        DETAILS_FIELD_NUMBER: _ClassVar[int]
        INPUT_PAYLOAD_FORMAT_FIELD_NUMBER: _ClassVar[int]
        ERROR_FIELD_NUMBER: _ClassVar[int]
        details: str
        input_payload_format: PipelineActivity.PayloadFormat
        error: _status_pb2.Status

        def __init__(self, details: _Optional[str]=..., input_payload_format: _Optional[_Union[PipelineActivity.PayloadFormat, str]]=..., error: _Optional[_Union[_status_pb2.Status, _Mapping]]=...) -> None:
            ...

    class MessageTransformed(_message.Message):
        __slots__ = ('details', 'error')
        DETAILS_FIELD_NUMBER: _ClassVar[int]
        ERROR_FIELD_NUMBER: _ClassVar[int]
        details: str
        error: _status_pb2.Status

        def __init__(self, details: _Optional[str]=..., error: _Optional[_Union[_status_pb2.Status, _Mapping]]=...) -> None:
            ...

    class MessageConverted(_message.Message):
        __slots__ = ('details', 'input_payload_format', 'output_payload_format', 'error')
        DETAILS_FIELD_NUMBER: _ClassVar[int]
        INPUT_PAYLOAD_FORMAT_FIELD_NUMBER: _ClassVar[int]
        OUTPUT_PAYLOAD_FORMAT_FIELD_NUMBER: _ClassVar[int]
        ERROR_FIELD_NUMBER: _ClassVar[int]
        details: str
        input_payload_format: PipelineActivity.PayloadFormat
        output_payload_format: PipelineActivity.PayloadFormat
        error: _status_pb2.Status

        def __init__(self, details: _Optional[str]=..., input_payload_format: _Optional[_Union[PipelineActivity.PayloadFormat, str]]=..., output_payload_format: _Optional[_Union[PipelineActivity.PayloadFormat, str]]=..., error: _Optional[_Union[_status_pb2.Status, _Mapping]]=...) -> None:
            ...

    class MessageRequestDispatched(_message.Message):
        __slots__ = ('details', 'destination', 'error')
        DETAILS_FIELD_NUMBER: _ClassVar[int]
        DESTINATION_FIELD_NUMBER: _ClassVar[int]
        ERROR_FIELD_NUMBER: _ClassVar[int]
        details: str
        destination: str
        error: _status_pb2.Status

        def __init__(self, details: _Optional[str]=..., destination: _Optional[str]=..., error: _Optional[_Union[_status_pb2.Status, _Mapping]]=...) -> None:
            ...

    class MessageResponseReceived(_message.Message):
        __slots__ = ('details', 'retry_status', 'retry_time', 'http_response_code', 'error')

        class RetryStatus(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
            __slots__ = ()
            RETRY_STATUS_UNSPECIFIED: _ClassVar[PipelineActivity.MessageResponseReceived.RetryStatus]
            WILL_RETRY: _ClassVar[PipelineActivity.MessageResponseReceived.RetryStatus]
            RETRY_EXHAUSTED: _ClassVar[PipelineActivity.MessageResponseReceived.RetryStatus]
        RETRY_STATUS_UNSPECIFIED: PipelineActivity.MessageResponseReceived.RetryStatus
        WILL_RETRY: PipelineActivity.MessageResponseReceived.RetryStatus
        RETRY_EXHAUSTED: PipelineActivity.MessageResponseReceived.RetryStatus
        DETAILS_FIELD_NUMBER: _ClassVar[int]
        RETRY_STATUS_FIELD_NUMBER: _ClassVar[int]
        RETRY_TIME_FIELD_NUMBER: _ClassVar[int]
        HTTP_RESPONSE_CODE_FIELD_NUMBER: _ClassVar[int]
        ERROR_FIELD_NUMBER: _ClassVar[int]
        details: str
        retry_status: PipelineActivity.MessageResponseReceived.RetryStatus
        retry_time: _timestamp_pb2.Timestamp
        http_response_code: int
        error: _status_pb2.Status

        def __init__(self, details: _Optional[str]=..., retry_status: _Optional[_Union[PipelineActivity.MessageResponseReceived.RetryStatus, str]]=..., retry_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]]=..., http_response_code: _Optional[int]=..., error: _Optional[_Union[_status_pb2.Status, _Mapping]]=...) -> None:
            ...

    class AttributesEntry(_message.Message):
        __slots__ = ('key', 'value')
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: str

        def __init__(self, key: _Optional[str]=..., value: _Optional[str]=...) -> None:
            ...
    MESSAGE_UID_FIELD_NUMBER: _ClassVar[int]
    ATTRIBUTES_FIELD_NUMBER: _ClassVar[int]
    ACTIVITY_TIME_FIELD_NUMBER: _ClassVar[int]
    MESSAGE_RECEIVED_FIELD_NUMBER: _ClassVar[int]
    MESSAGE_TRANSFORMED_FIELD_NUMBER: _ClassVar[int]
    MESSAGE_CONVERTED_FIELD_NUMBER: _ClassVar[int]
    MESSAGE_REQUEST_DISPATCHED_FIELD_NUMBER: _ClassVar[int]
    MESSAGE_RESPONSE_RECEIVED_FIELD_NUMBER: _ClassVar[int]
    message_uid: str
    attributes: _containers.ScalarMap[str, str]
    activity_time: _timestamp_pb2.Timestamp
    message_received: PipelineActivity.MessageReceived
    message_transformed: PipelineActivity.MessageTransformed
    message_converted: PipelineActivity.MessageConverted
    message_request_dispatched: PipelineActivity.MessageRequestDispatched
    message_response_received: PipelineActivity.MessageResponseReceived

    def __init__(self, message_uid: _Optional[str]=..., attributes: _Optional[_Mapping[str, str]]=..., activity_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]]=..., message_received: _Optional[_Union[PipelineActivity.MessageReceived, _Mapping]]=..., message_transformed: _Optional[_Union[PipelineActivity.MessageTransformed, _Mapping]]=..., message_converted: _Optional[_Union[PipelineActivity.MessageConverted, _Mapping]]=..., message_request_dispatched: _Optional[_Union[PipelineActivity.MessageRequestDispatched, _Mapping]]=..., message_response_received: _Optional[_Union[PipelineActivity.MessageResponseReceived, _Mapping]]=...) -> None:
        ...