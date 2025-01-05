from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar
DESCRIPTOR: _descriptor.FileDescriptor

class CompanyTypeEnum(_message.Message):
    __slots__ = ()

    class CompanyType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        COMPANY_TYPE_UNSPECIFIED: _ClassVar[CompanyTypeEnum.CompanyType]
        ADVERTISER: _ClassVar[CompanyTypeEnum.CompanyType]
        HOUSE_ADVERTISER: _ClassVar[CompanyTypeEnum.CompanyType]
        AGENCY: _ClassVar[CompanyTypeEnum.CompanyType]
        HOUSE_AGENCY: _ClassVar[CompanyTypeEnum.CompanyType]
        AD_NETWORK: _ClassVar[CompanyTypeEnum.CompanyType]
    COMPANY_TYPE_UNSPECIFIED: CompanyTypeEnum.CompanyType
    ADVERTISER: CompanyTypeEnum.CompanyType
    HOUSE_ADVERTISER: CompanyTypeEnum.CompanyType
    AGENCY: CompanyTypeEnum.CompanyType
    HOUSE_AGENCY: CompanyTypeEnum.CompanyType
    AD_NETWORK: CompanyTypeEnum.CompanyType

    def __init__(self) -> None:
        ...