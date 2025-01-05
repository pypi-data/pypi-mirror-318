from google.api import field_behavior_pb2 as _field_behavior_pb2
from google.api import resource_pb2 as _resource_pb2
from google.cloud.translate.v3 import common_pb2 as _common_pb2
from google.protobuf import timestamp_pb2 as _timestamp_pb2
from google.rpc import status_pb2 as _status_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union
DESCRIPTOR: _descriptor.FileDescriptor

class ImportDataRequest(_message.Message):
    __slots__ = ('dataset', 'input_config')
    DATASET_FIELD_NUMBER: _ClassVar[int]
    INPUT_CONFIG_FIELD_NUMBER: _ClassVar[int]
    dataset: str
    input_config: DatasetInputConfig

    def __init__(self, dataset: _Optional[str]=..., input_config: _Optional[_Union[DatasetInputConfig, _Mapping]]=...) -> None:
        ...

class DatasetInputConfig(_message.Message):
    __slots__ = ('input_files',)

    class InputFile(_message.Message):
        __slots__ = ('usage', 'gcs_source')
        USAGE_FIELD_NUMBER: _ClassVar[int]
        GCS_SOURCE_FIELD_NUMBER: _ClassVar[int]
        usage: str
        gcs_source: _common_pb2.GcsInputSource

        def __init__(self, usage: _Optional[str]=..., gcs_source: _Optional[_Union[_common_pb2.GcsInputSource, _Mapping]]=...) -> None:
            ...
    INPUT_FILES_FIELD_NUMBER: _ClassVar[int]
    input_files: _containers.RepeatedCompositeFieldContainer[DatasetInputConfig.InputFile]

    def __init__(self, input_files: _Optional[_Iterable[_Union[DatasetInputConfig.InputFile, _Mapping]]]=...) -> None:
        ...

class ImportDataMetadata(_message.Message):
    __slots__ = ('state', 'create_time', 'update_time', 'error')
    STATE_FIELD_NUMBER: _ClassVar[int]
    CREATE_TIME_FIELD_NUMBER: _ClassVar[int]
    UPDATE_TIME_FIELD_NUMBER: _ClassVar[int]
    ERROR_FIELD_NUMBER: _ClassVar[int]
    state: _common_pb2.OperationState
    create_time: _timestamp_pb2.Timestamp
    update_time: _timestamp_pb2.Timestamp
    error: _status_pb2.Status

    def __init__(self, state: _Optional[_Union[_common_pb2.OperationState, str]]=..., create_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]]=..., update_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]]=..., error: _Optional[_Union[_status_pb2.Status, _Mapping]]=...) -> None:
        ...

class ExportDataRequest(_message.Message):
    __slots__ = ('dataset', 'output_config')
    DATASET_FIELD_NUMBER: _ClassVar[int]
    OUTPUT_CONFIG_FIELD_NUMBER: _ClassVar[int]
    dataset: str
    output_config: DatasetOutputConfig

    def __init__(self, dataset: _Optional[str]=..., output_config: _Optional[_Union[DatasetOutputConfig, _Mapping]]=...) -> None:
        ...

class DatasetOutputConfig(_message.Message):
    __slots__ = ('gcs_destination',)
    GCS_DESTINATION_FIELD_NUMBER: _ClassVar[int]
    gcs_destination: _common_pb2.GcsOutputDestination

    def __init__(self, gcs_destination: _Optional[_Union[_common_pb2.GcsOutputDestination, _Mapping]]=...) -> None:
        ...

class ExportDataMetadata(_message.Message):
    __slots__ = ('state', 'create_time', 'update_time', 'error')
    STATE_FIELD_NUMBER: _ClassVar[int]
    CREATE_TIME_FIELD_NUMBER: _ClassVar[int]
    UPDATE_TIME_FIELD_NUMBER: _ClassVar[int]
    ERROR_FIELD_NUMBER: _ClassVar[int]
    state: _common_pb2.OperationState
    create_time: _timestamp_pb2.Timestamp
    update_time: _timestamp_pb2.Timestamp
    error: _status_pb2.Status

    def __init__(self, state: _Optional[_Union[_common_pb2.OperationState, str]]=..., create_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]]=..., update_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]]=..., error: _Optional[_Union[_status_pb2.Status, _Mapping]]=...) -> None:
        ...

