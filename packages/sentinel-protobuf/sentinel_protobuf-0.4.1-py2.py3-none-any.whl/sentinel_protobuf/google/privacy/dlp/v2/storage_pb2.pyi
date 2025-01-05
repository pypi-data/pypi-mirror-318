from google.api import resource_pb2 as _resource_pb2
from google.protobuf import timestamp_pb2 as _timestamp_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union
DESCRIPTOR: _descriptor.FileDescriptor

class Likelihood(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    LIKELIHOOD_UNSPECIFIED: _ClassVar[Likelihood]
    VERY_UNLIKELY: _ClassVar[Likelihood]
    UNLIKELY: _ClassVar[Likelihood]
    POSSIBLE: _ClassVar[Likelihood]
    LIKELY: _ClassVar[Likelihood]
    VERY_LIKELY: _ClassVar[Likelihood]

class FileType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    FILE_TYPE_UNSPECIFIED: _ClassVar[FileType]
    BINARY_FILE: _ClassVar[FileType]
    TEXT_FILE: _ClassVar[FileType]
    IMAGE: _ClassVar[FileType]
    WORD: _ClassVar[FileType]
    PDF: _ClassVar[FileType]
    AVRO: _ClassVar[FileType]
    CSV: _ClassVar[FileType]
    TSV: _ClassVar[FileType]
    POWERPOINT: _ClassVar[FileType]
    EXCEL: _ClassVar[FileType]
LIKELIHOOD_UNSPECIFIED: Likelihood
VERY_UNLIKELY: Likelihood
UNLIKELY: Likelihood
POSSIBLE: Likelihood
LIKELY: Likelihood
VERY_LIKELY: Likelihood
FILE_TYPE_UNSPECIFIED: FileType
BINARY_FILE: FileType
TEXT_FILE: FileType
IMAGE: FileType
WORD: FileType
PDF: FileType
AVRO: FileType
CSV: FileType
TSV: FileType
POWERPOINT: FileType
EXCEL: FileType

class InfoType(_message.Message):
    __slots__ = ('name', 'version', 'sensitivity_score')
    NAME_FIELD_NUMBER: _ClassVar[int]
    VERSION_FIELD_NUMBER: _ClassVar[int]
    SENSITIVITY_SCORE_FIELD_NUMBER: _ClassVar[int]
    name: str
    version: str
    sensitivity_score: SensitivityScore

    def __init__(self, name: _Optional[str]=..., version: _Optional[str]=..., sensitivity_score: _Optional[_Union[SensitivityScore, _Mapping]]=...) -> None:
        ...

class SensitivityScore(_message.Message):
    __slots__ = ('score',)

    class SensitivityScoreLevel(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        SENSITIVITY_SCORE_UNSPECIFIED: _ClassVar[SensitivityScore.SensitivityScoreLevel]
        SENSITIVITY_LOW: _ClassVar[SensitivityScore.SensitivityScoreLevel]
        SENSITIVITY_UNKNOWN: _ClassVar[SensitivityScore.SensitivityScoreLevel]
        SENSITIVITY_MODERATE: _ClassVar[SensitivityScore.SensitivityScoreLevel]
        SENSITIVITY_HIGH: _ClassVar[SensitivityScore.SensitivityScoreLevel]
    SENSITIVITY_SCORE_UNSPECIFIED: SensitivityScore.SensitivityScoreLevel
    SENSITIVITY_LOW: SensitivityScore.SensitivityScoreLevel
    SENSITIVITY_UNKNOWN: SensitivityScore.SensitivityScoreLevel
    SENSITIVITY_MODERATE: SensitivityScore.SensitivityScoreLevel
    SENSITIVITY_HIGH: SensitivityScore.SensitivityScoreLevel
    SCORE_FIELD_NUMBER: _ClassVar[int]
    score: SensitivityScore.SensitivityScoreLevel

    def __init__(self, score: _Optional[_Union[SensitivityScore.SensitivityScoreLevel, str]]=...) -> None:
        ...

class StoredType(_message.Message):
    __slots__ = ('name', 'create_time')
    NAME_FIELD_NUMBER: _ClassVar[int]
    CREATE_TIME_FIELD_NUMBER: _ClassVar[int]
    name: str
    create_time: _timestamp_pb2.Timestamp

    def __init__(self, name: _Optional[str]=..., create_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]]=...) -> None:
        ...

