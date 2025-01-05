from google.api import field_behavior_pb2 as _field_behavior_pb2
from google.api import resource_pb2 as _resource_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Optional as _Optional, Union as _Union
DESCRIPTOR: _descriptor.FileDescriptor

class Tenant(_message.Message):
    __slots__ = ('name', 'external_id', 'usage_type', 'keyword_searchable_profile_custom_attributes')

    class DataUsageType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        DATA_USAGE_TYPE_UNSPECIFIED: _ClassVar[Tenant.DataUsageType]
        AGGREGATED: _ClassVar[Tenant.DataUsageType]
        ISOLATED: _ClassVar[Tenant.DataUsageType]
    DATA_USAGE_TYPE_UNSPECIFIED: Tenant.DataUsageType
    AGGREGATED: Tenant.DataUsageType
    ISOLATED: Tenant.DataUsageType
    NAME_FIELD_NUMBER: _ClassVar[int]
    EXTERNAL_ID_FIELD_NUMBER: _ClassVar[int]
    USAGE_TYPE_FIELD_NUMBER: _ClassVar[int]
    KEYWORD_SEARCHABLE_PROFILE_CUSTOM_ATTRIBUTES_FIELD_NUMBER: _ClassVar[int]
    name: str
    external_id: str
    usage_type: Tenant.DataUsageType
    keyword_searchable_profile_custom_attributes: _containers.RepeatedScalarFieldContainer[str]

    def __init__(self, name: _Optional[str]=..., external_id: _Optional[str]=..., usage_type: _Optional[_Union[Tenant.DataUsageType, str]]=..., keyword_searchable_profile_custom_attributes: _Optional[_Iterable[str]]=...) -> None:
        ...