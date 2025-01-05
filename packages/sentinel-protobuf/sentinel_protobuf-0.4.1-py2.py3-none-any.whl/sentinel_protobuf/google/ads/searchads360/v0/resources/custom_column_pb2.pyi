from google.ads.searchads360.v0.enums import custom_column_render_type_pb2 as _custom_column_render_type_pb2
from google.ads.searchads360.v0.enums import custom_column_value_type_pb2 as _custom_column_value_type_pb2
from google.api import field_behavior_pb2 as _field_behavior_pb2
from google.api import resource_pb2 as _resource_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Optional as _Optional, Union as _Union
DESCRIPTOR: _descriptor.FileDescriptor

class CustomColumn(_message.Message):
    __slots__ = ('resource_name', 'id', 'name', 'description', 'value_type', 'references_attributes', 'references_metrics', 'queryable', 'referenced_system_columns', 'render_type')
    RESOURCE_NAME_FIELD_NUMBER: _ClassVar[int]
    ID_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    DESCRIPTION_FIELD_NUMBER: _ClassVar[int]
    VALUE_TYPE_FIELD_NUMBER: _ClassVar[int]
    REFERENCES_ATTRIBUTES_FIELD_NUMBER: _ClassVar[int]
    REFERENCES_METRICS_FIELD_NUMBER: _ClassVar[int]
    QUERYABLE_FIELD_NUMBER: _ClassVar[int]
    REFERENCED_SYSTEM_COLUMNS_FIELD_NUMBER: _ClassVar[int]
    RENDER_TYPE_FIELD_NUMBER: _ClassVar[int]
    resource_name: str
    id: int
    name: str
    description: str
    value_type: _custom_column_value_type_pb2.CustomColumnValueTypeEnum.CustomColumnValueType
    references_attributes: bool
    references_metrics: bool
    queryable: bool
    referenced_system_columns: _containers.RepeatedScalarFieldContainer[str]
    render_type: _custom_column_render_type_pb2.CustomColumnRenderTypeEnum.CustomColumnRenderType

    def __init__(self, resource_name: _Optional[str]=..., id: _Optional[int]=..., name: _Optional[str]=..., description: _Optional[str]=..., value_type: _Optional[_Union[_custom_column_value_type_pb2.CustomColumnValueTypeEnum.CustomColumnValueType, str]]=..., references_attributes: bool=..., references_metrics: bool=..., queryable: bool=..., referenced_system_columns: _Optional[_Iterable[str]]=..., render_type: _Optional[_Union[_custom_column_render_type_pb2.CustomColumnRenderTypeEnum.CustomColumnRenderType, str]]=...) -> None:
        ...