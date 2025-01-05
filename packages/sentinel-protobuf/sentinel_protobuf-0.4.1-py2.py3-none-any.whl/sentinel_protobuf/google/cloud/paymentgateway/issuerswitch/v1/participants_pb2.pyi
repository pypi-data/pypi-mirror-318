from google.api import annotations_pb2 as _annotations_pb2
from google.api import client_pb2 as _client_pb2
from google.api import field_behavior_pb2 as _field_behavior_pb2
from google.cloud.paymentgateway.issuerswitch.v1 import common_fields_pb2 as _common_fields_pb2
from google.protobuf import field_mask_pb2 as _field_mask_pb2
from google.protobuf import timestamp_pb2 as _timestamp_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union
DESCRIPTOR: _descriptor.FileDescriptor

class FetchParticipantRequest(_message.Message):
    __slots__ = ('parent', 'account_reference')
    PARENT_FIELD_NUMBER: _ClassVar[int]
    ACCOUNT_REFERENCE_FIELD_NUMBER: _ClassVar[int]
    parent: str
    account_reference: _common_fields_pb2.AccountReference

    def __init__(self, parent: _Optional[str]=..., account_reference: _Optional[_Union[_common_fields_pb2.AccountReference, _Mapping]]=...) -> None:
        ...

class IssuerParticipant(_message.Message):
    __slots__ = ('account_reference', 'mobile_number', 'state', 'metadata', 'mpin_failure_count', 'mpin_locked_time', 'create_time', 'update_time')

    class State(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        STATE_UNSPECIFIED: _ClassVar[IssuerParticipant.State]
        INACTIVE: _ClassVar[IssuerParticipant.State]
        ACTIVE: _ClassVar[IssuerParticipant.State]
        MPIN_LOCKED: _ClassVar[IssuerParticipant.State]
        MOBILE_NUMBER_CHANGED: _ClassVar[IssuerParticipant.State]
        NEW_REGISTRATION_INITIATED: _ClassVar[IssuerParticipant.State]
        RE_REGISTRATION_INITIATED: _ClassVar[IssuerParticipant.State]
    STATE_UNSPECIFIED: IssuerParticipant.State
    INACTIVE: IssuerParticipant.State
    ACTIVE: IssuerParticipant.State
    MPIN_LOCKED: IssuerParticipant.State
    MOBILE_NUMBER_CHANGED: IssuerParticipant.State
    NEW_REGISTRATION_INITIATED: IssuerParticipant.State
    RE_REGISTRATION_INITIATED: IssuerParticipant.State

    class Metadata(_message.Message):
        __slots__ = ('values',)

        class ValuesEntry(_message.Message):
            __slots__ = ('key', 'value')
            KEY_FIELD_NUMBER: _ClassVar[int]
            VALUE_FIELD_NUMBER: _ClassVar[int]
            key: str
            value: str

            def __init__(self, key: _Optional[str]=..., value: _Optional[str]=...) -> None:
                ...
        VALUES_FIELD_NUMBER: _ClassVar[int]
        values: _containers.ScalarMap[str, str]

        def __init__(self, values: _Optional[_Mapping[str, str]]=...) -> None:
            ...
    ACCOUNT_REFERENCE_FIELD_NUMBER: _ClassVar[int]
    MOBILE_NUMBER_FIELD_NUMBER: _ClassVar[int]
    STATE_FIELD_NUMBER: _ClassVar[int]
    METADATA_FIELD_NUMBER: _ClassVar[int]
    MPIN_FAILURE_COUNT_FIELD_NUMBER: _ClassVar[int]
    MPIN_LOCKED_TIME_FIELD_NUMBER: _ClassVar[int]
    CREATE_TIME_FIELD_NUMBER: _ClassVar[int]
    UPDATE_TIME_FIELD_NUMBER: _ClassVar[int]
    account_reference: _common_fields_pb2.AccountReference
    mobile_number: str
    state: IssuerParticipant.State
    metadata: IssuerParticipant.Metadata
    mpin_failure_count: int
    mpin_locked_time: _timestamp_pb2.Timestamp
    create_time: _timestamp_pb2.Timestamp
    update_time: _timestamp_pb2.Timestamp

    def __init__(self, account_reference: _Optional[_Union[_common_fields_pb2.AccountReference, _Mapping]]=..., mobile_number: _Optional[str]=..., state: _Optional[_Union[IssuerParticipant.State, str]]=..., metadata: _Optional[_Union[IssuerParticipant.Metadata, _Mapping]]=..., mpin_failure_count: _Optional[int]=..., mpin_locked_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]]=..., create_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]]=..., update_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]]=...) -> None:
        ...

class UpdateIssuerParticipantRequest(_message.Message):
    __slots__ = ('parent', 'issuer_participant', 'update_mask')
    PARENT_FIELD_NUMBER: _ClassVar[int]
    ISSUER_PARTICIPANT_FIELD_NUMBER: _ClassVar[int]
    UPDATE_MASK_FIELD_NUMBER: _ClassVar[int]
    parent: str
    issuer_participant: IssuerParticipant
    update_mask: _field_mask_pb2.FieldMask

    def __init__(self, parent: _Optional[str]=..., issuer_participant: _Optional[_Union[IssuerParticipant, _Mapping]]=..., update_mask: _Optional[_Union[_field_mask_pb2.FieldMask, _Mapping]]=...) -> None:
        ...

class ParticipantStateChangeRequest(_message.Message):
    __slots__ = ('parent', 'account_reference', 'mobile_number')
    PARENT_FIELD_NUMBER: _ClassVar[int]
    ACCOUNT_REFERENCE_FIELD_NUMBER: _ClassVar[int]
    MOBILE_NUMBER_FIELD_NUMBER: _ClassVar[int]
    parent: str
    account_reference: _common_fields_pb2.AccountReference
    mobile_number: str

    def __init__(self, parent: _Optional[str]=..., account_reference: _Optional[_Union[_common_fields_pb2.AccountReference, _Mapping]]=..., mobile_number: _Optional[str]=...) -> None:
        ...

class IssuerParticipants(_message.Message):
    __slots__ = ('participants',)
    PARTICIPANTS_FIELD_NUMBER: _ClassVar[int]
    participants: _containers.RepeatedCompositeFieldContainer[IssuerParticipant]

    def __init__(self, participants: _Optional[_Iterable[_Union[IssuerParticipant, _Mapping]]]=...) -> None:
        ...