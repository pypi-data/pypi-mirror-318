from google.ads.googleads.v18.enums import response_content_type_pb2 as _response_content_type_pb2
from google.ads.googleads.v18.resources import campaign_asset_pb2 as _campaign_asset_pb2
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

class MutateCampaignAssetsRequest(_message.Message):
    __slots__ = ("customer_id", "operations", "partial_failure", "validate_only", "response_content_type")
    CUSTOMER_ID_FIELD_NUMBER: _ClassVar[int]
    OPERATIONS_FIELD_NUMBER: _ClassVar[int]
    PARTIAL_FAILURE_FIELD_NUMBER: _ClassVar[int]
    VALIDATE_ONLY_FIELD_NUMBER: _ClassVar[int]
    RESPONSE_CONTENT_TYPE_FIELD_NUMBER: _ClassVar[int]
    customer_id: str
    operations: _containers.RepeatedCompositeFieldContainer[CampaignAssetOperation]
    partial_failure: bool
    validate_only: bool
    response_content_type: _response_content_type_pb2.ResponseContentTypeEnum.ResponseContentType
    def __init__(self, customer_id: _Optional[str] = ..., operations: _Optional[_Iterable[_Union[CampaignAssetOperation, _Mapping]]] = ..., partial_failure: bool = ..., validate_only: bool = ..., response_content_type: _Optional[_Union[_response_content_type_pb2.ResponseContentTypeEnum.ResponseContentType, str]] = ...) -> None: ...

class CampaignAssetOperation(_message.Message):
    __slots__ = ("update_mask", "create", "update", "remove")
    UPDATE_MASK_FIELD_NUMBER: _ClassVar[int]
    CREATE_FIELD_NUMBER: _ClassVar[int]
    UPDATE_FIELD_NUMBER: _ClassVar[int]
    REMOVE_FIELD_NUMBER: _ClassVar[int]
    update_mask: _field_mask_pb2.FieldMask
    create: _campaign_asset_pb2.CampaignAsset
    update: _campaign_asset_pb2.CampaignAsset
    remove: str
    def __init__(self, update_mask: _Optional[_Union[_field_mask_pb2.FieldMask, _Mapping]] = ..., create: _Optional[_Union[_campaign_asset_pb2.CampaignAsset, _Mapping]] = ..., update: _Optional[_Union[_campaign_asset_pb2.CampaignAsset, _Mapping]] = ..., remove: _Optional[str] = ...) -> None: ...

class MutateCampaignAssetsResponse(_message.Message):
    __slots__ = ("partial_failure_error", "results")
    PARTIAL_FAILURE_ERROR_FIELD_NUMBER: _ClassVar[int]
    RESULTS_FIELD_NUMBER: _ClassVar[int]
    partial_failure_error: _status_pb2.Status
    results: _containers.RepeatedCompositeFieldContainer[MutateCampaignAssetResult]
    def __init__(self, partial_failure_error: _Optional[_Union[_status_pb2.Status, _Mapping]] = ..., results: _Optional[_Iterable[_Union[MutateCampaignAssetResult, _Mapping]]] = ...) -> None: ...

class MutateCampaignAssetResult(_message.Message):
    __slots__ = ("resource_name", "campaign_asset")
    RESOURCE_NAME_FIELD_NUMBER: _ClassVar[int]
    CAMPAIGN_ASSET_FIELD_NUMBER: _ClassVar[int]
    resource_name: str
    campaign_asset: _campaign_asset_pb2.CampaignAsset
    def __init__(self, resource_name: _Optional[str] = ..., campaign_asset: _Optional[_Union[_campaign_asset_pb2.CampaignAsset, _Mapping]] = ...) -> None: ...
