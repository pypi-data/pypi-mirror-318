from google.api import annotations_pb2 as _annotations_pb2
from google.api import client_pb2 as _client_pb2
from google.api import field_behavior_pb2 as _field_behavior_pb2
from google.api import resource_pb2 as _resource_pb2
from google.longrunning import operations_pb2 as _operations_pb2
from google.protobuf import timestamp_pb2 as _timestamp_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union
DESCRIPTOR: _descriptor.FileDescriptor

class ThreatType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    THREAT_TYPE_UNSPECIFIED: _ClassVar[ThreatType]
    MALWARE: _ClassVar[ThreatType]
    SOCIAL_ENGINEERING: _ClassVar[ThreatType]
    UNWANTED_SOFTWARE: _ClassVar[ThreatType]
    SOCIAL_ENGINEERING_EXTENDED_COVERAGE: _ClassVar[ThreatType]

class CompressionType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    COMPRESSION_TYPE_UNSPECIFIED: _ClassVar[CompressionType]
    RAW: _ClassVar[CompressionType]
    RICE: _ClassVar[CompressionType]
THREAT_TYPE_UNSPECIFIED: ThreatType
MALWARE: ThreatType
SOCIAL_ENGINEERING: ThreatType
UNWANTED_SOFTWARE: ThreatType
SOCIAL_ENGINEERING_EXTENDED_COVERAGE: ThreatType
COMPRESSION_TYPE_UNSPECIFIED: CompressionType
RAW: CompressionType
RICE: CompressionType

class ComputeThreatListDiffRequest(_message.Message):
    __slots__ = ('threat_type', 'version_token', 'constraints')

    class Constraints(_message.Message):
        __slots__ = ('max_diff_entries', 'max_database_entries', 'supported_compressions')
        MAX_DIFF_ENTRIES_FIELD_NUMBER: _ClassVar[int]
        MAX_DATABASE_ENTRIES_FIELD_NUMBER: _ClassVar[int]
        SUPPORTED_COMPRESSIONS_FIELD_NUMBER: _ClassVar[int]
        max_diff_entries: int
        max_database_entries: int
        supported_compressions: _containers.RepeatedScalarFieldContainer[CompressionType]

        def __init__(self, max_diff_entries: _Optional[int]=..., max_database_entries: _Optional[int]=..., supported_compressions: _Optional[_Iterable[_Union[CompressionType, str]]]=...) -> None:
            ...
    THREAT_TYPE_FIELD_NUMBER: _ClassVar[int]
    VERSION_TOKEN_FIELD_NUMBER: _ClassVar[int]
    CONSTRAINTS_FIELD_NUMBER: _ClassVar[int]
    threat_type: ThreatType
    version_token: bytes
    constraints: ComputeThreatListDiffRequest.Constraints

    def __init__(self, threat_type: _Optional[_Union[ThreatType, str]]=..., version_token: _Optional[bytes]=..., constraints: _Optional[_Union[ComputeThreatListDiffRequest.Constraints, _Mapping]]=...) -> None:
        ...

