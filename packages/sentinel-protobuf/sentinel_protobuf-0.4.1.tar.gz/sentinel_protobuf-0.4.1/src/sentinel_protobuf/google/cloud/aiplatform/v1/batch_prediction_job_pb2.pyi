from google.api import field_behavior_pb2 as _field_behavior_pb2
from google.api import resource_pb2 as _resource_pb2
from google.cloud.aiplatform.v1 import completion_stats_pb2 as _completion_stats_pb2
from google.cloud.aiplatform.v1 import encryption_spec_pb2 as _encryption_spec_pb2
from google.cloud.aiplatform.v1 import explanation_pb2 as _explanation_pb2
from google.cloud.aiplatform.v1 import io_pb2 as _io_pb2
from google.cloud.aiplatform.v1 import job_state_pb2 as _job_state_pb2
from google.cloud.aiplatform.v1 import machine_resources_pb2 as _machine_resources_pb2
from google.cloud.aiplatform.v1 import manual_batch_tuning_parameters_pb2 as _manual_batch_tuning_parameters_pb2
from google.cloud.aiplatform.v1 import unmanaged_container_model_pb2 as _unmanaged_container_model_pb2
from google.protobuf import struct_pb2 as _struct_pb2
from google.protobuf import timestamp_pb2 as _timestamp_pb2
from google.rpc import status_pb2 as _status_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class BatchPredictionJob(_message.Message):
    __slots__ = ("name", "display_name", "model", "model_version_id", "unmanaged_container_model", "input_config", "instance_config", "model_parameters", "output_config", "dedicated_resources", "service_account", "manual_batch_tuning_parameters", "generate_explanation", "explanation_spec", "output_info", "state", "error", "partial_failures", "resources_consumed", "completion_stats", "create_time", "start_time", "end_time", "update_time", "labels", "encryption_spec", "disable_container_logging", "satisfies_pzs", "satisfies_pzi")
    class InputConfig(_message.Message):
        __slots__ = ("gcs_source", "bigquery_source", "instances_format")
        GCS_SOURCE_FIELD_NUMBER: _ClassVar[int]
        BIGQUERY_SOURCE_FIELD_NUMBER: _ClassVar[int]
        INSTANCES_FORMAT_FIELD_NUMBER: _ClassVar[int]
        gcs_source: _io_pb2.GcsSource
        bigquery_source: _io_pb2.BigQuerySource
        instances_format: str
        def __init__(self, gcs_source: _Optional[_Union[_io_pb2.GcsSource, _Mapping]] = ..., bigquery_source: _Optional[_Union[_io_pb2.BigQuerySource, _Mapping]] = ..., instances_format: _Optional[str] = ...) -> None: ...
    class InstanceConfig(_message.Message):
        __slots__ = ("instance_type", "key_field", "included_fields", "excluded_fields")
        INSTANCE_TYPE_FIELD_NUMBER: _ClassVar[int]
        KEY_FIELD_FIELD_NUMBER: _ClassVar[int]
        INCLUDED_FIELDS_FIELD_NUMBER: _ClassVar[int]
        EXCLUDED_FIELDS_FIELD_NUMBER: _ClassVar[int]
        instance_type: str
        key_field: str
        included_fields: _containers.RepeatedScalarFieldContainer[str]
        excluded_fields: _containers.RepeatedScalarFieldContainer[str]
        def __init__(self, instance_type: _Optional[str] = ..., key_field: _Optional[str] = ..., included_fields: _Optional[_Iterable[str]] = ..., excluded_fields: _Optional[_Iterable[str]] = ...) -> None: ...
    class OutputConfig(_message.Message):
        __slots__ = ("gcs_destination", "bigquery_destination", "predictions_format")
        GCS_DESTINATION_FIELD_NUMBER: _ClassVar[int]
        BIGQUERY_DESTINATION_FIELD_NUMBER: _ClassVar[int]
        PREDICTIONS_FORMAT_FIELD_NUMBER: _ClassVar[int]
        gcs_destination: _io_pb2.GcsDestination
        bigquery_destination: _io_pb2.BigQueryDestination
        predictions_format: str
        def __init__(self, gcs_destination: _Optional[_Union[_io_pb2.GcsDestination, _Mapping]] = ..., bigquery_destination: _Optional[_Union[_io_pb2.BigQueryDestination, _Mapping]] = ..., predictions_format: _Optional[str] = ...) -> None: ...
    class OutputInfo(_message.Message):
        __slots__ = ("gcs_output_directory", "bigquery_output_dataset", "bigquery_output_table")
        GCS_OUTPUT_DIRECTORY_FIELD_NUMBER: _ClassVar[int]
        BIGQUERY_OUTPUT_DATASET_FIELD_NUMBER: _ClassVar[int]
        BIGQUERY_OUTPUT_TABLE_FIELD_NUMBER: _ClassVar[int]
        gcs_output_directory: str
        bigquery_output_dataset: str
        bigquery_output_table: str
        def __init__(self, gcs_output_directory: _Optional[str] = ..., bigquery_output_dataset: _Optional[str] = ..., bigquery_output_table: _Optional[str] = ...) -> None: ...
    class LabelsEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: str
        def __init__(self, key: _Optional[str] = ..., value: _Optional[str] = ...) -> None: ...
    NAME_FIELD_NUMBER: _ClassVar[int]
    DISPLAY_NAME_FIELD_NUMBER: _ClassVar[int]
    MODEL_FIELD_NUMBER: _ClassVar[int]
    MODEL_VERSION_ID_FIELD_NUMBER: _ClassVar[int]
    UNMANAGED_CONTAINER_MODEL_FIELD_NUMBER: _ClassVar[int]
    INPUT_CONFIG_FIELD_NUMBER: _ClassVar[int]
    INSTANCE_CONFIG_FIELD_NUMBER: _ClassVar[int]
    MODEL_PARAMETERS_FIELD_NUMBER: _ClassVar[int]
    OUTPUT_CONFIG_FIELD_NUMBER: _ClassVar[int]
    DEDICATED_RESOURCES_FIELD_NUMBER: _ClassVar[int]
    SERVICE_ACCOUNT_FIELD_NUMBER: _ClassVar[int]
    MANUAL_BATCH_TUNING_PARAMETERS_FIELD_NUMBER: _ClassVar[int]
    GENERATE_EXPLANATION_FIELD_NUMBER: _ClassVar[int]
    EXPLANATION_SPEC_FIELD_NUMBER: _ClassVar[int]
    OUTPUT_INFO_FIELD_NUMBER: _ClassVar[int]
    STATE_FIELD_NUMBER: _ClassVar[int]
    ERROR_FIELD_NUMBER: _ClassVar[int]
    PARTIAL_FAILURES_FIELD_NUMBER: _ClassVar[int]
    RESOURCES_CONSUMED_FIELD_NUMBER: _ClassVar[int]
    COMPLETION_STATS_FIELD_NUMBER: _ClassVar[int]
    CREATE_TIME_FIELD_NUMBER: _ClassVar[int]
    START_TIME_FIELD_NUMBER: _ClassVar[int]
    END_TIME_FIELD_NUMBER: _ClassVar[int]
    UPDATE_TIME_FIELD_NUMBER: _ClassVar[int]
    LABELS_FIELD_NUMBER: _ClassVar[int]
    ENCRYPTION_SPEC_FIELD_NUMBER: _ClassVar[int]
    DISABLE_CONTAINER_LOGGING_FIELD_NUMBER: _ClassVar[int]
    SATISFIES_PZS_FIELD_NUMBER: _ClassVar[int]
    SATISFIES_PZI_FIELD_NUMBER: _ClassVar[int]
    name: str
    display_name: str
    model: str
    model_version_id: str
    unmanaged_container_model: _unmanaged_container_model_pb2.UnmanagedContainerModel
    input_config: BatchPredictionJob.InputConfig
    instance_config: BatchPredictionJob.InstanceConfig
    model_parameters: _struct_pb2.Value
    output_config: BatchPredictionJob.OutputConfig
    dedicated_resources: _machine_resources_pb2.BatchDedicatedResources
    service_account: str
    manual_batch_tuning_parameters: _manual_batch_tuning_parameters_pb2.ManualBatchTuningParameters
    generate_explanation: bool
    explanation_spec: _explanation_pb2.ExplanationSpec
    output_info: BatchPredictionJob.OutputInfo
    state: _job_state_pb2.JobState
    error: _status_pb2.Status
    partial_failures: _containers.RepeatedCompositeFieldContainer[_status_pb2.Status]
    resources_consumed: _machine_resources_pb2.ResourcesConsumed
    completion_stats: _completion_stats_pb2.CompletionStats
    create_time: _timestamp_pb2.Timestamp
    start_time: _timestamp_pb2.Timestamp
    end_time: _timestamp_pb2.Timestamp
    update_time: _timestamp_pb2.Timestamp
    labels: _containers.ScalarMap[str, str]
    encryption_spec: _encryption_spec_pb2.EncryptionSpec
    disable_container_logging: bool
    satisfies_pzs: bool
    satisfies_pzi: bool
    def __init__(self, name: _Optional[str] = ..., display_name: _Optional[str] = ..., model: _Optional[str] = ..., model_version_id: _Optional[str] = ..., unmanaged_container_model: _Optional[_Union[_unmanaged_container_model_pb2.UnmanagedContainerModel, _Mapping]] = ..., input_config: _Optional[_Union[BatchPredictionJob.InputConfig, _Mapping]] = ..., instance_config: _Optional[_Union[BatchPredictionJob.InstanceConfig, _Mapping]] = ..., model_parameters: _Optional[_Union[_struct_pb2.Value, _Mapping]] = ..., output_config: _Optional[_Union[BatchPredictionJob.OutputConfig, _Mapping]] = ..., dedicated_resources: _Optional[_Union[_machine_resources_pb2.BatchDedicatedResources, _Mapping]] = ..., service_account: _Optional[str] = ..., manual_batch_tuning_parameters: _Optional[_Union[_manual_batch_tuning_parameters_pb2.ManualBatchTuningParameters, _Mapping]] = ..., generate_explanation: bool = ..., explanation_spec: _Optional[_Union[_explanation_pb2.ExplanationSpec, _Mapping]] = ..., output_info: _Optional[_Union[BatchPredictionJob.OutputInfo, _Mapping]] = ..., state: _Optional[_Union[_job_state_pb2.JobState, str]] = ..., error: _Optional[_Union[_status_pb2.Status, _Mapping]] = ..., partial_failures: _Optional[_Iterable[_Union[_status_pb2.Status, _Mapping]]] = ..., resources_consumed: _Optional[_Union[_machine_resources_pb2.ResourcesConsumed, _Mapping]] = ..., completion_stats: _Optional[_Union[_completion_stats_pb2.CompletionStats, _Mapping]] = ..., create_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., start_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., end_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., update_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., labels: _Optional[_Mapping[str, str]] = ..., encryption_spec: _Optional[_Union[_encryption_spec_pb2.EncryptionSpec, _Mapping]] = ..., disable_container_logging: bool = ..., satisfies_pzs: bool = ..., satisfies_pzi: bool = ...) -> None: ...
