from google.api import field_behavior_pb2 as _field_behavior_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union
DESCRIPTOR: _descriptor.FileDescriptor

class Attributes(_message.Message):
    __slots__ = ('criticality', 'environment', 'developer_owners', 'operator_owners', 'business_owners')
    CRITICALITY_FIELD_NUMBER: _ClassVar[int]
    ENVIRONMENT_FIELD_NUMBER: _ClassVar[int]
    DEVELOPER_OWNERS_FIELD_NUMBER: _ClassVar[int]
    OPERATOR_OWNERS_FIELD_NUMBER: _ClassVar[int]
    BUSINESS_OWNERS_FIELD_NUMBER: _ClassVar[int]
    criticality: Criticality
    environment: Environment
    developer_owners: _containers.RepeatedCompositeFieldContainer[ContactInfo]
    operator_owners: _containers.RepeatedCompositeFieldContainer[ContactInfo]
    business_owners: _containers.RepeatedCompositeFieldContainer[ContactInfo]

    def __init__(self, criticality: _Optional[_Union[Criticality, _Mapping]]=..., environment: _Optional[_Union[Environment, _Mapping]]=..., developer_owners: _Optional[_Iterable[_Union[ContactInfo, _Mapping]]]=..., operator_owners: _Optional[_Iterable[_Union[ContactInfo, _Mapping]]]=..., business_owners: _Optional[_Iterable[_Union[ContactInfo, _Mapping]]]=...) -> None:
        ...

class Criticality(_message.Message):
    __slots__ = ('type',)

    class Type(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        TYPE_UNSPECIFIED: _ClassVar[Criticality.Type]
        MISSION_CRITICAL: _ClassVar[Criticality.Type]
        HIGH: _ClassVar[Criticality.Type]
        MEDIUM: _ClassVar[Criticality.Type]
        LOW: _ClassVar[Criticality.Type]
    TYPE_UNSPECIFIED: Criticality.Type
    MISSION_CRITICAL: Criticality.Type
    HIGH: Criticality.Type
    MEDIUM: Criticality.Type
    LOW: Criticality.Type
    TYPE_FIELD_NUMBER: _ClassVar[int]
    type: Criticality.Type

    def __init__(self, type: _Optional[_Union[Criticality.Type, str]]=...) -> None:
        ...

class Environment(_message.Message):
    __slots__ = ('type',)

    class Type(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        TYPE_UNSPECIFIED: _ClassVar[Environment.Type]
        PRODUCTION: _ClassVar[Environment.Type]
        STAGING: _ClassVar[Environment.Type]
        TEST: _ClassVar[Environment.Type]
        DEVELOPMENT: _ClassVar[Environment.Type]
    TYPE_UNSPECIFIED: Environment.Type
    PRODUCTION: Environment.Type
    STAGING: Environment.Type
    TEST: Environment.Type
    DEVELOPMENT: Environment.Type
    TYPE_FIELD_NUMBER: _ClassVar[int]
    type: Environment.Type

    def __init__(self, type: _Optional[_Union[Environment.Type, str]]=...) -> None:
        ...

class ContactInfo(_message.Message):
    __slots__ = ('display_name', 'email')
    DISPLAY_NAME_FIELD_NUMBER: _ClassVar[int]
    EMAIL_FIELD_NUMBER: _ClassVar[int]
    display_name: str
    email: str

    def __init__(self, display_name: _Optional[str]=..., email: _Optional[str]=...) -> None:
        ...