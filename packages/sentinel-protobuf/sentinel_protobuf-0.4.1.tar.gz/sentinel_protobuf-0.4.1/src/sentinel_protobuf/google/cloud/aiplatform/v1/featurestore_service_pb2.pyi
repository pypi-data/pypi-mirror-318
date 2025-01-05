from google.api import annotations_pb2 as _annotations_pb2
from google.api import client_pb2 as _client_pb2
from google.api import field_behavior_pb2 as _field_behavior_pb2
from google.api import resource_pb2 as _resource_pb2
from google.cloud.aiplatform.v1 import entity_type_pb2 as _entity_type_pb2
from google.cloud.aiplatform.v1 import feature_pb2 as _feature_pb2
from google.cloud.aiplatform.v1 import feature_selector_pb2 as _feature_selector_pb2
from google.cloud.aiplatform.v1 import featurestore_pb2 as _featurestore_pb2
from google.cloud.aiplatform.v1 import io_pb2 as _io_pb2
from google.cloud.aiplatform.v1 import operation_pb2 as _operation_pb2
from google.longrunning import operations_pb2 as _operations_pb2
from google.protobuf import empty_pb2 as _empty_pb2
from google.protobuf import field_mask_pb2 as _field_mask_pb2
from google.protobuf import timestamp_pb2 as _timestamp_pb2
from google.type import interval_pb2 as _interval_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union
DESCRIPTOR: _descriptor.FileDescriptor

class CreateFeaturestoreRequest(_message.Message):
    __slots__ = ('parent', 'featurestore', 'featurestore_id')
    PARENT_FIELD_NUMBER: _ClassVar[int]
    FEATURESTORE_FIELD_NUMBER: _ClassVar[int]
    FEATURESTORE_ID_FIELD_NUMBER: _ClassVar[int]
    parent: str
    featurestore: _featurestore_pb2.Featurestore
    featurestore_id: str

    def __init__(self, parent: _Optional[str]=..., featurestore: _Optional[_Union[_featurestore_pb2.Featurestore, _Mapping]]=..., featurestore_id: _Optional[str]=...) -> None:
        ...

class GetFeaturestoreRequest(_message.Message):
    __slots__ = ('name',)
    NAME_FIELD_NUMBER: _ClassVar[int]
    name: str

    def __init__(self, name: _Optional[str]=...) -> None:
        ...

class ListFeaturestoresRequest(_message.Message):
    __slots__ = ('parent', 'filter', 'page_size', 'page_token', 'order_by', 'read_mask')
    PARENT_FIELD_NUMBER: _ClassVar[int]
    FILTER_FIELD_NUMBER: _ClassVar[int]
    PAGE_SIZE_FIELD_NUMBER: _ClassVar[int]
    PAGE_TOKEN_FIELD_NUMBER: _ClassVar[int]
    ORDER_BY_FIELD_NUMBER: _ClassVar[int]
    READ_MASK_FIELD_NUMBER: _ClassVar[int]
    parent: str
    filter: str
    page_size: int
    page_token: str
    order_by: str
    read_mask: _field_mask_pb2.FieldMask

    def __init__(self, parent: _Optional[str]=..., filter: _Optional[str]=..., page_size: _Optional[int]=..., page_token: _Optional[str]=..., order_by: _Optional[str]=..., read_mask: _Optional[_Union[_field_mask_pb2.FieldMask, _Mapping]]=...) -> None:
        ...

class ListFeaturestoresResponse(_message.Message):
    __slots__ = ('featurestores', 'next_page_token')
    FEATURESTORES_FIELD_NUMBER: _ClassVar[int]
    NEXT_PAGE_TOKEN_FIELD_NUMBER: _ClassVar[int]
    featurestores: _containers.RepeatedCompositeFieldContainer[_featurestore_pb2.Featurestore]
    next_page_token: str

    def __init__(self, featurestores: _Optional[_Iterable[_Union[_featurestore_pb2.Featurestore, _Mapping]]]=..., next_page_token: _Optional[str]=...) -> None:
        ...

class UpdateFeaturestoreRequest(_message.Message):
    __slots__ = ('featurestore', 'update_mask')
    FEATURESTORE_FIELD_NUMBER: _ClassVar[int]
    UPDATE_MASK_FIELD_NUMBER: _ClassVar[int]
    featurestore: _featurestore_pb2.Featurestore
    update_mask: _field_mask_pb2.FieldMask

    def __init__(self, featurestore: _Optional[_Union[_featurestore_pb2.Featurestore, _Mapping]]=..., update_mask: _Optional[_Union[_field_mask_pb2.FieldMask, _Mapping]]=...) -> None:
        ...

