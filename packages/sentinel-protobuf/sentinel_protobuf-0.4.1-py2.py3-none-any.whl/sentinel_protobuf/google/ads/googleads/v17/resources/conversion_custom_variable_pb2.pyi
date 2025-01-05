from google.ads.googleads.v17.enums import conversion_custom_variable_status_pb2 as _conversion_custom_variable_status_pb2
from google.api import field_behavior_pb2 as _field_behavior_pb2
from google.api import resource_pb2 as _resource_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union
DESCRIPTOR: _descriptor.FileDescriptor

class ConversionCustomVariable(_message.Message):
    __slots__ = ('resource_name', 'id', 'name', 'tag', 'status', 'owner_customer')
    RESOURCE_NAME_FIELD_NUMBER: _ClassVar[int]
    ID_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    TAG_FIELD_NUMBER: _ClassVar[int]
    STATUS_FIELD_NUMBER: _ClassVar[int]
    OWNER_CUSTOMER_FIELD_NUMBER: _ClassVar[int]
    resource_name: str
    id: int
    name: str
    tag: str
    status: _conversion_custom_variable_status_pb2.ConversionCustomVariableStatusEnum.ConversionCustomVariableStatus
    owner_customer: str

    def __init__(self, resource_name: _Optional[str]=..., id: _Optional[int]=..., name: _Optional[str]=..., tag: _Optional[str]=..., status: _Optional[_Union[_conversion_custom_variable_status_pb2.ConversionCustomVariableStatusEnum.ConversionCustomVariableStatus, str]]=..., owner_customer: _Optional[str]=...) -> None:
        ...