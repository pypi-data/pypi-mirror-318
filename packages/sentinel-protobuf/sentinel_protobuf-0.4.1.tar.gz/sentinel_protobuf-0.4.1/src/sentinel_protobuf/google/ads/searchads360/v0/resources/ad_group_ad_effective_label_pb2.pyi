from google.api import field_behavior_pb2 as _field_behavior_pb2
from google.api import resource_pb2 as _resource_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional

DESCRIPTOR: _descriptor.FileDescriptor

class AdGroupAdEffectiveLabel(_message.Message):
    __slots__ = ("resource_name", "ad_group_ad", "label", "owner_customer_id")
    RESOURCE_NAME_FIELD_NUMBER: _ClassVar[int]
    AD_GROUP_AD_FIELD_NUMBER: _ClassVar[int]
    LABEL_FIELD_NUMBER: _ClassVar[int]
    OWNER_CUSTOMER_ID_FIELD_NUMBER: _ClassVar[int]
    resource_name: str
    ad_group_ad: str
    label: str
    owner_customer_id: int
    def __init__(self, resource_name: _Optional[str] = ..., ad_group_ad: _Optional[str] = ..., label: _Optional[str] = ..., owner_customer_id: _Optional[int] = ...) -> None: ...
