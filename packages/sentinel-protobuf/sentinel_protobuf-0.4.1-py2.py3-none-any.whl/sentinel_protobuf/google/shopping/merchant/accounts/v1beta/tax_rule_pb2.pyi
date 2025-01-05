from google.api import field_behavior_pb2 as _field_behavior_pb2
from google.type import interval_pb2 as _interval_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Mapping as _Mapping, Optional as _Optional, Union as _Union
DESCRIPTOR: _descriptor.FileDescriptor

class TaxRule(_message.Message):
    __slots__ = ('location_id', 'post_code_range', 'use_google_rate', 'self_specified_rate_micros', 'region_code', 'shipping_taxed', 'effective_time_period')

    class TaxPostalCodeRange(_message.Message):
        __slots__ = ('start', 'end')
        START_FIELD_NUMBER: _ClassVar[int]
        END_FIELD_NUMBER: _ClassVar[int]
        start: str
        end: str

        def __init__(self, start: _Optional[str]=..., end: _Optional[str]=...) -> None:
            ...
    LOCATION_ID_FIELD_NUMBER: _ClassVar[int]
    POST_CODE_RANGE_FIELD_NUMBER: _ClassVar[int]
    USE_GOOGLE_RATE_FIELD_NUMBER: _ClassVar[int]
    SELF_SPECIFIED_RATE_MICROS_FIELD_NUMBER: _ClassVar[int]
    REGION_CODE_FIELD_NUMBER: _ClassVar[int]
    SHIPPING_TAXED_FIELD_NUMBER: _ClassVar[int]
    EFFECTIVE_TIME_PERIOD_FIELD_NUMBER: _ClassVar[int]
    location_id: int
    post_code_range: TaxRule.TaxPostalCodeRange
    use_google_rate: bool
    self_specified_rate_micros: int
    region_code: str
    shipping_taxed: bool
    effective_time_period: _interval_pb2.Interval

    def __init__(self, location_id: _Optional[int]=..., post_code_range: _Optional[_Union[TaxRule.TaxPostalCodeRange, _Mapping]]=..., use_google_rate: bool=..., self_specified_rate_micros: _Optional[int]=..., region_code: _Optional[str]=..., shipping_taxed: bool=..., effective_time_period: _Optional[_Union[_interval_pb2.Interval, _Mapping]]=...) -> None:
        ...