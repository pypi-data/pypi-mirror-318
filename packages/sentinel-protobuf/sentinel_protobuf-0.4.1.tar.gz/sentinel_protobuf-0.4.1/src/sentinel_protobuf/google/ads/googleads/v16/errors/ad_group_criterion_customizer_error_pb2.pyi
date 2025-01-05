from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar
DESCRIPTOR: _descriptor.FileDescriptor

class AdGroupCriterionCustomizerErrorEnum(_message.Message):
    __slots__ = ()

    class AdGroupCriterionCustomizerError(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        UNSPECIFIED: _ClassVar[AdGroupCriterionCustomizerErrorEnum.AdGroupCriterionCustomizerError]
        UNKNOWN: _ClassVar[AdGroupCriterionCustomizerErrorEnum.AdGroupCriterionCustomizerError]
        CRITERION_IS_NOT_KEYWORD: _ClassVar[AdGroupCriterionCustomizerErrorEnum.AdGroupCriterionCustomizerError]
    UNSPECIFIED: AdGroupCriterionCustomizerErrorEnum.AdGroupCriterionCustomizerError
    UNKNOWN: AdGroupCriterionCustomizerErrorEnum.AdGroupCriterionCustomizerError
    CRITERION_IS_NOT_KEYWORD: AdGroupCriterionCustomizerErrorEnum.AdGroupCriterionCustomizerError

    def __init__(self) -> None:
        ...