class DeleteFeaturestoreRequest(_message.Message):
    __slots__ = ('name', 'force')
    NAME_FIELD_NUMBER: _ClassVar[int]
    FORCE_FIELD_NUMBER: _ClassVar[int]
    name: str
    force: bool

    def __init__(self, name: _Optional[str]=..., force: bool=...) -> None:
        ...

class ImportFeatureValuesRequest(_message.Message):
    __slots__ = ('avro_source', 'bigquery_source', 'csv_source', 'feature_time_field', 'feature_time', 'entity_type', 'entity_id_field', 'feature_specs', 'disable_online_serving', 'worker_count', 'disable_ingestion_analysis')

    class FeatureSpec(_message.Message):
        __slots__ = ('id', 'source_field')
        ID_FIELD_NUMBER: _ClassVar[int]
        SOURCE_FIELD_FIELD_NUMBER: _ClassVar[int]
        id: str
        source_field: str

        def __init__(self, id: _Optional[str]=..., source_field: _Optional[str]=...) -> None:
            ...
    AVRO_SOURCE_FIELD_NUMBER: _ClassVar[int]
    BIGQUERY_SOURCE_FIELD_NUMBER: _ClassVar[int]
    CSV_SOURCE_FIELD_NUMBER: _ClassVar[int]
    FEATURE_TIME_FIELD_FIELD_NUMBER: _ClassVar[int]
    FEATURE_TIME_FIELD_NUMBER: _ClassVar[int]
    ENTITY_TYPE_FIELD_NUMBER: _ClassVar[int]
    ENTITY_ID_FIELD_FIELD_NUMBER: _ClassVar[int]
    FEATURE_SPECS_FIELD_NUMBER: _ClassVar[int]
    DISABLE_ONLINE_SERVING_FIELD_NUMBER: _ClassVar[int]
    WORKER_COUNT_FIELD_NUMBER: _ClassVar[int]
    DISABLE_INGESTION_ANALYSIS_FIELD_NUMBER: _ClassVar[int]
    avro_source: _io_pb2.AvroSource
    bigquery_source: _io_pb2.BigQuerySource
    csv_source: _io_pb2.CsvSource
    feature_time_field: str
    feature_time: _timestamp_pb2.Timestamp
    entity_type: str
    entity_id_field: str
    feature_specs: _containers.RepeatedCompositeFieldContainer[ImportFeatureValuesRequest.FeatureSpec]
    disable_online_serving: bool
    worker_count: int
    disable_ingestion_analysis: bool

    def __init__(self, avro_source: _Optional[_Union[_io_pb2.AvroSource, _Mapping]]=..., bigquery_source: _Optional[_Union[_io_pb2.BigQuerySource, _Mapping]]=..., csv_source: _Optional[_Union[_io_pb2.CsvSource, _Mapping]]=..., feature_time_field: _Optional[str]=..., feature_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]]=..., entity_type: _Optional[str]=..., entity_id_field: _Optional[str]=..., feature_specs: _Optional[_Iterable[_Union[ImportFeatureValuesRequest.FeatureSpec, _Mapping]]]=..., disable_online_serving: bool=..., worker_count: _Optional[int]=..., disable_ingestion_analysis: bool=...) -> None:
        ...

class ImportFeatureValuesResponse(_message.Message):
    __slots__ = ('imported_entity_count', 'imported_feature_value_count', 'invalid_row_count', 'timestamp_outside_retention_rows_count')
    IMPORTED_ENTITY_COUNT_FIELD_NUMBER: _ClassVar[int]
    IMPORTED_FEATURE_VALUE_COUNT_FIELD_NUMBER: _ClassVar[int]
    INVALID_ROW_COUNT_FIELD_NUMBER: _ClassVar[int]
    TIMESTAMP_OUTSIDE_RETENTION_ROWS_COUNT_FIELD_NUMBER: _ClassVar[int]
    imported_entity_count: int
    imported_feature_value_count: int
    invalid_row_count: int
    timestamp_outside_retention_rows_count: int

    def __init__(self, imported_entity_count: _Optional[int]=..., imported_feature_value_count: _Optional[int]=..., invalid_row_count: _Optional[int]=..., timestamp_outside_retention_rows_count: _Optional[int]=...) -> None:
        ...

