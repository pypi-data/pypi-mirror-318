from google.api import field_behavior_pb2 as _field_behavior_pb2
from google.api import resource_pb2 as _resource_pb2
from google.cloud.documentai.v1 import document_pb2 as _document_pb2
from google.protobuf import timestamp_pb2 as _timestamp_pb2
from google.type import datetime_pb2 as _datetime_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union
DESCRIPTOR: _descriptor.FileDescriptor

class RawDocumentFileType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    RAW_DOCUMENT_FILE_TYPE_UNSPECIFIED: _ClassVar[RawDocumentFileType]
    RAW_DOCUMENT_FILE_TYPE_PDF: _ClassVar[RawDocumentFileType]
    RAW_DOCUMENT_FILE_TYPE_DOCX: _ClassVar[RawDocumentFileType]
    RAW_DOCUMENT_FILE_TYPE_XLSX: _ClassVar[RawDocumentFileType]
    RAW_DOCUMENT_FILE_TYPE_PPTX: _ClassVar[RawDocumentFileType]
    RAW_DOCUMENT_FILE_TYPE_TEXT: _ClassVar[RawDocumentFileType]
    RAW_DOCUMENT_FILE_TYPE_TIFF: _ClassVar[RawDocumentFileType]

class ContentCategory(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    CONTENT_CATEGORY_UNSPECIFIED: _ClassVar[ContentCategory]
    CONTENT_CATEGORY_IMAGE: _ClassVar[ContentCategory]
    CONTENT_CATEGORY_AUDIO: _ClassVar[ContentCategory]
    CONTENT_CATEGORY_VIDEO: _ClassVar[ContentCategory]
RAW_DOCUMENT_FILE_TYPE_UNSPECIFIED: RawDocumentFileType
RAW_DOCUMENT_FILE_TYPE_PDF: RawDocumentFileType
RAW_DOCUMENT_FILE_TYPE_DOCX: RawDocumentFileType
RAW_DOCUMENT_FILE_TYPE_XLSX: RawDocumentFileType
RAW_DOCUMENT_FILE_TYPE_PPTX: RawDocumentFileType
RAW_DOCUMENT_FILE_TYPE_TEXT: RawDocumentFileType
RAW_DOCUMENT_FILE_TYPE_TIFF: RawDocumentFileType
CONTENT_CATEGORY_UNSPECIFIED: ContentCategory
CONTENT_CATEGORY_IMAGE: ContentCategory
CONTENT_CATEGORY_AUDIO: ContentCategory
CONTENT_CATEGORY_VIDEO: ContentCategory

class Document(_message.Message):
    __slots__ = ('name', 'reference_id', 'display_name', 'title', 'display_uri', 'document_schema_name', 'plain_text', 'cloud_ai_document', 'structured_content_uri', 'raw_document_path', 'inline_raw_document', 'properties', 'update_time', 'create_time', 'raw_document_file_type', 'async_enabled', 'content_category', 'text_extraction_disabled', 'text_extraction_enabled', 'creator', 'updater', 'disposition_time', 'legal_hold')
    NAME_FIELD_NUMBER: _ClassVar[int]
    REFERENCE_ID_FIELD_NUMBER: _ClassVar[int]
    DISPLAY_NAME_FIELD_NUMBER: _ClassVar[int]
    TITLE_FIELD_NUMBER: _ClassVar[int]
    DISPLAY_URI_FIELD_NUMBER: _ClassVar[int]
    DOCUMENT_SCHEMA_NAME_FIELD_NUMBER: _ClassVar[int]
    PLAIN_TEXT_FIELD_NUMBER: _ClassVar[int]
    CLOUD_AI_DOCUMENT_FIELD_NUMBER: _ClassVar[int]
    STRUCTURED_CONTENT_URI_FIELD_NUMBER: _ClassVar[int]
    RAW_DOCUMENT_PATH_FIELD_NUMBER: _ClassVar[int]
    INLINE_RAW_DOCUMENT_FIELD_NUMBER: _ClassVar[int]
    PROPERTIES_FIELD_NUMBER: _ClassVar[int]
    UPDATE_TIME_FIELD_NUMBER: _ClassVar[int]
    CREATE_TIME_FIELD_NUMBER: _ClassVar[int]
    RAW_DOCUMENT_FILE_TYPE_FIELD_NUMBER: _ClassVar[int]
    ASYNC_ENABLED_FIELD_NUMBER: _ClassVar[int]
    CONTENT_CATEGORY_FIELD_NUMBER: _ClassVar[int]
    TEXT_EXTRACTION_DISABLED_FIELD_NUMBER: _ClassVar[int]
    TEXT_EXTRACTION_ENABLED_FIELD_NUMBER: _ClassVar[int]
    CREATOR_FIELD_NUMBER: _ClassVar[int]
    UPDATER_FIELD_NUMBER: _ClassVar[int]
    DISPOSITION_TIME_FIELD_NUMBER: _ClassVar[int]
    LEGAL_HOLD_FIELD_NUMBER: _ClassVar[int]
    name: str
    reference_id: str
    display_name: str
    title: str
    display_uri: str
    document_schema_name: str
    plain_text: str
    cloud_ai_document: _document_pb2.Document
    structured_content_uri: str
    raw_document_path: str
    inline_raw_document: bytes
    properties: _containers.RepeatedCompositeFieldContainer[Property]
    update_time: _timestamp_pb2.Timestamp
    create_time: _timestamp_pb2.Timestamp
    raw_document_file_type: RawDocumentFileType
    async_enabled: bool
    content_category: ContentCategory
    text_extraction_disabled: bool
    text_extraction_enabled: bool
    creator: str
    updater: str
    disposition_time: _timestamp_pb2.Timestamp
    legal_hold: bool

    def __init__(self, name: _Optional[str]=..., reference_id: _Optional[str]=..., display_name: _Optional[str]=..., title: _Optional[str]=..., display_uri: _Optional[str]=..., document_schema_name: _Optional[str]=..., plain_text: _Optional[str]=..., cloud_ai_document: _Optional[_Union[_document_pb2.Document, _Mapping]]=..., structured_content_uri: _Optional[str]=..., raw_document_path: _Optional[str]=..., inline_raw_document: _Optional[bytes]=..., properties: _Optional[_Iterable[_Union[Property, _Mapping]]]=..., update_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]]=..., create_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]]=..., raw_document_file_type: _Optional[_Union[RawDocumentFileType, str]]=..., async_enabled: bool=..., content_category: _Optional[_Union[ContentCategory, str]]=..., text_extraction_disabled: bool=..., text_extraction_enabled: bool=..., creator: _Optional[str]=..., updater: _Optional[str]=..., disposition_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]]=..., legal_hold: bool=...) -> None:
        ...

