from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar
DESCRIPTOR: _descriptor.FileDescriptor

class AudienceScopeEnum(_message.Message):
    __slots__ = ()

    class AudienceScope(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        UNSPECIFIED: _ClassVar[AudienceScopeEnum.AudienceScope]
        UNKNOWN: _ClassVar[AudienceScopeEnum.AudienceScope]
        CUSTOMER: _ClassVar[AudienceScopeEnum.AudienceScope]
        ASSET_GROUP: _ClassVar[AudienceScopeEnum.AudienceScope]
    UNSPECIFIED: AudienceScopeEnum.AudienceScope
    UNKNOWN: AudienceScopeEnum.AudienceScope
    CUSTOMER: AudienceScopeEnum.AudienceScope
    ASSET_GROUP: AudienceScopeEnum.AudienceScope

    def __init__(self) -> None:
        ...