class DeleteDatasetRequest(_message.Message):
    __slots__ = ('name',)
    NAME_FIELD_NUMBER: _ClassVar[int]
    name: str

    def __init__(self, name: _Optional[str]=...) -> None:
        ...

class DeleteDatasetMetadata(_message.Message):
    __slots__ = ('state', 'create_time', 'update_time', 'error')
    STATE_FIELD_NUMBER: _ClassVar[int]
    CREATE_TIME_FIELD_NUMBER: _ClassVar[int]
    UPDATE_TIME_FIELD_NUMBER: _ClassVar[int]
    ERROR_FIELD_NUMBER: _ClassVar[int]
    state: _common_pb2.OperationState
    create_time: _timestamp_pb2.Timestamp
    update_time: _timestamp_pb2.Timestamp
    error: _status_pb2.Status

    def __init__(self, state: _Optional[_Union[_common_pb2.OperationState, str]]=..., create_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]]=..., update_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]]=..., error: _Optional[_Union[_status_pb2.Status, _Mapping]]=...) -> None:
        ...

class GetDatasetRequest(_message.Message):
    __slots__ = ('name',)
    NAME_FIELD_NUMBER: _ClassVar[int]
    name: str

    def __init__(self, name: _Optional[str]=...) -> None:
        ...

class ListDatasetsRequest(_message.Message):
    __slots__ = ('parent', 'page_size', 'page_token')
    PARENT_FIELD_NUMBER: _ClassVar[int]
    PAGE_SIZE_FIELD_NUMBER: _ClassVar[int]
    PAGE_TOKEN_FIELD_NUMBER: _ClassVar[int]
    parent: str
    page_size: int
    page_token: str

    def __init__(self, parent: _Optional[str]=..., page_size: _Optional[int]=..., page_token: _Optional[str]=...) -> None:
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
    __slots__ = ('parent', 'dataset')
    PARENT_FIELD_NUMBER: _ClassVar[int]
    DATASET_FIELD_NUMBER: _ClassVar[int]
    parent: str
    dataset: Dataset

    def __init__(self, parent: _Optional[str]=..., dataset: _Optional[_Union[Dataset, _Mapping]]=...) -> None:
        ...

class CreateDatasetMetadata(_message.Message):
    __slots__ = ('state', 'create_time', 'update_time', 'error')
    STATE_FIELD_NUMBER: _ClassVar[int]
    CREATE_TIME_FIELD_NUMBER: _ClassVar[int]
    UPDATE_TIME_FIELD_NUMBER: _ClassVar[int]
    ERROR_FIELD_NUMBER: _ClassVar[int]
    state: _common_pb2.OperationState
    create_time: _timestamp_pb2.Timestamp
    update_time: _timestamp_pb2.Timestamp
    error: _status_pb2.Status

    def __init__(self, state: _Optional[_Union[_common_pb2.OperationState, str]]=..., create_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]]=..., update_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]]=..., error: _Optional[_Union[_status_pb2.Status, _Mapping]]=...) -> None:
        ...

class ListExamplesRequest(_message.Message):
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

class ListExamplesResponse(_message.Message):
    __slots__ = ('examples', 'next_page_token')
    EXAMPLES_FIELD_NUMBER: _ClassVar[int]
    NEXT_PAGE_TOKEN_FIELD_NUMBER: _ClassVar[int]
    examples: _containers.RepeatedCompositeFieldContainer[Example]
    next_page_token: str

    def __init__(self, examples: _Optional[_Iterable[_Union[Example, _Mapping]]]=..., next_page_token: _Optional[str]=...) -> None:
        ...

