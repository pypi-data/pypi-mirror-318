from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union
DESCRIPTOR: _descriptor.FileDescriptor

class NetworkSettings(_message.Message):
    __slots__ = ('ingress_traffic_allowed',)

    class IngressTrafficAllowed(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        INGRESS_TRAFFIC_ALLOWED_UNSPECIFIED: _ClassVar[NetworkSettings.IngressTrafficAllowed]
        INGRESS_TRAFFIC_ALLOWED_ALL: _ClassVar[NetworkSettings.IngressTrafficAllowed]
        INGRESS_TRAFFIC_ALLOWED_INTERNAL_ONLY: _ClassVar[NetworkSettings.IngressTrafficAllowed]
        INGRESS_TRAFFIC_ALLOWED_INTERNAL_AND_LB: _ClassVar[NetworkSettings.IngressTrafficAllowed]
    INGRESS_TRAFFIC_ALLOWED_UNSPECIFIED: NetworkSettings.IngressTrafficAllowed
    INGRESS_TRAFFIC_ALLOWED_ALL: NetworkSettings.IngressTrafficAllowed
    INGRESS_TRAFFIC_ALLOWED_INTERNAL_ONLY: NetworkSettings.IngressTrafficAllowed
    INGRESS_TRAFFIC_ALLOWED_INTERNAL_AND_LB: NetworkSettings.IngressTrafficAllowed
    INGRESS_TRAFFIC_ALLOWED_FIELD_NUMBER: _ClassVar[int]
    ingress_traffic_allowed: NetworkSettings.IngressTrafficAllowed

    def __init__(self, ingress_traffic_allowed: _Optional[_Union[NetworkSettings.IngressTrafficAllowed, str]]=...) -> None:
        ...