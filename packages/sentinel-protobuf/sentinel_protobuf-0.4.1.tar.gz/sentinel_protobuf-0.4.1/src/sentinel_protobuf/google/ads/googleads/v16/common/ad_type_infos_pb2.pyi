from google.ads.googleads.v16.common import ad_asset_pb2 as _ad_asset_pb2
from google.ads.googleads.v16.enums import call_conversion_reporting_state_pb2 as _call_conversion_reporting_state_pb2
from google.ads.googleads.v16.enums import display_ad_format_setting_pb2 as _display_ad_format_setting_pb2
from google.ads.googleads.v16.enums import display_upload_product_type_pb2 as _display_upload_product_type_pb2
from google.ads.googleads.v16.enums import legacy_app_install_ad_app_store_pb2 as _legacy_app_install_ad_app_store_pb2
from google.ads.googleads.v16.enums import mime_type_pb2 as _mime_type_pb2
from google.ads.googleads.v16.enums import video_thumbnail_pb2 as _video_thumbnail_pb2
from google.api import field_behavior_pb2 as _field_behavior_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class TextAdInfo(_message.Message):
    __slots__ = ("headline", "description1", "description2")
    HEADLINE_FIELD_NUMBER: _ClassVar[int]
    DESCRIPTION1_FIELD_NUMBER: _ClassVar[int]
    DESCRIPTION2_FIELD_NUMBER: _ClassVar[int]
    headline: str
    description1: str
    description2: str
    def __init__(self, headline: _Optional[str] = ..., description1: _Optional[str] = ..., description2: _Optional[str] = ...) -> None: ...

class ExpandedTextAdInfo(_message.Message):
    __slots__ = ("headline_part1", "headline_part2", "headline_part3", "description", "description2", "path1", "path2")
    HEADLINE_PART1_FIELD_NUMBER: _ClassVar[int]
    HEADLINE_PART2_FIELD_NUMBER: _ClassVar[int]
    HEADLINE_PART3_FIELD_NUMBER: _ClassVar[int]
    DESCRIPTION_FIELD_NUMBER: _ClassVar[int]
    DESCRIPTION2_FIELD_NUMBER: _ClassVar[int]
    PATH1_FIELD_NUMBER: _ClassVar[int]
    PATH2_FIELD_NUMBER: _ClassVar[int]
    headline_part1: str
    headline_part2: str
    headline_part3: str
    description: str
    description2: str
    path1: str
    path2: str
    def __init__(self, headline_part1: _Optional[str] = ..., headline_part2: _Optional[str] = ..., headline_part3: _Optional[str] = ..., description: _Optional[str] = ..., description2: _Optional[str] = ..., path1: _Optional[str] = ..., path2: _Optional[str] = ...) -> None: ...

class ExpandedDynamicSearchAdInfo(_message.Message):
    __slots__ = ("description", "description2")
    DESCRIPTION_FIELD_NUMBER: _ClassVar[int]
    DESCRIPTION2_FIELD_NUMBER: _ClassVar[int]
    description: str
    description2: str
    def __init__(self, description: _Optional[str] = ..., description2: _Optional[str] = ...) -> None: ...

