from google.cloud.automl.v1 import io_pb2 as _io_pb2
from google.protobuf import timestamp_pb2 as _timestamp_pb2
from google.rpc import status_pb2 as _status_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union
DESCRIPTOR: _descriptor.FileDescriptor

class OperationMetadata(_message.Message):
    __slots__ = ('delete_details', 'deploy_model_details', 'undeploy_model_details', 'create_model_details', 'create_dataset_details', 'import_data_details', 'batch_predict_details', 'export_data_details', 'export_model_details', 'progress_percent', 'partial_failures', 'create_time', 'update_time')
    DELETE_DETAILS_FIELD_NUMBER: _ClassVar[int]
    DEPLOY_MODEL_DETAILS_FIELD_NUMBER: _ClassVar[int]
    UNDEPLOY_MODEL_DETAILS_FIELD_NUMBER: _ClassVar[int]
    CREATE_MODEL_DETAILS_FIELD_NUMBER: _ClassVar[int]
    CREATE_DATASET_DETAILS_FIELD_NUMBER: _ClassVar[int]
    IMPORT_DATA_DETAILS_FIELD_NUMBER: _ClassVar[int]
    BATCH_PREDICT_DETAILS_FIELD_NUMBER: _ClassVar[int]
    EXPORT_DATA_DETAILS_FIELD_NUMBER: _ClassVar[int]
    EXPORT_MODEL_DETAILS_FIELD_NUMBER: _ClassVar[int]
    PROGRESS_PERCENT_FIELD_NUMBER: _ClassVar[int]
    PARTIAL_FAILURES_FIELD_NUMBER: _ClassVar[int]
    CREATE_TIME_FIELD_NUMBER: _ClassVar[int]
    UPDATE_TIME_FIELD_NUMBER: _ClassVar[int]
    delete_details: DeleteOperationMetadata
    deploy_model_details: DeployModelOperationMetadata
    undeploy_model_details: UndeployModelOperationMetadata
    create_model_details: CreateModelOperationMetadata
    create_dataset_details: CreateDatasetOperationMetadata
    import_data_details: ImportDataOperationMetadata
    batch_predict_details: BatchPredictOperationMetadata
    export_data_details: ExportDataOperationMetadata
    export_model_details: ExportModelOperationMetadata
    progress_percent: int
    partial_failures: _containers.RepeatedCompositeFieldContainer[_status_pb2.Status]
    create_time: _timestamp_pb2.Timestamp
    update_time: _timestamp_pb2.Timestamp

    def __init__(self, delete_details: _Optional[_Union[DeleteOperationMetadata, _Mapping]]=..., deploy_model_details: _Optional[_Union[DeployModelOperationMetadata, _Mapping]]=..., undeploy_model_details: _Optional[_Union[UndeployModelOperationMetadata, _Mapping]]=..., create_model_details: _Optional[_Union[CreateModelOperationMetadata, _Mapping]]=..., create_dataset_details: _Optional[_Union[CreateDatasetOperationMetadata, _Mapping]]=..., import_data_details: _Optional[_Union[ImportDataOperationMetadata, _Mapping]]=..., batch_predict_details: _Optional[_Union[BatchPredictOperationMetadata, _Mapping]]=..., export_data_details: _Optional[_Union[ExportDataOperationMetadata, _Mapping]]=..., export_model_details: _Optional[_Union[ExportModelOperationMetadata, _Mapping]]=..., progress_percent: _Optional[int]=..., partial_failures: _Optional[_Iterable[_Union[_status_pb2.Status, _Mapping]]]=..., create_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]]=..., update_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]]=...) -> None:
        ...

class DeleteOperationMetadata(_message.Message):
    __slots__ = ()

    def __init__(self) -> None:
        ...

class DeployModelOperationMetadata(_message.Message):
    __slots__ = ()

    def __init__(self) -> None:
        ...

class UndeployModelOperationMetadata(_message.Message):
    __slots__ = ()

    def __init__(self) -> None:
        ...

class CreateDatasetOperationMetadata(_message.Message):
    __slots__ = ()

    def __init__(self) -> None:
        ...

class CreateModelOperationMetadata(_message.Message):
    __slots__ = ()

    def __init__(self) -> None:
        ...

class ImportDataOperationMetadata(_message.Message):
    __slots__ = ()

    def __init__(self) -> None:
        ...

class ExportDataOperationMetadata(_message.Message):
    __slots__ = ('output_info',)

    class ExportDataOutputInfo(_message.Message):
        __slots__ = ('gcs_output_directory',)
        GCS_OUTPUT_DIRECTORY_FIELD_NUMBER: _ClassVar[int]
        gcs_output_directory: str

        def __init__(self, gcs_output_directory: _Optional[str]=...) -> None:
            ...
    OUTPUT_INFO_FIELD_NUMBER: _ClassVar[int]
    output_info: ExportDataOperationMetadata.ExportDataOutputInfo

    def __init__(self, output_info: _Optional[_Union[ExportDataOperationMetadata.ExportDataOutputInfo, _Mapping]]=...) -> None:
        ...

class BatchPredictOperationMetadata(_message.Message):
    __slots__ = ('input_config', 'output_info')

    class BatchPredictOutputInfo(_message.Message):
        __slots__ = ('gcs_output_directory',)
        GCS_OUTPUT_DIRECTORY_FIELD_NUMBER: _ClassVar[int]
        gcs_output_directory: str

        def __init__(self, gcs_output_directory: _Optional[str]=...) -> None:
            ...
    INPUT_CONFIG_FIELD_NUMBER: _ClassVar[int]
    OUTPUT_INFO_FIELD_NUMBER: _ClassVar[int]
    input_config: _io_pb2.BatchPredictInputConfig
    output_info: BatchPredictOperationMetadata.BatchPredictOutputInfo

    def __init__(self, input_config: _Optional[_Union[_io_pb2.BatchPredictInputConfig, _Mapping]]=..., output_info: _Optional[_Union[BatchPredictOperationMetadata.BatchPredictOutputInfo, _Mapping]]=...) -> None:
        ...

class ExportModelOperationMetadata(_message.Message):
    __slots__ = ('output_info',)

    class ExportModelOutputInfo(_message.Message):
        __slots__ = ('gcs_output_directory',)
        GCS_OUTPUT_DIRECTORY_FIELD_NUMBER: _ClassVar[int]
        gcs_output_directory: str

        def __init__(self, gcs_output_directory: _Optional[str]=...) -> None:
            ...
    OUTPUT_INFO_FIELD_NUMBER: _ClassVar[int]
    output_info: ExportModelOperationMetadata.ExportModelOutputInfo

    def __init__(self, output_info: _Optional[_Union[ExportModelOperationMetadata.ExportModelOutputInfo, _Mapping]]=...) -> None:
        ...