from google.api import field_behavior_pb2 as _field_behavior_pb2
from google.cloud.datacatalog.v1 import common_pb2 as _common_pb2
from google.protobuf import timestamp_pb2 as _timestamp_pb2
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Mapping as _Mapping, Optional as _Optional, Union as _Union
DESCRIPTOR: _descriptor.FileDescriptor

class SearchResultType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    SEARCH_RESULT_TYPE_UNSPECIFIED: _ClassVar[SearchResultType]
    ENTRY: _ClassVar[SearchResultType]
    TAG_TEMPLATE: _ClassVar[SearchResultType]
    ENTRY_GROUP: _ClassVar[SearchResultType]
SEARCH_RESULT_TYPE_UNSPECIFIED: SearchResultType
ENTRY: SearchResultType
TAG_TEMPLATE: SearchResultType
ENTRY_GROUP: SearchResultType

class SearchCatalogResult(_message.Message):
    __slots__ = ('search_result_type', 'search_result_subtype', 'relative_resource_name', 'linked_resource', 'modify_time', 'integrated_system', 'user_specified_system', 'fully_qualified_name', 'display_name', 'description')
    SEARCH_RESULT_TYPE_FIELD_NUMBER: _ClassVar[int]
    SEARCH_RESULT_SUBTYPE_FIELD_NUMBER: _ClassVar[int]
    RELATIVE_RESOURCE_NAME_FIELD_NUMBER: _ClassVar[int]
    LINKED_RESOURCE_FIELD_NUMBER: _ClassVar[int]
    MODIFY_TIME_FIELD_NUMBER: _ClassVar[int]
    INTEGRATED_SYSTEM_FIELD_NUMBER: _ClassVar[int]
    USER_SPECIFIED_SYSTEM_FIELD_NUMBER: _ClassVar[int]
    FULLY_QUALIFIED_NAME_FIELD_NUMBER: _ClassVar[int]
    DISPLAY_NAME_FIELD_NUMBER: _ClassVar[int]
    DESCRIPTION_FIELD_NUMBER: _ClassVar[int]
    search_result_type: SearchResultType
    search_result_subtype: str
    relative_resource_name: str
    linked_resource: str
    modify_time: _timestamp_pb2.Timestamp
    integrated_system: _common_pb2.IntegratedSystem
    user_specified_system: str
    fully_qualified_name: str
    display_name: str
    description: str

    def __init__(self, search_result_type: _Optional[_Union[SearchResultType, str]]=..., search_result_subtype: _Optional[str]=..., relative_resource_name: _Optional[str]=..., linked_resource: _Optional[str]=..., modify_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]]=..., integrated_system: _Optional[_Union[_common_pb2.IntegratedSystem, str]]=..., user_specified_system: _Optional[str]=..., fully_qualified_name: _Optional[str]=..., display_name: _Optional[str]=..., description: _Optional[str]=...) -> None:
        ...