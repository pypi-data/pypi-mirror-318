from google.api import annotations_pb2 as _annotations_pb2
from google.api import client_pb2 as _client_pb2
from google.api import field_behavior_pb2 as _field_behavior_pb2
from google.api import resource_pb2 as _resource_pb2
from google.cloud.essentialcontacts.v1 import enums_pb2 as _enums_pb2
from google.protobuf import empty_pb2 as _empty_pb2
from google.protobuf import field_mask_pb2 as _field_mask_pb2
from google.protobuf import timestamp_pb2 as _timestamp_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union
DESCRIPTOR: _descriptor.FileDescriptor

class Contact(_message.Message):
    __slots__ = ('name', 'email', 'notification_category_subscriptions', 'language_tag', 'validation_state', 'validate_time')
    NAME_FIELD_NUMBER: _ClassVar[int]
    EMAIL_FIELD_NUMBER: _ClassVar[int]
    NOTIFICATION_CATEGORY_SUBSCRIPTIONS_FIELD_NUMBER: _ClassVar[int]
    LANGUAGE_TAG_FIELD_NUMBER: _ClassVar[int]
    VALIDATION_STATE_FIELD_NUMBER: _ClassVar[int]
    VALIDATE_TIME_FIELD_NUMBER: _ClassVar[int]
    name: str
    email: str
    notification_category_subscriptions: _containers.RepeatedScalarFieldContainer[_enums_pb2.NotificationCategory]
    language_tag: str
    validation_state: _enums_pb2.ValidationState
    validate_time: _timestamp_pb2.Timestamp

    def __init__(self, name: _Optional[str]=..., email: _Optional[str]=..., notification_category_subscriptions: _Optional[_Iterable[_Union[_enums_pb2.NotificationCategory, str]]]=..., language_tag: _Optional[str]=..., validation_state: _Optional[_Union[_enums_pb2.ValidationState, str]]=..., validate_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]]=...) -> None:
        ...

class ListContactsRequest(_message.Message):
    __slots__ = ('parent', 'page_size', 'page_token')
    PARENT_FIELD_NUMBER: _ClassVar[int]
    PAGE_SIZE_FIELD_NUMBER: _ClassVar[int]
    PAGE_TOKEN_FIELD_NUMBER: _ClassVar[int]
    parent: str
    page_size: int
    page_token: str

    def __init__(self, parent: _Optional[str]=..., page_size: _Optional[int]=..., page_token: _Optional[str]=...) -> None:
        ...

class ListContactsResponse(_message.Message):
    __slots__ = ('contacts', 'next_page_token')
    CONTACTS_FIELD_NUMBER: _ClassVar[int]
    NEXT_PAGE_TOKEN_FIELD_NUMBER: _ClassVar[int]
    contacts: _containers.RepeatedCompositeFieldContainer[Contact]
    next_page_token: str

    def __init__(self, contacts: _Optional[_Iterable[_Union[Contact, _Mapping]]]=..., next_page_token: _Optional[str]=...) -> None:
        ...

class GetContactRequest(_message.Message):
    __slots__ = ('name',)
    NAME_FIELD_NUMBER: _ClassVar[int]
    name: str

    def __init__(self, name: _Optional[str]=...) -> None:
        ...

class DeleteContactRequest(_message.Message):
    __slots__ = ('name',)
    NAME_FIELD_NUMBER: _ClassVar[int]
    name: str

    def __init__(self, name: _Optional[str]=...) -> None:
        ...

class CreateContactRequest(_message.Message):
    __slots__ = ('parent', 'contact')
    PARENT_FIELD_NUMBER: _ClassVar[int]
    CONTACT_FIELD_NUMBER: _ClassVar[int]
    parent: str
    contact: Contact

    def __init__(self, parent: _Optional[str]=..., contact: _Optional[_Union[Contact, _Mapping]]=...) -> None:
        ...

class UpdateContactRequest(_message.Message):
    __slots__ = ('contact', 'update_mask')
    CONTACT_FIELD_NUMBER: _ClassVar[int]
    UPDATE_MASK_FIELD_NUMBER: _ClassVar[int]
    contact: Contact
    update_mask: _field_mask_pb2.FieldMask

    def __init__(self, contact: _Optional[_Union[Contact, _Mapping]]=..., update_mask: _Optional[_Union[_field_mask_pb2.FieldMask, _Mapping]]=...) -> None:
        ...

class ComputeContactsRequest(_message.Message):
    __slots__ = ('parent', 'notification_categories', 'page_size', 'page_token')
    PARENT_FIELD_NUMBER: _ClassVar[int]
    NOTIFICATION_CATEGORIES_FIELD_NUMBER: _ClassVar[int]
    PAGE_SIZE_FIELD_NUMBER: _ClassVar[int]
    PAGE_TOKEN_FIELD_NUMBER: _ClassVar[int]
    parent: str
    notification_categories: _containers.RepeatedScalarFieldContainer[_enums_pb2.NotificationCategory]
    page_size: int
    page_token: str

    def __init__(self, parent: _Optional[str]=..., notification_categories: _Optional[_Iterable[_Union[_enums_pb2.NotificationCategory, str]]]=..., page_size: _Optional[int]=..., page_token: _Optional[str]=...) -> None:
        ...

class ComputeContactsResponse(_message.Message):
    __slots__ = ('contacts', 'next_page_token')
    CONTACTS_FIELD_NUMBER: _ClassVar[int]
    NEXT_PAGE_TOKEN_FIELD_NUMBER: _ClassVar[int]
    contacts: _containers.RepeatedCompositeFieldContainer[Contact]
    next_page_token: str

    def __init__(self, contacts: _Optional[_Iterable[_Union[Contact, _Mapping]]]=..., next_page_token: _Optional[str]=...) -> None:
        ...

class SendTestMessageRequest(_message.Message):
    __slots__ = ('contacts', 'resource', 'notification_category')
    CONTACTS_FIELD_NUMBER: _ClassVar[int]
    RESOURCE_FIELD_NUMBER: _ClassVar[int]
    NOTIFICATION_CATEGORY_FIELD_NUMBER: _ClassVar[int]
    contacts: _containers.RepeatedScalarFieldContainer[str]
    resource: str
    notification_category: _enums_pb2.NotificationCategory

    def __init__(self, contacts: _Optional[_Iterable[str]]=..., resource: _Optional[str]=..., notification_category: _Optional[_Union[_enums_pb2.NotificationCategory, str]]=...) -> None:
        ...