class BatchReadFeatureValuesRequest(_message.Message):
    __slots__ = ('csv_read_instances', 'bigquery_read_instances', 'featurestore', 'destination', 'pass_through_fields', 'entity_type_specs', 'start_time')

    class PassThroughField(_message.Message):
        __slots__ = ('field_name',)
        FIELD_NAME_FIELD_NUMBER: _ClassVar[int]
        field_name: str

        def __init__(self, field_name: _Optional[str]=...) -> None:
            ...

    class EntityTypeSpec(_message.Message):
        __slots__ = ('entity_type_id', 'feature_selector', 'settings')
        ENTITY_TYPE_ID_FIELD_NUMBER: _ClassVar[int]
        FEATURE_SELECTOR_FIELD_NUMBER: _ClassVar[int]
        SETTINGS_FIELD_NUMBER: _ClassVar[int]
        entity_type_id: str
        feature_selector: _feature_selector_pb2.FeatureSelector
        settings: _containers.RepeatedCompositeFieldContainer[DestinationFeatureSetting]

        def __init__(self, entity_type_id: _Optional[str]=..., feature_selector: _Optional[_Union[_feature_selector_pb2.FeatureSelector, _Mapping]]=..., settings: _Optional[_Iterable[_Union[DestinationFeatureSetting, _Mapping]]]=...) -> None:
            ...
    CSV_READ_INSTANCES_FIELD_NUMBER: _ClassVar[int]
    BIGQUERY_READ_INSTANCES_FIELD_NUMBER: _ClassVar[int]
    FEATURESTORE_FIELD_NUMBER: _ClassVar[int]
    DESTINATION_FIELD_NUMBER: _ClassVar[int]
    PASS_THROUGH_FIELDS_FIELD_NUMBER: _ClassVar[int]
    ENTITY_TYPE_SPECS_FIELD_NUMBER: _ClassVar[int]
    START_TIME_FIELD_NUMBER: _ClassVar[int]
    csv_read_instances: _io_pb2.CsvSource
    bigquery_read_instances: _io_pb2.BigQuerySource
    featurestore: str
    destination: FeatureValueDestination
    pass_through_fields: _containers.RepeatedCompositeFieldContainer[BatchReadFeatureValuesRequest.PassThroughField]
    entity_type_specs: _containers.RepeatedCompositeFieldContainer[BatchReadFeatureValuesRequest.EntityTypeSpec]
    start_time: _timestamp_pb2.Timestamp

    def __init__(self, csv_read_instances: _Optional[_Union[_io_pb2.CsvSource, _Mapping]]=..., bigquery_read_instances: _Optional[_Union[_io_pb2.BigQuerySource, _Mapping]]=..., featurestore: _Optional[str]=..., destination: _Optional[_Union[FeatureValueDestination, _Mapping]]=..., pass_through_fields: _Optional[_Iterable[_Union[BatchReadFeatureValuesRequest.PassThroughField, _Mapping]]]=..., entity_type_specs: _Optional[_Iterable[_Union[BatchReadFeatureValuesRequest.EntityTypeSpec, _Mapping]]]=..., start_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]]=...) -> None:
        ...

class ExportFeatureValuesRequest(_message.Message):
    __slots__ = ('snapshot_export', 'full_export', 'entity_type', 'destination', 'feature_selector', 'settings')

    class SnapshotExport(_message.Message):
        __slots__ = ('snapshot_time', 'start_time')
        SNAPSHOT_TIME_FIELD_NUMBER: _ClassVar[int]
        START_TIME_FIELD_NUMBER: _ClassVar[int]
        snapshot_time: _timestamp_pb2.Timestamp
        start_time: _timestamp_pb2.Timestamp

        def __init__(self, snapshot_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]]=..., start_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]]=...) -> None:
            ...

    class FullExport(_message.Message):
        __slots__ = ('start_time', 'end_time')
        START_TIME_FIELD_NUMBER: _ClassVar[int]
        END_TIME_FIELD_NUMBER: _ClassVar[int]
        start_time: _timestamp_pb2.Timestamp
        end_time: _timestamp_pb2.Timestamp

        def __init__(self, start_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]]=..., end_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]]=...) -> None:
            ...
    SNAPSHOT_EXPORT_FIELD_NUMBER: _ClassVar[int]
    FULL_EXPORT_FIELD_NUMBER: _ClassVar[int]
    ENTITY_TYPE_FIELD_NUMBER: _ClassVar[int]
    DESTINATION_FIELD_NUMBER: _ClassVar[int]
    FEATURE_SELECTOR_FIELD_NUMBER: _ClassVar[int]
    SETTINGS_FIELD_NUMBER: _ClassVar[int]
    snapshot_export: ExportFeatureValuesRequest.SnapshotExport
    full_export: ExportFeatureValuesRequest.FullExport
    entity_type: str
    destination: FeatureValueDestination
    feature_selector: _feature_selector_pb2.FeatureSelector
    settings: _containers.RepeatedCompositeFieldContainer[DestinationFeatureSetting]

    def __init__(self, snapshot_export: _Optional[_Union[ExportFeatureValuesRequest.SnapshotExport, _Mapping]]=..., full_export: _Optional[_Union[ExportFeatureValuesRequest.FullExport, _Mapping]]=..., entity_type: _Optional[str]=..., destination: _Optional[_Union[FeatureValueDestination, _Mapping]]=..., feature_selector: _Optional[_Union[_feature_selector_pb2.FeatureSelector, _Mapping]]=..., settings: _Optional[_Iterable[_Union[DestinationFeatureSetting, _Mapping]]]=...) -> None:
        ...

