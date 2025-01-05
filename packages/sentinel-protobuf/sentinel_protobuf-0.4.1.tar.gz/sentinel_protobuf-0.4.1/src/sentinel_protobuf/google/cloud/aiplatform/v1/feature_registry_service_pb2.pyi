from google.api import annotations_pb2 as _annotations_pb2
from google.api import client_pb2 as _client_pb2
from google.api import field_behavior_pb2 as _field_behavior_pb2
from google.api import resource_pb2 as _resource_pb2
from google.cloud.aiplatform.v1 import feature_pb2 as _feature_pb2
from google.cloud.aiplatform.v1 import feature_group_pb2 as _feature_group_pb2
from google.cloud.aiplatform.v1 import featurestore_service_pb2 as _featurestore_service_pb2
from google.cloud.aiplatform.v1 import operation_pb2 as _operation_pb2
from google.longrunning import operations_pb2 as _operations_pb2
from google.protobuf import empty_pb2 as _empty_pb2
from google.protobuf import field_mask_pb2 as _field_mask_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union
DESCRIPTOR: _descriptor.FileDescriptor

class CreateFeatureGroupRequest(_message.Message):
    __slots__ = ('parent', 'feature_group', 'feature_group_id')
    PARENT_FIELD_NUMBER: _ClassVar[int]
    FEATURE_GROUP_FIELD_NUMBER: _ClassVar[int]
    FEATURE_GROUP_ID_FIELD_NUMBER: _ClassVar[int]
    parent: str
    feature_group: _feature_group_pb2.FeatureGroup
    feature_group_id: str

    def __init__(self, parent: _Optional[str]=..., feature_group: _Optional[_Union[_feature_group_pb2.FeatureGroup, _Mapping]]=..., feature_group_id: _Optional[str]=...) -> None:
        ...

class GetFeatureGroupRequest(_message.Message):
    __slots__ = ('name',)
    NAME_FIELD_NUMBER: _ClassVar[int]
    name: str

    def __init__(self, name: _Optional[str]=...) -> None:
        ...

class ListFeatureGroupsRequest(_message.Message):
    __slots__ = ('parent', 'filter', 'page_size', 'page_token', 'order_by')
    PARENT_FIELD_NUMBER: _ClassVar[int]
    FILTER_FIELD_NUMBER: _ClassVar[int]
    PAGE_SIZE_FIELD_NUMBER: _ClassVar[int]
    PAGE_TOKEN_FIELD_NUMBER: _ClassVar[int]
    ORDER_BY_FIELD_NUMBER: _ClassVar[int]
    parent: str
    filter: str
    page_size: int
    page_token: str
    order_by: str

    def __init__(self, parent: _Optional[str]=..., filter: _Optional[str]=..., page_size: _Optional[int]=..., page_token: _Optional[str]=..., order_by: _Optional[str]=...) -> None:
        ...

class ListFeatureGroupsResponse(_message.Message):
    __slots__ = ('feature_groups', 'next_page_token')
    FEATURE_GROUPS_FIELD_NUMBER: _ClassVar[int]
    NEXT_PAGE_TOKEN_FIELD_NUMBER: _ClassVar[int]
    feature_groups: _containers.RepeatedCompositeFieldContainer[_feature_group_pb2.FeatureGroup]
    next_page_token: str

    def __init__(self, feature_groups: _Optional[_Iterable[_Union[_feature_group_pb2.FeatureGroup, _Mapping]]]=..., next_page_token: _Optional[str]=...) -> None:
        ...

class UpdateFeatureGroupRequest(_message.Message):
    __slots__ = ('feature_group', 'update_mask')
    FEATURE_GROUP_FIELD_NUMBER: _ClassVar[int]
    UPDATE_MASK_FIELD_NUMBER: _ClassVar[int]
    feature_group: _feature_group_pb2.FeatureGroup
    update_mask: _field_mask_pb2.FieldMask

    def __init__(self, feature_group: _Optional[_Union[_feature_group_pb2.FeatureGroup, _Mapping]]=..., update_mask: _Optional[_Union[_field_mask_pb2.FieldMask, _Mapping]]=...) -> None:
        ...

class DeleteFeatureGroupRequest(_message.Message):
    __slots__ = ('name', 'force')
    NAME_FIELD_NUMBER: _ClassVar[int]
    FORCE_FIELD_NUMBER: _ClassVar[int]
    name: str
    force: bool

    def __init__(self, name: _Optional[str]=..., force: bool=...) -> None:
        ...

class CreateFeatureGroupOperationMetadata(_message.Message):
    __slots__ = ('generic_metadata',)
    GENERIC_METADATA_FIELD_NUMBER: _ClassVar[int]
    generic_metadata: _operation_pb2.GenericOperationMetadata

    def __init__(self, generic_metadata: _Optional[_Union[_operation_pb2.GenericOperationMetadata, _Mapping]]=...) -> None:
        ...

class UpdateFeatureGroupOperationMetadata(_message.Message):
    __slots__ = ('generic_metadata',)
    GENERIC_METADATA_FIELD_NUMBER: _ClassVar[int]
    generic_metadata: _operation_pb2.GenericOperationMetadata

    def __init__(self, generic_metadata: _Optional[_Union[_operation_pb2.GenericOperationMetadata, _Mapping]]=...) -> None:
        ...

class CreateRegistryFeatureOperationMetadata(_message.Message):
    __slots__ = ('generic_metadata',)
    GENERIC_METADATA_FIELD_NUMBER: _ClassVar[int]
    generic_metadata: _operation_pb2.GenericOperationMetadata

    def __init__(self, generic_metadata: _Optional[_Union[_operation_pb2.GenericOperationMetadata, _Mapping]]=...) -> None:
        ...

class UpdateFeatureOperationMetadata(_message.Message):
    __slots__ = ('generic_metadata',)
    GENERIC_METADATA_FIELD_NUMBER: _ClassVar[int]
    generic_metadata: _operation_pb2.GenericOperationMetadata

    def __init__(self, generic_metadata: _Optional[_Union[_operation_pb2.GenericOperationMetadata, _Mapping]]=...) -> None:
        ...