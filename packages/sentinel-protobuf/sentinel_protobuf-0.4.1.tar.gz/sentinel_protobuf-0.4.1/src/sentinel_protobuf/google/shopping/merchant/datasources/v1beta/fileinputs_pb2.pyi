from google.api import field_behavior_pb2 as _field_behavior_pb2
from google.type import dayofweek_pb2 as _dayofweek_pb2
from google.type import timeofday_pb2 as _timeofday_pb2
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Mapping as _Mapping, Optional as _Optional, Union as _Union
DESCRIPTOR: _descriptor.FileDescriptor

class FileInput(_message.Message):
    __slots__ = ('fetch_settings', 'file_name', 'file_input_type')

    class FileInputType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        FILE_INPUT_TYPE_UNSPECIFIED: _ClassVar[FileInput.FileInputType]
        UPLOAD: _ClassVar[FileInput.FileInputType]
        FETCH: _ClassVar[FileInput.FileInputType]
        GOOGLE_SHEETS: _ClassVar[FileInput.FileInputType]
    FILE_INPUT_TYPE_UNSPECIFIED: FileInput.FileInputType
    UPLOAD: FileInput.FileInputType
    FETCH: FileInput.FileInputType
    GOOGLE_SHEETS: FileInput.FileInputType

    class FetchSettings(_message.Message):
        __slots__ = ('enabled', 'day_of_month', 'time_of_day', 'day_of_week', 'time_zone', 'frequency', 'fetch_uri', 'username', 'password')

        class Frequency(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
            __slots__ = ()
            FREQUENCY_UNSPECIFIED: _ClassVar[FileInput.FetchSettings.Frequency]
            FREQUENCY_DAILY: _ClassVar[FileInput.FetchSettings.Frequency]
            FREQUENCY_WEEKLY: _ClassVar[FileInput.FetchSettings.Frequency]
            FREQUENCY_MONTHLY: _ClassVar[FileInput.FetchSettings.Frequency]
        FREQUENCY_UNSPECIFIED: FileInput.FetchSettings.Frequency
        FREQUENCY_DAILY: FileInput.FetchSettings.Frequency
        FREQUENCY_WEEKLY: FileInput.FetchSettings.Frequency
        FREQUENCY_MONTHLY: FileInput.FetchSettings.Frequency
        ENABLED_FIELD_NUMBER: _ClassVar[int]
        DAY_OF_MONTH_FIELD_NUMBER: _ClassVar[int]
        TIME_OF_DAY_FIELD_NUMBER: _ClassVar[int]
        DAY_OF_WEEK_FIELD_NUMBER: _ClassVar[int]
        TIME_ZONE_FIELD_NUMBER: _ClassVar[int]
        FREQUENCY_FIELD_NUMBER: _ClassVar[int]
        FETCH_URI_FIELD_NUMBER: _ClassVar[int]
        USERNAME_FIELD_NUMBER: _ClassVar[int]
        PASSWORD_FIELD_NUMBER: _ClassVar[int]
        enabled: bool
        day_of_month: int
        time_of_day: _timeofday_pb2.TimeOfDay
        day_of_week: _dayofweek_pb2.DayOfWeek
        time_zone: str
        frequency: FileInput.FetchSettings.Frequency
        fetch_uri: str
        username: str
        password: str

        def __init__(self, enabled: bool=..., day_of_month: _Optional[int]=..., time_of_day: _Optional[_Union[_timeofday_pb2.TimeOfDay, _Mapping]]=..., day_of_week: _Optional[_Union[_dayofweek_pb2.DayOfWeek, str]]=..., time_zone: _Optional[str]=..., frequency: _Optional[_Union[FileInput.FetchSettings.Frequency, str]]=..., fetch_uri: _Optional[str]=..., username: _Optional[str]=..., password: _Optional[str]=...) -> None:
            ...
    FETCH_SETTINGS_FIELD_NUMBER: _ClassVar[int]
    FILE_NAME_FIELD_NUMBER: _ClassVar[int]
    FILE_INPUT_TYPE_FIELD_NUMBER: _ClassVar[int]
    fetch_settings: FileInput.FetchSettings
    file_name: str
    file_input_type: FileInput.FileInputType

    def __init__(self, fetch_settings: _Optional[_Union[FileInput.FetchSettings, _Mapping]]=..., file_name: _Optional[str]=..., file_input_type: _Optional[_Union[FileInput.FileInputType, str]]=...) -> None:
        ...