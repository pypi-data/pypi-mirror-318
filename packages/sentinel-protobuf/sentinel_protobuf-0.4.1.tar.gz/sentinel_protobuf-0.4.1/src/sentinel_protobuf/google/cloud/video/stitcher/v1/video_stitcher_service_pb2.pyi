from google.api import annotations_pb2 as _annotations_pb2
from google.api import client_pb2 as _client_pb2
from google.api import field_behavior_pb2 as _field_behavior_pb2
from google.api import resource_pb2 as _resource_pb2
from google.cloud.video.stitcher.v1 import ad_tag_details_pb2 as _ad_tag_details_pb2
from google.cloud.video.stitcher.v1 import cdn_keys_pb2 as _cdn_keys_pb2
from google.cloud.video.stitcher.v1 import live_configs_pb2 as _live_configs_pb2
from google.cloud.video.stitcher.v1 import sessions_pb2 as _sessions_pb2
from google.cloud.video.stitcher.v1 import slates_pb2 as _slates_pb2
from google.cloud.video.stitcher.v1 import stitch_details_pb2 as _stitch_details_pb2
from google.cloud.video.stitcher.v1 import vod_configs_pb2 as _vod_configs_pb2
from google.longrunning import operations_pb2 as _operations_pb2
from google.protobuf import empty_pb2 as _empty_pb2
from google.protobuf import field_mask_pb2 as _field_mask_pb2
from google.protobuf import timestamp_pb2 as _timestamp_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union
DESCRIPTOR: _descriptor.FileDescriptor

class CreateCdnKeyRequest(_message.Message):
    __slots__ = ('parent', 'cdn_key', 'cdn_key_id')
    PARENT_FIELD_NUMBER: _ClassVar[int]
    CDN_KEY_FIELD_NUMBER: _ClassVar[int]
    CDN_KEY_ID_FIELD_NUMBER: _ClassVar[int]
    parent: str
    cdn_key: _cdn_keys_pb2.CdnKey
    cdn_key_id: str

    def __init__(self, parent: _Optional[str]=..., cdn_key: _Optional[_Union[_cdn_keys_pb2.CdnKey, _Mapping]]=..., cdn_key_id: _Optional[str]=...) -> None:
        ...

class ListCdnKeysRequest(_message.Message):
    __slots__ = ('parent', 'page_size', 'page_token', 'filter', 'order_by')
    PARENT_FIELD_NUMBER: _ClassVar[int]
    PAGE_SIZE_FIELD_NUMBER: _ClassVar[int]
    PAGE_TOKEN_FIELD_NUMBER: _ClassVar[int]
    FILTER_FIELD_NUMBER: _ClassVar[int]
    ORDER_BY_FIELD_NUMBER: _ClassVar[int]
    parent: str
    page_size: int
    page_token: str
    filter: str
    order_by: str

    def __init__(self, parent: _Optional[str]=..., page_size: _Optional[int]=..., page_token: _Optional[str]=..., filter: _Optional[str]=..., order_by: _Optional[str]=...) -> None:
        ...

class ListCdnKeysResponse(_message.Message):
    __slots__ = ('cdn_keys', 'next_page_token', 'unreachable')
    CDN_KEYS_FIELD_NUMBER: _ClassVar[int]
    NEXT_PAGE_TOKEN_FIELD_NUMBER: _ClassVar[int]
    UNREACHABLE_FIELD_NUMBER: _ClassVar[int]
    cdn_keys: _containers.RepeatedCompositeFieldContainer[_cdn_keys_pb2.CdnKey]
    next_page_token: str
    unreachable: _containers.RepeatedScalarFieldContainer[str]

    def __init__(self, cdn_keys: _Optional[_Iterable[_Union[_cdn_keys_pb2.CdnKey, _Mapping]]]=..., next_page_token: _Optional[str]=..., unreachable: _Optional[_Iterable[str]]=...) -> None:
        ...

class GetCdnKeyRequest(_message.Message):
    __slots__ = ('name',)
    NAME_FIELD_NUMBER: _ClassVar[int]
    name: str

    def __init__(self, name: _Optional[str]=...) -> None:
        ...

class DeleteCdnKeyRequest(_message.Message):
    __slots__ = ('name',)
    NAME_FIELD_NUMBER: _ClassVar[int]
    name: str

    def __init__(self, name: _Optional[str]=...) -> None:
        ...

