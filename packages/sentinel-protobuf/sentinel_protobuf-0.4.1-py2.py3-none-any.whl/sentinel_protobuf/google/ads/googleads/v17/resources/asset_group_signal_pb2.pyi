from google.ads.googleads.v17.common import criteria_pb2 as _criteria_pb2
from google.ads.googleads.v17.enums import asset_group_signal_approval_status_pb2 as _asset_group_signal_approval_status_pb2
from google.api import field_behavior_pb2 as _field_behavior_pb2
from google.api import resource_pb2 as _resource_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class AssetGroupSignal(_message.Message):
    __slots__ = ("resource_name", "asset_group", "approval_status", "disapproval_reasons", "audience", "search_theme")
    RESOURCE_NAME_FIELD_NUMBER: _ClassVar[int]
    ASSET_GROUP_FIELD_NUMBER: _ClassVar[int]
    APPROVAL_STATUS_FIELD_NUMBER: _ClassVar[int]
    DISAPPROVAL_REASONS_FIELD_NUMBER: _ClassVar[int]
    AUDIENCE_FIELD_NUMBER: _ClassVar[int]
    SEARCH_THEME_FIELD_NUMBER: _ClassVar[int]
    resource_name: str
    asset_group: str
    approval_status: _asset_group_signal_approval_status_pb2.AssetGroupSignalApprovalStatusEnum.AssetGroupSignalApprovalStatus
    disapproval_reasons: _containers.RepeatedScalarFieldContainer[str]
    audience: _criteria_pb2.AudienceInfo
    search_theme: _criteria_pb2.SearchThemeInfo
    def __init__(self, resource_name: _Optional[str] = ..., asset_group: _Optional[str] = ..., approval_status: _Optional[_Union[_asset_group_signal_approval_status_pb2.AssetGroupSignalApprovalStatusEnum.AssetGroupSignalApprovalStatus, str]] = ..., disapproval_reasons: _Optional[_Iterable[str]] = ..., audience: _Optional[_Union[_criteria_pb2.AudienceInfo, _Mapping]] = ..., search_theme: _Optional[_Union[_criteria_pb2.SearchThemeInfo, _Mapping]] = ...) -> None: ...