class ComputeThreatListDiffResponse(_message.Message):
    __slots__ = ('response_type', 'additions', 'removals', 'new_version_token', 'checksum', 'recommended_next_diff')

    class ResponseType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        RESPONSE_TYPE_UNSPECIFIED: _ClassVar[ComputeThreatListDiffResponse.ResponseType]
        DIFF: _ClassVar[ComputeThreatListDiffResponse.ResponseType]
        RESET: _ClassVar[ComputeThreatListDiffResponse.ResponseType]
    RESPONSE_TYPE_UNSPECIFIED: ComputeThreatListDiffResponse.ResponseType
    DIFF: ComputeThreatListDiffResponse.ResponseType
    RESET: ComputeThreatListDiffResponse.ResponseType

    class Checksum(_message.Message):
        __slots__ = ('sha256',)
        SHA256_FIELD_NUMBER: _ClassVar[int]
        sha256: bytes

        def __init__(self, sha256: _Optional[bytes]=...) -> None:
            ...
    RESPONSE_TYPE_FIELD_NUMBER: _ClassVar[int]
    ADDITIONS_FIELD_NUMBER: _ClassVar[int]
    REMOVALS_FIELD_NUMBER: _ClassVar[int]
    NEW_VERSION_TOKEN_FIELD_NUMBER: _ClassVar[int]
    CHECKSUM_FIELD_NUMBER: _ClassVar[int]
    RECOMMENDED_NEXT_DIFF_FIELD_NUMBER: _ClassVar[int]
    response_type: ComputeThreatListDiffResponse.ResponseType
    additions: ThreatEntryAdditions
    removals: ThreatEntryRemovals
    new_version_token: bytes
    checksum: ComputeThreatListDiffResponse.Checksum
    recommended_next_diff: _timestamp_pb2.Timestamp

    def __init__(self, response_type: _Optional[_Union[ComputeThreatListDiffResponse.ResponseType, str]]=..., additions: _Optional[_Union[ThreatEntryAdditions, _Mapping]]=..., removals: _Optional[_Union[ThreatEntryRemovals, _Mapping]]=..., new_version_token: _Optional[bytes]=..., checksum: _Optional[_Union[ComputeThreatListDiffResponse.Checksum, _Mapping]]=..., recommended_next_diff: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]]=...) -> None:
        ...

class SearchUrisRequest(_message.Message):
    __slots__ = ('uri', 'threat_types')
    URI_FIELD_NUMBER: _ClassVar[int]
    THREAT_TYPES_FIELD_NUMBER: _ClassVar[int]
    uri: str
    threat_types: _containers.RepeatedScalarFieldContainer[ThreatType]

    def __init__(self, uri: _Optional[str]=..., threat_types: _Optional[_Iterable[_Union[ThreatType, str]]]=...) -> None:
        ...

class SearchUrisResponse(_message.Message):
    __slots__ = ('threat',)

    class ThreatUri(_message.Message):
        __slots__ = ('threat_types', 'expire_time')
        THREAT_TYPES_FIELD_NUMBER: _ClassVar[int]
        EXPIRE_TIME_FIELD_NUMBER: _ClassVar[int]
        threat_types: _containers.RepeatedScalarFieldContainer[ThreatType]
        expire_time: _timestamp_pb2.Timestamp

        def __init__(self, threat_types: _Optional[_Iterable[_Union[ThreatType, str]]]=..., expire_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]]=...) -> None:
            ...
    THREAT_FIELD_NUMBER: _ClassVar[int]
    threat: SearchUrisResponse.ThreatUri

    def __init__(self, threat: _Optional[_Union[SearchUrisResponse.ThreatUri, _Mapping]]=...) -> None:
        ...

class SearchHashesRequest(_message.Message):
    __slots__ = ('hash_prefix', 'threat_types')
    HASH_PREFIX_FIELD_NUMBER: _ClassVar[int]
    THREAT_TYPES_FIELD_NUMBER: _ClassVar[int]
    hash_prefix: bytes
    threat_types: _containers.RepeatedScalarFieldContainer[ThreatType]

    def __init__(self, hash_prefix: _Optional[bytes]=..., threat_types: _Optional[_Iterable[_Union[ThreatType, str]]]=...) -> None:
        ...

class SearchHashesResponse(_message.Message):
    __slots__ = ('threats', 'negative_expire_time')

    class ThreatHash(_message.Message):
        __slots__ = ('threat_types', 'hash', 'expire_time')
        THREAT_TYPES_FIELD_NUMBER: _ClassVar[int]
        HASH_FIELD_NUMBER: _ClassVar[int]
        EXPIRE_TIME_FIELD_NUMBER: _ClassVar[int]
        threat_types: _containers.RepeatedScalarFieldContainer[ThreatType]
        hash: bytes
        expire_time: _timestamp_pb2.Timestamp

        def __init__(self, threat_types: _Optional[_Iterable[_Union[ThreatType, str]]]=..., hash: _Optional[bytes]=..., expire_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]]=...) -> None:
            ...
    THREATS_FIELD_NUMBER: _ClassVar[int]
    NEGATIVE_EXPIRE_TIME_FIELD_NUMBER: _ClassVar[int]
    threats: _containers.RepeatedCompositeFieldContainer[SearchHashesResponse.ThreatHash]
    negative_expire_time: _timestamp_pb2.Timestamp

    def __init__(self, threats: _Optional[_Iterable[_Union[SearchHashesResponse.ThreatHash, _Mapping]]]=..., negative_expire_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]]=...) -> None:
        ...

