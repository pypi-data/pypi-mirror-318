from google.api import field_behavior_pb2 as _field_behavior_pb2
from google.api import resource_pb2 as _resource_pb2
from google.monitoring.dashboard.v1 import dashboard_filter_pb2 as _dashboard_filter_pb2
from google.monitoring.dashboard.v1 import layouts_pb2 as _layouts_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union
DESCRIPTOR: _descriptor.FileDescriptor

class Dashboard(_message.Message):
    __slots__ = ('name', 'display_name', 'etag', 'grid_layout', 'mosaic_layout', 'row_layout', 'column_layout', 'dashboard_filters', 'labels')

    class LabelsEntry(_message.Message):
        __slots__ = ('key', 'value')
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: str

        def __init__(self, key: _Optional[str]=..., value: _Optional[str]=...) -> None:
            ...
    NAME_FIELD_NUMBER: _ClassVar[int]
    DISPLAY_NAME_FIELD_NUMBER: _ClassVar[int]
    ETAG_FIELD_NUMBER: _ClassVar[int]
    GRID_LAYOUT_FIELD_NUMBER: _ClassVar[int]
    MOSAIC_LAYOUT_FIELD_NUMBER: _ClassVar[int]
    ROW_LAYOUT_FIELD_NUMBER: _ClassVar[int]
    COLUMN_LAYOUT_FIELD_NUMBER: _ClassVar[int]
    DASHBOARD_FILTERS_FIELD_NUMBER: _ClassVar[int]
    LABELS_FIELD_NUMBER: _ClassVar[int]
    name: str
    display_name: str
    etag: str
    grid_layout: _layouts_pb2.GridLayout
    mosaic_layout: _layouts_pb2.MosaicLayout
    row_layout: _layouts_pb2.RowLayout
    column_layout: _layouts_pb2.ColumnLayout
    dashboard_filters: _containers.RepeatedCompositeFieldContainer[_dashboard_filter_pb2.DashboardFilter]
    labels: _containers.ScalarMap[str, str]

    def __init__(self, name: _Optional[str]=..., display_name: _Optional[str]=..., etag: _Optional[str]=..., grid_layout: _Optional[_Union[_layouts_pb2.GridLayout, _Mapping]]=..., mosaic_layout: _Optional[_Union[_layouts_pb2.MosaicLayout, _Mapping]]=..., row_layout: _Optional[_Union[_layouts_pb2.RowLayout, _Mapping]]=..., column_layout: _Optional[_Union[_layouts_pb2.ColumnLayout, _Mapping]]=..., dashboard_filters: _Optional[_Iterable[_Union[_dashboard_filter_pb2.DashboardFilter, _Mapping]]]=..., labels: _Optional[_Mapping[str, str]]=...) -> None:
        ...