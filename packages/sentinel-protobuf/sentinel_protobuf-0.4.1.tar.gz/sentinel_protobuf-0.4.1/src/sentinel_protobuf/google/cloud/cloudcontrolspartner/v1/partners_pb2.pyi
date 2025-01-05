from google.api import field_behavior_pb2 as _field_behavior_pb2
from google.api import resource_pb2 as _resource_pb2
from google.protobuf import timestamp_pb2 as _timestamp_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union
DESCRIPTOR: _descriptor.FileDescriptor

class Partner(_message.Message):
    __slots__ = ('name', 'skus', 'ekm_solutions', 'operated_cloud_regions', 'partner_project_id', 'create_time', 'update_time')
    NAME_FIELD_NUMBER: _ClassVar[int]
    SKUS_FIELD_NUMBER: _ClassVar[int]
    EKM_SOLUTIONS_FIELD_NUMBER: _ClassVar[int]
    OPERATED_CLOUD_REGIONS_FIELD_NUMBER: _ClassVar[int]
    PARTNER_PROJECT_ID_FIELD_NUMBER: _ClassVar[int]
    CREATE_TIME_FIELD_NUMBER: _ClassVar[int]
    UPDATE_TIME_FIELD_NUMBER: _ClassVar[int]
    name: str
    skus: _containers.RepeatedCompositeFieldContainer[Sku]
    ekm_solutions: _containers.RepeatedCompositeFieldContainer[EkmMetadata]
    operated_cloud_regions: _containers.RepeatedScalarFieldContainer[str]
    partner_project_id: str
    create_time: _timestamp_pb2.Timestamp
    update_time: _timestamp_pb2.Timestamp

    def __init__(self, name: _Optional[str]=..., skus: _Optional[_Iterable[_Union[Sku, _Mapping]]]=..., ekm_solutions: _Optional[_Iterable[_Union[EkmMetadata, _Mapping]]]=..., operated_cloud_regions: _Optional[_Iterable[str]]=..., partner_project_id: _Optional[str]=..., create_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]]=..., update_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]]=...) -> None:
        ...

class GetPartnerRequest(_message.Message):
    __slots__ = ('name',)
    NAME_FIELD_NUMBER: _ClassVar[int]
    name: str

    def __init__(self, name: _Optional[str]=...) -> None:
        ...

class Sku(_message.Message):
    __slots__ = ('id', 'display_name')
    ID_FIELD_NUMBER: _ClassVar[int]
    DISPLAY_NAME_FIELD_NUMBER: _ClassVar[int]
    id: str
    display_name: str

    def __init__(self, id: _Optional[str]=..., display_name: _Optional[str]=...) -> None:
        ...

class EkmMetadata(_message.Message):
    __slots__ = ('ekm_solution', 'ekm_endpoint_uri')

    class EkmSolution(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        EKM_SOLUTION_UNSPECIFIED: _ClassVar[EkmMetadata.EkmSolution]
        FORTANIX: _ClassVar[EkmMetadata.EkmSolution]
        FUTUREX: _ClassVar[EkmMetadata.EkmSolution]
        THALES: _ClassVar[EkmMetadata.EkmSolution]
        VIRTRU: _ClassVar[EkmMetadata.EkmSolution]
    EKM_SOLUTION_UNSPECIFIED: EkmMetadata.EkmSolution
    FORTANIX: EkmMetadata.EkmSolution
    FUTUREX: EkmMetadata.EkmSolution
    THALES: EkmMetadata.EkmSolution
    VIRTRU: EkmMetadata.EkmSolution
    EKM_SOLUTION_FIELD_NUMBER: _ClassVar[int]
    EKM_ENDPOINT_URI_FIELD_NUMBER: _ClassVar[int]
    ekm_solution: EkmMetadata.EkmSolution
    ekm_endpoint_uri: str

    def __init__(self, ekm_solution: _Optional[_Union[EkmMetadata.EkmSolution, str]]=..., ekm_endpoint_uri: _Optional[str]=...) -> None:
        ...