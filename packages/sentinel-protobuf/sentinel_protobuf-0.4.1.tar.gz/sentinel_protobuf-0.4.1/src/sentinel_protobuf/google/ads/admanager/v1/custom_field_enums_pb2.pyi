from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar
DESCRIPTOR: _descriptor.FileDescriptor

class CustomFieldDataTypeEnum(_message.Message):
    __slots__ = ()

    class CustomFieldDataType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        CUSTOM_FIELD_DATA_TYPE_UNSPECIFIED: _ClassVar[CustomFieldDataTypeEnum.CustomFieldDataType]
        STRING: _ClassVar[CustomFieldDataTypeEnum.CustomFieldDataType]
        NUMBER: _ClassVar[CustomFieldDataTypeEnum.CustomFieldDataType]
        TOGGLE: _ClassVar[CustomFieldDataTypeEnum.CustomFieldDataType]
        DROP_DOWN: _ClassVar[CustomFieldDataTypeEnum.CustomFieldDataType]
    CUSTOM_FIELD_DATA_TYPE_UNSPECIFIED: CustomFieldDataTypeEnum.CustomFieldDataType
    STRING: CustomFieldDataTypeEnum.CustomFieldDataType
    NUMBER: CustomFieldDataTypeEnum.CustomFieldDataType
    TOGGLE: CustomFieldDataTypeEnum.CustomFieldDataType
    DROP_DOWN: CustomFieldDataTypeEnum.CustomFieldDataType

    def __init__(self) -> None:
        ...

class CustomFieldEntityTypeEnum(_message.Message):
    __slots__ = ()

    class CustomFieldEntityType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        CUSTOM_FIELD_ENTITY_TYPE_UNSPECIFIED: _ClassVar[CustomFieldEntityTypeEnum.CustomFieldEntityType]
        LINE_ITEM: _ClassVar[CustomFieldEntityTypeEnum.CustomFieldEntityType]
        ORDER: _ClassVar[CustomFieldEntityTypeEnum.CustomFieldEntityType]
        CREATIVE: _ClassVar[CustomFieldEntityTypeEnum.CustomFieldEntityType]
        PROPOSAL: _ClassVar[CustomFieldEntityTypeEnum.CustomFieldEntityType]
        PROPOSAL_LINE_ITEM: _ClassVar[CustomFieldEntityTypeEnum.CustomFieldEntityType]
    CUSTOM_FIELD_ENTITY_TYPE_UNSPECIFIED: CustomFieldEntityTypeEnum.CustomFieldEntityType
    LINE_ITEM: CustomFieldEntityTypeEnum.CustomFieldEntityType
    ORDER: CustomFieldEntityTypeEnum.CustomFieldEntityType
    CREATIVE: CustomFieldEntityTypeEnum.CustomFieldEntityType
    PROPOSAL: CustomFieldEntityTypeEnum.CustomFieldEntityType
    PROPOSAL_LINE_ITEM: CustomFieldEntityTypeEnum.CustomFieldEntityType

    def __init__(self) -> None:
        ...

class CustomFieldStatusEnum(_message.Message):
    __slots__ = ()

    class CustomFieldStatus(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        CUSTOM_FIELD_STATUS_UNSPECIFIED: _ClassVar[CustomFieldStatusEnum.CustomFieldStatus]
        ACTIVE: _ClassVar[CustomFieldStatusEnum.CustomFieldStatus]
        INACTIVE: _ClassVar[CustomFieldStatusEnum.CustomFieldStatus]
    CUSTOM_FIELD_STATUS_UNSPECIFIED: CustomFieldStatusEnum.CustomFieldStatus
    ACTIVE: CustomFieldStatusEnum.CustomFieldStatus
    INACTIVE: CustomFieldStatusEnum.CustomFieldStatus

    def __init__(self) -> None:
        ...

class CustomFieldVisibilityEnum(_message.Message):
    __slots__ = ()

    class CustomFieldVisibility(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        CUSTOM_FIELD_VISIBILITY_UNSPECIFIED: _ClassVar[CustomFieldVisibilityEnum.CustomFieldVisibility]
        HIDDEN: _ClassVar[CustomFieldVisibilityEnum.CustomFieldVisibility]
        READ_ONLY: _ClassVar[CustomFieldVisibilityEnum.CustomFieldVisibility]
        EDITABLE: _ClassVar[CustomFieldVisibilityEnum.CustomFieldVisibility]
    CUSTOM_FIELD_VISIBILITY_UNSPECIFIED: CustomFieldVisibilityEnum.CustomFieldVisibility
    HIDDEN: CustomFieldVisibilityEnum.CustomFieldVisibility
    READ_ONLY: CustomFieldVisibilityEnum.CustomFieldVisibility
    EDITABLE: CustomFieldVisibilityEnum.CustomFieldVisibility

    def __init__(self) -> None:
        ...