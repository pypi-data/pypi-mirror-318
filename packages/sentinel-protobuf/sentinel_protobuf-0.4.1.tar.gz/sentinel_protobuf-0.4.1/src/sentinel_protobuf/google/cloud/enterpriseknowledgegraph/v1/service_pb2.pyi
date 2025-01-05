from google.api import annotations_pb2 as _annotations_pb2
from google.api import client_pb2 as _client_pb2
from google.api import field_behavior_pb2 as _field_behavior_pb2
from google.api import resource_pb2 as _resource_pb2
from google.cloud.enterpriseknowledgegraph.v1 import job_state_pb2 as _job_state_pb2
from google.cloud.enterpriseknowledgegraph.v1 import operation_metadata_pb2 as _operation_metadata_pb2
from google.protobuf import empty_pb2 as _empty_pb2
from google.protobuf import struct_pb2 as _struct_pb2
from google.protobuf import timestamp_pb2 as _timestamp_pb2
from google.protobuf import wrappers_pb2 as _wrappers_pb2
from google.rpc import status_pb2 as _status_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union
DESCRIPTOR: _descriptor.FileDescriptor

class InputConfig(_message.Message):
    __slots__ = ('bigquery_input_configs', 'entity_type', 'previous_result_bigquery_table')

    class EntityType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        ENTITY_TYPE_UNSPECIFIED: _ClassVar[InputConfig.EntityType]
        PEOPLE: _ClassVar[InputConfig.EntityType]
        ESTABLISHMENT: _ClassVar[InputConfig.EntityType]
        PROPERTY: _ClassVar[InputConfig.EntityType]
        PRODUCT: _ClassVar[InputConfig.EntityType]
        ORGANIZATION: _ClassVar[InputConfig.EntityType]
        LOCAL_BUSINESS: _ClassVar[InputConfig.EntityType]
        PERSON: _ClassVar[InputConfig.EntityType]
    ENTITY_TYPE_UNSPECIFIED: InputConfig.EntityType
    PEOPLE: InputConfig.EntityType
    ESTABLISHMENT: InputConfig.EntityType
    PROPERTY: InputConfig.EntityType
    PRODUCT: InputConfig.EntityType
    ORGANIZATION: InputConfig.EntityType
    LOCAL_BUSINESS: InputConfig.EntityType
    PERSON: InputConfig.EntityType
    BIGQUERY_INPUT_CONFIGS_FIELD_NUMBER: _ClassVar[int]
    ENTITY_TYPE_FIELD_NUMBER: _ClassVar[int]
    PREVIOUS_RESULT_BIGQUERY_TABLE_FIELD_NUMBER: _ClassVar[int]
    bigquery_input_configs: _containers.RepeatedCompositeFieldContainer[BigQueryInputConfig]
    entity_type: InputConfig.EntityType
    previous_result_bigquery_table: str

    def __init__(self, bigquery_input_configs: _Optional[_Iterable[_Union[BigQueryInputConfig, _Mapping]]]=..., entity_type: _Optional[_Union[InputConfig.EntityType, str]]=..., previous_result_bigquery_table: _Optional[str]=...) -> None:
        ...

class BigQueryInputConfig(_message.Message):
    __slots__ = ('bigquery_table', 'gcs_uri')
    BIGQUERY_TABLE_FIELD_NUMBER: _ClassVar[int]
    GCS_URI_FIELD_NUMBER: _ClassVar[int]
    bigquery_table: str
    gcs_uri: str

    def __init__(self, bigquery_table: _Optional[str]=..., gcs_uri: _Optional[str]=...) -> None:
        ...

class OutputConfig(_message.Message):
    __slots__ = ('bigquery_dataset',)
    BIGQUERY_DATASET_FIELD_NUMBER: _ClassVar[int]
    bigquery_dataset: str

    def __init__(self, bigquery_dataset: _Optional[str]=...) -> None:
        ...

