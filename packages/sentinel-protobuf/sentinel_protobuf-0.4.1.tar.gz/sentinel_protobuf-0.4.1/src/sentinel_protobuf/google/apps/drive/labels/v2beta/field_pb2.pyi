from google.api import field_behavior_pb2 as _field_behavior_pb2
from google.apps.drive.labels.v2beta import common_pb2 as _common_pb2
from google.protobuf import timestamp_pb2 as _timestamp_pb2
from google.type import date_pb2 as _date_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union
DESCRIPTOR: _descriptor.FileDescriptor

class Field(_message.Message):
    __slots__ = ('text_options', 'integer_options', 'date_options', 'selection_options', 'user_options', 'id', 'query_key', 'properties', 'lifecycle', 'display_hints', 'schema_capabilities', 'applied_capabilities', 'creator', 'create_time', 'updater', 'update_time', 'publisher', 'disabler', 'disable_time', 'lock_status')

    class Properties(_message.Message):
        __slots__ = ('display_name', 'required', 'insert_before_field')
        DISPLAY_NAME_FIELD_NUMBER: _ClassVar[int]
        REQUIRED_FIELD_NUMBER: _ClassVar[int]
        INSERT_BEFORE_FIELD_FIELD_NUMBER: _ClassVar[int]
        display_name: str
        required: bool
        insert_before_field: str

        def __init__(self, display_name: _Optional[str]=..., required: bool=..., insert_before_field: _Optional[str]=...) -> None:
            ...

    class DisplayHints(_message.Message):
        __slots__ = ('required', 'disabled', 'hidden_in_search', 'shown_in_apply')
        REQUIRED_FIELD_NUMBER: _ClassVar[int]
        DISABLED_FIELD_NUMBER: _ClassVar[int]
        HIDDEN_IN_SEARCH_FIELD_NUMBER: _ClassVar[int]
        SHOWN_IN_APPLY_FIELD_NUMBER: _ClassVar[int]
        required: bool
        disabled: bool
        hidden_in_search: bool
        shown_in_apply: bool

        def __init__(self, required: bool=..., disabled: bool=..., hidden_in_search: bool=..., shown_in_apply: bool=...) -> None:
            ...

    class SchemaCapabilities(_message.Message):
        __slots__ = ('can_update', 'can_delete', 'can_disable', 'can_enable')
        CAN_UPDATE_FIELD_NUMBER: _ClassVar[int]
        CAN_DELETE_FIELD_NUMBER: _ClassVar[int]
        CAN_DISABLE_FIELD_NUMBER: _ClassVar[int]
        CAN_ENABLE_FIELD_NUMBER: _ClassVar[int]
        can_update: bool
        can_delete: bool
        can_disable: bool
        can_enable: bool

        def __init__(self, can_update: bool=..., can_delete: bool=..., can_disable: bool=..., can_enable: bool=...) -> None:
            ...

    class AppliedCapabilities(_message.Message):
        __slots__ = ('can_read', 'can_search', 'can_write')
        CAN_READ_FIELD_NUMBER: _ClassVar[int]
        CAN_SEARCH_FIELD_NUMBER: _ClassVar[int]
        CAN_WRITE_FIELD_NUMBER: _ClassVar[int]
        can_read: bool
        can_search: bool
        can_write: bool

        def __init__(self, can_read: bool=..., can_search: bool=..., can_write: bool=...) -> None:
            ...

    class ListOptions(_message.Message):
        __slots__ = ('max_entries',)
        MAX_ENTRIES_FIELD_NUMBER: _ClassVar[int]
        max_entries: int

        def __init__(self, max_entries: _Optional[int]=...) -> None:
            ...

    class TextOptions(_message.Message):
        __slots__ = ('min_length', 'max_length')
        MIN_LENGTH_FIELD_NUMBER: _ClassVar[int]
        MAX_LENGTH_FIELD_NUMBER: _ClassVar[int]
        min_length: int
        max_length: int

        def __init__(self, min_length: _Optional[int]=..., max_length: _Optional[int]=...) -> None:
            ...

    class IntegerOptions(_message.Message):
        __slots__ = ('min_value', 'max_value')
        MIN_VALUE_FIELD_NUMBER: _ClassVar[int]
        MAX_VALUE_FIELD_NUMBER: _ClassVar[int]
        min_value: int
        max_value: int

        def __init__(self, min_value: _Optional[int]=..., max_value: _Optional[int]=...) -> None:
            ...

    class DateOptions(_message.Message):
        __slots__ = ('date_format_type', 'date_format', 'min_value', 'max_value')

        class DateFormat(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
            __slots__ = ()
            DATE_FORMAT_UNSPECIFIED: _ClassVar[Field.DateOptions.DateFormat]
            LONG_DATE: _ClassVar[Field.DateOptions.DateFormat]
            SHORT_DATE: _ClassVar[Field.DateOptions.DateFormat]
        DATE_FORMAT_UNSPECIFIED: Field.DateOptions.DateFormat
        LONG_DATE: Field.DateOptions.DateFormat
        SHORT_DATE: Field.DateOptions.DateFormat
        DATE_FORMAT_TYPE_FIELD_NUMBER: _ClassVar[int]
        DATE_FORMAT_FIELD_NUMBER: _ClassVar[int]
        MIN_VALUE_FIELD_NUMBER: _ClassVar[int]
        MAX_VALUE_FIELD_NUMBER: _ClassVar[int]
        date_format_type: Field.DateOptions.DateFormat
        date_format: str
        min_value: _date_pb2.Date
        max_value: _date_pb2.Date

        def __init__(self, date_format_type: _Optional[_Union[Field.DateOptions.DateFormat, str]]=..., date_format: _Optional[str]=..., min_value: _Optional[_Union[_date_pb2.Date, _Mapping]]=..., max_value: _Optional[_Union[_date_pb2.Date, _Mapping]]=...) -> None:
            ...

    class SelectionOptions(_message.Message):
        __slots__ = ('list_options', 'choices')

        class Choice(_message.Message):
            __slots__ = ('id', 'properties', 'lifecycle', 'display_hints', 'schema_capabilities', 'applied_capabilities', 'creator', 'create_time', 'updater', 'update_time', 'publisher', 'publish_time', 'disabler', 'disable_time', 'lock_status')

            class Properties(_message.Message):
                __slots__ = ('display_name', 'description', 'badge_config', 'insert_before_choice')
                DISPLAY_NAME_FIELD_NUMBER: _ClassVar[int]
                DESCRIPTION_FIELD_NUMBER: _ClassVar[int]
                BADGE_CONFIG_FIELD_NUMBER: _ClassVar[int]
                INSERT_BEFORE_CHOICE_FIELD_NUMBER: _ClassVar[int]
                display_name: str
                description: str
                badge_config: _common_pb2.BadgeConfig
                insert_before_choice: str

                def __init__(self, display_name: _Optional[str]=..., description: _Optional[str]=..., badge_config: _Optional[_Union[_common_pb2.BadgeConfig, _Mapping]]=..., insert_before_choice: _Optional[str]=...) -> None:
                    ...

            class DisplayHints(_message.Message):
                __slots__ = ('disabled', 'hidden_in_search', 'shown_in_apply', 'badge_colors', 'dark_badge_colors', 'badge_priority')
                DISABLED_FIELD_NUMBER: _ClassVar[int]
                HIDDEN_IN_SEARCH_FIELD_NUMBER: _ClassVar[int]
                SHOWN_IN_APPLY_FIELD_NUMBER: _ClassVar[int]
                BADGE_COLORS_FIELD_NUMBER: _ClassVar[int]
                DARK_BADGE_COLORS_FIELD_NUMBER: _ClassVar[int]
                BADGE_PRIORITY_FIELD_NUMBER: _ClassVar[int]
                disabled: bool
                hidden_in_search: bool
                shown_in_apply: bool
                badge_colors: _common_pb2.BadgeColors
                dark_badge_colors: _common_pb2.BadgeColors
                badge_priority: int

                def __init__(self, disabled: bool=..., hidden_in_search: bool=..., shown_in_apply: bool=..., badge_colors: _Optional[_Union[_common_pb2.BadgeColors, _Mapping]]=..., dark_badge_colors: _Optional[_Union[_common_pb2.BadgeColors, _Mapping]]=..., badge_priority: _Optional[int]=...) -> None:
                    ...

            class SchemaCapabilities(_message.Message):
                __slots__ = ('can_update', 'can_delete', 'can_disable', 'can_enable')
                CAN_UPDATE_FIELD_NUMBER: _ClassVar[int]
                CAN_DELETE_FIELD_NUMBER: _ClassVar[int]
                CAN_DISABLE_FIELD_NUMBER: _ClassVar[int]
                CAN_ENABLE_FIELD_NUMBER: _ClassVar[int]
                can_update: bool
                can_delete: bool
                can_disable: bool
                can_enable: bool

                def __init__(self, can_update: bool=..., can_delete: bool=..., can_disable: bool=..., can_enable: bool=...) -> None:
                    ...

            class AppliedCapabilities(_message.Message):
                __slots__ = ('can_read', 'can_search', 'can_select')
                CAN_READ_FIELD_NUMBER: _ClassVar[int]
                CAN_SEARCH_FIELD_NUMBER: _ClassVar[int]
                CAN_SELECT_FIELD_NUMBER: _ClassVar[int]
                can_read: bool
                can_search: bool
                can_select: bool

                def __init__(self, can_read: bool=..., can_search: bool=..., can_select: bool=...) -> None:
                    ...
            ID_FIELD_NUMBER: _ClassVar[int]
            PROPERTIES_FIELD_NUMBER: _ClassVar[int]
            LIFECYCLE_FIELD_NUMBER: _ClassVar[int]
            DISPLAY_HINTS_FIELD_NUMBER: _ClassVar[int]
            SCHEMA_CAPABILITIES_FIELD_NUMBER: _ClassVar[int]
            APPLIED_CAPABILITIES_FIELD_NUMBER: _ClassVar[int]
            CREATOR_FIELD_NUMBER: _ClassVar[int]
            CREATE_TIME_FIELD_NUMBER: _ClassVar[int]
            UPDATER_FIELD_NUMBER: _ClassVar[int]
            UPDATE_TIME_FIELD_NUMBER: _ClassVar[int]
            PUBLISHER_FIELD_NUMBER: _ClassVar[int]
            PUBLISH_TIME_FIELD_NUMBER: _ClassVar[int]
            DISABLER_FIELD_NUMBER: _ClassVar[int]
            DISABLE_TIME_FIELD_NUMBER: _ClassVar[int]
            LOCK_STATUS_FIELD_NUMBER: _ClassVar[int]
            id: str
            properties: Field.SelectionOptions.Choice.Properties
            lifecycle: _common_pb2.Lifecycle
            display_hints: Field.SelectionOptions.Choice.DisplayHints
            schema_capabilities: Field.SelectionOptions.Choice.SchemaCapabilities
            applied_capabilities: Field.SelectionOptions.Choice.AppliedCapabilities
            creator: _common_pb2.UserInfo
            create_time: _timestamp_pb2.Timestamp
            updater: _common_pb2.UserInfo
            update_time: _timestamp_pb2.Timestamp
            publisher: _common_pb2.UserInfo
            publish_time: _timestamp_pb2.Timestamp
            disabler: _common_pb2.UserInfo
            disable_time: _timestamp_pb2.Timestamp
            lock_status: _common_pb2.LockStatus

            def __init__(self, id: _Optional[str]=..., properties: _Optional[_Union[Field.SelectionOptions.Choice.Properties, _Mapping]]=..., lifecycle: _Optional[_Union[_common_pb2.Lifecycle, _Mapping]]=..., display_hints: _Optional[_Union[Field.SelectionOptions.Choice.DisplayHints, _Mapping]]=..., schema_capabilities: _Optional[_Union[Field.SelectionOptions.Choice.SchemaCapabilities, _Mapping]]=..., applied_capabilities: _Optional[_Union[Field.SelectionOptions.Choice.AppliedCapabilities, _Mapping]]=..., creator: _Optional[_Union[_common_pb2.UserInfo, _Mapping]]=..., create_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]]=..., updater: _Optional[_Union[_common_pb2.UserInfo, _Mapping]]=..., update_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]]=..., publisher: _Optional[_Union[_common_pb2.UserInfo, _Mapping]]=..., publish_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]]=..., disabler: _Optional[_Union[_common_pb2.UserInfo, _Mapping]]=..., disable_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]]=..., lock_status: _Optional[_Union[_common_pb2.LockStatus, _Mapping]]=...) -> None:
                ...
        LIST_OPTIONS_FIELD_NUMBER: _ClassVar[int]
        CHOICES_FIELD_NUMBER: _ClassVar[int]
        list_options: Field.ListOptions
        choices: _containers.RepeatedCompositeFieldContainer[Field.SelectionOptions.Choice]

        def __init__(self, list_options: _Optional[_Union[Field.ListOptions, _Mapping]]=..., choices: _Optional[_Iterable[_Union[Field.SelectionOptions.Choice, _Mapping]]]=...) -> None:
            ...

    class UserOptions(_message.Message):
        __slots__ = ('list_options',)
        LIST_OPTIONS_FIELD_NUMBER: _ClassVar[int]
        list_options: Field.ListOptions

        def __init__(self, list_options: _Optional[_Union[Field.ListOptions, _Mapping]]=...) -> None:
            ...
    TEXT_OPTIONS_FIELD_NUMBER: _ClassVar[int]
    INTEGER_OPTIONS_FIELD_NUMBER: _ClassVar[int]
    DATE_OPTIONS_FIELD_NUMBER: _ClassVar[int]
    SELECTION_OPTIONS_FIELD_NUMBER: _ClassVar[int]
    USER_OPTIONS_FIELD_NUMBER: _ClassVar[int]
    ID_FIELD_NUMBER: _ClassVar[int]
    QUERY_KEY_FIELD_NUMBER: _ClassVar[int]
    PROPERTIES_FIELD_NUMBER: _ClassVar[int]
    LIFECYCLE_FIELD_NUMBER: _ClassVar[int]
    DISPLAY_HINTS_FIELD_NUMBER: _ClassVar[int]
    SCHEMA_CAPABILITIES_FIELD_NUMBER: _ClassVar[int]
    APPLIED_CAPABILITIES_FIELD_NUMBER: _ClassVar[int]
    CREATOR_FIELD_NUMBER: _ClassVar[int]
    CREATE_TIME_FIELD_NUMBER: _ClassVar[int]
    UPDATER_FIELD_NUMBER: _ClassVar[int]
    UPDATE_TIME_FIELD_NUMBER: _ClassVar[int]
    PUBLISHER_FIELD_NUMBER: _ClassVar[int]
    DISABLER_FIELD_NUMBER: _ClassVar[int]
    DISABLE_TIME_FIELD_NUMBER: _ClassVar[int]
    LOCK_STATUS_FIELD_NUMBER: _ClassVar[int]
    text_options: Field.TextOptions
    integer_options: Field.IntegerOptions
    date_options: Field.DateOptions
    selection_options: Field.SelectionOptions
    user_options: Field.UserOptions
    id: str
    query_key: str
    properties: Field.Properties
    lifecycle: _common_pb2.Lifecycle
    display_hints: Field.DisplayHints
    schema_capabilities: Field.SchemaCapabilities
    applied_capabilities: Field.AppliedCapabilities
    creator: _common_pb2.UserInfo
    create_time: _timestamp_pb2.Timestamp
    updater: _common_pb2.UserInfo
    update_time: _timestamp_pb2.Timestamp
    publisher: _common_pb2.UserInfo
    disabler: _common_pb2.UserInfo
    disable_time: _timestamp_pb2.Timestamp
    lock_status: _common_pb2.LockStatus

    def __init__(self, text_options: _Optional[_Union[Field.TextOptions, _Mapping]]=..., integer_options: _Optional[_Union[Field.IntegerOptions, _Mapping]]=..., date_options: _Optional[_Union[Field.DateOptions, _Mapping]]=..., selection_options: _Optional[_Union[Field.SelectionOptions, _Mapping]]=..., user_options: _Optional[_Union[Field.UserOptions, _Mapping]]=..., id: _Optional[str]=..., query_key: _Optional[str]=..., properties: _Optional[_Union[Field.Properties, _Mapping]]=..., lifecycle: _Optional[_Union[_common_pb2.Lifecycle, _Mapping]]=..., display_hints: _Optional[_Union[Field.DisplayHints, _Mapping]]=..., schema_capabilities: _Optional[_Union[Field.SchemaCapabilities, _Mapping]]=..., applied_capabilities: _Optional[_Union[Field.AppliedCapabilities, _Mapping]]=..., creator: _Optional[_Union[_common_pb2.UserInfo, _Mapping]]=..., create_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]]=..., updater: _Optional[_Union[_common_pb2.UserInfo, _Mapping]]=..., update_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]]=..., publisher: _Optional[_Union[_common_pb2.UserInfo, _Mapping]]=..., disabler: _Optional[_Union[_common_pb2.UserInfo, _Mapping]]=..., disable_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]]=..., lock_status: _Optional[_Union[_common_pb2.LockStatus, _Mapping]]=...) -> None:
        ...