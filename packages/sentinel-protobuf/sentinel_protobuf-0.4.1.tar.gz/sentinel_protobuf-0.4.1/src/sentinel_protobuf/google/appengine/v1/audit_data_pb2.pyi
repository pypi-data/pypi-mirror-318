from google.appengine.v1 import appengine_pb2 as _appengine_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Mapping as _Mapping, Optional as _Optional, Union as _Union
DESCRIPTOR: _descriptor.FileDescriptor

class AuditData(_message.Message):
    __slots__ = ('update_service', 'create_version')
    UPDATE_SERVICE_FIELD_NUMBER: _ClassVar[int]
    CREATE_VERSION_FIELD_NUMBER: _ClassVar[int]
    update_service: UpdateServiceMethod
    create_version: CreateVersionMethod

    def __init__(self, update_service: _Optional[_Union[UpdateServiceMethod, _Mapping]]=..., create_version: _Optional[_Union[CreateVersionMethod, _Mapping]]=...) -> None:
        ...

class UpdateServiceMethod(_message.Message):
    __slots__ = ('request',)
    REQUEST_FIELD_NUMBER: _ClassVar[int]
    request: _appengine_pb2.UpdateServiceRequest

    def __init__(self, request: _Optional[_Union[_appengine_pb2.UpdateServiceRequest, _Mapping]]=...) -> None:
        ...

class CreateVersionMethod(_message.Message):
    __slots__ = ('request',)
    REQUEST_FIELD_NUMBER: _ClassVar[int]
    request: _appengine_pb2.CreateVersionRequest

    def __init__(self, request: _Optional[_Union[_appengine_pb2.CreateVersionRequest, _Mapping]]=...) -> None:
        ...