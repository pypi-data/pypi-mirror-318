from google.api import launch_stage_pb2 as _launch_stage_pb2
from google.api import resource_pb2 as _resource_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union
DESCRIPTOR: _descriptor.FileDescriptor

class ProcessorType(_message.Message):
    __slots__ = ('name', 'type', 'category', 'available_locations', 'allow_creation', 'launch_stage', 'sample_document_uris')

    class LocationInfo(_message.Message):
        __slots__ = ('location_id',)
        LOCATION_ID_FIELD_NUMBER: _ClassVar[int]
        location_id: str

        def __init__(self, location_id: _Optional[str]=...) -> None:
            ...
    NAME_FIELD_NUMBER: _ClassVar[int]
    TYPE_FIELD_NUMBER: _ClassVar[int]
    CATEGORY_FIELD_NUMBER: _ClassVar[int]
    AVAILABLE_LOCATIONS_FIELD_NUMBER: _ClassVar[int]
    ALLOW_CREATION_FIELD_NUMBER: _ClassVar[int]
    LAUNCH_STAGE_FIELD_NUMBER: _ClassVar[int]
    SAMPLE_DOCUMENT_URIS_FIELD_NUMBER: _ClassVar[int]
    name: str
    type: str
    category: str
    available_locations: _containers.RepeatedCompositeFieldContainer[ProcessorType.LocationInfo]
    allow_creation: bool
    launch_stage: _launch_stage_pb2.LaunchStage
    sample_document_uris: _containers.RepeatedScalarFieldContainer[str]

    def __init__(self, name: _Optional[str]=..., type: _Optional[str]=..., category: _Optional[str]=..., available_locations: _Optional[_Iterable[_Union[ProcessorType.LocationInfo, _Mapping]]]=..., allow_creation: bool=..., launch_stage: _Optional[_Union[_launch_stage_pb2.LaunchStage, str]]=..., sample_document_uris: _Optional[_Iterable[str]]=...) -> None:
        ...