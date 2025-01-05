from google.api import annotations_pb2 as _annotations_pb2
from google.api import client_pb2 as _client_pb2
from google.api import field_behavior_pb2 as _field_behavior_pb2
from google.api import resource_pb2 as _resource_pb2
from google.monitoring.v3 import service_pb2 as _service_pb2
from google.protobuf import empty_pb2 as _empty_pb2
from google.protobuf import field_mask_pb2 as _field_mask_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union
DESCRIPTOR: _descriptor.FileDescriptor

class CreateServiceRequest(_message.Message):
    __slots__ = ('parent', 'service_id', 'service')
    PARENT_FIELD_NUMBER: _ClassVar[int]
    SERVICE_ID_FIELD_NUMBER: _ClassVar[int]
    SERVICE_FIELD_NUMBER: _ClassVar[int]
    parent: str
    service_id: str
    service: _service_pb2.Service

    def __init__(self, parent: _Optional[str]=..., service_id: _Optional[str]=..., service: _Optional[_Union[_service_pb2.Service, _Mapping]]=...) -> None:
        ...

class GetServiceRequest(_message.Message):
    __slots__ = ('name',)
    NAME_FIELD_NUMBER: _ClassVar[int]
    name: str

    def __init__(self, name: _Optional[str]=...) -> None:
        ...

class ListServicesRequest(_message.Message):
    __slots__ = ('parent', 'filter', 'page_size', 'page_token')
    PARENT_FIELD_NUMBER: _ClassVar[int]
    FILTER_FIELD_NUMBER: _ClassVar[int]
    PAGE_SIZE_FIELD_NUMBER: _ClassVar[int]
    PAGE_TOKEN_FIELD_NUMBER: _ClassVar[int]
    parent: str
    filter: str
    page_size: int
    page_token: str

    def __init__(self, parent: _Optional[str]=..., filter: _Optional[str]=..., page_size: _Optional[int]=..., page_token: _Optional[str]=...) -> None:
        ...

class ListServicesResponse(_message.Message):
    __slots__ = ('services', 'next_page_token')
    SERVICES_FIELD_NUMBER: _ClassVar[int]
    NEXT_PAGE_TOKEN_FIELD_NUMBER: _ClassVar[int]
    services: _containers.RepeatedCompositeFieldContainer[_service_pb2.Service]
    next_page_token: str

    def __init__(self, services: _Optional[_Iterable[_Union[_service_pb2.Service, _Mapping]]]=..., next_page_token: _Optional[str]=...) -> None:
        ...

class UpdateServiceRequest(_message.Message):
    __slots__ = ('service', 'update_mask')
    SERVICE_FIELD_NUMBER: _ClassVar[int]
    UPDATE_MASK_FIELD_NUMBER: _ClassVar[int]
    service: _service_pb2.Service
    update_mask: _field_mask_pb2.FieldMask

    def __init__(self, service: _Optional[_Union[_service_pb2.Service, _Mapping]]=..., update_mask: _Optional[_Union[_field_mask_pb2.FieldMask, _Mapping]]=...) -> None:
        ...

class DeleteServiceRequest(_message.Message):
    __slots__ = ('name',)
    NAME_FIELD_NUMBER: _ClassVar[int]
    name: str

    def __init__(self, name: _Optional[str]=...) -> None:
        ...

class CreateServiceLevelObjectiveRequest(_message.Message):
    __slots__ = ('parent', 'service_level_objective_id', 'service_level_objective')
    PARENT_FIELD_NUMBER: _ClassVar[int]
    SERVICE_LEVEL_OBJECTIVE_ID_FIELD_NUMBER: _ClassVar[int]
    SERVICE_LEVEL_OBJECTIVE_FIELD_NUMBER: _ClassVar[int]
    parent: str
    service_level_objective_id: str
    service_level_objective: _service_pb2.ServiceLevelObjective

    def __init__(self, parent: _Optional[str]=..., service_level_objective_id: _Optional[str]=..., service_level_objective: _Optional[_Union[_service_pb2.ServiceLevelObjective, _Mapping]]=...) -> None:
        ...

class GetServiceLevelObjectiveRequest(_message.Message):
    __slots__ = ('name', 'view')
    NAME_FIELD_NUMBER: _ClassVar[int]
    VIEW_FIELD_NUMBER: _ClassVar[int]
    name: str
    view: _service_pb2.ServiceLevelObjective.View

    def __init__(self, name: _Optional[str]=..., view: _Optional[_Union[_service_pb2.ServiceLevelObjective.View, str]]=...) -> None:
        ...

class ListServiceLevelObjectivesRequest(_message.Message):
    __slots__ = ('parent', 'filter', 'page_size', 'page_token', 'view')
    PARENT_FIELD_NUMBER: _ClassVar[int]
    FILTER_FIELD_NUMBER: _ClassVar[int]
    PAGE_SIZE_FIELD_NUMBER: _ClassVar[int]
    PAGE_TOKEN_FIELD_NUMBER: _ClassVar[int]
    VIEW_FIELD_NUMBER: _ClassVar[int]
    parent: str
    filter: str
    page_size: int
    page_token: str
    view: _service_pb2.ServiceLevelObjective.View

    def __init__(self, parent: _Optional[str]=..., filter: _Optional[str]=..., page_size: _Optional[int]=..., page_token: _Optional[str]=..., view: _Optional[_Union[_service_pb2.ServiceLevelObjective.View, str]]=...) -> None:
        ...

class ListServiceLevelObjectivesResponse(_message.Message):
    __slots__ = ('service_level_objectives', 'next_page_token')
    SERVICE_LEVEL_OBJECTIVES_FIELD_NUMBER: _ClassVar[int]
    NEXT_PAGE_TOKEN_FIELD_NUMBER: _ClassVar[int]
    service_level_objectives: _containers.RepeatedCompositeFieldContainer[_service_pb2.ServiceLevelObjective]
    next_page_token: str

    def __init__(self, service_level_objectives: _Optional[_Iterable[_Union[_service_pb2.ServiceLevelObjective, _Mapping]]]=..., next_page_token: _Optional[str]=...) -> None:
        ...

class UpdateServiceLevelObjectiveRequest(_message.Message):
    __slots__ = ('service_level_objective', 'update_mask')
    SERVICE_LEVEL_OBJECTIVE_FIELD_NUMBER: _ClassVar[int]
    UPDATE_MASK_FIELD_NUMBER: _ClassVar[int]
    service_level_objective: _service_pb2.ServiceLevelObjective
    update_mask: _field_mask_pb2.FieldMask

    def __init__(self, service_level_objective: _Optional[_Union[_service_pb2.ServiceLevelObjective, _Mapping]]=..., update_mask: _Optional[_Union[_field_mask_pb2.FieldMask, _Mapping]]=...) -> None:
        ...

class DeleteServiceLevelObjectiveRequest(_message.Message):
    __slots__ = ('name',)
    NAME_FIELD_NUMBER: _ClassVar[int]
    name: str

    def __init__(self, name: _Optional[str]=...) -> None:
        ...