class UpdateCdnKeyRequest(_message.Message):
    __slots__ = ('cdn_key', 'update_mask')
    CDN_KEY_FIELD_NUMBER: _ClassVar[int]
    UPDATE_MASK_FIELD_NUMBER: _ClassVar[int]
    cdn_key: _cdn_keys_pb2.CdnKey
    update_mask: _field_mask_pb2.FieldMask

    def __init__(self, cdn_key: _Optional[_Union[_cdn_keys_pb2.CdnKey, _Mapping]]=..., update_mask: _Optional[_Union[_field_mask_pb2.FieldMask, _Mapping]]=...) -> None:
        ...

class CreateVodSessionRequest(_message.Message):
    __slots__ = ('parent', 'vod_session')
    PARENT_FIELD_NUMBER: _ClassVar[int]
    VOD_SESSION_FIELD_NUMBER: _ClassVar[int]
    parent: str
    vod_session: _sessions_pb2.VodSession

    def __init__(self, parent: _Optional[str]=..., vod_session: _Optional[_Union[_sessions_pb2.VodSession, _Mapping]]=...) -> None:
        ...

class GetVodSessionRequest(_message.Message):
    __slots__ = ('name',)
    NAME_FIELD_NUMBER: _ClassVar[int]
    name: str

    def __init__(self, name: _Optional[str]=...) -> None:
        ...

class ListVodStitchDetailsRequest(_message.Message):
    __slots__ = ('parent', 'page_size', 'page_token')
    PARENT_FIELD_NUMBER: _ClassVar[int]
    PAGE_SIZE_FIELD_NUMBER: _ClassVar[int]
    PAGE_TOKEN_FIELD_NUMBER: _ClassVar[int]
    parent: str
    page_size: int
    page_token: str

    def __init__(self, parent: _Optional[str]=..., page_size: _Optional[int]=..., page_token: _Optional[str]=...) -> None:
        ...

class ListVodStitchDetailsResponse(_message.Message):
    __slots__ = ('vod_stitch_details', 'next_page_token')
    VOD_STITCH_DETAILS_FIELD_NUMBER: _ClassVar[int]
    NEXT_PAGE_TOKEN_FIELD_NUMBER: _ClassVar[int]
    vod_stitch_details: _containers.RepeatedCompositeFieldContainer[_stitch_details_pb2.VodStitchDetail]
    next_page_token: str

    def __init__(self, vod_stitch_details: _Optional[_Iterable[_Union[_stitch_details_pb2.VodStitchDetail, _Mapping]]]=..., next_page_token: _Optional[str]=...) -> None:
        ...

class GetVodStitchDetailRequest(_message.Message):
    __slots__ = ('name',)
    NAME_FIELD_NUMBER: _ClassVar[int]
    name: str

    def __init__(self, name: _Optional[str]=...) -> None:
        ...

class ListVodAdTagDetailsRequest(_message.Message):
    __slots__ = ('parent', 'page_size', 'page_token')
    PARENT_FIELD_NUMBER: _ClassVar[int]
    PAGE_SIZE_FIELD_NUMBER: _ClassVar[int]
    PAGE_TOKEN_FIELD_NUMBER: _ClassVar[int]
    parent: str
    page_size: int
    page_token: str

    def __init__(self, parent: _Optional[str]=..., page_size: _Optional[int]=..., page_token: _Optional[str]=...) -> None:
        ...

class ListVodAdTagDetailsResponse(_message.Message):
    __slots__ = ('vod_ad_tag_details', 'next_page_token')
    VOD_AD_TAG_DETAILS_FIELD_NUMBER: _ClassVar[int]
    NEXT_PAGE_TOKEN_FIELD_NUMBER: _ClassVar[int]
    vod_ad_tag_details: _containers.RepeatedCompositeFieldContainer[_ad_tag_details_pb2.VodAdTagDetail]
    next_page_token: str

    def __init__(self, vod_ad_tag_details: _Optional[_Iterable[_Union[_ad_tag_details_pb2.VodAdTagDetail, _Mapping]]]=..., next_page_token: _Optional[str]=...) -> None:
        ...

class GetVodAdTagDetailRequest(_message.Message):
    __slots__ = ('name',)
    NAME_FIELD_NUMBER: _ClassVar[int]
    name: str

    def __init__(self, name: _Optional[str]=...) -> None:
        ...

