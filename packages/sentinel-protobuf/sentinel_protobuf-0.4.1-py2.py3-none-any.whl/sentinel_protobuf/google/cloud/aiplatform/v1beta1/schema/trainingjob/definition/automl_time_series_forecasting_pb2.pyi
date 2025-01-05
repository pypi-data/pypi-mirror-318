from google.cloud.aiplatform.v1beta1.schema.trainingjob.definition import export_evaluated_data_items_config_pb2 as _export_evaluated_data_items_config_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union
DESCRIPTOR: _descriptor.FileDescriptor

class AutoMlForecasting(_message.Message):
    __slots__ = ('inputs', 'metadata')
    INPUTS_FIELD_NUMBER: _ClassVar[int]
    METADATA_FIELD_NUMBER: _ClassVar[int]
    inputs: AutoMlForecastingInputs
    metadata: AutoMlForecastingMetadata

    def __init__(self, inputs: _Optional[_Union[AutoMlForecastingInputs, _Mapping]]=..., metadata: _Optional[_Union[AutoMlForecastingMetadata, _Mapping]]=...) -> None:
        ...

class AutoMlForecastingInputs(_message.Message):
    __slots__ = ('target_column', 'time_series_identifier_column', 'time_column', 'transformations', 'optimization_objective', 'train_budget_milli_node_hours', 'weight_column', 'time_series_attribute_columns', 'unavailable_at_forecast_columns', 'available_at_forecast_columns', 'data_granularity', 'forecast_horizon', 'context_window', 'export_evaluated_data_items_config', 'quantiles', 'validation_options', 'additional_experiments')

    class Transformation(_message.Message):
        __slots__ = ('auto', 'numeric', 'categorical', 'timestamp', 'text')

        class AutoTransformation(_message.Message):
            __slots__ = ('column_name',)
            COLUMN_NAME_FIELD_NUMBER: _ClassVar[int]
            column_name: str

            def __init__(self, column_name: _Optional[str]=...) -> None:
                ...

        class NumericTransformation(_message.Message):
            __slots__ = ('column_name',)
            COLUMN_NAME_FIELD_NUMBER: _ClassVar[int]
            column_name: str

            def __init__(self, column_name: _Optional[str]=...) -> None:
                ...

        class CategoricalTransformation(_message.Message):
            __slots__ = ('column_name',)
            COLUMN_NAME_FIELD_NUMBER: _ClassVar[int]
            column_name: str

            def __init__(self, column_name: _Optional[str]=...) -> None:
                ...

        class TimestampTransformation(_message.Message):
            __slots__ = ('column_name', 'time_format')
            COLUMN_NAME_FIELD_NUMBER: _ClassVar[int]
            TIME_FORMAT_FIELD_NUMBER: _ClassVar[int]
            column_name: str
            time_format: str

            def __init__(self, column_name: _Optional[str]=..., time_format: _Optional[str]=...) -> None:
                ...

        class TextTransformation(_message.Message):
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
        auto: AutoMlForecastingInputs.Transformation.AutoTransformation
        numeric: AutoMlForecastingInputs.Transformation.NumericTransformation
        categorical: AutoMlForecastingInputs.Transformation.CategoricalTransformation
        timestamp: AutoMlForecastingInputs.Transformation.TimestampTransformation
        text: AutoMlForecastingInputs.Transformation.TextTransformation

        def __init__(self, auto: _Optional[_Union[AutoMlForecastingInputs.Transformation.AutoTransformation, _Mapping]]=..., numeric: _Optional[_Union[AutoMlForecastingInputs.Transformation.NumericTransformation, _Mapping]]=..., categorical: _Optional[_Union[AutoMlForecastingInputs.Transformation.CategoricalTransformation, _Mapping]]=..., timestamp: _Optional[_Union[AutoMlForecastingInputs.Transformation.TimestampTransformation, _Mapping]]=..., text: _Optional[_Union[AutoMlForecastingInputs.Transformation.TextTransformation, _Mapping]]=...) -> None:
            ...

    class Granularity(_message.Message):
        __slots__ = ('unit', 'quantity')
        UNIT_FIELD_NUMBER: _ClassVar[int]
        QUANTITY_FIELD_NUMBER: _ClassVar[int]
        unit: str
        quantity: int

        def __init__(self, unit: _Optional[str]=..., quantity: _Optional[int]=...) -> None:
            ...
    TARGET_COLUMN_FIELD_NUMBER: _ClassVar[int]
    TIME_SERIES_IDENTIFIER_COLUMN_FIELD_NUMBER: _ClassVar[int]
    TIME_COLUMN_FIELD_NUMBER: _ClassVar[int]
    TRANSFORMATIONS_FIELD_NUMBER: _ClassVar[int]
    OPTIMIZATION_OBJECTIVE_FIELD_NUMBER: _ClassVar[int]
    TRAIN_BUDGET_MILLI_NODE_HOURS_FIELD_NUMBER: _ClassVar[int]
    WEIGHT_COLUMN_FIELD_NUMBER: _ClassVar[int]
    TIME_SERIES_ATTRIBUTE_COLUMNS_FIELD_NUMBER: _ClassVar[int]
    UNAVAILABLE_AT_FORECAST_COLUMNS_FIELD_NUMBER: _ClassVar[int]
    AVAILABLE_AT_FORECAST_COLUMNS_FIELD_NUMBER: _ClassVar[int]
    DATA_GRANULARITY_FIELD_NUMBER: _ClassVar[int]
    FORECAST_HORIZON_FIELD_NUMBER: _ClassVar[int]
    CONTEXT_WINDOW_FIELD_NUMBER: _ClassVar[int]
    EXPORT_EVALUATED_DATA_ITEMS_CONFIG_FIELD_NUMBER: _ClassVar[int]
    QUANTILES_FIELD_NUMBER: _ClassVar[int]
    VALIDATION_OPTIONS_FIELD_NUMBER: _ClassVar[int]
    ADDITIONAL_EXPERIMENTS_FIELD_NUMBER: _ClassVar[int]
    target_column: str
    time_series_identifier_column: str
    time_column: str
    transformations: _containers.RepeatedCompositeFieldContainer[AutoMlForecastingInputs.Transformation]
    optimization_objective: str
    train_budget_milli_node_hours: int
    weight_column: str
    time_series_attribute_columns: _containers.RepeatedScalarFieldContainer[str]
    unavailable_at_forecast_columns: _containers.RepeatedScalarFieldContainer[str]
    available_at_forecast_columns: _containers.RepeatedScalarFieldContainer[str]
    data_granularity: AutoMlForecastingInputs.Granularity
    forecast_horizon: int
    context_window: int
    export_evaluated_data_items_config: _export_evaluated_data_items_config_pb2.ExportEvaluatedDataItemsConfig
    quantiles: _containers.RepeatedScalarFieldContainer[float]
    validation_options: str
    additional_experiments: _containers.RepeatedScalarFieldContainer[str]

    def __init__(self, target_column: _Optional[str]=..., time_series_identifier_column: _Optional[str]=..., time_column: _Optional[str]=..., transformations: _Optional[_Iterable[_Union[AutoMlForecastingInputs.Transformation, _Mapping]]]=..., optimization_objective: _Optional[str]=..., train_budget_milli_node_hours: _Optional[int]=..., weight_column: _Optional[str]=..., time_series_attribute_columns: _Optional[_Iterable[str]]=..., unavailable_at_forecast_columns: _Optional[_Iterable[str]]=..., available_at_forecast_columns: _Optional[_Iterable[str]]=..., data_granularity: _Optional[_Union[AutoMlForecastingInputs.Granularity, _Mapping]]=..., forecast_horizon: _Optional[int]=..., context_window: _Optional[int]=..., export_evaluated_data_items_config: _Optional[_Union[_export_evaluated_data_items_config_pb2.ExportEvaluatedDataItemsConfig, _Mapping]]=..., quantiles: _Optional[_Iterable[float]]=..., validation_options: _Optional[str]=..., additional_experiments: _Optional[_Iterable[str]]=...) -> None:
        ...

class AutoMlForecastingMetadata(_message.Message):
    __slots__ = ('train_cost_milli_node_hours',)
    TRAIN_COST_MILLI_NODE_HOURS_FIELD_NUMBER: _ClassVar[int]
    train_cost_milli_node_hours: int

    def __init__(self, train_cost_milli_node_hours: _Optional[int]=...) -> None:
        ...