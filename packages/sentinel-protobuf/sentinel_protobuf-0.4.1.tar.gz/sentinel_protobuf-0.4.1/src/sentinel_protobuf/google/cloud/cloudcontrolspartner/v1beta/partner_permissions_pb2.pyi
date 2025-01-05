from google.api import field_behavior_pb2 as _field_behavior_pb2
from google.api import resource_pb2 as _resource_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Optional as _Optional, Union as _Union
DESCRIPTOR: _descriptor.FileDescriptor

class PartnerPermissions(_message.Message):
    __slots__ = ('name', 'partner_permissions')

    class Permission(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        PERMISSION_UNSPECIFIED: _ClassVar[PartnerPermissions.Permission]
        ACCESS_TRANSPARENCY_AND_EMERGENCY_ACCESS_LOGS: _ClassVar[PartnerPermissions.Permission]
        ASSURED_WORKLOADS_MONITORING: _ClassVar[PartnerPermissions.Permission]
        ACCESS_APPROVAL_REQUESTS: _ClassVar[PartnerPermissions.Permission]
        ASSURED_WORKLOADS_EKM_CONNECTION_STATUS: _ClassVar[PartnerPermissions.Permission]
        ACCESS_TRANSPARENCY_LOGS_SUPPORT_CASE_VIEWER: _ClassVar[PartnerPermissions.Permission]
    PERMISSION_UNSPECIFIED: PartnerPermissions.Permission
    ACCESS_TRANSPARENCY_AND_EMERGENCY_ACCESS_LOGS: PartnerPermissions.Permission
    ASSURED_WORKLOADS_MONITORING: PartnerPermissions.Permission
    ACCESS_APPROVAL_REQUESTS: PartnerPermissions.Permission
    ASSURED_WORKLOADS_EKM_CONNECTION_STATUS: PartnerPermissions.Permission
    ACCESS_TRANSPARENCY_LOGS_SUPPORT_CASE_VIEWER: PartnerPermissions.Permission
    NAME_FIELD_NUMBER: _ClassVar[int]
    PARTNER_PERMISSIONS_FIELD_NUMBER: _ClassVar[int]
    name: str
    partner_permissions: _containers.RepeatedScalarFieldContainer[PartnerPermissions.Permission]

    def __init__(self, name: _Optional[str]=..., partner_permissions: _Optional[_Iterable[_Union[PartnerPermissions.Permission, str]]]=...) -> None:
        ...

class GetPartnerPermissionsRequest(_message.Message):
    __slots__ = ('name',)
    NAME_FIELD_NUMBER: _ClassVar[int]
    name: str

    def __init__(self, name: _Optional[str]=...) -> None:
        ...