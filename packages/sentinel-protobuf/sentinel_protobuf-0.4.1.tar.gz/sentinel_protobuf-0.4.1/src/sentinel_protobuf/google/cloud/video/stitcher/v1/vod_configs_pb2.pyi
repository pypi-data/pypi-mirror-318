from google.api import field_behavior_pb2 as _field_behavior_pb2
from google.api import resource_pb2 as _resource_pb2
from google.cloud.video.stitcher.v1 import fetch_options_pb2 as _fetch_options_pb2
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Mapping as _Mapping, Optional as _Optional, Union as _Union
DESCRIPTOR: _descriptor.FileDescriptor

class VodConfig(_message.Message):
    __slots__ = ('name', 'source_uri', 'ad_tag_uri', 'gam_vod_config', 'state', 'source_fetch_options')

    class State(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        STATE_UNSPECIFIED: _ClassVar[VodConfig.State]
        CREATING: _ClassVar[VodConfig.State]
        READY: _ClassVar[VodConfig.State]
        DELETING: _ClassVar[VodConfig.State]
    STATE_UNSPECIFIED: VodConfig.State
    CREATING: VodConfig.State
    READY: VodConfig.State
    DELETING: VodConfig.State
    NAME_FIELD_NUMBER: _ClassVar[int]
    SOURCE_URI_FIELD_NUMBER: _ClassVar[int]
    AD_TAG_URI_FIELD_NUMBER: _ClassVar[int]
    GAM_VOD_CONFIG_FIELD_NUMBER: _ClassVar[int]
    STATE_FIELD_NUMBER: _ClassVar[int]
    SOURCE_FETCH_OPTIONS_FIELD_NUMBER: _ClassVar[int]
    name: str
    source_uri: str
    ad_tag_uri: str
    gam_vod_config: GamVodConfig
    state: VodConfig.State
    source_fetch_options: _fetch_options_pb2.FetchOptions

    def __init__(self, name: _Optional[str]=..., source_uri: _Optional[str]=..., ad_tag_uri: _Optional[str]=..., gam_vod_config: _Optional[_Union[GamVodConfig, _Mapping]]=..., state: _Optional[_Union[VodConfig.State, str]]=..., source_fetch_options: _Optional[_Union[_fetch_options_pb2.FetchOptions, _Mapping]]=...) -> None:
        ...

class GamVodConfig(_message.Message):
    __slots__ = ('network_code',)
    NETWORK_CODE_FIELD_NUMBER: _ClassVar[int]
    network_code: str

    def __init__(self, network_code: _Optional[str]=...) -> None:
        ...