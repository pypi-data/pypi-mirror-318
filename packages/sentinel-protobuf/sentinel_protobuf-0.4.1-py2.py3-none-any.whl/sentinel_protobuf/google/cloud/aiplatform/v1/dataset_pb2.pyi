from google.api import field_behavior_pb2 as _field_behavior_pb2
from google.api import resource_pb2 as _resource_pb2
from google.cloud.aiplatform.v1 import encryption_spec_pb2 as _encryption_spec_pb2
from google.cloud.aiplatform.v1 import io_pb2 as _io_pb2
from google.cloud.aiplatform.v1 import saved_query_pb2 as _saved_query_pb2
from google.protobuf import struct_pb2 as _struct_pb2
from google.protobuf import timestamp_pb2 as _timestamp_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union
DESCRIPTOR: _descriptor.FileDescriptor

class Dataset(_message.Message):
    __slots__ = ('name', 'display_name', 'description', 'metadata_schema_uri', 'metadata', 'data_item_count', 'create_time', 'update_time', 'etag', 'labels', 'saved_queries', 'encryption_spec', 'metadata_artifact', 'model_reference', 'satisfies_pzs', 'satisfies_pzi')

    class LabelsEntry(_message.Message):
        __slots__ = ('key', 'value')
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: str

        def __init__(self, key: _Optional[str]=..., value: _Optional[str]=...) -> None:
            ...
    NAME_FIELD_NUMBER: _ClassVar[int]
    DISPLAY_NAME_FIELD_NUMBER: _ClassVar[int]
    DESCRIPTION_FIELD_NUMBER: _ClassVar[int]
    METADATA_SCHEMA_URI_FIELD_NUMBER: _ClassVar[int]
    METADATA_FIELD_NUMBER: _ClassVar[int]
    DATA_ITEM_COUNT_FIELD_NUMBER: _ClassVar[int]
    CREATE_TIME_FIELD_NUMBER: _ClassVar[int]
    UPDATE_TIME_FIELD_NUMBER: _ClassVar[int]
    ETAG_FIELD_NUMBER: _ClassVar[int]
    LABELS_FIELD_NUMBER: _ClassVar[int]
    SAVED_QUERIES_FIELD_NUMBER: _ClassVar[int]
    ENCRYPTION_SPEC_FIELD_NUMBER: _ClassVar[int]
    METADATA_ARTIFACT_FIELD_NUMBER: _ClassVar[int]
    MODEL_REFERENCE_FIELD_NUMBER: _ClassVar[int]
    SATISFIES_PZS_FIELD_NUMBER: _ClassVar[int]
    SATISFIES_PZI_FIELD_NUMBER: _ClassVar[int]
    name: str
    display_name: str
    description: str
    metadata_schema_uri: str
    metadata: _struct_pb2.Value
    data_item_count: int
    create_time: _timestamp_pb2.Timestamp
    update_time: _timestamp_pb2.Timestamp
    etag: str
    labels: _containers.ScalarMap[str, str]
    saved_queries: _containers.RepeatedCompositeFieldContainer[_saved_query_pb2.SavedQuery]
    encryption_spec: _encryption_spec_pb2.EncryptionSpec
    metadata_artifact: str
    model_reference: str
    satisfies_pzs: bool
    satisfies_pzi: bool

    def __init__(self, name: _Optional[str]=..., display_name: _Optional[str]=..., description: _Optional[str]=..., metadata_schema_uri: _Optional[str]=..., metadata: _Optional[_Union[_struct_pb2.Value, _Mapping]]=..., data_item_count: _Optional[int]=..., create_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]]=..., update_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]]=..., etag: _Optional[str]=..., labels: _Optional[_Mapping[str, str]]=..., saved_queries: _Optional[_Iterable[_Union[_saved_query_pb2.SavedQuery, _Mapping]]]=..., encryption_spec: _Optional[_Union[_encryption_spec_pb2.EncryptionSpec, _Mapping]]=..., metadata_artifact: _Optional[str]=..., model_reference: _Optional[str]=..., satisfies_pzs: bool=..., satisfies_pzi: bool=...) -> None:
        ...

