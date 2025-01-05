from google.ads.googleads.v16.enums import customizer_attribute_status_pb2 as _customizer_attribute_status_pb2
from google.ads.googleads.v16.enums import customizer_attribute_type_pb2 as _customizer_attribute_type_pb2
from google.api import field_behavior_pb2 as _field_behavior_pb2
from google.api import resource_pb2 as _resource_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union
DESCRIPTOR: _descriptor.FileDescriptor

class CustomizerAttribute(_message.Message):
    __slots__ = ('resource_name', 'id', 'name', 'type', 'status')
    RESOURCE_NAME_FIELD_NUMBER: _ClassVar[int]
    ID_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    TYPE_FIELD_NUMBER: _ClassVar[int]
    STATUS_FIELD_NUMBER: _ClassVar[int]
    resource_name: str
    id: int
    name: str
    type: _customizer_attribute_type_pb2.CustomizerAttributeTypeEnum.CustomizerAttributeType
    status: _customizer_attribute_status_pb2.CustomizerAttributeStatusEnum.CustomizerAttributeStatus

    def __init__(self, resource_name: _Optional[str]=..., id: _Optional[int]=..., name: _Optional[str]=..., type: _Optional[_Union[_customizer_attribute_type_pb2.CustomizerAttributeTypeEnum.CustomizerAttributeType, str]]=..., status: _Optional[_Union[_customizer_attribute_status_pb2.CustomizerAttributeStatusEnum.CustomizerAttributeStatus, str]]=...) -> None:
        ...