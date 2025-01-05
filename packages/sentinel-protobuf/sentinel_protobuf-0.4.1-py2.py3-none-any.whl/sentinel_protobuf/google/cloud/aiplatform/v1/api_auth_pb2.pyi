from google.api import field_behavior_pb2 as _field_behavior_pb2
from google.api import resource_pb2 as _resource_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Mapping as _Mapping, Optional as _Optional, Union as _Union
DESCRIPTOR: _descriptor.FileDescriptor

class ApiAuth(_message.Message):
    __slots__ = ('api_key_config',)

    class ApiKeyConfig(_message.Message):
        __slots__ = ('api_key_secret_version',)
        API_KEY_SECRET_VERSION_FIELD_NUMBER: _ClassVar[int]
        api_key_secret_version: str

        def __init__(self, api_key_secret_version: _Optional[str]=...) -> None:
            ...
    API_KEY_CONFIG_FIELD_NUMBER: _ClassVar[int]
    api_key_config: ApiAuth.ApiKeyConfig

    def __init__(self, api_key_config: _Optional[_Union[ApiAuth.ApiKeyConfig, _Mapping]]=...) -> None:
        ...