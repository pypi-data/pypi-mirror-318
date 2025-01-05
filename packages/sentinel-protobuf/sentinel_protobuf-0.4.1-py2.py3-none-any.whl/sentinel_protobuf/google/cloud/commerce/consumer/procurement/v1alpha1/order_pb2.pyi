from google.api import field_behavior_pb2 as _field_behavior_pb2
from google.api import resource_pb2 as _resource_pb2
from google.protobuf import timestamp_pb2 as _timestamp_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union
DESCRIPTOR: _descriptor.FileDescriptor

class LineItemChangeType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    LINE_ITEM_CHANGE_TYPE_UNSPECIFIED: _ClassVar[LineItemChangeType]
    LINE_ITEM_CHANGE_TYPE_CREATE: _ClassVar[LineItemChangeType]
    LINE_ITEM_CHANGE_TYPE_UPDATE: _ClassVar[LineItemChangeType]
    LINE_ITEM_CHANGE_TYPE_CANCEL: _ClassVar[LineItemChangeType]
    LINE_ITEM_CHANGE_TYPE_REVERT_CANCELLATION: _ClassVar[LineItemChangeType]

class LineItemChangeState(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    LINE_ITEM_CHANGE_STATE_UNSPECIFIED: _ClassVar[LineItemChangeState]
    LINE_ITEM_CHANGE_STATE_PENDING_APPROVAL: _ClassVar[LineItemChangeState]
    LINE_ITEM_CHANGE_STATE_APPROVED: _ClassVar[LineItemChangeState]
    LINE_ITEM_CHANGE_STATE_COMPLETED: _ClassVar[LineItemChangeState]
    LINE_ITEM_CHANGE_STATE_REJECTED: _ClassVar[LineItemChangeState]
    LINE_ITEM_CHANGE_STATE_ABANDONED: _ClassVar[LineItemChangeState]
    LINE_ITEM_CHANGE_STATE_ACTIVATING: _ClassVar[LineItemChangeState]

class LineItemChangeStateReasonType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    LINE_ITEM_CHANGE_STATE_REASON_TYPE_UNSPECIFIED: _ClassVar[LineItemChangeStateReasonType]
    LINE_ITEM_CHANGE_STATE_REASON_TYPE_EXPIRED: _ClassVar[LineItemChangeStateReasonType]
    LINE_ITEM_CHANGE_STATE_REASON_TYPE_USER_CANCELLED: _ClassVar[LineItemChangeStateReasonType]
    LINE_ITEM_CHANGE_STATE_REASON_TYPE_SYSTEM_CANCELLED: _ClassVar[LineItemChangeStateReasonType]
LINE_ITEM_CHANGE_TYPE_UNSPECIFIED: LineItemChangeType
LINE_ITEM_CHANGE_TYPE_CREATE: LineItemChangeType
LINE_ITEM_CHANGE_TYPE_UPDATE: LineItemChangeType
LINE_ITEM_CHANGE_TYPE_CANCEL: LineItemChangeType
LINE_ITEM_CHANGE_TYPE_REVERT_CANCELLATION: LineItemChangeType
LINE_ITEM_CHANGE_STATE_UNSPECIFIED: LineItemChangeState
LINE_ITEM_CHANGE_STATE_PENDING_APPROVAL: LineItemChangeState
LINE_ITEM_CHANGE_STATE_APPROVED: LineItemChangeState
LINE_ITEM_CHANGE_STATE_COMPLETED: LineItemChangeState
LINE_ITEM_CHANGE_STATE_REJECTED: LineItemChangeState
LINE_ITEM_CHANGE_STATE_ABANDONED: LineItemChangeState
LINE_ITEM_CHANGE_STATE_ACTIVATING: LineItemChangeState
LINE_ITEM_CHANGE_STATE_REASON_TYPE_UNSPECIFIED: LineItemChangeStateReasonType
LINE_ITEM_CHANGE_STATE_REASON_TYPE_EXPIRED: LineItemChangeStateReasonType
LINE_ITEM_CHANGE_STATE_REASON_TYPE_USER_CANCELLED: LineItemChangeStateReasonType
LINE_ITEM_CHANGE_STATE_REASON_TYPE_SYSTEM_CANCELLED: LineItemChangeStateReasonType

class Order(_message.Message):
    __slots__ = ('name', 'display_name', 'line_items', 'cancelled_line_items', 'create_time', 'update_time', 'etag')
    NAME_FIELD_NUMBER: _ClassVar[int]
    DISPLAY_NAME_FIELD_NUMBER: _ClassVar[int]
    LINE_ITEMS_FIELD_NUMBER: _ClassVar[int]
    CANCELLED_LINE_ITEMS_FIELD_NUMBER: _ClassVar[int]
    CREATE_TIME_FIELD_NUMBER: _ClassVar[int]
    UPDATE_TIME_FIELD_NUMBER: _ClassVar[int]
    ETAG_FIELD_NUMBER: _ClassVar[int]
    name: str
    display_name: str
    line_items: _containers.RepeatedCompositeFieldContainer[LineItem]
    cancelled_line_items: _containers.RepeatedCompositeFieldContainer[LineItem]
    create_time: _timestamp_pb2.Timestamp
    update_time: _timestamp_pb2.Timestamp
    etag: str

    def __init__(self, name: _Optional[str]=..., display_name: _Optional[str]=..., line_items: _Optional[_Iterable[_Union[LineItem, _Mapping]]]=..., cancelled_line_items: _Optional[_Iterable[_Union[LineItem, _Mapping]]]=..., create_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]]=..., update_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]]=..., etag: _Optional[str]=...) -> None:
        ...

