from google.api import field_behavior_pb2 as _field_behavior_pb2
from google.api import resource_pb2 as _resource_pb2
from google.cloud.support.v2 import actor_pb2 as _actor_pb2
from google.protobuf import timestamp_pb2 as _timestamp_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union
DESCRIPTOR: _descriptor.FileDescriptor

class Case(_message.Message):
    __slots__ = ('name', 'display_name', 'description', 'classification', 'time_zone', 'subscriber_email_addresses', 'state', 'create_time', 'update_time', 'creator', 'contact_email', 'escalated', 'test_case', 'language_code', 'priority')

    class State(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        STATE_UNSPECIFIED: _ClassVar[Case.State]
        NEW: _ClassVar[Case.State]
        IN_PROGRESS_GOOGLE_SUPPORT: _ClassVar[Case.State]
        ACTION_REQUIRED: _ClassVar[Case.State]
        SOLUTION_PROVIDED: _ClassVar[Case.State]
        CLOSED: _ClassVar[Case.State]
    STATE_UNSPECIFIED: Case.State
    NEW: Case.State
    IN_PROGRESS_GOOGLE_SUPPORT: Case.State
    ACTION_REQUIRED: Case.State
    SOLUTION_PROVIDED: Case.State
    CLOSED: Case.State

    class Priority(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        PRIORITY_UNSPECIFIED: _ClassVar[Case.Priority]
        P0: _ClassVar[Case.Priority]
        P1: _ClassVar[Case.Priority]
        P2: _ClassVar[Case.Priority]
        P3: _ClassVar[Case.Priority]
        P4: _ClassVar[Case.Priority]
    PRIORITY_UNSPECIFIED: Case.Priority
    P0: Case.Priority
    P1: Case.Priority
    P2: Case.Priority
    P3: Case.Priority
    P4: Case.Priority
    NAME_FIELD_NUMBER: _ClassVar[int]
    DISPLAY_NAME_FIELD_NUMBER: _ClassVar[int]
    DESCRIPTION_FIELD_NUMBER: _ClassVar[int]
    CLASSIFICATION_FIELD_NUMBER: _ClassVar[int]
    TIME_ZONE_FIELD_NUMBER: _ClassVar[int]
    SUBSCRIBER_EMAIL_ADDRESSES_FIELD_NUMBER: _ClassVar[int]
    STATE_FIELD_NUMBER: _ClassVar[int]
    CREATE_TIME_FIELD_NUMBER: _ClassVar[int]
    UPDATE_TIME_FIELD_NUMBER: _ClassVar[int]
    CREATOR_FIELD_NUMBER: _ClassVar[int]
    CONTACT_EMAIL_FIELD_NUMBER: _ClassVar[int]
    ESCALATED_FIELD_NUMBER: _ClassVar[int]
    TEST_CASE_FIELD_NUMBER: _ClassVar[int]
    LANGUAGE_CODE_FIELD_NUMBER: _ClassVar[int]
    PRIORITY_FIELD_NUMBER: _ClassVar[int]
    name: str
    display_name: str
    description: str
    classification: CaseClassification
    time_zone: str
    subscriber_email_addresses: _containers.RepeatedScalarFieldContainer[str]
    state: Case.State
    create_time: _timestamp_pb2.Timestamp
    update_time: _timestamp_pb2.Timestamp
    creator: _actor_pb2.Actor
    contact_email: str
    escalated: bool
    test_case: bool
    language_code: str
    priority: Case.Priority

    def __init__(self, name: _Optional[str]=..., display_name: _Optional[str]=..., description: _Optional[str]=..., classification: _Optional[_Union[CaseClassification, _Mapping]]=..., time_zone: _Optional[str]=..., subscriber_email_addresses: _Optional[_Iterable[str]]=..., state: _Optional[_Union[Case.State, str]]=..., create_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]]=..., update_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]]=..., creator: _Optional[_Union[_actor_pb2.Actor, _Mapping]]=..., contact_email: _Optional[str]=..., escalated: bool=..., test_case: bool=..., language_code: _Optional[str]=..., priority: _Optional[_Union[Case.Priority, str]]=...) -> None:
        ...

class CaseClassification(_message.Message):
    __slots__ = ('id', 'display_name')
    ID_FIELD_NUMBER: _ClassVar[int]
    DISPLAY_NAME_FIELD_NUMBER: _ClassVar[int]
    id: str
    display_name: str

    def __init__(self, id: _Optional[str]=..., display_name: _Optional[str]=...) -> None:
        ...