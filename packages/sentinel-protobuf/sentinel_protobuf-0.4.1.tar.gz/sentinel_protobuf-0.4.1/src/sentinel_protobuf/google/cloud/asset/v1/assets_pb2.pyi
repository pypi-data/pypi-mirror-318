from google.api import resource_pb2 as _resource_pb2
from google.cloud.orgpolicy.v1 import orgpolicy_pb2 as _orgpolicy_pb2
from google.cloud.osconfig.v1 import inventory_pb2 as _inventory_pb2
from google.iam.v1 import policy_pb2 as _policy_pb2
from google.identity.accesscontextmanager.v1 import access_level_pb2 as _access_level_pb2
from google.identity.accesscontextmanager.v1 import access_policy_pb2 as _access_policy_pb2
from google.identity.accesscontextmanager.v1 import service_perimeter_pb2 as _service_perimeter_pb2
from google.protobuf import struct_pb2 as _struct_pb2
from google.protobuf import timestamp_pb2 as _timestamp_pb2
from google.rpc import code_pb2 as _code_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class TemporalAsset(_message.Message):
    __slots__ = ("window", "deleted", "asset", "prior_asset_state", "prior_asset")
    class PriorAssetState(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        PRIOR_ASSET_STATE_UNSPECIFIED: _ClassVar[TemporalAsset.PriorAssetState]
        PRESENT: _ClassVar[TemporalAsset.PriorAssetState]
        INVALID: _ClassVar[TemporalAsset.PriorAssetState]
        DOES_NOT_EXIST: _ClassVar[TemporalAsset.PriorAssetState]
        DELETED: _ClassVar[TemporalAsset.PriorAssetState]
    PRIOR_ASSET_STATE_UNSPECIFIED: TemporalAsset.PriorAssetState
    PRESENT: TemporalAsset.PriorAssetState
    INVALID: TemporalAsset.PriorAssetState
    DOES_NOT_EXIST: TemporalAsset.PriorAssetState
    DELETED: TemporalAsset.PriorAssetState
    WINDOW_FIELD_NUMBER: _ClassVar[int]
    DELETED_FIELD_NUMBER: _ClassVar[int]
    ASSET_FIELD_NUMBER: _ClassVar[int]
    PRIOR_ASSET_STATE_FIELD_NUMBER: _ClassVar[int]
    PRIOR_ASSET_FIELD_NUMBER: _ClassVar[int]
    window: TimeWindow
    deleted: bool
    asset: Asset
    prior_asset_state: TemporalAsset.PriorAssetState
    prior_asset: Asset
    def __init__(self, window: _Optional[_Union[TimeWindow, _Mapping]] = ..., deleted: bool = ..., asset: _Optional[_Union[Asset, _Mapping]] = ..., prior_asset_state: _Optional[_Union[TemporalAsset.PriorAssetState, str]] = ..., prior_asset: _Optional[_Union[Asset, _Mapping]] = ...) -> None: ...

class TimeWindow(_message.Message):
    __slots__ = ("start_time", "end_time")
    START_TIME_FIELD_NUMBER: _ClassVar[int]
    END_TIME_FIELD_NUMBER: _ClassVar[int]
    start_time: _timestamp_pb2.Timestamp
    end_time: _timestamp_pb2.Timestamp
    def __init__(self, start_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., end_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ...) -> None: ...

class Asset(_message.Message):
    __slots__ = ("update_time", "name", "asset_type", "resource", "iam_policy", "org_policy", "access_policy", "access_level", "service_perimeter", "os_inventory", "related_assets", "related_asset", "ancestors")
    UPDATE_TIME_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    ASSET_TYPE_FIELD_NUMBER: _ClassVar[int]
    RESOURCE_FIELD_NUMBER: _ClassVar[int]
    IAM_POLICY_FIELD_NUMBER: _ClassVar[int]
    ORG_POLICY_FIELD_NUMBER: _ClassVar[int]
    ACCESS_POLICY_FIELD_NUMBER: _ClassVar[int]
    ACCESS_LEVEL_FIELD_NUMBER: _ClassVar[int]
    SERVICE_PERIMETER_FIELD_NUMBER: _ClassVar[int]
    OS_INVENTORY_FIELD_NUMBER: _ClassVar[int]
    RELATED_ASSETS_FIELD_NUMBER: _ClassVar[int]
    RELATED_ASSET_FIELD_NUMBER: _ClassVar[int]
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
    os_inventory: _inventory_pb2.Inventory
    related_assets: RelatedAssets
    related_asset: RelatedAsset
    ancestors: _containers.RepeatedScalarFieldContainer[str]
    def __init__(self, update_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., name: _Optional[str] = ..., asset_type: _Optional[str] = ..., resource: _Optional[_Union[Resource, _Mapping]] = ..., iam_policy: _Optional[_Union[_policy_pb2.Policy, _Mapping]] = ..., org_policy: _Optional[_Iterable[_Union[_orgpolicy_pb2.Policy, _Mapping]]] = ..., access_policy: _Optional[_Union[_access_policy_pb2.AccessPolicy, _Mapping]] = ..., access_level: _Optional[_Union[_access_level_pb2.AccessLevel, _Mapping]] = ..., service_perimeter: _Optional[_Union[_service_perimeter_pb2.ServicePerimeter, _Mapping]] = ..., os_inventory: _Optional[_Union[_inventory_pb2.Inventory, _Mapping]] = ..., related_assets: _Optional[_Union[RelatedAssets, _Mapping]] = ..., related_asset: _Optional[_Union[RelatedAsset, _Mapping]] = ..., ancestors: _Optional[_Iterable[str]] = ...) -> None: ...

class Resource(_message.Message):
    __slots__ = ("version", "discovery_document_uri", "discovery_name", "resource_url", "parent", "data", "location")
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
    def __init__(self, version: _Optional[str] = ..., discovery_document_uri: _Optional[str] = ..., discovery_name: _Optional[str] = ..., resource_url: _Optional[str] = ..., parent: _Optional[str] = ..., data: _Optional[_Union[_struct_pb2.Struct, _Mapping]] = ..., location: _Optional[str] = ...) -> None: ...

class RelatedAssets(_message.Message):
    __slots__ = ("relationship_attributes", "assets")
    RELATIONSHIP_ATTRIBUTES_FIELD_NUMBER: _ClassVar[int]
    ASSETS_FIELD_NUMBER: _ClassVar[int]
    relationship_attributes: RelationshipAttributes
    assets: _containers.RepeatedCompositeFieldContainer[RelatedAsset]
    def __init__(self, relationship_attributes: _Optional[_Union[RelationshipAttributes, _Mapping]] = ..., assets: _Optional[_Iterable[_Union[RelatedAsset, _Mapping]]] = ...) -> None: ...

class RelationshipAttributes(_message.Message):
    __slots__ = ("type", "source_resource_type", "target_resource_type", "action")
    TYPE_FIELD_NUMBER: _ClassVar[int]
    SOURCE_RESOURCE_TYPE_FIELD_NUMBER: _ClassVar[int]
    TARGET_RESOURCE_TYPE_FIELD_NUMBER: _ClassVar[int]
    ACTION_FIELD_NUMBER: _ClassVar[int]
    type: str
    source_resource_type: str
    target_resource_type: str
    action: str
    def __init__(self, type: _Optional[str] = ..., source_resource_type: _Optional[str] = ..., target_resource_type: _Optional[str] = ..., action: _Optional[str] = ...) -> None: ...

class RelatedAsset(_message.Message):
    __slots__ = ("asset", "asset_type", "ancestors", "relationship_type")
    ASSET_FIELD_NUMBER: _ClassVar[int]
    ASSET_TYPE_FIELD_NUMBER: _ClassVar[int]
    ANCESTORS_FIELD_NUMBER: _ClassVar[int]
    RELATIONSHIP_TYPE_FIELD_NUMBER: _ClassVar[int]
    asset: str
    asset_type: str
    ancestors: _containers.RepeatedScalarFieldContainer[str]
    relationship_type: str
    def __init__(self, asset: _Optional[str] = ..., asset_type: _Optional[str] = ..., ancestors: _Optional[_Iterable[str]] = ..., relationship_type: _Optional[str] = ...) -> None: ...

class Tag(_message.Message):
    __slots__ = ("tag_key", "tag_key_id", "tag_value", "tag_value_id")
    TAG_KEY_FIELD_NUMBER: _ClassVar[int]
    TAG_KEY_ID_FIELD_NUMBER: _ClassVar[int]
    TAG_VALUE_FIELD_NUMBER: _ClassVar[int]
    TAG_VALUE_ID_FIELD_NUMBER: _ClassVar[int]
    tag_key: str
    tag_key_id: str
    tag_value: str
    tag_value_id: str
    def __init__(self, tag_key: _Optional[str] = ..., tag_key_id: _Optional[str] = ..., tag_value: _Optional[str] = ..., tag_value_id: _Optional[str] = ...) -> None: ...

class EffectiveTagDetails(_message.Message):
    __slots__ = ("attached_resource", "effective_tags")
    ATTACHED_RESOURCE_FIELD_NUMBER: _ClassVar[int]
    EFFECTIVE_TAGS_FIELD_NUMBER: _ClassVar[int]
    attached_resource: str
    effective_tags: _containers.RepeatedCompositeFieldContainer[Tag]
    def __init__(self, attached_resource: _Optional[str] = ..., effective_tags: _Optional[_Iterable[_Union[Tag, _Mapping]]] = ...) -> None: ...

class ResourceSearchResult(_message.Message):
    __slots__ = ("name", "asset_type", "project", "folders", "organization", "display_name", "description", "location", "labels", "network_tags", "kms_key", "kms_keys", "create_time", "update_time", "state", "additional_attributes", "parent_full_resource_name", "versioned_resources", "attached_resources", "relationships", "tag_keys", "tag_values", "tag_value_ids", "tags", "effective_tags", "parent_asset_type", "scc_security_marks")
    class LabelsEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: str
        def __init__(self, key: _Optional[str] = ..., value: _Optional[str] = ...) -> None: ...
    class RelationshipsEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: RelatedResources
        def __init__(self, key: _Optional[str] = ..., value: _Optional[_Union[RelatedResources, _Mapping]] = ...) -> None: ...
    class SccSecurityMarksEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: str
        def __init__(self, key: _Optional[str] = ..., value: _Optional[str] = ...) -> None: ...
    NAME_FIELD_NUMBER: _ClassVar[int]
    ASSET_TYPE_FIELD_NUMBER: _ClassVar[int]
    PROJECT_FIELD_NUMBER: _ClassVar[int]
    FOLDERS_FIELD_NUMBER: _ClassVar[int]
    ORGANIZATION_FIELD_NUMBER: _ClassVar[int]
    DISPLAY_NAME_FIELD_NUMBER: _ClassVar[int]
    DESCRIPTION_FIELD_NUMBER: _ClassVar[int]
    LOCATION_FIELD_NUMBER: _ClassVar[int]
    LABELS_FIELD_NUMBER: _ClassVar[int]
    NETWORK_TAGS_FIELD_NUMBER: _ClassVar[int]
    KMS_KEY_FIELD_NUMBER: _ClassVar[int]
    KMS_KEYS_FIELD_NUMBER: _ClassVar[int]
    CREATE_TIME_FIELD_NUMBER: _ClassVar[int]
    UPDATE_TIME_FIELD_NUMBER: _ClassVar[int]
    STATE_FIELD_NUMBER: _ClassVar[int]
    ADDITIONAL_ATTRIBUTES_FIELD_NUMBER: _ClassVar[int]
    PARENT_FULL_RESOURCE_NAME_FIELD_NUMBER: _ClassVar[int]
    VERSIONED_RESOURCES_FIELD_NUMBER: _ClassVar[int]
    ATTACHED_RESOURCES_FIELD_NUMBER: _ClassVar[int]
    RELATIONSHIPS_FIELD_NUMBER: _ClassVar[int]
    TAG_KEYS_FIELD_NUMBER: _ClassVar[int]
    TAG_VALUES_FIELD_NUMBER: _ClassVar[int]
    TAG_VALUE_IDS_FIELD_NUMBER: _ClassVar[int]
    TAGS_FIELD_NUMBER: _ClassVar[int]
    EFFECTIVE_TAGS_FIELD_NUMBER: _ClassVar[int]
    PARENT_ASSET_TYPE_FIELD_NUMBER: _ClassVar[int]
    SCC_SECURITY_MARKS_FIELD_NUMBER: _ClassVar[int]
    name: str
    asset_type: str
    project: str
    folders: _containers.RepeatedScalarFieldContainer[str]
    organization: str
    display_name: str
    description: str
    location: str
    labels: _containers.ScalarMap[str, str]
    network_tags: _containers.RepeatedScalarFieldContainer[str]
    kms_key: str
    kms_keys: _containers.RepeatedScalarFieldContainer[str]
    create_time: _timestamp_pb2.Timestamp
    update_time: _timestamp_pb2.Timestamp
    state: str
    additional_attributes: _struct_pb2.Struct
    parent_full_resource_name: str
    versioned_resources: _containers.RepeatedCompositeFieldContainer[VersionedResource]
    attached_resources: _containers.RepeatedCompositeFieldContainer[AttachedResource]
    relationships: _containers.MessageMap[str, RelatedResources]
    tag_keys: _containers.RepeatedScalarFieldContainer[str]
    tag_values: _containers.RepeatedScalarFieldContainer[str]
    tag_value_ids: _containers.RepeatedScalarFieldContainer[str]
    tags: _containers.RepeatedCompositeFieldContainer[Tag]
    effective_tags: _containers.RepeatedCompositeFieldContainer[EffectiveTagDetails]
    parent_asset_type: str
    scc_security_marks: _containers.ScalarMap[str, str]
    def __init__(self, name: _Optional[str] = ..., asset_type: _Optional[str] = ..., project: _Optional[str] = ..., folders: _Optional[_Iterable[str]] = ..., organization: _Optional[str] = ..., display_name: _Optional[str] = ..., description: _Optional[str] = ..., location: _Optional[str] = ..., labels: _Optional[_Mapping[str, str]] = ..., network_tags: _Optional[_Iterable[str]] = ..., kms_key: _Optional[str] = ..., kms_keys: _Optional[_Iterable[str]] = ..., create_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., update_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., state: _Optional[str] = ..., additional_attributes: _Optional[_Union[_struct_pb2.Struct, _Mapping]] = ..., parent_full_resource_name: _Optional[str] = ..., versioned_resources: _Optional[_Iterable[_Union[VersionedResource, _Mapping]]] = ..., attached_resources: _Optional[_Iterable[_Union[AttachedResource, _Mapping]]] = ..., relationships: _Optional[_Mapping[str, RelatedResources]] = ..., tag_keys: _Optional[_Iterable[str]] = ..., tag_values: _Optional[_Iterable[str]] = ..., tag_value_ids: _Optional[_Iterable[str]] = ..., tags: _Optional[_Iterable[_Union[Tag, _Mapping]]] = ..., effective_tags: _Optional[_Iterable[_Union[EffectiveTagDetails, _Mapping]]] = ..., parent_asset_type: _Optional[str] = ..., scc_security_marks: _Optional[_Mapping[str, str]] = ...) -> None: ...

class VersionedResource(_message.Message):
    __slots__ = ("version", "resource")
    VERSION_FIELD_NUMBER: _ClassVar[int]
    RESOURCE_FIELD_NUMBER: _ClassVar[int]
    version: str
    resource: _struct_pb2.Struct
    def __init__(self, version: _Optional[str] = ..., resource: _Optional[_Union[_struct_pb2.Struct, _Mapping]] = ...) -> None: ...

class AttachedResource(_message.Message):
    __slots__ = ("asset_type", "versioned_resources")
    ASSET_TYPE_FIELD_NUMBER: _ClassVar[int]
    VERSIONED_RESOURCES_FIELD_NUMBER: _ClassVar[int]
    asset_type: str
    versioned_resources: _containers.RepeatedCompositeFieldContainer[VersionedResource]
    def __init__(self, asset_type: _Optional[str] = ..., versioned_resources: _Optional[_Iterable[_Union[VersionedResource, _Mapping]]] = ...) -> None: ...

class RelatedResources(_message.Message):
    __slots__ = ("related_resources",)
    RELATED_RESOURCES_FIELD_NUMBER: _ClassVar[int]
    related_resources: _containers.RepeatedCompositeFieldContainer[RelatedResource]
    def __init__(self, related_resources: _Optional[_Iterable[_Union[RelatedResource, _Mapping]]] = ...) -> None: ...

class RelatedResource(_message.Message):
    __slots__ = ("asset_type", "full_resource_name")
    ASSET_TYPE_FIELD_NUMBER: _ClassVar[int]
    FULL_RESOURCE_NAME_FIELD_NUMBER: _ClassVar[int]
    asset_type: str
    full_resource_name: str
    def __init__(self, asset_type: _Optional[str] = ..., full_resource_name: _Optional[str] = ...) -> None: ...

class IamPolicySearchResult(_message.Message):
    __slots__ = ("resource", "asset_type", "project", "folders", "organization", "policy", "explanation")
    class Explanation(_message.Message):
        __slots__ = ("matched_permissions",)
        class Permissions(_message.Message):
            __slots__ = ("permissions",)
            PERMISSIONS_FIELD_NUMBER: _ClassVar[int]
            permissions: _containers.RepeatedScalarFieldContainer[str]
            def __init__(self, permissions: _Optional[_Iterable[str]] = ...) -> None: ...
        class MatchedPermissionsEntry(_message.Message):
            __slots__ = ("key", "value")
            KEY_FIELD_NUMBER: _ClassVar[int]
            VALUE_FIELD_NUMBER: _ClassVar[int]
            key: str
            value: IamPolicySearchResult.Explanation.Permissions
            def __init__(self, key: _Optional[str] = ..., value: _Optional[_Union[IamPolicySearchResult.Explanation.Permissions, _Mapping]] = ...) -> None: ...
        MATCHED_PERMISSIONS_FIELD_NUMBER: _ClassVar[int]
        matched_permissions: _containers.MessageMap[str, IamPolicySearchResult.Explanation.Permissions]
        def __init__(self, matched_permissions: _Optional[_Mapping[str, IamPolicySearchResult.Explanation.Permissions]] = ...) -> None: ...
    RESOURCE_FIELD_NUMBER: _ClassVar[int]
    ASSET_TYPE_FIELD_NUMBER: _ClassVar[int]
    PROJECT_FIELD_NUMBER: _ClassVar[int]
    FOLDERS_FIELD_NUMBER: _ClassVar[int]
    ORGANIZATION_FIELD_NUMBER: _ClassVar[int]
    POLICY_FIELD_NUMBER: _ClassVar[int]
    EXPLANATION_FIELD_NUMBER: _ClassVar[int]
    resource: str
    asset_type: str
    project: str
    folders: _containers.RepeatedScalarFieldContainer[str]
    organization: str
    policy: _policy_pb2.Policy
    explanation: IamPolicySearchResult.Explanation
    def __init__(self, resource: _Optional[str] = ..., asset_type: _Optional[str] = ..., project: _Optional[str] = ..., folders: _Optional[_Iterable[str]] = ..., organization: _Optional[str] = ..., policy: _Optional[_Union[_policy_pb2.Policy, _Mapping]] = ..., explanation: _Optional[_Union[IamPolicySearchResult.Explanation, _Mapping]] = ...) -> None: ...

class IamPolicyAnalysisState(_message.Message):
    __slots__ = ("code", "cause")
    CODE_FIELD_NUMBER: _ClassVar[int]
    CAUSE_FIELD_NUMBER: _ClassVar[int]
    code: _code_pb2.Code
    cause: str
    def __init__(self, code: _Optional[_Union[_code_pb2.Code, str]] = ..., cause: _Optional[str] = ...) -> None: ...

class ConditionEvaluation(_message.Message):
    __slots__ = ("evaluation_value",)
    class EvaluationValue(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        EVALUATION_VALUE_UNSPECIFIED: _ClassVar[ConditionEvaluation.EvaluationValue]
        TRUE: _ClassVar[ConditionEvaluation.EvaluationValue]
        FALSE: _ClassVar[ConditionEvaluation.EvaluationValue]
        CONDITIONAL: _ClassVar[ConditionEvaluation.EvaluationValue]
    EVALUATION_VALUE_UNSPECIFIED: ConditionEvaluation.EvaluationValue
    TRUE: ConditionEvaluation.EvaluationValue
    FALSE: ConditionEvaluation.EvaluationValue
    CONDITIONAL: ConditionEvaluation.EvaluationValue
    EVALUATION_VALUE_FIELD_NUMBER: _ClassVar[int]
    evaluation_value: ConditionEvaluation.EvaluationValue
    def __init__(self, evaluation_value: _Optional[_Union[ConditionEvaluation.EvaluationValue, str]] = ...) -> None: ...

class IamPolicyAnalysisResult(_message.Message):
    __slots__ = ("attached_resource_full_name", "iam_binding", "access_control_lists", "identity_list", "fully_explored")
    class Resource(_message.Message):
        __slots__ = ("full_resource_name", "analysis_state")
        FULL_RESOURCE_NAME_FIELD_NUMBER: _ClassVar[int]
        ANALYSIS_STATE_FIELD_NUMBER: _ClassVar[int]
        full_resource_name: str
        analysis_state: IamPolicyAnalysisState
        def __init__(self, full_resource_name: _Optional[str] = ..., analysis_state: _Optional[_Union[IamPolicyAnalysisState, _Mapping]] = ...) -> None: ...
    class Access(_message.Message):
        __slots__ = ("role", "permission", "analysis_state")
        ROLE_FIELD_NUMBER: _ClassVar[int]
        PERMISSION_FIELD_NUMBER: _ClassVar[int]
        ANALYSIS_STATE_FIELD_NUMBER: _ClassVar[int]
        role: str
        permission: str
        analysis_state: IamPolicyAnalysisState
        def __init__(self, role: _Optional[str] = ..., permission: _Optional[str] = ..., analysis_state: _Optional[_Union[IamPolicyAnalysisState, _Mapping]] = ...) -> None: ...
    class Identity(_message.Message):
        __slots__ = ("name", "analysis_state")
        NAME_FIELD_NUMBER: _ClassVar[int]
        ANALYSIS_STATE_FIELD_NUMBER: _ClassVar[int]
        name: str
        analysis_state: IamPolicyAnalysisState
        def __init__(self, name: _Optional[str] = ..., analysis_state: _Optional[_Union[IamPolicyAnalysisState, _Mapping]] = ...) -> None: ...
    class Edge(_message.Message):
        __slots__ = ("source_node", "target_node")
        SOURCE_NODE_FIELD_NUMBER: _ClassVar[int]
        TARGET_NODE_FIELD_NUMBER: _ClassVar[int]
        source_node: str
        target_node: str
        def __init__(self, source_node: _Optional[str] = ..., target_node: _Optional[str] = ...) -> None: ...
    class AccessControlList(_message.Message):
        __slots__ = ("resources", "accesses", "resource_edges", "condition_evaluation")
        RESOURCES_FIELD_NUMBER: _ClassVar[int]
        ACCESSES_FIELD_NUMBER: _ClassVar[int]
        RESOURCE_EDGES_FIELD_NUMBER: _ClassVar[int]
        CONDITION_EVALUATION_FIELD_NUMBER: _ClassVar[int]
        resources: _containers.RepeatedCompositeFieldContainer[IamPolicyAnalysisResult.Resource]
        accesses: _containers.RepeatedCompositeFieldContainer[IamPolicyAnalysisResult.Access]
        resource_edges: _containers.RepeatedCompositeFieldContainer[IamPolicyAnalysisResult.Edge]
        condition_evaluation: ConditionEvaluation
        def __init__(self, resources: _Optional[_Iterable[_Union[IamPolicyAnalysisResult.Resource, _Mapping]]] = ..., accesses: _Optional[_Iterable[_Union[IamPolicyAnalysisResult.Access, _Mapping]]] = ..., resource_edges: _Optional[_Iterable[_Union[IamPolicyAnalysisResult.Edge, _Mapping]]] = ..., condition_evaluation: _Optional[_Union[ConditionEvaluation, _Mapping]] = ...) -> None: ...
    class IdentityList(_message.Message):
        __slots__ = ("identities", "group_edges")
        IDENTITIES_FIELD_NUMBER: _ClassVar[int]
        GROUP_EDGES_FIELD_NUMBER: _ClassVar[int]
        identities: _containers.RepeatedCompositeFieldContainer[IamPolicyAnalysisResult.Identity]
        group_edges: _containers.RepeatedCompositeFieldContainer[IamPolicyAnalysisResult.Edge]
        def __init__(self, identities: _Optional[_Iterable[_Union[IamPolicyAnalysisResult.Identity, _Mapping]]] = ..., group_edges: _Optional[_Iterable[_Union[IamPolicyAnalysisResult.Edge, _Mapping]]] = ...) -> None: ...
    ATTACHED_RESOURCE_FULL_NAME_FIELD_NUMBER: _ClassVar[int]
    IAM_BINDING_FIELD_NUMBER: _ClassVar[int]
    ACCESS_CONTROL_LISTS_FIELD_NUMBER: _ClassVar[int]
    IDENTITY_LIST_FIELD_NUMBER: _ClassVar[int]
    FULLY_EXPLORED_FIELD_NUMBER: _ClassVar[int]
    attached_resource_full_name: str
    iam_binding: _policy_pb2.Binding
    access_control_lists: _containers.RepeatedCompositeFieldContainer[IamPolicyAnalysisResult.AccessControlList]
    identity_list: IamPolicyAnalysisResult.IdentityList
    fully_explored: bool
    def __init__(self, attached_resource_full_name: _Optional[str] = ..., iam_binding: _Optional[_Union[_policy_pb2.Binding, _Mapping]] = ..., access_control_lists: _Optional[_Iterable[_Union[IamPolicyAnalysisResult.AccessControlList, _Mapping]]] = ..., identity_list: _Optional[_Union[IamPolicyAnalysisResult.IdentityList, _Mapping]] = ..., fully_explored: bool = ...) -> None: ...