class Example(_message.Message):
    __slots__ = ('name', 'source_text', 'target_text', 'usage')
    NAME_FIELD_NUMBER: _ClassVar[int]
    SOURCE_TEXT_FIELD_NUMBER: _ClassVar[int]
    TARGET_TEXT_FIELD_NUMBER: _ClassVar[int]
    USAGE_FIELD_NUMBER: _ClassVar[int]
    name: str
    source_text: str
    target_text: str
    usage: str

    def __init__(self, name: _Optional[str]=..., source_text: _Optional[str]=..., target_text: _Optional[str]=..., usage: _Optional[str]=...) -> None:
        ...

class BatchTransferResourcesResponse(_message.Message):
    __slots__ = ('responses',)

    class TransferResourceResponse(_message.Message):
        __slots__ = ('source', 'target', 'error')
        SOURCE_FIELD_NUMBER: _ClassVar[int]
        TARGET_FIELD_NUMBER: _ClassVar[int]
        ERROR_FIELD_NUMBER: _ClassVar[int]
        source: str
        target: str
        error: _status_pb2.Status

        def __init__(self, source: _Optional[str]=..., target: _Optional[str]=..., error: _Optional[_Union[_status_pb2.Status, _Mapping]]=...) -> None:
            ...
    RESPONSES_FIELD_NUMBER: _ClassVar[int]
    responses: _containers.RepeatedCompositeFieldContainer[BatchTransferResourcesResponse.TransferResourceResponse]

    def __init__(self, responses: _Optional[_Iterable[_Union[BatchTransferResourcesResponse.TransferResourceResponse, _Mapping]]]=...) -> None:
        ...

class Dataset(_message.Message):
    __slots__ = ('name', 'display_name', 'source_language_code', 'target_language_code', 'example_count', 'train_example_count', 'validate_example_count', 'test_example_count', 'create_time', 'update_time')
    NAME_FIELD_NUMBER: _ClassVar[int]
    DISPLAY_NAME_FIELD_NUMBER: _ClassVar[int]
    SOURCE_LANGUAGE_CODE_FIELD_NUMBER: _ClassVar[int]
    TARGET_LANGUAGE_CODE_FIELD_NUMBER: _ClassVar[int]
    EXAMPLE_COUNT_FIELD_NUMBER: _ClassVar[int]
    TRAIN_EXAMPLE_COUNT_FIELD_NUMBER: _ClassVar[int]
    VALIDATE_EXAMPLE_COUNT_FIELD_NUMBER: _ClassVar[int]
    TEST_EXAMPLE_COUNT_FIELD_NUMBER: _ClassVar[int]
    CREATE_TIME_FIELD_NUMBER: _ClassVar[int]
    UPDATE_TIME_FIELD_NUMBER: _ClassVar[int]
    name: str
    display_name: str
    source_language_code: str
    target_language_code: str
    example_count: int
    train_example_count: int
    validate_example_count: int
    test_example_count: int
    create_time: _timestamp_pb2.Timestamp
    update_time: _timestamp_pb2.Timestamp

    def __init__(self, name: _Optional[str]=..., display_name: _Optional[str]=..., source_language_code: _Optional[str]=..., target_language_code: _Optional[str]=..., example_count: _Optional[int]=..., train_example_count: _Optional[int]=..., validate_example_count: _Optional[int]=..., test_example_count: _Optional[int]=..., create_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]]=..., update_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]]=...) -> None:
        ...

class CreateModelRequest(_message.Message):
    __slots__ = ('parent', 'model')
    PARENT_FIELD_NUMBER: _ClassVar[int]
    MODEL_FIELD_NUMBER: _ClassVar[int]
    parent: str
    model: Model

    def __init__(self, parent: _Optional[str]=..., model: _Optional[_Union[Model, _Mapping]]=...) -> None:
        ...

