from google.api import resource_pb2 as _resource_pb2
from google.devtools.resultstore.v2 import common_pb2 as _common_pb2
from google.devtools.resultstore.v2 import file_pb2 as _file_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union
DESCRIPTOR: _descriptor.FileDescriptor

class TargetType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    TARGET_TYPE_UNSPECIFIED: _ClassVar[TargetType]
    APPLICATION: _ClassVar[TargetType]
    BINARY: _ClassVar[TargetType]
    LIBRARY: _ClassVar[TargetType]
    PACKAGE: _ClassVar[TargetType]
    TEST: _ClassVar[TargetType]

class TestSize(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    TEST_SIZE_UNSPECIFIED: _ClassVar[TestSize]
    SMALL: _ClassVar[TestSize]
    MEDIUM: _ClassVar[TestSize]
    LARGE: _ClassVar[TestSize]
    ENORMOUS: _ClassVar[TestSize]
    OTHER_SIZE: _ClassVar[TestSize]
TARGET_TYPE_UNSPECIFIED: TargetType
APPLICATION: TargetType
BINARY: TargetType
LIBRARY: TargetType
PACKAGE: TargetType
TEST: TargetType
TEST_SIZE_UNSPECIFIED: TestSize
SMALL: TestSize
MEDIUM: TestSize
LARGE: TestSize
ENORMOUS: TestSize
OTHER_SIZE: TestSize

class Target(_message.Message):
    __slots__ = ('name', 'id', 'status_attributes', 'timing', 'target_attributes', 'test_attributes', 'properties', 'files', 'visible')

    class Id(_message.Message):
        __slots__ = ('invocation_id', 'target_id')
        INVOCATION_ID_FIELD_NUMBER: _ClassVar[int]
        TARGET_ID_FIELD_NUMBER: _ClassVar[int]
        invocation_id: str
        target_id: str

        def __init__(self, invocation_id: _Optional[str]=..., target_id: _Optional[str]=...) -> None:
            ...
    NAME_FIELD_NUMBER: _ClassVar[int]
    ID_FIELD_NUMBER: _ClassVar[int]
    STATUS_ATTRIBUTES_FIELD_NUMBER: _ClassVar[int]
    TIMING_FIELD_NUMBER: _ClassVar[int]
    TARGET_ATTRIBUTES_FIELD_NUMBER: _ClassVar[int]
    TEST_ATTRIBUTES_FIELD_NUMBER: _ClassVar[int]
    PROPERTIES_FIELD_NUMBER: _ClassVar[int]
    FILES_FIELD_NUMBER: _ClassVar[int]
    VISIBLE_FIELD_NUMBER: _ClassVar[int]
    name: str
    id: Target.Id
    status_attributes: _common_pb2.StatusAttributes
    timing: _common_pb2.Timing
    target_attributes: TargetAttributes
    test_attributes: TestAttributes
    properties: _containers.RepeatedCompositeFieldContainer[_common_pb2.Property]
    files: _containers.RepeatedCompositeFieldContainer[_file_pb2.File]
    visible: bool

    def __init__(self, name: _Optional[str]=..., id: _Optional[_Union[Target.Id, _Mapping]]=..., status_attributes: _Optional[_Union[_common_pb2.StatusAttributes, _Mapping]]=..., timing: _Optional[_Union[_common_pb2.Timing, _Mapping]]=..., target_attributes: _Optional[_Union[TargetAttributes, _Mapping]]=..., test_attributes: _Optional[_Union[TestAttributes, _Mapping]]=..., properties: _Optional[_Iterable[_Union[_common_pb2.Property, _Mapping]]]=..., files: _Optional[_Iterable[_Union[_file_pb2.File, _Mapping]]]=..., visible: bool=...) -> None:
        ...

class TargetAttributes(_message.Message):
    __slots__ = ('type', 'language', 'tags')
    TYPE_FIELD_NUMBER: _ClassVar[int]
    LANGUAGE_FIELD_NUMBER: _ClassVar[int]
    TAGS_FIELD_NUMBER: _ClassVar[int]
    type: TargetType
    language: _common_pb2.Language
    tags: _containers.RepeatedScalarFieldContainer[str]

    def __init__(self, type: _Optional[_Union[TargetType, str]]=..., language: _Optional[_Union[_common_pb2.Language, str]]=..., tags: _Optional[_Iterable[str]]=...) -> None:
        ...

class TestAttributes(_message.Message):
    __slots__ = ('size',)
    SIZE_FIELD_NUMBER: _ClassVar[int]
    size: TestSize

    def __init__(self, size: _Optional[_Union[TestSize, str]]=...) -> None:
        ...