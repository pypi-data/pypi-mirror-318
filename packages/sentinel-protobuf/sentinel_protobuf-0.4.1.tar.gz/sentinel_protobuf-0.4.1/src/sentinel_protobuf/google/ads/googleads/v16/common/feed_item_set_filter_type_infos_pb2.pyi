from google.ads.googleads.v16.enums import feed_item_set_string_filter_type_pb2 as _feed_item_set_string_filter_type_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union
DESCRIPTOR: _descriptor.FileDescriptor

class DynamicLocationSetFilter(_message.Message):
    __slots__ = ('labels', 'business_name_filter')
    LABELS_FIELD_NUMBER: _ClassVar[int]
    BUSINESS_NAME_FILTER_FIELD_NUMBER: _ClassVar[int]
    labels: _containers.RepeatedScalarFieldContainer[str]
    business_name_filter: BusinessNameFilter

    def __init__(self, labels: _Optional[_Iterable[str]]=..., business_name_filter: _Optional[_Union[BusinessNameFilter, _Mapping]]=...) -> None:
        ...

class BusinessNameFilter(_message.Message):
    __slots__ = ('business_name', 'filter_type')
    BUSINESS_NAME_FIELD_NUMBER: _ClassVar[int]
    FILTER_TYPE_FIELD_NUMBER: _ClassVar[int]
    business_name: str
    filter_type: _feed_item_set_string_filter_type_pb2.FeedItemSetStringFilterTypeEnum.FeedItemSetStringFilterType

    def __init__(self, business_name: _Optional[str]=..., filter_type: _Optional[_Union[_feed_item_set_string_filter_type_pb2.FeedItemSetStringFilterTypeEnum.FeedItemSetStringFilterType, str]]=...) -> None:
        ...

class DynamicAffiliateLocationSetFilter(_message.Message):
    __slots__ = ('chain_ids',)
    CHAIN_IDS_FIELD_NUMBER: _ClassVar[int]
    chain_ids: _containers.RepeatedScalarFieldContainer[int]

    def __init__(self, chain_ids: _Optional[_Iterable[int]]=...) -> None:
        ...