class DocumentReference(_message.Message):
    __slots__ = ('document_name', 'display_name', 'snippet', 'document_is_folder', 'update_time', 'create_time', 'delete_time', 'document_is_retention_folder', 'document_is_legal_hold_folder')
    DOCUMENT_NAME_FIELD_NUMBER: _ClassVar[int]
    DISPLAY_NAME_FIELD_NUMBER: _ClassVar[int]
    SNIPPET_FIELD_NUMBER: _ClassVar[int]
    DOCUMENT_IS_FOLDER_FIELD_NUMBER: _ClassVar[int]
    UPDATE_TIME_FIELD_NUMBER: _ClassVar[int]
    CREATE_TIME_FIELD_NUMBER: _ClassVar[int]
    DELETE_TIME_FIELD_NUMBER: _ClassVar[int]
    DOCUMENT_IS_RETENTION_FOLDER_FIELD_NUMBER: _ClassVar[int]
    DOCUMENT_IS_LEGAL_HOLD_FOLDER_FIELD_NUMBER: _ClassVar[int]
    document_name: str
    display_name: str
    snippet: str
    document_is_folder: bool
    update_time: _timestamp_pb2.Timestamp
    create_time: _timestamp_pb2.Timestamp
    delete_time: _timestamp_pb2.Timestamp
    document_is_retention_folder: bool
    document_is_legal_hold_folder: bool

    def __init__(self, document_name: _Optional[str]=..., display_name: _Optional[str]=..., snippet: _Optional[str]=..., document_is_folder: bool=..., update_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]]=..., create_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]]=..., delete_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]]=..., document_is_retention_folder: bool=..., document_is_legal_hold_folder: bool=...) -> None:
        ...

class Property(_message.Message):
    __slots__ = ('name', 'integer_values', 'float_values', 'text_values', 'enum_values', 'property_values', 'date_time_values', 'map_property', 'timestamp_values')
    NAME_FIELD_NUMBER: _ClassVar[int]
    INTEGER_VALUES_FIELD_NUMBER: _ClassVar[int]
    FLOAT_VALUES_FIELD_NUMBER: _ClassVar[int]
    TEXT_VALUES_FIELD_NUMBER: _ClassVar[int]
    ENUM_VALUES_FIELD_NUMBER: _ClassVar[int]
    PROPERTY_VALUES_FIELD_NUMBER: _ClassVar[int]
    DATE_TIME_VALUES_FIELD_NUMBER: _ClassVar[int]
    MAP_PROPERTY_FIELD_NUMBER: _ClassVar[int]
    TIMESTAMP_VALUES_FIELD_NUMBER: _ClassVar[int]
    name: str
    integer_values: IntegerArray
    float_values: FloatArray
    text_values: TextArray
    enum_values: EnumArray
    property_values: PropertyArray
    date_time_values: DateTimeArray
    map_property: MapProperty
    timestamp_values: TimestampArray

    def __init__(self, name: _Optional[str]=..., integer_values: _Optional[_Union[IntegerArray, _Mapping]]=..., float_values: _Optional[_Union[FloatArray, _Mapping]]=..., text_values: _Optional[_Union[TextArray, _Mapping]]=..., enum_values: _Optional[_Union[EnumArray, _Mapping]]=..., property_values: _Optional[_Union[PropertyArray, _Mapping]]=..., date_time_values: _Optional[_Union[DateTimeArray, _Mapping]]=..., map_property: _Optional[_Union[MapProperty, _Mapping]]=..., timestamp_values: _Optional[_Union[TimestampArray, _Mapping]]=...) -> None:
        ...

