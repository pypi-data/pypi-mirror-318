from google.api import field_behavior_pb2 as _field_behavior_pb2
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union
DESCRIPTOR: _descriptor.FileDescriptor

class RestrictionConfig(_message.Message):
    __slots__ = ('type',)

    class RestrictionType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        RESTRICTION_TYPE_UNSPECIFIED: _ClassVar[RestrictionConfig.RestrictionType]
        RESTRICTED_DATA_EGRESS: _ClassVar[RestrictionConfig.RestrictionType]
    RESTRICTION_TYPE_UNSPECIFIED: RestrictionConfig.RestrictionType
    RESTRICTED_DATA_EGRESS: RestrictionConfig.RestrictionType
    TYPE_FIELD_NUMBER: _ClassVar[int]
    type: RestrictionConfig.RestrictionType

    def __init__(self, type: _Optional[_Union[RestrictionConfig.RestrictionType, str]]=...) -> None:
        ...