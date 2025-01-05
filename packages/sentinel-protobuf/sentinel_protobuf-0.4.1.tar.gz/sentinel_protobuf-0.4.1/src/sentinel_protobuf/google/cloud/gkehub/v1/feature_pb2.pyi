from google.api import field_behavior_pb2 as _field_behavior_pb2
from google.api import resource_pb2 as _resource_pb2
from google.cloud.gkehub.v1.configmanagement import configmanagement_pb2 as _configmanagement_pb2
from google.cloud.gkehub.v1.multiclusteringress import multiclusteringress_pb2 as _multiclusteringress_pb2
from google.protobuf import timestamp_pb2 as _timestamp_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class Feature(_message.Message):
    __slots__ = ("name", "labels", "resource_state", "spec", "membership_specs", "state", "membership_states", "create_time", "update_time", "delete_time")
    class LabelsEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: str
        def __init__(self, key: _Optional[str] = ..., value: _Optional[str] = ...) -> None: ...
    class MembershipSpecsEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: MembershipFeatureSpec
        def __init__(self, key: _Optional[str] = ..., value: _Optional[_Union[MembershipFeatureSpec, _Mapping]] = ...) -> None: ...
    class MembershipStatesEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: MembershipFeatureState
        def __init__(self, key: _Optional[str] = ..., value: _Optional[_Union[MembershipFeatureState, _Mapping]] = ...) -> None: ...
    NAME_FIELD_NUMBER: _ClassVar[int]
    LABELS_FIELD_NUMBER: _ClassVar[int]
    RESOURCE_STATE_FIELD_NUMBER: _ClassVar[int]
    SPEC_FIELD_NUMBER: _ClassVar[int]
    MEMBERSHIP_SPECS_FIELD_NUMBER: _ClassVar[int]
    STATE_FIELD_NUMBER: _ClassVar[int]
    MEMBERSHIP_STATES_FIELD_NUMBER: _ClassVar[int]
    CREATE_TIME_FIELD_NUMBER: _ClassVar[int]
    UPDATE_TIME_FIELD_NUMBER: _ClassVar[int]
    DELETE_TIME_FIELD_NUMBER: _ClassVar[int]
    name: str
    labels: _containers.ScalarMap[str, str]
    resource_state: FeatureResourceState
    spec: CommonFeatureSpec
    membership_specs: _containers.MessageMap[str, MembershipFeatureSpec]
    state: CommonFeatureState
    membership_states: _containers.MessageMap[str, MembershipFeatureState]
    create_time: _timestamp_pb2.Timestamp
    update_time: _timestamp_pb2.Timestamp
    delete_time: _timestamp_pb2.Timestamp
    def __init__(self, name: _Optional[str] = ..., labels: _Optional[_Mapping[str, str]] = ..., resource_state: _Optional[_Union[FeatureResourceState, _Mapping]] = ..., spec: _Optional[_Union[CommonFeatureSpec, _Mapping]] = ..., membership_specs: _Optional[_Mapping[str, MembershipFeatureSpec]] = ..., state: _Optional[_Union[CommonFeatureState, _Mapping]] = ..., membership_states: _Optional[_Mapping[str, MembershipFeatureState]] = ..., create_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., update_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., delete_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ...) -> None: ...

class FeatureResourceState(_message.Message):
    __slots__ = ("state",)
    class State(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        STATE_UNSPECIFIED: _ClassVar[FeatureResourceState.State]
        ENABLING: _ClassVar[FeatureResourceState.State]
        ACTIVE: _ClassVar[FeatureResourceState.State]
        DISABLING: _ClassVar[FeatureResourceState.State]
        UPDATING: _ClassVar[FeatureResourceState.State]
        SERVICE_UPDATING: _ClassVar[FeatureResourceState.State]
    STATE_UNSPECIFIED: FeatureResourceState.State
    ENABLING: FeatureResourceState.State
    ACTIVE: FeatureResourceState.State
    DISABLING: FeatureResourceState.State
    UPDATING: FeatureResourceState.State
    SERVICE_UPDATING: FeatureResourceState.State
    STATE_FIELD_NUMBER: _ClassVar[int]
    state: FeatureResourceState.State
    def __init__(self, state: _Optional[_Union[FeatureResourceState.State, str]] = ...) -> None: ...

class FeatureState(_message.Message):
    __slots__ = ("code", "description", "update_time")
    class Code(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        CODE_UNSPECIFIED: _ClassVar[FeatureState.Code]
        OK: _ClassVar[FeatureState.Code]
        WARNING: _ClassVar[FeatureState.Code]
        ERROR: _ClassVar[FeatureState.Code]
    CODE_UNSPECIFIED: FeatureState.Code
    OK: FeatureState.Code
    WARNING: FeatureState.Code
    ERROR: FeatureState.Code
    CODE_FIELD_NUMBER: _ClassVar[int]
    DESCRIPTION_FIELD_NUMBER: _ClassVar[int]
    UPDATE_TIME_FIELD_NUMBER: _ClassVar[int]
    code: FeatureState.Code
    description: str
    update_time: _timestamp_pb2.Timestamp
    def __init__(self, code: _Optional[_Union[FeatureState.Code, str]] = ..., description: _Optional[str] = ..., update_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ...) -> None: ...

class CommonFeatureSpec(_message.Message):
    __slots__ = ("multiclusteringress",)
    MULTICLUSTERINGRESS_FIELD_NUMBER: _ClassVar[int]
    multiclusteringress: _multiclusteringress_pb2.FeatureSpec
    def __init__(self, multiclusteringress: _Optional[_Union[_multiclusteringress_pb2.FeatureSpec, _Mapping]] = ...) -> None: ...

class CommonFeatureState(_message.Message):
    __slots__ = ("state",)
    STATE_FIELD_NUMBER: _ClassVar[int]
    state: FeatureState
    def __init__(self, state: _Optional[_Union[FeatureState, _Mapping]] = ...) -> None: ...

class MembershipFeatureSpec(_message.Message):
    __slots__ = ("configmanagement",)
    CONFIGMANAGEMENT_FIELD_NUMBER: _ClassVar[int]
    configmanagement: _configmanagement_pb2.MembershipSpec
    def __init__(self, configmanagement: _Optional[_Union[_configmanagement_pb2.MembershipSpec, _Mapping]] = ...) -> None: ...

class MembershipFeatureState(_message.Message):
    __slots__ = ("configmanagement", "state")
    CONFIGMANAGEMENT_FIELD_NUMBER: _ClassVar[int]
    STATE_FIELD_NUMBER: _ClassVar[int]
    configmanagement: _configmanagement_pb2.MembershipState
    state: FeatureState
    def __init__(self, configmanagement: _Optional[_Union[_configmanagement_pb2.MembershipState, _Mapping]] = ..., state: _Optional[_Union[FeatureState, _Mapping]] = ...) -> None: ...
