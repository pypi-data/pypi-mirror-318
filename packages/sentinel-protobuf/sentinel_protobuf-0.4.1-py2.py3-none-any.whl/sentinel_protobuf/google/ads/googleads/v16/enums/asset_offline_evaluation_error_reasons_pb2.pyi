from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar
DESCRIPTOR: _descriptor.FileDescriptor

class AssetOfflineEvaluationErrorReasonsEnum(_message.Message):
    __slots__ = ()

    class AssetOfflineEvaluationErrorReasons(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        UNSPECIFIED: _ClassVar[AssetOfflineEvaluationErrorReasonsEnum.AssetOfflineEvaluationErrorReasons]
        UNKNOWN: _ClassVar[AssetOfflineEvaluationErrorReasonsEnum.AssetOfflineEvaluationErrorReasons]
        PRICE_ASSET_DESCRIPTION_REPEATS_ROW_HEADER: _ClassVar[AssetOfflineEvaluationErrorReasonsEnum.AssetOfflineEvaluationErrorReasons]
        PRICE_ASSET_REPETITIVE_HEADERS: _ClassVar[AssetOfflineEvaluationErrorReasonsEnum.AssetOfflineEvaluationErrorReasons]
        PRICE_ASSET_HEADER_INCOMPATIBLE_WITH_PRICE_TYPE: _ClassVar[AssetOfflineEvaluationErrorReasonsEnum.AssetOfflineEvaluationErrorReasons]
        PRICE_ASSET_DESCRIPTION_INCOMPATIBLE_WITH_ITEM_HEADER: _ClassVar[AssetOfflineEvaluationErrorReasonsEnum.AssetOfflineEvaluationErrorReasons]
        PRICE_ASSET_DESCRIPTION_HAS_PRICE_QUALIFIER: _ClassVar[AssetOfflineEvaluationErrorReasonsEnum.AssetOfflineEvaluationErrorReasons]
        PRICE_ASSET_UNSUPPORTED_LANGUAGE: _ClassVar[AssetOfflineEvaluationErrorReasonsEnum.AssetOfflineEvaluationErrorReasons]
        PRICE_ASSET_OTHER_ERROR: _ClassVar[AssetOfflineEvaluationErrorReasonsEnum.AssetOfflineEvaluationErrorReasons]
    UNSPECIFIED: AssetOfflineEvaluationErrorReasonsEnum.AssetOfflineEvaluationErrorReasons
    UNKNOWN: AssetOfflineEvaluationErrorReasonsEnum.AssetOfflineEvaluationErrorReasons
    PRICE_ASSET_DESCRIPTION_REPEATS_ROW_HEADER: AssetOfflineEvaluationErrorReasonsEnum.AssetOfflineEvaluationErrorReasons
    PRICE_ASSET_REPETITIVE_HEADERS: AssetOfflineEvaluationErrorReasonsEnum.AssetOfflineEvaluationErrorReasons
    PRICE_ASSET_HEADER_INCOMPATIBLE_WITH_PRICE_TYPE: AssetOfflineEvaluationErrorReasonsEnum.AssetOfflineEvaluationErrorReasons
    PRICE_ASSET_DESCRIPTION_INCOMPATIBLE_WITH_ITEM_HEADER: AssetOfflineEvaluationErrorReasonsEnum.AssetOfflineEvaluationErrorReasons
    PRICE_ASSET_DESCRIPTION_HAS_PRICE_QUALIFIER: AssetOfflineEvaluationErrorReasonsEnum.AssetOfflineEvaluationErrorReasons
    PRICE_ASSET_UNSUPPORTED_LANGUAGE: AssetOfflineEvaluationErrorReasonsEnum.AssetOfflineEvaluationErrorReasons
    PRICE_ASSET_OTHER_ERROR: AssetOfflineEvaluationErrorReasonsEnum.AssetOfflineEvaluationErrorReasons

    def __init__(self) -> None:
        ...