class LineItem(_message.Message):
    __slots__ = ('line_item_id', 'line_item_info', 'pending_change', 'change_history')
    LINE_ITEM_ID_FIELD_NUMBER: _ClassVar[int]
    LINE_ITEM_INFO_FIELD_NUMBER: _ClassVar[int]
    PENDING_CHANGE_FIELD_NUMBER: _ClassVar[int]
    CHANGE_HISTORY_FIELD_NUMBER: _ClassVar[int]
    line_item_id: str
    line_item_info: LineItemInfo
    pending_change: LineItemChange
    change_history: _containers.RepeatedCompositeFieldContainer[LineItemChange]

    def __init__(self, line_item_id: _Optional[str]=..., line_item_info: _Optional[_Union[LineItemInfo, _Mapping]]=..., pending_change: _Optional[_Union[LineItemChange, _Mapping]]=..., change_history: _Optional[_Iterable[_Union[LineItemChange, _Mapping]]]=...) -> None:
        ...

class LineItemChange(_message.Message):
    __slots__ = ('change_id', 'change_type', 'old_line_item_info', 'new_line_item_info', 'change_state', 'state_reason', 'change_state_reason_type', 'change_effective_time', 'create_time', 'update_time')
    CHANGE_ID_FIELD_NUMBER: _ClassVar[int]
    CHANGE_TYPE_FIELD_NUMBER: _ClassVar[int]
    OLD_LINE_ITEM_INFO_FIELD_NUMBER: _ClassVar[int]
    NEW_LINE_ITEM_INFO_FIELD_NUMBER: _ClassVar[int]
    CHANGE_STATE_FIELD_NUMBER: _ClassVar[int]
    STATE_REASON_FIELD_NUMBER: _ClassVar[int]
    CHANGE_STATE_REASON_TYPE_FIELD_NUMBER: _ClassVar[int]
    CHANGE_EFFECTIVE_TIME_FIELD_NUMBER: _ClassVar[int]
    CREATE_TIME_FIELD_NUMBER: _ClassVar[int]
    UPDATE_TIME_FIELD_NUMBER: _ClassVar[int]
    change_id: str
    change_type: LineItemChangeType
    old_line_item_info: LineItemInfo
    new_line_item_info: LineItemInfo
    change_state: LineItemChangeState
    state_reason: str
    change_state_reason_type: LineItemChangeStateReasonType
    change_effective_time: _timestamp_pb2.Timestamp
    create_time: _timestamp_pb2.Timestamp
    update_time: _timestamp_pb2.Timestamp

    def __init__(self, change_id: _Optional[str]=..., change_type: _Optional[_Union[LineItemChangeType, str]]=..., old_line_item_info: _Optional[_Union[LineItemInfo, _Mapping]]=..., new_line_item_info: _Optional[_Union[LineItemInfo, _Mapping]]=..., change_state: _Optional[_Union[LineItemChangeState, str]]=..., state_reason: _Optional[str]=..., change_state_reason_type: _Optional[_Union[LineItemChangeStateReasonType, str]]=..., change_effective_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]]=..., create_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]]=..., update_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]]=...) -> None:
        ...

class LineItemInfo(_message.Message):
    __slots__ = ('offer', 'parameters', 'subscription')
    OFFER_FIELD_NUMBER: _ClassVar[int]
    PARAMETERS_FIELD_NUMBER: _ClassVar[int]
    SUBSCRIPTION_FIELD_NUMBER: _ClassVar[int]
    offer: str
    parameters: _containers.RepeatedCompositeFieldContainer[Parameter]
    subscription: Subscription

    def __init__(self, offer: _Optional[str]=..., parameters: _Optional[_Iterable[_Union[Parameter, _Mapping]]]=..., subscription: _Optional[_Union[Subscription, _Mapping]]=...) -> None:
        ...

class Parameter(_message.Message):
    __slots__ = ('name', 'value')

    class Value(_message.Message):
        __slots__ = ('int64_value', 'string_value', 'double_value')
        INT64_VALUE_FIELD_NUMBER: _ClassVar[int]
        STRING_VALUE_FIELD_NUMBER: _ClassVar[int]
        DOUBLE_VALUE_FIELD_NUMBER: _ClassVar[int]
        int64_value: int
        string_value: str
        double_value: float

        def __init__(self, int64_value: _Optional[int]=..., string_value: _Optional[str]=..., double_value: _Optional[float]=...) -> None:
            ...
    NAME_FIELD_NUMBER: _ClassVar[int]
    VALUE_FIELD_NUMBER: _ClassVar[int]
    name: str
    value: Parameter.Value

    def __init__(self, name: _Optional[str]=..., value: _Optional[_Union[Parameter.Value, _Mapping]]=...) -> None:
        ...

class Subscription(_message.Message):
    __slots__ = ('start_time', 'end_time', 'auto_renewal_enabled')
    START_TIME_FIELD_NUMBER: _ClassVar[int]
    END_TIME_FIELD_NUMBER: _ClassVar[int]
    AUTO_RENEWAL_ENABLED_FIELD_NUMBER: _ClassVar[int]
    start_time: _timestamp_pb2.Timestamp
    end_time: _timestamp_pb2.Timestamp
    auto_renewal_enabled: bool

    def __init__(self, start_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]]=..., end_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]]=..., auto_renewal_enabled: bool=...) -> None:
        ...