class DestinationFeatureSetting(_message.Message):
    __slots__ = ('feature_id', 'destination_field')
    FEATURE_ID_FIELD_NUMBER: _ClassVar[int]
    DESTINATION_FIELD_FIELD_NUMBER: _ClassVar[int]
    feature_id: str
    destination_field: str

    def __init__(self, feature_id: _Optional[str]=..., destination_field: _Optional[str]=...) -> None:
        ...

class FeatureValueDestination(_message.Message):
    __slots__ = ('bigquery_destination', 'tfrecord_destination', 'csv_destination')
    BIGQUERY_DESTINATION_FIELD_NUMBER: _ClassVar[int]
    TFRECORD_DESTINATION_FIELD_NUMBER: _ClassVar[int]
    CSV_DESTINATION_FIELD_NUMBER: _ClassVar[int]
    bigquery_destination: _io_pb2.BigQueryDestination
    tfrecord_destination: _io_pb2.TFRecordDestination
    csv_destination: _io_pb2.CsvDestination

    def __init__(self, bigquery_destination: _Optional[_Union[_io_pb2.BigQueryDestination, _Mapping]]=..., tfrecord_destination: _Optional[_Union[_io_pb2.TFRecordDestination, _Mapping]]=..., csv_destination: _Optional[_Union[_io_pb2.CsvDestination, _Mapping]]=...) -> None:
        ...

class ExportFeatureValuesResponse(_message.Message):
    __slots__ = ()

    def __init__(self) -> None:
        ...

class BatchReadFeatureValuesResponse(_message.Message):
    __slots__ = ()

    def __init__(self) -> None:
        ...

class CreateEntityTypeRequest(_message.Message):
    __slots__ = ('parent', 'entity_type', 'entity_type_id')
    PARENT_FIELD_NUMBER: _ClassVar[int]
    ENTITY_TYPE_FIELD_NUMBER: _ClassVar[int]
    ENTITY_TYPE_ID_FIELD_NUMBER: _ClassVar[int]
    parent: str
    entity_type: _entity_type_pb2.EntityType
    entity_type_id: str

    def __init__(self, parent: _Optional[str]=..., entity_type: _Optional[_Union[_entity_type_pb2.EntityType, _Mapping]]=..., entity_type_id: _Optional[str]=...) -> None:
        ...

class GetEntityTypeRequest(_message.Message):
    __slots__ = ('name',)
    NAME_FIELD_NUMBER: _ClassVar[int]
    name: str

    def __init__(self, name: _Optional[str]=...) -> None:
        ...

class ListEntityTypesRequest(_message.Message):
    __slots__ = ('parent', 'filter', 'page_size', 'page_token', 'order_by', 'read_mask')
    PARENT_FIELD_NUMBER: _ClassVar[int]
    FILTER_FIELD_NUMBER: _ClassVar[int]
    PAGE_SIZE_FIELD_NUMBER: _ClassVar[int]
    PAGE_TOKEN_FIELD_NUMBER: _ClassVar[int]
    ORDER_BY_FIELD_NUMBER: _ClassVar[int]
    READ_MASK_FIELD_NUMBER: _ClassVar[int]
    parent: str
    filter: str
    page_size: int
    page_token: str
    order_by: str
    read_mask: _field_mask_pb2.FieldMask

    def __init__(self, parent: _Optional[str]=..., filter: _Optional[str]=..., page_size: _Optional[int]=..., page_token: _Optional[str]=..., order_by: _Optional[str]=..., read_mask: _Optional[_Union[_field_mask_pb2.FieldMask, _Mapping]]=...) -> None:
        ...

