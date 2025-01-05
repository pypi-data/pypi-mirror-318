from google.api import field_behavior_pb2 as _field_behavior_pb2
from google.cloud.securitycenter.v1 import folder_pb2 as _folder_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union
DESCRIPTOR: _descriptor.FileDescriptor

class CloudProvider(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    CLOUD_PROVIDER_UNSPECIFIED: _ClassVar[CloudProvider]
    GOOGLE_CLOUD_PLATFORM: _ClassVar[CloudProvider]
    AMAZON_WEB_SERVICES: _ClassVar[CloudProvider]
    MICROSOFT_AZURE: _ClassVar[CloudProvider]
CLOUD_PROVIDER_UNSPECIFIED: CloudProvider
GOOGLE_CLOUD_PLATFORM: CloudProvider
AMAZON_WEB_SERVICES: CloudProvider
MICROSOFT_AZURE: CloudProvider

class Resource(_message.Message):
    __slots__ = ('name', 'display_name', 'type', 'project', 'project_display_name', 'parent', 'parent_display_name', 'folders', 'cloud_provider', 'organization', 'service', 'location', 'aws_metadata', 'azure_metadata', 'resource_path', 'resource_path_string')
    NAME_FIELD_NUMBER: _ClassVar[int]
    DISPLAY_NAME_FIELD_NUMBER: _ClassVar[int]
    TYPE_FIELD_NUMBER: _ClassVar[int]
    PROJECT_FIELD_NUMBER: _ClassVar[int]
    PROJECT_DISPLAY_NAME_FIELD_NUMBER: _ClassVar[int]
    PARENT_FIELD_NUMBER: _ClassVar[int]
    PARENT_DISPLAY_NAME_FIELD_NUMBER: _ClassVar[int]
    FOLDERS_FIELD_NUMBER: _ClassVar[int]
    CLOUD_PROVIDER_FIELD_NUMBER: _ClassVar[int]
    ORGANIZATION_FIELD_NUMBER: _ClassVar[int]
    SERVICE_FIELD_NUMBER: _ClassVar[int]
    LOCATION_FIELD_NUMBER: _ClassVar[int]
    AWS_METADATA_FIELD_NUMBER: _ClassVar[int]
    AZURE_METADATA_FIELD_NUMBER: _ClassVar[int]
    RESOURCE_PATH_FIELD_NUMBER: _ClassVar[int]
    RESOURCE_PATH_STRING_FIELD_NUMBER: _ClassVar[int]
    name: str
    display_name: str
    type: str
    project: str
    project_display_name: str
    parent: str
    parent_display_name: str
    folders: _containers.RepeatedCompositeFieldContainer[_folder_pb2.Folder]
    cloud_provider: CloudProvider
    organization: str
    service: str
    location: str
    aws_metadata: AwsMetadata
    azure_metadata: AzureMetadata
    resource_path: ResourcePath
    resource_path_string: str

    def __init__(self, name: _Optional[str]=..., display_name: _Optional[str]=..., type: _Optional[str]=..., project: _Optional[str]=..., project_display_name: _Optional[str]=..., parent: _Optional[str]=..., parent_display_name: _Optional[str]=..., folders: _Optional[_Iterable[_Union[_folder_pb2.Folder, _Mapping]]]=..., cloud_provider: _Optional[_Union[CloudProvider, str]]=..., organization: _Optional[str]=..., service: _Optional[str]=..., location: _Optional[str]=..., aws_metadata: _Optional[_Union[AwsMetadata, _Mapping]]=..., azure_metadata: _Optional[_Union[AzureMetadata, _Mapping]]=..., resource_path: _Optional[_Union[ResourcePath, _Mapping]]=..., resource_path_string: _Optional[str]=...) -> None:
        ...

class AwsMetadata(_message.Message):
    __slots__ = ('organization', 'organizational_units', 'account')

    class AwsOrganization(_message.Message):
        __slots__ = ('id',)
        ID_FIELD_NUMBER: _ClassVar[int]
        id: str

        def __init__(self, id: _Optional[str]=...) -> None:
            ...

    class AwsOrganizationalUnit(_message.Message):
        __slots__ = ('id', 'name')
        ID_FIELD_NUMBER: _ClassVar[int]
        NAME_FIELD_NUMBER: _ClassVar[int]
        id: str
        name: str

        def __init__(self, id: _Optional[str]=..., name: _Optional[str]=...) -> None:
            ...

    class AwsAccount(_message.Message):
        __slots__ = ('id', 'name')
        ID_FIELD_NUMBER: _ClassVar[int]
        NAME_FIELD_NUMBER: _ClassVar[int]
        id: str
        name: str

        def __init__(self, id: _Optional[str]=..., name: _Optional[str]=...) -> None:
            ...
    ORGANIZATION_FIELD_NUMBER: _ClassVar[int]
    ORGANIZATIONAL_UNITS_FIELD_NUMBER: _ClassVar[int]
    ACCOUNT_FIELD_NUMBER: _ClassVar[int]
    organization: AwsMetadata.AwsOrganization
    organizational_units: _containers.RepeatedCompositeFieldContainer[AwsMetadata.AwsOrganizationalUnit]
    account: AwsMetadata.AwsAccount

    def __init__(self, organization: _Optional[_Union[AwsMetadata.AwsOrganization, _Mapping]]=..., organizational_units: _Optional[_Iterable[_Union[AwsMetadata.AwsOrganizationalUnit, _Mapping]]]=..., account: _Optional[_Union[AwsMetadata.AwsAccount, _Mapping]]=...) -> None:
        ...

class AzureMetadata(_message.Message):
    __slots__ = ('management_groups', 'subscription', 'resource_group')

    class AzureManagementGroup(_message.Message):
        __slots__ = ('id', 'display_name')
        ID_FIELD_NUMBER: _ClassVar[int]
        DISPLAY_NAME_FIELD_NUMBER: _ClassVar[int]
        id: str
        display_name: str

        def __init__(self, id: _Optional[str]=..., display_name: _Optional[str]=...) -> None:
            ...

    class AzureSubscription(_message.Message):
        __slots__ = ('id', 'display_name')
        ID_FIELD_NUMBER: _ClassVar[int]
        DISPLAY_NAME_FIELD_NUMBER: _ClassVar[int]
        id: str
        display_name: str

        def __init__(self, id: _Optional[str]=..., display_name: _Optional[str]=...) -> None:
            ...

    class AzureResourceGroup(_message.Message):
        __slots__ = ('name',)
        NAME_FIELD_NUMBER: _ClassVar[int]
        name: str

        def __init__(self, name: _Optional[str]=...) -> None:
            ...
    MANAGEMENT_GROUPS_FIELD_NUMBER: _ClassVar[int]
    SUBSCRIPTION_FIELD_NUMBER: _ClassVar[int]
    RESOURCE_GROUP_FIELD_NUMBER: _ClassVar[int]
    management_groups: _containers.RepeatedCompositeFieldContainer[AzureMetadata.AzureManagementGroup]
    subscription: AzureMetadata.AzureSubscription
    resource_group: AzureMetadata.AzureResourceGroup

    def __init__(self, management_groups: _Optional[_Iterable[_Union[AzureMetadata.AzureManagementGroup, _Mapping]]]=..., subscription: _Optional[_Union[AzureMetadata.AzureSubscription, _Mapping]]=..., resource_group: _Optional[_Union[AzureMetadata.AzureResourceGroup, _Mapping]]=...) -> None:
        ...

class ResourcePath(_message.Message):
    __slots__ = ('nodes',)

    class ResourcePathNodeType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        RESOURCE_PATH_NODE_TYPE_UNSPECIFIED: _ClassVar[ResourcePath.ResourcePathNodeType]
        GCP_ORGANIZATION: _ClassVar[ResourcePath.ResourcePathNodeType]
        GCP_FOLDER: _ClassVar[ResourcePath.ResourcePathNodeType]
        GCP_PROJECT: _ClassVar[ResourcePath.ResourcePathNodeType]
        AWS_ORGANIZATION: _ClassVar[ResourcePath.ResourcePathNodeType]
        AWS_ORGANIZATIONAL_UNIT: _ClassVar[ResourcePath.ResourcePathNodeType]
        AWS_ACCOUNT: _ClassVar[ResourcePath.ResourcePathNodeType]
        AZURE_MANAGEMENT_GROUP: _ClassVar[ResourcePath.ResourcePathNodeType]
        AZURE_SUBSCRIPTION: _ClassVar[ResourcePath.ResourcePathNodeType]
        AZURE_RESOURCE_GROUP: _ClassVar[ResourcePath.ResourcePathNodeType]
    RESOURCE_PATH_NODE_TYPE_UNSPECIFIED: ResourcePath.ResourcePathNodeType
    GCP_ORGANIZATION: ResourcePath.ResourcePathNodeType
    GCP_FOLDER: ResourcePath.ResourcePathNodeType
    GCP_PROJECT: ResourcePath.ResourcePathNodeType
    AWS_ORGANIZATION: ResourcePath.ResourcePathNodeType
    AWS_ORGANIZATIONAL_UNIT: ResourcePath.ResourcePathNodeType
    AWS_ACCOUNT: ResourcePath.ResourcePathNodeType
    AZURE_MANAGEMENT_GROUP: ResourcePath.ResourcePathNodeType
    AZURE_SUBSCRIPTION: ResourcePath.ResourcePathNodeType
    AZURE_RESOURCE_GROUP: ResourcePath.ResourcePathNodeType

    class ResourcePathNode(_message.Message):
        __slots__ = ('node_type', 'id', 'display_name')
        NODE_TYPE_FIELD_NUMBER: _ClassVar[int]
        ID_FIELD_NUMBER: _ClassVar[int]
        DISPLAY_NAME_FIELD_NUMBER: _ClassVar[int]
        node_type: ResourcePath.ResourcePathNodeType
        id: str
        display_name: str

        def __init__(self, node_type: _Optional[_Union[ResourcePath.ResourcePathNodeType, str]]=..., id: _Optional[str]=..., display_name: _Optional[str]=...) -> None:
            ...
    NODES_FIELD_NUMBER: _ClassVar[int]
    nodes: _containers.RepeatedCompositeFieldContainer[ResourcePath.ResourcePathNode]

    def __init__(self, nodes: _Optional[_Iterable[_Union[ResourcePath.ResourcePathNode, _Mapping]]]=...) -> None:
        ...