class ReconConfig(_message.Message):
    __slots__ = ('connected_components_config', 'affinity_clustering_config', 'options', 'model_config')

    class Options(_message.Message):
        __slots__ = ('enable_geocoding_separation',)
        ENABLE_GEOCODING_SEPARATION_FIELD_NUMBER: _ClassVar[int]
        enable_geocoding_separation: bool

        def __init__(self, enable_geocoding_separation: bool=...) -> None:
            ...

    class ModelConfig(_message.Message):
        __slots__ = ('model_name', 'version_tag')
        MODEL_NAME_FIELD_NUMBER: _ClassVar[int]
        VERSION_TAG_FIELD_NUMBER: _ClassVar[int]
        model_name: str
        version_tag: str

        def __init__(self, model_name: _Optional[str]=..., version_tag: _Optional[str]=...) -> None:
            ...
    CONNECTED_COMPONENTS_CONFIG_FIELD_NUMBER: _ClassVar[int]
    AFFINITY_CLUSTERING_CONFIG_FIELD_NUMBER: _ClassVar[int]
    OPTIONS_FIELD_NUMBER: _ClassVar[int]
    MODEL_CONFIG_FIELD_NUMBER: _ClassVar[int]
    connected_components_config: ConnectedComponentsConfig
    affinity_clustering_config: AffinityClusteringConfig
    options: ReconConfig.Options
    model_config: ReconConfig.ModelConfig

    def __init__(self, connected_components_config: _Optional[_Union[ConnectedComponentsConfig, _Mapping]]=..., affinity_clustering_config: _Optional[_Union[AffinityClusteringConfig, _Mapping]]=..., options: _Optional[_Union[ReconConfig.Options, _Mapping]]=..., model_config: _Optional[_Union[ReconConfig.ModelConfig, _Mapping]]=...) -> None:
        ...

class ConnectedComponentsConfig(_message.Message):
    __slots__ = ('weight_threshold',)
    WEIGHT_THRESHOLD_FIELD_NUMBER: _ClassVar[int]
    weight_threshold: float

    def __init__(self, weight_threshold: _Optional[float]=...) -> None:
        ...

class AffinityClusteringConfig(_message.Message):
    __slots__ = ('compression_round_count',)
    COMPRESSION_ROUND_COUNT_FIELD_NUMBER: _ClassVar[int]
    compression_round_count: int

    def __init__(self, compression_round_count: _Optional[int]=...) -> None:
        ...

class DeleteOperationMetadata(_message.Message):
    __slots__ = ('common_metadata',)
    COMMON_METADATA_FIELD_NUMBER: _ClassVar[int]
    common_metadata: _operation_metadata_pb2.CommonOperationMetadata

    def __init__(self, common_metadata: _Optional[_Union[_operation_metadata_pb2.CommonOperationMetadata, _Mapping]]=...) -> None:
        ...

class CreateEntityReconciliationJobRequest(_message.Message):
    __slots__ = ('parent', 'entity_reconciliation_job')
    PARENT_FIELD_NUMBER: _ClassVar[int]
    ENTITY_RECONCILIATION_JOB_FIELD_NUMBER: _ClassVar[int]
    parent: str
    entity_reconciliation_job: EntityReconciliationJob

    def __init__(self, parent: _Optional[str]=..., entity_reconciliation_job: _Optional[_Union[EntityReconciliationJob, _Mapping]]=...) -> None:
        ...

class GetEntityReconciliationJobRequest(_message.Message):
    __slots__ = ('name',)
    NAME_FIELD_NUMBER: _ClassVar[int]
    name: str

    def __init__(self, name: _Optional[str]=...) -> None:
        ...

class ListEntityReconciliationJobsRequest(_message.Message):
    __slots__ = ('parent', 'filter', 'page_size', 'page_token')
    PARENT_FIELD_NUMBER: _ClassVar[int]
    FILTER_FIELD_NUMBER: _ClassVar[int]
    PAGE_SIZE_FIELD_NUMBER: _ClassVar[int]
    PAGE_TOKEN_FIELD_NUMBER: _ClassVar[int]
    parent: str
    filter: str
    page_size: int
    page_token: str

    def __init__(self, parent: _Optional[str]=..., filter: _Optional[str]=..., page_size: _Optional[int]=..., page_token: _Optional[str]=...) -> None:
        ...

class ListEntityReconciliationJobsResponse(_message.Message):
    __slots__ = ('entity_reconciliation_jobs', 'next_page_token')
    ENTITY_RECONCILIATION_JOBS_FIELD_NUMBER: _ClassVar[int]
    NEXT_PAGE_TOKEN_FIELD_NUMBER: _ClassVar[int]
    entity_reconciliation_jobs: _containers.RepeatedCompositeFieldContainer[EntityReconciliationJob]
    next_page_token: str

    def __init__(self, entity_reconciliation_jobs: _Optional[_Iterable[_Union[EntityReconciliationJob, _Mapping]]]=..., next_page_token: _Optional[str]=...) -> None:
        ...

