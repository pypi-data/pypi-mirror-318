from google.ads.googleads.v18.enums import response_content_type_pb2 as _response_content_type_pb2
from google.ads.googleads.v18.resources import audience_pb2 as _audience_pb2
from google.api import annotations_pb2 as _annotations_pb2
from google.api import client_pb2 as _client_pb2
from google.api import field_behavior_pb2 as _field_behavior_pb2
from google.api import resource_pb2 as _resource_pb2
from google.protobuf import field_mask_pb2 as _field_mask_pb2
from google.rpc import status_pb2 as _status_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class MutateAudiencesRequest(_message.Message):
    __slots__ = ("customer_id", "operations", "partial_failure", "validate_only", "response_content_type")
    CUSTOMER_ID_FIELD_NUMBER: _ClassVar[int]
    OPERATIONS_FIELD_NUMBER: _ClassVar[int]
    PARTIAL_FAILURE_FIELD_NUMBER: _ClassVar[int]
    VALIDATE_ONLY_FIELD_NUMBER: _ClassVar[int]
    RESPONSE_CONTENT_TYPE_FIELD_NUMBER: _ClassVar[int]
    customer_id: str
    operations: _containers.RepeatedCompositeFieldContainer[AudienceOperation]
    partial_failure: bool
    validate_only: bool
    response_content_type: _response_content_type_pb2.ResponseContentTypeEnum.ResponseContentType
    def __init__(self, customer_id: _Optional[str] = ..., operations: _Optional[_Iterable[_Union[AudienceOperation, _Mapping]]] = ..., partial_failure: bool = ..., validate_only: bool = ..., response_content_type: _Optional[_Union[_response_content_type_pb2.ResponseContentTypeEnum.ResponseContentType, str]] = ...) -> None: ...

class MutateAudiencesResponse(_message.Message):
    __slots__ = ("results", "partial_failure_error")
    RESULTS_FIELD_NUMBER: _ClassVar[int]
    PARTIAL_FAILURE_ERROR_FIELD_NUMBER: _ClassVar[int]
    results: _containers.RepeatedCompositeFieldContainer[MutateAudienceResult]
    partial_failure_error: _status_pb2.Status
    def __init__(self, results: _Optional[_Iterable[_Union[MutateAudienceResult, _Mapping]]] = ..., partial_failure_error: _Optional[_Union[_status_pb2.Status, _Mapping]] = ...) -> None: ...

class AudienceOperation(_message.Message):
    __slots__ = ("update_mask", "create", "update")
    UPDATE_MASK_FIELD_NUMBER: _ClassVar[int]
    CREATE_FIELD_NUMBER: _ClassVar[int]
    UPDATE_FIELD_NUMBER: _ClassVar[int]
    update_mask: _field_mask_pb2.FieldMask
    create: _audience_pb2.Audience
    update: _audience_pb2.Audience
    def __init__(self, update_mask: _Optional[_Union[_field_mask_pb2.FieldMask, _Mapping]] = ..., create: _Optional[_Union[_audience_pb2.Audience, _Mapping]] = ..., update: _Optional[_Union[_audience_pb2.Audience, _Mapping]] = ...) -> None: ...

class MutateAudienceResult(_message.Message):
    __slots__ = ("resource_name", "audience")
    RESOURCE_NAME_FIELD_NUMBER: _ClassVar[int]
    AUDIENCE_FIELD_NUMBER: _ClassVar[int]
    resource_name: str
    audience: _audience_pb2.Audience
    def __init__(self, resource_name: _Optional[str] = ..., audience: _Optional[_Union[_audience_pb2.Audience, _Mapping]] = ...) -> None: ...
