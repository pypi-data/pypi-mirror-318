from google.ads.googleads.v17.enums import identity_verification_program_pb2 as _identity_verification_program_pb2
from google.ads.googleads.v17.enums import identity_verification_program_status_pb2 as _identity_verification_program_status_pb2
from google.api import annotations_pb2 as _annotations_pb2
from google.api import client_pb2 as _client_pb2
from google.api import field_behavior_pb2 as _field_behavior_pb2
from google.protobuf import empty_pb2 as _empty_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class StartIdentityVerificationRequest(_message.Message):
    __slots__ = ("customer_id", "verification_program")
    CUSTOMER_ID_FIELD_NUMBER: _ClassVar[int]
    VERIFICATION_PROGRAM_FIELD_NUMBER: _ClassVar[int]
    customer_id: str
    verification_program: _identity_verification_program_pb2.IdentityVerificationProgramEnum.IdentityVerificationProgram
    def __init__(self, customer_id: _Optional[str] = ..., verification_program: _Optional[_Union[_identity_verification_program_pb2.IdentityVerificationProgramEnum.IdentityVerificationProgram, str]] = ...) -> None: ...

class GetIdentityVerificationRequest(_message.Message):
    __slots__ = ("customer_id",)
    CUSTOMER_ID_FIELD_NUMBER: _ClassVar[int]
    customer_id: str
    def __init__(self, customer_id: _Optional[str] = ...) -> None: ...

class GetIdentityVerificationResponse(_message.Message):
    __slots__ = ("identity_verification",)
    IDENTITY_VERIFICATION_FIELD_NUMBER: _ClassVar[int]
    identity_verification: _containers.RepeatedCompositeFieldContainer[IdentityVerification]
    def __init__(self, identity_verification: _Optional[_Iterable[_Union[IdentityVerification, _Mapping]]] = ...) -> None: ...

class IdentityVerification(_message.Message):
    __slots__ = ("verification_program", "identity_verification_requirement", "verification_progress")
    VERIFICATION_PROGRAM_FIELD_NUMBER: _ClassVar[int]
    IDENTITY_VERIFICATION_REQUIREMENT_FIELD_NUMBER: _ClassVar[int]
    VERIFICATION_PROGRESS_FIELD_NUMBER: _ClassVar[int]
    verification_program: _identity_verification_program_pb2.IdentityVerificationProgramEnum.IdentityVerificationProgram
    identity_verification_requirement: IdentityVerificationRequirement
    verification_progress: IdentityVerificationProgress
    def __init__(self, verification_program: _Optional[_Union[_identity_verification_program_pb2.IdentityVerificationProgramEnum.IdentityVerificationProgram, str]] = ..., identity_verification_requirement: _Optional[_Union[IdentityVerificationRequirement, _Mapping]] = ..., verification_progress: _Optional[_Union[IdentityVerificationProgress, _Mapping]] = ...) -> None: ...

class IdentityVerificationProgress(_message.Message):
    __slots__ = ("program_status", "invitation_link_expiration_time", "action_url")
    PROGRAM_STATUS_FIELD_NUMBER: _ClassVar[int]
    INVITATION_LINK_EXPIRATION_TIME_FIELD_NUMBER: _ClassVar[int]
    ACTION_URL_FIELD_NUMBER: _ClassVar[int]
    program_status: _identity_verification_program_status_pb2.IdentityVerificationProgramStatusEnum.IdentityVerificationProgramStatus
    invitation_link_expiration_time: str
    action_url: str
    def __init__(self, program_status: _Optional[_Union[_identity_verification_program_status_pb2.IdentityVerificationProgramStatusEnum.IdentityVerificationProgramStatus, str]] = ..., invitation_link_expiration_time: _Optional[str] = ..., action_url: _Optional[str] = ...) -> None: ...

class IdentityVerificationRequirement(_message.Message):
    __slots__ = ("verification_start_deadline_time", "verification_completion_deadline_time")
    VERIFICATION_START_DEADLINE_TIME_FIELD_NUMBER: _ClassVar[int]
    VERIFICATION_COMPLETION_DEADLINE_TIME_FIELD_NUMBER: _ClassVar[int]
    verification_start_deadline_time: str
    verification_completion_deadline_time: str
    def __init__(self, verification_start_deadline_time: _Optional[str] = ..., verification_completion_deadline_time: _Optional[str] = ...) -> None: ...
