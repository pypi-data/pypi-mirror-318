from google.api import field_behavior_pb2 as _field_behavior_pb2
from google.api import field_info_pb2 as _field_info_pb2
from google.api import resource_pb2 as _resource_pb2
from google.protobuf import timestamp_pb2 as _timestamp_pb2
from google.type import expr_pb2 as _expr_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Mapping as _Mapping, Optional as _Optional, Union as _Union
DESCRIPTOR: _descriptor.FileDescriptor

class PolicyBinding(_message.Message):
    __slots__ = ('name', 'uid', 'etag', 'display_name', 'annotations', 'target', 'policy_kind', 'policy', 'policy_uid', 'condition', 'create_time', 'update_time')

    class PolicyKind(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        POLICY_KIND_UNSPECIFIED: _ClassVar[PolicyBinding.PolicyKind]
        PRINCIPAL_ACCESS_BOUNDARY: _ClassVar[PolicyBinding.PolicyKind]
    POLICY_KIND_UNSPECIFIED: PolicyBinding.PolicyKind
    PRINCIPAL_ACCESS_BOUNDARY: PolicyBinding.PolicyKind

    class Target(_message.Message):
        __slots__ = ('principal_set',)
        PRINCIPAL_SET_FIELD_NUMBER: _ClassVar[int]
        principal_set: str

        def __init__(self, principal_set: _Optional[str]=...) -> None:
            ...

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
    TARGET_FIELD_NUMBER: _ClassVar[int]
    POLICY_KIND_FIELD_NUMBER: _ClassVar[int]
    POLICY_FIELD_NUMBER: _ClassVar[int]
    POLICY_UID_FIELD_NUMBER: _ClassVar[int]
    CONDITION_FIELD_NUMBER: _ClassVar[int]
    CREATE_TIME_FIELD_NUMBER: _ClassVar[int]
    UPDATE_TIME_FIELD_NUMBER: _ClassVar[int]
    name: str
    uid: str
    etag: str
    display_name: str
    annotations: _containers.ScalarMap[str, str]
    target: PolicyBinding.Target
    policy_kind: PolicyBinding.PolicyKind
    policy: str
    policy_uid: str
    condition: _expr_pb2.Expr
    create_time: _timestamp_pb2.Timestamp
    update_time: _timestamp_pb2.Timestamp

    def __init__(self, name: _Optional[str]=..., uid: _Optional[str]=..., etag: _Optional[str]=..., display_name: _Optional[str]=..., annotations: _Optional[_Mapping[str, str]]=..., target: _Optional[_Union[PolicyBinding.Target, _Mapping]]=..., policy_kind: _Optional[_Union[PolicyBinding.PolicyKind, str]]=..., policy: _Optional[str]=..., policy_uid: _Optional[str]=..., condition: _Optional[_Union[_expr_pb2.Expr, _Mapping]]=..., create_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]]=..., update_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]]=...) -> None:
        ...