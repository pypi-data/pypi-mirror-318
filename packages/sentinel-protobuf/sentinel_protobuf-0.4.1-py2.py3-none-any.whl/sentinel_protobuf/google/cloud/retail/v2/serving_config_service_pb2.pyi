from google.api import annotations_pb2 as _annotations_pb2
from google.api import client_pb2 as _client_pb2
from google.api import field_behavior_pb2 as _field_behavior_pb2
from google.api import resource_pb2 as _resource_pb2
from google.cloud.retail.v2 import serving_config_pb2 as _serving_config_pb2
from google.protobuf import empty_pb2 as _empty_pb2
from google.protobuf import field_mask_pb2 as _field_mask_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class CreateServingConfigRequest(_message.Message):
    __slots__ = ("parent", "serving_config", "serving_config_id")
    PARENT_FIELD_NUMBER: _ClassVar[int]
    SERVING_CONFIG_FIELD_NUMBER: _ClassVar[int]
    SERVING_CONFIG_ID_FIELD_NUMBER: _ClassVar[int]
    parent: str
    serving_config: _serving_config_pb2.ServingConfig
    serving_config_id: str
    def __init__(self, parent: _Optional[str] = ..., serving_config: _Optional[_Union[_serving_config_pb2.ServingConfig, _Mapping]] = ..., serving_config_id: _Optional[str] = ...) -> None: ...

class UpdateServingConfigRequest(_message.Message):
    __slots__ = ("serving_config", "update_mask")
    SERVING_CONFIG_FIELD_NUMBER: _ClassVar[int]
    UPDATE_MASK_FIELD_NUMBER: _ClassVar[int]
    serving_config: _serving_config_pb2.ServingConfig
    update_mask: _field_mask_pb2.FieldMask
    def __init__(self, serving_config: _Optional[_Union[_serving_config_pb2.ServingConfig, _Mapping]] = ..., update_mask: _Optional[_Union[_field_mask_pb2.FieldMask, _Mapping]] = ...) -> None: ...

class DeleteServingConfigRequest(_message.Message):
    __slots__ = ("name",)
    NAME_FIELD_NUMBER: _ClassVar[int]
    name: str
    def __init__(self, name: _Optional[str] = ...) -> None: ...

class GetServingConfigRequest(_message.Message):
    __slots__ = ("name",)
    NAME_FIELD_NUMBER: _ClassVar[int]
    name: str
    def __init__(self, name: _Optional[str] = ...) -> None: ...

class ListServingConfigsRequest(_message.Message):
    __slots__ = ("parent", "page_size", "page_token")
    PARENT_FIELD_NUMBER: _ClassVar[int]
    PAGE_SIZE_FIELD_NUMBER: _ClassVar[int]
    PAGE_TOKEN_FIELD_NUMBER: _ClassVar[int]
    parent: str
    page_size: int
    page_token: str
    def __init__(self, parent: _Optional[str] = ..., page_size: _Optional[int] = ..., page_token: _Optional[str] = ...) -> None: ...

class ListServingConfigsResponse(_message.Message):
    __slots__ = ("serving_configs", "next_page_token")
    SERVING_CONFIGS_FIELD_NUMBER: _ClassVar[int]
    NEXT_PAGE_TOKEN_FIELD_NUMBER: _ClassVar[int]
    serving_configs: _containers.RepeatedCompositeFieldContainer[_serving_config_pb2.ServingConfig]
    next_page_token: str
    def __init__(self, serving_configs: _Optional[_Iterable[_Union[_serving_config_pb2.ServingConfig, _Mapping]]] = ..., next_page_token: _Optional[str] = ...) -> None: ...

class AddControlRequest(_message.Message):
    __slots__ = ("serving_config", "control_id")
    SERVING_CONFIG_FIELD_NUMBER: _ClassVar[int]
    CONTROL_ID_FIELD_NUMBER: _ClassVar[int]
    serving_config: str
    control_id: str
    def __init__(self, serving_config: _Optional[str] = ..., control_id: _Optional[str] = ...) -> None: ...

class RemoveControlRequest(_message.Message):
    __slots__ = ("serving_config", "control_id")
    SERVING_CONFIG_FIELD_NUMBER: _ClassVar[int]
    CONTROL_ID_FIELD_NUMBER: _ClassVar[int]
    serving_config: str
    control_id: str
    def __init__(self, serving_config: _Optional[str] = ..., control_id: _Optional[str] = ...) -> None: ...
