from google.cloud.automl.v1beta1 import geometry_pb2 as _geometry_pb2
from google.cloud.automl.v1beta1 import io_pb2 as _io_pb2
from google.cloud.automl.v1beta1 import temporal_pb2 as _temporal_pb2
from google.cloud.automl.v1beta1 import text_segment_pb2 as _text_segment_pb2
from google.protobuf import struct_pb2 as _struct_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union
DESCRIPTOR: _descriptor.FileDescriptor

class Image(_message.Message):
    __slots__ = ('image_bytes', 'input_config', 'thumbnail_uri')
    IMAGE_BYTES_FIELD_NUMBER: _ClassVar[int]
    INPUT_CONFIG_FIELD_NUMBER: _ClassVar[int]
    THUMBNAIL_URI_FIELD_NUMBER: _ClassVar[int]
    image_bytes: bytes
    input_config: _io_pb2.InputConfig
    thumbnail_uri: str

    def __init__(self, image_bytes: _Optional[bytes]=..., input_config: _Optional[_Union[_io_pb2.InputConfig, _Mapping]]=..., thumbnail_uri: _Optional[str]=...) -> None:
        ...

class TextSnippet(_message.Message):
    __slots__ = ('content', 'mime_type', 'content_uri')
    CONTENT_FIELD_NUMBER: _ClassVar[int]
    MIME_TYPE_FIELD_NUMBER: _ClassVar[int]
    CONTENT_URI_FIELD_NUMBER: _ClassVar[int]
    content: str
    mime_type: str
    content_uri: str

    def __init__(self, content: _Optional[str]=..., mime_type: _Optional[str]=..., content_uri: _Optional[str]=...) -> None:
        ...

