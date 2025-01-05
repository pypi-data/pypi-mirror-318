from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from typing import ClassVar as _ClassVar
DESCRIPTOR: _descriptor.FileDescriptor

class NotificationCategory(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    NOTIFICATION_CATEGORY_UNSPECIFIED: _ClassVar[NotificationCategory]
    ALL: _ClassVar[NotificationCategory]
    SUSPENSION: _ClassVar[NotificationCategory]
    SECURITY: _ClassVar[NotificationCategory]
    TECHNICAL: _ClassVar[NotificationCategory]
    BILLING: _ClassVar[NotificationCategory]
    LEGAL: _ClassVar[NotificationCategory]
    PRODUCT_UPDATES: _ClassVar[NotificationCategory]
    TECHNICAL_INCIDENTS: _ClassVar[NotificationCategory]

class ValidationState(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    VALIDATION_STATE_UNSPECIFIED: _ClassVar[ValidationState]
    VALID: _ClassVar[ValidationState]
    INVALID: _ClassVar[ValidationState]
NOTIFICATION_CATEGORY_UNSPECIFIED: NotificationCategory
ALL: NotificationCategory
SUSPENSION: NotificationCategory
SECURITY: NotificationCategory
TECHNICAL: NotificationCategory
BILLING: NotificationCategory
LEGAL: NotificationCategory
PRODUCT_UPDATES: NotificationCategory
TECHNICAL_INCIDENTS: NotificationCategory
VALIDATION_STATE_UNSPECIFIED: ValidationState
VALID: ValidationState
INVALID: ValidationState