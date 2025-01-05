from google.api import field_behavior_pb2 as _field_behavior_pb2
from google.api import resource_pb2 as _resource_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Mapping as _Mapping, Optional as _Optional, Union as _Union
DESCRIPTOR: _descriptor.FileDescriptor

class CdnKey(_message.Message):
    __slots__ = ('google_cdn_key', 'akamai_cdn_key', 'media_cdn_key', 'name', 'hostname')
    GOOGLE_CDN_KEY_FIELD_NUMBER: _ClassVar[int]
    AKAMAI_CDN_KEY_FIELD_NUMBER: _ClassVar[int]
    MEDIA_CDN_KEY_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    HOSTNAME_FIELD_NUMBER: _ClassVar[int]
    google_cdn_key: GoogleCdnKey
    akamai_cdn_key: AkamaiCdnKey
    media_cdn_key: MediaCdnKey
    name: str
    hostname: str

    def __init__(self, google_cdn_key: _Optional[_Union[GoogleCdnKey, _Mapping]]=..., akamai_cdn_key: _Optional[_Union[AkamaiCdnKey, _Mapping]]=..., media_cdn_key: _Optional[_Union[MediaCdnKey, _Mapping]]=..., name: _Optional[str]=..., hostname: _Optional[str]=...) -> None:
        ...

class GoogleCdnKey(_message.Message):
    __slots__ = ('private_key', 'key_name')
    PRIVATE_KEY_FIELD_NUMBER: _ClassVar[int]
    KEY_NAME_FIELD_NUMBER: _ClassVar[int]
    private_key: bytes
    key_name: str

    def __init__(self, private_key: _Optional[bytes]=..., key_name: _Optional[str]=...) -> None:
        ...

class AkamaiCdnKey(_message.Message):
    __slots__ = ('token_key',)
    TOKEN_KEY_FIELD_NUMBER: _ClassVar[int]
    token_key: bytes

    def __init__(self, token_key: _Optional[bytes]=...) -> None:
        ...

class MediaCdnKey(_message.Message):
    __slots__ = ('private_key', 'key_name', 'token_config')

    class TokenConfig(_message.Message):
        __slots__ = ('query_parameter',)
        QUERY_PARAMETER_FIELD_NUMBER: _ClassVar[int]
        query_parameter: str

        def __init__(self, query_parameter: _Optional[str]=...) -> None:
            ...
    PRIVATE_KEY_FIELD_NUMBER: _ClassVar[int]
    KEY_NAME_FIELD_NUMBER: _ClassVar[int]
    TOKEN_CONFIG_FIELD_NUMBER: _ClassVar[int]
    private_key: bytes
    key_name: str
    token_config: MediaCdnKey.TokenConfig

    def __init__(self, private_key: _Optional[bytes]=..., key_name: _Optional[str]=..., token_config: _Optional[_Union[MediaCdnKey.TokenConfig, _Mapping]]=...) -> None:
        ...