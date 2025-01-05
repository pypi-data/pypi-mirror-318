from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union
DESCRIPTOR: _descriptor.FileDescriptor

class DomainMapping(_message.Message):
    __slots__ = ('name', 'id', 'ssl_settings', 'resource_records')
    NAME_FIELD_NUMBER: _ClassVar[int]
    ID_FIELD_NUMBER: _ClassVar[int]
    SSL_SETTINGS_FIELD_NUMBER: _ClassVar[int]
    RESOURCE_RECORDS_FIELD_NUMBER: _ClassVar[int]
    name: str
    id: str
    ssl_settings: SslSettings
    resource_records: _containers.RepeatedCompositeFieldContainer[ResourceRecord]

    def __init__(self, name: _Optional[str]=..., id: _Optional[str]=..., ssl_settings: _Optional[_Union[SslSettings, _Mapping]]=..., resource_records: _Optional[_Iterable[_Union[ResourceRecord, _Mapping]]]=...) -> None:
        ...

class SslSettings(_message.Message):
    __slots__ = ('certificate_id', 'ssl_management_type', 'pending_managed_certificate_id')

    class SslManagementType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        SSL_MANAGEMENT_TYPE_UNSPECIFIED: _ClassVar[SslSettings.SslManagementType]
        AUTOMATIC: _ClassVar[SslSettings.SslManagementType]
        MANUAL: _ClassVar[SslSettings.SslManagementType]
    SSL_MANAGEMENT_TYPE_UNSPECIFIED: SslSettings.SslManagementType
    AUTOMATIC: SslSettings.SslManagementType
    MANUAL: SslSettings.SslManagementType
    CERTIFICATE_ID_FIELD_NUMBER: _ClassVar[int]
    SSL_MANAGEMENT_TYPE_FIELD_NUMBER: _ClassVar[int]
    PENDING_MANAGED_CERTIFICATE_ID_FIELD_NUMBER: _ClassVar[int]
    certificate_id: str
    ssl_management_type: SslSettings.SslManagementType
    pending_managed_certificate_id: str

    def __init__(self, certificate_id: _Optional[str]=..., ssl_management_type: _Optional[_Union[SslSettings.SslManagementType, str]]=..., pending_managed_certificate_id: _Optional[str]=...) -> None:
        ...

class ResourceRecord(_message.Message):
    __slots__ = ('name', 'rrdata', 'type')

    class RecordType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        RECORD_TYPE_UNSPECIFIED: _ClassVar[ResourceRecord.RecordType]
        A: _ClassVar[ResourceRecord.RecordType]
        AAAA: _ClassVar[ResourceRecord.RecordType]
        CNAME: _ClassVar[ResourceRecord.RecordType]
    RECORD_TYPE_UNSPECIFIED: ResourceRecord.RecordType
    A: ResourceRecord.RecordType
    AAAA: ResourceRecord.RecordType
    CNAME: ResourceRecord.RecordType
    NAME_FIELD_NUMBER: _ClassVar[int]
    RRDATA_FIELD_NUMBER: _ClassVar[int]
    TYPE_FIELD_NUMBER: _ClassVar[int]
    name: str
    rrdata: str
    type: ResourceRecord.RecordType

    def __init__(self, name: _Optional[str]=..., rrdata: _Optional[str]=..., type: _Optional[_Union[ResourceRecord.RecordType, str]]=...) -> None:
        ...