class ThreatEntryAdditions(_message.Message):
    __slots__ = ('raw_hashes', 'rice_hashes')
    RAW_HASHES_FIELD_NUMBER: _ClassVar[int]
    RICE_HASHES_FIELD_NUMBER: _ClassVar[int]
    raw_hashes: _containers.RepeatedCompositeFieldContainer[RawHashes]
    rice_hashes: RiceDeltaEncoding

    def __init__(self, raw_hashes: _Optional[_Iterable[_Union[RawHashes, _Mapping]]]=..., rice_hashes: _Optional[_Union[RiceDeltaEncoding, _Mapping]]=...) -> None:
        ...

class ThreatEntryRemovals(_message.Message):
    __slots__ = ('raw_indices', 'rice_indices')
    RAW_INDICES_FIELD_NUMBER: _ClassVar[int]
    RICE_INDICES_FIELD_NUMBER: _ClassVar[int]
    raw_indices: RawIndices
    rice_indices: RiceDeltaEncoding

    def __init__(self, raw_indices: _Optional[_Union[RawIndices, _Mapping]]=..., rice_indices: _Optional[_Union[RiceDeltaEncoding, _Mapping]]=...) -> None:
        ...

class RawIndices(_message.Message):
    __slots__ = ('indices',)
    INDICES_FIELD_NUMBER: _ClassVar[int]
    indices: _containers.RepeatedScalarFieldContainer[int]

    def __init__(self, indices: _Optional[_Iterable[int]]=...) -> None:
        ...

class RawHashes(_message.Message):
    __slots__ = ('prefix_size', 'raw_hashes')
    PREFIX_SIZE_FIELD_NUMBER: _ClassVar[int]
    RAW_HASHES_FIELD_NUMBER: _ClassVar[int]
    prefix_size: int
    raw_hashes: bytes

    def __init__(self, prefix_size: _Optional[int]=..., raw_hashes: _Optional[bytes]=...) -> None:
        ...

class RiceDeltaEncoding(_message.Message):
    __slots__ = ('first_value', 'rice_parameter', 'entry_count', 'encoded_data')
    FIRST_VALUE_FIELD_NUMBER: _ClassVar[int]
    RICE_PARAMETER_FIELD_NUMBER: _ClassVar[int]
    ENTRY_COUNT_FIELD_NUMBER: _ClassVar[int]
    ENCODED_DATA_FIELD_NUMBER: _ClassVar[int]
    first_value: int
    rice_parameter: int
    entry_count: int
    encoded_data: bytes

    def __init__(self, first_value: _Optional[int]=..., rice_parameter: _Optional[int]=..., entry_count: _Optional[int]=..., encoded_data: _Optional[bytes]=...) -> None:
        ...

class Submission(_message.Message):
    __slots__ = ('uri', 'threat_types')
    URI_FIELD_NUMBER: _ClassVar[int]
    THREAT_TYPES_FIELD_NUMBER: _ClassVar[int]
    uri: str
    threat_types: _containers.RepeatedScalarFieldContainer[ThreatType]

    def __init__(self, uri: _Optional[str]=..., threat_types: _Optional[_Iterable[_Union[ThreatType, str]]]=...) -> None:
        ...

