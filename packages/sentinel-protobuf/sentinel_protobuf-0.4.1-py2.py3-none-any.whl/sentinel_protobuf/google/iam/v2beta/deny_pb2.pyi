from google.type import expr_pb2 as _expr_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union
DESCRIPTOR: _descriptor.FileDescriptor

class DenyRule(_message.Message):
    __slots__ = ('denied_principals', 'exception_principals', 'denied_permissions', 'exception_permissions', 'denial_condition')
    DENIED_PRINCIPALS_FIELD_NUMBER: _ClassVar[int]
    EXCEPTION_PRINCIPALS_FIELD_NUMBER: _ClassVar[int]
    DENIED_PERMISSIONS_FIELD_NUMBER: _ClassVar[int]
    EXCEPTION_PERMISSIONS_FIELD_NUMBER: _ClassVar[int]
    DENIAL_CONDITION_FIELD_NUMBER: _ClassVar[int]
    denied_principals: _containers.RepeatedScalarFieldContainer[str]
    exception_principals: _containers.RepeatedScalarFieldContainer[str]
    denied_permissions: _containers.RepeatedScalarFieldContainer[str]
    exception_permissions: _containers.RepeatedScalarFieldContainer[str]
    denial_condition: _expr_pb2.Expr

    def __init__(self, denied_principals: _Optional[_Iterable[str]]=..., exception_principals: _Optional[_Iterable[str]]=..., denied_permissions: _Optional[_Iterable[str]]=..., exception_permissions: _Optional[_Iterable[str]]=..., denial_condition: _Optional[_Union[_expr_pb2.Expr, _Mapping]]=...) -> None:
        ...