class DocumentDimensions(_message.Message):
    __slots__ = ('unit', 'width', 'height')

    class DocumentDimensionUnit(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        DOCUMENT_DIMENSION_UNIT_UNSPECIFIED: _ClassVar[DocumentDimensions.DocumentDimensionUnit]
        INCH: _ClassVar[DocumentDimensions.DocumentDimensionUnit]
        CENTIMETER: _ClassVar[DocumentDimensions.DocumentDimensionUnit]
        POINT: _ClassVar[DocumentDimensions.DocumentDimensionUnit]
    DOCUMENT_DIMENSION_UNIT_UNSPECIFIED: DocumentDimensions.DocumentDimensionUnit
    INCH: DocumentDimensions.DocumentDimensionUnit
    CENTIMETER: DocumentDimensions.DocumentDimensionUnit
    POINT: DocumentDimensions.DocumentDimensionUnit
    UNIT_FIELD_NUMBER: _ClassVar[int]
    WIDTH_FIELD_NUMBER: _ClassVar[int]
    HEIGHT_FIELD_NUMBER: _ClassVar[int]
    unit: DocumentDimensions.DocumentDimensionUnit
    width: float
    height: float

    def __init__(self, unit: _Optional[_Union[DocumentDimensions.DocumentDimensionUnit, str]]=..., width: _Optional[float]=..., height: _Optional[float]=...) -> None:
        ...

class Document(_message.Message):
    __slots__ = ('input_config', 'document_text', 'layout', 'document_dimensions', 'page_count')

    class Layout(_message.Message):
        __slots__ = ('text_segment', 'page_number', 'bounding_poly', 'text_segment_type')

        class TextSegmentType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
            __slots__ = ()
            TEXT_SEGMENT_TYPE_UNSPECIFIED: _ClassVar[Document.Layout.TextSegmentType]
            TOKEN: _ClassVar[Document.Layout.TextSegmentType]
            PARAGRAPH: _ClassVar[Document.Layout.TextSegmentType]
            FORM_FIELD: _ClassVar[Document.Layout.TextSegmentType]
            FORM_FIELD_NAME: _ClassVar[Document.Layout.TextSegmentType]
            FORM_FIELD_CONTENTS: _ClassVar[Document.Layout.TextSegmentType]
            TABLE: _ClassVar[Document.Layout.TextSegmentType]
            TABLE_HEADER: _ClassVar[Document.Layout.TextSegmentType]
            TABLE_ROW: _ClassVar[Document.Layout.TextSegmentType]
            TABLE_CELL: _ClassVar[Document.Layout.TextSegmentType]
        TEXT_SEGMENT_TYPE_UNSPECIFIED: Document.Layout.TextSegmentType
        TOKEN: Document.Layout.TextSegmentType
        PARAGRAPH: Document.Layout.TextSegmentType
        FORM_FIELD: Document.Layout.TextSegmentType
        FORM_FIELD_NAME: Document.Layout.TextSegmentType
        FORM_FIELD_CONTENTS: Document.Layout.TextSegmentType
        TABLE: Document.Layout.TextSegmentType
        TABLE_HEADER: Document.Layout.TextSegmentType
        TABLE_ROW: Document.Layout.TextSegmentType
        TABLE_CELL: Document.Layout.TextSegmentType
        TEXT_SEGMENT_FIELD_NUMBER: _ClassVar[int]
        PAGE_NUMBER_FIELD_NUMBER: _ClassVar[int]
        BOUNDING_POLY_FIELD_NUMBER: _ClassVar[int]
        TEXT_SEGMENT_TYPE_FIELD_NUMBER: _ClassVar[int]
        text_segment: _text_segment_pb2.TextSegment
        page_number: int
        bounding_poly: _geometry_pb2.BoundingPoly
        text_segment_type: Document.Layout.TextSegmentType

        def __init__(self, text_segment: _Optional[_Union[_text_segment_pb2.TextSegment, _Mapping]]=..., page_number: _Optional[int]=..., bounding_poly: _Optional[_Union[_geometry_pb2.BoundingPoly, _Mapping]]=..., text_segment_type: _Optional[_Union[Document.Layout.TextSegmentType, str]]=...) -> None:
            ...
    INPUT_CONFIG_FIELD_NUMBER: _ClassVar[int]
    DOCUMENT_TEXT_FIELD_NUMBER: _ClassVar[int]
    LAYOUT_FIELD_NUMBER: _ClassVar[int]
    DOCUMENT_DIMENSIONS_FIELD_NUMBER: _ClassVar[int]
    PAGE_COUNT_FIELD_NUMBER: _ClassVar[int]
    input_config: _io_pb2.DocumentInputConfig
    document_text: TextSnippet
    layout: _containers.RepeatedCompositeFieldContainer[Document.Layout]
    document_dimensions: DocumentDimensions
    page_count: int

    def __init__(self, input_config: _Optional[_Union[_io_pb2.DocumentInputConfig, _Mapping]]=..., document_text: _Optional[_Union[TextSnippet, _Mapping]]=..., layout: _Optional[_Iterable[_Union[Document.Layout, _Mapping]]]=..., document_dimensions: _Optional[_Union[DocumentDimensions, _Mapping]]=..., page_count: _Optional[int]=...) -> None:
        ...

class Row(_message.Message):
    __slots__ = ('column_spec_ids', 'values')
    COLUMN_SPEC_IDS_FIELD_NUMBER: _ClassVar[int]
    VALUES_FIELD_NUMBER: _ClassVar[int]
    column_spec_ids: _containers.RepeatedScalarFieldContainer[str]
    values: _containers.RepeatedCompositeFieldContainer[_struct_pb2.Value]

    def __init__(self, column_spec_ids: _Optional[_Iterable[str]]=..., values: _Optional[_Iterable[_Union[_struct_pb2.Value, _Mapping]]]=...) -> None:
        ...

class ExamplePayload(_message.Message):
    __slots__ = ('image', 'text_snippet', 'document', 'row')
    IMAGE_FIELD_NUMBER: _ClassVar[int]
    TEXT_SNIPPET_FIELD_NUMBER: _ClassVar[int]
    DOCUMENT_FIELD_NUMBER: _ClassVar[int]
    ROW_FIELD_NUMBER: _ClassVar[int]
    image: Image
    text_snippet: TextSnippet
    document: Document
    row: Row

    def __init__(self, image: _Optional[_Union[Image, _Mapping]]=..., text_snippet: _Optional[_Union[TextSnippet, _Mapping]]=..., document: _Optional[_Union[Document, _Mapping]]=..., row: _Optional[_Union[Row, _Mapping]]=...) -> None:
        ...