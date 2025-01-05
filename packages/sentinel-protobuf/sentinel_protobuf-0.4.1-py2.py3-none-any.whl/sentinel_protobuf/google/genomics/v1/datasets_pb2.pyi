from google.api import annotations_pb2 as _annotations_pb2
from google.iam.v1 import iam_policy_pb2 as _iam_policy_pb2
from google.iam.v1 import policy_pb2 as _policy_pb2
from google.protobuf import empty_pb2 as _empty_pb2
from google.protobuf import field_mask_pb2 as _field_mask_pb2
from google.protobuf import timestamp_pb2 as _timestamp_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union
DESCRIPTOR: _descriptor.FileDescriptor

class Dataset(_message.Message):
    __slots__ = ('id', 'project_id', 'name', 'create_time')
    ID_FIELD_NUMBER: _ClassVar[int]
    PROJECT_ID_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    CREATE_TIME_FIELD_NUMBER: _ClassVar[int]
    id: str
    project_id: str
    name: str
    create_time: _timestamp_pb2.Timestamp

    def __init__(self, id: _Optional[str]=..., project_id: _Optional[str]=..., name: _Optional[str]=..., create_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]]=...) -> None:
        ...

class ListDatasetsRequest(_message.Message):
    __slots__ = ('project_id', 'page_size', 'page_token')
    PROJECT_ID_FIELD_NUMBER: _ClassVar[int]
    PAGE_SIZE_FIELD_NUMBER: _ClassVar[int]
    PAGE_TOKEN_FIELD_NUMBER: _ClassVar[int]
    project_id: str
    page_size: int
    page_token: str

    def __init__(self, project_id: _Optional[str]=..., page_size: _Optional[int]=..., page_token: _Optional[str]=...) -> None:
        ...

class ListDatasetsResponse(_message.Message):
    __slots__ = ('datasets', 'next_page_token')
    DATASETS_FIELD_NUMBER: _ClassVar[int]
    NEXT_PAGE_TOKEN_FIELD_NUMBER: _ClassVar[int]
    datasets: _containers.RepeatedCompositeFieldContainer[Dataset]
    next_page_token: str

    def __init__(self, datasets: _Optional[_Iterable[_Union[Dataset, _Mapping]]]=..., next_page_token: _Optional[str]=...) -> None:
        ...

class CreateDatasetRequest(_message.Message):
    __slots__ = ('dataset',)
    DATASET_FIELD_NUMBER: _ClassVar[int]
    dataset: Dataset

    def __init__(self, dataset: _Optional[_Union[Dataset, _Mapping]]=...) -> None:
        ...

class UpdateDatasetRequest(_message.Message):
    __slots__ = ('dataset_id', 'dataset', 'update_mask')
    DATASET_ID_FIELD_NUMBER: _ClassVar[int]
    DATASET_FIELD_NUMBER: _ClassVar[int]
    UPDATE_MASK_FIELD_NUMBER: _ClassVar[int]
    dataset_id: str
    dataset: Dataset
    update_mask: _field_mask_pb2.FieldMask

    def __init__(self, dataset_id: _Optional[str]=..., dataset: _Optional[_Union[Dataset, _Mapping]]=..., update_mask: _Optional[_Union[_field_mask_pb2.FieldMask, _Mapping]]=...) -> None:
        ...

class DeleteDatasetRequest(_message.Message):
    __slots__ = ('dataset_id',)
    DATASET_ID_FIELD_NUMBER: _ClassVar[int]
    dataset_id: str

    def __init__(self, dataset_id: _Optional[str]=...) -> None:
        ...

class UndeleteDatasetRequest(_message.Message):
    __slots__ = ('dataset_id',)
    DATASET_ID_FIELD_NUMBER: _ClassVar[int]
    dataset_id: str

    def __init__(self, dataset_id: _Optional[str]=...) -> None:
        ...

class GetDatasetRequest(_message.Message):
    __slots__ = ('dataset_id',)
    DATASET_ID_FIELD_NUMBER: _ClassVar[int]
    dataset_id: str

    def __init__(self, dataset_id: _Optional[str]=...) -> None:
        ...