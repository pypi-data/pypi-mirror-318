from google.api import resource_pb2 as _resource_pb2
from google.cloud.orgpolicy.v1 import orgpolicy_pb2 as _orgpolicy_pb2
from google.iam.v1 import policy_pb2 as _policy_pb2
from google.identity.accesscontextmanager.v1 import access_level_pb2 as _access_level_pb2
from google.identity.accesscontextmanager.v1 import access_policy_pb2 as _access_policy_pb2
from google.identity.accesscontextmanager.v1 import service_perimeter_pb2 as _service_perimeter_pb2
from google.protobuf import struct_pb2 as _struct_pb2
from google.protobuf import timestamp_pb2 as _timestamp_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union
DESCRIPTOR: _descriptor.FileDescriptor

class Asset(_message.Message):
    __slots__ = ('update_time', 'name', 'asset_type', 'resource', 'iam_policy', 'org_policy', 'access_policy', 'access_level', 'service_perimeter', 'related_assets', 'ancestors')
    UPDATE_TIME_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    ASSET_TYPE_FIELD_NUMBER: _ClassVar[int]
    RESOURCE_FIELD_NUMBER: _ClassVar[int]
    IAM_POLICY_FIELD_NUMBER: _ClassVar[int]
    ORG_POLICY_FIELD_NUMBER: _ClassVar[int]
    ACCESS_POLICY_FIELD_NUMBER: _ClassVar[int]
    ACCESS_LEVEL_FIELD_NUMBER: _ClassVar[int]
    SERVICE_PERIMETER_FIELD_NUMBER: _ClassVar[int]
    RELATED_ASSETS_FIELD_NUMBER: _ClassVar[int]
    ANCESTORS_FIELD_NUMBER: _ClassVar[int]
    update_time: _timestamp_pb2.Timestamp
    name: str
    asset_type: str
    resource: Resource
    iam_policy: _policy_pb2.Policy
    org_policy: _containers.RepeatedCompositeFieldContainer[_orgpolicy_pb2.Policy]
    access_policy: _access_policy_pb2.AccessPolicy
    access_level: _access_level_pb2.AccessLevel
    service_perimeter: _service_perimeter_pb2.ServicePerimeter
    related_assets: RelatedAssets
    ancestors: _containers.RepeatedScalarFieldContainer[str]

    def __init__(self, update_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]]=..., name: _Optional[str]=..., asset_type: _Optional[str]=..., resource: _Optional[_Union[Resource, _Mapping]]=..., iam_policy: _Optional[_Union[_policy_pb2.Policy, _Mapping]]=..., org_policy: _Optional[_Iterable[_Union[_orgpolicy_pb2.Policy, _Mapping]]]=..., access_policy: _Optional[_Union[_access_policy_pb2.AccessPolicy, _Mapping]]=..., access_level: _Optional[_Union[_access_level_pb2.AccessLevel, _Mapping]]=..., service_perimeter: _Optional[_Union[_service_perimeter_pb2.ServicePerimeter, _Mapping]]=..., related_assets: _Optional[_Union[RelatedAssets, _Mapping]]=..., ancestors: _Optional[_Iterable[str]]=...) -> None:
        ...

class Resource(_message.Message):
    __slots__ = ('version', 'discovery_document_uri', 'discovery_name', 'resource_url', 'parent', 'data', 'location')
    VERSION_FIELD_NUMBER: _ClassVar[int]
    DISCOVERY_DOCUMENT_URI_FIELD_NUMBER: _ClassVar[int]
    DISCOVERY_NAME_FIELD_NUMBER: _ClassVar[int]
    RESOURCE_URL_FIELD_NUMBER: _ClassVar[int]
    PARENT_FIELD_NUMBER: _ClassVar[int]
    DATA_FIELD_NUMBER: _ClassVar[int]
    LOCATION_FIELD_NUMBER: _ClassVar[int]
    version: str
    discovery_document_uri: str
    discovery_name: str
    resource_url: str
    parent: str
    data: _struct_pb2.Struct
    location: str

    def __init__(self, version: _Optional[str]=..., discovery_document_uri: _Optional[str]=..., discovery_name: _Optional[str]=..., resource_url: _Optional[str]=..., parent: _Optional[str]=..., data: _Optional[_Union[_struct_pb2.Struct, _Mapping]]=..., location: _Optional[str]=...) -> None:
        ...

class RelatedAssets(_message.Message):
    __slots__ = ('relationship_attributes', 'assets')
    RELATIONSHIP_ATTRIBUTES_FIELD_NUMBER: _ClassVar[int]
    ASSETS_FIELD_NUMBER: _ClassVar[int]
    relationship_attributes: RelationshipAttributes
    assets: _containers.RepeatedCompositeFieldContainer[RelatedAsset]

    def __init__(self, relationship_attributes: _Optional[_Union[RelationshipAttributes, _Mapping]]=..., assets: _Optional[_Iterable[_Union[RelatedAsset, _Mapping]]]=...) -> None:
        ...

class RelationshipAttributes(_message.Message):
    __slots__ = ('type', 'source_resource_type', 'target_resource_type', 'action')
    TYPE_FIELD_NUMBER: _ClassVar[int]
    SOURCE_RESOURCE_TYPE_FIELD_NUMBER: _ClassVar[int]
    TARGET_RESOURCE_TYPE_FIELD_NUMBER: _ClassVar[int]
    ACTION_FIELD_NUMBER: _ClassVar[int]
    type: str
    source_resource_type: str
    target_resource_type: str
    action: str

    def __init__(self, type: _Optional[str]=..., source_resource_type: _Optional[str]=..., target_resource_type: _Optional[str]=..., action: _Optional[str]=...) -> None:
        ...

class RelatedAsset(_message.Message):
    __slots__ = ('asset', 'asset_type', 'ancestors')
    ASSET_FIELD_NUMBER: _ClassVar[int]
    ASSET_TYPE_FIELD_NUMBER: _ClassVar[int]
    ANCESTORS_FIELD_NUMBER: _ClassVar[int]
    asset: str
    asset_type: str
    ancestors: _containers.RepeatedScalarFieldContainer[str]

    def __init__(self, asset: _Optional[str]=..., asset_type: _Optional[str]=..., ancestors: _Optional[_Iterable[str]]=...) -> None:
        ...