from google.api import field_behavior_pb2 as _field_behavior_pb2
from google.protobuf import struct_pb2 as _struct_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union
DESCRIPTOR: _descriptor.FileDescriptor

class FeatureState(_message.Message):
    __slots__ = ('analysis_messages',)
    ANALYSIS_MESSAGES_FIELD_NUMBER: _ClassVar[int]
    analysis_messages: _containers.RepeatedCompositeFieldContainer[AnalysisMessage]

    def __init__(self, analysis_messages: _Optional[_Iterable[_Union[AnalysisMessage, _Mapping]]]=...) -> None:
        ...

class MembershipState(_message.Message):
    __slots__ = ('analysis_messages',)
    ANALYSIS_MESSAGES_FIELD_NUMBER: _ClassVar[int]
    analysis_messages: _containers.RepeatedCompositeFieldContainer[AnalysisMessage]

    def __init__(self, analysis_messages: _Optional[_Iterable[_Union[AnalysisMessage, _Mapping]]]=...) -> None:
        ...

class AnalysisMessageBase(_message.Message):
    __slots__ = ('type', 'level', 'documentation_url')

    class Level(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        LEVEL_UNSPECIFIED: _ClassVar[AnalysisMessageBase.Level]
        ERROR: _ClassVar[AnalysisMessageBase.Level]
        WARNING: _ClassVar[AnalysisMessageBase.Level]
        INFO: _ClassVar[AnalysisMessageBase.Level]
    LEVEL_UNSPECIFIED: AnalysisMessageBase.Level
    ERROR: AnalysisMessageBase.Level
    WARNING: AnalysisMessageBase.Level
    INFO: AnalysisMessageBase.Level

    class Type(_message.Message):
        __slots__ = ('display_name', 'code')
        DISPLAY_NAME_FIELD_NUMBER: _ClassVar[int]
        CODE_FIELD_NUMBER: _ClassVar[int]
        display_name: str
        code: str

        def __init__(self, display_name: _Optional[str]=..., code: _Optional[str]=...) -> None:
            ...
    TYPE_FIELD_NUMBER: _ClassVar[int]
    LEVEL_FIELD_NUMBER: _ClassVar[int]
    DOCUMENTATION_URL_FIELD_NUMBER: _ClassVar[int]
    type: AnalysisMessageBase.Type
    level: AnalysisMessageBase.Level
    documentation_url: str

    def __init__(self, type: _Optional[_Union[AnalysisMessageBase.Type, _Mapping]]=..., level: _Optional[_Union[AnalysisMessageBase.Level, str]]=..., documentation_url: _Optional[str]=...) -> None:
        ...

class AnalysisMessage(_message.Message):
    __slots__ = ('message_base', 'description', 'resource_paths', 'args')
    MESSAGE_BASE_FIELD_NUMBER: _ClassVar[int]
    DESCRIPTION_FIELD_NUMBER: _ClassVar[int]
    RESOURCE_PATHS_FIELD_NUMBER: _ClassVar[int]
    ARGS_FIELD_NUMBER: _ClassVar[int]
    message_base: AnalysisMessageBase
    description: str
    resource_paths: _containers.RepeatedScalarFieldContainer[str]
    args: _struct_pb2.Struct

    def __init__(self, message_base: _Optional[_Union[AnalysisMessageBase, _Mapping]]=..., description: _Optional[str]=..., resource_paths: _Optional[_Iterable[str]]=..., args: _Optional[_Union[_struct_pb2.Struct, _Mapping]]=...) -> None:
        ...