from google.ads.googleads.v16.enums import response_content_type_pb2 as _response_content_type_pb2
from google.ads.googleads.v16.resources import ad_group_criterion_customizer_pb2 as _ad_group_criterion_customizer_pb2
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

class MutateAdGroupCriterionCustomizersRequest(_message.Message):
    __slots__ = ("customer_id", "operations", "partial_failure", "validate_only", "response_content_type")
    CUSTOMER_ID_FIELD_NUMBER: _ClassVar[int]
    OPERATIONS_FIELD_NUMBER: _ClassVar[int]
    PARTIAL_FAILURE_FIELD_NUMBER: _ClassVar[int]
    VALIDATE_ONLY_FIELD_NUMBER: _ClassVar[int]
    RESPONSE_CONTENT_TYPE_FIELD_NUMBER: _ClassVar[int]
    customer_id: str
    operations: _containers.RepeatedCompositeFieldContainer[AdGroupCriterionCustomizerOperation]
    partial_failure: bool
    validate_only: bool
    response_content_type: _response_content_type_pb2.ResponseContentTypeEnum.ResponseContentType
    def __init__(self, customer_id: _Optional[str] = ..., operations: _Optional[_Iterable[_Union[AdGroupCriterionCustomizerOperation, _Mapping]]] = ..., partial_failure: bool = ..., validate_only: bool = ..., response_content_type: _Optional[_Union[_response_content_type_pb2.ResponseContentTypeEnum.ResponseContentType, str]] = ...) -> None: ...

class AdGroupCriterionCustomizerOperation(_message.Message):
    __slots__ = ("create", "remove")
    CREATE_FIELD_NUMBER: _ClassVar[int]
    REMOVE_FIELD_NUMBER: _ClassVar[int]
    create: _ad_group_criterion_customizer_pb2.AdGroupCriterionCustomizer
    remove: str
    def __init__(self, create: _Optional[_Union[_ad_group_criterion_customizer_pb2.AdGroupCriterionCustomizer, _Mapping]] = ..., remove: _Optional[str] = ...) -> None: ...

class MutateAdGroupCriterionCustomizersResponse(_message.Message):
    __slots__ = ("results", "partial_failure_error")
    RESULTS_FIELD_NUMBER: _ClassVar[int]
    PARTIAL_FAILURE_ERROR_FIELD_NUMBER: _ClassVar[int]
    results: _containers.RepeatedCompositeFieldContainer[MutateAdGroupCriterionCustomizerResult]
    partial_failure_error: _status_pb2.Status
    def __init__(self, results: _Optional[_Iterable[_Union[MutateAdGroupCriterionCustomizerResult, _Mapping]]] = ..., partial_failure_error: _Optional[_Union[_status_pb2.Status, _Mapping]] = ...) -> None: ...

class MutateAdGroupCriterionCustomizerResult(_message.Message):
    __slots__ = ("resource_name", "ad_group_criterion_customizer")
    RESOURCE_NAME_FIELD_NUMBER: _ClassVar[int]
    AD_GROUP_CRITERION_CUSTOMIZER_FIELD_NUMBER: _ClassVar[int]
    resource_name: str
    ad_group_criterion_customizer: _ad_group_criterion_customizer_pb2.AdGroupCriterionCustomizer
    def __init__(self, resource_name: _Optional[str] = ..., ad_group_criterion_customizer: _Optional[_Union[_ad_group_criterion_customizer_pb2.AdGroupCriterionCustomizer, _Mapping]] = ...) -> None: ...
