from google.api import resource_pb2 as _resource_pb2
from google.type import date_pb2 as _date_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Mapping as _Mapping, Optional as _Optional, Union as _Union
DESCRIPTOR: _descriptor.FileDescriptor

class LabelLimits(_message.Message):
    __slots__ = ('name', 'max_title_length', 'max_description_length', 'max_fields', 'max_deleted_fields', 'max_draft_revisions', 'field_limits')
    NAME_FIELD_NUMBER: _ClassVar[int]
    MAX_TITLE_LENGTH_FIELD_NUMBER: _ClassVar[int]
    MAX_DESCRIPTION_LENGTH_FIELD_NUMBER: _ClassVar[int]
    MAX_FIELDS_FIELD_NUMBER: _ClassVar[int]
    MAX_DELETED_FIELDS_FIELD_NUMBER: _ClassVar[int]
    MAX_DRAFT_REVISIONS_FIELD_NUMBER: _ClassVar[int]
    FIELD_LIMITS_FIELD_NUMBER: _ClassVar[int]
    name: str
    max_title_length: int
    max_description_length: int
    max_fields: int
    max_deleted_fields: int
    max_draft_revisions: int
    field_limits: FieldLimits

    def __init__(self, name: _Optional[str]=..., max_title_length: _Optional[int]=..., max_description_length: _Optional[int]=..., max_fields: _Optional[int]=..., max_deleted_fields: _Optional[int]=..., max_draft_revisions: _Optional[int]=..., field_limits: _Optional[_Union[FieldLimits, _Mapping]]=...) -> None:
        ...

class FieldLimits(_message.Message):
    __slots__ = ('max_id_length', 'max_display_name_length', 'max_description_length', 'text_limits', 'long_text_limits', 'integer_limits', 'date_limits', 'user_limits', 'selection_limits')
    MAX_ID_LENGTH_FIELD_NUMBER: _ClassVar[int]
    MAX_DISPLAY_NAME_LENGTH_FIELD_NUMBER: _ClassVar[int]
    MAX_DESCRIPTION_LENGTH_FIELD_NUMBER: _ClassVar[int]
    TEXT_LIMITS_FIELD_NUMBER: _ClassVar[int]
    LONG_TEXT_LIMITS_FIELD_NUMBER: _ClassVar[int]
    INTEGER_LIMITS_FIELD_NUMBER: _ClassVar[int]
    DATE_LIMITS_FIELD_NUMBER: _ClassVar[int]
    USER_LIMITS_FIELD_NUMBER: _ClassVar[int]
    SELECTION_LIMITS_FIELD_NUMBER: _ClassVar[int]
    max_id_length: int
    max_display_name_length: int
    max_description_length: int
    text_limits: TextLimits
    long_text_limits: LongTextLimits
    integer_limits: IntegerLimits
    date_limits: DateLimits
    user_limits: UserLimits
    selection_limits: SelectionLimits

    def __init__(self, max_id_length: _Optional[int]=..., max_display_name_length: _Optional[int]=..., max_description_length: _Optional[int]=..., text_limits: _Optional[_Union[TextLimits, _Mapping]]=..., long_text_limits: _Optional[_Union[LongTextLimits, _Mapping]]=..., integer_limits: _Optional[_Union[IntegerLimits, _Mapping]]=..., date_limits: _Optional[_Union[DateLimits, _Mapping]]=..., user_limits: _Optional[_Union[UserLimits, _Mapping]]=..., selection_limits: _Optional[_Union[SelectionLimits, _Mapping]]=...) -> None:
        ...

class ListLimits(_message.Message):
    __slots__ = ('max_entries',)
    MAX_ENTRIES_FIELD_NUMBER: _ClassVar[int]
    max_entries: int

    def __init__(self, max_entries: _Optional[int]=...) -> None:
        ...

class TextLimits(_message.Message):
    __slots__ = ('min_length', 'max_length')
    MIN_LENGTH_FIELD_NUMBER: _ClassVar[int]
    MAX_LENGTH_FIELD_NUMBER: _ClassVar[int]
    min_length: int
    max_length: int

    def __init__(self, min_length: _Optional[int]=..., max_length: _Optional[int]=...) -> None:
        ...

class LongTextLimits(_message.Message):
    __slots__ = ('min_length', 'max_length')
    MIN_LENGTH_FIELD_NUMBER: _ClassVar[int]
    MAX_LENGTH_FIELD_NUMBER: _ClassVar[int]
    min_length: int
    max_length: int

    def __init__(self, min_length: _Optional[int]=..., max_length: _Optional[int]=...) -> None:
        ...

class IntegerLimits(_message.Message):
    __slots__ = ('min_value', 'max_value')
    MIN_VALUE_FIELD_NUMBER: _ClassVar[int]
    MAX_VALUE_FIELD_NUMBER: _ClassVar[int]
    min_value: int
    max_value: int

    def __init__(self, min_value: _Optional[int]=..., max_value: _Optional[int]=...) -> None:
        ...

class DateLimits(_message.Message):
    __slots__ = ('min_value', 'max_value')
    MIN_VALUE_FIELD_NUMBER: _ClassVar[int]
    MAX_VALUE_FIELD_NUMBER: _ClassVar[int]
    min_value: _date_pb2.Date
    max_value: _date_pb2.Date

    def __init__(self, min_value: _Optional[_Union[_date_pb2.Date, _Mapping]]=..., max_value: _Optional[_Union[_date_pb2.Date, _Mapping]]=...) -> None:
        ...

class SelectionLimits(_message.Message):
    __slots__ = ('list_limits', 'max_id_length', 'max_display_name_length', 'max_choices', 'max_deleted_choices')
    LIST_LIMITS_FIELD_NUMBER: _ClassVar[int]
    MAX_ID_LENGTH_FIELD_NUMBER: _ClassVar[int]
    MAX_DISPLAY_NAME_LENGTH_FIELD_NUMBER: _ClassVar[int]
    MAX_CHOICES_FIELD_NUMBER: _ClassVar[int]
    MAX_DELETED_CHOICES_FIELD_NUMBER: _ClassVar[int]
    list_limits: ListLimits
    max_id_length: int
    max_display_name_length: int
    max_choices: int
    max_deleted_choices: int

    def __init__(self, list_limits: _Optional[_Union[ListLimits, _Mapping]]=..., max_id_length: _Optional[int]=..., max_display_name_length: _Optional[int]=..., max_choices: _Optional[int]=..., max_deleted_choices: _Optional[int]=...) -> None:
        ...

class UserLimits(_message.Message):
    __slots__ = ('list_limits',)
    LIST_LIMITS_FIELD_NUMBER: _ClassVar[int]
    list_limits: ListLimits

    def __init__(self, list_limits: _Optional[_Union[ListLimits, _Mapping]]=...) -> None:
        ...