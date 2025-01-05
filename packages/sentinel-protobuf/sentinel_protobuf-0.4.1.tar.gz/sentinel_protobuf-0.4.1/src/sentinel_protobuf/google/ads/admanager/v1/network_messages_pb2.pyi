from google.api import field_behavior_pb2 as _field_behavior_pb2
from google.api import resource_pb2 as _resource_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Optional as _Optional
DESCRIPTOR: _descriptor.FileDescriptor

class Network(_message.Message):
    __slots__ = ('name', 'display_name', 'network_code', 'property_code', 'time_zone', 'currency_code', 'secondary_currency_codes', 'effective_root_ad_unit', 'test_network', 'network_id')
    NAME_FIELD_NUMBER: _ClassVar[int]
    DISPLAY_NAME_FIELD_NUMBER: _ClassVar[int]
    NETWORK_CODE_FIELD_NUMBER: _ClassVar[int]
    PROPERTY_CODE_FIELD_NUMBER: _ClassVar[int]
    TIME_ZONE_FIELD_NUMBER: _ClassVar[int]
    CURRENCY_CODE_FIELD_NUMBER: _ClassVar[int]
    SECONDARY_CURRENCY_CODES_FIELD_NUMBER: _ClassVar[int]
    EFFECTIVE_ROOT_AD_UNIT_FIELD_NUMBER: _ClassVar[int]
    TEST_NETWORK_FIELD_NUMBER: _ClassVar[int]
    NETWORK_ID_FIELD_NUMBER: _ClassVar[int]
    name: str
    display_name: str
    network_code: str
    property_code: str
    time_zone: str
    currency_code: str
    secondary_currency_codes: _containers.RepeatedScalarFieldContainer[str]
    effective_root_ad_unit: str
    test_network: bool
    network_id: int

    def __init__(self, name: _Optional[str]=..., display_name: _Optional[str]=..., network_code: _Optional[str]=..., property_code: _Optional[str]=..., time_zone: _Optional[str]=..., currency_code: _Optional[str]=..., secondary_currency_codes: _Optional[_Iterable[str]]=..., effective_root_ad_unit: _Optional[str]=..., test_network: bool=..., network_id: _Optional[int]=...) -> None:
        ...