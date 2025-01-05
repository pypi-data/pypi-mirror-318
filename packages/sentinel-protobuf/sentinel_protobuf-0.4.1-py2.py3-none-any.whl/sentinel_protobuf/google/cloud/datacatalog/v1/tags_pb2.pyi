from google.api import field_behavior_pb2 as _field_behavior_pb2
from google.api import resource_pb2 as _resource_pb2
from google.protobuf import timestamp_pb2 as _timestamp_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union
DESCRIPTOR: _descriptor.FileDescriptor

class Tag(_message.Message):
    __slots__ = ('name', 'template', 'template_display_name', 'column', 'fields', 'dataplex_transfer_status')

    class FieldsEntry(_message.Message):
        __slots__ = ('key', 'value')
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: TagField

        def __init__(self, key: _Optional[str]=..., value: _Optional[_Union[TagField, _Mapping]]=...) -> None:
            ...
    NAME_FIELD_NUMBER: _ClassVar[int]
    TEMPLATE_FIELD_NUMBER: _ClassVar[int]
    TEMPLATE_DISPLAY_NAME_FIELD_NUMBER: _ClassVar[int]
    COLUMN_FIELD_NUMBER: _ClassVar[int]
    FIELDS_FIELD_NUMBER: _ClassVar[int]
    DATAPLEX_TRANSFER_STATUS_FIELD_NUMBER: _ClassVar[int]
    name: str
    template: str
    template_display_name: str
    column: str
    fields: _containers.MessageMap[str, TagField]
    dataplex_transfer_status: TagTemplate.DataplexTransferStatus

    def __init__(self, name: _Optional[str]=..., template: _Optional[str]=..., template_display_name: _Optional[str]=..., column: _Optional[str]=..., fields: _Optional[_Mapping[str, TagField]]=..., dataplex_transfer_status: _Optional[_Union[TagTemplate.DataplexTransferStatus, str]]=...) -> None:
        ...

class TagField(_message.Message):
    __slots__ = ('display_name', 'double_value', 'string_value', 'bool_value', 'timestamp_value', 'enum_value', 'richtext_value', 'order')

    class EnumValue(_message.Message):
        __slots__ = ('display_name',)
        DISPLAY_NAME_FIELD_NUMBER: _ClassVar[int]
        display_name: str

        def __init__(self, display_name: _Optional[str]=...) -> None:
            ...
    DISPLAY_NAME_FIELD_NUMBER: _ClassVar[int]
    DOUBLE_VALUE_FIELD_NUMBER: _ClassVar[int]
    STRING_VALUE_FIELD_NUMBER: _ClassVar[int]
    BOOL_VALUE_FIELD_NUMBER: _ClassVar[int]
    TIMESTAMP_VALUE_FIELD_NUMBER: _ClassVar[int]
    ENUM_VALUE_FIELD_NUMBER: _ClassVar[int]
    RICHTEXT_VALUE_FIELD_NUMBER: _ClassVar[int]
    ORDER_FIELD_NUMBER: _ClassVar[int]
    display_name: str
    double_value: float
    string_value: str
    bool_value: bool
    timestamp_value: _timestamp_pb2.Timestamp
    enum_value: TagField.EnumValue
    richtext_value: str
    order: int

    def __init__(self, display_name: _Optional[str]=..., double_value: _Optional[float]=..., string_value: _Optional[str]=..., bool_value: bool=..., timestamp_value: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]]=..., enum_value: _Optional[_Union[TagField.EnumValue, _Mapping]]=..., richtext_value: _Optional[str]=..., order: _Optional[int]=...) -> None:
        ...