class ListEntityTypesResponse(_message.Message):
    __slots__ = ('entity_types', 'next_page_token')
    ENTITY_TYPES_FIELD_NUMBER: _ClassVar[int]
    NEXT_PAGE_TOKEN_FIELD_NUMBER: _ClassVar[int]
    entity_types: _containers.RepeatedCompositeFieldContainer[_entity_type_pb2.EntityType]
    next_page_token: str

    def __init__(self, entity_types: _Optional[_Iterable[_Union[_entity_type_pb2.EntityType, _Mapping]]]=..., next_page_token: _Optional[str]=...) -> None:
        ...

class UpdateEntityTypeRequest(_message.Message):
    __slots__ = ('entity_type', 'update_mask')
    ENTITY_TYPE_FIELD_NUMBER: _ClassVar[int]
    UPDATE_MASK_FIELD_NUMBER: _ClassVar[int]
    entity_type: _entity_type_pb2.EntityType
    update_mask: _field_mask_pb2.FieldMask

    def __init__(self, entity_type: _Optional[_Union[_entity_type_pb2.EntityType, _Mapping]]=..., update_mask: _Optional[_Union[_field_mask_pb2.FieldMask, _Mapping]]=...) -> None:
        ...

class DeleteEntityTypeRequest(_message.Message):
    __slots__ = ('name', 'force')
    NAME_FIELD_NUMBER: _ClassVar[int]
    FORCE_FIELD_NUMBER: _ClassVar[int]
    name: str
    force: bool

    def __init__(self, name: _Optional[str]=..., force: bool=...) -> None:
        ...

class CreateFeatureRequest(_message.Message):
    __slots__ = ('parent', 'feature', 'feature_id')
    PARENT_FIELD_NUMBER: _ClassVar[int]
    FEATURE_FIELD_NUMBER: _ClassVar[int]
    FEATURE_ID_FIELD_NUMBER: _ClassVar[int]
    parent: str
    feature: _feature_pb2.Feature
    feature_id: str

    def __init__(self, parent: _Optional[str]=..., feature: _Optional[_Union[_feature_pb2.Feature, _Mapping]]=..., feature_id: _Optional[str]=...) -> None:
        ...

class BatchCreateFeaturesRequest(_message.Message):
    __slots__ = ('parent', 'requests')
    PARENT_FIELD_NUMBER: _ClassVar[int]
    REQUESTS_FIELD_NUMBER: _ClassVar[int]
    parent: str
    requests: _containers.RepeatedCompositeFieldContainer[CreateFeatureRequest]

    def __init__(self, parent: _Optional[str]=..., requests: _Optional[_Iterable[_Union[CreateFeatureRequest, _Mapping]]]=...) -> None:
        ...

class BatchCreateFeaturesResponse(_message.Message):
    __slots__ = ('features',)
    FEATURES_FIELD_NUMBER: _ClassVar[int]
    features: _containers.RepeatedCompositeFieldContainer[_feature_pb2.Feature]

    def __init__(self, features: _Optional[_Iterable[_Union[_feature_pb2.Feature, _Mapping]]]=...) -> None:
        ...

class GetFeatureRequest(_message.Message):
    __slots__ = ('name',)
    NAME_FIELD_NUMBER: _ClassVar[int]
    name: str

    def __init__(self, name: _Optional[str]=...) -> None:
        ...

class ListFeaturesRequest(_message.Message):
    __slots__ = ('parent', 'filter', 'page_size', 'page_token', 'order_by', 'read_mask', 'latest_stats_count')
    PARENT_FIELD_NUMBER: _ClassVar[int]
    FILTER_FIELD_NUMBER: _ClassVar[int]
    PAGE_SIZE_FIELD_NUMBER: _ClassVar[int]
    PAGE_TOKEN_FIELD_NUMBER: _ClassVar[int]
    ORDER_BY_FIELD_NUMBER: _ClassVar[int]
    READ_MASK_FIELD_NUMBER: _ClassVar[int]
    LATEST_STATS_COUNT_FIELD_NUMBER: _ClassVar[int]
    parent: str
    filter: str
    page_size: int
    page_token: str
    order_by: str
    read_mask: _field_mask_pb2.FieldMask
    latest_stats_count: int

    def __init__(self, parent: _Optional[str]=..., filter: _Optional[str]=..., page_size: _Optional[int]=..., page_token: _Optional[str]=..., order_by: _Optional[str]=..., read_mask: _Optional[_Union[_field_mask_pb2.FieldMask, _Mapping]]=..., latest_stats_count: _Optional[int]=...) -> None:
        ...

