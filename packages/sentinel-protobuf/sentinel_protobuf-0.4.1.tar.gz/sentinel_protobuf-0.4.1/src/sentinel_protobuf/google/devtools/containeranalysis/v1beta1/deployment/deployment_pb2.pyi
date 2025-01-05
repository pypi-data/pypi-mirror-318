from google.protobuf import timestamp_pb2 as _timestamp_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union
DESCRIPTOR: _descriptor.FileDescriptor

class Deployable(_message.Message):
    __slots__ = ('resource_uri',)
    RESOURCE_URI_FIELD_NUMBER: _ClassVar[int]
    resource_uri: _containers.RepeatedScalarFieldContainer[str]

    def __init__(self, resource_uri: _Optional[_Iterable[str]]=...) -> None:
        ...

class Details(_message.Message):
    __slots__ = ('deployment',)
    DEPLOYMENT_FIELD_NUMBER: _ClassVar[int]
    deployment: Deployment

    def __init__(self, deployment: _Optional[_Union[Deployment, _Mapping]]=...) -> None:
        ...

class Deployment(_message.Message):
    __slots__ = ('user_email', 'deploy_time', 'undeploy_time', 'config', 'address', 'resource_uri', 'platform')

    class Platform(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        PLATFORM_UNSPECIFIED: _ClassVar[Deployment.Platform]
        GKE: _ClassVar[Deployment.Platform]
        FLEX: _ClassVar[Deployment.Platform]
        CUSTOM: _ClassVar[Deployment.Platform]
    PLATFORM_UNSPECIFIED: Deployment.Platform
    GKE: Deployment.Platform
    FLEX: Deployment.Platform
    CUSTOM: Deployment.Platform
    USER_EMAIL_FIELD_NUMBER: _ClassVar[int]
    DEPLOY_TIME_FIELD_NUMBER: _ClassVar[int]
    UNDEPLOY_TIME_FIELD_NUMBER: _ClassVar[int]
    CONFIG_FIELD_NUMBER: _ClassVar[int]
    ADDRESS_FIELD_NUMBER: _ClassVar[int]
    RESOURCE_URI_FIELD_NUMBER: _ClassVar[int]
    PLATFORM_FIELD_NUMBER: _ClassVar[int]
    user_email: str
    deploy_time: _timestamp_pb2.Timestamp
    undeploy_time: _timestamp_pb2.Timestamp
    config: str
    address: str
    resource_uri: _containers.RepeatedScalarFieldContainer[str]
    platform: Deployment.Platform

    def __init__(self, user_email: _Optional[str]=..., deploy_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]]=..., undeploy_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]]=..., config: _Optional[str]=..., address: _Optional[str]=..., resource_uri: _Optional[_Iterable[str]]=..., platform: _Optional[_Union[Deployment.Platform, str]]=...) -> None:
        ...