class CreateModelMetadata(_message.Message):
    __slots__ = ('state', 'create_time', 'update_time', 'error')
    STATE_FIELD_NUMBER: _ClassVar[int]
    CREATE_TIME_FIELD_NUMBER: _ClassVar[int]
    UPDATE_TIME_FIELD_NUMBER: _ClassVar[int]
    ERROR_FIELD_NUMBER: _ClassVar[int]
    state: _common_pb2.OperationState
    create_time: _timestamp_pb2.Timestamp
    update_time: _timestamp_pb2.Timestamp
    error: _status_pb2.Status

    def __init__(self, state: _Optional[_Union[_common_pb2.OperationState, str]]=..., create_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]]=..., update_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]]=..., error: _Optional[_Union[_status_pb2.Status, _Mapping]]=...) -> None:
        ...

class ListModelsRequest(_message.Message):
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

class ListModelsResponse(_message.Message):
    __slots__ = ('models', 'next_page_token')
    MODELS_FIELD_NUMBER: _ClassVar[int]
    NEXT_PAGE_TOKEN_FIELD_NUMBER: _ClassVar[int]
    models: _containers.RepeatedCompositeFieldContainer[Model]
    next_page_token: str

    def __init__(self, models: _Optional[_Iterable[_Union[Model, _Mapping]]]=..., next_page_token: _Optional[str]=...) -> None:
        ...

class GetModelRequest(_message.Message):
    __slots__ = ('name',)
    NAME_FIELD_NUMBER: _ClassVar[int]
    name: str

    def __init__(self, name: _Optional[str]=...) -> None:
        ...

class DeleteModelRequest(_message.Message):
    __slots__ = ('name',)
    NAME_FIELD_NUMBER: _ClassVar[int]
    name: str

    def __init__(self, name: _Optional[str]=...) -> None:
        ...

class DeleteModelMetadata(_message.Message):
    __slots__ = ('state', 'create_time', 'update_time', 'error')
    STATE_FIELD_NUMBER: _ClassVar[int]
    CREATE_TIME_FIELD_NUMBER: _ClassVar[int]
    UPDATE_TIME_FIELD_NUMBER: _ClassVar[int]
    ERROR_FIELD_NUMBER: _ClassVar[int]
    state: _common_pb2.OperationState
    create_time: _timestamp_pb2.Timestamp
    update_time: _timestamp_pb2.Timestamp
    error: _status_pb2.Status

    def __init__(self, state: _Optional[_Union[_common_pb2.OperationState, str]]=..., create_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]]=..., update_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]]=..., error: _Optional[_Union[_status_pb2.Status, _Mapping]]=...) -> None:
        ...

class Model(_message.Message):
    __slots__ = ('name', 'display_name', 'dataset', 'source_language_code', 'target_language_code', 'train_example_count', 'validate_example_count', 'test_example_count', 'create_time', 'update_time')
    NAME_FIELD_NUMBER: _ClassVar[int]
    DISPLAY_NAME_FIELD_NUMBER: _ClassVar[int]
    DATASET_FIELD_NUMBER: _ClassVar[int]
    SOURCE_LANGUAGE_CODE_FIELD_NUMBER: _ClassVar[int]
    TARGET_LANGUAGE_CODE_FIELD_NUMBER: _ClassVar[int]
    TRAIN_EXAMPLE_COUNT_FIELD_NUMBER: _ClassVar[int]
    VALIDATE_EXAMPLE_COUNT_FIELD_NUMBER: _ClassVar[int]
    TEST_EXAMPLE_COUNT_FIELD_NUMBER: _ClassVar[int]
    CREATE_TIME_FIELD_NUMBER: _ClassVar[int]
    UPDATE_TIME_FIELD_NUMBER: _ClassVar[int]
    name: str
    display_name: str
    dataset: str
    source_language_code: str
    target_language_code: str
    train_example_count: int
    validate_example_count: int
    test_example_count: int
    create_time: _timestamp_pb2.Timestamp
    update_time: _timestamp_pb2.Timestamp

    def __init__(self, name: _Optional[str]=..., display_name: _Optional[str]=..., dataset: _Optional[str]=..., source_language_code: _Optional[str]=..., target_language_code: _Optional[str]=..., train_example_count: _Optional[int]=..., validate_example_count: _Optional[int]=..., test_example_count: _Optional[int]=..., create_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]]=..., update_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]]=...) -> None:
        ...