class ListLiveAdTagDetailsRequest(_message.Message):
    __slots__ = ('parent', 'page_size', 'page_token')
    PARENT_FIELD_NUMBER: _ClassVar[int]
    PAGE_SIZE_FIELD_NUMBER: _ClassVar[int]
    PAGE_TOKEN_FIELD_NUMBER: _ClassVar[int]
    parent: str
    page_size: int
    page_token: str

    def __init__(self, parent: _Optional[str]=..., page_size: _Optional[int]=..., page_token: _Optional[str]=...) -> None:
        ...

class ListLiveAdTagDetailsResponse(_message.Message):
    __slots__ = ('live_ad_tag_details', 'next_page_token')
    LIVE_AD_TAG_DETAILS_FIELD_NUMBER: _ClassVar[int]
    NEXT_PAGE_TOKEN_FIELD_NUMBER: _ClassVar[int]
    live_ad_tag_details: _containers.RepeatedCompositeFieldContainer[_ad_tag_details_pb2.LiveAdTagDetail]
    next_page_token: str

    def __init__(self, live_ad_tag_details: _Optional[_Iterable[_Union[_ad_tag_details_pb2.LiveAdTagDetail, _Mapping]]]=..., next_page_token: _Optional[str]=...) -> None:
        ...

class GetLiveAdTagDetailRequest(_message.Message):
    __slots__ = ('name',)
    NAME_FIELD_NUMBER: _ClassVar[int]
    name: str

    def __init__(self, name: _Optional[str]=...) -> None:
        ...

class CreateSlateRequest(_message.Message):
    __slots__ = ('parent', 'slate_id', 'slate', 'request_id')
    PARENT_FIELD_NUMBER: _ClassVar[int]
    SLATE_ID_FIELD_NUMBER: _ClassVar[int]
    SLATE_FIELD_NUMBER: _ClassVar[int]
    REQUEST_ID_FIELD_NUMBER: _ClassVar[int]
    parent: str
    slate_id: str
    slate: _slates_pb2.Slate
    request_id: str

    def __init__(self, parent: _Optional[str]=..., slate_id: _Optional[str]=..., slate: _Optional[_Union[_slates_pb2.Slate, _Mapping]]=..., request_id: _Optional[str]=...) -> None:
        ...

class GetSlateRequest(_message.Message):
    __slots__ = ('name',)
    NAME_FIELD_NUMBER: _ClassVar[int]
    name: str

    def __init__(self, name: _Optional[str]=...) -> None:
        ...

class ListSlatesRequest(_message.Message):
    __slots__ = ('parent', 'page_size', 'page_token', 'filter', 'order_by')
    PARENT_FIELD_NUMBER: _ClassVar[int]
    PAGE_SIZE_FIELD_NUMBER: _ClassVar[int]
    PAGE_TOKEN_FIELD_NUMBER: _ClassVar[int]
    FILTER_FIELD_NUMBER: _ClassVar[int]
    ORDER_BY_FIELD_NUMBER: _ClassVar[int]
    parent: str
    page_size: int
    page_token: str
    filter: str
    order_by: str

    def __init__(self, parent: _Optional[str]=..., page_size: _Optional[int]=..., page_token: _Optional[str]=..., filter: _Optional[str]=..., order_by: _Optional[str]=...) -> None:
        ...

class ListSlatesResponse(_message.Message):
    __slots__ = ('slates', 'next_page_token', 'unreachable')
    SLATES_FIELD_NUMBER: _ClassVar[int]
    NEXT_PAGE_TOKEN_FIELD_NUMBER: _ClassVar[int]
    UNREACHABLE_FIELD_NUMBER: _ClassVar[int]
    slates: _containers.RepeatedCompositeFieldContainer[_slates_pb2.Slate]
    next_page_token: str
    unreachable: _containers.RepeatedScalarFieldContainer[str]

    def __init__(self, slates: _Optional[_Iterable[_Union[_slates_pb2.Slate, _Mapping]]]=..., next_page_token: _Optional[str]=..., unreachable: _Optional[_Iterable[str]]=...) -> None:
        ...

class UpdateSlateRequest(_message.Message):
    __slots__ = ('slate', 'update_mask')
    SLATE_FIELD_NUMBER: _ClassVar[int]
    UPDATE_MASK_FIELD_NUMBER: _ClassVar[int]
    slate: _slates_pb2.Slate
    update_mask: _field_mask_pb2.FieldMask

    def __init__(self, slate: _Optional[_Union[_slates_pb2.Slate, _Mapping]]=..., update_mask: _Optional[_Union[_field_mask_pb2.FieldMask, _Mapping]]=...) -> None:
        ...