class HotelAdInfo(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class TravelAdInfo(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class ShoppingSmartAdInfo(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class ShoppingProductAdInfo(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class ShoppingComparisonListingAdInfo(_message.Message):
    __slots__ = ("headline",)
    HEADLINE_FIELD_NUMBER: _ClassVar[int]
    headline: str
    def __init__(self, headline: _Optional[str] = ...) -> None: ...

class ImageAdInfo(_message.Message):
    __slots__ = ("pixel_width", "pixel_height", "image_url", "preview_pixel_width", "preview_pixel_height", "preview_image_url", "mime_type", "name", "image_asset", "data", "ad_id_to_copy_image_from")
    PIXEL_WIDTH_FIELD_NUMBER: _ClassVar[int]
    PIXEL_HEIGHT_FIELD_NUMBER: _ClassVar[int]
    IMAGE_URL_FIELD_NUMBER: _ClassVar[int]
    PREVIEW_PIXEL_WIDTH_FIELD_NUMBER: _ClassVar[int]
    PREVIEW_PIXEL_HEIGHT_FIELD_NUMBER: _ClassVar[int]
    PREVIEW_IMAGE_URL_FIELD_NUMBER: _ClassVar[int]
    MIME_TYPE_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    IMAGE_ASSET_FIELD_NUMBER: _ClassVar[int]
    DATA_FIELD_NUMBER: _ClassVar[int]
    AD_ID_TO_COPY_IMAGE_FROM_FIELD_NUMBER: _ClassVar[int]
    pixel_width: int
    pixel_height: int
    image_url: str
    preview_pixel_width: int
    preview_pixel_height: int
    preview_image_url: str
    mime_type: _mime_type_pb2.MimeTypeEnum.MimeType
    name: str
    image_asset: _ad_asset_pb2.AdImageAsset
    data: bytes
    ad_id_to_copy_image_from: int
    def __init__(self, pixel_width: _Optional[int] = ..., pixel_height: _Optional[int] = ..., image_url: _Optional[str] = ..., preview_pixel_width: _Optional[int] = ..., preview_pixel_height: _Optional[int] = ..., preview_image_url: _Optional[str] = ..., mime_type: _Optional[_Union[_mime_type_pb2.MimeTypeEnum.MimeType, str]] = ..., name: _Optional[str] = ..., image_asset: _Optional[_Union[_ad_asset_pb2.AdImageAsset, _Mapping]] = ..., data: _Optional[bytes] = ..., ad_id_to_copy_image_from: _Optional[int] = ...) -> None: ...

class VideoBumperInStreamAdInfo(_message.Message):
    __slots__ = ("companion_banner", "action_button_label", "action_headline")
    COMPANION_BANNER_FIELD_NUMBER: _ClassVar[int]
    ACTION_BUTTON_LABEL_FIELD_NUMBER: _ClassVar[int]
    ACTION_HEADLINE_FIELD_NUMBER: _ClassVar[int]
    companion_banner: _ad_asset_pb2.AdImageAsset
    action_button_label: str
    action_headline: str
    def __init__(self, companion_banner: _Optional[_Union[_ad_asset_pb2.AdImageAsset, _Mapping]] = ..., action_button_label: _Optional[str] = ..., action_headline: _Optional[str] = ...) -> None: ...

class VideoNonSkippableInStreamAdInfo(_message.Message):
    __slots__ = ("companion_banner", "action_button_label", "action_headline")
    COMPANION_BANNER_FIELD_NUMBER: _ClassVar[int]
    ACTION_BUTTON_LABEL_FIELD_NUMBER: _ClassVar[int]
    ACTION_HEADLINE_FIELD_NUMBER: _ClassVar[int]
    companion_banner: _ad_asset_pb2.AdImageAsset
    action_button_label: str
    action_headline: str
    def __init__(self, companion_banner: _Optional[_Union[_ad_asset_pb2.AdImageAsset, _Mapping]] = ..., action_button_label: _Optional[str] = ..., action_headline: _Optional[str] = ...) -> None: ...

class VideoTrueViewInStreamAdInfo(_message.Message):
    __slots__ = ("action_button_label", "action_headline", "companion_banner")
    ACTION_BUTTON_LABEL_FIELD_NUMBER: _ClassVar[int]
    ACTION_HEADLINE_FIELD_NUMBER: _ClassVar[int]
    COMPANION_BANNER_FIELD_NUMBER: _ClassVar[int]
    action_button_label: str
    action_headline: str
    companion_banner: _ad_asset_pb2.AdImageAsset
    def __init__(self, action_button_label: _Optional[str] = ..., action_headline: _Optional[str] = ..., companion_banner: _Optional[_Union[_ad_asset_pb2.AdImageAsset, _Mapping]] = ...) -> None: ...

class VideoOutstreamAdInfo(_message.Message):
    __slots__ = ("headline", "description")
    HEADLINE_FIELD_NUMBER: _ClassVar[int]
    DESCRIPTION_FIELD_NUMBER: _ClassVar[int]
    headline: str
    description: str
    def __init__(self, headline: _Optional[str] = ..., description: _Optional[str] = ...) -> None: ...

class InFeedVideoAdInfo(_message.Message):
    __slots__ = ("headline", "description1", "description2", "thumbnail")
    HEADLINE_FIELD_NUMBER: _ClassVar[int]
    DESCRIPTION1_FIELD_NUMBER: _ClassVar[int]
    DESCRIPTION2_FIELD_NUMBER: _ClassVar[int]
    THUMBNAIL_FIELD_NUMBER: _ClassVar[int]
    headline: str
    description1: str
    description2: str
    thumbnail: _video_thumbnail_pb2.VideoThumbnailEnum.VideoThumbnail
    def __init__(self, headline: _Optional[str] = ..., description1: _Optional[str] = ..., description2: _Optional[str] = ..., thumbnail: _Optional[_Union[_video_thumbnail_pb2.VideoThumbnailEnum.VideoThumbnail, str]] = ...) -> None: ...

class VideoAdInfo(_message.Message):
    __slots__ = ("video", "in_stream", "bumper", "out_stream", "non_skippable", "in_feed")
    VIDEO_FIELD_NUMBER: _ClassVar[int]
    IN_STREAM_FIELD_NUMBER: _ClassVar[int]
    BUMPER_FIELD_NUMBER: _ClassVar[int]
    OUT_STREAM_FIELD_NUMBER: _ClassVar[int]
    NON_SKIPPABLE_FIELD_NUMBER: _ClassVar[int]
    IN_FEED_FIELD_NUMBER: _ClassVar[int]
    video: _ad_asset_pb2.AdVideoAsset
    in_stream: VideoTrueViewInStreamAdInfo
    bumper: VideoBumperInStreamAdInfo
    out_stream: VideoOutstreamAdInfo
    non_skippable: VideoNonSkippableInStreamAdInfo
    in_feed: InFeedVideoAdInfo
    def __init__(self, video: _Optional[_Union[_ad_asset_pb2.AdVideoAsset, _Mapping]] = ..., in_stream: _Optional[_Union[VideoTrueViewInStreamAdInfo, _Mapping]] = ..., bumper: _Optional[_Union[VideoBumperInStreamAdInfo, _Mapping]] = ..., out_stream: _Optional[_Union[VideoOutstreamAdInfo, _Mapping]] = ..., non_skippable: _Optional[_Union[VideoNonSkippableInStreamAdInfo, _Mapping]] = ..., in_feed: _Optional[_Union[InFeedVideoAdInfo, _Mapping]] = ...) -> None: ...

class VideoResponsiveAdInfo(_message.Message):
    __slots__ = ("headlines", "long_headlines", "descriptions", "call_to_actions", "videos", "companion_banners", "breadcrumb1", "breadcrumb2")
    HEADLINES_FIELD_NUMBER: _ClassVar[int]
    LONG_HEADLINES_FIELD_NUMBER: _ClassVar[int]
    DESCRIPTIONS_FIELD_NUMBER: _ClassVar[int]
    CALL_TO_ACTIONS_FIELD_NUMBER: _ClassVar[int]
    VIDEOS_FIELD_NUMBER: _ClassVar[int]
    COMPANION_BANNERS_FIELD_NUMBER: _ClassVar[int]
    BREADCRUMB1_FIELD_NUMBER: _ClassVar[int]
    BREADCRUMB2_FIELD_NUMBER: _ClassVar[int]
    headlines: _containers.RepeatedCompositeFieldContainer[_ad_asset_pb2.AdTextAsset]
    long_headlines: _containers.RepeatedCompositeFieldContainer[_ad_asset_pb2.AdTextAsset]
    descriptions: _containers.RepeatedCompositeFieldContainer[_ad_asset_pb2.AdTextAsset]
    call_to_actions: _containers.RepeatedCompositeFieldContainer[_ad_asset_pb2.AdTextAsset]
    videos: _containers.RepeatedCompositeFieldContainer[_ad_asset_pb2.AdVideoAsset]
    companion_banners: _containers.RepeatedCompositeFieldContainer[_ad_asset_pb2.AdImageAsset]
    breadcrumb1: str
    breadcrumb2: str
    def __init__(self, headlines: _Optional[_Iterable[_Union[_ad_asset_pb2.AdTextAsset, _Mapping]]] = ..., long_headlines: _Optional[_Iterable[_Union[_ad_asset_pb2.AdTextAsset, _Mapping]]] = ..., descriptions: _Optional[_Iterable[_Union[_ad_asset_pb2.AdTextAsset, _Mapping]]] = ..., call_to_actions: _Optional[_Iterable[_Union[_ad_asset_pb2.AdTextAsset, _Mapping]]] = ..., videos: _Optional[_Iterable[_Union[_ad_asset_pb2.AdVideoAsset, _Mapping]]] = ..., companion_banners: _Optional[_Iterable[_Union[_ad_asset_pb2.AdImageAsset, _Mapping]]] = ..., breadcrumb1: _Optional[str] = ..., breadcrumb2: _Optional[str] = ...) -> None: ...

class ResponsiveSearchAdInfo(_message.Message):
    __slots__ = ("headlines", "descriptions", "path1", "path2")
    HEADLINES_FIELD_NUMBER: _ClassVar[int]
    DESCRIPTIONS_FIELD_NUMBER: _ClassVar[int]
    PATH1_FIELD_NUMBER: _ClassVar[int]
    PATH2_FIELD_NUMBER: _ClassVar[int]
    headlines: _containers.RepeatedCompositeFieldContainer[_ad_asset_pb2.AdTextAsset]
    descriptions: _containers.RepeatedCompositeFieldContainer[_ad_asset_pb2.AdTextAsset]
    path1: str
    path2: str
    def __init__(self, headlines: _Optional[_Iterable[_Union[_ad_asset_pb2.AdTextAsset, _Mapping]]] = ..., descriptions: _Optional[_Iterable[_Union[_ad_asset_pb2.AdTextAsset, _Mapping]]] = ..., path1: _Optional[str] = ..., path2: _Optional[str] = ...) -> None: ...

class LegacyResponsiveDisplayAdInfo(_message.Message):
    __slots__ = ("short_headline", "long_headline", "description", "business_name", "allow_flexible_color", "accent_color", "main_color", "call_to_action_text", "logo_image", "square_logo_image", "marketing_image", "square_marketing_image", "format_setting", "price_prefix", "promo_text")
    SHORT_HEADLINE_FIELD_NUMBER: _ClassVar[int]
    LONG_HEADLINE_FIELD_NUMBER: _ClassVar[int]
    DESCRIPTION_FIELD_NUMBER: _ClassVar[int]
    BUSINESS_NAME_FIELD_NUMBER: _ClassVar[int]
    ALLOW_FLEXIBLE_COLOR_FIELD_NUMBER: _ClassVar[int]
    ACCENT_COLOR_FIELD_NUMBER: _ClassVar[int]
    MAIN_COLOR_FIELD_NUMBER: _ClassVar[int]
    CALL_TO_ACTION_TEXT_FIELD_NUMBER: _ClassVar[int]
    LOGO_IMAGE_FIELD_NUMBER: _ClassVar[int]
    SQUARE_LOGO_IMAGE_FIELD_NUMBER: _ClassVar[int]
    MARKETING_IMAGE_FIELD_NUMBER: _ClassVar[int]
    SQUARE_MARKETING_IMAGE_FIELD_NUMBER: _ClassVar[int]
    FORMAT_SETTING_FIELD_NUMBER: _ClassVar[int]
    PRICE_PREFIX_FIELD_NUMBER: _ClassVar[int]
    PROMO_TEXT_FIELD_NUMBER: _ClassVar[int]
    short_headline: str
    long_headline: str
    description: str
    business_name: str
    allow_flexible_color: bool
    accent_color: str
    main_color: str
    call_to_action_text: str
    logo_image: str
    square_logo_image: str
    marketing_image: str
    square_marketing_image: str
    format_setting: _display_ad_format_setting_pb2.DisplayAdFormatSettingEnum.DisplayAdFormatSetting
    price_prefix: str
    promo_text: str
    def __init__(self, short_headline: _Optional[str] = ..., long_headline: _Optional[str] = ..., description: _Optional[str] = ..., business_name: _Optional[str] = ..., allow_flexible_color: bool = ..., accent_color: _Optional[str] = ..., main_color: _Optional[str] = ..., call_to_action_text: _Optional[str] = ..., logo_image: _Optional[str] = ..., square_logo_image: _Optional[str] = ..., marketing_image: _Optional[str] = ..., square_marketing_image: _Optional[str] = ..., format_setting: _Optional[_Union[_display_ad_format_setting_pb2.DisplayAdFormatSettingEnum.DisplayAdFormatSetting, str]] = ..., price_prefix: _Optional[str] = ..., promo_text: _Optional[str] = ...) -> None: ...

class AppAdInfo(_message.Message):
    __slots__ = ("mandatory_ad_text", "headlines", "descriptions", "images", "youtube_videos", "html5_media_bundles")
    MANDATORY_AD_TEXT_FIELD_NUMBER: _ClassVar[int]
    HEADLINES_FIELD_NUMBER: _ClassVar[int]
    DESCRIPTIONS_FIELD_NUMBER: _ClassVar[int]
    IMAGES_FIELD_NUMBER: _ClassVar[int]
    YOUTUBE_VIDEOS_FIELD_NUMBER: _ClassVar[int]
    HTML5_MEDIA_BUNDLES_FIELD_NUMBER: _ClassVar[int]
    mandatory_ad_text: _ad_asset_pb2.AdTextAsset
    headlines: _containers.RepeatedCompositeFieldContainer[_ad_asset_pb2.AdTextAsset]
    descriptions: _containers.RepeatedCompositeFieldContainer[_ad_asset_pb2.AdTextAsset]
    images: _containers.RepeatedCompositeFieldContainer[_ad_asset_pb2.AdImageAsset]
    youtube_videos: _containers.RepeatedCompositeFieldContainer[_ad_asset_pb2.AdVideoAsset]
    html5_media_bundles: _containers.RepeatedCompositeFieldContainer[_ad_asset_pb2.AdMediaBundleAsset]
    def __init__(self, mandatory_ad_text: _Optional[_Union[_ad_asset_pb2.AdTextAsset, _Mapping]] = ..., headlines: _Optional[_Iterable[_Union[_ad_asset_pb2.AdTextAsset, _Mapping]]] = ..., descriptions: _Optional[_Iterable[_Union[_ad_asset_pb2.AdTextAsset, _Mapping]]] = ..., images: _Optional[_Iterable[_Union[_ad_asset_pb2.AdImageAsset, _Mapping]]] = ..., youtube_videos: _Optional[_Iterable[_Union[_ad_asset_pb2.AdVideoAsset, _Mapping]]] = ..., html5_media_bundles: _Optional[_Iterable[_Union[_ad_asset_pb2.AdMediaBundleAsset, _Mapping]]] = ...) -> None: ...

class AppEngagementAdInfo(_message.Message):
    __slots__ = ("headlines", "descriptions", "images", "videos")
    HEADLINES_FIELD_NUMBER: _ClassVar[int]
    DESCRIPTIONS_FIELD_NUMBER: _ClassVar[int]
    IMAGES_FIELD_NUMBER: _ClassVar[int]
    VIDEOS_FIELD_NUMBER: _ClassVar[int]
    headlines: _containers.RepeatedCompositeFieldContainer[_ad_asset_pb2.AdTextAsset]
    descriptions: _containers.RepeatedCompositeFieldContainer[_ad_asset_pb2.AdTextAsset]
    images: _containers.RepeatedCompositeFieldContainer[_ad_asset_pb2.AdImageAsset]
    videos: _containers.RepeatedCompositeFieldContainer[_ad_asset_pb2.AdVideoAsset]
    def __init__(self, headlines: _Optional[_Iterable[_Union[_ad_asset_pb2.AdTextAsset, _Mapping]]] = ..., descriptions: _Optional[_Iterable[_Union[_ad_asset_pb2.AdTextAsset, _Mapping]]] = ..., images: _Optional[_Iterable[_Union[_ad_asset_pb2.AdImageAsset, _Mapping]]] = ..., videos: _Optional[_Iterable[_Union[_ad_asset_pb2.AdVideoAsset, _Mapping]]] = ...) -> None: ...

class AppPreRegistrationAdInfo(_message.Message):
    __slots__ = ("headlines", "descriptions", "images", "youtube_videos")
    HEADLINES_FIELD_NUMBER: _ClassVar[int]
    DESCRIPTIONS_FIELD_NUMBER: _ClassVar[int]
    IMAGES_FIELD_NUMBER: _ClassVar[int]
    YOUTUBE_VIDEOS_FIELD_NUMBER: _ClassVar[int]
    headlines: _containers.RepeatedCompositeFieldContainer[_ad_asset_pb2.AdTextAsset]
    descriptions: _containers.RepeatedCompositeFieldContainer[_ad_asset_pb2.AdTextAsset]
    images: _containers.RepeatedCompositeFieldContainer[_ad_asset_pb2.AdImageAsset]
    youtube_videos: _containers.RepeatedCompositeFieldContainer[_ad_asset_pb2.AdVideoAsset]
    def __init__(self, headlines: _Optional[_Iterable[_Union[_ad_asset_pb2.AdTextAsset, _Mapping]]] = ..., descriptions: _Optional[_Iterable[_Union[_ad_asset_pb2.AdTextAsset, _Mapping]]] = ..., images: _Optional[_Iterable[_Union[_ad_asset_pb2.AdImageAsset, _Mapping]]] = ..., youtube_videos: _Optional[_Iterable[_Union[_ad_asset_pb2.AdVideoAsset, _Mapping]]] = ...) -> None: ...

class LegacyAppInstallAdInfo(_message.Message):
    __slots__ = ("app_id", "app_store", "headline", "description1", "description2")
    APP_ID_FIELD_NUMBER: _ClassVar[int]
    APP_STORE_FIELD_NUMBER: _ClassVar[int]
    HEADLINE_FIELD_NUMBER: _ClassVar[int]
    DESCRIPTION1_FIELD_NUMBER: _ClassVar[int]
    DESCRIPTION2_FIELD_NUMBER: _ClassVar[int]
    app_id: str
    app_store: _legacy_app_install_ad_app_store_pb2.LegacyAppInstallAdAppStoreEnum.LegacyAppInstallAdAppStore
    headline: str
    description1: str
    description2: str
    def __init__(self, app_id: _Optional[str] = ..., app_store: _Optional[_Union[_legacy_app_install_ad_app_store_pb2.LegacyAppInstallAdAppStoreEnum.LegacyAppInstallAdAppStore, str]] = ..., headline: _Optional[str] = ..., description1: _Optional[str] = ..., description2: _Optional[str] = ...) -> None: ...

class ResponsiveDisplayAdInfo(_message.Message):
    __slots__ = ("marketing_images", "square_marketing_images", "logo_images", "square_logo_images", "headlines", "long_headline", "descriptions", "youtube_videos", "business_name", "main_color", "accent_color", "allow_flexible_color", "call_to_action_text", "price_prefix", "promo_text", "format_setting", "control_spec")
    MARKETING_IMAGES_FIELD_NUMBER: _ClassVar[int]
    SQUARE_MARKETING_IMAGES_FIELD_NUMBER: _ClassVar[int]
    LOGO_IMAGES_FIELD_NUMBER: _ClassVar[int]
    SQUARE_LOGO_IMAGES_FIELD_NUMBER: _ClassVar[int]
    HEADLINES_FIELD_NUMBER: _ClassVar[int]
    LONG_HEADLINE_FIELD_NUMBER: _ClassVar[int]
    DESCRIPTIONS_FIELD_NUMBER: _ClassVar[int]
    YOUTUBE_VIDEOS_FIELD_NUMBER: _ClassVar[int]
    BUSINESS_NAME_FIELD_NUMBER: _ClassVar[int]
    MAIN_COLOR_FIELD_NUMBER: _ClassVar[int]
    ACCENT_COLOR_FIELD_NUMBER: _ClassVar[int]
    ALLOW_FLEXIBLE_COLOR_FIELD_NUMBER: _ClassVar[int]
    CALL_TO_ACTION_TEXT_FIELD_NUMBER: _ClassVar[int]
    PRICE_PREFIX_FIELD_NUMBER: _ClassVar[int]
    PROMO_TEXT_FIELD_NUMBER: _ClassVar[int]
    FORMAT_SETTING_FIELD_NUMBER: _ClassVar[int]
    CONTROL_SPEC_FIELD_NUMBER: _ClassVar[int]
    marketing_images: _containers.RepeatedCompositeFieldContainer[_ad_asset_pb2.AdImageAsset]
    square_marketing_images: _containers.RepeatedCompositeFieldContainer[_ad_asset_pb2.AdImageAsset]
    logo_images: _containers.RepeatedCompositeFieldContainer[_ad_asset_pb2.AdImageAsset]
    square_logo_images: _containers.RepeatedCompositeFieldContainer[_ad_asset_pb2.AdImageAsset]
    headlines: _containers.RepeatedCompositeFieldContainer[_ad_asset_pb2.AdTextAsset]
    long_headline: _ad_asset_pb2.AdTextAsset
    descriptions: _containers.RepeatedCompositeFieldContainer[_ad_asset_pb2.AdTextAsset]
    youtube_videos: _containers.RepeatedCompositeFieldContainer[_ad_asset_pb2.AdVideoAsset]
    business_name: str
    main_color: str
    accent_color: str
    allow_flexible_color: bool
    call_to_action_text: str
    price_prefix: str
    promo_text: str
    format_setting: _display_ad_format_setting_pb2.DisplayAdFormatSettingEnum.DisplayAdFormatSetting
    control_spec: ResponsiveDisplayAdControlSpec
    def __init__(self, marketing_images: _Optional[_Iterable[_Union[_ad_asset_pb2.AdImageAsset, _Mapping]]] = ..., square_marketing_images: _Optional[_Iterable[_Union[_ad_asset_pb2.AdImageAsset, _Mapping]]] = ..., logo_images: _Optional[_Iterable[_Union[_ad_asset_pb2.AdImageAsset, _Mapping]]] = ..., square_logo_images: _Optional[_Iterable[_Union[_ad_asset_pb2.AdImageAsset, _Mapping]]] = ..., headlines: _Optional[_Iterable[_Union[_ad_asset_pb2.AdTextAsset, _Mapping]]] = ..., long_headline: _Optional[_Union[_ad_asset_pb2.AdTextAsset, _Mapping]] = ..., descriptions: _Optional[_Iterable[_Union[_ad_asset_pb2.AdTextAsset, _Mapping]]] = ..., youtube_videos: _Optional[_Iterable[_Union[_ad_asset_pb2.AdVideoAsset, _Mapping]]] = ..., business_name: _Optional[str] = ..., main_color: _Optional[str] = ..., accent_color: _Optional[str] = ..., allow_flexible_color: bool = ..., call_to_action_text: _Optional[str] = ..., price_prefix: _Optional[str] = ..., promo_text: _Optional[str] = ..., format_setting: _Optional[_Union[_display_ad_format_setting_pb2.DisplayAdFormatSettingEnum.DisplayAdFormatSetting, str]] = ..., control_spec: _Optional[_Union[ResponsiveDisplayAdControlSpec, _Mapping]] = ...) -> None: ...

class LocalAdInfo(_message.Message):
    __slots__ = ("headlines", "descriptions", "call_to_actions", "marketing_images", "logo_images", "videos", "path1", "path2")
    HEADLINES_FIELD_NUMBER: _ClassVar[int]
    DESCRIPTIONS_FIELD_NUMBER: _ClassVar[int]
    CALL_TO_ACTIONS_FIELD_NUMBER: _ClassVar[int]
    MARKETING_IMAGES_FIELD_NUMBER: _ClassVar[int]
    LOGO_IMAGES_FIELD_NUMBER: _ClassVar[int]
    VIDEOS_FIELD_NUMBER: _ClassVar[int]
    PATH1_FIELD_NUMBER: _ClassVar[int]
    PATH2_FIELD_NUMBER: _ClassVar[int]
    headlines: _containers.RepeatedCompositeFieldContainer[_ad_asset_pb2.AdTextAsset]
    descriptions: _containers.RepeatedCompositeFieldContainer[_ad_asset_pb2.AdTextAsset]
    call_to_actions: _containers.RepeatedCompositeFieldContainer[_ad_asset_pb2.AdTextAsset]
    marketing_images: _containers.RepeatedCompositeFieldContainer[_ad_asset_pb2.AdImageAsset]
    logo_images: _containers.RepeatedCompositeFieldContainer[_ad_asset_pb2.AdImageAsset]
    videos: _containers.RepeatedCompositeFieldContainer[_ad_asset_pb2.AdVideoAsset]
    path1: str
    path2: str
    def __init__(self, headlines: _Optional[_Iterable[_Union[_ad_asset_pb2.AdTextAsset, _Mapping]]] = ..., descriptions: _Optional[_Iterable[_Union[_ad_asset_pb2.AdTextAsset, _Mapping]]] = ..., call_to_actions: _Optional[_Iterable[_Union[_ad_asset_pb2.AdTextAsset, _Mapping]]] = ..., marketing_images: _Optional[_Iterable[_Union[_ad_asset_pb2.AdImageAsset, _Mapping]]] = ..., logo_images: _Optional[_Iterable[_Union[_ad_asset_pb2.AdImageAsset, _Mapping]]] = ..., videos: _Optional[_Iterable[_Union[_ad_asset_pb2.AdVideoAsset, _Mapping]]] = ..., path1: _Optional[str] = ..., path2: _Optional[str] = ...) -> None: ...

class DisplayUploadAdInfo(_message.Message):
    __slots__ = ("display_upload_product_type", "media_bundle")
    DISPLAY_UPLOAD_PRODUCT_TYPE_FIELD_NUMBER: _ClassVar[int]
    MEDIA_BUNDLE_FIELD_NUMBER: _ClassVar[int]
    display_upload_product_type: _display_upload_product_type_pb2.DisplayUploadProductTypeEnum.DisplayUploadProductType
    media_bundle: _ad_asset_pb2.AdMediaBundleAsset
    def __init__(self, display_upload_product_type: _Optional[_Union[_display_upload_product_type_pb2.DisplayUploadProductTypeEnum.DisplayUploadProductType, str]] = ..., media_bundle: _Optional[_Union[_ad_asset_pb2.AdMediaBundleAsset, _Mapping]] = ...) -> None: ...

class ResponsiveDisplayAdControlSpec(_message.Message):
    __slots__ = ("enable_asset_enhancements", "enable_autogen_video")
    ENABLE_ASSET_ENHANCEMENTS_FIELD_NUMBER: _ClassVar[int]
    ENABLE_AUTOGEN_VIDEO_FIELD_NUMBER: _ClassVar[int]
    enable_asset_enhancements: bool
    enable_autogen_video: bool
    def __init__(self, enable_asset_enhancements: bool = ..., enable_autogen_video: bool = ...) -> None: ...

class SmartCampaignAdInfo(_message.Message):
    __slots__ = ("headlines", "descriptions")
    HEADLINES_FIELD_NUMBER: _ClassVar[int]
    DESCRIPTIONS_FIELD_NUMBER: _ClassVar[int]
    headlines: _containers.RepeatedCompositeFieldContainer[_ad_asset_pb2.AdTextAsset]
    descriptions: _containers.RepeatedCompositeFieldContainer[_ad_asset_pb2.AdTextAsset]
    def __init__(self, headlines: _Optional[_Iterable[_Union[_ad_asset_pb2.AdTextAsset, _Mapping]]] = ..., descriptions: _Optional[_Iterable[_Union[_ad_asset_pb2.AdTextAsset, _Mapping]]] = ...) -> None: ...

class CallAdInfo(_message.Message):
    __slots__ = ("country_code", "phone_number", "business_name", "headline1", "headline2", "description1", "description2", "call_tracked", "disable_call_conversion", "phone_number_verification_url", "conversion_action", "conversion_reporting_state", "path1", "path2")
    COUNTRY_CODE_FIELD_NUMBER: _ClassVar[int]
    PHONE_NUMBER_FIELD_NUMBER: _ClassVar[int]
    BUSINESS_NAME_FIELD_NUMBER: _ClassVar[int]
    HEADLINE1_FIELD_NUMBER: _ClassVar[int]
    HEADLINE2_FIELD_NUMBER: _ClassVar[int]
    DESCRIPTION1_FIELD_NUMBER: _ClassVar[int]
    DESCRIPTION2_FIELD_NUMBER: _ClassVar[int]
    CALL_TRACKED_FIELD_NUMBER: _ClassVar[int]
    DISABLE_CALL_CONVERSION_FIELD_NUMBER: _ClassVar[int]
    PHONE_NUMBER_VERIFICATION_URL_FIELD_NUMBER: _ClassVar[int]
    CONVERSION_ACTION_FIELD_NUMBER: _ClassVar[int]
    CONVERSION_REPORTING_STATE_FIELD_NUMBER: _ClassVar[int]
    PATH1_FIELD_NUMBER: _ClassVar[int]
    PATH2_FIELD_NUMBER: _ClassVar[int]
    country_code: str
    phone_number: str
    business_name: str
    headline1: str
    headline2: str
    description1: str
    description2: str
    call_tracked: bool
    disable_call_conversion: bool
    phone_number_verification_url: str
    conversion_action: str
    conversion_reporting_state: _call_conversion_reporting_state_pb2.CallConversionReportingStateEnum.CallConversionReportingState
    path1: str
    path2: str
    def __init__(self, country_code: _Optional[str] = ..., phone_number: _Optional[str] = ..., business_name: _Optional[str] = ..., headline1: _Optional[str] = ..., headline2: _Optional[str] = ..., description1: _Optional[str] = ..., description2: _Optional[str] = ..., call_tracked: bool = ..., disable_call_conversion: bool = ..., phone_number_verification_url: _Optional[str] = ..., conversion_action: _Optional[str] = ..., conversion_reporting_state: _Optional[_Union[_call_conversion_reporting_state_pb2.CallConversionReportingStateEnum.CallConversionReportingState, str]] = ..., path1: _Optional[str] = ..., path2: _Optional[str] = ...) -> None: ...

class DiscoveryMultiAssetAdInfo(_message.Message):
    __slots__ = ("marketing_images", "square_marketing_images", "portrait_marketing_images", "logo_images", "headlines", "descriptions", "business_name", "call_to_action_text", "lead_form_only")
    MARKETING_IMAGES_FIELD_NUMBER: _ClassVar[int]
    SQUARE_MARKETING_IMAGES_FIELD_NUMBER: _ClassVar[int]
    PORTRAIT_MARKETING_IMAGES_FIELD_NUMBER: _ClassVar[int]
    LOGO_IMAGES_FIELD_NUMBER: _ClassVar[int]
    HEADLINES_FIELD_NUMBER: _ClassVar[int]
    DESCRIPTIONS_FIELD_NUMBER: _ClassVar[int]
    BUSINESS_NAME_FIELD_NUMBER: _ClassVar[int]
    CALL_TO_ACTION_TEXT_FIELD_NUMBER: _ClassVar[int]
    LEAD_FORM_ONLY_FIELD_NUMBER: _ClassVar[int]
    marketing_images: _containers.RepeatedCompositeFieldContainer[_ad_asset_pb2.AdImageAsset]
    square_marketing_images: _containers.RepeatedCompositeFieldContainer[_ad_asset_pb2.AdImageAsset]
    portrait_marketing_images: _containers.RepeatedCompositeFieldContainer[_ad_asset_pb2.AdImageAsset]
    logo_images: _containers.RepeatedCompositeFieldContainer[_ad_asset_pb2.AdImageAsset]
    headlines: _containers.RepeatedCompositeFieldContainer[_ad_asset_pb2.AdTextAsset]
    descriptions: _containers.RepeatedCompositeFieldContainer[_ad_asset_pb2.AdTextAsset]
    business_name: str
    call_to_action_text: str
    lead_form_only: bool
    def __init__(self, marketing_images: _Optional[_Iterable[_Union[_ad_asset_pb2.AdImageAsset, _Mapping]]] = ..., square_marketing_images: _Optional[_Iterable[_Union[_ad_asset_pb2.AdImageAsset, _Mapping]]] = ..., portrait_marketing_images: _Optional[_Iterable[_Union[_ad_asset_pb2.AdImageAsset, _Mapping]]] = ..., logo_images: _Optional[_Iterable[_Union[_ad_asset_pb2.AdImageAsset, _Mapping]]] = ..., headlines: _Optional[_Iterable[_Union[_ad_asset_pb2.AdTextAsset, _Mapping]]] = ..., descriptions: _Optional[_Iterable[_Union[_ad_asset_pb2.AdTextAsset, _Mapping]]] = ..., business_name: _Optional[str] = ..., call_to_action_text: _Optional[str] = ..., lead_form_only: bool = ...) -> None: ...

class DiscoveryCarouselAdInfo(_message.Message):
    __slots__ = ("business_name", "logo_image", "headline", "description", "call_to_action_text", "carousel_cards")
    BUSINESS_NAME_FIELD_NUMBER: _ClassVar[int]
    LOGO_IMAGE_FIELD_NUMBER: _ClassVar[int]
    HEADLINE_FIELD_NUMBER: _ClassVar[int]
    DESCRIPTION_FIELD_NUMBER: _ClassVar[int]
    CALL_TO_ACTION_TEXT_FIELD_NUMBER: _ClassVar[int]
    CAROUSEL_CARDS_FIELD_NUMBER: _ClassVar[int]
    business_name: str
    logo_image: _ad_asset_pb2.AdImageAsset
    headline: _ad_asset_pb2.AdTextAsset
    description: _ad_asset_pb2.AdTextAsset
    call_to_action_text: str
    carousel_cards: _containers.RepeatedCompositeFieldContainer[_ad_asset_pb2.AdDiscoveryCarouselCardAsset]
    def __init__(self, business_name: _Optional[str] = ..., logo_image: _Optional[_Union[_ad_asset_pb2.AdImageAsset, _Mapping]] = ..., headline: _Optional[_Union[_ad_asset_pb2.AdTextAsset, _Mapping]] = ..., description: _Optional[_Union[_ad_asset_pb2.AdTextAsset, _Mapping]] = ..., call_to_action_text: _Optional[str] = ..., carousel_cards: _Optional[_Iterable[_Union[_ad_asset_pb2.AdDiscoveryCarouselCardAsset, _Mapping]]] = ...) -> None: ...

class DiscoveryVideoResponsiveAdInfo(_message.Message):
    __slots__ = ("headlines", "long_headlines", "descriptions", "videos", "logo_images", "breadcrumb1", "breadcrumb2", "business_name", "call_to_actions")
    HEADLINES_FIELD_NUMBER: _ClassVar[int]
    LONG_HEADLINES_FIELD_NUMBER: _ClassVar[int]
    DESCRIPTIONS_FIELD_NUMBER: _ClassVar[int]
    VIDEOS_FIELD_NUMBER: _ClassVar[int]
    LOGO_IMAGES_FIELD_NUMBER: _ClassVar[int]
    BREADCRUMB1_FIELD_NUMBER: _ClassVar[int]
    BREADCRUMB2_FIELD_NUMBER: _ClassVar[int]
    BUSINESS_NAME_FIELD_NUMBER: _ClassVar[int]
    CALL_TO_ACTIONS_FIELD_NUMBER: _ClassVar[int]
    headlines: _containers.RepeatedCompositeFieldContainer[_ad_asset_pb2.AdTextAsset]
    long_headlines: _containers.RepeatedCompositeFieldContainer[_ad_asset_pb2.AdTextAsset]
    descriptions: _containers.RepeatedCompositeFieldContainer[_ad_asset_pb2.AdTextAsset]
    videos: _containers.RepeatedCompositeFieldContainer[_ad_asset_pb2.AdVideoAsset]
    logo_images: _containers.RepeatedCompositeFieldContainer[_ad_asset_pb2.AdImageAsset]
    breadcrumb1: str
    breadcrumb2: str
    business_name: _ad_asset_pb2.AdTextAsset
    call_to_actions: _containers.RepeatedCompositeFieldContainer[_ad_asset_pb2.AdCallToActionAsset]
    def __init__(self, headlines: _Optional[_Iterable[_Union[_ad_asset_pb2.AdTextAsset, _Mapping]]] = ..., long_headlines: _Optional[_Iterable[_Union[_ad_asset_pb2.AdTextAsset, _Mapping]]] = ..., descriptions: _Optional[_Iterable[_Union[_ad_asset_pb2.AdTextAsset, _Mapping]]] = ..., videos: _Optional[_Iterable[_Union[_ad_asset_pb2.AdVideoAsset, _Mapping]]] = ..., logo_images: _Optional[_Iterable[_Union[_ad_asset_pb2.AdImageAsset, _Mapping]]] = ..., breadcrumb1: _Optional[str] = ..., breadcrumb2: _Optional[str] = ..., business_name: _Optional[_Union[_ad_asset_pb2.AdTextAsset, _Mapping]] = ..., call_to_actions: _Optional[_Iterable[_Union[_ad_asset_pb2.AdCallToActionAsset, _Mapping]]] = ...) -> None: ...

class DemandGenProductAdInfo(_message.Message):
    __slots__ = ("headline", "description", "logo_image", "breadcrumb1", "breadcrumb2", "business_name", "call_to_action")
    HEADLINE_FIELD_NUMBER: _ClassVar[int]
    DESCRIPTION_FIELD_NUMBER: _ClassVar[int]
    LOGO_IMAGE_FIELD_NUMBER: _ClassVar[int]
    BREADCRUMB1_FIELD_NUMBER: _ClassVar[int]
    BREADCRUMB2_FIELD_NUMBER: _ClassVar[int]
    BUSINESS_NAME_FIELD_NUMBER: _ClassVar[int]
    CALL_TO_ACTION_FIELD_NUMBER: _ClassVar[int]
    headline: _ad_asset_pb2.AdTextAsset
    description: _ad_asset_pb2.AdTextAsset
    logo_image: _ad_asset_pb2.AdImageAsset
    breadcrumb1: str
    breadcrumb2: str
    business_name: _ad_asset_pb2.AdTextAsset
    call_to_action: _ad_asset_pb2.AdCallToActionAsset
    def __init__(self, headline: _Optional[_Union[_ad_asset_pb2.AdTextAsset, _Mapping]] = ..., description: _Optional[_Union[_ad_asset_pb2.AdTextAsset, _Mapping]] = ..., logo_image: _Optional[_Union[_ad_asset_pb2.AdImageAsset, _Mapping]] = ..., breadcrumb1: _Optional[str] = ..., breadcrumb2: _Optional[str] = ..., business_name: _Optional[_Union[_ad_asset_pb2.AdTextAsset, _Mapping]] = ..., call_to_action: _Optional[_Union[_ad_asset_pb2.AdCallToActionAsset, _Mapping]] = ...) -> None: ...
