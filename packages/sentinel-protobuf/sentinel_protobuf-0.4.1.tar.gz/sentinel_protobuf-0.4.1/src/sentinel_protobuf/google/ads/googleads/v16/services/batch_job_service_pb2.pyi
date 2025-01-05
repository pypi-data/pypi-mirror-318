from google.ads.googleads.v16.enums import response_content_type_pb2 as _response_content_type_pb2
from google.ads.googleads.v16.resources import batch_job_pb2 as _batch_job_pb2
from google.ads.googleads.v16.services import google_ads_service_pb2 as _google_ads_service_pb2
from google.api import annotations_pb2 as _annotations_pb2
from google.api import client_pb2 as _client_pb2
from google.api import field_behavior_pb2 as _field_behavior_pb2
from google.api import resource_pb2 as _resource_pb2
from google.longrunning import operations_pb2 as _operations_pb2
from google.protobuf import empty_pb2 as _empty_pb2
from google.rpc import status_pb2 as _status_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class MutateBatchJobRequest(_message.Message):
    __slots__ = ("customer_id", "operation")
    CUSTOMER_ID_FIELD_NUMBER: _ClassVar[int]
    OPERATION_FIELD_NUMBER: _ClassVar[int]
    customer_id: str
    operation: BatchJobOperation
    def __init__(self, customer_id: _Optional[str] = ..., operation: _Optional[_Union[BatchJobOperation, _Mapping]] = ...) -> None: ...

class BatchJobOperation(_message.Message):
    __slots__ = ("create", "remove")
    CREATE_FIELD_NUMBER: _ClassVar[int]
    REMOVE_FIELD_NUMBER: _ClassVar[int]
    create: _batch_job_pb2.BatchJob
    remove: str
    def __init__(self, create: _Optional[_Union[_batch_job_pb2.BatchJob, _Mapping]] = ..., remove: _Optional[str] = ...) -> None: ...

class MutateBatchJobResponse(_message.Message):
    __slots__ = ("result",)
    RESULT_FIELD_NUMBER: _ClassVar[int]
    result: MutateBatchJobResult
    def __init__(self, result: _Optional[_Union[MutateBatchJobResult, _Mapping]] = ...) -> None: ...

class MutateBatchJobResult(_message.Message):
    __slots__ = ("resource_name",)
    RESOURCE_NAME_FIELD_NUMBER: _ClassVar[int]
    resource_name: str
    def __init__(self, resource_name: _Optional[str] = ...) -> None: ...

class RunBatchJobRequest(_message.Message):
    __slots__ = ("resource_name",)
    RESOURCE_NAME_FIELD_NUMBER: _ClassVar[int]
    resource_name: str
    def __init__(self, resource_name: _Optional[str] = ...) -> None: ...

class AddBatchJobOperationsRequest(_message.Message):
    __slots__ = ("resource_name", "sequence_token", "mutate_operations")
    RESOURCE_NAME_FIELD_NUMBER: _ClassVar[int]
    SEQUENCE_TOKEN_FIELD_NUMBER: _ClassVar[int]
    MUTATE_OPERATIONS_FIELD_NUMBER: _ClassVar[int]
    resource_name: str
    sequence_token: str
    mutate_operations: _containers.RepeatedCompositeFieldContainer[_google_ads_service_pb2.MutateOperation]
    def __init__(self, resource_name: _Optional[str] = ..., sequence_token: _Optional[str] = ..., mutate_operations: _Optional[_Iterable[_Union[_google_ads_service_pb2.MutateOperation, _Mapping]]] = ...) -> None: ...

class AddBatchJobOperationsResponse(_message.Message):
    __slots__ = ("total_operations", "next_sequence_token")
    TOTAL_OPERATIONS_FIELD_NUMBER: _ClassVar[int]
    NEXT_SEQUENCE_TOKEN_FIELD_NUMBER: _ClassVar[int]
    total_operations: int
    next_sequence_token: str
    def __init__(self, total_operations: _Optional[int] = ..., next_sequence_token: _Optional[str] = ...) -> None: ...

class ListBatchJobResultsRequest(_message.Message):
    __slots__ = ("resource_name", "page_token", "page_size", "response_content_type")
    RESOURCE_NAME_FIELD_NUMBER: _ClassVar[int]
    PAGE_TOKEN_FIELD_NUMBER: _ClassVar[int]
    PAGE_SIZE_FIELD_NUMBER: _ClassVar[int]
    RESPONSE_CONTENT_TYPE_FIELD_NUMBER: _ClassVar[int]
    resource_name: str
    page_token: str
    page_size: int
    response_content_type: _response_content_type_pb2.ResponseContentTypeEnum.ResponseContentType
    def __init__(self, resource_name: _Optional[str] = ..., page_token: _Optional[str] = ..., page_size: _Optional[int] = ..., response_content_type: _Optional[_Union[_response_content_type_pb2.ResponseContentTypeEnum.ResponseContentType, str]] = ...) -> None: ...

class ListBatchJobResultsResponse(_message.Message):
    __slots__ = ("results", "next_page_token")
    RESULTS_FIELD_NUMBER: _ClassVar[int]
    NEXT_PAGE_TOKEN_FIELD_NUMBER: _ClassVar[int]
    results: _containers.RepeatedCompositeFieldContainer[BatchJobResult]
    next_page_token: str
    def __init__(self, results: _Optional[_Iterable[_Union[BatchJobResult, _Mapping]]] = ..., next_page_token: _Optional[str] = ...) -> None: ...

class BatchJobResult(_message.Message):
    __slots__ = ("operation_index", "mutate_operation_response", "status")
    OPERATION_INDEX_FIELD_NUMBER: _ClassVar[int]
    MUTATE_OPERATION_RESPONSE_FIELD_NUMBER: _ClassVar[int]
    STATUS_FIELD_NUMBER: _ClassVar[int]
    operation_index: int
    mutate_operation_response: _google_ads_service_pb2.MutateOperationResponse
    status: _status_pb2.Status
    def __init__(self, operation_index: _Optional[int] = ..., mutate_operation_response: _Optional[_Union[_google_ads_service_pb2.MutateOperationResponse, _Mapping]] = ..., status: _Optional[_Union[_status_pb2.Status, _Mapping]] = ...) -> None: ...
