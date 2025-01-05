from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar
DESCRIPTOR: _descriptor.FileDescriptor

class DsaPageFeedCriterionFieldEnum(_message.Message):
    __slots__ = ()

    class DsaPageFeedCriterionField(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        UNSPECIFIED: _ClassVar[DsaPageFeedCriterionFieldEnum.DsaPageFeedCriterionField]
        UNKNOWN: _ClassVar[DsaPageFeedCriterionFieldEnum.DsaPageFeedCriterionField]
        PAGE_URL: _ClassVar[DsaPageFeedCriterionFieldEnum.DsaPageFeedCriterionField]
        LABEL: _ClassVar[DsaPageFeedCriterionFieldEnum.DsaPageFeedCriterionField]
    UNSPECIFIED: DsaPageFeedCriterionFieldEnum.DsaPageFeedCriterionField
    UNKNOWN: DsaPageFeedCriterionFieldEnum.DsaPageFeedCriterionField
    PAGE_URL: DsaPageFeedCriterionFieldEnum.DsaPageFeedCriterionField
    LABEL: DsaPageFeedCriterionFieldEnum.DsaPageFeedCriterionField

    def __init__(self) -> None:
        ...