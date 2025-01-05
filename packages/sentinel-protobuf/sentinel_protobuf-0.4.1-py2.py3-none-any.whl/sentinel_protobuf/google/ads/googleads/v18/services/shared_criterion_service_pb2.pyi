from google.ads.googleads.v18.enums import response_content_type_pb2 as _response_content_type_pb2
from google.ads.googleads.v18.resources import shared_criterion_pb2 as _shared_criterion_pb2
from google.api import annotations_pb2 as _annotations_pb2
from google.api import client_pb2 as _client_pb2
from google.api import field_behavior_pb2 as _field_behavior_pb2
from google.api import resource_pb2 as _resource_pb2
from google.rpc import status_pb2 as _status_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class MutateSharedCriteriaRequest(_message.Message):
    __slots__ = ("customer_id", "operations", "partial_failure", "validate_only", "response_content_type")
    CUSTOMER_ID_FIELD_NUMBER: _ClassVar[int]
    OPERATIONS_FIELD_NUMBER: _ClassVar[int]
    PARTIAL_FAILURE_FIELD_NUMBER: _ClassVar[int]
    VALIDATE_ONLY_FIELD_NUMBER: _ClassVar[int]
    RESPONSE_CONTENT_TYPE_FIELD_NUMBER: _ClassVar[int]
    customer_id: str
    operations: _containers.RepeatedCompositeFieldContainer[SharedCriterionOperation]
    partial_failure: bool
    validate_only: bool
    response_content_type: _response_content_type_pb2.ResponseContentTypeEnum.ResponseContentType
    def __init__(self, customer_id: _Optional[str] = ..., operations: _Optional[_Iterable[_Union[SharedCriterionOperation, _Mapping]]] = ..., partial_failure: bool = ..., validate_only: bool = ..., response_content_type: _Optional[_Union[_response_content_type_pb2.ResponseContentTypeEnum.ResponseContentType, str]] = ...) -> None: ...

class SharedCriterionOperation(_message.Message):
    __slots__ = ("create", "remove")
    CREATE_FIELD_NUMBER: _ClassVar[int]
    REMOVE_FIELD_NUMBER: _ClassVar[int]
    create: _shared_criterion_pb2.SharedCriterion
    remove: str
    def __init__(self, create: _Optional[_Union[_shared_criterion_pb2.SharedCriterion, _Mapping]] = ..., remove: _Optional[str] = ...) -> None: ...

class MutateSharedCriteriaResponse(_message.Message):
    __slots__ = ("partial_failure_error", "results")
    PARTIAL_FAILURE_ERROR_FIELD_NUMBER: _ClassVar[int]
    RESULTS_FIELD_NUMBER: _ClassVar[int]
    partial_failure_error: _status_pb2.Status
    results: _containers.RepeatedCompositeFieldContainer[MutateSharedCriterionResult]
    def __init__(self, partial_failure_error: _Optional[_Union[_status_pb2.Status, _Mapping]] = ..., results: _Optional[_Iterable[_Union[MutateSharedCriterionResult, _Mapping]]] = ...) -> None: ...

class MutateSharedCriterionResult(_message.Message):
    __slots__ = ("resource_name", "shared_criterion")
    RESOURCE_NAME_FIELD_NUMBER: _ClassVar[int]
    SHARED_CRITERION_FIELD_NUMBER: _ClassVar[int]
    resource_name: str
    shared_criterion: _shared_criterion_pb2.SharedCriterion
    def __init__(self, resource_name: _Optional[str] = ..., shared_criterion: _Optional[_Union[_shared_criterion_pb2.SharedCriterion, _Mapping]] = ...) -> None: ...
