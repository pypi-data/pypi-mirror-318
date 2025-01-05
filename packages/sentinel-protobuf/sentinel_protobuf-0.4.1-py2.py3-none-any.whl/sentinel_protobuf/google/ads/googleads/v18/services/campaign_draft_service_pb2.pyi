from google.ads.googleads.v18.enums import response_content_type_pb2 as _response_content_type_pb2
from google.ads.googleads.v18.resources import campaign_draft_pb2 as _campaign_draft_pb2
from google.api import annotations_pb2 as _annotations_pb2
from google.api import client_pb2 as _client_pb2
from google.api import field_behavior_pb2 as _field_behavior_pb2
from google.api import resource_pb2 as _resource_pb2
from google.longrunning import operations_pb2 as _operations_pb2
from google.protobuf import empty_pb2 as _empty_pb2
from google.protobuf import field_mask_pb2 as _field_mask_pb2
from google.rpc import status_pb2 as _status_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class MutateCampaignDraftsRequest(_message.Message):
    __slots__ = ("customer_id", "operations", "partial_failure", "validate_only", "response_content_type")
    CUSTOMER_ID_FIELD_NUMBER: _ClassVar[int]
    OPERATIONS_FIELD_NUMBER: _ClassVar[int]
    PARTIAL_FAILURE_FIELD_NUMBER: _ClassVar[int]
    VALIDATE_ONLY_FIELD_NUMBER: _ClassVar[int]
    RESPONSE_CONTENT_TYPE_FIELD_NUMBER: _ClassVar[int]
    customer_id: str
    operations: _containers.RepeatedCompositeFieldContainer[CampaignDraftOperation]
    partial_failure: bool
    validate_only: bool
    response_content_type: _response_content_type_pb2.ResponseContentTypeEnum.ResponseContentType
    def __init__(self, customer_id: _Optional[str] = ..., operations: _Optional[_Iterable[_Union[CampaignDraftOperation, _Mapping]]] = ..., partial_failure: bool = ..., validate_only: bool = ..., response_content_type: _Optional[_Union[_response_content_type_pb2.ResponseContentTypeEnum.ResponseContentType, str]] = ...) -> None: ...

class PromoteCampaignDraftRequest(_message.Message):
    __slots__ = ("campaign_draft", "validate_only")
    CAMPAIGN_DRAFT_FIELD_NUMBER: _ClassVar[int]
    VALIDATE_ONLY_FIELD_NUMBER: _ClassVar[int]
    campaign_draft: str
    validate_only: bool
    def __init__(self, campaign_draft: _Optional[str] = ..., validate_only: bool = ...) -> None: ...

class CampaignDraftOperation(_message.Message):
    __slots__ = ("update_mask", "create", "update", "remove")
    UPDATE_MASK_FIELD_NUMBER: _ClassVar[int]
    CREATE_FIELD_NUMBER: _ClassVar[int]
    UPDATE_FIELD_NUMBER: _ClassVar[int]
    REMOVE_FIELD_NUMBER: _ClassVar[int]
    update_mask: _field_mask_pb2.FieldMask
    create: _campaign_draft_pb2.CampaignDraft
    update: _campaign_draft_pb2.CampaignDraft
    remove: str
    def __init__(self, update_mask: _Optional[_Union[_field_mask_pb2.FieldMask, _Mapping]] = ..., create: _Optional[_Union[_campaign_draft_pb2.CampaignDraft, _Mapping]] = ..., update: _Optional[_Union[_campaign_draft_pb2.CampaignDraft, _Mapping]] = ..., remove: _Optional[str] = ...) -> None: ...

class MutateCampaignDraftsResponse(_message.Message):
    __slots__ = ("partial_failure_error", "results")
    PARTIAL_FAILURE_ERROR_FIELD_NUMBER: _ClassVar[int]
    RESULTS_FIELD_NUMBER: _ClassVar[int]
    partial_failure_error: _status_pb2.Status
    results: _containers.RepeatedCompositeFieldContainer[MutateCampaignDraftResult]
    def __init__(self, partial_failure_error: _Optional[_Union[_status_pb2.Status, _Mapping]] = ..., results: _Optional[_Iterable[_Union[MutateCampaignDraftResult, _Mapping]]] = ...) -> None: ...

class MutateCampaignDraftResult(_message.Message):
    __slots__ = ("resource_name", "campaign_draft")
    RESOURCE_NAME_FIELD_NUMBER: _ClassVar[int]
    CAMPAIGN_DRAFT_FIELD_NUMBER: _ClassVar[int]
    resource_name: str
    campaign_draft: _campaign_draft_pb2.CampaignDraft
    def __init__(self, resource_name: _Optional[str] = ..., campaign_draft: _Optional[_Union[_campaign_draft_pb2.CampaignDraft, _Mapping]] = ...) -> None: ...

class ListCampaignDraftAsyncErrorsRequest(_message.Message):
    __slots__ = ("resource_name", "page_token", "page_size")
    RESOURCE_NAME_FIELD_NUMBER: _ClassVar[int]
    PAGE_TOKEN_FIELD_NUMBER: _ClassVar[int]
    PAGE_SIZE_FIELD_NUMBER: _ClassVar[int]
    resource_name: str
    page_token: str
    page_size: int
    def __init__(self, resource_name: _Optional[str] = ..., page_token: _Optional[str] = ..., page_size: _Optional[int] = ...) -> None: ...

class ListCampaignDraftAsyncErrorsResponse(_message.Message):
    __slots__ = ("errors", "next_page_token")
    ERRORS_FIELD_NUMBER: _ClassVar[int]
    NEXT_PAGE_TOKEN_FIELD_NUMBER: _ClassVar[int]
    errors: _containers.RepeatedCompositeFieldContainer[_status_pb2.Status]
    next_page_token: str
    def __init__(self, errors: _Optional[_Iterable[_Union[_status_pb2.Status, _Mapping]]] = ..., next_page_token: _Optional[str] = ...) -> None: ...
