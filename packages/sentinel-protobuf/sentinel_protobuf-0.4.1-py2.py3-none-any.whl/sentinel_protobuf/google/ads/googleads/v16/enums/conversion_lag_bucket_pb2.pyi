from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar
DESCRIPTOR: _descriptor.FileDescriptor

class ConversionLagBucketEnum(_message.Message):
    __slots__ = ()

    class ConversionLagBucket(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        UNSPECIFIED: _ClassVar[ConversionLagBucketEnum.ConversionLagBucket]
        UNKNOWN: _ClassVar[ConversionLagBucketEnum.ConversionLagBucket]
        LESS_THAN_ONE_DAY: _ClassVar[ConversionLagBucketEnum.ConversionLagBucket]
        ONE_TO_TWO_DAYS: _ClassVar[ConversionLagBucketEnum.ConversionLagBucket]
        TWO_TO_THREE_DAYS: _ClassVar[ConversionLagBucketEnum.ConversionLagBucket]
        THREE_TO_FOUR_DAYS: _ClassVar[ConversionLagBucketEnum.ConversionLagBucket]
        FOUR_TO_FIVE_DAYS: _ClassVar[ConversionLagBucketEnum.ConversionLagBucket]
        FIVE_TO_SIX_DAYS: _ClassVar[ConversionLagBucketEnum.ConversionLagBucket]
        SIX_TO_SEVEN_DAYS: _ClassVar[ConversionLagBucketEnum.ConversionLagBucket]
        SEVEN_TO_EIGHT_DAYS: _ClassVar[ConversionLagBucketEnum.ConversionLagBucket]
        EIGHT_TO_NINE_DAYS: _ClassVar[ConversionLagBucketEnum.ConversionLagBucket]
        NINE_TO_TEN_DAYS: _ClassVar[ConversionLagBucketEnum.ConversionLagBucket]
        TEN_TO_ELEVEN_DAYS: _ClassVar[ConversionLagBucketEnum.ConversionLagBucket]
        ELEVEN_TO_TWELVE_DAYS: _ClassVar[ConversionLagBucketEnum.ConversionLagBucket]
        TWELVE_TO_THIRTEEN_DAYS: _ClassVar[ConversionLagBucketEnum.ConversionLagBucket]
        THIRTEEN_TO_FOURTEEN_DAYS: _ClassVar[ConversionLagBucketEnum.ConversionLagBucket]
        FOURTEEN_TO_TWENTY_ONE_DAYS: _ClassVar[ConversionLagBucketEnum.ConversionLagBucket]
        TWENTY_ONE_TO_THIRTY_DAYS: _ClassVar[ConversionLagBucketEnum.ConversionLagBucket]
        THIRTY_TO_FORTY_FIVE_DAYS: _ClassVar[ConversionLagBucketEnum.ConversionLagBucket]
        FORTY_FIVE_TO_SIXTY_DAYS: _ClassVar[ConversionLagBucketEnum.ConversionLagBucket]
        SIXTY_TO_NINETY_DAYS: _ClassVar[ConversionLagBucketEnum.ConversionLagBucket]
    UNSPECIFIED: ConversionLagBucketEnum.ConversionLagBucket
    UNKNOWN: ConversionLagBucketEnum.ConversionLagBucket
    LESS_THAN_ONE_DAY: ConversionLagBucketEnum.ConversionLagBucket
    ONE_TO_TWO_DAYS: ConversionLagBucketEnum.ConversionLagBucket
    TWO_TO_THREE_DAYS: ConversionLagBucketEnum.ConversionLagBucket
    THREE_TO_FOUR_DAYS: ConversionLagBucketEnum.ConversionLagBucket
    FOUR_TO_FIVE_DAYS: ConversionLagBucketEnum.ConversionLagBucket
    FIVE_TO_SIX_DAYS: ConversionLagBucketEnum.ConversionLagBucket
    SIX_TO_SEVEN_DAYS: ConversionLagBucketEnum.ConversionLagBucket
    SEVEN_TO_EIGHT_DAYS: ConversionLagBucketEnum.ConversionLagBucket
    EIGHT_TO_NINE_DAYS: ConversionLagBucketEnum.ConversionLagBucket
    NINE_TO_TEN_DAYS: ConversionLagBucketEnum.ConversionLagBucket
    TEN_TO_ELEVEN_DAYS: ConversionLagBucketEnum.ConversionLagBucket
    ELEVEN_TO_TWELVE_DAYS: ConversionLagBucketEnum.ConversionLagBucket
    TWELVE_TO_THIRTEEN_DAYS: ConversionLagBucketEnum.ConversionLagBucket
    THIRTEEN_TO_FOURTEEN_DAYS: ConversionLagBucketEnum.ConversionLagBucket
    FOURTEEN_TO_TWENTY_ONE_DAYS: ConversionLagBucketEnum.ConversionLagBucket
    TWENTY_ONE_TO_THIRTY_DAYS: ConversionLagBucketEnum.ConversionLagBucket
    THIRTY_TO_FORTY_FIVE_DAYS: ConversionLagBucketEnum.ConversionLagBucket
    FORTY_FIVE_TO_SIXTY_DAYS: ConversionLagBucketEnum.ConversionLagBucket
    SIXTY_TO_NINETY_DAYS: ConversionLagBucketEnum.ConversionLagBucket

    def __init__(self) -> None:
        ...