from google.api import annotations_pb2 as _annotations_pb2
from google.api import client_pb2 as _client_pb2
from google.api import field_behavior_pb2 as _field_behavior_pb2
from google.rpc import status_pb2 as _status_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union
DESCRIPTOR: _descriptor.FileDescriptor

class GenerateShareablePreviewsRequest(_message.Message):
    __slots__ = ('customer_id', 'shareable_previews')
    CUSTOMER_ID_FIELD_NUMBER: _ClassVar[int]
    SHAREABLE_PREVIEWS_FIELD_NUMBER: _ClassVar[int]
    customer_id: str
    shareable_previews: _containers.RepeatedCompositeFieldContainer[ShareablePreview]

    def __init__(self, customer_id: _Optional[str]=..., shareable_previews: _Optional[_Iterable[_Union[ShareablePreview, _Mapping]]]=...) -> None:
        ...

class ShareablePreview(_message.Message):
    __slots__ = ('asset_group_identifier',)
    ASSET_GROUP_IDENTIFIER_FIELD_NUMBER: _ClassVar[int]
    asset_group_identifier: AssetGroupIdentifier

    def __init__(self, asset_group_identifier: _Optional[_Union[AssetGroupIdentifier, _Mapping]]=...) -> None:
        ...

class AssetGroupIdentifier(_message.Message):
    __slots__ = ('asset_group_id',)
    ASSET_GROUP_ID_FIELD_NUMBER: _ClassVar[int]
    asset_group_id: int

    def __init__(self, asset_group_id: _Optional[int]=...) -> None:
        ...

class GenerateShareablePreviewsResponse(_message.Message):
    __slots__ = ('responses',)
    RESPONSES_FIELD_NUMBER: _ClassVar[int]
    responses: _containers.RepeatedCompositeFieldContainer[ShareablePreviewOrError]

    def __init__(self, responses: _Optional[_Iterable[_Union[ShareablePreviewOrError, _Mapping]]]=...) -> None:
        ...

class ShareablePreviewOrError(_message.Message):
    __slots__ = ('asset_group_identifier', 'shareable_preview_result', 'partial_failure_error')
    ASSET_GROUP_IDENTIFIER_FIELD_NUMBER: _ClassVar[int]
    SHAREABLE_PREVIEW_RESULT_FIELD_NUMBER: _ClassVar[int]
    PARTIAL_FAILURE_ERROR_FIELD_NUMBER: _ClassVar[int]
    asset_group_identifier: AssetGroupIdentifier
    shareable_preview_result: ShareablePreviewResult
    partial_failure_error: _status_pb2.Status

    def __init__(self, asset_group_identifier: _Optional[_Union[AssetGroupIdentifier, _Mapping]]=..., shareable_preview_result: _Optional[_Union[ShareablePreviewResult, _Mapping]]=..., partial_failure_error: _Optional[_Union[_status_pb2.Status, _Mapping]]=...) -> None:
        ...

class ShareablePreviewResult(_message.Message):
    __slots__ = ('shareable_preview_url', 'expiration_date_time')
    SHAREABLE_PREVIEW_URL_FIELD_NUMBER: _ClassVar[int]
    EXPIRATION_DATE_TIME_FIELD_NUMBER: _ClassVar[int]
    shareable_preview_url: str
    expiration_date_time: str

    def __init__(self, shareable_preview_url: _Optional[str]=..., expiration_date_time: _Optional[str]=...) -> None:
        ...