class CustomInfoType(_message.Message):
    __slots__ = ('info_type', 'likelihood', 'dictionary', 'regex', 'surrogate_type', 'stored_type', 'detection_rules', 'exclusion_type', 'sensitivity_score')

    class ExclusionType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        EXCLUSION_TYPE_UNSPECIFIED: _ClassVar[CustomInfoType.ExclusionType]
        EXCLUSION_TYPE_EXCLUDE: _ClassVar[CustomInfoType.ExclusionType]
    EXCLUSION_TYPE_UNSPECIFIED: CustomInfoType.ExclusionType
    EXCLUSION_TYPE_EXCLUDE: CustomInfoType.ExclusionType

    class Dictionary(_message.Message):
        __slots__ = ('word_list', 'cloud_storage_path')

        class WordList(_message.Message):
            __slots__ = ('words',)
            WORDS_FIELD_NUMBER: _ClassVar[int]
            words: _containers.RepeatedScalarFieldContainer[str]

            def __init__(self, words: _Optional[_Iterable[str]]=...) -> None:
                ...
        WORD_LIST_FIELD_NUMBER: _ClassVar[int]
        CLOUD_STORAGE_PATH_FIELD_NUMBER: _ClassVar[int]
        word_list: CustomInfoType.Dictionary.WordList
        cloud_storage_path: CloudStoragePath

        def __init__(self, word_list: _Optional[_Union[CustomInfoType.Dictionary.WordList, _Mapping]]=..., cloud_storage_path: _Optional[_Union[CloudStoragePath, _Mapping]]=...) -> None:
            ...

    class Regex(_message.Message):
        __slots__ = ('pattern', 'group_indexes')
        PATTERN_FIELD_NUMBER: _ClassVar[int]
        GROUP_INDEXES_FIELD_NUMBER: _ClassVar[int]
        pattern: str
        group_indexes: _containers.RepeatedScalarFieldContainer[int]

        def __init__(self, pattern: _Optional[str]=..., group_indexes: _Optional[_Iterable[int]]=...) -> None:
            ...

    class SurrogateType(_message.Message):
        __slots__ = ()

        def __init__(self) -> None:
            ...

    class DetectionRule(_message.Message):
        __slots__ = ('hotword_rule',)

        class Proximity(_message.Message):
            __slots__ = ('window_before', 'window_after')
            WINDOW_BEFORE_FIELD_NUMBER: _ClassVar[int]
            WINDOW_AFTER_FIELD_NUMBER: _ClassVar[int]
            window_before: int
            window_after: int

            def __init__(self, window_before: _Optional[int]=..., window_after: _Optional[int]=...) -> None:
                ...

        class LikelihoodAdjustment(_message.Message):
            __slots__ = ('fixed_likelihood', 'relative_likelihood')
            FIXED_LIKELIHOOD_FIELD_NUMBER: _ClassVar[int]
            RELATIVE_LIKELIHOOD_FIELD_NUMBER: _ClassVar[int]
            fixed_likelihood: Likelihood
            relative_likelihood: int

            def __init__(self, fixed_likelihood: _Optional[_Union[Likelihood, str]]=..., relative_likelihood: _Optional[int]=...) -> None:
                ...

        class HotwordRule(_message.Message):
            __slots__ = ('hotword_regex', 'proximity', 'likelihood_adjustment')
            HOTWORD_REGEX_FIELD_NUMBER: _ClassVar[int]
            PROXIMITY_FIELD_NUMBER: _ClassVar[int]
            LIKELIHOOD_ADJUSTMENT_FIELD_NUMBER: _ClassVar[int]
            hotword_regex: CustomInfoType.Regex
            proximity: CustomInfoType.DetectionRule.Proximity
            likelihood_adjustment: CustomInfoType.DetectionRule.LikelihoodAdjustment

            def __init__(self, hotword_regex: _Optional[_Union[CustomInfoType.Regex, _Mapping]]=..., proximity: _Optional[_Union[CustomInfoType.DetectionRule.Proximity, _Mapping]]=..., likelihood_adjustment: _Optional[_Union[CustomInfoType.DetectionRule.LikelihoodAdjustment, _Mapping]]=...) -> None:
                ...
        HOTWORD_RULE_FIELD_NUMBER: _ClassVar[int]
        hotword_rule: CustomInfoType.DetectionRule.HotwordRule

        def __init__(self, hotword_rule: _Optional[_Union[CustomInfoType.DetectionRule.HotwordRule, _Mapping]]=...) -> None:
            ...
    INFO_TYPE_FIELD_NUMBER: _ClassVar[int]
    LIKELIHOOD_FIELD_NUMBER: _ClassVar[int]
    DICTIONARY_FIELD_NUMBER: _ClassVar[int]
    REGEX_FIELD_NUMBER: _ClassVar[int]
    SURROGATE_TYPE_FIELD_NUMBER: _ClassVar[int]
    STORED_TYPE_FIELD_NUMBER: _ClassVar[int]
    DETECTION_RULES_FIELD_NUMBER: _ClassVar[int]
    EXCLUSION_TYPE_FIELD_NUMBER: _ClassVar[int]
    SENSITIVITY_SCORE_FIELD_NUMBER: _ClassVar[int]
    info_type: InfoType
    likelihood: Likelihood
    dictionary: CustomInfoType.Dictionary
    regex: CustomInfoType.Regex
    surrogate_type: CustomInfoType.SurrogateType
    stored_type: StoredType
    detection_rules: _containers.RepeatedCompositeFieldContainer[CustomInfoType.DetectionRule]
    exclusion_type: CustomInfoType.ExclusionType
    sensitivity_score: SensitivityScore

    def __init__(self, info_type: _Optional[_Union[InfoType, _Mapping]]=..., likelihood: _Optional[_Union[Likelihood, str]]=..., dictionary: _Optional[_Union[CustomInfoType.Dictionary, _Mapping]]=..., regex: _Optional[_Union[CustomInfoType.Regex, _Mapping]]=..., surrogate_type: _Optional[_Union[CustomInfoType.SurrogateType, _Mapping]]=..., stored_type: _Optional[_Union[StoredType, _Mapping]]=..., detection_rules: _Optional[_Iterable[_Union[CustomInfoType.DetectionRule, _Mapping]]]=..., exclusion_type: _Optional[_Union[CustomInfoType.ExclusionType, str]]=..., sensitivity_score: _Optional[_Union[SensitivityScore, _Mapping]]=...) -> None:
        ...

