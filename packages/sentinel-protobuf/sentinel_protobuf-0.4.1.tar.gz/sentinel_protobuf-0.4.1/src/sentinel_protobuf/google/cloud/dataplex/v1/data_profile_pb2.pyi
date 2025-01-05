from google.api import field_behavior_pb2 as _field_behavior_pb2
from google.cloud.dataplex.v1 import processing_pb2 as _processing_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union
DESCRIPTOR: _descriptor.FileDescriptor

class DataProfileSpec(_message.Message):
    __slots__ = ('sampling_percent', 'row_filter', 'post_scan_actions', 'include_fields', 'exclude_fields')

    class PostScanActions(_message.Message):
        __slots__ = ('bigquery_export',)

        class BigQueryExport(_message.Message):
            __slots__ = ('results_table',)
            RESULTS_TABLE_FIELD_NUMBER: _ClassVar[int]
            results_table: str

            def __init__(self, results_table: _Optional[str]=...) -> None:
                ...
        BIGQUERY_EXPORT_FIELD_NUMBER: _ClassVar[int]
        bigquery_export: DataProfileSpec.PostScanActions.BigQueryExport

        def __init__(self, bigquery_export: _Optional[_Union[DataProfileSpec.PostScanActions.BigQueryExport, _Mapping]]=...) -> None:
            ...

    class SelectedFields(_message.Message):
        __slots__ = ('field_names',)
        FIELD_NAMES_FIELD_NUMBER: _ClassVar[int]
        field_names: _containers.RepeatedScalarFieldContainer[str]

        def __init__(self, field_names: _Optional[_Iterable[str]]=...) -> None:
            ...
    SAMPLING_PERCENT_FIELD_NUMBER: _ClassVar[int]
    ROW_FILTER_FIELD_NUMBER: _ClassVar[int]
    POST_SCAN_ACTIONS_FIELD_NUMBER: _ClassVar[int]
    INCLUDE_FIELDS_FIELD_NUMBER: _ClassVar[int]
    EXCLUDE_FIELDS_FIELD_NUMBER: _ClassVar[int]
    sampling_percent: float
    row_filter: str
    post_scan_actions: DataProfileSpec.PostScanActions
    include_fields: DataProfileSpec.SelectedFields
    exclude_fields: DataProfileSpec.SelectedFields

    def __init__(self, sampling_percent: _Optional[float]=..., row_filter: _Optional[str]=..., post_scan_actions: _Optional[_Union[DataProfileSpec.PostScanActions, _Mapping]]=..., include_fields: _Optional[_Union[DataProfileSpec.SelectedFields, _Mapping]]=..., exclude_fields: _Optional[_Union[DataProfileSpec.SelectedFields, _Mapping]]=...) -> None:
        ...

