from google.protobuf import timestamp_pb2 as _timestamp_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union
DESCRIPTOR: _descriptor.FileDescriptor

class ManagementStatus(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    MANAGEMENT_STATUS_UNSPECIFIED: _ClassVar[ManagementStatus]
    OK: _ClassVar[ManagementStatus]
    PENDING: _ClassVar[ManagementStatus]
    FAILED_RETRYING_NOT_VISIBLE: _ClassVar[ManagementStatus]
    FAILED_PERMANENT: _ClassVar[ManagementStatus]
    FAILED_RETRYING_CAA_FORBIDDEN: _ClassVar[ManagementStatus]
    FAILED_RETRYING_CAA_CHECKING: _ClassVar[ManagementStatus]
MANAGEMENT_STATUS_UNSPECIFIED: ManagementStatus
OK: ManagementStatus
PENDING: ManagementStatus
FAILED_RETRYING_NOT_VISIBLE: ManagementStatus
FAILED_PERMANENT: ManagementStatus
FAILED_RETRYING_CAA_FORBIDDEN: ManagementStatus
FAILED_RETRYING_CAA_CHECKING: ManagementStatus

class AuthorizedCertificate(_message.Message):
    __slots__ = ('name', 'id', 'display_name', 'domain_names', 'expire_time', 'certificate_raw_data', 'managed_certificate', 'visible_domain_mappings', 'domain_mappings_count')
    NAME_FIELD_NUMBER: _ClassVar[int]
    ID_FIELD_NUMBER: _ClassVar[int]
    DISPLAY_NAME_FIELD_NUMBER: _ClassVar[int]
    DOMAIN_NAMES_FIELD_NUMBER: _ClassVar[int]
    EXPIRE_TIME_FIELD_NUMBER: _ClassVar[int]
    CERTIFICATE_RAW_DATA_FIELD_NUMBER: _ClassVar[int]
    MANAGED_CERTIFICATE_FIELD_NUMBER: _ClassVar[int]
    VISIBLE_DOMAIN_MAPPINGS_FIELD_NUMBER: _ClassVar[int]
    DOMAIN_MAPPINGS_COUNT_FIELD_NUMBER: _ClassVar[int]
    name: str
    id: str
    display_name: str
    domain_names: _containers.RepeatedScalarFieldContainer[str]
    expire_time: _timestamp_pb2.Timestamp
    certificate_raw_data: CertificateRawData
    managed_certificate: ManagedCertificate
    visible_domain_mappings: _containers.RepeatedScalarFieldContainer[str]
    domain_mappings_count: int

    def __init__(self, name: _Optional[str]=..., id: _Optional[str]=..., display_name: _Optional[str]=..., domain_names: _Optional[_Iterable[str]]=..., expire_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]]=..., certificate_raw_data: _Optional[_Union[CertificateRawData, _Mapping]]=..., managed_certificate: _Optional[_Union[ManagedCertificate, _Mapping]]=..., visible_domain_mappings: _Optional[_Iterable[str]]=..., domain_mappings_count: _Optional[int]=...) -> None:
        ...

class CertificateRawData(_message.Message):
    __slots__ = ('public_certificate', 'private_key')
    PUBLIC_CERTIFICATE_FIELD_NUMBER: _ClassVar[int]
    PRIVATE_KEY_FIELD_NUMBER: _ClassVar[int]
    public_certificate: str
    private_key: str

    def __init__(self, public_certificate: _Optional[str]=..., private_key: _Optional[str]=...) -> None:
        ...

class ManagedCertificate(_message.Message):
    __slots__ = ('last_renewal_time', 'status')
    LAST_RENEWAL_TIME_FIELD_NUMBER: _ClassVar[int]
    STATUS_FIELD_NUMBER: _ClassVar[int]
    last_renewal_time: _timestamp_pb2.Timestamp
    status: ManagementStatus

    def __init__(self, last_renewal_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]]=..., status: _Optional[_Union[ManagementStatus, str]]=...) -> None:
        ...