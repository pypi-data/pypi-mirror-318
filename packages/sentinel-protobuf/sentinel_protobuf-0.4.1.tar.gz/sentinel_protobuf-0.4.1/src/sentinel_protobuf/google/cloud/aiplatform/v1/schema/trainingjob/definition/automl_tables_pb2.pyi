from google.cloud.aiplatform.v1.schema.trainingjob.definition import export_evaluated_data_items_config_pb2 as _export_evaluated_data_items_config_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union
DESCRIPTOR: _descriptor.FileDescriptor

class AutoMlTables(_message.Message):
    __slots__ = ('inputs', 'metadata')
    INPUTS_FIELD_NUMBER: _ClassVar[int]
    METADATA_FIELD_NUMBER: _ClassVar[int]
    inputs: AutoMlTablesInputs
    metadata: AutoMlTablesMetadata

    def __init__(self, inputs: _Optional[_Union[AutoMlTablesInputs, _Mapping]]=..., metadata: _Optional[_Union[AutoMlTablesMetadata, _Mapping]]=...) -> None:
        ...

class AutoMlTablesInputs(_message.Message):
    __slots__ = ('optimization_objective_recall_value', 'optimization_objective_precision_value', 'prediction_type', 'target_column', 'transformations', 'optimization_objective', 'train_budget_milli_node_hours', 'disable_early_stopping', 'weight_column_name', 'export_evaluated_data_items_config', 'additional_experiments')

    class Transformation(_message.Message):
        __slots__ = ('auto', 'numeric', 'categorical', 'timestamp', 'text', 'repeated_numeric', 'repeated_categorical', 'repeated_text')

        class AutoTransformation(_message.Message):
            __slots__ = ('column_name',)
            COLUMN_NAME_FIELD_NUMBER: _ClassVar[int]
            column_name: str

            def __init__(self, column_name: _Optional[str]=...) -> None:
                ...

        class NumericTransformation(_message.Message):
            __slots__ = ('column_name', 'invalid_values_allowed')
            COLUMN_NAME_FIELD_NUMBER: _ClassVar[int]
            INVALID_VALUES_ALLOWED_FIELD_NUMBER: _ClassVar[int]
            column_name: str
            invalid_values_allowed: bool

            def __init__(self, column_name: _Optional[str]=..., invalid_values_allowed: bool=...) -> None:
                ...

        class CategoricalTransformation(_message.Message):
            __slots__ = ('column_name',)
            COLUMN_NAME_FIELD_NUMBER: _ClassVar[int]
            column_name: str

            def __init__(self, column_name: _Optional[str]=...) -> None:
                ...

        class TimestampTransformation(_message.Message):
            __slots__ = ('column_name', 'time_format', 'invalid_values_allowed')
            COLUMN_NAME_FIELD_NUMBER: _ClassVar[int]
            TIME_FORMAT_FIELD_NUMBER: _ClassVar[int]
            INVALID_VALUES_ALLOWED_FIELD_NUMBER: _ClassVar[int]
            column_name: str
            time_format: str
            invalid_values_allowed: bool

            def __init__(self, column_name: _Optional[str]=..., time_format: _Optional[str]=..., invalid_values_allowed: bool=...) -> None:
                ...

        class TextTransformation(_message.Message):
            __slots__ = ('column_name',)
            COLUMN_NAME_FIELD_NUMBER: _ClassVar[int]
            column_name: str

            def __init__(self, column_name: _Optional[str]=...) -> None:
                ...

        class NumericArrayTransformation(_message.Message):
            __slots__ = ('column_name', 'invalid_values_allowed')
            COLUMN_NAME_FIELD_NUMBER: _ClassVar[int]
            INVALID_VALUES_ALLOWED_FIELD_NUMBER: _ClassVar[int]
            column_name: str
            invalid_values_allowed: bool

            def __init__(self, column_name: _Optional[str]=..., invalid_values_allowed: bool=...) -> None:
                ...

        class CategoricalArrayTransformation(_message.Message):
            __slots__ = ('column_name',)
            COLUMN_NAME_FIELD_NUMBER: _ClassVar[int]
            column_name: str

            def __init__(self, column_name: _Optional[str]=...) -> None:
                ...

        class TextArrayTransformation(_message.Message):
            __slots__ = ('column_name',)
            COLUMN_NAME_FIELD_NUMBER: _ClassVar[int]
            column_name: str

            def __init__(self, column_name: _Optional[str]=...) -> None:
                ...
        AUTO_FIELD_NUMBER: _ClassVar[int]
        NUMERIC_FIELD_NUMBER: _ClassVar[int]
        CATEGORICAL_FIELD_NUMBER: _ClassVar[int]
        TIMESTAMP_FIELD_NUMBER: _ClassVar[int]
        TEXT_FIELD_NUMBER: _ClassVar[int]
        REPEATED_NUMERIC_FIELD_NUMBER: _ClassVar[int]
        REPEATED_CATEGORICAL_FIELD_NUMBER: _ClassVar[int]
        REPEATED_TEXT_FIELD_NUMBER: _ClassVar[int]
        auto: AutoMlTablesInputs.Transformation.AutoTransformation
        numeric: AutoMlTablesInputs.Transformation.NumericTransformation
        categorical: AutoMlTablesInputs.Transformation.CategoricalTransformation
        timestamp: AutoMlTablesInputs.Transformation.TimestampTransformation
        text: AutoMlTablesInputs.Transformation.TextTransformation
        repeated_numeric: AutoMlTablesInputs.Transformation.NumericArrayTransformation
        repeated_categorical: AutoMlTablesInputs.Transformation.CategoricalArrayTransformation
        repeated_text: AutoMlTablesInputs.Transformation.TextArrayTransformation

        def __init__(self, auto: _Optional[_Union[AutoMlTablesInputs.Transformation.AutoTransformation, _Mapping]]=..., numeric: _Optional[_Union[AutoMlTablesInputs.Transformation.NumericTransformation, _Mapping]]=..., categorical: _Optional[_Union[AutoMlTablesInputs.Transformation.CategoricalTransformation, _Mapping]]=..., timestamp: _Optional[_Union[AutoMlTablesInputs.Transformation.TimestampTransformation, _Mapping]]=..., text: _Optional[_Union[AutoMlTablesInputs.Transformation.TextTransformation, _Mapping]]=..., repeated_numeric: _Optional[_Union[AutoMlTablesInputs.Transformation.NumericArrayTransformation, _Mapping]]=..., repeated_categorical: _Optional[_Union[AutoMlTablesInputs.Transformation.CategoricalArrayTransformation, _Mapping]]=..., repeated_text: _Optional[_Union[AutoMlTablesInputs.Transformation.TextArrayTransformation, _Mapping]]=...) -> None:
            ...
    OPTIMIZATION_OBJECTIVE_RECALL_VALUE_FIELD_NUMBER: _ClassVar[int]
    OPTIMIZATION_OBJECTIVE_PRECISION_VALUE_FIELD_NUMBER: _ClassVar[int]
    PREDICTION_TYPE_FIELD_NUMBER: _ClassVar[int]
    TARGET_COLUMN_FIELD_NUMBER: _ClassVar[int]
    TRANSFORMATIONS_FIELD_NUMBER: _ClassVar[int]
    OPTIMIZATION_OBJECTIVE_FIELD_NUMBER: _ClassVar[int]
    TRAIN_BUDGET_MILLI_NODE_HOURS_FIELD_NUMBER: _ClassVar[int]
    DISABLE_EARLY_STOPPING_FIELD_NUMBER: _ClassVar[int]
    WEIGHT_COLUMN_NAME_FIELD_NUMBER: _ClassVar[int]
    EXPORT_EVALUATED_DATA_ITEMS_CONFIG_FIELD_NUMBER: _ClassVar[int]
    ADDITIONAL_EXPERIMENTS_FIELD_NUMBER: _ClassVar[int]
    optimization_objective_recall_value: float
    optimization_objective_precision_value: float
    prediction_type: str
    target_column: str
    transformations: _containers.RepeatedCompositeFieldContainer[AutoMlTablesInputs.Transformation]
    optimization_objective: str
    train_budget_milli_node_hours: int
    disable_early_stopping: bool
    weight_column_name: str
    export_evaluated_data_items_config: _export_evaluated_data_items_config_pb2.ExportEvaluatedDataItemsConfig
    additional_experiments: _containers.RepeatedScalarFieldContainer[str]

    def __init__(self, optimization_objective_recall_value: _Optional[float]=..., optimization_objective_precision_value: _Optional[float]=..., prediction_type: _Optional[str]=..., target_column: _Optional[str]=..., transformations: _Optional[_Iterable[_Union[AutoMlTablesInputs.Transformation, _Mapping]]]=..., optimization_objective: _Optional[str]=..., train_budget_milli_node_hours: _Optional[int]=..., disable_early_stopping: bool=..., weight_column_name: _Optional[str]=..., export_evaluated_data_items_config: _Optional[_Union[_export_evaluated_data_items_config_pb2.ExportEvaluatedDataItemsConfig, _Mapping]]=..., additional_experiments: _Optional[_Iterable[str]]=...) -> None:
        ...

class AutoMlTablesMetadata(_message.Message):
    __slots__ = ('train_cost_milli_node_hours',)
    TRAIN_COST_MILLI_NODE_HOURS_FIELD_NUMBER: _ClassVar[int]
    train_cost_milli_node_hours: int

    def __init__(self, train_cost_milli_node_hours: _Optional[int]=...) -> None:
        ...