from google.api import field_behavior_pb2 as _field_behavior_pb2
from google.api import resource_pb2 as _resource_pb2
from google.cloud.channel.v1 import common_pb2 as _common_pb2
from google.protobuf import timestamp_pb2 as _timestamp_pb2
from google.type import postal_address_pb2 as _postal_address_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Mapping as _Mapping, Optional as _Optional, Union as _Union
DESCRIPTOR: _descriptor.FileDescriptor

class Customer(_message.Message):
    __slots__ = ('name', 'org_display_name', 'org_postal_address', 'primary_contact_info', 'alternate_email', 'domain', 'create_time', 'update_time', 'cloud_identity_id', 'language_code', 'cloud_identity_info', 'channel_partner_id', 'correlation_id')
    NAME_FIELD_NUMBER: _ClassVar[int]
    ORG_DISPLAY_NAME_FIELD_NUMBER: _ClassVar[int]
    ORG_POSTAL_ADDRESS_FIELD_NUMBER: _ClassVar[int]
    PRIMARY_CONTACT_INFO_FIELD_NUMBER: _ClassVar[int]
    ALTERNATE_EMAIL_FIELD_NUMBER: _ClassVar[int]
    DOMAIN_FIELD_NUMBER: _ClassVar[int]
    CREATE_TIME_FIELD_NUMBER: _ClassVar[int]
    UPDATE_TIME_FIELD_NUMBER: _ClassVar[int]
    CLOUD_IDENTITY_ID_FIELD_NUMBER: _ClassVar[int]
    LANGUAGE_CODE_FIELD_NUMBER: _ClassVar[int]
    CLOUD_IDENTITY_INFO_FIELD_NUMBER: _ClassVar[int]
    CHANNEL_PARTNER_ID_FIELD_NUMBER: _ClassVar[int]
    CORRELATION_ID_FIELD_NUMBER: _ClassVar[int]
    name: str
    org_display_name: str
    org_postal_address: _postal_address_pb2.PostalAddress
    primary_contact_info: ContactInfo
    alternate_email: str
    domain: str
    create_time: _timestamp_pb2.Timestamp
    update_time: _timestamp_pb2.Timestamp
    cloud_identity_id: str
    language_code: str
    cloud_identity_info: _common_pb2.CloudIdentityInfo
    channel_partner_id: str
    correlation_id: str

    def __init__(self, name: _Optional[str]=..., org_display_name: _Optional[str]=..., org_postal_address: _Optional[_Union[_postal_address_pb2.PostalAddress, _Mapping]]=..., primary_contact_info: _Optional[_Union[ContactInfo, _Mapping]]=..., alternate_email: _Optional[str]=..., domain: _Optional[str]=..., create_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]]=..., update_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]]=..., cloud_identity_id: _Optional[str]=..., language_code: _Optional[str]=..., cloud_identity_info: _Optional[_Union[_common_pb2.CloudIdentityInfo, _Mapping]]=..., channel_partner_id: _Optional[str]=..., correlation_id: _Optional[str]=...) -> None:
        ...

class ContactInfo(_message.Message):
    __slots__ = ('first_name', 'last_name', 'display_name', 'email', 'title', 'phone')
    FIRST_NAME_FIELD_NUMBER: _ClassVar[int]
    LAST_NAME_FIELD_NUMBER: _ClassVar[int]
    DISPLAY_NAME_FIELD_NUMBER: _ClassVar[int]
    EMAIL_FIELD_NUMBER: _ClassVar[int]
    TITLE_FIELD_NUMBER: _ClassVar[int]
    PHONE_FIELD_NUMBER: _ClassVar[int]
    first_name: str
    last_name: str
    display_name: str
    email: str
    title: str
    phone: str

    def __init__(self, first_name: _Optional[str]=..., last_name: _Optional[str]=..., display_name: _Optional[str]=..., email: _Optional[str]=..., title: _Optional[str]=..., phone: _Optional[str]=...) -> None:
        ...