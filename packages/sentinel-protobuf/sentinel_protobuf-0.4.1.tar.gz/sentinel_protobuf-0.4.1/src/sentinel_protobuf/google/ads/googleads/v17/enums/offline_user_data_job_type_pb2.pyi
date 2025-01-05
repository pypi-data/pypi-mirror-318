from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar
DESCRIPTOR: _descriptor.FileDescriptor

class OfflineUserDataJobTypeEnum(_message.Message):
    __slots__ = ()

    class OfflineUserDataJobType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        UNSPECIFIED: _ClassVar[OfflineUserDataJobTypeEnum.OfflineUserDataJobType]
        UNKNOWN: _ClassVar[OfflineUserDataJobTypeEnum.OfflineUserDataJobType]
        STORE_SALES_UPLOAD_FIRST_PARTY: _ClassVar[OfflineUserDataJobTypeEnum.OfflineUserDataJobType]
        STORE_SALES_UPLOAD_THIRD_PARTY: _ClassVar[OfflineUserDataJobTypeEnum.OfflineUserDataJobType]
        CUSTOMER_MATCH_USER_LIST: _ClassVar[OfflineUserDataJobTypeEnum.OfflineUserDataJobType]
        CUSTOMER_MATCH_WITH_ATTRIBUTES: _ClassVar[OfflineUserDataJobTypeEnum.OfflineUserDataJobType]
    UNSPECIFIED: OfflineUserDataJobTypeEnum.OfflineUserDataJobType
    UNKNOWN: OfflineUserDataJobTypeEnum.OfflineUserDataJobType
    STORE_SALES_UPLOAD_FIRST_PARTY: OfflineUserDataJobTypeEnum.OfflineUserDataJobType
    STORE_SALES_UPLOAD_THIRD_PARTY: OfflineUserDataJobTypeEnum.OfflineUserDataJobType
    CUSTOMER_MATCH_USER_LIST: OfflineUserDataJobTypeEnum.OfflineUserDataJobType
    CUSTOMER_MATCH_WITH_ATTRIBUTES: OfflineUserDataJobTypeEnum.OfflineUserDataJobType

    def __init__(self) -> None:
        ...