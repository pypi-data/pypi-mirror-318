from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar
DESCRIPTOR: _descriptor.FileDescriptor

class OfflineEventUploadClientEnum(_message.Message):
    __slots__ = ()

    class OfflineEventUploadClient(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        UNSPECIFIED: _ClassVar[OfflineEventUploadClientEnum.OfflineEventUploadClient]
        UNKNOWN: _ClassVar[OfflineEventUploadClientEnum.OfflineEventUploadClient]
        GOOGLE_ADS_API: _ClassVar[OfflineEventUploadClientEnum.OfflineEventUploadClient]
        GOOGLE_ADS_WEB_CLIENT: _ClassVar[OfflineEventUploadClientEnum.OfflineEventUploadClient]
        ADS_DATA_CONNECTOR: _ClassVar[OfflineEventUploadClientEnum.OfflineEventUploadClient]
    UNSPECIFIED: OfflineEventUploadClientEnum.OfflineEventUploadClient
    UNKNOWN: OfflineEventUploadClientEnum.OfflineEventUploadClient
    GOOGLE_ADS_API: OfflineEventUploadClientEnum.OfflineEventUploadClient
    GOOGLE_ADS_WEB_CLIENT: OfflineEventUploadClientEnum.OfflineEventUploadClient
    ADS_DATA_CONNECTOR: OfflineEventUploadClientEnum.OfflineEventUploadClient

    def __init__(self) -> None:
        ...