class ListFeaturesResponse(_message.Message):
    __slots__ = ('features', 'next_page_token')
    FEATURES_FIELD_NUMBER: _ClassVar[int]
    NEXT_PAGE_TOKEN_FIELD_NUMBER: _ClassVar[int]
    features: _containers.RepeatedCompositeFieldContainer[_feature_pb2.Feature]
    next_page_token: str

    def __init__(self, features: _Optional[_Iterable[_Union[_feature_pb2.Feature, _Mapping]]]=..., next_page_token: _Optional[str]=...) -> None:
        ...

class SearchFeaturesRequest(_message.Message):
    __slots__ = ('location', 'query', 'page_size', 'page_token')
    LOCATION_FIELD_NUMBER: _ClassVar[int]
    QUERY_FIELD_NUMBER: _ClassVar[int]
    PAGE_SIZE_FIELD_NUMBER: _ClassVar[int]
    PAGE_TOKEN_FIELD_NUMBER: _ClassVar[int]
    location: str
    query: str
    page_size: int
    page_token: str

    def __init__(self, location: _Optional[str]=..., query: _Optional[str]=..., page_size: _Optional[int]=..., page_token: _Optional[str]=...) -> None:
        ...

class SearchFeaturesResponse(_message.Message):
    __slots__ = ('features', 'next_page_token')
    FEATURES_FIELD_NUMBER: _ClassVar[int]
    NEXT_PAGE_TOKEN_FIELD_NUMBER: _ClassVar[int]
    features: _containers.RepeatedCompositeFieldContainer[_feature_pb2.Feature]
    next_page_token: str

    def __init__(self, features: _Optional[_Iterable[_Union[_feature_pb2.Feature, _Mapping]]]=..., next_page_token: _Optional[str]=...) -> None:
        ...

class UpdateFeatureRequest(_message.Message):
    __slots__ = ('feature', 'update_mask')
    FEATURE_FIELD_NUMBER: _ClassVar[int]
    UPDATE_MASK_FIELD_NUMBER: _ClassVar[int]
    feature: _feature_pb2.Feature
    update_mask: _field_mask_pb2.FieldMask

    def __init__(self, feature: _Optional[_Union[_feature_pb2.Feature, _Mapping]]=..., update_mask: _Optional[_Union[_field_mask_pb2.FieldMask, _Mapping]]=...) -> None:
        ...

class DeleteFeatureRequest(_message.Message):
    __slots__ = ('name',)
    NAME_FIELD_NUMBER: _ClassVar[int]
    name: str

    def __init__(self, name: _Optional[str]=...) -> None:
        ...

class CreateFeaturestoreOperationMetadata(_message.Message):
    __slots__ = ('generic_metadata',)
    GENERIC_METADATA_FIELD_NUMBER: _ClassVar[int]
    generic_metadata: _operation_pb2.GenericOperationMetadata

    def __init__(self, generic_metadata: _Optional[_Union[_operation_pb2.GenericOperationMetadata, _Mapping]]=...) -> None:
        ...

class UpdateFeaturestoreOperationMetadata(_message.Message):
    __slots__ = ('generic_metadata',)
    GENERIC_METADATA_FIELD_NUMBER: _ClassVar[int]
    generic_metadata: _operation_pb2.GenericOperationMetadata

    def __init__(self, generic_metadata: _Optional[_Union[_operation_pb2.GenericOperationMetadata, _Mapping]]=...) -> None:
        ...

