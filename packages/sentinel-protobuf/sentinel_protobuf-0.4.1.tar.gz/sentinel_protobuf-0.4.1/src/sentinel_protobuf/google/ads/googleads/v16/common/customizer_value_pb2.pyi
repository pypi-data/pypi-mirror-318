from google.ads.googleads.v16.enums import customizer_attribute_type_pb2 as _customizer_attribute_type_pb2
from google.api import field_behavior_pb2 as _field_behavior_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union
DESCRIPTOR: _descriptor.FileDescriptor

class CustomizerValue(_message.Message):
    __slots__ = ('type', 'string_value')
    TYPE_FIELD_NUMBER: _ClassVar[int]
    STRING_VALUE_FIELD_NUMBER: _ClassVar[int]
    type: _customizer_attribute_type_pb2.CustomizerAttributeTypeEnum.CustomizerAttributeType
    string_value: str

    def __init__(self, type: _Optional[_Union[_customizer_attribute_type_pb2.CustomizerAttributeTypeEnum.CustomizerAttributeType, str]]=..., string_value: _Optional[str]=...) -> None:
        ...