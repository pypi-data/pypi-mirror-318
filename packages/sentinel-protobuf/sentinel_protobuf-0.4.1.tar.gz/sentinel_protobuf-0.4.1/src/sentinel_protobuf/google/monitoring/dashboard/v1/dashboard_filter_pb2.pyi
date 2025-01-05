from google.api import field_behavior_pb2 as _field_behavior_pb2
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union
DESCRIPTOR: _descriptor.FileDescriptor

class DashboardFilter(_message.Message):
    __slots__ = ('label_key', 'template_variable', 'string_value', 'filter_type')

    class FilterType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        FILTER_TYPE_UNSPECIFIED: _ClassVar[DashboardFilter.FilterType]
        RESOURCE_LABEL: _ClassVar[DashboardFilter.FilterType]
        METRIC_LABEL: _ClassVar[DashboardFilter.FilterType]
        USER_METADATA_LABEL: _ClassVar[DashboardFilter.FilterType]
        SYSTEM_METADATA_LABEL: _ClassVar[DashboardFilter.FilterType]
        GROUP: _ClassVar[DashboardFilter.FilterType]
    FILTER_TYPE_UNSPECIFIED: DashboardFilter.FilterType
    RESOURCE_LABEL: DashboardFilter.FilterType
    METRIC_LABEL: DashboardFilter.FilterType
    USER_METADATA_LABEL: DashboardFilter.FilterType
    SYSTEM_METADATA_LABEL: DashboardFilter.FilterType
    GROUP: DashboardFilter.FilterType
    LABEL_KEY_FIELD_NUMBER: _ClassVar[int]
    TEMPLATE_VARIABLE_FIELD_NUMBER: _ClassVar[int]
    STRING_VALUE_FIELD_NUMBER: _ClassVar[int]
    FILTER_TYPE_FIELD_NUMBER: _ClassVar[int]
    label_key: str
    template_variable: str
    string_value: str
    filter_type: DashboardFilter.FilterType

    def __init__(self, label_key: _Optional[str]=..., template_variable: _Optional[str]=..., string_value: _Optional[str]=..., filter_type: _Optional[_Union[DashboardFilter.FilterType, str]]=...) -> None:
        ...