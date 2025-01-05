from google.api import field_behavior_pb2 as _field_behavior_pb2
from google.cloud.documentai.v1 import barcode_pb2 as _barcode_pb2
from google.cloud.documentai.v1 import geometry_pb2 as _geometry_pb2
from google.protobuf import timestamp_pb2 as _timestamp_pb2
from google.rpc import status_pb2 as _status_pb2
from google.type import color_pb2 as _color_pb2
from google.type import date_pb2 as _date_pb2
from google.type import datetime_pb2 as _datetime_pb2
from google.type import money_pb2 as _money_pb2
from google.type import postal_address_pb2 as _postal_address_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union
DESCRIPTOR: _descriptor.FileDescriptor

class Document(_message.Message):
    __slots__ = ('uri', 'content', 'mime_type', 'text', 'text_styles', 'pages', 'entities', 'entity_relations', 'text_changes', 'shard_info', 'error', 'revisions', 'document_layout', 'chunked_document')

    class ShardInfo(_message.Message):
        __slots__ = ('shard_index', 'shard_count', 'text_offset')
        SHARD_INDEX_FIELD_NUMBER: _ClassVar[int]
        SHARD_COUNT_FIELD_NUMBER: _ClassVar[int]
        TEXT_OFFSET_FIELD_NUMBER: _ClassVar[int]
        shard_index: int
        shard_count: int
        text_offset: int

        def __init__(self, shard_index: _Optional[int]=..., shard_count: _Optional[int]=..., text_offset: _Optional[int]=...) -> None:
            ...

    class Style(_message.Message):
        __slots__ = ('text_anchor', 'color', 'background_color', 'font_weight', 'text_style', 'text_decoration', 'font_size', 'font_family')

        class FontSize(_message.Message):
            __slots__ = ('size', 'unit')
            SIZE_FIELD_NUMBER: _ClassVar[int]
            UNIT_FIELD_NUMBER: _ClassVar[int]
            size: float
            unit: str

            def __init__(self, size: _Optional[float]=..., unit: _Optional[str]=...) -> None:
                ...
        TEXT_ANCHOR_FIELD_NUMBER: _ClassVar[int]
        COLOR_FIELD_NUMBER: _ClassVar[int]
        BACKGROUND_COLOR_FIELD_NUMBER: _ClassVar[int]
        FONT_WEIGHT_FIELD_NUMBER: _ClassVar[int]
        TEXT_STYLE_FIELD_NUMBER: _ClassVar[int]
        TEXT_DECORATION_FIELD_NUMBER: _ClassVar[int]
        FONT_SIZE_FIELD_NUMBER: _ClassVar[int]
        FONT_FAMILY_FIELD_NUMBER: _ClassVar[int]
        text_anchor: Document.TextAnchor
        color: _color_pb2.Color
        background_color: _color_pb2.Color
        font_weight: str
        text_style: str
        text_decoration: str
        font_size: Document.Style.FontSize
        font_family: str

        def __init__(self, text_anchor: _Optional[_Union[Document.TextAnchor, _Mapping]]=..., color: _Optional[_Union[_color_pb2.Color, _Mapping]]=..., background_color: _Optional[_Union[_color_pb2.Color, _Mapping]]=..., font_weight: _Optional[str]=..., text_style: _Optional[str]=..., text_decoration: _Optional[str]=..., font_size: _Optional[_Union[Document.Style.FontSize, _Mapping]]=..., font_family: _Optional[str]=...) -> None:
            ...

    class Page(_message.Message):
        __slots__ = ('page_number', 'image', 'transforms', 'dimension', 'layout', 'detected_languages', 'blocks', 'paragraphs', 'lines', 'tokens', 'visual_elements', 'tables', 'form_fields', 'symbols', 'detected_barcodes', 'image_quality_scores', 'provenance')

        class Dimension(_message.Message):
            __slots__ = ('width', 'height', 'unit')
            WIDTH_FIELD_NUMBER: _ClassVar[int]
            HEIGHT_FIELD_NUMBER: _ClassVar[int]
            UNIT_FIELD_NUMBER: _ClassVar[int]
            width: float
            height: float
            unit: str

            def __init__(self, width: _Optional[float]=..., height: _Optional[float]=..., unit: _Optional[str]=...) -> None:
                ...

        class Image(_message.Message):
            __slots__ = ('content', 'mime_type', 'width', 'height')
            CONTENT_FIELD_NUMBER: _ClassVar[int]
            MIME_TYPE_FIELD_NUMBER: _ClassVar[int]
            WIDTH_FIELD_NUMBER: _ClassVar[int]
            HEIGHT_FIELD_NUMBER: _ClassVar[int]
            content: bytes
            mime_type: str
            width: int
            height: int

            def __init__(self, content: _Optional[bytes]=..., mime_type: _Optional[str]=..., width: _Optional[int]=..., height: _Optional[int]=...) -> None:
                ...

        class Matrix(_message.Message):
            __slots__ = ('rows', 'cols', 'type', 'data')
            ROWS_FIELD_NUMBER: _ClassVar[int]
            COLS_FIELD_NUMBER: _ClassVar[int]
            TYPE_FIELD_NUMBER: _ClassVar[int]
            DATA_FIELD_NUMBER: _ClassVar[int]
            rows: int
            cols: int
            type: int
            data: bytes

            def __init__(self, rows: _Optional[int]=..., cols: _Optional[int]=..., type: _Optional[int]=..., data: _Optional[bytes]=...) -> None:
                ...

        class Layout(_message.Message):
            __slots__ = ('text_anchor', 'confidence', 'bounding_poly', 'orientation')

            class Orientation(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
                __slots__ = ()
                ORIENTATION_UNSPECIFIED: _ClassVar[Document.Page.Layout.Orientation]
                PAGE_UP: _ClassVar[Document.Page.Layout.Orientation]
                PAGE_RIGHT: _ClassVar[Document.Page.Layout.Orientation]
                PAGE_DOWN: _ClassVar[Document.Page.Layout.Orientation]
                PAGE_LEFT: _ClassVar[Document.Page.Layout.Orientation]
            ORIENTATION_UNSPECIFIED: Document.Page.Layout.Orientation
            PAGE_UP: Document.Page.Layout.Orientation
            PAGE_RIGHT: Document.Page.Layout.Orientation
            PAGE_DOWN: Document.Page.Layout.Orientation
            PAGE_LEFT: Document.Page.Layout.Orientation
            TEXT_ANCHOR_FIELD_NUMBER: _ClassVar[int]
            CONFIDENCE_FIELD_NUMBER: _ClassVar[int]
            BOUNDING_POLY_FIELD_NUMBER: _ClassVar[int]
            ORIENTATION_FIELD_NUMBER: _ClassVar[int]
            text_anchor: Document.TextAnchor
            confidence: float
            bounding_poly: _geometry_pb2.BoundingPoly
            orientation: Document.Page.Layout.Orientation

            def __init__(self, text_anchor: _Optional[_Union[Document.TextAnchor, _Mapping]]=..., confidence: _Optional[float]=..., bounding_poly: _Optional[_Union[_geometry_pb2.BoundingPoly, _Mapping]]=..., orientation: _Optional[_Union[Document.Page.Layout.Orientation, str]]=...) -> None:
                ...

        class Block(_message.Message):
            __slots__ = ('layout', 'detected_languages', 'provenance')
            LAYOUT_FIELD_NUMBER: _ClassVar[int]
            DETECTED_LANGUAGES_FIELD_NUMBER: _ClassVar[int]
            PROVENANCE_FIELD_NUMBER: _ClassVar[int]
            layout: Document.Page.Layout
            detected_languages: _containers.RepeatedCompositeFieldContainer[Document.Page.DetectedLanguage]
            provenance: Document.Provenance

            def __init__(self, layout: _Optional[_Union[Document.Page.Layout, _Mapping]]=..., detected_languages: _Optional[_Iterable[_Union[Document.Page.DetectedLanguage, _Mapping]]]=..., provenance: _Optional[_Union[Document.Provenance, _Mapping]]=...) -> None:
                ...

        class Paragraph(_message.Message):
            __slots__ = ('layout', 'detected_languages', 'provenance')
            LAYOUT_FIELD_NUMBER: _ClassVar[int]
            DETECTED_LANGUAGES_FIELD_NUMBER: _ClassVar[int]
            PROVENANCE_FIELD_NUMBER: _ClassVar[int]
            layout: Document.Page.Layout
            detected_languages: _containers.RepeatedCompositeFieldContainer[Document.Page.DetectedLanguage]
            provenance: Document.Provenance

            def __init__(self, layout: _Optional[_Union[Document.Page.Layout, _Mapping]]=..., detected_languages: _Optional[_Iterable[_Union[Document.Page.DetectedLanguage, _Mapping]]]=..., provenance: _Optional[_Union[Document.Provenance, _Mapping]]=...) -> None:
                ...

        class Line(_message.Message):
            __slots__ = ('layout', 'detected_languages', 'provenance')
            LAYOUT_FIELD_NUMBER: _ClassVar[int]
            DETECTED_LANGUAGES_FIELD_NUMBER: _ClassVar[int]
            PROVENANCE_FIELD_NUMBER: _ClassVar[int]
            layout: Document.Page.Layout
            detected_languages: _containers.RepeatedCompositeFieldContainer[Document.Page.DetectedLanguage]
            provenance: Document.Provenance

            def __init__(self, layout: _Optional[_Union[Document.Page.Layout, _Mapping]]=..., detected_languages: _Optional[_Iterable[_Union[Document.Page.DetectedLanguage, _Mapping]]]=..., provenance: _Optional[_Union[Document.Provenance, _Mapping]]=...) -> None:
                ...

        class Token(_message.Message):
            __slots__ = ('layout', 'detected_break', 'detected_languages', 'provenance', 'style_info')

            class DetectedBreak(_message.Message):
                __slots__ = ('type',)

                class Type(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
                    __slots__ = ()
                    TYPE_UNSPECIFIED: _ClassVar[Document.Page.Token.DetectedBreak.Type]
                    SPACE: _ClassVar[Document.Page.Token.DetectedBreak.Type]
                    WIDE_SPACE: _ClassVar[Document.Page.Token.DetectedBreak.Type]
                    HYPHEN: _ClassVar[Document.Page.Token.DetectedBreak.Type]
                TYPE_UNSPECIFIED: Document.Page.Token.DetectedBreak.Type
                SPACE: Document.Page.Token.DetectedBreak.Type
                WIDE_SPACE: Document.Page.Token.DetectedBreak.Type
                HYPHEN: Document.Page.Token.DetectedBreak.Type
                TYPE_FIELD_NUMBER: _ClassVar[int]
                type: Document.Page.Token.DetectedBreak.Type

                def __init__(self, type: _Optional[_Union[Document.Page.Token.DetectedBreak.Type, str]]=...) -> None:
                    ...

            class StyleInfo(_message.Message):
                __slots__ = ('font_size', 'pixel_font_size', 'letter_spacing', 'font_type', 'bold', 'italic', 'underlined', 'strikeout', 'subscript', 'superscript', 'smallcaps', 'font_weight', 'handwritten', 'text_color', 'background_color')
                FONT_SIZE_FIELD_NUMBER: _ClassVar[int]
                PIXEL_FONT_SIZE_FIELD_NUMBER: _ClassVar[int]
                LETTER_SPACING_FIELD_NUMBER: _ClassVar[int]
                FONT_TYPE_FIELD_NUMBER: _ClassVar[int]
                BOLD_FIELD_NUMBER: _ClassVar[int]
                ITALIC_FIELD_NUMBER: _ClassVar[int]
                UNDERLINED_FIELD_NUMBER: _ClassVar[int]
                STRIKEOUT_FIELD_NUMBER: _ClassVar[int]
                SUBSCRIPT_FIELD_NUMBER: _ClassVar[int]
                SUPERSCRIPT_FIELD_NUMBER: _ClassVar[int]
                SMALLCAPS_FIELD_NUMBER: _ClassVar[int]
                FONT_WEIGHT_FIELD_NUMBER: _ClassVar[int]
                HANDWRITTEN_FIELD_NUMBER: _ClassVar[int]
                TEXT_COLOR_FIELD_NUMBER: _ClassVar[int]
                BACKGROUND_COLOR_FIELD_NUMBER: _ClassVar[int]
                font_size: int
                pixel_font_size: float
                letter_spacing: float
                font_type: str
                bold: bool
                italic: bool
                underlined: bool
                strikeout: bool
                subscript: bool
                superscript: bool
                smallcaps: bool
                font_weight: int
                handwritten: bool
                text_color: _color_pb2.Color
                background_color: _color_pb2.Color

                def __init__(self, font_size: _Optional[int]=..., pixel_font_size: _Optional[float]=..., letter_spacing: _Optional[float]=..., font_type: _Optional[str]=..., bold: bool=..., italic: bool=..., underlined: bool=..., strikeout: bool=..., subscript: bool=..., superscript: bool=..., smallcaps: bool=..., font_weight: _Optional[int]=..., handwritten: bool=..., text_color: _Optional[_Union[_color_pb2.Color, _Mapping]]=..., background_color: _Optional[_Union[_color_pb2.Color, _Mapping]]=...) -> None:
                    ...
            LAYOUT_FIELD_NUMBER: _ClassVar[int]
            DETECTED_BREAK_FIELD_NUMBER: _ClassVar[int]
            DETECTED_LANGUAGES_FIELD_NUMBER: _ClassVar[int]
            PROVENANCE_FIELD_NUMBER: _ClassVar[int]
            STYLE_INFO_FIELD_NUMBER: _ClassVar[int]
            layout: Document.Page.Layout
            detected_break: Document.Page.Token.DetectedBreak
            detected_languages: _containers.RepeatedCompositeFieldContainer[Document.Page.DetectedLanguage]
            provenance: Document.Provenance
            style_info: Document.Page.Token.StyleInfo

            def __init__(self, layout: _Optional[_Union[Document.Page.Layout, _Mapping]]=..., detected_break: _Optional[_Union[Document.Page.Token.DetectedBreak, _Mapping]]=..., detected_languages: _Optional[_Iterable[_Union[Document.Page.DetectedLanguage, _Mapping]]]=..., provenance: _Optional[_Union[Document.Provenance, _Mapping]]=..., style_info: _Optional[_Union[Document.Page.Token.StyleInfo, _Mapping]]=...) -> None:
                ...

        class Symbol(_message.Message):
            __slots__ = ('layout', 'detected_languages')
            LAYOUT_FIELD_NUMBER: _ClassVar[int]
            DETECTED_LANGUAGES_FIELD_NUMBER: _ClassVar[int]
            layout: Document.Page.Layout
            detected_languages: _containers.RepeatedCompositeFieldContainer[Document.Page.DetectedLanguage]

            def __init__(self, layout: _Optional[_Union[Document.Page.Layout, _Mapping]]=..., detected_languages: _Optional[_Iterable[_Union[Document.Page.DetectedLanguage, _Mapping]]]=...) -> None:
                ...

        class VisualElement(_message.Message):
            __slots__ = ('layout', 'type', 'detected_languages')
            LAYOUT_FIELD_NUMBER: _ClassVar[int]
            TYPE_FIELD_NUMBER: _ClassVar[int]
            DETECTED_LANGUAGES_FIELD_NUMBER: _ClassVar[int]
            layout: Document.Page.Layout
            type: str
            detected_languages: _containers.RepeatedCompositeFieldContainer[Document.Page.DetectedLanguage]

            def __init__(self, layout: _Optional[_Union[Document.Page.Layout, _Mapping]]=..., type: _Optional[str]=..., detected_languages: _Optional[_Iterable[_Union[Document.Page.DetectedLanguage, _Mapping]]]=...) -> None:
                ...

        class Table(_message.Message):
            __slots__ = ('layout', 'header_rows', 'body_rows', 'detected_languages', 'provenance')

            class TableRow(_message.Message):
                __slots__ = ('cells',)
                CELLS_FIELD_NUMBER: _ClassVar[int]
                cells: _containers.RepeatedCompositeFieldContainer[Document.Page.Table.TableCell]

                def __init__(self, cells: _Optional[_Iterable[_Union[Document.Page.Table.TableCell, _Mapping]]]=...) -> None:
                    ...

            class TableCell(_message.Message):
                __slots__ = ('layout', 'row_span', 'col_span', 'detected_languages')
                LAYOUT_FIELD_NUMBER: _ClassVar[int]
                ROW_SPAN_FIELD_NUMBER: _ClassVar[int]
                COL_SPAN_FIELD_NUMBER: _ClassVar[int]
                DETECTED_LANGUAGES_FIELD_NUMBER: _ClassVar[int]
                layout: Document.Page.Layout
                row_span: int
                col_span: int
                detected_languages: _containers.RepeatedCompositeFieldContainer[Document.Page.DetectedLanguage]

                def __init__(self, layout: _Optional[_Union[Document.Page.Layout, _Mapping]]=..., row_span: _Optional[int]=..., col_span: _Optional[int]=..., detected_languages: _Optional[_Iterable[_Union[Document.Page.DetectedLanguage, _Mapping]]]=...) -> None:
                    ...
            LAYOUT_FIELD_NUMBER: _ClassVar[int]
            HEADER_ROWS_FIELD_NUMBER: _ClassVar[int]
            BODY_ROWS_FIELD_NUMBER: _ClassVar[int]
            DETECTED_LANGUAGES_FIELD_NUMBER: _ClassVar[int]
            PROVENANCE_FIELD_NUMBER: _ClassVar[int]
            layout: Document.Page.Layout
            header_rows: _containers.RepeatedCompositeFieldContainer[Document.Page.Table.TableRow]
            body_rows: _containers.RepeatedCompositeFieldContainer[Document.Page.Table.TableRow]
            detected_languages: _containers.RepeatedCompositeFieldContainer[Document.Page.DetectedLanguage]
            provenance: Document.Provenance

            def __init__(self, layout: _Optional[_Union[Document.Page.Layout, _Mapping]]=..., header_rows: _Optional[_Iterable[_Union[Document.Page.Table.TableRow, _Mapping]]]=..., body_rows: _Optional[_Iterable[_Union[Document.Page.Table.TableRow, _Mapping]]]=..., detected_languages: _Optional[_Iterable[_Union[Document.Page.DetectedLanguage, _Mapping]]]=..., provenance: _Optional[_Union[Document.Provenance, _Mapping]]=...) -> None:
                ...

        class FormField(_message.Message):
            __slots__ = ('field_name', 'field_value', 'name_detected_languages', 'value_detected_languages', 'value_type', 'corrected_key_text', 'corrected_value_text', 'provenance')
            FIELD_NAME_FIELD_NUMBER: _ClassVar[int]
            FIELD_VALUE_FIELD_NUMBER: _ClassVar[int]
            NAME_DETECTED_LANGUAGES_FIELD_NUMBER: _ClassVar[int]
            VALUE_DETECTED_LANGUAGES_FIELD_NUMBER: _ClassVar[int]
            VALUE_TYPE_FIELD_NUMBER: _ClassVar[int]
            CORRECTED_KEY_TEXT_FIELD_NUMBER: _ClassVar[int]
            CORRECTED_VALUE_TEXT_FIELD_NUMBER: _ClassVar[int]
            PROVENANCE_FIELD_NUMBER: _ClassVar[int]
            field_name: Document.Page.Layout
            field_value: Document.Page.Layout
            name_detected_languages: _containers.RepeatedCompositeFieldContainer[Document.Page.DetectedLanguage]
            value_detected_languages: _containers.RepeatedCompositeFieldContainer[Document.Page.DetectedLanguage]
            value_type: str
            corrected_key_text: str
            corrected_value_text: str
            provenance: Document.Provenance

            def __init__(self, field_name: _Optional[_Union[Document.Page.Layout, _Mapping]]=..., field_value: _Optional[_Union[Document.Page.Layout, _Mapping]]=..., name_detected_languages: _Optional[_Iterable[_Union[Document.Page.DetectedLanguage, _Mapping]]]=..., value_detected_languages: _Optional[_Iterable[_Union[Document.Page.DetectedLanguage, _Mapping]]]=..., value_type: _Optional[str]=..., corrected_key_text: _Optional[str]=..., corrected_value_text: _Optional[str]=..., provenance: _Optional[_Union[Document.Provenance, _Mapping]]=...) -> None:
                ...

        class DetectedBarcode(_message.Message):
            __slots__ = ('layout', 'barcode')
            LAYOUT_FIELD_NUMBER: _ClassVar[int]
            BARCODE_FIELD_NUMBER: _ClassVar[int]
            layout: Document.Page.Layout
            barcode: _barcode_pb2.Barcode

            def __init__(self, layout: _Optional[_Union[Document.Page.Layout, _Mapping]]=..., barcode: _Optional[_Union[_barcode_pb2.Barcode, _Mapping]]=...) -> None:
                ...

        class DetectedLanguage(_message.Message):
            __slots__ = ('language_code', 'confidence')
            LANGUAGE_CODE_FIELD_NUMBER: _ClassVar[int]
            CONFIDENCE_FIELD_NUMBER: _ClassVar[int]
            language_code: str
            confidence: float

            def __init__(self, language_code: _Optional[str]=..., confidence: _Optional[float]=...) -> None:
                ...

        class ImageQualityScores(_message.Message):
            __slots__ = ('quality_score', 'detected_defects')

            class DetectedDefect(_message.Message):
                __slots__ = ('type', 'confidence')
                TYPE_FIELD_NUMBER: _ClassVar[int]
                CONFIDENCE_FIELD_NUMBER: _ClassVar[int]
                type: str
                confidence: float

                def __init__(self, type: _Optional[str]=..., confidence: _Optional[float]=...) -> None:
                    ...
            QUALITY_SCORE_FIELD_NUMBER: _ClassVar[int]
            DETECTED_DEFECTS_FIELD_NUMBER: _ClassVar[int]
            quality_score: float
            detected_defects: _containers.RepeatedCompositeFieldContainer[Document.Page.ImageQualityScores.DetectedDefect]

            def __init__(self, quality_score: _Optional[float]=..., detected_defects: _Optional[_Iterable[_Union[Document.Page.ImageQualityScores.DetectedDefect, _Mapping]]]=...) -> None:
                ...
        PAGE_NUMBER_FIELD_NUMBER: _ClassVar[int]
        IMAGE_FIELD_NUMBER: _ClassVar[int]
        TRANSFORMS_FIELD_NUMBER: _ClassVar[int]
        DIMENSION_FIELD_NUMBER: _ClassVar[int]
        LAYOUT_FIELD_NUMBER: _ClassVar[int]
        DETECTED_LANGUAGES_FIELD_NUMBER: _ClassVar[int]
        BLOCKS_FIELD_NUMBER: _ClassVar[int]
        PARAGRAPHS_FIELD_NUMBER: _ClassVar[int]
        LINES_FIELD_NUMBER: _ClassVar[int]
        TOKENS_FIELD_NUMBER: _ClassVar[int]
        VISUAL_ELEMENTS_FIELD_NUMBER: _ClassVar[int]
        TABLES_FIELD_NUMBER: _ClassVar[int]
        FORM_FIELDS_FIELD_NUMBER: _ClassVar[int]
        SYMBOLS_FIELD_NUMBER: _ClassVar[int]
        DETECTED_BARCODES_FIELD_NUMBER: _ClassVar[int]
        IMAGE_QUALITY_SCORES_FIELD_NUMBER: _ClassVar[int]
        PROVENANCE_FIELD_NUMBER: _ClassVar[int]
        page_number: int
        image: Document.Page.Image
        transforms: _containers.RepeatedCompositeFieldContainer[Document.Page.Matrix]
        dimension: Document.Page.Dimension
        layout: Document.Page.Layout
        detected_languages: _containers.RepeatedCompositeFieldContainer[Document.Page.DetectedLanguage]
        blocks: _containers.RepeatedCompositeFieldContainer[Document.Page.Block]
        paragraphs: _containers.RepeatedCompositeFieldContainer[Document.Page.Paragraph]
        lines: _containers.RepeatedCompositeFieldContainer[Document.Page.Line]
        tokens: _containers.RepeatedCompositeFieldContainer[Document.Page.Token]
        visual_elements: _containers.RepeatedCompositeFieldContainer[Document.Page.VisualElement]
        tables: _containers.RepeatedCompositeFieldContainer[Document.Page.Table]
        form_fields: _containers.RepeatedCompositeFieldContainer[Document.Page.FormField]
        symbols: _containers.RepeatedCompositeFieldContainer[Document.Page.Symbol]
        detected_barcodes: _containers.RepeatedCompositeFieldContainer[Document.Page.DetectedBarcode]
        image_quality_scores: Document.Page.ImageQualityScores
        provenance: Document.Provenance

        def __init__(self, page_number: _Optional[int]=..., image: _Optional[_Union[Document.Page.Image, _Mapping]]=..., transforms: _Optional[_Iterable[_Union[Document.Page.Matrix, _Mapping]]]=..., dimension: _Optional[_Union[Document.Page.Dimension, _Mapping]]=..., layout: _Optional[_Union[Document.Page.Layout, _Mapping]]=..., detected_languages: _Optional[_Iterable[_Union[Document.Page.DetectedLanguage, _Mapping]]]=..., blocks: _Optional[_Iterable[_Union[Document.Page.Block, _Mapping]]]=..., paragraphs: _Optional[_Iterable[_Union[Document.Page.Paragraph, _Mapping]]]=..., lines: _Optional[_Iterable[_Union[Document.Page.Line, _Mapping]]]=..., tokens: _Optional[_Iterable[_Union[Document.Page.Token, _Mapping]]]=..., visual_elements: _Optional[_Iterable[_Union[Document.Page.VisualElement, _Mapping]]]=..., tables: _Optional[_Iterable[_Union[Document.Page.Table, _Mapping]]]=..., form_fields: _Optional[_Iterable[_Union[Document.Page.FormField, _Mapping]]]=..., symbols: _Optional[_Iterable[_Union[Document.Page.Symbol, _Mapping]]]=..., detected_barcodes: _Optional[_Iterable[_Union[Document.Page.DetectedBarcode, _Mapping]]]=..., image_quality_scores: _Optional[_Union[Document.Page.ImageQualityScores, _Mapping]]=..., provenance: _Optional[_Union[Document.Provenance, _Mapping]]=...) -> None:
            ...

    class Entity(_message.Message):
        __slots__ = ('text_anchor', 'type', 'mention_text', 'mention_id', 'confidence', 'page_anchor', 'id', 'normalized_value', 'properties', 'provenance', 'redacted')

        class NormalizedValue(_message.Message):
            __slots__ = ('money_value', 'date_value', 'datetime_value', 'address_value', 'boolean_value', 'integer_value', 'float_value', 'text')
            MONEY_VALUE_FIELD_NUMBER: _ClassVar[int]
            DATE_VALUE_FIELD_NUMBER: _ClassVar[int]
            DATETIME_VALUE_FIELD_NUMBER: _ClassVar[int]
            ADDRESS_VALUE_FIELD_NUMBER: _ClassVar[int]
            BOOLEAN_VALUE_FIELD_NUMBER: _ClassVar[int]
            INTEGER_VALUE_FIELD_NUMBER: _ClassVar[int]
            FLOAT_VALUE_FIELD_NUMBER: _ClassVar[int]
            TEXT_FIELD_NUMBER: _ClassVar[int]
            money_value: _money_pb2.Money
            date_value: _date_pb2.Date
            datetime_value: _datetime_pb2.DateTime
            address_value: _postal_address_pb2.PostalAddress
            boolean_value: bool
            integer_value: int
            float_value: float
            text: str

            def __init__(self, money_value: _Optional[_Union[_money_pb2.Money, _Mapping]]=..., date_value: _Optional[_Union[_date_pb2.Date, _Mapping]]=..., datetime_value: _Optional[_Union[_datetime_pb2.DateTime, _Mapping]]=..., address_value: _Optional[_Union[_postal_address_pb2.PostalAddress, _Mapping]]=..., boolean_value: bool=..., integer_value: _Optional[int]=..., float_value: _Optional[float]=..., text: _Optional[str]=...) -> None:
                ...
        TEXT_ANCHOR_FIELD_NUMBER: _ClassVar[int]
        TYPE_FIELD_NUMBER: _ClassVar[int]
        MENTION_TEXT_FIELD_NUMBER: _ClassVar[int]
        MENTION_ID_FIELD_NUMBER: _ClassVar[int]
        CONFIDENCE_FIELD_NUMBER: _ClassVar[int]
        PAGE_ANCHOR_FIELD_NUMBER: _ClassVar[int]
        ID_FIELD_NUMBER: _ClassVar[int]
        NORMALIZED_VALUE_FIELD_NUMBER: _ClassVar[int]
        PROPERTIES_FIELD_NUMBER: _ClassVar[int]
        PROVENANCE_FIELD_NUMBER: _ClassVar[int]
        REDACTED_FIELD_NUMBER: _ClassVar[int]
        text_anchor: Document.TextAnchor
        type: str
        mention_text: str
        mention_id: str
        confidence: float
        page_anchor: Document.PageAnchor
        id: str
        normalized_value: Document.Entity.NormalizedValue
        properties: _containers.RepeatedCompositeFieldContainer[Document.Entity]
        provenance: Document.Provenance
        redacted: bool

        def __init__(self, text_anchor: _Optional[_Union[Document.TextAnchor, _Mapping]]=..., type: _Optional[str]=..., mention_text: _Optional[str]=..., mention_id: _Optional[str]=..., confidence: _Optional[float]=..., page_anchor: _Optional[_Union[Document.PageAnchor, _Mapping]]=..., id: _Optional[str]=..., normalized_value: _Optional[_Union[Document.Entity.NormalizedValue, _Mapping]]=..., properties: _Optional[_Iterable[_Union[Document.Entity, _Mapping]]]=..., provenance: _Optional[_Union[Document.Provenance, _Mapping]]=..., redacted: bool=...) -> None:
            ...

    class EntityRelation(_message.Message):
        __slots__ = ('subject_id', 'object_id', 'relation')
        SUBJECT_ID_FIELD_NUMBER: _ClassVar[int]
        OBJECT_ID_FIELD_NUMBER: _ClassVar[int]
        RELATION_FIELD_NUMBER: _ClassVar[int]
        subject_id: str
        object_id: str
        relation: str

        def __init__(self, subject_id: _Optional[str]=..., object_id: _Optional[str]=..., relation: _Optional[str]=...) -> None:
            ...

    class TextAnchor(_message.Message):
        __slots__ = ('text_segments', 'content')

        class TextSegment(_message.Message):
            __slots__ = ('start_index', 'end_index')
            START_INDEX_FIELD_NUMBER: _ClassVar[int]
            END_INDEX_FIELD_NUMBER: _ClassVar[int]
            start_index: int
            end_index: int

            def __init__(self, start_index: _Optional[int]=..., end_index: _Optional[int]=...) -> None:
                ...
        TEXT_SEGMENTS_FIELD_NUMBER: _ClassVar[int]
        CONTENT_FIELD_NUMBER: _ClassVar[int]
        text_segments: _containers.RepeatedCompositeFieldContainer[Document.TextAnchor.TextSegment]
        content: str

        def __init__(self, text_segments: _Optional[_Iterable[_Union[Document.TextAnchor.TextSegment, _Mapping]]]=..., content: _Optional[str]=...) -> None:
            ...

    class PageAnchor(_message.Message):
        __slots__ = ('page_refs',)

        class PageRef(_message.Message):
            __slots__ = ('page', 'layout_type', 'layout_id', 'bounding_poly', 'confidence')

            class LayoutType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
                __slots__ = ()
                LAYOUT_TYPE_UNSPECIFIED: _ClassVar[Document.PageAnchor.PageRef.LayoutType]
                BLOCK: _ClassVar[Document.PageAnchor.PageRef.LayoutType]
                PARAGRAPH: _ClassVar[Document.PageAnchor.PageRef.LayoutType]
                LINE: _ClassVar[Document.PageAnchor.PageRef.LayoutType]
                TOKEN: _ClassVar[Document.PageAnchor.PageRef.LayoutType]
                VISUAL_ELEMENT: _ClassVar[Document.PageAnchor.PageRef.LayoutType]
                TABLE: _ClassVar[Document.PageAnchor.PageRef.LayoutType]
                FORM_FIELD: _ClassVar[Document.PageAnchor.PageRef.LayoutType]
            LAYOUT_TYPE_UNSPECIFIED: Document.PageAnchor.PageRef.LayoutType
            BLOCK: Document.PageAnchor.PageRef.LayoutType
            PARAGRAPH: Document.PageAnchor.PageRef.LayoutType
            LINE: Document.PageAnchor.PageRef.LayoutType
            TOKEN: Document.PageAnchor.PageRef.LayoutType
            VISUAL_ELEMENT: Document.PageAnchor.PageRef.LayoutType
            TABLE: Document.PageAnchor.PageRef.LayoutType
            FORM_FIELD: Document.PageAnchor.PageRef.LayoutType
            PAGE_FIELD_NUMBER: _ClassVar[int]
            LAYOUT_TYPE_FIELD_NUMBER: _ClassVar[int]
            LAYOUT_ID_FIELD_NUMBER: _ClassVar[int]
            BOUNDING_POLY_FIELD_NUMBER: _ClassVar[int]
            CONFIDENCE_FIELD_NUMBER: _ClassVar[int]
            page: int
            layout_type: Document.PageAnchor.PageRef.LayoutType
            layout_id: str
            bounding_poly: _geometry_pb2.BoundingPoly
            confidence: float

            def __init__(self, page: _Optional[int]=..., layout_type: _Optional[_Union[Document.PageAnchor.PageRef.LayoutType, str]]=..., layout_id: _Optional[str]=..., bounding_poly: _Optional[_Union[_geometry_pb2.BoundingPoly, _Mapping]]=..., confidence: _Optional[float]=...) -> None:
                ...
        PAGE_REFS_FIELD_NUMBER: _ClassVar[int]
        page_refs: _containers.RepeatedCompositeFieldContainer[Document.PageAnchor.PageRef]

        def __init__(self, page_refs: _Optional[_Iterable[_Union[Document.PageAnchor.PageRef, _Mapping]]]=...) -> None:
            ...

    class Provenance(_message.Message):
        __slots__ = ('revision', 'id', 'parents', 'type')

        class OperationType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
            __slots__ = ()
            OPERATION_TYPE_UNSPECIFIED: _ClassVar[Document.Provenance.OperationType]
            ADD: _ClassVar[Document.Provenance.OperationType]
            REMOVE: _ClassVar[Document.Provenance.OperationType]
            UPDATE: _ClassVar[Document.Provenance.OperationType]
            REPLACE: _ClassVar[Document.Provenance.OperationType]
            EVAL_REQUESTED: _ClassVar[Document.Provenance.OperationType]
            EVAL_APPROVED: _ClassVar[Document.Provenance.OperationType]
            EVAL_SKIPPED: _ClassVar[Document.Provenance.OperationType]
        OPERATION_TYPE_UNSPECIFIED: Document.Provenance.OperationType
        ADD: Document.Provenance.OperationType
        REMOVE: Document.Provenance.OperationType
        UPDATE: Document.Provenance.OperationType
        REPLACE: Document.Provenance.OperationType
        EVAL_REQUESTED: Document.Provenance.OperationType
        EVAL_APPROVED: Document.Provenance.OperationType
        EVAL_SKIPPED: Document.Provenance.OperationType

        class Parent(_message.Message):
            __slots__ = ('revision', 'index', 'id')
            REVISION_FIELD_NUMBER: _ClassVar[int]
            INDEX_FIELD_NUMBER: _ClassVar[int]
            ID_FIELD_NUMBER: _ClassVar[int]
            revision: int
            index: int
            id: int

            def __init__(self, revision: _Optional[int]=..., index: _Optional[int]=..., id: _Optional[int]=...) -> None:
                ...
        REVISION_FIELD_NUMBER: _ClassVar[int]
        ID_FIELD_NUMBER: _ClassVar[int]
        PARENTS_FIELD_NUMBER: _ClassVar[int]
        TYPE_FIELD_NUMBER: _ClassVar[int]
        revision: int
        id: int
        parents: _containers.RepeatedCompositeFieldContainer[Document.Provenance.Parent]
        type: Document.Provenance.OperationType

        def __init__(self, revision: _Optional[int]=..., id: _Optional[int]=..., parents: _Optional[_Iterable[_Union[Document.Provenance.Parent, _Mapping]]]=..., type: _Optional[_Union[Document.Provenance.OperationType, str]]=...) -> None:
            ...

    class Revision(_message.Message):
        __slots__ = ('agent', 'processor', 'id', 'parent', 'parent_ids', 'create_time', 'human_review')

        class HumanReview(_message.Message):
            __slots__ = ('state', 'state_message')
            STATE_FIELD_NUMBER: _ClassVar[int]
            STATE_MESSAGE_FIELD_NUMBER: _ClassVar[int]
            state: str
            state_message: str

            def __init__(self, state: _Optional[str]=..., state_message: _Optional[str]=...) -> None:
                ...
        AGENT_FIELD_NUMBER: _ClassVar[int]
        PROCESSOR_FIELD_NUMBER: _ClassVar[int]
        ID_FIELD_NUMBER: _ClassVar[int]
        PARENT_FIELD_NUMBER: _ClassVar[int]
        PARENT_IDS_FIELD_NUMBER: _ClassVar[int]
        CREATE_TIME_FIELD_NUMBER: _ClassVar[int]
        HUMAN_REVIEW_FIELD_NUMBER: _ClassVar[int]
        agent: str
        processor: str
        id: str
        parent: _containers.RepeatedScalarFieldContainer[int]
        parent_ids: _containers.RepeatedScalarFieldContainer[str]
        create_time: _timestamp_pb2.Timestamp
        human_review: Document.Revision.HumanReview

        def __init__(self, agent: _Optional[str]=..., processor: _Optional[str]=..., id: _Optional[str]=..., parent: _Optional[_Iterable[int]]=..., parent_ids: _Optional[_Iterable[str]]=..., create_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]]=..., human_review: _Optional[_Union[Document.Revision.HumanReview, _Mapping]]=...) -> None:
            ...

    class TextChange(_message.Message):
        __slots__ = ('text_anchor', 'changed_text', 'provenance')
        TEXT_ANCHOR_FIELD_NUMBER: _ClassVar[int]
        CHANGED_TEXT_FIELD_NUMBER: _ClassVar[int]
        PROVENANCE_FIELD_NUMBER: _ClassVar[int]
        text_anchor: Document.TextAnchor
        changed_text: str
        provenance: _containers.RepeatedCompositeFieldContainer[Document.Provenance]

        def __init__(self, text_anchor: _Optional[_Union[Document.TextAnchor, _Mapping]]=..., changed_text: _Optional[str]=..., provenance: _Optional[_Iterable[_Union[Document.Provenance, _Mapping]]]=...) -> None:
            ...

    class DocumentLayout(_message.Message):
        __slots__ = ('blocks',)

        class DocumentLayoutBlock(_message.Message):
            __slots__ = ('text_block', 'table_block', 'list_block', 'block_id', 'page_span')

            class LayoutPageSpan(_message.Message):
                __slots__ = ('page_start', 'page_end')
                PAGE_START_FIELD_NUMBER: _ClassVar[int]
                PAGE_END_FIELD_NUMBER: _ClassVar[int]
                page_start: int
                page_end: int

                def __init__(self, page_start: _Optional[int]=..., page_end: _Optional[int]=...) -> None:
                    ...

            class LayoutTextBlock(_message.Message):
                __slots__ = ('text', 'type', 'blocks')
                TEXT_FIELD_NUMBER: _ClassVar[int]
                TYPE_FIELD_NUMBER: _ClassVar[int]
                BLOCKS_FIELD_NUMBER: _ClassVar[int]
                text: str
                type: str
                blocks: _containers.RepeatedCompositeFieldContainer[Document.DocumentLayout.DocumentLayoutBlock]

                def __init__(self, text: _Optional[str]=..., type: _Optional[str]=..., blocks: _Optional[_Iterable[_Union[Document.DocumentLayout.DocumentLayoutBlock, _Mapping]]]=...) -> None:
                    ...

            class LayoutTableBlock(_message.Message):
                __slots__ = ('header_rows', 'body_rows', 'caption')
                HEADER_ROWS_FIELD_NUMBER: _ClassVar[int]
                BODY_ROWS_FIELD_NUMBER: _ClassVar[int]
                CAPTION_FIELD_NUMBER: _ClassVar[int]
                header_rows: _containers.RepeatedCompositeFieldContainer[Document.DocumentLayout.DocumentLayoutBlock.LayoutTableRow]
                body_rows: _containers.RepeatedCompositeFieldContainer[Document.DocumentLayout.DocumentLayoutBlock.LayoutTableRow]
                caption: str

                def __init__(self, header_rows: _Optional[_Iterable[_Union[Document.DocumentLayout.DocumentLayoutBlock.LayoutTableRow, _Mapping]]]=..., body_rows: _Optional[_Iterable[_Union[Document.DocumentLayout.DocumentLayoutBlock.LayoutTableRow, _Mapping]]]=..., caption: _Optional[str]=...) -> None:
                    ...

            class LayoutTableRow(_message.Message):
                __slots__ = ('cells',)
                CELLS_FIELD_NUMBER: _ClassVar[int]
                cells: _containers.RepeatedCompositeFieldContainer[Document.DocumentLayout.DocumentLayoutBlock.LayoutTableCell]

                def __init__(self, cells: _Optional[_Iterable[_Union[Document.DocumentLayout.DocumentLayoutBlock.LayoutTableCell, _Mapping]]]=...) -> None:
                    ...

            class LayoutTableCell(_message.Message):
                __slots__ = ('blocks', 'row_span', 'col_span')
                BLOCKS_FIELD_NUMBER: _ClassVar[int]
                ROW_SPAN_FIELD_NUMBER: _ClassVar[int]
                COL_SPAN_FIELD_NUMBER: _ClassVar[int]
                blocks: _containers.RepeatedCompositeFieldContainer[Document.DocumentLayout.DocumentLayoutBlock]
                row_span: int
                col_span: int

                def __init__(self, blocks: _Optional[_Iterable[_Union[Document.DocumentLayout.DocumentLayoutBlock, _Mapping]]]=..., row_span: _Optional[int]=..., col_span: _Optional[int]=...) -> None:
                    ...

            class LayoutListBlock(_message.Message):
                __slots__ = ('list_entries', 'type')
                LIST_ENTRIES_FIELD_NUMBER: _ClassVar[int]
                TYPE_FIELD_NUMBER: _ClassVar[int]
                list_entries: _containers.RepeatedCompositeFieldContainer[Document.DocumentLayout.DocumentLayoutBlock.LayoutListEntry]
                type: str

                def __init__(self, list_entries: _Optional[_Iterable[_Union[Document.DocumentLayout.DocumentLayoutBlock.LayoutListEntry, _Mapping]]]=..., type: _Optional[str]=...) -> None:
                    ...

            class LayoutListEntry(_message.Message):
                __slots__ = ('blocks',)
                BLOCKS_FIELD_NUMBER: _ClassVar[int]
                blocks: _containers.RepeatedCompositeFieldContainer[Document.DocumentLayout.DocumentLayoutBlock]

                def __init__(self, blocks: _Optional[_Iterable[_Union[Document.DocumentLayout.DocumentLayoutBlock, _Mapping]]]=...) -> None:
                    ...
            TEXT_BLOCK_FIELD_NUMBER: _ClassVar[int]
            TABLE_BLOCK_FIELD_NUMBER: _ClassVar[int]
            LIST_BLOCK_FIELD_NUMBER: _ClassVar[int]
            BLOCK_ID_FIELD_NUMBER: _ClassVar[int]
            PAGE_SPAN_FIELD_NUMBER: _ClassVar[int]
            text_block: Document.DocumentLayout.DocumentLayoutBlock.LayoutTextBlock
            table_block: Document.DocumentLayout.DocumentLayoutBlock.LayoutTableBlock
            list_block: Document.DocumentLayout.DocumentLayoutBlock.LayoutListBlock
            block_id: str
            page_span: Document.DocumentLayout.DocumentLayoutBlock.LayoutPageSpan

            def __init__(self, text_block: _Optional[_Union[Document.DocumentLayout.DocumentLayoutBlock.LayoutTextBlock, _Mapping]]=..., table_block: _Optional[_Union[Document.DocumentLayout.DocumentLayoutBlock.LayoutTableBlock, _Mapping]]=..., list_block: _Optional[_Union[Document.DocumentLayout.DocumentLayoutBlock.LayoutListBlock, _Mapping]]=..., block_id: _Optional[str]=..., page_span: _Optional[_Union[Document.DocumentLayout.DocumentLayoutBlock.LayoutPageSpan, _Mapping]]=...) -> None:
                ...
        BLOCKS_FIELD_NUMBER: _ClassVar[int]
        blocks: _containers.RepeatedCompositeFieldContainer[Document.DocumentLayout.DocumentLayoutBlock]

        def __init__(self, blocks: _Optional[_Iterable[_Union[Document.DocumentLayout.DocumentLayoutBlock, _Mapping]]]=...) -> None:
            ...

    class ChunkedDocument(_message.Message):
        __slots__ = ('chunks',)

        class Chunk(_message.Message):
            __slots__ = ('chunk_id', 'source_block_ids', 'content', 'page_span', 'page_headers', 'page_footers')

            class ChunkPageSpan(_message.Message):
                __slots__ = ('page_start', 'page_end')
                PAGE_START_FIELD_NUMBER: _ClassVar[int]
                PAGE_END_FIELD_NUMBER: _ClassVar[int]
                page_start: int
                page_end: int

                def __init__(self, page_start: _Optional[int]=..., page_end: _Optional[int]=...) -> None:
                    ...

            class ChunkPageHeader(_message.Message):
                __slots__ = ('text', 'page_span')
                TEXT_FIELD_NUMBER: _ClassVar[int]
                PAGE_SPAN_FIELD_NUMBER: _ClassVar[int]
                text: str
                page_span: Document.ChunkedDocument.Chunk.ChunkPageSpan

                def __init__(self, text: _Optional[str]=..., page_span: _Optional[_Union[Document.ChunkedDocument.Chunk.ChunkPageSpan, _Mapping]]=...) -> None:
                    ...

            class ChunkPageFooter(_message.Message):
                __slots__ = ('text', 'page_span')
                TEXT_FIELD_NUMBER: _ClassVar[int]
                PAGE_SPAN_FIELD_NUMBER: _ClassVar[int]
                text: str
                page_span: Document.ChunkedDocument.Chunk.ChunkPageSpan

                def __init__(self, text: _Optional[str]=..., page_span: _Optional[_Union[Document.ChunkedDocument.Chunk.ChunkPageSpan, _Mapping]]=...) -> None:
                    ...
            CHUNK_ID_FIELD_NUMBER: _ClassVar[int]
            SOURCE_BLOCK_IDS_FIELD_NUMBER: _ClassVar[int]
            CONTENT_FIELD_NUMBER: _ClassVar[int]
            PAGE_SPAN_FIELD_NUMBER: _ClassVar[int]
            PAGE_HEADERS_FIELD_NUMBER: _ClassVar[int]
            PAGE_FOOTERS_FIELD_NUMBER: _ClassVar[int]
            chunk_id: str
            source_block_ids: _containers.RepeatedScalarFieldContainer[str]
            content: str
            page_span: Document.ChunkedDocument.Chunk.ChunkPageSpan
            page_headers: _containers.RepeatedCompositeFieldContainer[Document.ChunkedDocument.Chunk.ChunkPageHeader]
            page_footers: _containers.RepeatedCompositeFieldContainer[Document.ChunkedDocument.Chunk.ChunkPageFooter]

            def __init__(self, chunk_id: _Optional[str]=..., source_block_ids: _Optional[_Iterable[str]]=..., content: _Optional[str]=..., page_span: _Optional[_Union[Document.ChunkedDocument.Chunk.ChunkPageSpan, _Mapping]]=..., page_headers: _Optional[_Iterable[_Union[Document.ChunkedDocument.Chunk.ChunkPageHeader, _Mapping]]]=..., page_footers: _Optional[_Iterable[_Union[Document.ChunkedDocument.Chunk.ChunkPageFooter, _Mapping]]]=...) -> None:
                ...
        CHUNKS_FIELD_NUMBER: _ClassVar[int]
        chunks: _containers.RepeatedCompositeFieldContainer[Document.ChunkedDocument.Chunk]

        def __init__(self, chunks: _Optional[_Iterable[_Union[Document.ChunkedDocument.Chunk, _Mapping]]]=...) -> None:
            ...
    URI_FIELD_NUMBER: _ClassVar[int]
    CONTENT_FIELD_NUMBER: _ClassVar[int]
    MIME_TYPE_FIELD_NUMBER: _ClassVar[int]
    TEXT_FIELD_NUMBER: _ClassVar[int]
    TEXT_STYLES_FIELD_NUMBER: _ClassVar[int]
    PAGES_FIELD_NUMBER: _ClassVar[int]
    ENTITIES_FIELD_NUMBER: _ClassVar[int]
    ENTITY_RELATIONS_FIELD_NUMBER: _ClassVar[int]
    TEXT_CHANGES_FIELD_NUMBER: _ClassVar[int]
    SHARD_INFO_FIELD_NUMBER: _ClassVar[int]
    ERROR_FIELD_NUMBER: _ClassVar[int]
    REVISIONS_FIELD_NUMBER: _ClassVar[int]
    DOCUMENT_LAYOUT_FIELD_NUMBER: _ClassVar[int]
    CHUNKED_DOCUMENT_FIELD_NUMBER: _ClassVar[int]
    uri: str
    content: bytes
    mime_type: str
    text: str
    text_styles: _containers.RepeatedCompositeFieldContainer[Document.Style]
    pages: _containers.RepeatedCompositeFieldContainer[Document.Page]
    entities: _containers.RepeatedCompositeFieldContainer[Document.Entity]
    entity_relations: _containers.RepeatedCompositeFieldContainer[Document.EntityRelation]
    text_changes: _containers.RepeatedCompositeFieldContainer[Document.TextChange]
    shard_info: Document.ShardInfo
    error: _status_pb2.Status
    revisions: _containers.RepeatedCompositeFieldContainer[Document.Revision]
    document_layout: Document.DocumentLayout
    chunked_document: Document.ChunkedDocument

    def __init__(self, uri: _Optional[str]=..., content: _Optional[bytes]=..., mime_type: _Optional[str]=..., text: _Optional[str]=..., text_styles: _Optional[_Iterable[_Union[Document.Style, _Mapping]]]=..., pages: _Optional[_Iterable[_Union[Document.Page, _Mapping]]]=..., entities: _Optional[_Iterable[_Union[Document.Entity, _Mapping]]]=..., entity_relations: _Optional[_Iterable[_Union[Document.EntityRelation, _Mapping]]]=..., text_changes: _Optional[_Iterable[_Union[Document.TextChange, _Mapping]]]=..., shard_info: _Optional[_Union[Document.ShardInfo, _Mapping]]=..., error: _Optional[_Union[_status_pb2.Status, _Mapping]]=..., revisions: _Optional[_Iterable[_Union[Document.Revision, _Mapping]]]=..., document_layout: _Optional[_Union[Document.DocumentLayout, _Mapping]]=..., chunked_document: _Optional[_Union[Document.ChunkedDocument, _Mapping]]=...) -> None:
        ...