from google.chat.v1 import widgets_pb2 as _widgets_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union
DESCRIPTOR: _descriptor.FileDescriptor

class ContextualAddOnMarkup(_message.Message):
    __slots__ = ()

    class Card(_message.Message):
        __slots__ = ('header', 'sections', 'card_actions', 'name')

        class CardHeader(_message.Message):
            __slots__ = ('title', 'subtitle', 'image_style', 'image_url')

            class ImageStyle(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
                __slots__ = ()
                IMAGE_STYLE_UNSPECIFIED: _ClassVar[ContextualAddOnMarkup.Card.CardHeader.ImageStyle]
                IMAGE: _ClassVar[ContextualAddOnMarkup.Card.CardHeader.ImageStyle]
                AVATAR: _ClassVar[ContextualAddOnMarkup.Card.CardHeader.ImageStyle]
            IMAGE_STYLE_UNSPECIFIED: ContextualAddOnMarkup.Card.CardHeader.ImageStyle
            IMAGE: ContextualAddOnMarkup.Card.CardHeader.ImageStyle
            AVATAR: ContextualAddOnMarkup.Card.CardHeader.ImageStyle
            TITLE_FIELD_NUMBER: _ClassVar[int]
            SUBTITLE_FIELD_NUMBER: _ClassVar[int]
            IMAGE_STYLE_FIELD_NUMBER: _ClassVar[int]
            IMAGE_URL_FIELD_NUMBER: _ClassVar[int]
            title: str
            subtitle: str
            image_style: ContextualAddOnMarkup.Card.CardHeader.ImageStyle
            image_url: str

            def __init__(self, title: _Optional[str]=..., subtitle: _Optional[str]=..., image_style: _Optional[_Union[ContextualAddOnMarkup.Card.CardHeader.ImageStyle, str]]=..., image_url: _Optional[str]=...) -> None:
                ...

        class Section(_message.Message):
            __slots__ = ('header', 'widgets')
            HEADER_FIELD_NUMBER: _ClassVar[int]
            WIDGETS_FIELD_NUMBER: _ClassVar[int]
            header: str
            widgets: _containers.RepeatedCompositeFieldContainer[_widgets_pb2.WidgetMarkup]

            def __init__(self, header: _Optional[str]=..., widgets: _Optional[_Iterable[_Union[_widgets_pb2.WidgetMarkup, _Mapping]]]=...) -> None:
                ...

        class CardAction(_message.Message):
            __slots__ = ('action_label', 'on_click')
            ACTION_LABEL_FIELD_NUMBER: _ClassVar[int]
            ON_CLICK_FIELD_NUMBER: _ClassVar[int]
            action_label: str
            on_click: _widgets_pb2.WidgetMarkup.OnClick

            def __init__(self, action_label: _Optional[str]=..., on_click: _Optional[_Union[_widgets_pb2.WidgetMarkup.OnClick, _Mapping]]=...) -> None:
                ...
        HEADER_FIELD_NUMBER: _ClassVar[int]
        SECTIONS_FIELD_NUMBER: _ClassVar[int]
        CARD_ACTIONS_FIELD_NUMBER: _ClassVar[int]
        NAME_FIELD_NUMBER: _ClassVar[int]
        header: ContextualAddOnMarkup.Card.CardHeader
        sections: _containers.RepeatedCompositeFieldContainer[ContextualAddOnMarkup.Card.Section]
        card_actions: _containers.RepeatedCompositeFieldContainer[ContextualAddOnMarkup.Card.CardAction]
        name: str

        def __init__(self, header: _Optional[_Union[ContextualAddOnMarkup.Card.CardHeader, _Mapping]]=..., sections: _Optional[_Iterable[_Union[ContextualAddOnMarkup.Card.Section, _Mapping]]]=..., card_actions: _Optional[_Iterable[_Union[ContextualAddOnMarkup.Card.CardAction, _Mapping]]]=..., name: _Optional[str]=...) -> None:
            ...

    def __init__(self) -> None:
        ...