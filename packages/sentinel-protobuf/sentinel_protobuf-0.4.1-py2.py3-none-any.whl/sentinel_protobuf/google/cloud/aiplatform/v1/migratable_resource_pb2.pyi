from google.api import field_behavior_pb2 as _field_behavior_pb2
from google.api import resource_pb2 as _resource_pb2
from google.protobuf import timestamp_pb2 as _timestamp_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union
DESCRIPTOR: _descriptor.FileDescriptor

class MigratableResource(_message.Message):
    __slots__ = ('ml_engine_model_version', 'automl_model', 'automl_dataset', 'data_labeling_dataset', 'last_migrate_time', 'last_update_time')

    class MlEngineModelVersion(_message.Message):
        __slots__ = ('endpoint', 'version')
        ENDPOINT_FIELD_NUMBER: _ClassVar[int]
        VERSION_FIELD_NUMBER: _ClassVar[int]
        endpoint: str
        version: str

        def __init__(self, endpoint: _Optional[str]=..., version: _Optional[str]=...) -> None:
            ...

    class AutomlModel(_message.Message):
        __slots__ = ('model', 'model_display_name')
        MODEL_FIELD_NUMBER: _ClassVar[int]
        MODEL_DISPLAY_NAME_FIELD_NUMBER: _ClassVar[int]
        model: str
        model_display_name: str

        def __init__(self, model: _Optional[str]=..., model_display_name: _Optional[str]=...) -> None:
            ...

    class AutomlDataset(_message.Message):
        __slots__ = ('dataset', 'dataset_display_name')
        DATASET_FIELD_NUMBER: _ClassVar[int]
        DATASET_DISPLAY_NAME_FIELD_NUMBER: _ClassVar[int]
        dataset: str
        dataset_display_name: str

        def __init__(self, dataset: _Optional[str]=..., dataset_display_name: _Optional[str]=...) -> None:
            ...

    class DataLabelingDataset(_message.Message):
        __slots__ = ('dataset', 'dataset_display_name', 'data_labeling_annotated_datasets')

        class DataLabelingAnnotatedDataset(_message.Message):
            __slots__ = ('annotated_dataset', 'annotated_dataset_display_name')
            ANNOTATED_DATASET_FIELD_NUMBER: _ClassVar[int]
            ANNOTATED_DATASET_DISPLAY_NAME_FIELD_NUMBER: _ClassVar[int]
            annotated_dataset: str
            annotated_dataset_display_name: str

            def __init__(self, annotated_dataset: _Optional[str]=..., annotated_dataset_display_name: _Optional[str]=...) -> None:
                ...
        DATASET_FIELD_NUMBER: _ClassVar[int]
        DATASET_DISPLAY_NAME_FIELD_NUMBER: _ClassVar[int]
        DATA_LABELING_ANNOTATED_DATASETS_FIELD_NUMBER: _ClassVar[int]
        dataset: str
        dataset_display_name: str
        data_labeling_annotated_datasets: _containers.RepeatedCompositeFieldContainer[MigratableResource.DataLabelingDataset.DataLabelingAnnotatedDataset]

        def __init__(self, dataset: _Optional[str]=..., dataset_display_name: _Optional[str]=..., data_labeling_annotated_datasets: _Optional[_Iterable[_Union[MigratableResource.DataLabelingDataset.DataLabelingAnnotatedDataset, _Mapping]]]=...) -> None:
            ...
    ML_ENGINE_MODEL_VERSION_FIELD_NUMBER: _ClassVar[int]
    AUTOML_MODEL_FIELD_NUMBER: _ClassVar[int]
    AUTOML_DATASET_FIELD_NUMBER: _ClassVar[int]
    DATA_LABELING_DATASET_FIELD_NUMBER: _ClassVar[int]
    LAST_MIGRATE_TIME_FIELD_NUMBER: _ClassVar[int]
    LAST_UPDATE_TIME_FIELD_NUMBER: _ClassVar[int]
    ml_engine_model_version: MigratableResource.MlEngineModelVersion
    automl_model: MigratableResource.AutomlModel
    automl_dataset: MigratableResource.AutomlDataset
    data_labeling_dataset: MigratableResource.DataLabelingDataset
    last_migrate_time: _timestamp_pb2.Timestamp
    last_update_time: _timestamp_pb2.Timestamp

    def __init__(self, ml_engine_model_version: _Optional[_Union[MigratableResource.MlEngineModelVersion, _Mapping]]=..., automl_model: _Optional[_Union[MigratableResource.AutomlModel, _Mapping]]=..., automl_dataset: _Optional[_Union[MigratableResource.AutomlDataset, _Mapping]]=..., data_labeling_dataset: _Optional[_Union[MigratableResource.DataLabelingDataset, _Mapping]]=..., last_migrate_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]]=..., last_update_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]]=...) -> None:
        ...