class ThreatInfo(_message.Message):
    __slots__ = ('abuse_type', 'threat_confidence', 'threat_justification')

    class AbuseType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        ABUSE_TYPE_UNSPECIFIED: _ClassVar[ThreatInfo.AbuseType]
        MALWARE: _ClassVar[ThreatInfo.AbuseType]
        SOCIAL_ENGINEERING: _ClassVar[ThreatInfo.AbuseType]
        UNWANTED_SOFTWARE: _ClassVar[ThreatInfo.AbuseType]
    ABUSE_TYPE_UNSPECIFIED: ThreatInfo.AbuseType
    MALWARE: ThreatInfo.AbuseType
    SOCIAL_ENGINEERING: ThreatInfo.AbuseType
    UNWANTED_SOFTWARE: ThreatInfo.AbuseType

    class Confidence(_message.Message):
        __slots__ = ('score', 'level')

        class ConfidenceLevel(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
            __slots__ = ()
            CONFIDENCE_LEVEL_UNSPECIFIED: _ClassVar[ThreatInfo.Confidence.ConfidenceLevel]
            LOW: _ClassVar[ThreatInfo.Confidence.ConfidenceLevel]
            MEDIUM: _ClassVar[ThreatInfo.Confidence.ConfidenceLevel]
            HIGH: _ClassVar[ThreatInfo.Confidence.ConfidenceLevel]
        CONFIDENCE_LEVEL_UNSPECIFIED: ThreatInfo.Confidence.ConfidenceLevel
        LOW: ThreatInfo.Confidence.ConfidenceLevel
        MEDIUM: ThreatInfo.Confidence.ConfidenceLevel
        HIGH: ThreatInfo.Confidence.ConfidenceLevel
        SCORE_FIELD_NUMBER: _ClassVar[int]
        LEVEL_FIELD_NUMBER: _ClassVar[int]
        score: float
        level: ThreatInfo.Confidence.ConfidenceLevel

        def __init__(self, score: _Optional[float]=..., level: _Optional[_Union[ThreatInfo.Confidence.ConfidenceLevel, str]]=...) -> None:
            ...

    class ThreatJustification(_message.Message):
        __slots__ = ('labels', 'comments')

        class JustificationLabel(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
            __slots__ = ()
            JUSTIFICATION_LABEL_UNSPECIFIED: _ClassVar[ThreatInfo.ThreatJustification.JustificationLabel]
            MANUAL_VERIFICATION: _ClassVar[ThreatInfo.ThreatJustification.JustificationLabel]
            USER_REPORT: _ClassVar[ThreatInfo.ThreatJustification.JustificationLabel]
            AUTOMATED_REPORT: _ClassVar[ThreatInfo.ThreatJustification.JustificationLabel]
        JUSTIFICATION_LABEL_UNSPECIFIED: ThreatInfo.ThreatJustification.JustificationLabel
        MANUAL_VERIFICATION: ThreatInfo.ThreatJustification.JustificationLabel
        USER_REPORT: ThreatInfo.ThreatJustification.JustificationLabel
        AUTOMATED_REPORT: ThreatInfo.ThreatJustification.JustificationLabel
        LABELS_FIELD_NUMBER: _ClassVar[int]
        COMMENTS_FIELD_NUMBER: _ClassVar[int]
        labels: _containers.RepeatedScalarFieldContainer[ThreatInfo.ThreatJustification.JustificationLabel]
        comments: _containers.RepeatedScalarFieldContainer[str]

        def __init__(self, labels: _Optional[_Iterable[_Union[ThreatInfo.ThreatJustification.JustificationLabel, str]]]=..., comments: _Optional[_Iterable[str]]=...) -> None:
            ...
    ABUSE_TYPE_FIELD_NUMBER: _ClassVar[int]
    THREAT_CONFIDENCE_FIELD_NUMBER: _ClassVar[int]
    THREAT_JUSTIFICATION_FIELD_NUMBER: _ClassVar[int]
    abuse_type: ThreatInfo.AbuseType
    threat_confidence: ThreatInfo.Confidence
    threat_justification: ThreatInfo.ThreatJustification

    def __init__(self, abuse_type: _Optional[_Union[ThreatInfo.AbuseType, str]]=..., threat_confidence: _Optional[_Union[ThreatInfo.Confidence, _Mapping]]=..., threat_justification: _Optional[_Union[ThreatInfo.ThreatJustification, _Mapping]]=...) -> None:
        ...

class ThreatDiscovery(_message.Message):
    __slots__ = ('platform', 'region_codes')

    class Platform(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        PLATFORM_UNSPECIFIED: _ClassVar[ThreatDiscovery.Platform]
        ANDROID: _ClassVar[ThreatDiscovery.Platform]
        IOS: _ClassVar[ThreatDiscovery.Platform]
        MACOS: _ClassVar[ThreatDiscovery.Platform]
        WINDOWS: _ClassVar[ThreatDiscovery.Platform]
    PLATFORM_UNSPECIFIED: ThreatDiscovery.Platform
    ANDROID: ThreatDiscovery.Platform
    IOS: ThreatDiscovery.Platform
    MACOS: ThreatDiscovery.Platform
    WINDOWS: ThreatDiscovery.Platform
    PLATFORM_FIELD_NUMBER: _ClassVar[int]
    REGION_CODES_FIELD_NUMBER: _ClassVar[int]
    platform: ThreatDiscovery.Platform
    region_codes: _containers.RepeatedScalarFieldContainer[str]

    def __init__(self, platform: _Optional[_Union[ThreatDiscovery.Platform, str]]=..., region_codes: _Optional[_Iterable[str]]=...) -> None:
        ...

class CreateSubmissionRequest(_message.Message):
    __slots__ = ('parent', 'submission')
    PARENT_FIELD_NUMBER: _ClassVar[int]
    SUBMISSION_FIELD_NUMBER: _ClassVar[int]
    parent: str
    submission: Submission

    def __init__(self, parent: _Optional[str]=..., submission: _Optional[_Union[Submission, _Mapping]]=...) -> None:
        ...

class SubmitUriRequest(_message.Message):
    __slots__ = ('parent', 'submission', 'threat_info', 'threat_discovery')
    PARENT_FIELD_NUMBER: _ClassVar[int]
    SUBMISSION_FIELD_NUMBER: _ClassVar[int]
    THREAT_INFO_FIELD_NUMBER: _ClassVar[int]
    THREAT_DISCOVERY_FIELD_NUMBER: _ClassVar[int]
    parent: str
    submission: Submission
    threat_info: ThreatInfo
    threat_discovery: ThreatDiscovery

    def __init__(self, parent: _Optional[str]=..., submission: _Optional[_Union[Submission, _Mapping]]=..., threat_info: _Optional[_Union[ThreatInfo, _Mapping]]=..., threat_discovery: _Optional[_Union[ThreatDiscovery, _Mapping]]=...) -> None:
        ...

class SubmitUriMetadata(_message.Message):
    __slots__ = ('state', 'create_time', 'update_time')

    class State(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        STATE_UNSPECIFIED: _ClassVar[SubmitUriMetadata.State]
        RUNNING: _ClassVar[SubmitUriMetadata.State]
        SUCCEEDED: _ClassVar[SubmitUriMetadata.State]
        CANCELLED: _ClassVar[SubmitUriMetadata.State]
        FAILED: _ClassVar[SubmitUriMetadata.State]
        CLOSED: _ClassVar[SubmitUriMetadata.State]
    STATE_UNSPECIFIED: SubmitUriMetadata.State
    RUNNING: SubmitUriMetadata.State
    SUCCEEDED: SubmitUriMetadata.State
    CANCELLED: SubmitUriMetadata.State
    FAILED: SubmitUriMetadata.State
    CLOSED: SubmitUriMetadata.State
    STATE_FIELD_NUMBER: _ClassVar[int]
    CREATE_TIME_FIELD_NUMBER: _ClassVar[int]
    UPDATE_TIME_FIELD_NUMBER: _ClassVar[int]
    state: SubmitUriMetadata.State
    create_time: _timestamp_pb2.Timestamp
    update_time: _timestamp_pb2.Timestamp

    def __init__(self, state: _Optional[_Union[SubmitUriMetadata.State, str]]=..., create_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]]=..., update_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]]=...) -> None:
        ...