class ImportDataConfig(_message.Message):
    __slots__ = ('gcs_source', 'data_item_labels', 'annotation_labels', 'import_schema_uri')

    class DataItemLabelsEntry(_message.Message):
        __slots__ = ('key', 'value')
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: str

        def __init__(self, key: _Optional[str]=..., value: _Optional[str]=...) -> None:
            ...

    class AnnotationLabelsEntry(_message.Message):
        __slots__ = ('key', 'value')
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: str

        def __init__(self, key: _Optional[str]=..., value: _Optional[str]=...) -> None:
            ...
    GCS_SOURCE_FIELD_NUMBER: _ClassVar[int]
    DATA_ITEM_LABELS_FIELD_NUMBER: _ClassVar[int]
    ANNOTATION_LABELS_FIELD_NUMBER: _ClassVar[int]
    IMPORT_SCHEMA_URI_FIELD_NUMBER: _ClassVar[int]
    gcs_source: _io_pb2.GcsSource
    data_item_labels: _containers.ScalarMap[str, str]
    annotation_labels: _containers.ScalarMap[str, str]
    import_schema_uri: str

    def __init__(self, gcs_source: _Optional[_Union[_io_pb2.GcsSource, _Mapping]]=..., data_item_labels: _Optional[_Mapping[str, str]]=..., annotation_labels: _Optional[_Mapping[str, str]]=..., import_schema_uri: _Optional[str]=...) -> None:
        ...

class ExportDataConfig(_message.Message):
    __slots__ = ('gcs_destination', 'fraction_split', 'filter_split', 'annotations_filter', 'saved_query_id', 'annotation_schema_uri', 'export_use')

    class ExportUse(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        EXPORT_USE_UNSPECIFIED: _ClassVar[ExportDataConfig.ExportUse]
        CUSTOM_CODE_TRAINING: _ClassVar[ExportDataConfig.ExportUse]
    EXPORT_USE_UNSPECIFIED: ExportDataConfig.ExportUse
    CUSTOM_CODE_TRAINING: ExportDataConfig.ExportUse
    GCS_DESTINATION_FIELD_NUMBER: _ClassVar[int]
    FRACTION_SPLIT_FIELD_NUMBER: _ClassVar[int]
    FILTER_SPLIT_FIELD_NUMBER: _ClassVar[int]
    ANNOTATIONS_FILTER_FIELD_NUMBER: _ClassVar[int]
    SAVED_QUERY_ID_FIELD_NUMBER: _ClassVar[int]
    ANNOTATION_SCHEMA_URI_FIELD_NUMBER: _ClassVar[int]
    EXPORT_USE_FIELD_NUMBER: _ClassVar[int]
    gcs_destination: _io_pb2.GcsDestination
    fraction_split: ExportFractionSplit
    filter_split: ExportFilterSplit
    annotations_filter: str
    saved_query_id: str
    annotation_schema_uri: str
    export_use: ExportDataConfig.ExportUse

    def __init__(self, gcs_destination: _Optional[_Union[_io_pb2.GcsDestination, _Mapping]]=..., fraction_split: _Optional[_Union[ExportFractionSplit, _Mapping]]=..., filter_split: _Optional[_Union[ExportFilterSplit, _Mapping]]=..., annotations_filter: _Optional[str]=..., saved_query_id: _Optional[str]=..., annotation_schema_uri: _Optional[str]=..., export_use: _Optional[_Union[ExportDataConfig.ExportUse, str]]=...) -> None:
        ...

class ExportFractionSplit(_message.Message):
    __slots__ = ('training_fraction', 'validation_fraction', 'test_fraction')
    TRAINING_FRACTION_FIELD_NUMBER: _ClassVar[int]
    VALIDATION_FRACTION_FIELD_NUMBER: _ClassVar[int]
    TEST_FRACTION_FIELD_NUMBER: _ClassVar[int]
    training_fraction: float
    validation_fraction: float
    test_fraction: float

    def __init__(self, training_fraction: _Optional[float]=..., validation_fraction: _Optional[float]=..., test_fraction: _Optional[float]=...) -> None:
        ...

class ExportFilterSplit(_message.Message):
    __slots__ = ('training_filter', 'validation_filter', 'test_filter')
    TRAINING_FILTER_FIELD_NUMBER: _ClassVar[int]
    VALIDATION_FILTER_FIELD_NUMBER: _ClassVar[int]
    TEST_FILTER_FIELD_NUMBER: _ClassVar[int]
    training_filter: str
    validation_filter: str
    test_filter: str

    def __init__(self, training_filter: _Optional[str]=..., validation_filter: _Optional[str]=..., test_filter: _Optional[str]=...) -> None:
        ...