class IntegerArray(_message.Message):
    __slots__ = ('values',)
    VALUES_FIELD_NUMBER: _ClassVar[int]
    values: _containers.RepeatedScalarFieldContainer[int]

    def __init__(self, values: _Optional[_Iterable[int]]=...) -> None:
        ...

class FloatArray(_message.Message):
    __slots__ = ('values',)
    VALUES_FIELD_NUMBER: _ClassVar[int]
    values: _containers.RepeatedScalarFieldContainer[float]

    def __init__(self, values: _Optional[_Iterable[float]]=...) -> None:
        ...

class TextArray(_message.Message):
    __slots__ = ('values',)
    VALUES_FIELD_NUMBER: _ClassVar[int]
    values: _containers.RepeatedScalarFieldContainer[str]

    def __init__(self, values: _Optional[_Iterable[str]]=...) -> None:
        ...

class EnumArray(_message.Message):
    __slots__ = ('values',)
    VALUES_FIELD_NUMBER: _ClassVar[int]
    values: _containers.RepeatedScalarFieldContainer[str]

    def __init__(self, values: _Optional[_Iterable[str]]=...) -> None:
        ...

class DateTimeArray(_message.Message):
    __slots__ = ('values',)
    VALUES_FIELD_NUMBER: _ClassVar[int]
    values: _containers.RepeatedCompositeFieldContainer[_datetime_pb2.DateTime]

    def __init__(self, values: _Optional[_Iterable[_Union[_datetime_pb2.DateTime, _Mapping]]]=...) -> None:
        ...

class TimestampArray(_message.Message):
    __slots__ = ('values',)
    VALUES_FIELD_NUMBER: _ClassVar[int]
    values: _containers.RepeatedCompositeFieldContainer[TimestampValue]

    def __init__(self, values: _Optional[_Iterable[_Union[TimestampValue, _Mapping]]]=...) -> None:
        ...

class TimestampValue(_message.Message):
    __slots__ = ('timestamp_value', 'text_value')
    TIMESTAMP_VALUE_FIELD_NUMBER: _ClassVar[int]
    TEXT_VALUE_FIELD_NUMBER: _ClassVar[int]
    timestamp_value: _timestamp_pb2.Timestamp
    text_value: str

    def __init__(self, timestamp_value: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]]=..., text_value: _Optional[str]=...) -> None:
        ...

class PropertyArray(_message.Message):
    __slots__ = ('properties',)
    PROPERTIES_FIELD_NUMBER: _ClassVar[int]
    properties: _containers.RepeatedCompositeFieldContainer[Property]

    def __init__(self, properties: _Optional[_Iterable[_Union[Property, _Mapping]]]=...) -> None:
        ...

class MapProperty(_message.Message):
    __slots__ = ('fields',)

    class FieldsEntry(_message.Message):
        __slots__ = ('key', 'value')
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: Value

        def __init__(self, key: _Optional[str]=..., value: _Optional[_Union[Value, _Mapping]]=...) -> None:
            ...
    FIELDS_FIELD_NUMBER: _ClassVar[int]
    fields: _containers.MessageMap[str, Value]

    def __init__(self, fields: _Optional[_Mapping[str, Value]]=...) -> None:
        ...

class Value(_message.Message):
    __slots__ = ('float_value', 'int_value', 'string_value', 'enum_value', 'datetime_value', 'timestamp_value', 'boolean_value')
    FLOAT_VALUE_FIELD_NUMBER: _ClassVar[int]
    INT_VALUE_FIELD_NUMBER: _ClassVar[int]
    STRING_VALUE_FIELD_NUMBER: _ClassVar[int]
    ENUM_VALUE_FIELD_NUMBER: _ClassVar[int]
    DATETIME_VALUE_FIELD_NUMBER: _ClassVar[int]
    TIMESTAMP_VALUE_FIELD_NUMBER: _ClassVar[int]
    BOOLEAN_VALUE_FIELD_NUMBER: _ClassVar[int]
    float_value: float
    int_value: int
    string_value: str
    enum_value: EnumValue
    datetime_value: _datetime_pb2.DateTime
    timestamp_value: TimestampValue
    boolean_value: bool

    def __init__(self, float_value: _Optional[float]=..., int_value: _Optional[int]=..., string_value: _Optional[str]=..., enum_value: _Optional[_Union[EnumValue, _Mapping]]=..., datetime_value: _Optional[_Union[_datetime_pb2.DateTime, _Mapping]]=..., timestamp_value: _Optional[_Union[TimestampValue, _Mapping]]=..., boolean_value: bool=...) -> None:
        ...

class EnumValue(_message.Message):
    __slots__ = ('value',)
    VALUE_FIELD_NUMBER: _ClassVar[int]
    value: str

    def __init__(self, value: _Optional[str]=...) -> None:
        ...