class FieldId(_message.Message):
    __slots__ = ('name',)
    NAME_FIELD_NUMBER: _ClassVar[int]
    name: str

    def __init__(self, name: _Optional[str]=...) -> None:
        ...

class PartitionId(_message.Message):
    __slots__ = ('project_id', 'namespace_id')
    PROJECT_ID_FIELD_NUMBER: _ClassVar[int]
    NAMESPACE_ID_FIELD_NUMBER: _ClassVar[int]
    project_id: str
    namespace_id: str

    def __init__(self, project_id: _Optional[str]=..., namespace_id: _Optional[str]=...) -> None:
        ...

class KindExpression(_message.Message):
    __slots__ = ('name',)
    NAME_FIELD_NUMBER: _ClassVar[int]
    name: str

    def __init__(self, name: _Optional[str]=...) -> None:
        ...

class DatastoreOptions(_message.Message):
    __slots__ = ('partition_id', 'kind')
    PARTITION_ID_FIELD_NUMBER: _ClassVar[int]
    KIND_FIELD_NUMBER: _ClassVar[int]
    partition_id: PartitionId
    kind: KindExpression

    def __init__(self, partition_id: _Optional[_Union[PartitionId, _Mapping]]=..., kind: _Optional[_Union[KindExpression, _Mapping]]=...) -> None:
        ...

class CloudStorageRegexFileSet(_message.Message):
    __slots__ = ('bucket_name', 'include_regex', 'exclude_regex')
    BUCKET_NAME_FIELD_NUMBER: _ClassVar[int]
    INCLUDE_REGEX_FIELD_NUMBER: _ClassVar[int]
    EXCLUDE_REGEX_FIELD_NUMBER: _ClassVar[int]
    bucket_name: str
    include_regex: _containers.RepeatedScalarFieldContainer[str]
    exclude_regex: _containers.RepeatedScalarFieldContainer[str]

    def __init__(self, bucket_name: _Optional[str]=..., include_regex: _Optional[_Iterable[str]]=..., exclude_regex: _Optional[_Iterable[str]]=...) -> None:
        ...

