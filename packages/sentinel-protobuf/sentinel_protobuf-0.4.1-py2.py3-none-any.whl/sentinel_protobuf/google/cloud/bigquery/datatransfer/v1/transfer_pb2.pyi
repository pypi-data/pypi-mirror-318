from google.api import field_behavior_pb2 as _field_behavior_pb2
from google.api import resource_pb2 as _resource_pb2
from google.protobuf import struct_pb2 as _struct_pb2
from google.protobuf import timestamp_pb2 as _timestamp_pb2
from google.protobuf import wrappers_pb2 as _wrappers_pb2
from google.rpc import status_pb2 as _status_pb2
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class TransferType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    TRANSFER_TYPE_UNSPECIFIED: _ClassVar[TransferType]
    BATCH: _ClassVar[TransferType]
    STREAMING: _ClassVar[TransferType]

class TransferState(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    TRANSFER_STATE_UNSPECIFIED: _ClassVar[TransferState]
    PENDING: _ClassVar[TransferState]
    RUNNING: _ClassVar[TransferState]
    SUCCEEDED: _ClassVar[TransferState]
    FAILED: _ClassVar[TransferState]
    CANCELLED: _ClassVar[TransferState]
TRANSFER_TYPE_UNSPECIFIED: TransferType
BATCH: TransferType
STREAMING: TransferType
TRANSFER_STATE_UNSPECIFIED: TransferState
PENDING: TransferState
RUNNING: TransferState
SUCCEEDED: TransferState
FAILED: TransferState
CANCELLED: TransferState

class EmailPreferences(_message.Message):
    __slots__ = ("enable_failure_email",)
    ENABLE_FAILURE_EMAIL_FIELD_NUMBER: _ClassVar[int]
    enable_failure_email: bool
    def __init__(self, enable_failure_email: bool = ...) -> None: ...

class ScheduleOptions(_message.Message):
    __slots__ = ("disable_auto_scheduling", "start_time", "end_time")
    DISABLE_AUTO_SCHEDULING_FIELD_NUMBER: _ClassVar[int]
    START_TIME_FIELD_NUMBER: _ClassVar[int]
    END_TIME_FIELD_NUMBER: _ClassVar[int]
    disable_auto_scheduling: bool
    start_time: _timestamp_pb2.Timestamp
    end_time: _timestamp_pb2.Timestamp
    def __init__(self, disable_auto_scheduling: bool = ..., start_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., end_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ...) -> None: ...

class ScheduleOptionsV2(_message.Message):
    __slots__ = ("time_based_schedule", "manual_schedule", "event_driven_schedule")
    TIME_BASED_SCHEDULE_FIELD_NUMBER: _ClassVar[int]
    MANUAL_SCHEDULE_FIELD_NUMBER: _ClassVar[int]
    EVENT_DRIVEN_SCHEDULE_FIELD_NUMBER: _ClassVar[int]
    time_based_schedule: TimeBasedSchedule
    manual_schedule: ManualSchedule
    event_driven_schedule: EventDrivenSchedule
    def __init__(self, time_based_schedule: _Optional[_Union[TimeBasedSchedule, _Mapping]] = ..., manual_schedule: _Optional[_Union[ManualSchedule, _Mapping]] = ..., event_driven_schedule: _Optional[_Union[EventDrivenSchedule, _Mapping]] = ...) -> None: ...

class TimeBasedSchedule(_message.Message):
    __slots__ = ("schedule", "start_time", "end_time")
    SCHEDULE_FIELD_NUMBER: _ClassVar[int]
    START_TIME_FIELD_NUMBER: _ClassVar[int]
    END_TIME_FIELD_NUMBER: _ClassVar[int]
    schedule: str
    start_time: _timestamp_pb2.Timestamp
    end_time: _timestamp_pb2.Timestamp
    def __init__(self, schedule: _Optional[str] = ..., start_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., end_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ...) -> None: ...

class ManualSchedule(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class EventDrivenSchedule(_message.Message):
    __slots__ = ("pubsub_subscription",)
    PUBSUB_SUBSCRIPTION_FIELD_NUMBER: _ClassVar[int]
    pubsub_subscription: str
    def __init__(self, pubsub_subscription: _Optional[str] = ...) -> None: ...

class UserInfo(_message.Message):
    __slots__ = ("email",)
    EMAIL_FIELD_NUMBER: _ClassVar[int]
    email: str
    def __init__(self, email: _Optional[str] = ...) -> None: ...

class TransferConfig(_message.Message):
    __slots__ = ("name", "destination_dataset_id", "display_name", "data_source_id", "params", "schedule", "schedule_options", "schedule_options_v2", "data_refresh_window_days", "disabled", "update_time", "next_run_time", "state", "user_id", "dataset_region", "notification_pubsub_topic", "email_preferences", "owner_info", "encryption_configuration", "error")
    NAME_FIELD_NUMBER: _ClassVar[int]
    DESTINATION_DATASET_ID_FIELD_NUMBER: _ClassVar[int]
    DISPLAY_NAME_FIELD_NUMBER: _ClassVar[int]
    DATA_SOURCE_ID_FIELD_NUMBER: _ClassVar[int]
    PARAMS_FIELD_NUMBER: _ClassVar[int]
    SCHEDULE_FIELD_NUMBER: _ClassVar[int]
    SCHEDULE_OPTIONS_FIELD_NUMBER: _ClassVar[int]
    SCHEDULE_OPTIONS_V2_FIELD_NUMBER: _ClassVar[int]
    DATA_REFRESH_WINDOW_DAYS_FIELD_NUMBER: _ClassVar[int]
    DISABLED_FIELD_NUMBER: _ClassVar[int]
    UPDATE_TIME_FIELD_NUMBER: _ClassVar[int]
    NEXT_RUN_TIME_FIELD_NUMBER: _ClassVar[int]
    STATE_FIELD_NUMBER: _ClassVar[int]
    USER_ID_FIELD_NUMBER: _ClassVar[int]
    DATASET_REGION_FIELD_NUMBER: _ClassVar[int]
    NOTIFICATION_PUBSUB_TOPIC_FIELD_NUMBER: _ClassVar[int]
    EMAIL_PREFERENCES_FIELD_NUMBER: _ClassVar[int]
    OWNER_INFO_FIELD_NUMBER: _ClassVar[int]
    ENCRYPTION_CONFIGURATION_FIELD_NUMBER: _ClassVar[int]
    ERROR_FIELD_NUMBER: _ClassVar[int]
    name: str
    destination_dataset_id: str
    display_name: str
    data_source_id: str
    params: _struct_pb2.Struct
    schedule: str
    schedule_options: ScheduleOptions
    schedule_options_v2: ScheduleOptionsV2
    data_refresh_window_days: int
    disabled: bool
    update_time: _timestamp_pb2.Timestamp
    next_run_time: _timestamp_pb2.Timestamp
    state: TransferState
    user_id: int
    dataset_region: str
    notification_pubsub_topic: str
    email_preferences: EmailPreferences
    owner_info: UserInfo
    encryption_configuration: EncryptionConfiguration
    error: _status_pb2.Status
    def __init__(self, name: _Optional[str] = ..., destination_dataset_id: _Optional[str] = ..., display_name: _Optional[str] = ..., data_source_id: _Optional[str] = ..., params: _Optional[_Union[_struct_pb2.Struct, _Mapping]] = ..., schedule: _Optional[str] = ..., schedule_options: _Optional[_Union[ScheduleOptions, _Mapping]] = ..., schedule_options_v2: _Optional[_Union[ScheduleOptionsV2, _Mapping]] = ..., data_refresh_window_days: _Optional[int] = ..., disabled: bool = ..., update_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., next_run_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., state: _Optional[_Union[TransferState, str]] = ..., user_id: _Optional[int] = ..., dataset_region: _Optional[str] = ..., notification_pubsub_topic: _Optional[str] = ..., email_preferences: _Optional[_Union[EmailPreferences, _Mapping]] = ..., owner_info: _Optional[_Union[UserInfo, _Mapping]] = ..., encryption_configuration: _Optional[_Union[EncryptionConfiguration, _Mapping]] = ..., error: _Optional[_Union[_status_pb2.Status, _Mapping]] = ...) -> None: ...

class EncryptionConfiguration(_message.Message):
    __slots__ = ("kms_key_name",)
    KMS_KEY_NAME_FIELD_NUMBER: _ClassVar[int]
    kms_key_name: _wrappers_pb2.StringValue
    def __init__(self, kms_key_name: _Optional[_Union[_wrappers_pb2.StringValue, _Mapping]] = ...) -> None: ...

class TransferRun(_message.Message):
    __slots__ = ("name", "schedule_time", "run_time", "error_status", "start_time", "end_time", "update_time", "params", "destination_dataset_id", "data_source_id", "state", "user_id", "schedule", "notification_pubsub_topic", "email_preferences")
    NAME_FIELD_NUMBER: _ClassVar[int]
    SCHEDULE_TIME_FIELD_NUMBER: _ClassVar[int]
    RUN_TIME_FIELD_NUMBER: _ClassVar[int]
    ERROR_STATUS_FIELD_NUMBER: _ClassVar[int]
    START_TIME_FIELD_NUMBER: _ClassVar[int]
    END_TIME_FIELD_NUMBER: _ClassVar[int]
    UPDATE_TIME_FIELD_NUMBER: _ClassVar[int]
    PARAMS_FIELD_NUMBER: _ClassVar[int]
    DESTINATION_DATASET_ID_FIELD_NUMBER: _ClassVar[int]
    DATA_SOURCE_ID_FIELD_NUMBER: _ClassVar[int]
    STATE_FIELD_NUMBER: _ClassVar[int]
    USER_ID_FIELD_NUMBER: _ClassVar[int]
    SCHEDULE_FIELD_NUMBER: _ClassVar[int]
    NOTIFICATION_PUBSUB_TOPIC_FIELD_NUMBER: _ClassVar[int]
    EMAIL_PREFERENCES_FIELD_NUMBER: _ClassVar[int]
    name: str
    schedule_time: _timestamp_pb2.Timestamp
    run_time: _timestamp_pb2.Timestamp
    error_status: _status_pb2.Status
    start_time: _timestamp_pb2.Timestamp
    end_time: _timestamp_pb2.Timestamp
    update_time: _timestamp_pb2.Timestamp
    params: _struct_pb2.Struct
    destination_dataset_id: str
    data_source_id: str
    state: TransferState
    user_id: int
    schedule: str
    notification_pubsub_topic: str
    email_preferences: EmailPreferences
    def __init__(self, name: _Optional[str] = ..., schedule_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., run_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., error_status: _Optional[_Union[_status_pb2.Status, _Mapping]] = ..., start_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., end_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., update_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., params: _Optional[_Union[_struct_pb2.Struct, _Mapping]] = ..., destination_dataset_id: _Optional[str] = ..., data_source_id: _Optional[str] = ..., state: _Optional[_Union[TransferState, str]] = ..., user_id: _Optional[int] = ..., schedule: _Optional[str] = ..., notification_pubsub_topic: _Optional[str] = ..., email_preferences: _Optional[_Union[EmailPreferences, _Mapping]] = ...) -> None: ...

class TransferMessage(_message.Message):
    __slots__ = ("message_time", "severity", "message_text")
    class MessageSeverity(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        MESSAGE_SEVERITY_UNSPECIFIED: _ClassVar[TransferMessage.MessageSeverity]
        INFO: _ClassVar[TransferMessage.MessageSeverity]
        WARNING: _ClassVar[TransferMessage.MessageSeverity]
        ERROR: _ClassVar[TransferMessage.MessageSeverity]
    MESSAGE_SEVERITY_UNSPECIFIED: TransferMessage.MessageSeverity
    INFO: TransferMessage.MessageSeverity
    WARNING: TransferMessage.MessageSeverity
    ERROR: TransferMessage.MessageSeverity
    MESSAGE_TIME_FIELD_NUMBER: _ClassVar[int]
    SEVERITY_FIELD_NUMBER: _ClassVar[int]
    MESSAGE_TEXT_FIELD_NUMBER: _ClassVar[int]
    message_time: _timestamp_pb2.Timestamp
    severity: TransferMessage.MessageSeverity
    message_text: str
    def __init__(self, message_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., severity: _Optional[_Union[TransferMessage.MessageSeverity, str]] = ..., message_text: _Optional[str] = ...) -> None: ...