class DataProfileResult(_message.Message):
    __slots__ = ('row_count', 'profile', 'scanned_data', 'post_scan_actions_result')

    class Profile(_message.Message):
        __slots__ = ('fields',)

        class Field(_message.Message):
            __slots__ = ('name', 'type', 'mode', 'profile')

            class ProfileInfo(_message.Message):
                __slots__ = ('null_ratio', 'distinct_ratio', 'top_n_values', 'string_profile', 'integer_profile', 'double_profile')

                class StringFieldInfo(_message.Message):
                    __slots__ = ('min_length', 'max_length', 'average_length')
                    MIN_LENGTH_FIELD_NUMBER: _ClassVar[int]
                    MAX_LENGTH_FIELD_NUMBER: _ClassVar[int]
                    AVERAGE_LENGTH_FIELD_NUMBER: _ClassVar[int]
                    min_length: int
                    max_length: int
                    average_length: float

                    def __init__(self, min_length: _Optional[int]=..., max_length: _Optional[int]=..., average_length: _Optional[float]=...) -> None:
                        ...

                class IntegerFieldInfo(_message.Message):
                    __slots__ = ('average', 'standard_deviation', 'min', 'quartiles', 'max')
                    AVERAGE_FIELD_NUMBER: _ClassVar[int]
                    STANDARD_DEVIATION_FIELD_NUMBER: _ClassVar[int]
                    MIN_FIELD_NUMBER: _ClassVar[int]
                    QUARTILES_FIELD_NUMBER: _ClassVar[int]
                    MAX_FIELD_NUMBER: _ClassVar[int]
                    average: float
                    standard_deviation: float
                    min: int
                    quartiles: _containers.RepeatedScalarFieldContainer[int]
                    max: int

                    def __init__(self, average: _Optional[float]=..., standard_deviation: _Optional[float]=..., min: _Optional[int]=..., quartiles: _Optional[_Iterable[int]]=..., max: _Optional[int]=...) -> None:
                        ...

                class DoubleFieldInfo(_message.Message):
                    __slots__ = ('average', 'standard_deviation', 'min', 'quartiles', 'max')
                    AVERAGE_FIELD_NUMBER: _ClassVar[int]
                    STANDARD_DEVIATION_FIELD_NUMBER: _ClassVar[int]
                    MIN_FIELD_NUMBER: _ClassVar[int]
                    QUARTILES_FIELD_NUMBER: _ClassVar[int]
                    MAX_FIELD_NUMBER: _ClassVar[int]
                    average: float
                    standard_deviation: float
                    min: float
                    quartiles: _containers.RepeatedScalarFieldContainer[float]
                    max: float

                    def __init__(self, average: _Optional[float]=..., standard_deviation: _Optional[float]=..., min: _Optional[float]=..., quartiles: _Optional[_Iterable[float]]=..., max: _Optional[float]=...) -> None:
                        ...

                class TopNValue(_message.Message):
                    __slots__ = ('value', 'count', 'ratio')
                    VALUE_FIELD_NUMBER: _ClassVar[int]
                    COUNT_FIELD_NUMBER: _ClassVar[int]
                    RATIO_FIELD_NUMBER: _ClassVar[int]
                    value: str
                    count: int
                    ratio: float

                    def __init__(self, value: _Optional[str]=..., count: _Optional[int]=..., ratio: _Optional[float]=...) -> None:
                        ...
                NULL_RATIO_FIELD_NUMBER: _ClassVar[int]
                DISTINCT_RATIO_FIELD_NUMBER: _ClassVar[int]
                TOP_N_VALUES_FIELD_NUMBER: _ClassVar[int]
                STRING_PROFILE_FIELD_NUMBER: _ClassVar[int]
                INTEGER_PROFILE_FIELD_NUMBER: _ClassVar[int]
                DOUBLE_PROFILE_FIELD_NUMBER: _ClassVar[int]
                null_ratio: float
                distinct_ratio: float
                top_n_values: _containers.RepeatedCompositeFieldContainer[DataProfileResult.Profile.Field.ProfileInfo.TopNValue]
                string_profile: DataProfileResult.Profile.Field.ProfileInfo.StringFieldInfo
                integer_profile: DataProfileResult.Profile.Field.ProfileInfo.IntegerFieldInfo
                double_profile: DataProfileResult.Profile.Field.ProfileInfo.DoubleFieldInfo

                def __init__(self, null_ratio: _Optional[float]=..., distinct_ratio: _Optional[float]=..., top_n_values: _Optional[_Iterable[_Union[DataProfileResult.Profile.Field.ProfileInfo.TopNValue, _Mapping]]]=..., string_profile: _Optional[_Union[DataProfileResult.Profile.Field.ProfileInfo.StringFieldInfo, _Mapping]]=..., integer_profile: _Optional[_Union[DataProfileResult.Profile.Field.ProfileInfo.IntegerFieldInfo, _Mapping]]=..., double_profile: _Optional[_Union[DataProfileResult.Profile.Field.ProfileInfo.DoubleFieldInfo, _Mapping]]=...) -> None:
                    ...
            NAME_FIELD_NUMBER: _ClassVar[int]
            TYPE_FIELD_NUMBER: _ClassVar[int]
            MODE_FIELD_NUMBER: _ClassVar[int]
            PROFILE_FIELD_NUMBER: _ClassVar[int]
            name: str
            type: str
            mode: str
            profile: DataProfileResult.Profile.Field.ProfileInfo

            def __init__(self, name: _Optional[str]=..., type: _Optional[str]=..., mode: _Optional[str]=..., profile: _Optional[_Union[DataProfileResult.Profile.Field.ProfileInfo, _Mapping]]=...) -> None:
                ...
        FIELDS_FIELD_NUMBER: _ClassVar[int]
        fields: _containers.RepeatedCompositeFieldContainer[DataProfileResult.Profile.Field]

        def __init__(self, fields: _Optional[_Iterable[_Union[DataProfileResult.Profile.Field, _Mapping]]]=...) -> None:
            ...

    class PostScanActionsResult(_message.Message):
        __slots__ = ('bigquery_export_result',)

        class BigQueryExportResult(_message.Message):
            __slots__ = ('state', 'message')

            class State(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
                __slots__ = ()
                STATE_UNSPECIFIED: _ClassVar[DataProfileResult.PostScanActionsResult.BigQueryExportResult.State]
                SUCCEEDED: _ClassVar[DataProfileResult.PostScanActionsResult.BigQueryExportResult.State]
                FAILED: _ClassVar[DataProfileResult.PostScanActionsResult.BigQueryExportResult.State]
                SKIPPED: _ClassVar[DataProfileResult.PostScanActionsResult.BigQueryExportResult.State]
            STATE_UNSPECIFIED: DataProfileResult.PostScanActionsResult.BigQueryExportResult.State
            SUCCEEDED: DataProfileResult.PostScanActionsResult.BigQueryExportResult.State
            FAILED: DataProfileResult.PostScanActionsResult.BigQueryExportResult.State
            SKIPPED: DataProfileResult.PostScanActionsResult.BigQueryExportResult.State
            STATE_FIELD_NUMBER: _ClassVar[int]
            MESSAGE_FIELD_NUMBER: _ClassVar[int]
            state: DataProfileResult.PostScanActionsResult.BigQueryExportResult.State
            message: str

            def __init__(self, state: _Optional[_Union[DataProfileResult.PostScanActionsResult.BigQueryExportResult.State, str]]=..., message: _Optional[str]=...) -> None:
                ...
        BIGQUERY_EXPORT_RESULT_FIELD_NUMBER: _ClassVar[int]
        bigquery_export_result: DataProfileResult.PostScanActionsResult.BigQueryExportResult

        def __init__(self, bigquery_export_result: _Optional[_Union[DataProfileResult.PostScanActionsResult.BigQueryExportResult, _Mapping]]=...) -> None:
            ...
    ROW_COUNT_FIELD_NUMBER: _ClassVar[int]
    PROFILE_FIELD_NUMBER: _ClassVar[int]
    SCANNED_DATA_FIELD_NUMBER: _ClassVar[int]
    POST_SCAN_ACTIONS_RESULT_FIELD_NUMBER: _ClassVar[int]
    row_count: int
    profile: DataProfileResult.Profile
    scanned_data: _processing_pb2.ScannedData
    post_scan_actions_result: DataProfileResult.PostScanActionsResult

    def __init__(self, row_count: _Optional[int]=..., profile: _Optional[_Union[DataProfileResult.Profile, _Mapping]]=..., scanned_data: _Optional[_Union[_processing_pb2.ScannedData, _Mapping]]=..., post_scan_actions_result: _Optional[_Union[DataProfileResult.PostScanActionsResult, _Mapping]]=...) -> None:
        ...