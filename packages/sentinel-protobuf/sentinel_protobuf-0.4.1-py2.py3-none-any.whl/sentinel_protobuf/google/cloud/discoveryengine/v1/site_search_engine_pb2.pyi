from google.api import field_behavior_pb2 as _field_behavior_pb2
from google.api import resource_pb2 as _resource_pb2
from google.protobuf import timestamp_pb2 as _timestamp_pb2
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Mapping as _Mapping, Optional as _Optional, Union as _Union
DESCRIPTOR: _descriptor.FileDescriptor

class SiteSearchEngine(_message.Message):
    __slots__ = ('name',)
    NAME_FIELD_NUMBER: _ClassVar[int]
    name: str

    def __init__(self, name: _Optional[str]=...) -> None:
        ...

class TargetSite(_message.Message):
    __slots__ = ('name', 'provided_uri_pattern', 'type', 'exact_match', 'generated_uri_pattern', 'root_domain_uri', 'site_verification_info', 'indexing_status', 'update_time', 'failure_reason')

    class Type(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        TYPE_UNSPECIFIED: _ClassVar[TargetSite.Type]
        INCLUDE: _ClassVar[TargetSite.Type]
        EXCLUDE: _ClassVar[TargetSite.Type]
    TYPE_UNSPECIFIED: TargetSite.Type
    INCLUDE: TargetSite.Type
    EXCLUDE: TargetSite.Type

    class IndexingStatus(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        INDEXING_STATUS_UNSPECIFIED: _ClassVar[TargetSite.IndexingStatus]
        PENDING: _ClassVar[TargetSite.IndexingStatus]
        FAILED: _ClassVar[TargetSite.IndexingStatus]
        SUCCEEDED: _ClassVar[TargetSite.IndexingStatus]
        DELETING: _ClassVar[TargetSite.IndexingStatus]
    INDEXING_STATUS_UNSPECIFIED: TargetSite.IndexingStatus
    PENDING: TargetSite.IndexingStatus
    FAILED: TargetSite.IndexingStatus
    SUCCEEDED: TargetSite.IndexingStatus
    DELETING: TargetSite.IndexingStatus

    class FailureReason(_message.Message):
        __slots__ = ('quota_failure',)

        class QuotaFailure(_message.Message):
            __slots__ = ('total_required_quota',)
            TOTAL_REQUIRED_QUOTA_FIELD_NUMBER: _ClassVar[int]
            total_required_quota: int

            def __init__(self, total_required_quota: _Optional[int]=...) -> None:
                ...
        QUOTA_FAILURE_FIELD_NUMBER: _ClassVar[int]
        quota_failure: TargetSite.FailureReason.QuotaFailure

        def __init__(self, quota_failure: _Optional[_Union[TargetSite.FailureReason.QuotaFailure, _Mapping]]=...) -> None:
            ...
    NAME_FIELD_NUMBER: _ClassVar[int]
    PROVIDED_URI_PATTERN_FIELD_NUMBER: _ClassVar[int]
    TYPE_FIELD_NUMBER: _ClassVar[int]
    EXACT_MATCH_FIELD_NUMBER: _ClassVar[int]
    GENERATED_URI_PATTERN_FIELD_NUMBER: _ClassVar[int]
    ROOT_DOMAIN_URI_FIELD_NUMBER: _ClassVar[int]
    SITE_VERIFICATION_INFO_FIELD_NUMBER: _ClassVar[int]
    INDEXING_STATUS_FIELD_NUMBER: _ClassVar[int]
    UPDATE_TIME_FIELD_NUMBER: _ClassVar[int]
    FAILURE_REASON_FIELD_NUMBER: _ClassVar[int]
    name: str
    provided_uri_pattern: str
    type: TargetSite.Type
    exact_match: bool
    generated_uri_pattern: str
    root_domain_uri: str
    site_verification_info: SiteVerificationInfo
    indexing_status: TargetSite.IndexingStatus
    update_time: _timestamp_pb2.Timestamp
    failure_reason: TargetSite.FailureReason

    def __init__(self, name: _Optional[str]=..., provided_uri_pattern: _Optional[str]=..., type: _Optional[_Union[TargetSite.Type, str]]=..., exact_match: bool=..., generated_uri_pattern: _Optional[str]=..., root_domain_uri: _Optional[str]=..., site_verification_info: _Optional[_Union[SiteVerificationInfo, _Mapping]]=..., indexing_status: _Optional[_Union[TargetSite.IndexingStatus, str]]=..., update_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]]=..., failure_reason: _Optional[_Union[TargetSite.FailureReason, _Mapping]]=...) -> None:
        ...

class SiteVerificationInfo(_message.Message):
    __slots__ = ('site_verification_state', 'verify_time')

    class SiteVerificationState(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        SITE_VERIFICATION_STATE_UNSPECIFIED: _ClassVar[SiteVerificationInfo.SiteVerificationState]
        VERIFIED: _ClassVar[SiteVerificationInfo.SiteVerificationState]
        UNVERIFIED: _ClassVar[SiteVerificationInfo.SiteVerificationState]
        EXEMPTED: _ClassVar[SiteVerificationInfo.SiteVerificationState]
    SITE_VERIFICATION_STATE_UNSPECIFIED: SiteVerificationInfo.SiteVerificationState
    VERIFIED: SiteVerificationInfo.SiteVerificationState
    UNVERIFIED: SiteVerificationInfo.SiteVerificationState
    EXEMPTED: SiteVerificationInfo.SiteVerificationState
    SITE_VERIFICATION_STATE_FIELD_NUMBER: _ClassVar[int]
    VERIFY_TIME_FIELD_NUMBER: _ClassVar[int]
    site_verification_state: SiteVerificationInfo.SiteVerificationState
    verify_time: _timestamp_pb2.Timestamp

    def __init__(self, site_verification_state: _Optional[_Union[SiteVerificationInfo.SiteVerificationState, str]]=..., verify_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]]=...) -> None:
        ...