class CloudStorageOptions(_message.Message):
    __slots__ = ('file_set', 'bytes_limit_per_file', 'bytes_limit_per_file_percent', 'file_types', 'sample_method', 'files_limit_percent')

    class SampleMethod(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        SAMPLE_METHOD_UNSPECIFIED: _ClassVar[CloudStorageOptions.SampleMethod]
        TOP: _ClassVar[CloudStorageOptions.SampleMethod]
        RANDOM_START: _ClassVar[CloudStorageOptions.SampleMethod]
    SAMPLE_METHOD_UNSPECIFIED: CloudStorageOptions.SampleMethod
    TOP: CloudStorageOptions.SampleMethod
    RANDOM_START: CloudStorageOptions.SampleMethod

    class FileSet(_message.Message):
        __slots__ = ('url', 'regex_file_set')
        URL_FIELD_NUMBER: _ClassVar[int]
        REGEX_FILE_SET_FIELD_NUMBER: _ClassVar[int]
        url: str
        regex_file_set: CloudStorageRegexFileSet

        def __init__(self, url: _Optional[str]=..., regex_file_set: _Optional[_Union[CloudStorageRegexFileSet, _Mapping]]=...) -> None:
            ...
    FILE_SET_FIELD_NUMBER: _ClassVar[int]
    BYTES_LIMIT_PER_FILE_FIELD_NUMBER: _ClassVar[int]
    BYTES_LIMIT_PER_FILE_PERCENT_FIELD_NUMBER: _ClassVar[int]
    FILE_TYPES_FIELD_NUMBER: _ClassVar[int]
    SAMPLE_METHOD_FIELD_NUMBER: _ClassVar[int]
    FILES_LIMIT_PERCENT_FIELD_NUMBER: _ClassVar[int]
    file_set: CloudStorageOptions.FileSet
    bytes_limit_per_file: int
    bytes_limit_per_file_percent: int
    file_types: _containers.RepeatedScalarFieldContainer[FileType]
    sample_method: CloudStorageOptions.SampleMethod
    files_limit_percent: int

    def __init__(self, file_set: _Optional[_Union[CloudStorageOptions.FileSet, _Mapping]]=..., bytes_limit_per_file: _Optional[int]=..., bytes_limit_per_file_percent: _Optional[int]=..., file_types: _Optional[_Iterable[_Union[FileType, str]]]=..., sample_method: _Optional[_Union[CloudStorageOptions.SampleMethod, str]]=..., files_limit_percent: _Optional[int]=...) -> None:
        ...

class CloudStorageFileSet(_message.Message):
    __slots__ = ('url',)
    URL_FIELD_NUMBER: _ClassVar[int]
    url: str

    def __init__(self, url: _Optional[str]=...) -> None:
        ...

class CloudStoragePath(_message.Message):
    __slots__ = ('path',)
    PATH_FIELD_NUMBER: _ClassVar[int]
    path: str

    def __init__(self, path: _Optional[str]=...) -> None:
        ...

class BigQueryOptions(_message.Message):
    __slots__ = ('table_reference', 'identifying_fields', 'rows_limit', 'rows_limit_percent', 'sample_method', 'excluded_fields', 'included_fields')

    class SampleMethod(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        SAMPLE_METHOD_UNSPECIFIED: _ClassVar[BigQueryOptions.SampleMethod]
        TOP: _ClassVar[BigQueryOptions.SampleMethod]
        RANDOM_START: _ClassVar[BigQueryOptions.SampleMethod]
    SAMPLE_METHOD_UNSPECIFIED: BigQueryOptions.SampleMethod
    TOP: BigQueryOptions.SampleMethod
    RANDOM_START: BigQueryOptions.SampleMethod
    TABLE_REFERENCE_FIELD_NUMBER: _ClassVar[int]
    IDENTIFYING_FIELDS_FIELD_NUMBER: _ClassVar[int]
    ROWS_LIMIT_FIELD_NUMBER: _ClassVar[int]
    ROWS_LIMIT_PERCENT_FIELD_NUMBER: _ClassVar[int]
    SAMPLE_METHOD_FIELD_NUMBER: _ClassVar[int]
    EXCLUDED_FIELDS_FIELD_NUMBER: _ClassVar[int]
    INCLUDED_FIELDS_FIELD_NUMBER: _ClassVar[int]
    table_reference: BigQueryTable
    identifying_fields: _containers.RepeatedCompositeFieldContainer[FieldId]
    rows_limit: int
    rows_limit_percent: int
    sample_method: BigQueryOptions.SampleMethod
    excluded_fields: _containers.RepeatedCompositeFieldContainer[FieldId]
    included_fields: _containers.RepeatedCompositeFieldContainer[FieldId]

    def __init__(self, table_reference: _Optional[_Union[BigQueryTable, _Mapping]]=..., identifying_fields: _Optional[_Iterable[_Union[FieldId, _Mapping]]]=..., rows_limit: _Optional[int]=..., rows_limit_percent: _Optional[int]=..., sample_method: _Optional[_Union[BigQueryOptions.SampleMethod, str]]=..., excluded_fields: _Optional[_Iterable[_Union[FieldId, _Mapping]]]=..., included_fields: _Optional[_Iterable[_Union[FieldId, _Mapping]]]=...) -> None:
        ...

class StorageConfig(_message.Message):
    __slots__ = ('datastore_options', 'cloud_storage_options', 'big_query_options', 'hybrid_options', 'timespan_config')

    class TimespanConfig(_message.Message):
        __slots__ = ('start_time', 'end_time', 'timestamp_field', 'enable_auto_population_of_timespan_config')
        START_TIME_FIELD_NUMBER: _ClassVar[int]
        END_TIME_FIELD_NUMBER: _ClassVar[int]
        TIMESTAMP_FIELD_FIELD_NUMBER: _ClassVar[int]
        ENABLE_AUTO_POPULATION_OF_TIMESPAN_CONFIG_FIELD_NUMBER: _ClassVar[int]
        start_time: _timestamp_pb2.Timestamp
        end_time: _timestamp_pb2.Timestamp
        timestamp_field: FieldId
        enable_auto_population_of_timespan_config: bool

        def __init__(self, start_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]]=..., end_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]]=..., timestamp_field: _Optional[_Union[FieldId, _Mapping]]=..., enable_auto_population_of_timespan_config: bool=...) -> None:
            ...
    DATASTORE_OPTIONS_FIELD_NUMBER: _ClassVar[int]
    CLOUD_STORAGE_OPTIONS_FIELD_NUMBER: _ClassVar[int]
    BIG_QUERY_OPTIONS_FIELD_NUMBER: _ClassVar[int]
    HYBRID_OPTIONS_FIELD_NUMBER: _ClassVar[int]
    TIMESPAN_CONFIG_FIELD_NUMBER: _ClassVar[int]
    datastore_options: DatastoreOptions
    cloud_storage_options: CloudStorageOptions
    big_query_options: BigQueryOptions
    hybrid_options: HybridOptions
    timespan_config: StorageConfig.TimespanConfig

    def __init__(self, datastore_options: _Optional[_Union[DatastoreOptions, _Mapping]]=..., cloud_storage_options: _Optional[_Union[CloudStorageOptions, _Mapping]]=..., big_query_options: _Optional[_Union[BigQueryOptions, _Mapping]]=..., hybrid_options: _Optional[_Union[HybridOptions, _Mapping]]=..., timespan_config: _Optional[_Union[StorageConfig.TimespanConfig, _Mapping]]=...) -> None:
        ...

