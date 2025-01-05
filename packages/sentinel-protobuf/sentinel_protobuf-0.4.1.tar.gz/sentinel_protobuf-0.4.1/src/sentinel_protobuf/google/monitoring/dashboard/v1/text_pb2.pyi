from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Mapping as _Mapping, Optional as _Optional, Union as _Union
DESCRIPTOR: _descriptor.FileDescriptor

class Text(_message.Message):
    __slots__ = ('content', 'format', 'style')

    class Format(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        FORMAT_UNSPECIFIED: _ClassVar[Text.Format]
        MARKDOWN: _ClassVar[Text.Format]
        RAW: _ClassVar[Text.Format]
    FORMAT_UNSPECIFIED: Text.Format
    MARKDOWN: Text.Format
    RAW: Text.Format

    class TextStyle(_message.Message):
        __slots__ = ('background_color', 'text_color', 'horizontal_alignment', 'vertical_alignment', 'padding', 'font_size', 'pointer_location')

        class HorizontalAlignment(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
            __slots__ = ()
            HORIZONTAL_ALIGNMENT_UNSPECIFIED: _ClassVar[Text.TextStyle.HorizontalAlignment]
            H_LEFT: _ClassVar[Text.TextStyle.HorizontalAlignment]
            H_CENTER: _ClassVar[Text.TextStyle.HorizontalAlignment]
            H_RIGHT: _ClassVar[Text.TextStyle.HorizontalAlignment]
        HORIZONTAL_ALIGNMENT_UNSPECIFIED: Text.TextStyle.HorizontalAlignment
        H_LEFT: Text.TextStyle.HorizontalAlignment
        H_CENTER: Text.TextStyle.HorizontalAlignment
        H_RIGHT: Text.TextStyle.HorizontalAlignment

        class VerticalAlignment(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
            __slots__ = ()
            VERTICAL_ALIGNMENT_UNSPECIFIED: _ClassVar[Text.TextStyle.VerticalAlignment]
            V_TOP: _ClassVar[Text.TextStyle.VerticalAlignment]
            V_CENTER: _ClassVar[Text.TextStyle.VerticalAlignment]
            V_BOTTOM: _ClassVar[Text.TextStyle.VerticalAlignment]
        VERTICAL_ALIGNMENT_UNSPECIFIED: Text.TextStyle.VerticalAlignment
        V_TOP: Text.TextStyle.VerticalAlignment
        V_CENTER: Text.TextStyle.VerticalAlignment
        V_BOTTOM: Text.TextStyle.VerticalAlignment

        class PaddingSize(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
            __slots__ = ()
            PADDING_SIZE_UNSPECIFIED: _ClassVar[Text.TextStyle.PaddingSize]
            P_EXTRA_SMALL: _ClassVar[Text.TextStyle.PaddingSize]
            P_SMALL: _ClassVar[Text.TextStyle.PaddingSize]
            P_MEDIUM: _ClassVar[Text.TextStyle.PaddingSize]
            P_LARGE: _ClassVar[Text.TextStyle.PaddingSize]
            P_EXTRA_LARGE: _ClassVar[Text.TextStyle.PaddingSize]
        PADDING_SIZE_UNSPECIFIED: Text.TextStyle.PaddingSize
        P_EXTRA_SMALL: Text.TextStyle.PaddingSize
        P_SMALL: Text.TextStyle.PaddingSize
        P_MEDIUM: Text.TextStyle.PaddingSize
        P_LARGE: Text.TextStyle.PaddingSize
        P_EXTRA_LARGE: Text.TextStyle.PaddingSize

        class FontSize(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
            __slots__ = ()
            FONT_SIZE_UNSPECIFIED: _ClassVar[Text.TextStyle.FontSize]
            FS_EXTRA_SMALL: _ClassVar[Text.TextStyle.FontSize]
            FS_SMALL: _ClassVar[Text.TextStyle.FontSize]
            FS_MEDIUM: _ClassVar[Text.TextStyle.FontSize]
            FS_LARGE: _ClassVar[Text.TextStyle.FontSize]
            FS_EXTRA_LARGE: _ClassVar[Text.TextStyle.FontSize]
        FONT_SIZE_UNSPECIFIED: Text.TextStyle.FontSize
        FS_EXTRA_SMALL: Text.TextStyle.FontSize
        FS_SMALL: Text.TextStyle.FontSize
        FS_MEDIUM: Text.TextStyle.FontSize
        FS_LARGE: Text.TextStyle.FontSize
        FS_EXTRA_LARGE: Text.TextStyle.FontSize

        class PointerLocation(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
            __slots__ = ()
            POINTER_LOCATION_UNSPECIFIED: _ClassVar[Text.TextStyle.PointerLocation]
            PL_TOP: _ClassVar[Text.TextStyle.PointerLocation]
            PL_RIGHT: _ClassVar[Text.TextStyle.PointerLocation]
            PL_BOTTOM: _ClassVar[Text.TextStyle.PointerLocation]
            PL_LEFT: _ClassVar[Text.TextStyle.PointerLocation]
            PL_TOP_LEFT: _ClassVar[Text.TextStyle.PointerLocation]
            PL_TOP_RIGHT: _ClassVar[Text.TextStyle.PointerLocation]
            PL_RIGHT_TOP: _ClassVar[Text.TextStyle.PointerLocation]
            PL_RIGHT_BOTTOM: _ClassVar[Text.TextStyle.PointerLocation]
            PL_BOTTOM_RIGHT: _ClassVar[Text.TextStyle.PointerLocation]
            PL_BOTTOM_LEFT: _ClassVar[Text.TextStyle.PointerLocation]
            PL_LEFT_BOTTOM: _ClassVar[Text.TextStyle.PointerLocation]
            PL_LEFT_TOP: _ClassVar[Text.TextStyle.PointerLocation]
        POINTER_LOCATION_UNSPECIFIED: Text.TextStyle.PointerLocation
        PL_TOP: Text.TextStyle.PointerLocation
        PL_RIGHT: Text.TextStyle.PointerLocation
        PL_BOTTOM: Text.TextStyle.PointerLocation
        PL_LEFT: Text.TextStyle.PointerLocation
        PL_TOP_LEFT: Text.TextStyle.PointerLocation
        PL_TOP_RIGHT: Text.TextStyle.PointerLocation
        PL_RIGHT_TOP: Text.TextStyle.PointerLocation
        PL_RIGHT_BOTTOM: Text.TextStyle.PointerLocation
        PL_BOTTOM_RIGHT: Text.TextStyle.PointerLocation
        PL_BOTTOM_LEFT: Text.TextStyle.PointerLocation
        PL_LEFT_BOTTOM: Text.TextStyle.PointerLocation
        PL_LEFT_TOP: Text.TextStyle.PointerLocation
        BACKGROUND_COLOR_FIELD_NUMBER: _ClassVar[int]
        TEXT_COLOR_FIELD_NUMBER: _ClassVar[int]
        HORIZONTAL_ALIGNMENT_FIELD_NUMBER: _ClassVar[int]
        VERTICAL_ALIGNMENT_FIELD_NUMBER: _ClassVar[int]
        PADDING_FIELD_NUMBER: _ClassVar[int]
        FONT_SIZE_FIELD_NUMBER: _ClassVar[int]
        POINTER_LOCATION_FIELD_NUMBER: _ClassVar[int]
        background_color: str
        text_color: str
        horizontal_alignment: Text.TextStyle.HorizontalAlignment
        vertical_alignment: Text.TextStyle.VerticalAlignment
        padding: Text.TextStyle.PaddingSize
        font_size: Text.TextStyle.FontSize
        pointer_location: Text.TextStyle.PointerLocation

        def __init__(self, background_color: _Optional[str]=..., text_color: _Optional[str]=..., horizontal_alignment: _Optional[_Union[Text.TextStyle.HorizontalAlignment, str]]=..., vertical_alignment: _Optional[_Union[Text.TextStyle.VerticalAlignment, str]]=..., padding: _Optional[_Union[Text.TextStyle.PaddingSize, str]]=..., font_size: _Optional[_Union[Text.TextStyle.FontSize, str]]=..., pointer_location: _Optional[_Union[Text.TextStyle.PointerLocation, str]]=...) -> None:
            ...
    CONTENT_FIELD_NUMBER: _ClassVar[int]
    FORMAT_FIELD_NUMBER: _ClassVar[int]
    STYLE_FIELD_NUMBER: _ClassVar[int]
    content: str
    format: Text.Format
    style: Text.TextStyle

    def __init__(self, content: _Optional[str]=..., format: _Optional[_Union[Text.Format, str]]=..., style: _Optional[_Union[Text.TextStyle, _Mapping]]=...) -> None:
        ...