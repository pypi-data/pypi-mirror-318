from google.ads.googleads.v17.enums import conversion_action_category_pb2 as _conversion_action_category_pb2
from google.ads.googleads.v17.enums import conversion_origin_pb2 as _conversion_origin_pb2
from google.api import field_behavior_pb2 as _field_behavior_pb2
from google.api import resource_pb2 as _resource_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union
DESCRIPTOR: _descriptor.FileDescriptor

class CustomerConversionGoal(_message.Message):
    __slots__ = ('resource_name', 'category', 'origin', 'biddable')
    RESOURCE_NAME_FIELD_NUMBER: _ClassVar[int]
    CATEGORY_FIELD_NUMBER: _ClassVar[int]
    ORIGIN_FIELD_NUMBER: _ClassVar[int]
    BIDDABLE_FIELD_NUMBER: _ClassVar[int]
    resource_name: str
    category: _conversion_action_category_pb2.ConversionActionCategoryEnum.ConversionActionCategory
    origin: _conversion_origin_pb2.ConversionOriginEnum.ConversionOrigin
    biddable: bool

    def __init__(self, resource_name: _Optional[str]=..., category: _Optional[_Union[_conversion_action_category_pb2.ConversionActionCategoryEnum.ConversionActionCategory, str]]=..., origin: _Optional[_Union[_conversion_origin_pb2.ConversionOriginEnum.ConversionOrigin, str]]=..., biddable: bool=...) -> None:
        ...