class ImportFeatureValuesOperationMetadata(_message.Message):
    __slots__ = ('generic_metadata', 'imported_entity_count', 'imported_feature_value_count', 'source_uris', 'invalid_row_count', 'timestamp_outside_retention_rows_count', 'blocking_operation_ids')
    GENERIC_METADATA_FIELD_NUMBER: _ClassVar[int]
    IMPORTED_ENTITY_COUNT_FIELD_NUMBER: _ClassVar[int]
    IMPORTED_FEATURE_VALUE_COUNT_FIELD_NUMBER: _ClassVar[int]
    SOURCE_URIS_FIELD_NUMBER: _ClassVar[int]
    INVALID_ROW_COUNT_FIELD_NUMBER: _ClassVar[int]
    TIMESTAMP_OUTSIDE_RETENTION_ROWS_COUNT_FIELD_NUMBER: _ClassVar[int]
    BLOCKING_OPERATION_IDS_FIELD_NUMBER: _ClassVar[int]
    generic_metadata: _operation_pb2.GenericOperationMetadata
    imported_entity_count: int
    imported_feature_value_count: int
    source_uris: _containers.RepeatedScalarFieldContainer[str]
    invalid_row_count: int
    timestamp_outside_retention_rows_count: int
    blocking_operation_ids: _containers.RepeatedScalarFieldContainer[int]

    def __init__(self, generic_metadata: _Optional[_Union[_operation_pb2.GenericOperationMetadata, _Mapping]]=..., imported_entity_count: _Optional[int]=..., imported_feature_value_count: _Optional[int]=..., source_uris: _Optional[_Iterable[str]]=..., invalid_row_count: _Optional[int]=..., timestamp_outside_retention_rows_count: _Optional[int]=..., blocking_operation_ids: _Optional[_Iterable[int]]=...) -> None:
        ...

class ExportFeatureValuesOperationMetadata(_message.Message):
    __slots__ = ('generic_metadata',)
    GENERIC_METADATA_FIELD_NUMBER: _ClassVar[int]
    generic_metadata: _operation_pb2.GenericOperationMetadata

    def __init__(self, generic_metadata: _Optional[_Union[_operation_pb2.GenericOperationMetadata, _Mapping]]=...) -> None:
        ...

class BatchReadFeatureValuesOperationMetadata(_message.Message):
    __slots__ = ('generic_metadata',)
    GENERIC_METADATA_FIELD_NUMBER: _ClassVar[int]
    generic_metadata: _operation_pb2.GenericOperationMetadata

    def __init__(self, generic_metadata: _Optional[_Union[_operation_pb2.GenericOperationMetadata, _Mapping]]=...) -> None:
        ...

class DeleteFeatureValuesOperationMetadata(_message.Message):
    __slots__ = ('generic_metadata',)
    GENERIC_METADATA_FIELD_NUMBER: _ClassVar[int]
    generic_metadata: _operation_pb2.GenericOperationMetadata

    def __init__(self, generic_metadata: _Optional[_Union[_operation_pb2.GenericOperationMetadata, _Mapping]]=...) -> None:
        ...

class CreateEntityTypeOperationMetadata(_message.Message):
    __slots__ = ('generic_metadata',)
    GENERIC_METADATA_FIELD_NUMBER: _ClassVar[int]
    generic_metadata: _operation_pb2.GenericOperationMetadata

    def __init__(self, generic_metadata: _Optional[_Union[_operation_pb2.GenericOperationMetadata, _Mapping]]=...) -> None:
        ...

class CreateFeatureOperationMetadata(_message.Message):
    __slots__ = ('generic_metadata',)
    GENERIC_METADATA_FIELD_NUMBER: _ClassVar[int]
    generic_metadata: _operation_pb2.GenericOperationMetadata

    def __init__(self, generic_metadata: _Optional[_Union[_operation_pb2.GenericOperationMetadata, _Mapping]]=...) -> None:
        ...

class BatchCreateFeaturesOperationMetadata(_message.Message):
    __slots__ = ('generic_metadata',)
    GENERIC_METADATA_FIELD_NUMBER: _ClassVar[int]
    generic_metadata: _operation_pb2.GenericOperationMetadata

    def __init__(self, generic_metadata: _Optional[_Union[_operation_pb2.GenericOperationMetadata, _Mapping]]=...) -> None:
        ...