class DeleteSlateRequest(_message.Message):
    __slots__ = ('name',)
    NAME_FIELD_NUMBER: _ClassVar[int]
    name: str

    def __init__(self, name: _Optional[str]=...) -> None:
        ...

class CreateLiveSessionRequest(_message.Message):
    __slots__ = ('parent', 'live_session')
    PARENT_FIELD_NUMBER: _ClassVar[int]
    LIVE_SESSION_FIELD_NUMBER: _ClassVar[int]
    parent: str
    live_session: _sessions_pb2.LiveSession

    def __init__(self, parent: _Optional[str]=..., live_session: _Optional[_Union[_sessions_pb2.LiveSession, _Mapping]]=...) -> None:
        ...

class GetLiveSessionRequest(_message.Message):
    __slots__ = ('name',)
    NAME_FIELD_NUMBER: _ClassVar[int]
    name: str

    def __init__(self, name: _Optional[str]=...) -> None:
        ...

class CreateLiveConfigRequest(_message.Message):
    __slots__ = ('parent', 'live_config_id', 'live_config', 'request_id')
    PARENT_FIELD_NUMBER: _ClassVar[int]
    LIVE_CONFIG_ID_FIELD_NUMBER: _ClassVar[int]
    LIVE_CONFIG_FIELD_NUMBER: _ClassVar[int]
    REQUEST_ID_FIELD_NUMBER: _ClassVar[int]
    parent: str
    live_config_id: str
    live_config: _live_configs_pb2.LiveConfig
    request_id: str

    def __init__(self, parent: _Optional[str]=..., live_config_id: _Optional[str]=..., live_config: _Optional[_Union[_live_configs_pb2.LiveConfig, _Mapping]]=..., request_id: _Optional[str]=...) -> None:
        ...

class ListLiveConfigsRequest(_message.Message):
    __slots__ = ('parent', 'page_size', 'page_token', 'filter', 'order_by')
    PARENT_FIELD_NUMBER: _ClassVar[int]
    PAGE_SIZE_FIELD_NUMBER: _ClassVar[int]
    PAGE_TOKEN_FIELD_NUMBER: _ClassVar[int]
    FILTER_FIELD_NUMBER: _ClassVar[int]
    ORDER_BY_FIELD_NUMBER: _ClassVar[int]
    parent: str
    page_size: int
    page_token: str
    filter: str
    order_by: str

    def __init__(self, parent: _Optional[str]=..., page_size: _Optional[int]=..., page_token: _Optional[str]=..., filter: _Optional[str]=..., order_by: _Optional[str]=...) -> None:
        ...

class ListLiveConfigsResponse(_message.Message):
    __slots__ = ('live_configs', 'next_page_token', 'unreachable')
    LIVE_CONFIGS_FIELD_NUMBER: _ClassVar[int]
    NEXT_PAGE_TOKEN_FIELD_NUMBER: _ClassVar[int]
    UNREACHABLE_FIELD_NUMBER: _ClassVar[int]
    live_configs: _containers.RepeatedCompositeFieldContainer[_live_configs_pb2.LiveConfig]
    next_page_token: str
    unreachable: _containers.RepeatedScalarFieldContainer[str]

    def __init__(self, live_configs: _Optional[_Iterable[_Union[_live_configs_pb2.LiveConfig, _Mapping]]]=..., next_page_token: _Optional[str]=..., unreachable: _Optional[_Iterable[str]]=...) -> None:
        ...

class GetLiveConfigRequest(_message.Message):
    __slots__ = ('name',)
    NAME_FIELD_NUMBER: _ClassVar[int]
    name: str

    def __init__(self, name: _Optional[str]=...) -> None:
        ...

class DeleteLiveConfigRequest(_message.Message):
    __slots__ = ('name',)
    NAME_FIELD_NUMBER: _ClassVar[int]
    name: str

    def __init__(self, name: _Optional[str]=...) -> None:
        ...

class UpdateLiveConfigRequest(_message.Message):
    __slots__ = ('live_config', 'update_mask')
    LIVE_CONFIG_FIELD_NUMBER: _ClassVar[int]
    UPDATE_MASK_FIELD_NUMBER: _ClassVar[int]
    live_config: _live_configs_pb2.LiveConfig
    update_mask: _field_mask_pb2.FieldMask

    def __init__(self, live_config: _Optional[_Union[_live_configs_pb2.LiveConfig, _Mapping]]=..., update_mask: _Optional[_Union[_field_mask_pb2.FieldMask, _Mapping]]=...) -> None:
        ...

