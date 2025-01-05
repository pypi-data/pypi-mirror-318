from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar
DESCRIPTOR: _descriptor.FileDescriptor

class AutomaticallyCreatedAssetRemovalErrorEnum(_message.Message):
    __slots__ = ()

    class AutomaticallyCreatedAssetRemovalError(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        UNSPECIFIED: _ClassVar[AutomaticallyCreatedAssetRemovalErrorEnum.AutomaticallyCreatedAssetRemovalError]
        UNKNOWN: _ClassVar[AutomaticallyCreatedAssetRemovalErrorEnum.AutomaticallyCreatedAssetRemovalError]
        AD_DOES_NOT_EXIST: _ClassVar[AutomaticallyCreatedAssetRemovalErrorEnum.AutomaticallyCreatedAssetRemovalError]
        INVALID_AD_TYPE: _ClassVar[AutomaticallyCreatedAssetRemovalErrorEnum.AutomaticallyCreatedAssetRemovalError]
        ASSET_DOES_NOT_EXIST: _ClassVar[AutomaticallyCreatedAssetRemovalErrorEnum.AutomaticallyCreatedAssetRemovalError]
        ASSET_FIELD_TYPE_DOES_NOT_MATCH: _ClassVar[AutomaticallyCreatedAssetRemovalErrorEnum.AutomaticallyCreatedAssetRemovalError]
        NOT_AN_AUTOMATICALLY_CREATED_ASSET: _ClassVar[AutomaticallyCreatedAssetRemovalErrorEnum.AutomaticallyCreatedAssetRemovalError]
    UNSPECIFIED: AutomaticallyCreatedAssetRemovalErrorEnum.AutomaticallyCreatedAssetRemovalError
    UNKNOWN: AutomaticallyCreatedAssetRemovalErrorEnum.AutomaticallyCreatedAssetRemovalError
    AD_DOES_NOT_EXIST: AutomaticallyCreatedAssetRemovalErrorEnum.AutomaticallyCreatedAssetRemovalError
    INVALID_AD_TYPE: AutomaticallyCreatedAssetRemovalErrorEnum.AutomaticallyCreatedAssetRemovalError
    ASSET_DOES_NOT_EXIST: AutomaticallyCreatedAssetRemovalErrorEnum.AutomaticallyCreatedAssetRemovalError
    ASSET_FIELD_TYPE_DOES_NOT_MATCH: AutomaticallyCreatedAssetRemovalErrorEnum.AutomaticallyCreatedAssetRemovalError
    NOT_AN_AUTOMATICALLY_CREATED_ASSET: AutomaticallyCreatedAssetRemovalErrorEnum.AutomaticallyCreatedAssetRemovalError

    def __init__(self) -> None:
        ...