class DeleteFeatureValuesRequest(_message.Message):
    __slots__ = ('select_entity', 'select_time_range_and_feature', 'entity_type')

    class SelectEntity(_message.Message):
        __slots__ = ('entity_id_selector',)
        ENTITY_ID_SELECTOR_FIELD_NUMBER: _ClassVar[int]
        entity_id_selector: EntityIdSelector

        def __init__(self, entity_id_selector: _Optional[_Union[EntityIdSelector, _Mapping]]=...) -> None:
            ...

    class SelectTimeRangeAndFeature(_message.Message):
        __slots__ = ('time_range', 'feature_selector', 'skip_online_storage_delete')
        TIME_RANGE_FIELD_NUMBER: _ClassVar[int]
        FEATURE_SELECTOR_FIELD_NUMBER: _ClassVar[int]
        SKIP_ONLINE_STORAGE_DELETE_FIELD_NUMBER: _ClassVar[int]
        time_range: _interval_pb2.Interval
        feature_selector: _feature_selector_pb2.FeatureSelector
        skip_online_storage_delete: bool

        def __init__(self, time_range: _Optional[_Union[_interval_pb2.Interval, _Mapping]]=..., feature_selector: _Optional[_Union[_feature_selector_pb2.FeatureSelector, _Mapping]]=..., skip_online_storage_delete: bool=...) -> None:
            ...
    SELECT_ENTITY_FIELD_NUMBER: _ClassVar[int]
    SELECT_TIME_RANGE_AND_FEATURE_FIELD_NUMBER: _ClassVar[int]
    ENTITY_TYPE_FIELD_NUMBER: _ClassVar[int]
    select_entity: DeleteFeatureValuesRequest.SelectEntity
    select_time_range_and_feature: DeleteFeatureValuesRequest.SelectTimeRangeAndFeature
    entity_type: str

    def __init__(self, select_entity: _Optional[_Union[DeleteFeatureValuesRequest.SelectEntity, _Mapping]]=..., select_time_range_and_feature: _Optional[_Union[DeleteFeatureValuesRequest.SelectTimeRangeAndFeature, _Mapping]]=..., entity_type: _Optional[str]=...) -> None:
        ...

class DeleteFeatureValuesResponse(_message.Message):
    __slots__ = ('select_entity', 'select_time_range_and_feature')

    class SelectEntity(_message.Message):
        __slots__ = ('offline_storage_deleted_entity_row_count', 'online_storage_deleted_entity_count')
        OFFLINE_STORAGE_DELETED_ENTITY_ROW_COUNT_FIELD_NUMBER: _ClassVar[int]
        ONLINE_STORAGE_DELETED_ENTITY_COUNT_FIELD_NUMBER: _ClassVar[int]
        offline_storage_deleted_entity_row_count: int
        online_storage_deleted_entity_count: int

        def __init__(self, offline_storage_deleted_entity_row_count: _Optional[int]=..., online_storage_deleted_entity_count: _Optional[int]=...) -> None:
            ...

    class SelectTimeRangeAndFeature(_message.Message):
        __slots__ = ('impacted_feature_count', 'offline_storage_modified_entity_row_count', 'online_storage_modified_entity_count')
        IMPACTED_FEATURE_COUNT_FIELD_NUMBER: _ClassVar[int]
        OFFLINE_STORAGE_MODIFIED_ENTITY_ROW_COUNT_FIELD_NUMBER: _ClassVar[int]
        ONLINE_STORAGE_MODIFIED_ENTITY_COUNT_FIELD_NUMBER: _ClassVar[int]
        impacted_feature_count: int
        offline_storage_modified_entity_row_count: int
        online_storage_modified_entity_count: int

        def __init__(self, impacted_feature_count: _Optional[int]=..., offline_storage_modified_entity_row_count: _Optional[int]=..., online_storage_modified_entity_count: _Optional[int]=...) -> None:
            ...
    SELECT_ENTITY_FIELD_NUMBER: _ClassVar[int]
    SELECT_TIME_RANGE_AND_FEATURE_FIELD_NUMBER: _ClassVar[int]
    select_entity: DeleteFeatureValuesResponse.SelectEntity
    select_time_range_and_feature: DeleteFeatureValuesResponse.SelectTimeRangeAndFeature

    def __init__(self, select_entity: _Optional[_Union[DeleteFeatureValuesResponse.SelectEntity, _Mapping]]=..., select_time_range_and_feature: _Optional[_Union[DeleteFeatureValuesResponse.SelectTimeRangeAndFeature, _Mapping]]=...) -> None:
        ...

class EntityIdSelector(_message.Message):
    __slots__ = ('csv_source', 'entity_id_field')
    CSV_SOURCE_FIELD_NUMBER: _ClassVar[int]
    ENTITY_ID_FIELD_FIELD_NUMBER: _ClassVar[int]
    csv_source: _io_pb2.CsvSource
    entity_id_field: str

    def __init__(self, csv_source: _Optional[_Union[_io_pb2.CsvSource, _Mapping]]=..., entity_id_field: _Optional[str]=...) -> None:
        ...