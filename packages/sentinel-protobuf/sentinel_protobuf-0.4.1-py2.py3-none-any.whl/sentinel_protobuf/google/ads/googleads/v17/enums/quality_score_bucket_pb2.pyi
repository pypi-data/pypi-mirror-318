from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar
DESCRIPTOR: _descriptor.FileDescriptor

class QualityScoreBucketEnum(_message.Message):
    __slots__ = ()

    class QualityScoreBucket(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        UNSPECIFIED: _ClassVar[QualityScoreBucketEnum.QualityScoreBucket]
        UNKNOWN: _ClassVar[QualityScoreBucketEnum.QualityScoreBucket]
        BELOW_AVERAGE: _ClassVar[QualityScoreBucketEnum.QualityScoreBucket]
        AVERAGE: _ClassVar[QualityScoreBucketEnum.QualityScoreBucket]
        ABOVE_AVERAGE: _ClassVar[QualityScoreBucketEnum.QualityScoreBucket]
    UNSPECIFIED: QualityScoreBucketEnum.QualityScoreBucket
    UNKNOWN: QualityScoreBucketEnum.QualityScoreBucket
    BELOW_AVERAGE: QualityScoreBucketEnum.QualityScoreBucket
    AVERAGE: QualityScoreBucketEnum.QualityScoreBucket
    ABOVE_AVERAGE: QualityScoreBucketEnum.QualityScoreBucket

    def __init__(self) -> None:
        ...