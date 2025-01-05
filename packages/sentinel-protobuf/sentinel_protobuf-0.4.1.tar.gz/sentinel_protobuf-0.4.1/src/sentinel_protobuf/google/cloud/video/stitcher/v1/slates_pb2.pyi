from google.api import field_behavior_pb2 as _field_behavior_pb2
from google.api import resource_pb2 as _resource_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Mapping as _Mapping, Optional as _Optional, Union as _Union
DESCRIPTOR: _descriptor.FileDescriptor

class Slate(_message.Message):
    __slots__ = ('name', 'uri', 'gam_slate')

    class GamSlate(_message.Message):
        __slots__ = ('network_code', 'gam_slate_id')
        NETWORK_CODE_FIELD_NUMBER: _ClassVar[int]
        GAM_SLATE_ID_FIELD_NUMBER: _ClassVar[int]
        network_code: str
        gam_slate_id: int

        def __init__(self, network_code: _Optional[str]=..., gam_slate_id: _Optional[int]=...) -> None:
            ...
    NAME_FIELD_NUMBER: _ClassVar[int]
    URI_FIELD_NUMBER: _ClassVar[int]
    GAM_SLATE_FIELD_NUMBER: _ClassVar[int]
    name: str
    uri: str
    gam_slate: Slate.GamSlate

    def __init__(self, name: _Optional[str]=..., uri: _Optional[str]=..., gam_slate: _Optional[_Union[Slate.GamSlate, _Mapping]]=...) -> None:
        ...