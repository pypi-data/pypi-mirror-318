from google.ads.googleads.v17.common import criterion_category_availability_pb2 as _criterion_category_availability_pb2
from google.api import field_behavior_pb2 as _field_behavior_pb2
from google.api import resource_pb2 as _resource_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class DetailedDemographic(_message.Message):
    __slots__ = ("resource_name", "id", "name", "parent", "launched_to_all", "availabilities")
    RESOURCE_NAME_FIELD_NUMBER: _ClassVar[int]
    ID_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    PARENT_FIELD_NUMBER: _ClassVar[int]
    LAUNCHED_TO_ALL_FIELD_NUMBER: _ClassVar[int]
    AVAILABILITIES_FIELD_NUMBER: _ClassVar[int]
    resource_name: str
    id: int
    name: str
    parent: str
    launched_to_all: bool
    availabilities: _containers.RepeatedCompositeFieldContainer[_criterion_category_availability_pb2.CriterionCategoryAvailability]
    def __init__(self, resource_name: _Optional[str] = ..., id: _Optional[int] = ..., name: _Optional[str] = ..., parent: _Optional[str] = ..., launched_to_all: bool = ..., availabilities: _Optional[_Iterable[_Union[_criterion_category_availability_pb2.CriterionCategoryAvailability, _Mapping]]] = ...) -> None: ...
