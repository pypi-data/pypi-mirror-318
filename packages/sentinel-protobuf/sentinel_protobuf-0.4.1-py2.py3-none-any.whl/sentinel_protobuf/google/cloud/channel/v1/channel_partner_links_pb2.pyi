from google.api import field_behavior_pb2 as _field_behavior_pb2
from google.api import resource_pb2 as _resource_pb2
from google.cloud.channel.v1 import common_pb2 as _common_pb2
from google.protobuf import timestamp_pb2 as _timestamp_pb2
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Mapping as _Mapping, Optional as _Optional, Union as _Union
DESCRIPTOR: _descriptor.FileDescriptor

class ChannelPartnerLinkView(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    UNSPECIFIED: _ClassVar[ChannelPartnerLinkView]
    BASIC: _ClassVar[ChannelPartnerLinkView]
    FULL: _ClassVar[ChannelPartnerLinkView]

class ChannelPartnerLinkState(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    CHANNEL_PARTNER_LINK_STATE_UNSPECIFIED: _ClassVar[ChannelPartnerLinkState]
    INVITED: _ClassVar[ChannelPartnerLinkState]
    ACTIVE: _ClassVar[ChannelPartnerLinkState]
    REVOKED: _ClassVar[ChannelPartnerLinkState]
    SUSPENDED: _ClassVar[ChannelPartnerLinkState]
UNSPECIFIED: ChannelPartnerLinkView
BASIC: ChannelPartnerLinkView
FULL: ChannelPartnerLinkView
CHANNEL_PARTNER_LINK_STATE_UNSPECIFIED: ChannelPartnerLinkState
INVITED: ChannelPartnerLinkState
ACTIVE: ChannelPartnerLinkState
REVOKED: ChannelPartnerLinkState
SUSPENDED: ChannelPartnerLinkState

class ChannelPartnerLink(_message.Message):
    __slots__ = ('name', 'reseller_cloud_identity_id', 'link_state', 'invite_link_uri', 'create_time', 'update_time', 'public_id', 'channel_partner_cloud_identity_info')
    NAME_FIELD_NUMBER: _ClassVar[int]
    RESELLER_CLOUD_IDENTITY_ID_FIELD_NUMBER: _ClassVar[int]
    LINK_STATE_FIELD_NUMBER: _ClassVar[int]
    INVITE_LINK_URI_FIELD_NUMBER: _ClassVar[int]
    CREATE_TIME_FIELD_NUMBER: _ClassVar[int]
    UPDATE_TIME_FIELD_NUMBER: _ClassVar[int]
    PUBLIC_ID_FIELD_NUMBER: _ClassVar[int]
    CHANNEL_PARTNER_CLOUD_IDENTITY_INFO_FIELD_NUMBER: _ClassVar[int]
    name: str
    reseller_cloud_identity_id: str
    link_state: ChannelPartnerLinkState
    invite_link_uri: str
    create_time: _timestamp_pb2.Timestamp
    update_time: _timestamp_pb2.Timestamp
    public_id: str
    channel_partner_cloud_identity_info: _common_pb2.CloudIdentityInfo

    def __init__(self, name: _Optional[str]=..., reseller_cloud_identity_id: _Optional[str]=..., link_state: _Optional[_Union[ChannelPartnerLinkState, str]]=..., invite_link_uri: _Optional[str]=..., create_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]]=..., update_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]]=..., public_id: _Optional[str]=..., channel_partner_cloud_identity_info: _Optional[_Union[_common_pb2.CloudIdentityInfo, _Mapping]]=...) -> None:
        ...