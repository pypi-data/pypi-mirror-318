from google.ads.googleads.v16.enums import local_services_lead_credit_state_pb2 as _local_services_lead_credit_state_pb2
from google.ads.googleads.v16.enums import local_services_lead_status_pb2 as _local_services_lead_status_pb2
from google.ads.googleads.v16.enums import local_services_lead_type_pb2 as _local_services_lead_type_pb2
from google.api import field_behavior_pb2 as _field_behavior_pb2
from google.api import resource_pb2 as _resource_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class LocalServicesLead(_message.Message):
    __slots__ = ("resource_name", "id", "category_id", "service_id", "contact_details", "lead_type", "lead_status", "creation_date_time", "locale", "note", "lead_charged", "credit_details")
    RESOURCE_NAME_FIELD_NUMBER: _ClassVar[int]
    ID_FIELD_NUMBER: _ClassVar[int]
    CATEGORY_ID_FIELD_NUMBER: _ClassVar[int]
    SERVICE_ID_FIELD_NUMBER: _ClassVar[int]
    CONTACT_DETAILS_FIELD_NUMBER: _ClassVar[int]
    LEAD_TYPE_FIELD_NUMBER: _ClassVar[int]
    LEAD_STATUS_FIELD_NUMBER: _ClassVar[int]
    CREATION_DATE_TIME_FIELD_NUMBER: _ClassVar[int]
    LOCALE_FIELD_NUMBER: _ClassVar[int]
    NOTE_FIELD_NUMBER: _ClassVar[int]
    LEAD_CHARGED_FIELD_NUMBER: _ClassVar[int]
    CREDIT_DETAILS_FIELD_NUMBER: _ClassVar[int]
    resource_name: str
    id: int
    category_id: str
    service_id: str
    contact_details: ContactDetails
    lead_type: _local_services_lead_type_pb2.LocalServicesLeadTypeEnum.LeadType
    lead_status: _local_services_lead_status_pb2.LocalServicesLeadStatusEnum.LeadStatus
    creation_date_time: str
    locale: str
    note: Note
    lead_charged: bool
    credit_details: CreditDetails
    def __init__(self, resource_name: _Optional[str] = ..., id: _Optional[int] = ..., category_id: _Optional[str] = ..., service_id: _Optional[str] = ..., contact_details: _Optional[_Union[ContactDetails, _Mapping]] = ..., lead_type: _Optional[_Union[_local_services_lead_type_pb2.LocalServicesLeadTypeEnum.LeadType, str]] = ..., lead_status: _Optional[_Union[_local_services_lead_status_pb2.LocalServicesLeadStatusEnum.LeadStatus, str]] = ..., creation_date_time: _Optional[str] = ..., locale: _Optional[str] = ..., note: _Optional[_Union[Note, _Mapping]] = ..., lead_charged: bool = ..., credit_details: _Optional[_Union[CreditDetails, _Mapping]] = ...) -> None: ...

class ContactDetails(_message.Message):
    __slots__ = ("phone_number", "email", "consumer_name")
    PHONE_NUMBER_FIELD_NUMBER: _ClassVar[int]
    EMAIL_FIELD_NUMBER: _ClassVar[int]
    CONSUMER_NAME_FIELD_NUMBER: _ClassVar[int]
    phone_number: str
    email: str
    consumer_name: str
    def __init__(self, phone_number: _Optional[str] = ..., email: _Optional[str] = ..., consumer_name: _Optional[str] = ...) -> None: ...

class Note(_message.Message):
    __slots__ = ("edit_date_time", "description")
    EDIT_DATE_TIME_FIELD_NUMBER: _ClassVar[int]
    DESCRIPTION_FIELD_NUMBER: _ClassVar[int]
    edit_date_time: str
    description: str
    def __init__(self, edit_date_time: _Optional[str] = ..., description: _Optional[str] = ...) -> None: ...

class CreditDetails(_message.Message):
    __slots__ = ("credit_state", "credit_state_last_update_date_time")
    CREDIT_STATE_FIELD_NUMBER: _ClassVar[int]
    CREDIT_STATE_LAST_UPDATE_DATE_TIME_FIELD_NUMBER: _ClassVar[int]
    credit_state: _local_services_lead_credit_state_pb2.LocalServicesCreditStateEnum.CreditState
    credit_state_last_update_date_time: str
    def __init__(self, credit_state: _Optional[_Union[_local_services_lead_credit_state_pb2.LocalServicesCreditStateEnum.CreditState, str]] = ..., credit_state_last_update_date_time: _Optional[str] = ...) -> None: ...