class CancelEntityReconciliationJobRequest(_message.Message):
    __slots__ = ('name',)
    NAME_FIELD_NUMBER: _ClassVar[int]
    name: str

    def __init__(self, name: _Optional[str]=...) -> None:
        ...

class DeleteEntityReconciliationJobRequest(_message.Message):
    __slots__ = ('name',)
    NAME_FIELD_NUMBER: _ClassVar[int]
    name: str

    def __init__(self, name: _Optional[str]=...) -> None:
        ...

class EntityReconciliationJob(_message.Message):
    __slots__ = ('name', 'input_config', 'output_config', 'state', 'error', 'create_time', 'end_time', 'update_time', 'recon_config')
    NAME_FIELD_NUMBER: _ClassVar[int]
    INPUT_CONFIG_FIELD_NUMBER: _ClassVar[int]
    OUTPUT_CONFIG_FIELD_NUMBER: _ClassVar[int]
    STATE_FIELD_NUMBER: _ClassVar[int]
    ERROR_FIELD_NUMBER: _ClassVar[int]
    CREATE_TIME_FIELD_NUMBER: _ClassVar[int]
    END_TIME_FIELD_NUMBER: _ClassVar[int]
    UPDATE_TIME_FIELD_NUMBER: _ClassVar[int]
    RECON_CONFIG_FIELD_NUMBER: _ClassVar[int]
    name: str
    input_config: InputConfig
    output_config: OutputConfig
    state: _job_state_pb2.JobState
    error: _status_pb2.Status
    create_time: _timestamp_pb2.Timestamp
    end_time: _timestamp_pb2.Timestamp
    update_time: _timestamp_pb2.Timestamp
    recon_config: ReconConfig

    def __init__(self, name: _Optional[str]=..., input_config: _Optional[_Union[InputConfig, _Mapping]]=..., output_config: _Optional[_Union[OutputConfig, _Mapping]]=..., state: _Optional[_Union[_job_state_pb2.JobState, str]]=..., error: _Optional[_Union[_status_pb2.Status, _Mapping]]=..., create_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]]=..., end_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]]=..., update_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]]=..., recon_config: _Optional[_Union[ReconConfig, _Mapping]]=...) -> None:
        ...

class LookupRequest(_message.Message):
    __slots__ = ('parent', 'ids', 'languages')
    PARENT_FIELD_NUMBER: _ClassVar[int]
    IDS_FIELD_NUMBER: _ClassVar[int]
    LANGUAGES_FIELD_NUMBER: _ClassVar[int]
    parent: str
    ids: _containers.RepeatedScalarFieldContainer[str]
    languages: _containers.RepeatedScalarFieldContainer[str]

    def __init__(self, parent: _Optional[str]=..., ids: _Optional[_Iterable[str]]=..., languages: _Optional[_Iterable[str]]=...) -> None:
        ...

class LookupResponse(_message.Message):
    __slots__ = ('context', 'type', 'item_list_element')
    CONTEXT_FIELD_NUMBER: _ClassVar[int]
    TYPE_FIELD_NUMBER: _ClassVar[int]
    ITEM_LIST_ELEMENT_FIELD_NUMBER: _ClassVar[int]
    context: _struct_pb2.Value
    type: _struct_pb2.Value
    item_list_element: _struct_pb2.ListValue

    def __init__(self, context: _Optional[_Union[_struct_pb2.Value, _Mapping]]=..., type: _Optional[_Union[_struct_pb2.Value, _Mapping]]=..., item_list_element: _Optional[_Union[_struct_pb2.ListValue, _Mapping]]=...) -> None:
        ...

class SearchRequest(_message.Message):
    __slots__ = ('parent', 'query', 'languages', 'types', 'limit')
    PARENT_FIELD_NUMBER: _ClassVar[int]
    QUERY_FIELD_NUMBER: _ClassVar[int]
    LANGUAGES_FIELD_NUMBER: _ClassVar[int]
    TYPES_FIELD_NUMBER: _ClassVar[int]
    LIMIT_FIELD_NUMBER: _ClassVar[int]
    parent: str
    query: str
    languages: _containers.RepeatedScalarFieldContainer[str]
    types: _containers.RepeatedScalarFieldContainer[str]
    limit: _wrappers_pb2.Int32Value

    def __init__(self, parent: _Optional[str]=..., query: _Optional[str]=..., languages: _Optional[_Iterable[str]]=..., types: _Optional[_Iterable[str]]=..., limit: _Optional[_Union[_wrappers_pb2.Int32Value, _Mapping]]=...) -> None:
        ...

