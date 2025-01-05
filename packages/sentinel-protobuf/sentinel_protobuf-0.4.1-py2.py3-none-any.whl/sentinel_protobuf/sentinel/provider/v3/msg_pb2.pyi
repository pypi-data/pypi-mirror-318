from gogoproto import gogo_pb2 as _gogo_pb2
from sentinel.provider.v2 import params_pb2 as _params_pb2
from sentinel.types.v1 import status_pb2 as _status_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Mapping as _Mapping, Optional as _Optional, Union as _Union
DESCRIPTOR: _descriptor.FileDescriptor

class MsgRegisterProviderRequest(_message.Message):
    __slots__ = ('name', 'identity', 'website', 'description')
    FROM_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    IDENTITY_FIELD_NUMBER: _ClassVar[int]
    WEBSITE_FIELD_NUMBER: _ClassVar[int]
    DESCRIPTION_FIELD_NUMBER: _ClassVar[int]
    name: str
    identity: str
    website: str
    description: str

    def __init__(self, name: _Optional[str]=..., identity: _Optional[str]=..., website: _Optional[str]=..., description: _Optional[str]=..., **kwargs) -> None:
        ...

class MsgUpdateProviderDetailsRequest(_message.Message):
    __slots__ = ('name', 'identity', 'website', 'description')
    FROM_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    IDENTITY_FIELD_NUMBER: _ClassVar[int]
    WEBSITE_FIELD_NUMBER: _ClassVar[int]
    DESCRIPTION_FIELD_NUMBER: _ClassVar[int]
    name: str
    identity: str
    website: str
    description: str

    def __init__(self, name: _Optional[str]=..., identity: _Optional[str]=..., website: _Optional[str]=..., description: _Optional[str]=..., **kwargs) -> None:
        ...

class MsgUpdateProviderStatusRequest(_message.Message):
    __slots__ = ('status',)
    FROM_FIELD_NUMBER: _ClassVar[int]
    STATUS_FIELD_NUMBER: _ClassVar[int]
    status: _status_pb2.Status

    def __init__(self, status: _Optional[_Union[_status_pb2.Status, str]]=..., **kwargs) -> None:
        ...

class MsgUpdateParamsRequest(_message.Message):
    __slots__ = ('params',)
    FROM_FIELD_NUMBER: _ClassVar[int]
    PARAMS_FIELD_NUMBER: _ClassVar[int]
    params: _params_pb2.Params

    def __init__(self, params: _Optional[_Union[_params_pb2.Params, _Mapping]]=..., **kwargs) -> None:
        ...

class MsgRegisterProviderResponse(_message.Message):
    __slots__ = ()

    def __init__(self) -> None:
        ...

class MsgUpdateProviderDetailsResponse(_message.Message):
    __slots__ = ()

    def __init__(self) -> None:
        ...

class MsgUpdateProviderStatusResponse(_message.Message):
    __slots__ = ()

    def __init__(self) -> None:
        ...

class MsgUpdateParamsResponse(_message.Message):
    __slots__ = ()

    def __init__(self) -> None:
        ...