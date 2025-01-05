from google.api import annotations_pb2 as _annotations_pb2
from google.api import client_pb2 as _client_pb2
from google.api import field_behavior_pb2 as _field_behavior_pb2
from google.api import resource_pb2 as _resource_pb2
from google.monitoring.v3 import uptime_pb2 as _uptime_pb2
from google.protobuf import empty_pb2 as _empty_pb2
from google.protobuf import field_mask_pb2 as _field_mask_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union
DESCRIPTOR: _descriptor.FileDescriptor

class ListUptimeCheckConfigsRequest(_message.Message):
    __slots__ = ('parent', 'filter', 'page_size', 'page_token')
    PARENT_FIELD_NUMBER: _ClassVar[int]
    FILTER_FIELD_NUMBER: _ClassVar[int]
    PAGE_SIZE_FIELD_NUMBER: _ClassVar[int]
    PAGE_TOKEN_FIELD_NUMBER: _ClassVar[int]
    parent: str
    filter: str
    page_size: int
    page_token: str

    def __init__(self, parent: _Optional[str]=..., filter: _Optional[str]=..., page_size: _Optional[int]=..., page_token: _Optional[str]=...) -> None:
        ...

class ListUptimeCheckConfigsResponse(_message.Message):
    __slots__ = ('uptime_check_configs', 'next_page_token', 'total_size')
    UPTIME_CHECK_CONFIGS_FIELD_NUMBER: _ClassVar[int]
    NEXT_PAGE_TOKEN_FIELD_NUMBER: _ClassVar[int]
    TOTAL_SIZE_FIELD_NUMBER: _ClassVar[int]
    uptime_check_configs: _containers.RepeatedCompositeFieldContainer[_uptime_pb2.UptimeCheckConfig]
    next_page_token: str
    total_size: int

    def __init__(self, uptime_check_configs: _Optional[_Iterable[_Union[_uptime_pb2.UptimeCheckConfig, _Mapping]]]=..., next_page_token: _Optional[str]=..., total_size: _Optional[int]=...) -> None:
        ...

class GetUptimeCheckConfigRequest(_message.Message):
    __slots__ = ('name',)
    NAME_FIELD_NUMBER: _ClassVar[int]
    name: str

    def __init__(self, name: _Optional[str]=...) -> None:
        ...

class CreateUptimeCheckConfigRequest(_message.Message):
    __slots__ = ('parent', 'uptime_check_config')
    PARENT_FIELD_NUMBER: _ClassVar[int]
    UPTIME_CHECK_CONFIG_FIELD_NUMBER: _ClassVar[int]
    parent: str
    uptime_check_config: _uptime_pb2.UptimeCheckConfig

    def __init__(self, parent: _Optional[str]=..., uptime_check_config: _Optional[_Union[_uptime_pb2.UptimeCheckConfig, _Mapping]]=...) -> None:
        ...

class UpdateUptimeCheckConfigRequest(_message.Message):
    __slots__ = ('update_mask', 'uptime_check_config')
    UPDATE_MASK_FIELD_NUMBER: _ClassVar[int]
    UPTIME_CHECK_CONFIG_FIELD_NUMBER: _ClassVar[int]
    update_mask: _field_mask_pb2.FieldMask
    uptime_check_config: _uptime_pb2.UptimeCheckConfig

    def __init__(self, update_mask: _Optional[_Union[_field_mask_pb2.FieldMask, _Mapping]]=..., uptime_check_config: _Optional[_Union[_uptime_pb2.UptimeCheckConfig, _Mapping]]=...) -> None:
        ...

class DeleteUptimeCheckConfigRequest(_message.Message):
    __slots__ = ('name',)
    NAME_FIELD_NUMBER: _ClassVar[int]
    name: str

    def __init__(self, name: _Optional[str]=...) -> None:
        ...

class ListUptimeCheckIpsRequest(_message.Message):
    __slots__ = ('page_size', 'page_token')
    PAGE_SIZE_FIELD_NUMBER: _ClassVar[int]
    PAGE_TOKEN_FIELD_NUMBER: _ClassVar[int]
    page_size: int
    page_token: str

    def __init__(self, page_size: _Optional[int]=..., page_token: _Optional[str]=...) -> None:
        ...

class ListUptimeCheckIpsResponse(_message.Message):
    __slots__ = ('uptime_check_ips', 'next_page_token')
    UPTIME_CHECK_IPS_FIELD_NUMBER: _ClassVar[int]
    NEXT_PAGE_TOKEN_FIELD_NUMBER: _ClassVar[int]
    uptime_check_ips: _containers.RepeatedCompositeFieldContainer[_uptime_pb2.UptimeCheckIp]
    next_page_token: str

    def __init__(self, uptime_check_ips: _Optional[_Iterable[_Union[_uptime_pb2.UptimeCheckIp, _Mapping]]]=..., next_page_token: _Optional[str]=...) -> None:
        ...