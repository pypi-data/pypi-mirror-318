from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar
DESCRIPTOR: _descriptor.FileDescriptor

class LabelErrorEnum(_message.Message):
    __slots__ = ()

    class LabelError(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        UNSPECIFIED: _ClassVar[LabelErrorEnum.LabelError]
        UNKNOWN: _ClassVar[LabelErrorEnum.LabelError]
        CANNOT_APPLY_INACTIVE_LABEL: _ClassVar[LabelErrorEnum.LabelError]
        CANNOT_APPLY_LABEL_TO_DISABLED_AD_GROUP_CRITERION: _ClassVar[LabelErrorEnum.LabelError]
        CANNOT_APPLY_LABEL_TO_NEGATIVE_AD_GROUP_CRITERION: _ClassVar[LabelErrorEnum.LabelError]
        EXCEEDED_LABEL_LIMIT_PER_TYPE: _ClassVar[LabelErrorEnum.LabelError]
        INVALID_RESOURCE_FOR_MANAGER_LABEL: _ClassVar[LabelErrorEnum.LabelError]
        DUPLICATE_NAME: _ClassVar[LabelErrorEnum.LabelError]
        INVALID_LABEL_NAME: _ClassVar[LabelErrorEnum.LabelError]
        CANNOT_ATTACH_LABEL_TO_DRAFT: _ClassVar[LabelErrorEnum.LabelError]
        CANNOT_ATTACH_NON_MANAGER_LABEL_TO_CUSTOMER: _ClassVar[LabelErrorEnum.LabelError]
    UNSPECIFIED: LabelErrorEnum.LabelError
    UNKNOWN: LabelErrorEnum.LabelError
    CANNOT_APPLY_INACTIVE_LABEL: LabelErrorEnum.LabelError
    CANNOT_APPLY_LABEL_TO_DISABLED_AD_GROUP_CRITERION: LabelErrorEnum.LabelError
    CANNOT_APPLY_LABEL_TO_NEGATIVE_AD_GROUP_CRITERION: LabelErrorEnum.LabelError
    EXCEEDED_LABEL_LIMIT_PER_TYPE: LabelErrorEnum.LabelError
    INVALID_RESOURCE_FOR_MANAGER_LABEL: LabelErrorEnum.LabelError
    DUPLICATE_NAME: LabelErrorEnum.LabelError
    INVALID_LABEL_NAME: LabelErrorEnum.LabelError
    CANNOT_ATTACH_LABEL_TO_DRAFT: LabelErrorEnum.LabelError
    CANNOT_ATTACH_NON_MANAGER_LABEL_TO_CUSTOMER: LabelErrorEnum.LabelError

    def __init__(self) -> None:
        ...