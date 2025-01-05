from google.ads.googleads.v17.enums import asset_field_type_pb2 as _asset_field_type_pb2
from google.ads.googleads.v17.enums import call_to_action_type_pb2 as _call_to_action_type_pb2
from google.ads.googleads.v17.enums import hotel_asset_suggestion_status_pb2 as _hotel_asset_suggestion_status_pb2
from google.api import annotations_pb2 as _annotations_pb2
from google.api import client_pb2 as _client_pb2
from google.api import field_behavior_pb2 as _field_behavior_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union
DESCRIPTOR: _descriptor.FileDescriptor

class SuggestTravelAssetsRequest(_message.Message):
    __slots__ = ('customer_id', 'language_option', 'place_ids')
    CUSTOMER_ID_FIELD_NUMBER: _ClassVar[int]
    LANGUAGE_OPTION_FIELD_NUMBER: _ClassVar[int]
    PLACE_IDS_FIELD_NUMBER: _ClassVar[int]
    customer_id: str
    language_option: str
    place_ids: _containers.RepeatedScalarFieldContainer[str]

    def __init__(self, customer_id: _Optional[str]=..., language_option: _Optional[str]=..., place_ids: _Optional[_Iterable[str]]=...) -> None:
        ...

class SuggestTravelAssetsResponse(_message.Message):
    __slots__ = ('hotel_asset_suggestions',)
    HOTEL_ASSET_SUGGESTIONS_FIELD_NUMBER: _ClassVar[int]
    hotel_asset_suggestions: _containers.RepeatedCompositeFieldContainer[HotelAssetSuggestion]

    def __init__(self, hotel_asset_suggestions: _Optional[_Iterable[_Union[HotelAssetSuggestion, _Mapping]]]=...) -> None:
        ...

class HotelAssetSuggestion(_message.Message):
    __slots__ = ('place_id', 'final_url', 'hotel_name', 'call_to_action', 'text_assets', 'image_assets', 'status')
    PLACE_ID_FIELD_NUMBER: _ClassVar[int]
    FINAL_URL_FIELD_NUMBER: _ClassVar[int]
    HOTEL_NAME_FIELD_NUMBER: _ClassVar[int]
    CALL_TO_ACTION_FIELD_NUMBER: _ClassVar[int]
    TEXT_ASSETS_FIELD_NUMBER: _ClassVar[int]
    IMAGE_ASSETS_FIELD_NUMBER: _ClassVar[int]
    STATUS_FIELD_NUMBER: _ClassVar[int]
    place_id: str
    final_url: str
    hotel_name: str
    call_to_action: _call_to_action_type_pb2.CallToActionTypeEnum.CallToActionType
    text_assets: _containers.RepeatedCompositeFieldContainer[HotelTextAsset]
    image_assets: _containers.RepeatedCompositeFieldContainer[HotelImageAsset]
    status: _hotel_asset_suggestion_status_pb2.HotelAssetSuggestionStatusEnum.HotelAssetSuggestionStatus

    def __init__(self, place_id: _Optional[str]=..., final_url: _Optional[str]=..., hotel_name: _Optional[str]=..., call_to_action: _Optional[_Union[_call_to_action_type_pb2.CallToActionTypeEnum.CallToActionType, str]]=..., text_assets: _Optional[_Iterable[_Union[HotelTextAsset, _Mapping]]]=..., image_assets: _Optional[_Iterable[_Union[HotelImageAsset, _Mapping]]]=..., status: _Optional[_Union[_hotel_asset_suggestion_status_pb2.HotelAssetSuggestionStatusEnum.HotelAssetSuggestionStatus, str]]=...) -> None:
        ...

class HotelTextAsset(_message.Message):
    __slots__ = ('text', 'asset_field_type')
    TEXT_FIELD_NUMBER: _ClassVar[int]
    ASSET_FIELD_TYPE_FIELD_NUMBER: _ClassVar[int]
    text: str
    asset_field_type: _asset_field_type_pb2.AssetFieldTypeEnum.AssetFieldType

    def __init__(self, text: _Optional[str]=..., asset_field_type: _Optional[_Union[_asset_field_type_pb2.AssetFieldTypeEnum.AssetFieldType, str]]=...) -> None:
        ...

class HotelImageAsset(_message.Message):
    __slots__ = ('uri', 'asset_field_type')
    URI_FIELD_NUMBER: _ClassVar[int]
    ASSET_FIELD_TYPE_FIELD_NUMBER: _ClassVar[int]
    uri: str
    asset_field_type: _asset_field_type_pb2.AssetFieldTypeEnum.AssetFieldType

    def __init__(self, uri: _Optional[str]=..., asset_field_type: _Optional[_Union[_asset_field_type_pb2.AssetFieldTypeEnum.AssetFieldType, str]]=...) -> None:
        ...