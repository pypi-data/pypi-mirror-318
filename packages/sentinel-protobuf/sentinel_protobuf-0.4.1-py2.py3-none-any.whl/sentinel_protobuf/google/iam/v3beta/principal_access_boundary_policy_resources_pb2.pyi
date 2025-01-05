from google.api import field_behavior_pb2 as _field_behavior_pb2
from google.api import field_info_pb2 as _field_info_pb2
from google.api import resource_pb2 as _resource_pb2
from google.protobuf import timestamp_pb2 as _timestamp_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union
DESCRIPTOR: _descriptor.FileDescriptor

class PrincipalAccessBoundaryPolicy(_message.Message):
    __slots__ = ('name', 'uid', 'etag', 'display_name', 'annotations', 'create_time', 'update_time', 'details')

    class AnnotationsEntry(_message.Message):
        __slots__ = ('key', 'value')
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: str

        def __init__(self, key: _Optional[str]=..., value: _Optional[str]=...) -> None:
            ...
    NAME_FIELD_NUMBER: _ClassVar[int]
    UID_FIELD_NUMBER: _ClassVar[int]
    ETAG_FIELD_NUMBER: _ClassVar[int]
    DISPLAY_NAME_FIELD_NUMBER: _ClassVar[int]
    ANNOTATIONS_FIELD_NUMBER: _ClassVar[int]
    CREATE_TIME_FIELD_NUMBER: _ClassVar[int]
    UPDATE_TIME_FIELD_NUMBER: _ClassVar[int]
    DETAILS_FIELD_NUMBER: _ClassVar[int]
    name: str
    uid: str
    etag: str
    display_name: str
    annotations: _containers.ScalarMap[str, str]
    create_time: _timestamp_pb2.Timestamp
    update_time: _timestamp_pb2.Timestamp
    details: PrincipalAccessBoundaryPolicyDetails

    def __init__(self, name: _Optional[str]=..., uid: _Optional[str]=..., etag: _Optional[str]=..., display_name: _Optional[str]=..., annotations: _Optional[_Mapping[str, str]]=..., create_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]]=..., update_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]]=..., details: _Optional[_Union[PrincipalAccessBoundaryPolicyDetails, _Mapping]]=...) -> None:
        ...

class PrincipalAccessBoundaryPolicyDetails(_message.Message):
    __slots__ = ('rules', 'enforcement_version')
    RULES_FIELD_NUMBER: _ClassVar[int]
    ENFORCEMENT_VERSION_FIELD_NUMBER: _ClassVar[int]
    rules: _containers.RepeatedCompositeFieldContainer[PrincipalAccessBoundaryPolicyRule]
    enforcement_version: str

    def __init__(self, rules: _Optional[_Iterable[_Union[PrincipalAccessBoundaryPolicyRule, _Mapping]]]=..., enforcement_version: _Optional[str]=...) -> None:
        ...

class PrincipalAccessBoundaryPolicyRule(_message.Message):
    __slots__ = ('description', 'resources', 'effect')

    class Effect(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        EFFECT_UNSPECIFIED: _ClassVar[PrincipalAccessBoundaryPolicyRule.Effect]
        ALLOW: _ClassVar[PrincipalAccessBoundaryPolicyRule.Effect]
    EFFECT_UNSPECIFIED: PrincipalAccessBoundaryPolicyRule.Effect
    ALLOW: PrincipalAccessBoundaryPolicyRule.Effect
    DESCRIPTION_FIELD_NUMBER: _ClassVar[int]
    RESOURCES_FIELD_NUMBER: _ClassVar[int]
    EFFECT_FIELD_NUMBER: _ClassVar[int]
    description: str
    resources: _containers.RepeatedScalarFieldContainer[str]
    effect: PrincipalAccessBoundaryPolicyRule.Effect

    def __init__(self, description: _Optional[str]=..., resources: _Optional[_Iterable[str]]=..., effect: _Optional[_Union[PrincipalAccessBoundaryPolicyRule.Effect, str]]=...) -> None:
        ...