from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union
DESCRIPTOR: _descriptor.FileDescriptor

class AuditData(_message.Message):
    __slots__ = ('permission_delta',)

    class PermissionDelta(_message.Message):
        __slots__ = ('added_permissions', 'removed_permissions')
        ADDED_PERMISSIONS_FIELD_NUMBER: _ClassVar[int]
        REMOVED_PERMISSIONS_FIELD_NUMBER: _ClassVar[int]
        added_permissions: _containers.RepeatedScalarFieldContainer[str]
        removed_permissions: _containers.RepeatedScalarFieldContainer[str]

        def __init__(self, added_permissions: _Optional[_Iterable[str]]=..., removed_permissions: _Optional[_Iterable[str]]=...) -> None:
            ...
    PERMISSION_DELTA_FIELD_NUMBER: _ClassVar[int]
    permission_delta: AuditData.PermissionDelta

    def __init__(self, permission_delta: _Optional[_Union[AuditData.PermissionDelta, _Mapping]]=...) -> None:
        ...