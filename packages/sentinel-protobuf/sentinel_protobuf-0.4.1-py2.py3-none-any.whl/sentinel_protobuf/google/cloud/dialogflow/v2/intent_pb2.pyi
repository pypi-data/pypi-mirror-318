from google.api import annotations_pb2 as _annotations_pb2
from google.api import client_pb2 as _client_pb2
from google.api import field_behavior_pb2 as _field_behavior_pb2
from google.api import resource_pb2 as _resource_pb2
from google.cloud.dialogflow.v2 import context_pb2 as _context_pb2
from google.longrunning import operations_pb2 as _operations_pb2
from google.protobuf import empty_pb2 as _empty_pb2
from google.protobuf import field_mask_pb2 as _field_mask_pb2
from google.protobuf import struct_pb2 as _struct_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union
DESCRIPTOR: _descriptor.FileDescriptor

class IntentView(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    INTENT_VIEW_UNSPECIFIED: _ClassVar[IntentView]
    INTENT_VIEW_FULL: _ClassVar[IntentView]
INTENT_VIEW_UNSPECIFIED: IntentView
INTENT_VIEW_FULL: IntentView

class Intent(_message.Message):
    __slots__ = ('name', 'display_name', 'webhook_state', 'priority', 'is_fallback', 'ml_disabled', 'live_agent_handoff', 'end_interaction', 'input_context_names', 'events', 'training_phrases', 'action', 'output_contexts', 'reset_contexts', 'parameters', 'messages', 'default_response_platforms', 'root_followup_intent_name', 'parent_followup_intent_name', 'followup_intent_info')

    class WebhookState(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        WEBHOOK_STATE_UNSPECIFIED: _ClassVar[Intent.WebhookState]
        WEBHOOK_STATE_ENABLED: _ClassVar[Intent.WebhookState]
        WEBHOOK_STATE_ENABLED_FOR_SLOT_FILLING: _ClassVar[Intent.WebhookState]
    WEBHOOK_STATE_UNSPECIFIED: Intent.WebhookState
    WEBHOOK_STATE_ENABLED: Intent.WebhookState
    WEBHOOK_STATE_ENABLED_FOR_SLOT_FILLING: Intent.WebhookState

    class TrainingPhrase(_message.Message):
        __slots__ = ('name', 'type', 'parts', 'times_added_count')

        class Type(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
            __slots__ = ()
            TYPE_UNSPECIFIED: _ClassVar[Intent.TrainingPhrase.Type]
            EXAMPLE: _ClassVar[Intent.TrainingPhrase.Type]
            TEMPLATE: _ClassVar[Intent.TrainingPhrase.Type]
        TYPE_UNSPECIFIED: Intent.TrainingPhrase.Type
        EXAMPLE: Intent.TrainingPhrase.Type
        TEMPLATE: Intent.TrainingPhrase.Type

        class Part(_message.Message):
            __slots__ = ('text', 'entity_type', 'alias', 'user_defined')
            TEXT_FIELD_NUMBER: _ClassVar[int]
            ENTITY_TYPE_FIELD_NUMBER: _ClassVar[int]
            ALIAS_FIELD_NUMBER: _ClassVar[int]
            USER_DEFINED_FIELD_NUMBER: _ClassVar[int]
            text: str
            entity_type: str
            alias: str
            user_defined: bool

            def __init__(self, text: _Optional[str]=..., entity_type: _Optional[str]=..., alias: _Optional[str]=..., user_defined: bool=...) -> None:
                ...
        NAME_FIELD_NUMBER: _ClassVar[int]
        TYPE_FIELD_NUMBER: _ClassVar[int]
        PARTS_FIELD_NUMBER: _ClassVar[int]
        TIMES_ADDED_COUNT_FIELD_NUMBER: _ClassVar[int]
        name: str
        type: Intent.TrainingPhrase.Type
        parts: _containers.RepeatedCompositeFieldContainer[Intent.TrainingPhrase.Part]
        times_added_count: int

        def __init__(self, name: _Optional[str]=..., type: _Optional[_Union[Intent.TrainingPhrase.Type, str]]=..., parts: _Optional[_Iterable[_Union[Intent.TrainingPhrase.Part, _Mapping]]]=..., times_added_count: _Optional[int]=...) -> None:
            ...

    class Parameter(_message.Message):
        __slots__ = ('name', 'display_name', 'value', 'default_value', 'entity_type_display_name', 'mandatory', 'prompts', 'is_list')
        NAME_FIELD_NUMBER: _ClassVar[int]
        DISPLAY_NAME_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        DEFAULT_VALUE_FIELD_NUMBER: _ClassVar[int]
        ENTITY_TYPE_DISPLAY_NAME_FIELD_NUMBER: _ClassVar[int]
        MANDATORY_FIELD_NUMBER: _ClassVar[int]
        PROMPTS_FIELD_NUMBER: _ClassVar[int]
        IS_LIST_FIELD_NUMBER: _ClassVar[int]
        name: str
        display_name: str
        value: str
        default_value: str
        entity_type_display_name: str
        mandatory: bool
        prompts: _containers.RepeatedScalarFieldContainer[str]
        is_list: bool

        def __init__(self, name: _Optional[str]=..., display_name: _Optional[str]=..., value: _Optional[str]=..., default_value: _Optional[str]=..., entity_type_display_name: _Optional[str]=..., mandatory: bool=..., prompts: _Optional[_Iterable[str]]=..., is_list: bool=...) -> None:
            ...

    class Message(_message.Message):
        __slots__ = ('text', 'image', 'quick_replies', 'card', 'payload', 'simple_responses', 'basic_card', 'suggestions', 'link_out_suggestion', 'list_select', 'carousel_select', 'browse_carousel_card', 'table_card', 'media_content', 'platform')

        class Platform(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
            __slots__ = ()
            PLATFORM_UNSPECIFIED: _ClassVar[Intent.Message.Platform]
            FACEBOOK: _ClassVar[Intent.Message.Platform]
            SLACK: _ClassVar[Intent.Message.Platform]
            TELEGRAM: _ClassVar[Intent.Message.Platform]
            KIK: _ClassVar[Intent.Message.Platform]
            SKYPE: _ClassVar[Intent.Message.Platform]
            LINE: _ClassVar[Intent.Message.Platform]
            VIBER: _ClassVar[Intent.Message.Platform]
            ACTIONS_ON_GOOGLE: _ClassVar[Intent.Message.Platform]
            GOOGLE_HANGOUTS: _ClassVar[Intent.Message.Platform]
        PLATFORM_UNSPECIFIED: Intent.Message.Platform
        FACEBOOK: Intent.Message.Platform
        SLACK: Intent.Message.Platform
        TELEGRAM: Intent.Message.Platform
        KIK: Intent.Message.Platform
        SKYPE: Intent.Message.Platform
        LINE: Intent.Message.Platform
        VIBER: Intent.Message.Platform
        ACTIONS_ON_GOOGLE: Intent.Message.Platform
        GOOGLE_HANGOUTS: Intent.Message.Platform

        class Text(_message.Message):
            __slots__ = ('text',)
            TEXT_FIELD_NUMBER: _ClassVar[int]
            text: _containers.RepeatedScalarFieldContainer[str]

            def __init__(self, text: _Optional[_Iterable[str]]=...) -> None:
                ...

        class Image(_message.Message):
            __slots__ = ('image_uri', 'accessibility_text')
            IMAGE_URI_FIELD_NUMBER: _ClassVar[int]
            ACCESSIBILITY_TEXT_FIELD_NUMBER: _ClassVar[int]
            image_uri: str
            accessibility_text: str

            def __init__(self, image_uri: _Optional[str]=..., accessibility_text: _Optional[str]=...) -> None:
                ...

        class QuickReplies(_message.Message):
            __slots__ = ('title', 'quick_replies')
            TITLE_FIELD_NUMBER: _ClassVar[int]
            QUICK_REPLIES_FIELD_NUMBER: _ClassVar[int]
            title: str
            quick_replies: _containers.RepeatedScalarFieldContainer[str]

            def __init__(self, title: _Optional[str]=..., quick_replies: _Optional[_Iterable[str]]=...) -> None:
                ...

        class Card(_message.Message):
            __slots__ = ('title', 'subtitle', 'image_uri', 'buttons')

            class Button(_message.Message):
                __slots__ = ('text', 'postback')
                TEXT_FIELD_NUMBER: _ClassVar[int]
                POSTBACK_FIELD_NUMBER: _ClassVar[int]
                text: str
                postback: str

                def __init__(self, text: _Optional[str]=..., postback: _Optional[str]=...) -> None:
                    ...
            TITLE_FIELD_NUMBER: _ClassVar[int]
            SUBTITLE_FIELD_NUMBER: _ClassVar[int]
            IMAGE_URI_FIELD_NUMBER: _ClassVar[int]
            BUTTONS_FIELD_NUMBER: _ClassVar[int]
            title: str
            subtitle: str
            image_uri: str
            buttons: _containers.RepeatedCompositeFieldContainer[Intent.Message.Card.Button]

            def __init__(self, title: _Optional[str]=..., subtitle: _Optional[str]=..., image_uri: _Optional[str]=..., buttons: _Optional[_Iterable[_Union[Intent.Message.Card.Button, _Mapping]]]=...) -> None:
                ...

        class SimpleResponse(_message.Message):
            __slots__ = ('text_to_speech', 'ssml', 'display_text')
            TEXT_TO_SPEECH_FIELD_NUMBER: _ClassVar[int]
            SSML_FIELD_NUMBER: _ClassVar[int]
            DISPLAY_TEXT_FIELD_NUMBER: _ClassVar[int]
            text_to_speech: str
            ssml: str
            display_text: str

            def __init__(self, text_to_speech: _Optional[str]=..., ssml: _Optional[str]=..., display_text: _Optional[str]=...) -> None:
                ...

        class SimpleResponses(_message.Message):
            __slots__ = ('simple_responses',)
            SIMPLE_RESPONSES_FIELD_NUMBER: _ClassVar[int]
            simple_responses: _containers.RepeatedCompositeFieldContainer[Intent.Message.SimpleResponse]

            def __init__(self, simple_responses: _Optional[_Iterable[_Union[Intent.Message.SimpleResponse, _Mapping]]]=...) -> None:
                ...

        class BasicCard(_message.Message):
            __slots__ = ('title', 'subtitle', 'formatted_text', 'image', 'buttons')

            class Button(_message.Message):
                __slots__ = ('title', 'open_uri_action')

                class OpenUriAction(_message.Message):
                    __slots__ = ('uri',)
                    URI_FIELD_NUMBER: _ClassVar[int]
                    uri: str

                    def __init__(self, uri: _Optional[str]=...) -> None:
                        ...
                TITLE_FIELD_NUMBER: _ClassVar[int]
                OPEN_URI_ACTION_FIELD_NUMBER: _ClassVar[int]
                title: str
                open_uri_action: Intent.Message.BasicCard.Button.OpenUriAction

                def __init__(self, title: _Optional[str]=..., open_uri_action: _Optional[_Union[Intent.Message.BasicCard.Button.OpenUriAction, _Mapping]]=...) -> None:
                    ...
            TITLE_FIELD_NUMBER: _ClassVar[int]
            SUBTITLE_FIELD_NUMBER: _ClassVar[int]
            FORMATTED_TEXT_FIELD_NUMBER: _ClassVar[int]
            IMAGE_FIELD_NUMBER: _ClassVar[int]
            BUTTONS_FIELD_NUMBER: _ClassVar[int]
            title: str
            subtitle: str
            formatted_text: str
            image: Intent.Message.Image
            buttons: _containers.RepeatedCompositeFieldContainer[Intent.Message.BasicCard.Button]

            def __init__(self, title: _Optional[str]=..., subtitle: _Optional[str]=..., formatted_text: _Optional[str]=..., image: _Optional[_Union[Intent.Message.Image, _Mapping]]=..., buttons: _Optional[_Iterable[_Union[Intent.Message.BasicCard.Button, _Mapping]]]=...) -> None:
                ...

        class Suggestion(_message.Message):
            __slots__ = ('title',)
            TITLE_FIELD_NUMBER: _ClassVar[int]
            title: str

            def __init__(self, title: _Optional[str]=...) -> None:
                ...

        class Suggestions(_message.Message):
            __slots__ = ('suggestions',)
            SUGGESTIONS_FIELD_NUMBER: _ClassVar[int]
            suggestions: _containers.RepeatedCompositeFieldContainer[Intent.Message.Suggestion]

            def __init__(self, suggestions: _Optional[_Iterable[_Union[Intent.Message.Suggestion, _Mapping]]]=...) -> None:
                ...

        class LinkOutSuggestion(_message.Message):
            __slots__ = ('destination_name', 'uri')
            DESTINATION_NAME_FIELD_NUMBER: _ClassVar[int]
            URI_FIELD_NUMBER: _ClassVar[int]
            destination_name: str
            uri: str

            def __init__(self, destination_name: _Optional[str]=..., uri: _Optional[str]=...) -> None:
                ...

        class ListSelect(_message.Message):
            __slots__ = ('title', 'items', 'subtitle')

            class Item(_message.Message):
                __slots__ = ('info', 'title', 'description', 'image')
                INFO_FIELD_NUMBER: _ClassVar[int]
                TITLE_FIELD_NUMBER: _ClassVar[int]
                DESCRIPTION_FIELD_NUMBER: _ClassVar[int]
                IMAGE_FIELD_NUMBER: _ClassVar[int]
                info: Intent.Message.SelectItemInfo
                title: str
                description: str
                image: Intent.Message.Image

                def __init__(self, info: _Optional[_Union[Intent.Message.SelectItemInfo, _Mapping]]=..., title: _Optional[str]=..., description: _Optional[str]=..., image: _Optional[_Union[Intent.Message.Image, _Mapping]]=...) -> None:
                    ...
            TITLE_FIELD_NUMBER: _ClassVar[int]
            ITEMS_FIELD_NUMBER: _ClassVar[int]
            SUBTITLE_FIELD_NUMBER: _ClassVar[int]
            title: str
            items: _containers.RepeatedCompositeFieldContainer[Intent.Message.ListSelect.Item]
            subtitle: str

            def __init__(self, title: _Optional[str]=..., items: _Optional[_Iterable[_Union[Intent.Message.ListSelect.Item, _Mapping]]]=..., subtitle: _Optional[str]=...) -> None:
                ...

        class CarouselSelect(_message.Message):
            __slots__ = ('items',)

            class Item(_message.Message):
                __slots__ = ('info', 'title', 'description', 'image')
                INFO_FIELD_NUMBER: _ClassVar[int]
                TITLE_FIELD_NUMBER: _ClassVar[int]
                DESCRIPTION_FIELD_NUMBER: _ClassVar[int]
                IMAGE_FIELD_NUMBER: _ClassVar[int]
                info: Intent.Message.SelectItemInfo
                title: str
                description: str
                image: Intent.Message.Image

                def __init__(self, info: _Optional[_Union[Intent.Message.SelectItemInfo, _Mapping]]=..., title: _Optional[str]=..., description: _Optional[str]=..., image: _Optional[_Union[Intent.Message.Image, _Mapping]]=...) -> None:
                    ...
            ITEMS_FIELD_NUMBER: _ClassVar[int]
            items: _containers.RepeatedCompositeFieldContainer[Intent.Message.CarouselSelect.Item]

            def __init__(self, items: _Optional[_Iterable[_Union[Intent.Message.CarouselSelect.Item, _Mapping]]]=...) -> None:
                ...

        class SelectItemInfo(_message.Message):
            __slots__ = ('key', 'synonyms')
            KEY_FIELD_NUMBER: _ClassVar[int]
            SYNONYMS_FIELD_NUMBER: _ClassVar[int]
            key: str
            synonyms: _containers.RepeatedScalarFieldContainer[str]

            def __init__(self, key: _Optional[str]=..., synonyms: _Optional[_Iterable[str]]=...) -> None:
                ...

        class MediaContent(_message.Message):
            __slots__ = ('media_type', 'media_objects')

            class ResponseMediaType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
                __slots__ = ()
                RESPONSE_MEDIA_TYPE_UNSPECIFIED: _ClassVar[Intent.Message.MediaContent.ResponseMediaType]
                AUDIO: _ClassVar[Intent.Message.MediaContent.ResponseMediaType]
            RESPONSE_MEDIA_TYPE_UNSPECIFIED: Intent.Message.MediaContent.ResponseMediaType
            AUDIO: Intent.Message.MediaContent.ResponseMediaType

            class ResponseMediaObject(_message.Message):
                __slots__ = ('name', 'description', 'large_image', 'icon', 'content_url')
                NAME_FIELD_NUMBER: _ClassVar[int]
                DESCRIPTION_FIELD_NUMBER: _ClassVar[int]
                LARGE_IMAGE_FIELD_NUMBER: _ClassVar[int]
                ICON_FIELD_NUMBER: _ClassVar[int]
                CONTENT_URL_FIELD_NUMBER: _ClassVar[int]
                name: str
                description: str
                large_image: Intent.Message.Image
                icon: Intent.Message.Image
                content_url: str

                def __init__(self, name: _Optional[str]=..., description: _Optional[str]=..., large_image: _Optional[_Union[Intent.Message.Image, _Mapping]]=..., icon: _Optional[_Union[Intent.Message.Image, _Mapping]]=..., content_url: _Optional[str]=...) -> None:
                    ...
            MEDIA_TYPE_FIELD_NUMBER: _ClassVar[int]
            MEDIA_OBJECTS_FIELD_NUMBER: _ClassVar[int]
            media_type: Intent.Message.MediaContent.ResponseMediaType
            media_objects: _containers.RepeatedCompositeFieldContainer[Intent.Message.MediaContent.ResponseMediaObject]

            def __init__(self, media_type: _Optional[_Union[Intent.Message.MediaContent.ResponseMediaType, str]]=..., media_objects: _Optional[_Iterable[_Union[Intent.Message.MediaContent.ResponseMediaObject, _Mapping]]]=...) -> None:
                ...

        class BrowseCarouselCard(_message.Message):
            __slots__ = ('items', 'image_display_options')

            class ImageDisplayOptions(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
                __slots__ = ()
                IMAGE_DISPLAY_OPTIONS_UNSPECIFIED: _ClassVar[Intent.Message.BrowseCarouselCard.ImageDisplayOptions]
                GRAY: _ClassVar[Intent.Message.BrowseCarouselCard.ImageDisplayOptions]
                WHITE: _ClassVar[Intent.Message.BrowseCarouselCard.ImageDisplayOptions]
                CROPPED: _ClassVar[Intent.Message.BrowseCarouselCard.ImageDisplayOptions]
                BLURRED_BACKGROUND: _ClassVar[Intent.Message.BrowseCarouselCard.ImageDisplayOptions]
            IMAGE_DISPLAY_OPTIONS_UNSPECIFIED: Intent.Message.BrowseCarouselCard.ImageDisplayOptions
            GRAY: Intent.Message.BrowseCarouselCard.ImageDisplayOptions
            WHITE: Intent.Message.BrowseCarouselCard.ImageDisplayOptions
            CROPPED: Intent.Message.BrowseCarouselCard.ImageDisplayOptions
            BLURRED_BACKGROUND: Intent.Message.BrowseCarouselCard.ImageDisplayOptions

            class BrowseCarouselCardItem(_message.Message):
                __slots__ = ('open_uri_action', 'title', 'description', 'image', 'footer')

                class OpenUrlAction(_message.Message):
                    __slots__ = ('url', 'url_type_hint')

                    class UrlTypeHint(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
                        __slots__ = ()
                        URL_TYPE_HINT_UNSPECIFIED: _ClassVar[Intent.Message.BrowseCarouselCard.BrowseCarouselCardItem.OpenUrlAction.UrlTypeHint]
                        AMP_ACTION: _ClassVar[Intent.Message.BrowseCarouselCard.BrowseCarouselCardItem.OpenUrlAction.UrlTypeHint]
                        AMP_CONTENT: _ClassVar[Intent.Message.BrowseCarouselCard.BrowseCarouselCardItem.OpenUrlAction.UrlTypeHint]
                    URL_TYPE_HINT_UNSPECIFIED: Intent.Message.BrowseCarouselCard.BrowseCarouselCardItem.OpenUrlAction.UrlTypeHint
                    AMP_ACTION: Intent.Message.BrowseCarouselCard.BrowseCarouselCardItem.OpenUrlAction.UrlTypeHint
                    AMP_CONTENT: Intent.Message.BrowseCarouselCard.BrowseCarouselCardItem.OpenUrlAction.UrlTypeHint
                    URL_FIELD_NUMBER: _ClassVar[int]
                    URL_TYPE_HINT_FIELD_NUMBER: _ClassVar[int]
                    url: str
                    url_type_hint: Intent.Message.BrowseCarouselCard.BrowseCarouselCardItem.OpenUrlAction.UrlTypeHint

                    def __init__(self, url: _Optional[str]=..., url_type_hint: _Optional[_Union[Intent.Message.BrowseCarouselCard.BrowseCarouselCardItem.OpenUrlAction.UrlTypeHint, str]]=...) -> None:
                        ...
                OPEN_URI_ACTION_FIELD_NUMBER: _ClassVar[int]
                TITLE_FIELD_NUMBER: _ClassVar[int]
                DESCRIPTION_FIELD_NUMBER: _ClassVar[int]
                IMAGE_FIELD_NUMBER: _ClassVar[int]
                FOOTER_FIELD_NUMBER: _ClassVar[int]
                open_uri_action: Intent.Message.BrowseCarouselCard.BrowseCarouselCardItem.OpenUrlAction
                title: str
                description: str
                image: Intent.Message.Image
                footer: str

                def __init__(self, open_uri_action: _Optional[_Union[Intent.Message.BrowseCarouselCard.BrowseCarouselCardItem.OpenUrlAction, _Mapping]]=..., title: _Optional[str]=..., description: _Optional[str]=..., image: _Optional[_Union[Intent.Message.Image, _Mapping]]=..., footer: _Optional[str]=...) -> None:
                    ...
            ITEMS_FIELD_NUMBER: _ClassVar[int]
            IMAGE_DISPLAY_OPTIONS_FIELD_NUMBER: _ClassVar[int]
            items: _containers.RepeatedCompositeFieldContainer[Intent.Message.BrowseCarouselCard.BrowseCarouselCardItem]
            image_display_options: Intent.Message.BrowseCarouselCard.ImageDisplayOptions

            def __init__(self, items: _Optional[_Iterable[_Union[Intent.Message.BrowseCarouselCard.BrowseCarouselCardItem, _Mapping]]]=..., image_display_options: _Optional[_Union[Intent.Message.BrowseCarouselCard.ImageDisplayOptions, str]]=...) -> None:
                ...

        class TableCard(_message.Message):
            __slots__ = ('title', 'subtitle', 'image', 'column_properties', 'rows', 'buttons')
            TITLE_FIELD_NUMBER: _ClassVar[int]
            SUBTITLE_FIELD_NUMBER: _ClassVar[int]
            IMAGE_FIELD_NUMBER: _ClassVar[int]
            COLUMN_PROPERTIES_FIELD_NUMBER: _ClassVar[int]
            ROWS_FIELD_NUMBER: _ClassVar[int]
            BUTTONS_FIELD_NUMBER: _ClassVar[int]
            title: str
            subtitle: str
            image: Intent.Message.Image
            column_properties: _containers.RepeatedCompositeFieldContainer[Intent.Message.ColumnProperties]
            rows: _containers.RepeatedCompositeFieldContainer[Intent.Message.TableCardRow]
            buttons: _containers.RepeatedCompositeFieldContainer[Intent.Message.BasicCard.Button]

            def __init__(self, title: _Optional[str]=..., subtitle: _Optional[str]=..., image: _Optional[_Union[Intent.Message.Image, _Mapping]]=..., column_properties: _Optional[_Iterable[_Union[Intent.Message.ColumnProperties, _Mapping]]]=..., rows: _Optional[_Iterable[_Union[Intent.Message.TableCardRow, _Mapping]]]=..., buttons: _Optional[_Iterable[_Union[Intent.Message.BasicCard.Button, _Mapping]]]=...) -> None:
                ...

        class ColumnProperties(_message.Message):
            __slots__ = ('header', 'horizontal_alignment')

            class HorizontalAlignment(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
                __slots__ = ()
                HORIZONTAL_ALIGNMENT_UNSPECIFIED: _ClassVar[Intent.Message.ColumnProperties.HorizontalAlignment]
                LEADING: _ClassVar[Intent.Message.ColumnProperties.HorizontalAlignment]
                CENTER: _ClassVar[Intent.Message.ColumnProperties.HorizontalAlignment]
                TRAILING: _ClassVar[Intent.Message.ColumnProperties.HorizontalAlignment]
            HORIZONTAL_ALIGNMENT_UNSPECIFIED: Intent.Message.ColumnProperties.HorizontalAlignment
            LEADING: Intent.Message.ColumnProperties.HorizontalAlignment
            CENTER: Intent.Message.ColumnProperties.HorizontalAlignment
            TRAILING: Intent.Message.ColumnProperties.HorizontalAlignment
            HEADER_FIELD_NUMBER: _ClassVar[int]
            HORIZONTAL_ALIGNMENT_FIELD_NUMBER: _ClassVar[int]
            header: str
            horizontal_alignment: Intent.Message.ColumnProperties.HorizontalAlignment

            def __init__(self, header: _Optional[str]=..., horizontal_alignment: _Optional[_Union[Intent.Message.ColumnProperties.HorizontalAlignment, str]]=...) -> None:
                ...

        class TableCardRow(_message.Message):
            __slots__ = ('cells', 'divider_after')
            CELLS_FIELD_NUMBER: _ClassVar[int]
            DIVIDER_AFTER_FIELD_NUMBER: _ClassVar[int]
            cells: _containers.RepeatedCompositeFieldContainer[Intent.Message.TableCardCell]
            divider_after: bool

            def __init__(self, cells: _Optional[_Iterable[_Union[Intent.Message.TableCardCell, _Mapping]]]=..., divider_after: bool=...) -> None:
                ...

        class TableCardCell(_message.Message):
            __slots__ = ('text',)
            TEXT_FIELD_NUMBER: _ClassVar[int]
            text: str

            def __init__(self, text: _Optional[str]=...) -> None:
                ...
        TEXT_FIELD_NUMBER: _ClassVar[int]
        IMAGE_FIELD_NUMBER: _ClassVar[int]
        QUICK_REPLIES_FIELD_NUMBER: _ClassVar[int]
        CARD_FIELD_NUMBER: _ClassVar[int]
        PAYLOAD_FIELD_NUMBER: _ClassVar[int]
        SIMPLE_RESPONSES_FIELD_NUMBER: _ClassVar[int]
        BASIC_CARD_FIELD_NUMBER: _ClassVar[int]
        SUGGESTIONS_FIELD_NUMBER: _ClassVar[int]
        LINK_OUT_SUGGESTION_FIELD_NUMBER: _ClassVar[int]
        LIST_SELECT_FIELD_NUMBER: _ClassVar[int]
        CAROUSEL_SELECT_FIELD_NUMBER: _ClassVar[int]
        BROWSE_CAROUSEL_CARD_FIELD_NUMBER: _ClassVar[int]
        TABLE_CARD_FIELD_NUMBER: _ClassVar[int]
        MEDIA_CONTENT_FIELD_NUMBER: _ClassVar[int]
        PLATFORM_FIELD_NUMBER: _ClassVar[int]
        text: Intent.Message.Text
        image: Intent.Message.Image
        quick_replies: Intent.Message.QuickReplies
        card: Intent.Message.Card
        payload: _struct_pb2.Struct
        simple_responses: Intent.Message.SimpleResponses
        basic_card: Intent.Message.BasicCard
        suggestions: Intent.Message.Suggestions
        link_out_suggestion: Intent.Message.LinkOutSuggestion
        list_select: Intent.Message.ListSelect
        carousel_select: Intent.Message.CarouselSelect
        browse_carousel_card: Intent.Message.BrowseCarouselCard
        table_card: Intent.Message.TableCard
        media_content: Intent.Message.MediaContent
        platform: Intent.Message.Platform

        def __init__(self, text: _Optional[_Union[Intent.Message.Text, _Mapping]]=..., image: _Optional[_Union[Intent.Message.Image, _Mapping]]=..., quick_replies: _Optional[_Union[Intent.Message.QuickReplies, _Mapping]]=..., card: _Optional[_Union[Intent.Message.Card, _Mapping]]=..., payload: _Optional[_Union[_struct_pb2.Struct, _Mapping]]=..., simple_responses: _Optional[_Union[Intent.Message.SimpleResponses, _Mapping]]=..., basic_card: _Optional[_Union[Intent.Message.BasicCard, _Mapping]]=..., suggestions: _Optional[_Union[Intent.Message.Suggestions, _Mapping]]=..., link_out_suggestion: _Optional[_Union[Intent.Message.LinkOutSuggestion, _Mapping]]=..., list_select: _Optional[_Union[Intent.Message.ListSelect, _Mapping]]=..., carousel_select: _Optional[_Union[Intent.Message.CarouselSelect, _Mapping]]=..., browse_carousel_card: _Optional[_Union[Intent.Message.BrowseCarouselCard, _Mapping]]=..., table_card: _Optional[_Union[Intent.Message.TableCard, _Mapping]]=..., media_content: _Optional[_Union[Intent.Message.MediaContent, _Mapping]]=..., platform: _Optional[_Union[Intent.Message.Platform, str]]=...) -> None:
            ...

    class FollowupIntentInfo(_message.Message):
        __slots__ = ('followup_intent_name', 'parent_followup_intent_name')
        FOLLOWUP_INTENT_NAME_FIELD_NUMBER: _ClassVar[int]
        PARENT_FOLLOWUP_INTENT_NAME_FIELD_NUMBER: _ClassVar[int]
        followup_intent_name: str
        parent_followup_intent_name: str

        def __init__(self, followup_intent_name: _Optional[str]=..., parent_followup_intent_name: _Optional[str]=...) -> None:
            ...
    NAME_FIELD_NUMBER: _ClassVar[int]
    DISPLAY_NAME_FIELD_NUMBER: _ClassVar[int]
    WEBHOOK_STATE_FIELD_NUMBER: _ClassVar[int]
    PRIORITY_FIELD_NUMBER: _ClassVar[int]
    IS_FALLBACK_FIELD_NUMBER: _ClassVar[int]
    ML_DISABLED_FIELD_NUMBER: _ClassVar[int]
    LIVE_AGENT_HANDOFF_FIELD_NUMBER: _ClassVar[int]
    END_INTERACTION_FIELD_NUMBER: _ClassVar[int]
    INPUT_CONTEXT_NAMES_FIELD_NUMBER: _ClassVar[int]
    EVENTS_FIELD_NUMBER: _ClassVar[int]
    TRAINING_PHRASES_FIELD_NUMBER: _ClassVar[int]
    ACTION_FIELD_NUMBER: _ClassVar[int]
    OUTPUT_CONTEXTS_FIELD_NUMBER: _ClassVar[int]
    RESET_CONTEXTS_FIELD_NUMBER: _ClassVar[int]
    PARAMETERS_FIELD_NUMBER: _ClassVar[int]
    MESSAGES_FIELD_NUMBER: _ClassVar[int]
    DEFAULT_RESPONSE_PLATFORMS_FIELD_NUMBER: _ClassVar[int]
    ROOT_FOLLOWUP_INTENT_NAME_FIELD_NUMBER: _ClassVar[int]
    PARENT_FOLLOWUP_INTENT_NAME_FIELD_NUMBER: _ClassVar[int]
    FOLLOWUP_INTENT_INFO_FIELD_NUMBER: _ClassVar[int]
    name: str
    display_name: str
    webhook_state: Intent.WebhookState
    priority: int
    is_fallback: bool
    ml_disabled: bool
    live_agent_handoff: bool
    end_interaction: bool
    input_context_names: _containers.RepeatedScalarFieldContainer[str]
    events: _containers.RepeatedScalarFieldContainer[str]
    training_phrases: _containers.RepeatedCompositeFieldContainer[Intent.TrainingPhrase]
    action: str
    output_contexts: _containers.RepeatedCompositeFieldContainer[_context_pb2.Context]
    reset_contexts: bool
    parameters: _containers.RepeatedCompositeFieldContainer[Intent.Parameter]
    messages: _containers.RepeatedCompositeFieldContainer[Intent.Message]
    default_response_platforms: _containers.RepeatedScalarFieldContainer[Intent.Message.Platform]
    root_followup_intent_name: str
    parent_followup_intent_name: str
    followup_intent_info: _containers.RepeatedCompositeFieldContainer[Intent.FollowupIntentInfo]

    def __init__(self, name: _Optional[str]=..., display_name: _Optional[str]=..., webhook_state: _Optional[_Union[Intent.WebhookState, str]]=..., priority: _Optional[int]=..., is_fallback: bool=..., ml_disabled: bool=..., live_agent_handoff: bool=..., end_interaction: bool=..., input_context_names: _Optional[_Iterable[str]]=..., events: _Optional[_Iterable[str]]=..., training_phrases: _Optional[_Iterable[_Union[Intent.TrainingPhrase, _Mapping]]]=..., action: _Optional[str]=..., output_contexts: _Optional[_Iterable[_Union[_context_pb2.Context, _Mapping]]]=..., reset_contexts: bool=..., parameters: _Optional[_Iterable[_Union[Intent.Parameter, _Mapping]]]=..., messages: _Optional[_Iterable[_Union[Intent.Message, _Mapping]]]=..., default_response_platforms: _Optional[_Iterable[_Union[Intent.Message.Platform, str]]]=..., root_followup_intent_name: _Optional[str]=..., parent_followup_intent_name: _Optional[str]=..., followup_intent_info: _Optional[_Iterable[_Union[Intent.FollowupIntentInfo, _Mapping]]]=...) -> None:
        ...

class ListIntentsRequest(_message.Message):
    __slots__ = ('parent', 'language_code', 'intent_view', 'page_size', 'page_token')
    PARENT_FIELD_NUMBER: _ClassVar[int]
    LANGUAGE_CODE_FIELD_NUMBER: _ClassVar[int]
    INTENT_VIEW_FIELD_NUMBER: _ClassVar[int]
    PAGE_SIZE_FIELD_NUMBER: _ClassVar[int]
    PAGE_TOKEN_FIELD_NUMBER: _ClassVar[int]
    parent: str
    language_code: str
    intent_view: IntentView
    page_size: int
    page_token: str

    def __init__(self, parent: _Optional[str]=..., language_code: _Optional[str]=..., intent_view: _Optional[_Union[IntentView, str]]=..., page_size: _Optional[int]=..., page_token: _Optional[str]=...) -> None:
        ...

class ListIntentsResponse(_message.Message):
    __slots__ = ('intents', 'next_page_token')
    INTENTS_FIELD_NUMBER: _ClassVar[int]
    NEXT_PAGE_TOKEN_FIELD_NUMBER: _ClassVar[int]
    intents: _containers.RepeatedCompositeFieldContainer[Intent]
    next_page_token: str

    def __init__(self, intents: _Optional[_Iterable[_Union[Intent, _Mapping]]]=..., next_page_token: _Optional[str]=...) -> None:
        ...

class GetIntentRequest(_message.Message):
    __slots__ = ('name', 'language_code', 'intent_view')
    NAME_FIELD_NUMBER: _ClassVar[int]
    LANGUAGE_CODE_FIELD_NUMBER: _ClassVar[int]
    INTENT_VIEW_FIELD_NUMBER: _ClassVar[int]
    name: str
    language_code: str
    intent_view: IntentView

    def __init__(self, name: _Optional[str]=..., language_code: _Optional[str]=..., intent_view: _Optional[_Union[IntentView, str]]=...) -> None:
        ...

class CreateIntentRequest(_message.Message):
    __slots__ = ('parent', 'intent', 'language_code', 'intent_view')
    PARENT_FIELD_NUMBER: _ClassVar[int]
    INTENT_FIELD_NUMBER: _ClassVar[int]
    LANGUAGE_CODE_FIELD_NUMBER: _ClassVar[int]
    INTENT_VIEW_FIELD_NUMBER: _ClassVar[int]
    parent: str
    intent: Intent
    language_code: str
    intent_view: IntentView

    def __init__(self, parent: _Optional[str]=..., intent: _Optional[_Union[Intent, _Mapping]]=..., language_code: _Optional[str]=..., intent_view: _Optional[_Union[IntentView, str]]=...) -> None:
        ...

class UpdateIntentRequest(_message.Message):
    __slots__ = ('intent', 'language_code', 'update_mask', 'intent_view')
    INTENT_FIELD_NUMBER: _ClassVar[int]
    LANGUAGE_CODE_FIELD_NUMBER: _ClassVar[int]
    UPDATE_MASK_FIELD_NUMBER: _ClassVar[int]
    INTENT_VIEW_FIELD_NUMBER: _ClassVar[int]
    intent: Intent
    language_code: str
    update_mask: _field_mask_pb2.FieldMask
    intent_view: IntentView

    def __init__(self, intent: _Optional[_Union[Intent, _Mapping]]=..., language_code: _Optional[str]=..., update_mask: _Optional[_Union[_field_mask_pb2.FieldMask, _Mapping]]=..., intent_view: _Optional[_Union[IntentView, str]]=...) -> None:
        ...

class DeleteIntentRequest(_message.Message):
    __slots__ = ('name',)
    NAME_FIELD_NUMBER: _ClassVar[int]
    name: str

    def __init__(self, name: _Optional[str]=...) -> None:
        ...

class BatchUpdateIntentsRequest(_message.Message):
    __slots__ = ('parent', 'intent_batch_uri', 'intent_batch_inline', 'language_code', 'update_mask', 'intent_view')
    PARENT_FIELD_NUMBER: _ClassVar[int]
    INTENT_BATCH_URI_FIELD_NUMBER: _ClassVar[int]
    INTENT_BATCH_INLINE_FIELD_NUMBER: _ClassVar[int]
    LANGUAGE_CODE_FIELD_NUMBER: _ClassVar[int]
    UPDATE_MASK_FIELD_NUMBER: _ClassVar[int]
    INTENT_VIEW_FIELD_NUMBER: _ClassVar[int]
    parent: str
    intent_batch_uri: str
    intent_batch_inline: IntentBatch
    language_code: str
    update_mask: _field_mask_pb2.FieldMask
    intent_view: IntentView

    def __init__(self, parent: _Optional[str]=..., intent_batch_uri: _Optional[str]=..., intent_batch_inline: _Optional[_Union[IntentBatch, _Mapping]]=..., language_code: _Optional[str]=..., update_mask: _Optional[_Union[_field_mask_pb2.FieldMask, _Mapping]]=..., intent_view: _Optional[_Union[IntentView, str]]=...) -> None:
        ...

class BatchUpdateIntentsResponse(_message.Message):
    __slots__ = ('intents',)
    INTENTS_FIELD_NUMBER: _ClassVar[int]
    intents: _containers.RepeatedCompositeFieldContainer[Intent]

    def __init__(self, intents: _Optional[_Iterable[_Union[Intent, _Mapping]]]=...) -> None:
        ...

class BatchDeleteIntentsRequest(_message.Message):
    __slots__ = ('parent', 'intents')
    PARENT_FIELD_NUMBER: _ClassVar[int]
    INTENTS_FIELD_NUMBER: _ClassVar[int]
    parent: str
    intents: _containers.RepeatedCompositeFieldContainer[Intent]

    def __init__(self, parent: _Optional[str]=..., intents: _Optional[_Iterable[_Union[Intent, _Mapping]]]=...) -> None:
        ...

class IntentBatch(_message.Message):
    __slots__ = ('intents',)
    INTENTS_FIELD_NUMBER: _ClassVar[int]
    intents: _containers.RepeatedCompositeFieldContainer[Intent]

    def __init__(self, intents: _Optional[_Iterable[_Union[Intent, _Mapping]]]=...) -> None:
        ...