from google.iam.v1 import policy_pb2 as _policy_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union
DESCRIPTOR: _descriptor.FileDescriptor

class StandardResourceMetadata(_message.Message):
    __slots__ = ('name', 'asset_type', 'project', 'display_name', 'description', 'additional_attributes', 'location', 'labels', 'network_tags')

    class LabelsEntry(_message.Message):
        __slots__ = ('key', 'value')
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: str

        def __init__(self, key: _Optional[str]=..., value: _Optional[str]=...) -> None:
            ...
    NAME_FIELD_NUMBER: _ClassVar[int]
    ASSET_TYPE_FIELD_NUMBER: _ClassVar[int]
    PROJECT_FIELD_NUMBER: _ClassVar[int]
    DISPLAY_NAME_FIELD_NUMBER: _ClassVar[int]
    DESCRIPTION_FIELD_NUMBER: _ClassVar[int]
    ADDITIONAL_ATTRIBUTES_FIELD_NUMBER: _ClassVar[int]
    LOCATION_FIELD_NUMBER: _ClassVar[int]
    LABELS_FIELD_NUMBER: _ClassVar[int]
    NETWORK_TAGS_FIELD_NUMBER: _ClassVar[int]
    name: str
    asset_type: str
    project: str
    display_name: str
    description: str
    additional_attributes: _containers.RepeatedScalarFieldContainer[str]
    location: str
    labels: _containers.ScalarMap[str, str]
    network_tags: _containers.RepeatedScalarFieldContainer[str]

    def __init__(self, name: _Optional[str]=..., asset_type: _Optional[str]=..., project: _Optional[str]=..., display_name: _Optional[str]=..., description: _Optional[str]=..., additional_attributes: _Optional[_Iterable[str]]=..., location: _Optional[str]=..., labels: _Optional[_Mapping[str, str]]=..., network_tags: _Optional[_Iterable[str]]=...) -> None:
        ...

class IamPolicySearchResult(_message.Message):
    __slots__ = ('resource', 'project', 'policy', 'explanation')

    class Explanation(_message.Message):
        __slots__ = ('matched_permissions',)

        class MatchedPermissionsEntry(_message.Message):
            __slots__ = ('key', 'value')
            KEY_FIELD_NUMBER: _ClassVar[int]
            VALUE_FIELD_NUMBER: _ClassVar[int]
            key: str
            value: Permissions

            def __init__(self, key: _Optional[str]=..., value: _Optional[_Union[Permissions, _Mapping]]=...) -> None:
                ...
        MATCHED_PERMISSIONS_FIELD_NUMBER: _ClassVar[int]
        matched_permissions: _containers.MessageMap[str, Permissions]

        def __init__(self, matched_permissions: _Optional[_Mapping[str, Permissions]]=...) -> None:
            ...
    RESOURCE_FIELD_NUMBER: _ClassVar[int]
    PROJECT_FIELD_NUMBER: _ClassVar[int]
    POLICY_FIELD_NUMBER: _ClassVar[int]
    EXPLANATION_FIELD_NUMBER: _ClassVar[int]
    resource: str
    project: str
    policy: _policy_pb2.Policy
    explanation: IamPolicySearchResult.Explanation

    def __init__(self, resource: _Optional[str]=..., project: _Optional[str]=..., policy: _Optional[_Union[_policy_pb2.Policy, _Mapping]]=..., explanation: _Optional[_Union[IamPolicySearchResult.Explanation, _Mapping]]=...) -> None:
        ...

class Permissions(_message.Message):
    __slots__ = ('permissions',)
    PERMISSIONS_FIELD_NUMBER: _ClassVar[int]
    permissions: _containers.RepeatedScalarFieldContainer[str]

    def __init__(self, permissions: _Optional[_Iterable[str]]=...) -> None:
        ...