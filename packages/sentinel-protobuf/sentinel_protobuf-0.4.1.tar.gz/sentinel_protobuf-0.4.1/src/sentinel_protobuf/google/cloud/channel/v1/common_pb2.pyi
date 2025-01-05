from google.api import field_behavior_pb2 as _field_behavior_pb2
from google.protobuf import any_pb2 as _any_pb2
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Mapping as _Mapping, Optional as _Optional, Union as _Union
DESCRIPTOR: _descriptor.FileDescriptor

class EduData(_message.Message):
    __slots__ = ('institute_type', 'institute_size', 'website')

    class InstituteType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        INSTITUTE_TYPE_UNSPECIFIED: _ClassVar[EduData.InstituteType]
        K12: _ClassVar[EduData.InstituteType]
        UNIVERSITY: _ClassVar[EduData.InstituteType]
    INSTITUTE_TYPE_UNSPECIFIED: EduData.InstituteType
    K12: EduData.InstituteType
    UNIVERSITY: EduData.InstituteType

    class InstituteSize(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        INSTITUTE_SIZE_UNSPECIFIED: _ClassVar[EduData.InstituteSize]
        SIZE_1_100: _ClassVar[EduData.InstituteSize]
        SIZE_101_500: _ClassVar[EduData.InstituteSize]
        SIZE_501_1000: _ClassVar[EduData.InstituteSize]
        SIZE_1001_2000: _ClassVar[EduData.InstituteSize]
        SIZE_2001_5000: _ClassVar[EduData.InstituteSize]
        SIZE_5001_10000: _ClassVar[EduData.InstituteSize]
        SIZE_10001_OR_MORE: _ClassVar[EduData.InstituteSize]
    INSTITUTE_SIZE_UNSPECIFIED: EduData.InstituteSize
    SIZE_1_100: EduData.InstituteSize
    SIZE_101_500: EduData.InstituteSize
    SIZE_501_1000: EduData.InstituteSize
    SIZE_1001_2000: EduData.InstituteSize
    SIZE_2001_5000: EduData.InstituteSize
    SIZE_5001_10000: EduData.InstituteSize
    SIZE_10001_OR_MORE: EduData.InstituteSize
    INSTITUTE_TYPE_FIELD_NUMBER: _ClassVar[int]
    INSTITUTE_SIZE_FIELD_NUMBER: _ClassVar[int]
    WEBSITE_FIELD_NUMBER: _ClassVar[int]
    institute_type: EduData.InstituteType
    institute_size: EduData.InstituteSize
    website: str

    def __init__(self, institute_type: _Optional[_Union[EduData.InstituteType, str]]=..., institute_size: _Optional[_Union[EduData.InstituteSize, str]]=..., website: _Optional[str]=...) -> None:
        ...

class CloudIdentityInfo(_message.Message):
    __slots__ = ('customer_type', 'primary_domain', 'is_domain_verified', 'alternate_email', 'phone_number', 'language_code', 'admin_console_uri', 'edu_data')

    class CustomerType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        CUSTOMER_TYPE_UNSPECIFIED: _ClassVar[CloudIdentityInfo.CustomerType]
        DOMAIN: _ClassVar[CloudIdentityInfo.CustomerType]
        TEAM: _ClassVar[CloudIdentityInfo.CustomerType]
    CUSTOMER_TYPE_UNSPECIFIED: CloudIdentityInfo.CustomerType
    DOMAIN: CloudIdentityInfo.CustomerType
    TEAM: CloudIdentityInfo.CustomerType
    CUSTOMER_TYPE_FIELD_NUMBER: _ClassVar[int]
    PRIMARY_DOMAIN_FIELD_NUMBER: _ClassVar[int]
    IS_DOMAIN_VERIFIED_FIELD_NUMBER: _ClassVar[int]
    ALTERNATE_EMAIL_FIELD_NUMBER: _ClassVar[int]
    PHONE_NUMBER_FIELD_NUMBER: _ClassVar[int]
    LANGUAGE_CODE_FIELD_NUMBER: _ClassVar[int]
    ADMIN_CONSOLE_URI_FIELD_NUMBER: _ClassVar[int]
    EDU_DATA_FIELD_NUMBER: _ClassVar[int]
    customer_type: CloudIdentityInfo.CustomerType
    primary_domain: str
    is_domain_verified: bool
    alternate_email: str
    phone_number: str
    language_code: str
    admin_console_uri: str
    edu_data: EduData

    def __init__(self, customer_type: _Optional[_Union[CloudIdentityInfo.CustomerType, str]]=..., primary_domain: _Optional[str]=..., is_domain_verified: bool=..., alternate_email: _Optional[str]=..., phone_number: _Optional[str]=..., language_code: _Optional[str]=..., admin_console_uri: _Optional[str]=..., edu_data: _Optional[_Union[EduData, _Mapping]]=...) -> None:
        ...

class Value(_message.Message):
    __slots__ = ('int64_value', 'string_value', 'double_value', 'proto_value', 'bool_value')
    INT64_VALUE_FIELD_NUMBER: _ClassVar[int]
    STRING_VALUE_FIELD_NUMBER: _ClassVar[int]
    DOUBLE_VALUE_FIELD_NUMBER: _ClassVar[int]
    PROTO_VALUE_FIELD_NUMBER: _ClassVar[int]
    BOOL_VALUE_FIELD_NUMBER: _ClassVar[int]
    int64_value: int
    string_value: str
    double_value: float
    proto_value: _any_pb2.Any
    bool_value: bool

    def __init__(self, int64_value: _Optional[int]=..., string_value: _Optional[str]=..., double_value: _Optional[float]=..., proto_value: _Optional[_Union[_any_pb2.Any, _Mapping]]=..., bool_value: bool=...) -> None:
        ...

class AdminUser(_message.Message):
    __slots__ = ('email', 'given_name', 'family_name')
    EMAIL_FIELD_NUMBER: _ClassVar[int]
    GIVEN_NAME_FIELD_NUMBER: _ClassVar[int]
    FAMILY_NAME_FIELD_NUMBER: _ClassVar[int]
    email: str
    given_name: str
    family_name: str

    def __init__(self, email: _Optional[str]=..., given_name: _Optional[str]=..., family_name: _Optional[str]=...) -> None:
        ...