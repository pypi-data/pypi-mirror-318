from google.api import field_behavior_pb2 as _field_behavior_pb2
from google.api import resource_pb2 as _resource_pb2
from google.protobuf import timestamp_pb2 as _timestamp_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Mapping as _Mapping, Optional as _Optional, Union as _Union
DESCRIPTOR: _descriptor.FileDescriptor

class Project(_message.Message):
    __slots__ = ('name', 'create_time', 'provision_completion_time', 'service_terms_map')

    class ServiceTerms(_message.Message):
        __slots__ = ('id', 'version', 'state', 'accept_time', 'decline_time')

        class State(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
            __slots__ = ()
            STATE_UNSPECIFIED: _ClassVar[Project.ServiceTerms.State]
            TERMS_ACCEPTED: _ClassVar[Project.ServiceTerms.State]
            TERMS_PENDING: _ClassVar[Project.ServiceTerms.State]
            TERMS_DECLINED: _ClassVar[Project.ServiceTerms.State]
        STATE_UNSPECIFIED: Project.ServiceTerms.State
        TERMS_ACCEPTED: Project.ServiceTerms.State
        TERMS_PENDING: Project.ServiceTerms.State
        TERMS_DECLINED: Project.ServiceTerms.State
        ID_FIELD_NUMBER: _ClassVar[int]
        VERSION_FIELD_NUMBER: _ClassVar[int]
        STATE_FIELD_NUMBER: _ClassVar[int]
        ACCEPT_TIME_FIELD_NUMBER: _ClassVar[int]
        DECLINE_TIME_FIELD_NUMBER: _ClassVar[int]
        id: str
        version: str
        state: Project.ServiceTerms.State
        accept_time: _timestamp_pb2.Timestamp
        decline_time: _timestamp_pb2.Timestamp

        def __init__(self, id: _Optional[str]=..., version: _Optional[str]=..., state: _Optional[_Union[Project.ServiceTerms.State, str]]=..., accept_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]]=..., decline_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]]=...) -> None:
            ...

    class ServiceTermsMapEntry(_message.Message):
        __slots__ = ('key', 'value')
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: Project.ServiceTerms

        def __init__(self, key: _Optional[str]=..., value: _Optional[_Union[Project.ServiceTerms, _Mapping]]=...) -> None:
            ...
    NAME_FIELD_NUMBER: _ClassVar[int]
    CREATE_TIME_FIELD_NUMBER: _ClassVar[int]
    PROVISION_COMPLETION_TIME_FIELD_NUMBER: _ClassVar[int]
    SERVICE_TERMS_MAP_FIELD_NUMBER: _ClassVar[int]
    name: str
    create_time: _timestamp_pb2.Timestamp
    provision_completion_time: _timestamp_pb2.Timestamp
    service_terms_map: _containers.MessageMap[str, Project.ServiceTerms]

    def __init__(self, name: _Optional[str]=..., create_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]]=..., provision_completion_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]]=..., service_terms_map: _Optional[_Mapping[str, Project.ServiceTerms]]=...) -> None:
        ...