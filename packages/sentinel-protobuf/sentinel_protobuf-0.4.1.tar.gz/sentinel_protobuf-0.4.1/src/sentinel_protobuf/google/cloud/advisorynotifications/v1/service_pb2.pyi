from google.api import annotations_pb2 as _annotations_pb2
from google.api import client_pb2 as _client_pb2
from google.api import field_behavior_pb2 as _field_behavior_pb2
from google.api import resource_pb2 as _resource_pb2
from google.protobuf import timestamp_pb2 as _timestamp_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union
DESCRIPTOR: _descriptor.FileDescriptor

class NotificationView(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    NOTIFICATION_VIEW_UNSPECIFIED: _ClassVar[NotificationView]
    BASIC: _ClassVar[NotificationView]
    FULL: _ClassVar[NotificationView]

class LocalizationState(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    LOCALIZATION_STATE_UNSPECIFIED: _ClassVar[LocalizationState]
    LOCALIZATION_STATE_NOT_APPLICABLE: _ClassVar[LocalizationState]
    LOCALIZATION_STATE_PENDING: _ClassVar[LocalizationState]
    LOCALIZATION_STATE_COMPLETED: _ClassVar[LocalizationState]

class NotificationType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    NOTIFICATION_TYPE_UNSPECIFIED: _ClassVar[NotificationType]
    NOTIFICATION_TYPE_SECURITY_PRIVACY_ADVISORY: _ClassVar[NotificationType]
    NOTIFICATION_TYPE_SENSITIVE_ACTIONS: _ClassVar[NotificationType]
    NOTIFICATION_TYPE_SECURITY_MSA: _ClassVar[NotificationType]
    NOTIFICATION_TYPE_THREAT_HORIZONS: _ClassVar[NotificationType]
NOTIFICATION_VIEW_UNSPECIFIED: NotificationView
BASIC: NotificationView
FULL: NotificationView
LOCALIZATION_STATE_UNSPECIFIED: LocalizationState
LOCALIZATION_STATE_NOT_APPLICABLE: LocalizationState
LOCALIZATION_STATE_PENDING: LocalizationState
LOCALIZATION_STATE_COMPLETED: LocalizationState
NOTIFICATION_TYPE_UNSPECIFIED: NotificationType
NOTIFICATION_TYPE_SECURITY_PRIVACY_ADVISORY: NotificationType
NOTIFICATION_TYPE_SENSITIVE_ACTIONS: NotificationType
NOTIFICATION_TYPE_SECURITY_MSA: NotificationType
NOTIFICATION_TYPE_THREAT_HORIZONS: NotificationType

class Notification(_message.Message):
    __slots__ = ('name', 'subject', 'messages', 'create_time', 'notification_type')
    NAME_FIELD_NUMBER: _ClassVar[int]
    SUBJECT_FIELD_NUMBER: _ClassVar[int]
    MESSAGES_FIELD_NUMBER: _ClassVar[int]
    CREATE_TIME_FIELD_NUMBER: _ClassVar[int]
    NOTIFICATION_TYPE_FIELD_NUMBER: _ClassVar[int]
    name: str
    subject: Subject
    messages: _containers.RepeatedCompositeFieldContainer[Message]
    create_time: _timestamp_pb2.Timestamp
    notification_type: NotificationType

    def __init__(self, name: _Optional[str]=..., subject: _Optional[_Union[Subject, _Mapping]]=..., messages: _Optional[_Iterable[_Union[Message, _Mapping]]]=..., create_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]]=..., notification_type: _Optional[_Union[NotificationType, str]]=...) -> None:
        ...

class Text(_message.Message):
    __slots__ = ('en_text', 'localized_text', 'localization_state')
    EN_TEXT_FIELD_NUMBER: _ClassVar[int]
    LOCALIZED_TEXT_FIELD_NUMBER: _ClassVar[int]
    LOCALIZATION_STATE_FIELD_NUMBER: _ClassVar[int]
    en_text: str
    localized_text: str
    localization_state: LocalizationState

    def __init__(self, en_text: _Optional[str]=..., localized_text: _Optional[str]=..., localization_state: _Optional[_Union[LocalizationState, str]]=...) -> None:
        ...

class Subject(_message.Message):
    __slots__ = ('text',)
    TEXT_FIELD_NUMBER: _ClassVar[int]
    text: Text

    def __init__(self, text: _Optional[_Union[Text, _Mapping]]=...) -> None:
        ...

class Message(_message.Message):
    __slots__ = ('body', 'attachments', 'create_time', 'localization_time')

    class Body(_message.Message):
        __slots__ = ('text',)
        TEXT_FIELD_NUMBER: _ClassVar[int]
        text: Text

        def __init__(self, text: _Optional[_Union[Text, _Mapping]]=...) -> None:
            ...
    BODY_FIELD_NUMBER: _ClassVar[int]
    ATTACHMENTS_FIELD_NUMBER: _ClassVar[int]
    CREATE_TIME_FIELD_NUMBER: _ClassVar[int]
    LOCALIZATION_TIME_FIELD_NUMBER: _ClassVar[int]
    body: Message.Body
    attachments: _containers.RepeatedCompositeFieldContainer[Attachment]
    create_time: _timestamp_pb2.Timestamp
    localization_time: _timestamp_pb2.Timestamp

    def __init__(self, body: _Optional[_Union[Message.Body, _Mapping]]=..., attachments: _Optional[_Iterable[_Union[Attachment, _Mapping]]]=..., create_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]]=..., localization_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]]=...) -> None:
        ...

