from google.protobuf import timestamp_pb2 as _timestamp_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union
DESCRIPTOR: _descriptor.FileDescriptor

class UndeliverableFirstGenEvent(_message.Message):
    __slots__ = ('message', 'reason', 'document_name', 'document_change_type', 'function_name', 'triggered_time')

    class Reason(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        REASON_UNSPECIFIED: _ClassVar[UndeliverableFirstGenEvent.Reason]
        EXCEEDING_SIZE_LIMIT: _ClassVar[UndeliverableFirstGenEvent.Reason]
    REASON_UNSPECIFIED: UndeliverableFirstGenEvent.Reason
    EXCEEDING_SIZE_LIMIT: UndeliverableFirstGenEvent.Reason

    class DocumentChangeType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        DOCUMENT_CHANGE_TYPE_UNSPECIFIED: _ClassVar[UndeliverableFirstGenEvent.DocumentChangeType]
        CREATE: _ClassVar[UndeliverableFirstGenEvent.DocumentChangeType]
        DELETE: _ClassVar[UndeliverableFirstGenEvent.DocumentChangeType]
        UPDATE: _ClassVar[UndeliverableFirstGenEvent.DocumentChangeType]
    DOCUMENT_CHANGE_TYPE_UNSPECIFIED: UndeliverableFirstGenEvent.DocumentChangeType
    CREATE: UndeliverableFirstGenEvent.DocumentChangeType
    DELETE: UndeliverableFirstGenEvent.DocumentChangeType
    UPDATE: UndeliverableFirstGenEvent.DocumentChangeType
    MESSAGE_FIELD_NUMBER: _ClassVar[int]
    REASON_FIELD_NUMBER: _ClassVar[int]
    DOCUMENT_NAME_FIELD_NUMBER: _ClassVar[int]
    DOCUMENT_CHANGE_TYPE_FIELD_NUMBER: _ClassVar[int]
    FUNCTION_NAME_FIELD_NUMBER: _ClassVar[int]
    TRIGGERED_TIME_FIELD_NUMBER: _ClassVar[int]
    message: str
    reason: UndeliverableFirstGenEvent.Reason
    document_name: str
    document_change_type: UndeliverableFirstGenEvent.DocumentChangeType
    function_name: _containers.RepeatedScalarFieldContainer[str]
    triggered_time: _timestamp_pb2.Timestamp

    def __init__(self, message: _Optional[str]=..., reason: _Optional[_Union[UndeliverableFirstGenEvent.Reason, str]]=..., document_name: _Optional[str]=..., document_change_type: _Optional[_Union[UndeliverableFirstGenEvent.DocumentChangeType, str]]=..., function_name: _Optional[_Iterable[str]]=..., triggered_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]]=...) -> None:
        ...