class SearchResponse(_message.Message):
    __slots__ = ('context', 'type', 'item_list_element')
    CONTEXT_FIELD_NUMBER: _ClassVar[int]
    TYPE_FIELD_NUMBER: _ClassVar[int]
    ITEM_LIST_ELEMENT_FIELD_NUMBER: _ClassVar[int]
    context: _struct_pb2.Value
    type: _struct_pb2.Value
    item_list_element: _struct_pb2.ListValue

    def __init__(self, context: _Optional[_Union[_struct_pb2.Value, _Mapping]]=..., type: _Optional[_Union[_struct_pb2.Value, _Mapping]]=..., item_list_element: _Optional[_Union[_struct_pb2.ListValue, _Mapping]]=...) -> None:
        ...

class LookupPublicKgRequest(_message.Message):
    __slots__ = ('parent', 'ids', 'languages')
    PARENT_FIELD_NUMBER: _ClassVar[int]
    IDS_FIELD_NUMBER: _ClassVar[int]
    LANGUAGES_FIELD_NUMBER: _ClassVar[int]
    parent: str
    ids: _containers.RepeatedScalarFieldContainer[str]
    languages: _containers.RepeatedScalarFieldContainer[str]

    def __init__(self, parent: _Optional[str]=..., ids: _Optional[_Iterable[str]]=..., languages: _Optional[_Iterable[str]]=...) -> None:
        ...

class LookupPublicKgResponse(_message.Message):
    __slots__ = ('context', 'type', 'item_list_element')
    CONTEXT_FIELD_NUMBER: _ClassVar[int]
    TYPE_FIELD_NUMBER: _ClassVar[int]
    ITEM_LIST_ELEMENT_FIELD_NUMBER: _ClassVar[int]
    context: _struct_pb2.Value
    type: _struct_pb2.Value
    item_list_element: _struct_pb2.ListValue

    def __init__(self, context: _Optional[_Union[_struct_pb2.Value, _Mapping]]=..., type: _Optional[_Union[_struct_pb2.Value, _Mapping]]=..., item_list_element: _Optional[_Union[_struct_pb2.ListValue, _Mapping]]=...) -> None:
        ...

class SearchPublicKgRequest(_message.Message):
    __slots__ = ('parent', 'query', 'languages', 'types', 'limit')
    PARENT_FIELD_NUMBER: _ClassVar[int]
    QUERY_FIELD_NUMBER: _ClassVar[int]
    LANGUAGES_FIELD_NUMBER: _ClassVar[int]
    TYPES_FIELD_NUMBER: _ClassVar[int]
    LIMIT_FIELD_NUMBER: _ClassVar[int]
    parent: str
    query: str
    languages: _containers.RepeatedScalarFieldContainer[str]
    types: _containers.RepeatedScalarFieldContainer[str]
    limit: _wrappers_pb2.Int32Value

    def __init__(self, parent: _Optional[str]=..., query: _Optional[str]=..., languages: _Optional[_Iterable[str]]=..., types: _Optional[_Iterable[str]]=..., limit: _Optional[_Union[_wrappers_pb2.Int32Value, _Mapping]]=...) -> None:
        ...

class SearchPublicKgResponse(_message.Message):
    __slots__ = ('context', 'type', 'item_list_element')
    CONTEXT_FIELD_NUMBER: _ClassVar[int]
    TYPE_FIELD_NUMBER: _ClassVar[int]
    ITEM_LIST_ELEMENT_FIELD_NUMBER: _ClassVar[int]
    context: _struct_pb2.Value
    type: _struct_pb2.Value
    item_list_element: _struct_pb2.ListValue

    def __init__(self, context: _Optional[_Union[_struct_pb2.Value, _Mapping]]=..., type: _Optional[_Union[_struct_pb2.Value, _Mapping]]=..., item_list_element: _Optional[_Union[_struct_pb2.ListValue, _Mapping]]=...) -> None:
        ...