class Attachment(_message.Message):
    __slots__ = ('csv', 'display_name')
    CSV_FIELD_NUMBER: _ClassVar[int]
    DISPLAY_NAME_FIELD_NUMBER: _ClassVar[int]
    csv: Csv
    display_name: str

    def __init__(self, csv: _Optional[_Union[Csv, _Mapping]]=..., display_name: _Optional[str]=...) -> None:
        ...

class Csv(_message.Message):
    __slots__ = ('headers', 'data_rows')

    class CsvRow(_message.Message):
        __slots__ = ('entries',)
        ENTRIES_FIELD_NUMBER: _ClassVar[int]
        entries: _containers.RepeatedScalarFieldContainer[str]

        def __init__(self, entries: _Optional[_Iterable[str]]=...) -> None:
            ...
    HEADERS_FIELD_NUMBER: _ClassVar[int]
    DATA_ROWS_FIELD_NUMBER: _ClassVar[int]
    headers: _containers.RepeatedScalarFieldContainer[str]
    data_rows: _containers.RepeatedCompositeFieldContainer[Csv.CsvRow]

    def __init__(self, headers: _Optional[_Iterable[str]]=..., data_rows: _Optional[_Iterable[_Union[Csv.CsvRow, _Mapping]]]=...) -> None:
        ...

class ListNotificationsRequest(_message.Message):
    __slots__ = ('parent', 'page_size', 'page_token', 'view', 'language_code')
    PARENT_FIELD_NUMBER: _ClassVar[int]
    PAGE_SIZE_FIELD_NUMBER: _ClassVar[int]
    PAGE_TOKEN_FIELD_NUMBER: _ClassVar[int]
    VIEW_FIELD_NUMBER: _ClassVar[int]
    LANGUAGE_CODE_FIELD_NUMBER: _ClassVar[int]
    parent: str
    page_size: int
    page_token: str
    view: NotificationView
    language_code: str

    def __init__(self, parent: _Optional[str]=..., page_size: _Optional[int]=..., page_token: _Optional[str]=..., view: _Optional[_Union[NotificationView, str]]=..., language_code: _Optional[str]=...) -> None:
        ...

class ListNotificationsResponse(_message.Message):
    __slots__ = ('notifications', 'next_page_token', 'total_size')
    NOTIFICATIONS_FIELD_NUMBER: _ClassVar[int]
    NEXT_PAGE_TOKEN_FIELD_NUMBER: _ClassVar[int]
    TOTAL_SIZE_FIELD_NUMBER: _ClassVar[int]
    notifications: _containers.RepeatedCompositeFieldContainer[Notification]
    next_page_token: str
    total_size: int

    def __init__(self, notifications: _Optional[_Iterable[_Union[Notification, _Mapping]]]=..., next_page_token: _Optional[str]=..., total_size: _Optional[int]=...) -> None:
        ...

class GetNotificationRequest(_message.Message):
    __slots__ = ('name', 'language_code')
    NAME_FIELD_NUMBER: _ClassVar[int]
    LANGUAGE_CODE_FIELD_NUMBER: _ClassVar[int]
    name: str
    language_code: str

    def __init__(self, name: _Optional[str]=..., language_code: _Optional[str]=...) -> None:
        ...

class Settings(_message.Message):
    __slots__ = ('name', 'notification_settings', 'etag')

    class NotificationSettingsEntry(_message.Message):
        __slots__ = ('key', 'value')
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: NotificationSettings

        def __init__(self, key: _Optional[str]=..., value: _Optional[_Union[NotificationSettings, _Mapping]]=...) -> None:
            ...
    NAME_FIELD_NUMBER: _ClassVar[int]
    NOTIFICATION_SETTINGS_FIELD_NUMBER: _ClassVar[int]
    ETAG_FIELD_NUMBER: _ClassVar[int]
    name: str
    notification_settings: _containers.MessageMap[str, NotificationSettings]
    etag: str

    def __init__(self, name: _Optional[str]=..., notification_settings: _Optional[_Mapping[str, NotificationSettings]]=..., etag: _Optional[str]=...) -> None:
        ...

class NotificationSettings(_message.Message):
    __slots__ = ('enabled',)
    ENABLED_FIELD_NUMBER: _ClassVar[int]
    enabled: bool

    def __init__(self, enabled: bool=...) -> None:
        ...

class GetSettingsRequest(_message.Message):
    __slots__ = ('name',)
    NAME_FIELD_NUMBER: _ClassVar[int]
    name: str

    def __init__(self, name: _Optional[str]=...) -> None:
        ...

class UpdateSettingsRequest(_message.Message):
    __slots__ = ('settings',)
    SETTINGS_FIELD_NUMBER: _ClassVar[int]
    settings: Settings

    def __init__(self, settings: _Optional[_Union[Settings, _Mapping]]=...) -> None:
        ...