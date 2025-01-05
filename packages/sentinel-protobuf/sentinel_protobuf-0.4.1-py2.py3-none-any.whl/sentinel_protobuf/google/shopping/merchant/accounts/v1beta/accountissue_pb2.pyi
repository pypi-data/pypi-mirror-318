from google.api import annotations_pb2 as _annotations_pb2
from google.api import client_pb2 as _client_pb2
from google.api import field_behavior_pb2 as _field_behavior_pb2
from google.api import resource_pb2 as _resource_pb2
from google.shopping.type import types_pb2 as _types_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class AccountIssue(_message.Message):
    __slots__ = ("name", "title", "severity", "impacted_destinations", "detail", "documentation_uri")
    class Severity(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        SEVERITY_UNSPECIFIED: _ClassVar[AccountIssue.Severity]
        CRITICAL: _ClassVar[AccountIssue.Severity]
        ERROR: _ClassVar[AccountIssue.Severity]
        SUGGESTION: _ClassVar[AccountIssue.Severity]
    SEVERITY_UNSPECIFIED: AccountIssue.Severity
    CRITICAL: AccountIssue.Severity
    ERROR: AccountIssue.Severity
    SUGGESTION: AccountIssue.Severity
    class ImpactedDestination(_message.Message):
        __slots__ = ("reporting_context", "impacts")
        class Impact(_message.Message):
            __slots__ = ("region_code", "severity")
            REGION_CODE_FIELD_NUMBER: _ClassVar[int]
            SEVERITY_FIELD_NUMBER: _ClassVar[int]
            region_code: str
            severity: AccountIssue.Severity
            def __init__(self, region_code: _Optional[str] = ..., severity: _Optional[_Union[AccountIssue.Severity, str]] = ...) -> None: ...
        REPORTING_CONTEXT_FIELD_NUMBER: _ClassVar[int]
        IMPACTS_FIELD_NUMBER: _ClassVar[int]
        reporting_context: _types_pb2.ReportingContext.ReportingContextEnum
        impacts: _containers.RepeatedCompositeFieldContainer[AccountIssue.ImpactedDestination.Impact]
        def __init__(self, reporting_context: _Optional[_Union[_types_pb2.ReportingContext.ReportingContextEnum, str]] = ..., impacts: _Optional[_Iterable[_Union[AccountIssue.ImpactedDestination.Impact, _Mapping]]] = ...) -> None: ...
    NAME_FIELD_NUMBER: _ClassVar[int]
    TITLE_FIELD_NUMBER: _ClassVar[int]
    SEVERITY_FIELD_NUMBER: _ClassVar[int]
    IMPACTED_DESTINATIONS_FIELD_NUMBER: _ClassVar[int]
    DETAIL_FIELD_NUMBER: _ClassVar[int]
    DOCUMENTATION_URI_FIELD_NUMBER: _ClassVar[int]
    name: str
    title: str
    severity: AccountIssue.Severity
    impacted_destinations: _containers.RepeatedCompositeFieldContainer[AccountIssue.ImpactedDestination]
    detail: str
    documentation_uri: str
    def __init__(self, name: _Optional[str] = ..., title: _Optional[str] = ..., severity: _Optional[_Union[AccountIssue.Severity, str]] = ..., impacted_destinations: _Optional[_Iterable[_Union[AccountIssue.ImpactedDestination, _Mapping]]] = ..., detail: _Optional[str] = ..., documentation_uri: _Optional[str] = ...) -> None: ...

class ListAccountIssuesRequest(_message.Message):
    __slots__ = ("parent", "page_size", "page_token", "language_code", "time_zone")
    PARENT_FIELD_NUMBER: _ClassVar[int]
    PAGE_SIZE_FIELD_NUMBER: _ClassVar[int]
    PAGE_TOKEN_FIELD_NUMBER: _ClassVar[int]
    LANGUAGE_CODE_FIELD_NUMBER: _ClassVar[int]
    TIME_ZONE_FIELD_NUMBER: _ClassVar[int]
    parent: str
    page_size: int
    page_token: str
    language_code: str
    time_zone: str
    def __init__(self, parent: _Optional[str] = ..., page_size: _Optional[int] = ..., page_token: _Optional[str] = ..., language_code: _Optional[str] = ..., time_zone: _Optional[str] = ...) -> None: ...

class ListAccountIssuesResponse(_message.Message):
    __slots__ = ("account_issues", "next_page_token")
    ACCOUNT_ISSUES_FIELD_NUMBER: _ClassVar[int]
    NEXT_PAGE_TOKEN_FIELD_NUMBER: _ClassVar[int]
    account_issues: _containers.RepeatedCompositeFieldContainer[AccountIssue]
    next_page_token: str
    def __init__(self, account_issues: _Optional[_Iterable[_Union[AccountIssue, _Mapping]]] = ..., next_page_token: _Optional[str] = ...) -> None: ...
