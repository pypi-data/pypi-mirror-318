from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union
DESCRIPTOR: _descriptor.FileDescriptor

class InvalidArgument(_message.Message):
    __slots__ = ('field_violations',)

    class FieldViolation(_message.Message):
        __slots__ = ('field', 'reason', 'display_message')

        class Reason(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
            __slots__ = ()
            REASON_UNSPECIFIED: _ClassVar[InvalidArgument.FieldViolation.Reason]
            FIELD_REQUIRED: _ClassVar[InvalidArgument.FieldViolation.Reason]
            INVALID_VALUE: _ClassVar[InvalidArgument.FieldViolation.Reason]
            VALUE_OUT_OF_RANGE: _ClassVar[InvalidArgument.FieldViolation.Reason]
            STRING_VALUE_TOO_LONG: _ClassVar[InvalidArgument.FieldViolation.Reason]
            MAX_ENTRIES_EXCEEDED: _ClassVar[InvalidArgument.FieldViolation.Reason]
            FIELD_NOT_FOUND: _ClassVar[InvalidArgument.FieldViolation.Reason]
            CHOICE_NOT_FOUND: _ClassVar[InvalidArgument.FieldViolation.Reason]
        REASON_UNSPECIFIED: InvalidArgument.FieldViolation.Reason
        FIELD_REQUIRED: InvalidArgument.FieldViolation.Reason
        INVALID_VALUE: InvalidArgument.FieldViolation.Reason
        VALUE_OUT_OF_RANGE: InvalidArgument.FieldViolation.Reason
        STRING_VALUE_TOO_LONG: InvalidArgument.FieldViolation.Reason
        MAX_ENTRIES_EXCEEDED: InvalidArgument.FieldViolation.Reason
        FIELD_NOT_FOUND: InvalidArgument.FieldViolation.Reason
        CHOICE_NOT_FOUND: InvalidArgument.FieldViolation.Reason
        FIELD_FIELD_NUMBER: _ClassVar[int]
        REASON_FIELD_NUMBER: _ClassVar[int]
        DISPLAY_MESSAGE_FIELD_NUMBER: _ClassVar[int]
        field: str
        reason: InvalidArgument.FieldViolation.Reason
        display_message: str

        def __init__(self, field: _Optional[str]=..., reason: _Optional[_Union[InvalidArgument.FieldViolation.Reason, str]]=..., display_message: _Optional[str]=...) -> None:
            ...
    FIELD_VIOLATIONS_FIELD_NUMBER: _ClassVar[int]
    field_violations: _containers.RepeatedCompositeFieldContainer[InvalidArgument.FieldViolation]

    def __init__(self, field_violations: _Optional[_Iterable[_Union[InvalidArgument.FieldViolation, _Mapping]]]=...) -> None:
        ...

class PreconditionFailure(_message.Message):
    __slots__ = ('violation',)

    class Violation(_message.Message):
        __slots__ = ('field', 'reason', 'display_message')

        class Reason(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
            __slots__ = ()
            REASON_UNSPECIFIED: _ClassVar[PreconditionFailure.Violation.Reason]
            CANNOT_DISABLE: _ClassVar[PreconditionFailure.Violation.Reason]
            CANNOT_ENABLE: _ClassVar[PreconditionFailure.Violation.Reason]
            CANNOT_PUBLISH: _ClassVar[PreconditionFailure.Violation.Reason]
            CANNOT_UNPUBLISH: _ClassVar[PreconditionFailure.Violation.Reason]
            CANNOT_DELETE: _ClassVar[PreconditionFailure.Violation.Reason]
            CANNOT_RESTRICT_RANGE: _ClassVar[PreconditionFailure.Violation.Reason]
            CANNOT_CHANGE_PUBLISHED_FIELD: _ClassVar[PreconditionFailure.Violation.Reason]
            CANNOT_CREATE_MORE_LABELS: _ClassVar[PreconditionFailure.Violation.Reason]
            CANNOT_CHANGE_PUBLISHED_FIELD_TYPE: _ClassVar[PreconditionFailure.Violation.Reason]
            CANNOT_MODIFY_LOCKED_COMPONENT: _ClassVar[PreconditionFailure.Violation.Reason]
            UNSUPPORT_ENABLED_APP_SETTINGS: _ClassVar[PreconditionFailure.Violation.Reason]
        REASON_UNSPECIFIED: PreconditionFailure.Violation.Reason
        CANNOT_DISABLE: PreconditionFailure.Violation.Reason
        CANNOT_ENABLE: PreconditionFailure.Violation.Reason
        CANNOT_PUBLISH: PreconditionFailure.Violation.Reason
        CANNOT_UNPUBLISH: PreconditionFailure.Violation.Reason
        CANNOT_DELETE: PreconditionFailure.Violation.Reason
        CANNOT_RESTRICT_RANGE: PreconditionFailure.Violation.Reason
        CANNOT_CHANGE_PUBLISHED_FIELD: PreconditionFailure.Violation.Reason
        CANNOT_CREATE_MORE_LABELS: PreconditionFailure.Violation.Reason
        CANNOT_CHANGE_PUBLISHED_FIELD_TYPE: PreconditionFailure.Violation.Reason
        CANNOT_MODIFY_LOCKED_COMPONENT: PreconditionFailure.Violation.Reason
        UNSUPPORT_ENABLED_APP_SETTINGS: PreconditionFailure.Violation.Reason
        FIELD_FIELD_NUMBER: _ClassVar[int]
        REASON_FIELD_NUMBER: _ClassVar[int]
        DISPLAY_MESSAGE_FIELD_NUMBER: _ClassVar[int]
        field: str
        reason: PreconditionFailure.Violation.Reason
        display_message: str

        def __init__(self, field: _Optional[str]=..., reason: _Optional[_Union[PreconditionFailure.Violation.Reason, str]]=..., display_message: _Optional[str]=...) -> None:
            ...
    VIOLATION_FIELD_NUMBER: _ClassVar[int]
    violation: _containers.RepeatedCompositeFieldContainer[PreconditionFailure.Violation]

    def __init__(self, violation: _Optional[_Iterable[_Union[PreconditionFailure.Violation, _Mapping]]]=...) -> None:
        ...