class HybridOptions(_message.Message):
    __slots__ = ('description', 'required_finding_label_keys', 'labels', 'table_options')

    class LabelsEntry(_message.Message):
        __slots__ = ('key', 'value')
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: str

        def __init__(self, key: _Optional[str]=..., value: _Optional[str]=...) -> None:
            ...
    DESCRIPTION_FIELD_NUMBER: _ClassVar[int]
    REQUIRED_FINDING_LABEL_KEYS_FIELD_NUMBER: _ClassVar[int]
    LABELS_FIELD_NUMBER: _ClassVar[int]
    TABLE_OPTIONS_FIELD_NUMBER: _ClassVar[int]
    description: str
    required_finding_label_keys: _containers.RepeatedScalarFieldContainer[str]
    labels: _containers.ScalarMap[str, str]
    table_options: TableOptions

    def __init__(self, description: _Optional[str]=..., required_finding_label_keys: _Optional[_Iterable[str]]=..., labels: _Optional[_Mapping[str, str]]=..., table_options: _Optional[_Union[TableOptions, _Mapping]]=...) -> None:
        ...

class BigQueryKey(_message.Message):
    __slots__ = ('table_reference', 'row_number')
    TABLE_REFERENCE_FIELD_NUMBER: _ClassVar[int]
    ROW_NUMBER_FIELD_NUMBER: _ClassVar[int]
    table_reference: BigQueryTable
    row_number: int

    def __init__(self, table_reference: _Optional[_Union[BigQueryTable, _Mapping]]=..., row_number: _Optional[int]=...) -> None:
        ...