class TagTemplate(_message.Message):
    __slots__ = ('name', 'display_name', 'is_publicly_readable', 'fields', 'dataplex_transfer_status')

    class DataplexTransferStatus(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        DATAPLEX_TRANSFER_STATUS_UNSPECIFIED: _ClassVar[TagTemplate.DataplexTransferStatus]
        MIGRATED: _ClassVar[TagTemplate.DataplexTransferStatus]
        TRANSFERRED: _ClassVar[TagTemplate.DataplexTransferStatus]
    DATAPLEX_TRANSFER_STATUS_UNSPECIFIED: TagTemplate.DataplexTransferStatus
    MIGRATED: TagTemplate.DataplexTransferStatus
    TRANSFERRED: TagTemplate.DataplexTransferStatus

    class FieldsEntry(_message.Message):
        __slots__ = ('key', 'value')
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: TagTemplateField

        def __init__(self, key: _Optional[str]=..., value: _Optional[_Union[TagTemplateField, _Mapping]]=...) -> None:
            ...
    NAME_FIELD_NUMBER: _ClassVar[int]
    DISPLAY_NAME_FIELD_NUMBER: _ClassVar[int]
    IS_PUBLICLY_READABLE_FIELD_NUMBER: _ClassVar[int]
    FIELDS_FIELD_NUMBER: _ClassVar[int]
    DATAPLEX_TRANSFER_STATUS_FIELD_NUMBER: _ClassVar[int]
    name: str
    display_name: str
    is_publicly_readable: bool
    fields: _containers.MessageMap[str, TagTemplateField]
    dataplex_transfer_status: TagTemplate.DataplexTransferStatus

    def __init__(self, name: _Optional[str]=..., display_name: _Optional[str]=..., is_publicly_readable: bool=..., fields: _Optional[_Mapping[str, TagTemplateField]]=..., dataplex_transfer_status: _Optional[_Union[TagTemplate.DataplexTransferStatus, str]]=...) -> None:
        ...

class TagTemplateField(_message.Message):
    __slots__ = ('name', 'display_name', 'type', 'is_required', 'description', 'order')
    NAME_FIELD_NUMBER: _ClassVar[int]
    DISPLAY_NAME_FIELD_NUMBER: _ClassVar[int]
    TYPE_FIELD_NUMBER: _ClassVar[int]
    IS_REQUIRED_FIELD_NUMBER: _ClassVar[int]
    DESCRIPTION_FIELD_NUMBER: _ClassVar[int]
    ORDER_FIELD_NUMBER: _ClassVar[int]
    name: str
    display_name: str
    type: FieldType
    is_required: bool
    description: str
    order: int

    def __init__(self, name: _Optional[str]=..., display_name: _Optional[str]=..., type: _Optional[_Union[FieldType, _Mapping]]=..., is_required: bool=..., description: _Optional[str]=..., order: _Optional[int]=...) -> None:
        ...

class FieldType(_message.Message):
    __slots__ = ('primitive_type', 'enum_type')

    class PrimitiveType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        PRIMITIVE_TYPE_UNSPECIFIED: _ClassVar[FieldType.PrimitiveType]
        DOUBLE: _ClassVar[FieldType.PrimitiveType]
        STRING: _ClassVar[FieldType.PrimitiveType]
        BOOL: _ClassVar[FieldType.PrimitiveType]
        TIMESTAMP: _ClassVar[FieldType.PrimitiveType]
        RICHTEXT: _ClassVar[FieldType.PrimitiveType]
    PRIMITIVE_TYPE_UNSPECIFIED: FieldType.PrimitiveType
    DOUBLE: FieldType.PrimitiveType
    STRING: FieldType.PrimitiveType
    BOOL: FieldType.PrimitiveType
    TIMESTAMP: FieldType.PrimitiveType
    RICHTEXT: FieldType.PrimitiveType

    class EnumType(_message.Message):
        __slots__ = ('allowed_values',)

        class EnumValue(_message.Message):
            __slots__ = ('display_name',)
            DISPLAY_NAME_FIELD_NUMBER: _ClassVar[int]
            display_name: str

            def __init__(self, display_name: _Optional[str]=...) -> None:
                ...
        ALLOWED_VALUES_FIELD_NUMBER: _ClassVar[int]
        allowed_values: _containers.RepeatedCompositeFieldContainer[FieldType.EnumType.EnumValue]

        def __init__(self, allowed_values: _Optional[_Iterable[_Union[FieldType.EnumType.EnumValue, _Mapping]]]=...) -> None:
            ...
    PRIMITIVE_TYPE_FIELD_NUMBER: _ClassVar[int]
    ENUM_TYPE_FIELD_NUMBER: _ClassVar[int]
    primitive_type: FieldType.PrimitiveType
    enum_type: FieldType.EnumType

    def __init__(self, primitive_type: _Optional[_Union[FieldType.PrimitiveType, str]]=..., enum_type: _Optional[_Union[FieldType.EnumType, _Mapping]]=...) -> None:
        ...