from google.api import field_behavior_pb2 as _field_behavior_pb2
from google.api import resource_pb2 as _resource_pb2
from google.protobuf import field_mask_pb2 as _field_mask_pb2
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Mapping as _Mapping, Optional as _Optional, Union as _Union
DESCRIPTOR: _descriptor.FileDescriptor

class VPCSCConfig(_message.Message):
    __slots__ = ('name', 'vpcsc_policy')

    class VPCSCPolicy(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        VPCSC_POLICY_UNSPECIFIED: _ClassVar[VPCSCConfig.VPCSCPolicy]
        DENY: _ClassVar[VPCSCConfig.VPCSCPolicy]
        ALLOW: _ClassVar[VPCSCConfig.VPCSCPolicy]
    VPCSC_POLICY_UNSPECIFIED: VPCSCConfig.VPCSCPolicy
    DENY: VPCSCConfig.VPCSCPolicy
    ALLOW: VPCSCConfig.VPCSCPolicy
    NAME_FIELD_NUMBER: _ClassVar[int]
    VPCSC_POLICY_FIELD_NUMBER: _ClassVar[int]
    name: str
    vpcsc_policy: VPCSCConfig.VPCSCPolicy

    def __init__(self, name: _Optional[str]=..., vpcsc_policy: _Optional[_Union[VPCSCConfig.VPCSCPolicy, str]]=...) -> None:
        ...

class GetVPCSCConfigRequest(_message.Message):
    __slots__ = ('name',)
    NAME_FIELD_NUMBER: _ClassVar[int]
    name: str

    def __init__(self, name: _Optional[str]=...) -> None:
        ...

class UpdateVPCSCConfigRequest(_message.Message):
    __slots__ = ('vpcsc_config', 'update_mask')
    VPCSC_CONFIG_FIELD_NUMBER: _ClassVar[int]
    UPDATE_MASK_FIELD_NUMBER: _ClassVar[int]
    vpcsc_config: VPCSCConfig
    update_mask: _field_mask_pb2.FieldMask

    def __init__(self, vpcsc_config: _Optional[_Union[VPCSCConfig, _Mapping]]=..., update_mask: _Optional[_Union[_field_mask_pb2.FieldMask, _Mapping]]=...) -> None:
        ...