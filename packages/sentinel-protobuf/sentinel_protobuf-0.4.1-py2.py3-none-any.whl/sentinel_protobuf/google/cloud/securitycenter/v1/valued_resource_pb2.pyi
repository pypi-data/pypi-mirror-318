from google.api import resource_pb2 as _resource_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union
DESCRIPTOR: _descriptor.FileDescriptor

class ValuedResource(_message.Message):
    __slots__ = ('name', 'resource', 'resource_type', 'display_name', 'resource_value', 'exposed_score', 'resource_value_configs_used')

    class ResourceValue(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        RESOURCE_VALUE_UNSPECIFIED: _ClassVar[ValuedResource.ResourceValue]
        RESOURCE_VALUE_LOW: _ClassVar[ValuedResource.ResourceValue]
        RESOURCE_VALUE_MEDIUM: _ClassVar[ValuedResource.ResourceValue]
        RESOURCE_VALUE_HIGH: _ClassVar[ValuedResource.ResourceValue]
    RESOURCE_VALUE_UNSPECIFIED: ValuedResource.ResourceValue
    RESOURCE_VALUE_LOW: ValuedResource.ResourceValue
    RESOURCE_VALUE_MEDIUM: ValuedResource.ResourceValue
    RESOURCE_VALUE_HIGH: ValuedResource.ResourceValue
    NAME_FIELD_NUMBER: _ClassVar[int]
    RESOURCE_FIELD_NUMBER: _ClassVar[int]
    RESOURCE_TYPE_FIELD_NUMBER: _ClassVar[int]
    DISPLAY_NAME_FIELD_NUMBER: _ClassVar[int]
    RESOURCE_VALUE_FIELD_NUMBER: _ClassVar[int]
    EXPOSED_SCORE_FIELD_NUMBER: _ClassVar[int]
    RESOURCE_VALUE_CONFIGS_USED_FIELD_NUMBER: _ClassVar[int]
    name: str
    resource: str
    resource_type: str
    display_name: str
    resource_value: ValuedResource.ResourceValue
    exposed_score: float
    resource_value_configs_used: _containers.RepeatedCompositeFieldContainer[ResourceValueConfigMetadata]

    def __init__(self, name: _Optional[str]=..., resource: _Optional[str]=..., resource_type: _Optional[str]=..., display_name: _Optional[str]=..., resource_value: _Optional[_Union[ValuedResource.ResourceValue, str]]=..., exposed_score: _Optional[float]=..., resource_value_configs_used: _Optional[_Iterable[_Union[ResourceValueConfigMetadata, _Mapping]]]=...) -> None:
        ...

class ResourceValueConfigMetadata(_message.Message):
    __slots__ = ('name',)
    NAME_FIELD_NUMBER: _ClassVar[int]
    name: str

    def __init__(self, name: _Optional[str]=...) -> None:
        ...