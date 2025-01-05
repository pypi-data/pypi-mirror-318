from google.api import field_behavior_pb2 as _field_behavior_pb2
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union
DESCRIPTOR: _descriptor.FileDescriptor

class ParameterDefinition(_message.Message):
    __slots__ = ('name', 'type', 'description')

    class ParameterType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        PARAMETER_TYPE_UNSPECIFIED: _ClassVar[ParameterDefinition.ParameterType]
        STRING: _ClassVar[ParameterDefinition.ParameterType]
        NUMBER: _ClassVar[ParameterDefinition.ParameterType]
        BOOLEAN: _ClassVar[ParameterDefinition.ParameterType]
        NULL: _ClassVar[ParameterDefinition.ParameterType]
        OBJECT: _ClassVar[ParameterDefinition.ParameterType]
        LIST: _ClassVar[ParameterDefinition.ParameterType]
    PARAMETER_TYPE_UNSPECIFIED: ParameterDefinition.ParameterType
    STRING: ParameterDefinition.ParameterType
    NUMBER: ParameterDefinition.ParameterType
    BOOLEAN: ParameterDefinition.ParameterType
    NULL: ParameterDefinition.ParameterType
    OBJECT: ParameterDefinition.ParameterType
    LIST: ParameterDefinition.ParameterType
    NAME_FIELD_NUMBER: _ClassVar[int]
    TYPE_FIELD_NUMBER: _ClassVar[int]
    DESCRIPTION_FIELD_NUMBER: _ClassVar[int]
    name: str
    type: ParameterDefinition.ParameterType
    description: str

    def __init__(self, name: _Optional[str]=..., type: _Optional[_Union[ParameterDefinition.ParameterType, str]]=..., description: _Optional[str]=...) -> None:
        ...