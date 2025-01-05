from google.ads.googleads.v16.common import customizer_value_pb2 as _customizer_value_pb2
from google.ads.googleads.v16.enums import customizer_value_status_pb2 as _customizer_value_status_pb2
from google.api import field_behavior_pb2 as _field_behavior_pb2
from google.api import resource_pb2 as _resource_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Mapping as _Mapping, Optional as _Optional, Union as _Union
DESCRIPTOR: _descriptor.FileDescriptor

class AdGroupCustomizer(_message.Message):
    __slots__ = ('resource_name', 'ad_group', 'customizer_attribute', 'status', 'value')
    RESOURCE_NAME_FIELD_NUMBER: _ClassVar[int]
    AD_GROUP_FIELD_NUMBER: _ClassVar[int]
    CUSTOMIZER_ATTRIBUTE_FIELD_NUMBER: _ClassVar[int]
    STATUS_FIELD_NUMBER: _ClassVar[int]
    VALUE_FIELD_NUMBER: _ClassVar[int]
    resource_name: str
    ad_group: str
    customizer_attribute: str
    status: _customizer_value_status_pb2.CustomizerValueStatusEnum.CustomizerValueStatus
    value: _customizer_value_pb2.CustomizerValue

    def __init__(self, resource_name: _Optional[str]=..., ad_group: _Optional[str]=..., customizer_attribute: _Optional[str]=..., status: _Optional[_Union[_customizer_value_status_pb2.CustomizerValueStatusEnum.CustomizerValueStatus, str]]=..., value: _Optional[_Union[_customizer_value_pb2.CustomizerValue, _Mapping]]=...) -> None:
        ...