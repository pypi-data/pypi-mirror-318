from google.api import field_behavior_pb2 as _field_behavior_pb2
from google.api import resource_pb2 as _resource_pb2
from google.cloud.aiplatform.v1beta1 import explanation_pb2 as _explanation_pb2
from google.cloud.aiplatform.v1beta1 import model_monitoring_spec_pb2 as _model_monitoring_spec_pb2
from google.protobuf import timestamp_pb2 as _timestamp_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class ModelMonitor(_message.Message):
    __slots__ = ("tabular_objective", "name", "display_name", "model_monitoring_target", "training_dataset", "notification_spec", "output_spec", "explanation_spec", "model_monitoring_schema", "create_time", "update_time", "satisfies_pzs", "satisfies_pzi")
    class ModelMonitoringTarget(_message.Message):
        __slots__ = ("vertex_model",)
        class VertexModelSource(_message.Message):
            __slots__ = ("model", "model_version_id")
            MODEL_FIELD_NUMBER: _ClassVar[int]
            MODEL_VERSION_ID_FIELD_NUMBER: _ClassVar[int]
            model: str
            model_version_id: str
            def __init__(self, model: _Optional[str] = ..., model_version_id: _Optional[str] = ...) -> None: ...
        VERTEX_MODEL_FIELD_NUMBER: _ClassVar[int]
        vertex_model: ModelMonitor.ModelMonitoringTarget.VertexModelSource
        def __init__(self, vertex_model: _Optional[_Union[ModelMonitor.ModelMonitoringTarget.VertexModelSource, _Mapping]] = ...) -> None: ...
    TABULAR_OBJECTIVE_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    DISPLAY_NAME_FIELD_NUMBER: _ClassVar[int]
    MODEL_MONITORING_TARGET_FIELD_NUMBER: _ClassVar[int]
    TRAINING_DATASET_FIELD_NUMBER: _ClassVar[int]
    NOTIFICATION_SPEC_FIELD_NUMBER: _ClassVar[int]
    OUTPUT_SPEC_FIELD_NUMBER: _ClassVar[int]
    EXPLANATION_SPEC_FIELD_NUMBER: _ClassVar[int]
    MODEL_MONITORING_SCHEMA_FIELD_NUMBER: _ClassVar[int]
    CREATE_TIME_FIELD_NUMBER: _ClassVar[int]
    UPDATE_TIME_FIELD_NUMBER: _ClassVar[int]
    SATISFIES_PZS_FIELD_NUMBER: _ClassVar[int]
    SATISFIES_PZI_FIELD_NUMBER: _ClassVar[int]
    tabular_objective: _model_monitoring_spec_pb2.ModelMonitoringObjectiveSpec.TabularObjective
    name: str
    display_name: str
    model_monitoring_target: ModelMonitor.ModelMonitoringTarget
    training_dataset: _model_monitoring_spec_pb2.ModelMonitoringInput
    notification_spec: _model_monitoring_spec_pb2.ModelMonitoringNotificationSpec
    output_spec: _model_monitoring_spec_pb2.ModelMonitoringOutputSpec
    explanation_spec: _explanation_pb2.ExplanationSpec
    model_monitoring_schema: ModelMonitoringSchema
    create_time: _timestamp_pb2.Timestamp
    update_time: _timestamp_pb2.Timestamp
    satisfies_pzs: bool
    satisfies_pzi: bool
    def __init__(self, tabular_objective: _Optional[_Union[_model_monitoring_spec_pb2.ModelMonitoringObjectiveSpec.TabularObjective, _Mapping]] = ..., name: _Optional[str] = ..., display_name: _Optional[str] = ..., model_monitoring_target: _Optional[_Union[ModelMonitor.ModelMonitoringTarget, _Mapping]] = ..., training_dataset: _Optional[_Union[_model_monitoring_spec_pb2.ModelMonitoringInput, _Mapping]] = ..., notification_spec: _Optional[_Union[_model_monitoring_spec_pb2.ModelMonitoringNotificationSpec, _Mapping]] = ..., output_spec: _Optional[_Union[_model_monitoring_spec_pb2.ModelMonitoringOutputSpec, _Mapping]] = ..., explanation_spec: _Optional[_Union[_explanation_pb2.ExplanationSpec, _Mapping]] = ..., model_monitoring_schema: _Optional[_Union[ModelMonitoringSchema, _Mapping]] = ..., create_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., update_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., satisfies_pzs: bool = ..., satisfies_pzi: bool = ...) -> None: ...

class ModelMonitoringSchema(_message.Message):
    __slots__ = ("feature_fields", "prediction_fields", "ground_truth_fields")
    class FieldSchema(_message.Message):
        __slots__ = ("name", "data_type", "repeated")
        NAME_FIELD_NUMBER: _ClassVar[int]
        DATA_TYPE_FIELD_NUMBER: _ClassVar[int]
        REPEATED_FIELD_NUMBER: _ClassVar[int]
        name: str
        data_type: str
        repeated: bool
        def __init__(self, name: _Optional[str] = ..., data_type: _Optional[str] = ..., repeated: bool = ...) -> None: ...
    FEATURE_FIELDS_FIELD_NUMBER: _ClassVar[int]
    PREDICTION_FIELDS_FIELD_NUMBER: _ClassVar[int]
    GROUND_TRUTH_FIELDS_FIELD_NUMBER: _ClassVar[int]
    feature_fields: _containers.RepeatedCompositeFieldContainer[ModelMonitoringSchema.FieldSchema]
    prediction_fields: _containers.RepeatedCompositeFieldContainer[ModelMonitoringSchema.FieldSchema]
    ground_truth_fields: _containers.RepeatedCompositeFieldContainer[ModelMonitoringSchema.FieldSchema]
    def __init__(self, feature_fields: _Optional[_Iterable[_Union[ModelMonitoringSchema.FieldSchema, _Mapping]]] = ..., prediction_fields: _Optional[_Iterable[_Union[ModelMonitoringSchema.FieldSchema, _Mapping]]] = ..., ground_truth_fields: _Optional[_Iterable[_Union[ModelMonitoringSchema.FieldSchema, _Mapping]]] = ...) -> None: ...
