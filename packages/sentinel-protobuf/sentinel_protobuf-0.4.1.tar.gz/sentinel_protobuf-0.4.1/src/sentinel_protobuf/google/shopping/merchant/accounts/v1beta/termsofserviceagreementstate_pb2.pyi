from google.api import annotations_pb2 as _annotations_pb2
from google.api import client_pb2 as _client_pb2
from google.api import field_behavior_pb2 as _field_behavior_pb2
from google.api import resource_pb2 as _resource_pb2
from google.shopping.merchant.accounts.v1beta import termsofservicekind_pb2 as _termsofservicekind_pb2
from google.type import date_pb2 as _date_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class TermsOfServiceAgreementState(_message.Message):
    __slots__ = ("name", "region_code", "terms_of_service_kind", "accepted", "required")
    NAME_FIELD_NUMBER: _ClassVar[int]
    REGION_CODE_FIELD_NUMBER: _ClassVar[int]
    TERMS_OF_SERVICE_KIND_FIELD_NUMBER: _ClassVar[int]
    ACCEPTED_FIELD_NUMBER: _ClassVar[int]
    REQUIRED_FIELD_NUMBER: _ClassVar[int]
    name: str
    region_code: str
    terms_of_service_kind: _termsofservicekind_pb2.TermsOfServiceKind
    accepted: Accepted
    required: Required
    def __init__(self, name: _Optional[str] = ..., region_code: _Optional[str] = ..., terms_of_service_kind: _Optional[_Union[_termsofservicekind_pb2.TermsOfServiceKind, str]] = ..., accepted: _Optional[_Union[Accepted, _Mapping]] = ..., required: _Optional[_Union[Required, _Mapping]] = ...) -> None: ...

class Accepted(_message.Message):
    __slots__ = ("terms_of_service", "accepted_by", "valid_until")
    TERMS_OF_SERVICE_FIELD_NUMBER: _ClassVar[int]
    ACCEPTED_BY_FIELD_NUMBER: _ClassVar[int]
    VALID_UNTIL_FIELD_NUMBER: _ClassVar[int]
    terms_of_service: str
    accepted_by: str
    valid_until: _date_pb2.Date
    def __init__(self, terms_of_service: _Optional[str] = ..., accepted_by: _Optional[str] = ..., valid_until: _Optional[_Union[_date_pb2.Date, _Mapping]] = ...) -> None: ...

class Required(_message.Message):
    __slots__ = ("terms_of_service", "tos_file_uri")
    TERMS_OF_SERVICE_FIELD_NUMBER: _ClassVar[int]
    TOS_FILE_URI_FIELD_NUMBER: _ClassVar[int]
    terms_of_service: str
    tos_file_uri: str
    def __init__(self, terms_of_service: _Optional[str] = ..., tos_file_uri: _Optional[str] = ...) -> None: ...

class GetTermsOfServiceAgreementStateRequest(_message.Message):
    __slots__ = ("name",)
    NAME_FIELD_NUMBER: _ClassVar[int]
    name: str
    def __init__(self, name: _Optional[str] = ...) -> None: ...

class RetrieveForApplicationTermsOfServiceAgreementStateRequest(_message.Message):
    __slots__ = ("parent",)
    PARENT_FIELD_NUMBER: _ClassVar[int]
    parent: str
    def __init__(self, parent: _Optional[str] = ...) -> None: ...
