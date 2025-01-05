from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar
DESCRIPTOR: _descriptor.FileDescriptor

class AssetGroupSignalErrorEnum(_message.Message):
    __slots__ = ()

    class AssetGroupSignalError(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        UNSPECIFIED: _ClassVar[AssetGroupSignalErrorEnum.AssetGroupSignalError]
        UNKNOWN: _ClassVar[AssetGroupSignalErrorEnum.AssetGroupSignalError]
        TOO_MANY_WORDS: _ClassVar[AssetGroupSignalErrorEnum.AssetGroupSignalError]
        SEARCH_THEME_POLICY_VIOLATION: _ClassVar[AssetGroupSignalErrorEnum.AssetGroupSignalError]
        AUDIENCE_WITH_WRONG_ASSET_GROUP_ID: _ClassVar[AssetGroupSignalErrorEnum.AssetGroupSignalError]
    UNSPECIFIED: AssetGroupSignalErrorEnum.AssetGroupSignalError
    UNKNOWN: AssetGroupSignalErrorEnum.AssetGroupSignalError
    TOO_MANY_WORDS: AssetGroupSignalErrorEnum.AssetGroupSignalError
    SEARCH_THEME_POLICY_VIOLATION: AssetGroupSignalErrorEnum.AssetGroupSignalError
    AUDIENCE_WITH_WRONG_ASSET_GROUP_ID: AssetGroupSignalErrorEnum.AssetGroupSignalError

    def __init__(self) -> None:
        ...