class DatastoreKey(_message.Message):
    __slots__ = ('entity_key',)
    ENTITY_KEY_FIELD_NUMBER: _ClassVar[int]
    entity_key: Key

    def __init__(self, entity_key: _Optional[_Union[Key, _Mapping]]=...) -> None:
        ...

class Key(_message.Message):
    __slots__ = ('partition_id', 'path')

    class PathElement(_message.Message):
        __slots__ = ('kind', 'id', 'name')
        KIND_FIELD_NUMBER: _ClassVar[int]
        ID_FIELD_NUMBER: _ClassVar[int]
        NAME_FIELD_NUMBER: _ClassVar[int]
        kind: str
        id: int
        name: str

        def __init__(self, kind: _Optional[str]=..., id: _Optional[int]=..., name: _Optional[str]=...) -> None:
            ...
    PARTITION_ID_FIELD_NUMBER: _ClassVar[int]
    PATH_FIELD_NUMBER: _ClassVar[int]
    partition_id: PartitionId
    path: _containers.RepeatedCompositeFieldContainer[Key.PathElement]

    def __init__(self, partition_id: _Optional[_Union[PartitionId, _Mapping]]=..., path: _Optional[_Iterable[_Union[Key.PathElement, _Mapping]]]=...) -> None:
        ...

class RecordKey(_message.Message):
    __slots__ = ('datastore_key', 'big_query_key', 'id_values')
    DATASTORE_KEY_FIELD_NUMBER: _ClassVar[int]
    BIG_QUERY_KEY_FIELD_NUMBER: _ClassVar[int]
    ID_VALUES_FIELD_NUMBER: _ClassVar[int]
    datastore_key: DatastoreKey
    big_query_key: BigQueryKey
    id_values: _containers.RepeatedScalarFieldContainer[str]

    def __init__(self, datastore_key: _Optional[_Union[DatastoreKey, _Mapping]]=..., big_query_key: _Optional[_Union[BigQueryKey, _Mapping]]=..., id_values: _Optional[_Iterable[str]]=...) -> None:
        ...

class BigQueryTable(_message.Message):
    __slots__ = ('project_id', 'dataset_id', 'table_id')
    PROJECT_ID_FIELD_NUMBER: _ClassVar[int]
    DATASET_ID_FIELD_NUMBER: _ClassVar[int]
    TABLE_ID_FIELD_NUMBER: _ClassVar[int]
    project_id: str
    dataset_id: str
    table_id: str

    def __init__(self, project_id: _Optional[str]=..., dataset_id: _Optional[str]=..., table_id: _Optional[str]=...) -> None:
        ...

class TableReference(_message.Message):
    __slots__ = ('dataset_id', 'table_id')
    DATASET_ID_FIELD_NUMBER: _ClassVar[int]
    TABLE_ID_FIELD_NUMBER: _ClassVar[int]
    dataset_id: str
    table_id: str

    def __init__(self, dataset_id: _Optional[str]=..., table_id: _Optional[str]=...) -> None:
        ...

class BigQueryField(_message.Message):
    __slots__ = ('table', 'field')
    TABLE_FIELD_NUMBER: _ClassVar[int]
    FIELD_FIELD_NUMBER: _ClassVar[int]
    table: BigQueryTable
    field: FieldId

    def __init__(self, table: _Optional[_Union[BigQueryTable, _Mapping]]=..., field: _Optional[_Union[FieldId, _Mapping]]=...) -> None:
        ...

class EntityId(_message.Message):
    __slots__ = ('field',)
    FIELD_FIELD_NUMBER: _ClassVar[int]
    field: FieldId

    def __init__(self, field: _Optional[_Union[FieldId, _Mapping]]=...) -> None:
        ...

class TableOptions(_message.Message):
    __slots__ = ('identifying_fields',)
    IDENTIFYING_FIELDS_FIELD_NUMBER: _ClassVar[int]
    identifying_fields: _containers.RepeatedCompositeFieldContainer[FieldId]

    def __init__(self, identifying_fields: _Optional[_Iterable[_Union[FieldId, _Mapping]]]=...) -> None:
        ...