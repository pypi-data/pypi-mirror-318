from google.api import field_behavior_pb2 as _field_behavior_pb2
from google.protobuf import duration_pb2 as _duration_pb2
from google.protobuf import timestamp_pb2 as _timestamp_pb2
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Mapping as _Mapping, Optional as _Optional, Union as _Union
DESCRIPTOR: _descriptor.FileDescriptor

class Language(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    LANGUAGE_UNSPECIFIED: _ClassVar[Language]
    NONE: _ClassVar[Language]
    ANDROID: _ClassVar[Language]
    AS: _ClassVar[Language]
    CC: _ClassVar[Language]
    CSS: _ClassVar[Language]
    DART: _ClassVar[Language]
    GO: _ClassVar[Language]
    GWT: _ClassVar[Language]
    HASKELL: _ClassVar[Language]
    JAVA: _ClassVar[Language]
    JS: _ClassVar[Language]
    LISP: _ClassVar[Language]
    OBJC: _ClassVar[Language]
    PY: _ClassVar[Language]
    SH: _ClassVar[Language]
    SWIFT: _ClassVar[Language]
    TS: _ClassVar[Language]
    WEB: _ClassVar[Language]
    SCALA: _ClassVar[Language]
    PROTO: _ClassVar[Language]
    XML: _ClassVar[Language]

class Status(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    STATUS_UNSPECIFIED: _ClassVar[Status]
    BUILDING: _ClassVar[Status]
    BUILT: _ClassVar[Status]
    FAILED_TO_BUILD: _ClassVar[Status]
    TESTING: _ClassVar[Status]
    PASSED: _ClassVar[Status]
    FAILED: _ClassVar[Status]
    TIMED_OUT: _ClassVar[Status]
    CANCELLED: _ClassVar[Status]
    TOOL_FAILED: _ClassVar[Status]
    INCOMPLETE: _ClassVar[Status]
    FLAKY: _ClassVar[Status]
    UNKNOWN: _ClassVar[Status]
    SKIPPED: _ClassVar[Status]

class UploadStatus(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    UPLOAD_STATUS_UNSPECIFIED: _ClassVar[UploadStatus]
    UPLOADING: _ClassVar[UploadStatus]
    POST_PROCESSING: _ClassVar[UploadStatus]
    IMMUTABLE: _ClassVar[UploadStatus]
LANGUAGE_UNSPECIFIED: Language
NONE: Language
ANDROID: Language
AS: Language
CC: Language
CSS: Language
DART: Language
GO: Language
GWT: Language
HASKELL: Language
JAVA: Language
JS: Language
LISP: Language
OBJC: Language
PY: Language
SH: Language
SWIFT: Language
TS: Language
WEB: Language
SCALA: Language
PROTO: Language
XML: Language
STATUS_UNSPECIFIED: Status
BUILDING: Status
BUILT: Status
FAILED_TO_BUILD: Status
TESTING: Status
PASSED: Status
FAILED: Status
TIMED_OUT: Status
CANCELLED: Status
TOOL_FAILED: Status
INCOMPLETE: Status
FLAKY: Status
UNKNOWN: Status
SKIPPED: Status
UPLOAD_STATUS_UNSPECIFIED: UploadStatus
UPLOADING: UploadStatus
POST_PROCESSING: UploadStatus
IMMUTABLE: UploadStatus

class StatusAttributes(_message.Message):
    __slots__ = ('status', 'description')
    STATUS_FIELD_NUMBER: _ClassVar[int]
    DESCRIPTION_FIELD_NUMBER: _ClassVar[int]
    status: Status
    description: str

    def __init__(self, status: _Optional[_Union[Status, str]]=..., description: _Optional[str]=...) -> None:
        ...

class Property(_message.Message):
    __slots__ = ('key', 'value')
    KEY_FIELD_NUMBER: _ClassVar[int]
    VALUE_FIELD_NUMBER: _ClassVar[int]
    key: str
    value: str

    def __init__(self, key: _Optional[str]=..., value: _Optional[str]=...) -> None:
        ...

class Timing(_message.Message):
    __slots__ = ('start_time', 'duration')
    START_TIME_FIELD_NUMBER: _ClassVar[int]
    DURATION_FIELD_NUMBER: _ClassVar[int]
    start_time: _timestamp_pb2.Timestamp
    duration: _duration_pb2.Duration

    def __init__(self, start_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]]=..., duration: _Optional[_Union[_duration_pb2.Duration, _Mapping]]=...) -> None:
        ...

class Dependency(_message.Message):
    __slots__ = ('target', 'configured_target', 'action', 'id', 'label')

    class Id(_message.Message):
        __slots__ = ('target_id', 'configuration_id', 'action_id')
        TARGET_ID_FIELD_NUMBER: _ClassVar[int]
        CONFIGURATION_ID_FIELD_NUMBER: _ClassVar[int]
        ACTION_ID_FIELD_NUMBER: _ClassVar[int]
        target_id: str
        configuration_id: str
        action_id: str

        def __init__(self, target_id: _Optional[str]=..., configuration_id: _Optional[str]=..., action_id: _Optional[str]=...) -> None:
            ...
    TARGET_FIELD_NUMBER: _ClassVar[int]
    CONFIGURED_TARGET_FIELD_NUMBER: _ClassVar[int]
    ACTION_FIELD_NUMBER: _ClassVar[int]
    ID_FIELD_NUMBER: _ClassVar[int]
    LABEL_FIELD_NUMBER: _ClassVar[int]
    target: str
    configured_target: str
    action: str
    id: Dependency.Id
    label: str

    def __init__(self, target: _Optional[str]=..., configured_target: _Optional[str]=..., action: _Optional[str]=..., id: _Optional[_Union[Dependency.Id, _Mapping]]=..., label: _Optional[str]=...) -> None:
        ...