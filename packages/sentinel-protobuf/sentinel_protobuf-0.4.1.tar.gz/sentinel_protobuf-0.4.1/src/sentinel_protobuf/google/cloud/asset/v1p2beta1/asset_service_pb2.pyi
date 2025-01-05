from google.api import annotations_pb2 as _annotations_pb2
from google.api import client_pb2 as _client_pb2
from google.api import field_behavior_pb2 as _field_behavior_pb2
from google.api import resource_pb2 as _resource_pb2
from google.cloud.asset.v1p2beta1 import assets_pb2 as _assets_pb2
from google.protobuf import empty_pb2 as _empty_pb2
from google.protobuf import field_mask_pb2 as _field_mask_pb2
from google.protobuf import timestamp_pb2 as _timestamp_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union
DESCRIPTOR: _descriptor.FileDescriptor

class ContentType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    CONTENT_TYPE_UNSPECIFIED: _ClassVar[ContentType]
    RESOURCE: _ClassVar[ContentType]
    IAM_POLICY: _ClassVar[ContentType]
CONTENT_TYPE_UNSPECIFIED: ContentType
RESOURCE: ContentType
IAM_POLICY: ContentType

class ExportAssetsResponse(_message.Message):
    __slots__ = ('read_time', 'output_config')
    READ_TIME_FIELD_NUMBER: _ClassVar[int]
    OUTPUT_CONFIG_FIELD_NUMBER: _ClassVar[int]
    read_time: _timestamp_pb2.Timestamp
    output_config: OutputConfig

    def __init__(self, read_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]]=..., output_config: _Optional[_Union[OutputConfig, _Mapping]]=...) -> None:
        ...

class BatchGetAssetsHistoryResponse(_message.Message):
    __slots__ = ('assets',)
    ASSETS_FIELD_NUMBER: _ClassVar[int]
    assets: _containers.RepeatedCompositeFieldContainer[_assets_pb2.TemporalAsset]

    def __init__(self, assets: _Optional[_Iterable[_Union[_assets_pb2.TemporalAsset, _Mapping]]]=...) -> None:
        ...

class CreateFeedRequest(_message.Message):
    __slots__ = ('parent', 'feed_id', 'feed')
    PARENT_FIELD_NUMBER: _ClassVar[int]
    FEED_ID_FIELD_NUMBER: _ClassVar[int]
    FEED_FIELD_NUMBER: _ClassVar[int]
    parent: str
    feed_id: str
    feed: Feed

    def __init__(self, parent: _Optional[str]=..., feed_id: _Optional[str]=..., feed: _Optional[_Union[Feed, _Mapping]]=...) -> None:
        ...

class GetFeedRequest(_message.Message):
    __slots__ = ('name',)
    NAME_FIELD_NUMBER: _ClassVar[int]
    name: str

    def __init__(self, name: _Optional[str]=...) -> None:
        ...

class ListFeedsRequest(_message.Message):
    __slots__ = ('parent',)
    PARENT_FIELD_NUMBER: _ClassVar[int]
    parent: str

    def __init__(self, parent: _Optional[str]=...) -> None:
        ...

class ListFeedsResponse(_message.Message):
    __slots__ = ('feeds',)
    FEEDS_FIELD_NUMBER: _ClassVar[int]
    feeds: _containers.RepeatedCompositeFieldContainer[Feed]

    def __init__(self, feeds: _Optional[_Iterable[_Union[Feed, _Mapping]]]=...) -> None:
        ...

class UpdateFeedRequest(_message.Message):
    __slots__ = ('feed', 'update_mask')
    FEED_FIELD_NUMBER: _ClassVar[int]
    UPDATE_MASK_FIELD_NUMBER: _ClassVar[int]
    feed: Feed
    update_mask: _field_mask_pb2.FieldMask

    def __init__(self, feed: _Optional[_Union[Feed, _Mapping]]=..., update_mask: _Optional[_Union[_field_mask_pb2.FieldMask, _Mapping]]=...) -> None:
        ...

class DeleteFeedRequest(_message.Message):
    __slots__ = ('name',)
    NAME_FIELD_NUMBER: _ClassVar[int]
    name: str

    def __init__(self, name: _Optional[str]=...) -> None:
        ...

class OutputConfig(_message.Message):
    __slots__ = ('gcs_destination',)
    GCS_DESTINATION_FIELD_NUMBER: _ClassVar[int]
    gcs_destination: GcsDestination

    def __init__(self, gcs_destination: _Optional[_Union[GcsDestination, _Mapping]]=...) -> None:
        ...

class GcsDestination(_message.Message):
    __slots__ = ('uri',)
    URI_FIELD_NUMBER: _ClassVar[int]
    uri: str

    def __init__(self, uri: _Optional[str]=...) -> None:
        ...

class PubsubDestination(_message.Message):
    __slots__ = ('topic',)
    TOPIC_FIELD_NUMBER: _ClassVar[int]
    topic: str

    def __init__(self, topic: _Optional[str]=...) -> None:
        ...

class FeedOutputConfig(_message.Message):
    __slots__ = ('pubsub_destination',)
    PUBSUB_DESTINATION_FIELD_NUMBER: _ClassVar[int]
    pubsub_destination: PubsubDestination

    def __init__(self, pubsub_destination: _Optional[_Union[PubsubDestination, _Mapping]]=...) -> None:
        ...

class Feed(_message.Message):
    __slots__ = ('name', 'asset_names', 'asset_types', 'content_type', 'feed_output_config')
    NAME_FIELD_NUMBER: _ClassVar[int]
    ASSET_NAMES_FIELD_NUMBER: _ClassVar[int]
    ASSET_TYPES_FIELD_NUMBER: _ClassVar[int]
    CONTENT_TYPE_FIELD_NUMBER: _ClassVar[int]
    FEED_OUTPUT_CONFIG_FIELD_NUMBER: _ClassVar[int]
    name: str
    asset_names: _containers.RepeatedScalarFieldContainer[str]
    asset_types: _containers.RepeatedScalarFieldContainer[str]
    content_type: ContentType
    feed_output_config: FeedOutputConfig

    def __init__(self, name: _Optional[str]=..., asset_names: _Optional[_Iterable[str]]=..., asset_types: _Optional[_Iterable[str]]=..., content_type: _Optional[_Union[ContentType, str]]=..., feed_output_config: _Optional[_Union[FeedOutputConfig, _Mapping]]=...) -> None:
        ...