from google.ads.admanager.v1 import applied_label_pb2 as _applied_label_pb2
from google.ads.admanager.v1 import company_credit_status_enum_pb2 as _company_credit_status_enum_pb2
from google.ads.admanager.v1 import company_type_enum_pb2 as _company_type_enum_pb2
from google.api import field_behavior_pb2 as _field_behavior_pb2
from google.api import resource_pb2 as _resource_pb2
from google.protobuf import timestamp_pb2 as _timestamp_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class Company(_message.Message):
    __slots__ = ("name", "company_id", "display_name", "type", "address", "email", "fax", "phone", "external_id", "comment", "credit_status", "applied_labels", "primary_contact", "applied_teams", "update_time", "third_party_company_id")
    NAME_FIELD_NUMBER: _ClassVar[int]
    COMPANY_ID_FIELD_NUMBER: _ClassVar[int]
    DISPLAY_NAME_FIELD_NUMBER: _ClassVar[int]
    TYPE_FIELD_NUMBER: _ClassVar[int]
    ADDRESS_FIELD_NUMBER: _ClassVar[int]
    EMAIL_FIELD_NUMBER: _ClassVar[int]
    FAX_FIELD_NUMBER: _ClassVar[int]
    PHONE_FIELD_NUMBER: _ClassVar[int]
    EXTERNAL_ID_FIELD_NUMBER: _ClassVar[int]
    COMMENT_FIELD_NUMBER: _ClassVar[int]
    CREDIT_STATUS_FIELD_NUMBER: _ClassVar[int]
    APPLIED_LABELS_FIELD_NUMBER: _ClassVar[int]
    PRIMARY_CONTACT_FIELD_NUMBER: _ClassVar[int]
    APPLIED_TEAMS_FIELD_NUMBER: _ClassVar[int]
    UPDATE_TIME_FIELD_NUMBER: _ClassVar[int]
    THIRD_PARTY_COMPANY_ID_FIELD_NUMBER: _ClassVar[int]
    name: str
    company_id: int
    display_name: str
    type: _company_type_enum_pb2.CompanyTypeEnum.CompanyType
    address: str
    email: str
    fax: str
    phone: str
    external_id: str
    comment: str
    credit_status: _company_credit_status_enum_pb2.CompanyCreditStatusEnum.CompanyCreditStatus
    applied_labels: _containers.RepeatedCompositeFieldContainer[_applied_label_pb2.AppliedLabel]
    primary_contact: str
    applied_teams: _containers.RepeatedScalarFieldContainer[str]
    update_time: _timestamp_pb2.Timestamp
    third_party_company_id: int
    def __init__(self, name: _Optional[str] = ..., company_id: _Optional[int] = ..., display_name: _Optional[str] = ..., type: _Optional[_Union[_company_type_enum_pb2.CompanyTypeEnum.CompanyType, str]] = ..., address: _Optional[str] = ..., email: _Optional[str] = ..., fax: _Optional[str] = ..., phone: _Optional[str] = ..., external_id: _Optional[str] = ..., comment: _Optional[str] = ..., credit_status: _Optional[_Union[_company_credit_status_enum_pb2.CompanyCreditStatusEnum.CompanyCreditStatus, str]] = ..., applied_labels: _Optional[_Iterable[_Union[_applied_label_pb2.AppliedLabel, _Mapping]]] = ..., primary_contact: _Optional[str] = ..., applied_teams: _Optional[_Iterable[str]] = ..., update_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., third_party_company_id: _Optional[int] = ...) -> None: ...
