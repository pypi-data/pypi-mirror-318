from google.api import field_behavior_pb2 as _field_behavior_pb2
from google.api import resource_pb2 as _resource_pb2
from google.protobuf import timestamp_pb2 as _timestamp_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union
DESCRIPTOR: _descriptor.FileDescriptor

class MerchantCenterAccountLink(_message.Message):
    __slots__ = ('name', 'id', 'merchant_center_account_id', 'branch_id', 'feed_label', 'language_code', 'feed_filters', 'state', 'project_id', 'source')

    class State(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        STATE_UNSPECIFIED: _ClassVar[MerchantCenterAccountLink.State]
        PENDING: _ClassVar[MerchantCenterAccountLink.State]
        ACTIVE: _ClassVar[MerchantCenterAccountLink.State]
        FAILED: _ClassVar[MerchantCenterAccountLink.State]
    STATE_UNSPECIFIED: MerchantCenterAccountLink.State
    PENDING: MerchantCenterAccountLink.State
    ACTIVE: MerchantCenterAccountLink.State
    FAILED: MerchantCenterAccountLink.State

    class MerchantCenterFeedFilter(_message.Message):
        __slots__ = ('primary_feed_id', 'primary_feed_name')
        PRIMARY_FEED_ID_FIELD_NUMBER: _ClassVar[int]
        PRIMARY_FEED_NAME_FIELD_NUMBER: _ClassVar[int]
        primary_feed_id: int
        primary_feed_name: str

        def __init__(self, primary_feed_id: _Optional[int]=..., primary_feed_name: _Optional[str]=...) -> None:
            ...
    NAME_FIELD_NUMBER: _ClassVar[int]
    ID_FIELD_NUMBER: _ClassVar[int]
    MERCHANT_CENTER_ACCOUNT_ID_FIELD_NUMBER: _ClassVar[int]
    BRANCH_ID_FIELD_NUMBER: _ClassVar[int]
    FEED_LABEL_FIELD_NUMBER: _ClassVar[int]
    LANGUAGE_CODE_FIELD_NUMBER: _ClassVar[int]
    FEED_FILTERS_FIELD_NUMBER: _ClassVar[int]
    STATE_FIELD_NUMBER: _ClassVar[int]
    PROJECT_ID_FIELD_NUMBER: _ClassVar[int]
    SOURCE_FIELD_NUMBER: _ClassVar[int]
    name: str
    id: str
    merchant_center_account_id: int
    branch_id: str
    feed_label: str
    language_code: str
    feed_filters: _containers.RepeatedCompositeFieldContainer[MerchantCenterAccountLink.MerchantCenterFeedFilter]
    state: MerchantCenterAccountLink.State
    project_id: str
    source: str

    def __init__(self, name: _Optional[str]=..., id: _Optional[str]=..., merchant_center_account_id: _Optional[int]=..., branch_id: _Optional[str]=..., feed_label: _Optional[str]=..., language_code: _Optional[str]=..., feed_filters: _Optional[_Iterable[_Union[MerchantCenterAccountLink.MerchantCenterFeedFilter, _Mapping]]]=..., state: _Optional[_Union[MerchantCenterAccountLink.State, str]]=..., project_id: _Optional[str]=..., source: _Optional[str]=...) -> None:
        ...

class CreateMerchantCenterAccountLinkMetadata(_message.Message):
    __slots__ = ('create_time', 'update_time')
    CREATE_TIME_FIELD_NUMBER: _ClassVar[int]
    UPDATE_TIME_FIELD_NUMBER: _ClassVar[int]
    create_time: _timestamp_pb2.Timestamp
    update_time: _timestamp_pb2.Timestamp

    def __init__(self, create_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]]=..., update_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]]=...) -> None:
        ...