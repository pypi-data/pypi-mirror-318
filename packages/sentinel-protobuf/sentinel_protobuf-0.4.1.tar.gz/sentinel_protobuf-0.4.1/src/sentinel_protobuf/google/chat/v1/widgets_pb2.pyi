from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union
DESCRIPTOR: _descriptor.FileDescriptor

class WidgetMarkup(_message.Message):
    __slots__ = ('text_paragraph', 'image', 'key_value', 'buttons')

    class Icon(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        ICON_UNSPECIFIED: _ClassVar[WidgetMarkup.Icon]
        AIRPLANE: _ClassVar[WidgetMarkup.Icon]
        BOOKMARK: _ClassVar[WidgetMarkup.Icon]
        BUS: _ClassVar[WidgetMarkup.Icon]
        CAR: _ClassVar[WidgetMarkup.Icon]
        CLOCK: _ClassVar[WidgetMarkup.Icon]
        CONFIRMATION_NUMBER_ICON: _ClassVar[WidgetMarkup.Icon]
        DOLLAR: _ClassVar[WidgetMarkup.Icon]
        DESCRIPTION: _ClassVar[WidgetMarkup.Icon]
        EMAIL: _ClassVar[WidgetMarkup.Icon]
        EVENT_PERFORMER: _ClassVar[WidgetMarkup.Icon]
        EVENT_SEAT: _ClassVar[WidgetMarkup.Icon]
        FLIGHT_ARRIVAL: _ClassVar[WidgetMarkup.Icon]
        FLIGHT_DEPARTURE: _ClassVar[WidgetMarkup.Icon]
        HOTEL: _ClassVar[WidgetMarkup.Icon]
        HOTEL_ROOM_TYPE: _ClassVar[WidgetMarkup.Icon]
        INVITE: _ClassVar[WidgetMarkup.Icon]
        MAP_PIN: _ClassVar[WidgetMarkup.Icon]
        MEMBERSHIP: _ClassVar[WidgetMarkup.Icon]
        MULTIPLE_PEOPLE: _ClassVar[WidgetMarkup.Icon]
        OFFER: _ClassVar[WidgetMarkup.Icon]
        PERSON: _ClassVar[WidgetMarkup.Icon]
        PHONE: _ClassVar[WidgetMarkup.Icon]
        RESTAURANT_ICON: _ClassVar[WidgetMarkup.Icon]
        SHOPPING_CART: _ClassVar[WidgetMarkup.Icon]
        STAR: _ClassVar[WidgetMarkup.Icon]
        STORE: _ClassVar[WidgetMarkup.Icon]
        TICKET: _ClassVar[WidgetMarkup.Icon]
        TRAIN: _ClassVar[WidgetMarkup.Icon]
        VIDEO_CAMERA: _ClassVar[WidgetMarkup.Icon]
        VIDEO_PLAY: _ClassVar[WidgetMarkup.Icon]
    ICON_UNSPECIFIED: WidgetMarkup.Icon
    AIRPLANE: WidgetMarkup.Icon
    BOOKMARK: WidgetMarkup.Icon
    BUS: WidgetMarkup.Icon
    CAR: WidgetMarkup.Icon
    CLOCK: WidgetMarkup.Icon
    CONFIRMATION_NUMBER_ICON: WidgetMarkup.Icon
    DOLLAR: WidgetMarkup.Icon
    DESCRIPTION: WidgetMarkup.Icon
    EMAIL: WidgetMarkup.Icon
    EVENT_PERFORMER: WidgetMarkup.Icon
    EVENT_SEAT: WidgetMarkup.Icon
    FLIGHT_ARRIVAL: WidgetMarkup.Icon
    FLIGHT_DEPARTURE: WidgetMarkup.Icon
    HOTEL: WidgetMarkup.Icon
    HOTEL_ROOM_TYPE: WidgetMarkup.Icon
    INVITE: WidgetMarkup.Icon
    MAP_PIN: WidgetMarkup.Icon
    MEMBERSHIP: WidgetMarkup.Icon
    MULTIPLE_PEOPLE: WidgetMarkup.Icon
    OFFER: WidgetMarkup.Icon
    PERSON: WidgetMarkup.Icon
    PHONE: WidgetMarkup.Icon
    RESTAURANT_ICON: WidgetMarkup.Icon
    SHOPPING_CART: WidgetMarkup.Icon
    STAR: WidgetMarkup.Icon
    STORE: WidgetMarkup.Icon
    TICKET: WidgetMarkup.Icon
    TRAIN: WidgetMarkup.Icon
    VIDEO_CAMERA: WidgetMarkup.Icon
    VIDEO_PLAY: WidgetMarkup.Icon

    class TextParagraph(_message.Message):
        __slots__ = ('text',)
        TEXT_FIELD_NUMBER: _ClassVar[int]
        text: str

        def __init__(self, text: _Optional[str]=...) -> None:
            ...

    class Button(_message.Message):
        __slots__ = ('text_button', 'image_button')
        TEXT_BUTTON_FIELD_NUMBER: _ClassVar[int]
        IMAGE_BUTTON_FIELD_NUMBER: _ClassVar[int]
        text_button: WidgetMarkup.TextButton
        image_button: WidgetMarkup.ImageButton

        def __init__(self, text_button: _Optional[_Union[WidgetMarkup.TextButton, _Mapping]]=..., image_button: _Optional[_Union[WidgetMarkup.ImageButton, _Mapping]]=...) -> None:
            ...

    class TextButton(_message.Message):
        __slots__ = ('text', 'on_click')
        TEXT_FIELD_NUMBER: _ClassVar[int]
        ON_CLICK_FIELD_NUMBER: _ClassVar[int]
        text: str
        on_click: WidgetMarkup.OnClick

        def __init__(self, text: _Optional[str]=..., on_click: _Optional[_Union[WidgetMarkup.OnClick, _Mapping]]=...) -> None:
            ...

    class KeyValue(_message.Message):
        __slots__ = ('icon', 'icon_url', 'top_label', 'content', 'content_multiline', 'bottom_label', 'on_click', 'button')
        ICON_FIELD_NUMBER: _ClassVar[int]
        ICON_URL_FIELD_NUMBER: _ClassVar[int]
        TOP_LABEL_FIELD_NUMBER: _ClassVar[int]
        CONTENT_FIELD_NUMBER: _ClassVar[int]
        CONTENT_MULTILINE_FIELD_NUMBER: _ClassVar[int]
        BOTTOM_LABEL_FIELD_NUMBER: _ClassVar[int]
        ON_CLICK_FIELD_NUMBER: _ClassVar[int]
        BUTTON_FIELD_NUMBER: _ClassVar[int]
        icon: WidgetMarkup.Icon
        icon_url: str
        top_label: str
        content: str
        content_multiline: bool
        bottom_label: str
        on_click: WidgetMarkup.OnClick
        button: WidgetMarkup.Button

        def __init__(self, icon: _Optional[_Union[WidgetMarkup.Icon, str]]=..., icon_url: _Optional[str]=..., top_label: _Optional[str]=..., content: _Optional[str]=..., content_multiline: bool=..., bottom_label: _Optional[str]=..., on_click: _Optional[_Union[WidgetMarkup.OnClick, _Mapping]]=..., button: _Optional[_Union[WidgetMarkup.Button, _Mapping]]=...) -> None:
            ...

    class Image(_message.Message):
        __slots__ = ('image_url', 'on_click', 'aspect_ratio')
        IMAGE_URL_FIELD_NUMBER: _ClassVar[int]
        ON_CLICK_FIELD_NUMBER: _ClassVar[int]
        ASPECT_RATIO_FIELD_NUMBER: _ClassVar[int]
        image_url: str
        on_click: WidgetMarkup.OnClick
        aspect_ratio: float

        def __init__(self, image_url: _Optional[str]=..., on_click: _Optional[_Union[WidgetMarkup.OnClick, _Mapping]]=..., aspect_ratio: _Optional[float]=...) -> None:
            ...

    class ImageButton(_message.Message):
        __slots__ = ('icon', 'icon_url', 'on_click', 'name')
        ICON_FIELD_NUMBER: _ClassVar[int]
        ICON_URL_FIELD_NUMBER: _ClassVar[int]
        ON_CLICK_FIELD_NUMBER: _ClassVar[int]
        NAME_FIELD_NUMBER: _ClassVar[int]
        icon: WidgetMarkup.Icon
        icon_url: str
        on_click: WidgetMarkup.OnClick
        name: str

        def __init__(self, icon: _Optional[_Union[WidgetMarkup.Icon, str]]=..., icon_url: _Optional[str]=..., on_click: _Optional[_Union[WidgetMarkup.OnClick, _Mapping]]=..., name: _Optional[str]=...) -> None:
            ...

    class OnClick(_message.Message):
        __slots__ = ('action', 'open_link')
        ACTION_FIELD_NUMBER: _ClassVar[int]
        OPEN_LINK_FIELD_NUMBER: _ClassVar[int]
        action: WidgetMarkup.FormAction
        open_link: WidgetMarkup.OpenLink

        def __init__(self, action: _Optional[_Union[WidgetMarkup.FormAction, _Mapping]]=..., open_link: _Optional[_Union[WidgetMarkup.OpenLink, _Mapping]]=...) -> None:
            ...

    class OpenLink(_message.Message):
        __slots__ = ('url',)
        URL_FIELD_NUMBER: _ClassVar[int]
        url: str

        def __init__(self, url: _Optional[str]=...) -> None:
            ...

    class FormAction(_message.Message):
        __slots__ = ('action_method_name', 'parameters')

        class ActionParameter(_message.Message):
            __slots__ = ('key', 'value')
            KEY_FIELD_NUMBER: _ClassVar[int]
            VALUE_FIELD_NUMBER: _ClassVar[int]
            key: str
            value: str

            def __init__(self, key: _Optional[str]=..., value: _Optional[str]=...) -> None:
                ...
        ACTION_METHOD_NAME_FIELD_NUMBER: _ClassVar[int]
        PARAMETERS_FIELD_NUMBER: _ClassVar[int]
        action_method_name: str
        parameters: _containers.RepeatedCompositeFieldContainer[WidgetMarkup.FormAction.ActionParameter]

        def __init__(self, action_method_name: _Optional[str]=..., parameters: _Optional[_Iterable[_Union[WidgetMarkup.FormAction.ActionParameter, _Mapping]]]=...) -> None:
            ...
    TEXT_PARAGRAPH_FIELD_NUMBER: _ClassVar[int]
    IMAGE_FIELD_NUMBER: _ClassVar[int]
    KEY_VALUE_FIELD_NUMBER: _ClassVar[int]
    BUTTONS_FIELD_NUMBER: _ClassVar[int]
    text_paragraph: WidgetMarkup.TextParagraph
    image: WidgetMarkup.Image
    key_value: WidgetMarkup.KeyValue
    buttons: _containers.RepeatedCompositeFieldContainer[WidgetMarkup.Button]

    def __init__(self, text_paragraph: _Optional[_Union[WidgetMarkup.TextParagraph, _Mapping]]=..., image: _Optional[_Union[WidgetMarkup.Image, _Mapping]]=..., key_value: _Optional[_Union[WidgetMarkup.KeyValue, _Mapping]]=..., buttons: _Optional[_Iterable[_Union[WidgetMarkup.Button, _Mapping]]]=...) -> None:
        ...