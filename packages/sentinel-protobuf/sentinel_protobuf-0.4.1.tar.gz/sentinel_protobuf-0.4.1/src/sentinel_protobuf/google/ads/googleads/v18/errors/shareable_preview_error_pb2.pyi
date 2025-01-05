from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar
DESCRIPTOR: _descriptor.FileDescriptor

class ShareablePreviewErrorEnum(_message.Message):
    __slots__ = ()

    class ShareablePreviewError(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        UNSPECIFIED: _ClassVar[ShareablePreviewErrorEnum.ShareablePreviewError]
        UNKNOWN: _ClassVar[ShareablePreviewErrorEnum.ShareablePreviewError]
        TOO_MANY_ASSET_GROUPS_IN_REQUEST: _ClassVar[ShareablePreviewErrorEnum.ShareablePreviewError]
        ASSET_GROUP_DOES_NOT_EXIST_UNDER_THIS_CUSTOMER: _ClassVar[ShareablePreviewErrorEnum.ShareablePreviewError]
    UNSPECIFIED: ShareablePreviewErrorEnum.ShareablePreviewError
    UNKNOWN: ShareablePreviewErrorEnum.ShareablePreviewError
    TOO_MANY_ASSET_GROUPS_IN_REQUEST: ShareablePreviewErrorEnum.ShareablePreviewError
    ASSET_GROUP_DOES_NOT_EXIST_UNDER_THIS_CUSTOMER: ShareablePreviewErrorEnum.ShareablePreviewError

    def __init__(self) -> None:
        ...