from google.api import resource_pb2 as _resource_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union
DESCRIPTOR: _descriptor.FileDescriptor

class OrganizationSettings(_message.Message):
    __slots__ = ('name', 'enable_asset_discovery', 'asset_discovery_config')

    class AssetDiscoveryConfig(_message.Message):
        __slots__ = ('project_ids', 'inclusion_mode')

        class InclusionMode(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
            __slots__ = ()
            INCLUSION_MODE_UNSPECIFIED: _ClassVar[OrganizationSettings.AssetDiscoveryConfig.InclusionMode]
            INCLUDE_ONLY: _ClassVar[OrganizationSettings.AssetDiscoveryConfig.InclusionMode]
            EXCLUDE: _ClassVar[OrganizationSettings.AssetDiscoveryConfig.InclusionMode]
        INCLUSION_MODE_UNSPECIFIED: OrganizationSettings.AssetDiscoveryConfig.InclusionMode
        INCLUDE_ONLY: OrganizationSettings.AssetDiscoveryConfig.InclusionMode
        EXCLUDE: OrganizationSettings.AssetDiscoveryConfig.InclusionMode
        PROJECT_IDS_FIELD_NUMBER: _ClassVar[int]
        INCLUSION_MODE_FIELD_NUMBER: _ClassVar[int]
        project_ids: _containers.RepeatedScalarFieldContainer[str]
        inclusion_mode: OrganizationSettings.AssetDiscoveryConfig.InclusionMode

        def __init__(self, project_ids: _Optional[_Iterable[str]]=..., inclusion_mode: _Optional[_Union[OrganizationSettings.AssetDiscoveryConfig.InclusionMode, str]]=...) -> None:
            ...
    NAME_FIELD_NUMBER: _ClassVar[int]
    ENABLE_ASSET_DISCOVERY_FIELD_NUMBER: _ClassVar[int]
    ASSET_DISCOVERY_CONFIG_FIELD_NUMBER: _ClassVar[int]
    name: str
    enable_asset_discovery: bool
    asset_discovery_config: OrganizationSettings.AssetDiscoveryConfig

    def __init__(self, name: _Optional[str]=..., enable_asset_discovery: bool=..., asset_discovery_config: _Optional[_Union[OrganizationSettings.AssetDiscoveryConfig, _Mapping]]=...) -> None:
        ...