class CreateVodConfigRequest(_message.Message):
    __slots__ = ('parent', 'vod_config_id', 'vod_config', 'request_id')
    PARENT_FIELD_NUMBER: _ClassVar[int]
    VOD_CONFIG_ID_FIELD_NUMBER: _ClassVar[int]
    VOD_CONFIG_FIELD_NUMBER: _ClassVar[int]
    REQUEST_ID_FIELD_NUMBER: _ClassVar[int]
    parent: str
    vod_config_id: str
    vod_config: _vod_configs_pb2.VodConfig
    request_id: str

    def __init__(self, parent: _Optional[str]=..., vod_config_id: _Optional[str]=..., vod_config: _Optional[_Union[_vod_configs_pb2.VodConfig, _Mapping]]=..., request_id: _Optional[str]=...) -> None:
        ...

class ListVodConfigsRequest(_message.Message):
    __slots__ = ('parent', 'page_size', 'page_token', 'filter', 'order_by')
    PARENT_FIELD_NUMBER: _ClassVar[int]
    PAGE_SIZE_FIELD_NUMBER: _ClassVar[int]
    PAGE_TOKEN_FIELD_NUMBER: _ClassVar[int]
    FILTER_FIELD_NUMBER: _ClassVar[int]
    ORDER_BY_FIELD_NUMBER: _ClassVar[int]
    parent: str
    page_size: int
    page_token: str
    filter: str
    order_by: str

    def __init__(self, parent: _Optional[str]=..., page_size: _Optional[int]=..., page_token: _Optional[str]=..., filter: _Optional[str]=..., order_by: _Optional[str]=...) -> None:
        ...

class ListVodConfigsResponse(_message.Message):
    __slots__ = ('vod_configs', 'next_page_token', 'unreachable')
    VOD_CONFIGS_FIELD_NUMBER: _ClassVar[int]
    NEXT_PAGE_TOKEN_FIELD_NUMBER: _ClassVar[int]
    UNREACHABLE_FIELD_NUMBER: _ClassVar[int]
    vod_configs: _containers.RepeatedCompositeFieldContainer[_vod_configs_pb2.VodConfig]
    next_page_token: str
    unreachable: _containers.RepeatedScalarFieldContainer[str]

    def __init__(self, vod_configs: _Optional[_Iterable[_Union[_vod_configs_pb2.VodConfig, _Mapping]]]=..., next_page_token: _Optional[str]=..., unreachable: _Optional[_Iterable[str]]=...) -> None:
        ...

class GetVodConfigRequest(_message.Message):
    __slots__ = ('name',)
    NAME_FIELD_NUMBER: _ClassVar[int]
    name: str

    def __init__(self, name: _Optional[str]=...) -> None:
        ...

class DeleteVodConfigRequest(_message.Message):
    __slots__ = ('name',)
    NAME_FIELD_NUMBER: _ClassVar[int]
    name: str

    def __init__(self, name: _Optional[str]=...) -> None:
        ...

class UpdateVodConfigRequest(_message.Message):
    __slots__ = ('vod_config', 'update_mask')
    VOD_CONFIG_FIELD_NUMBER: _ClassVar[int]
    UPDATE_MASK_FIELD_NUMBER: _ClassVar[int]
    vod_config: _vod_configs_pb2.VodConfig
    update_mask: _field_mask_pb2.FieldMask

    def __init__(self, vod_config: _Optional[_Union[_vod_configs_pb2.VodConfig, _Mapping]]=..., update_mask: _Optional[_Union[_field_mask_pb2.FieldMask, _Mapping]]=...) -> None:
        ...

class OperationMetadata(_message.Message):
    __slots__ = ('create_time', 'end_time', 'target', 'verb')
    CREATE_TIME_FIELD_NUMBER: _ClassVar[int]
    END_TIME_FIELD_NUMBER: _ClassVar[int]
    TARGET_FIELD_NUMBER: _ClassVar[int]
    VERB_FIELD_NUMBER: _ClassVar[int]
    create_time: _timestamp_pb2.Timestamp
    end_time: _timestamp_pb2.Timestamp
    target: str
    verb: str

    def __init__(self, create_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]]=..., end_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]]=..., target: _Optional[str]=..., verb: _Optional[str]=...) -> None:
        ...