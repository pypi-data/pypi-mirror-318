from google.ads.googleads.v18.enums import access_role_pb2 as _access_role_pb2
from google.ads.googleads.v18.enums import response_content_type_pb2 as _response_content_type_pb2
from google.ads.googleads.v18.resources import customer_pb2 as _customer_pb2
from google.api import annotations_pb2 as _annotations_pb2
from google.api import client_pb2 as _client_pb2
from google.api import field_behavior_pb2 as _field_behavior_pb2
from google.api import resource_pb2 as _resource_pb2
from google.protobuf import field_mask_pb2 as _field_mask_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class MutateCustomerRequest(_message.Message):
    __slots__ = ("customer_id", "operation", "validate_only", "response_content_type")
    CUSTOMER_ID_FIELD_NUMBER: _ClassVar[int]
    OPERATION_FIELD_NUMBER: _ClassVar[int]
    VALIDATE_ONLY_FIELD_NUMBER: _ClassVar[int]
    RESPONSE_CONTENT_TYPE_FIELD_NUMBER: _ClassVar[int]
    customer_id: str
    operation: CustomerOperation
    validate_only: bool
    response_content_type: _response_content_type_pb2.ResponseContentTypeEnum.ResponseContentType
    def __init__(self, customer_id: _Optional[str] = ..., operation: _Optional[_Union[CustomerOperation, _Mapping]] = ..., validate_only: bool = ..., response_content_type: _Optional[_Union[_response_content_type_pb2.ResponseContentTypeEnum.ResponseContentType, str]] = ...) -> None: ...

class CreateCustomerClientRequest(_message.Message):
    __slots__ = ("customer_id", "customer_client", "email_address", "access_role", "validate_only")
    CUSTOMER_ID_FIELD_NUMBER: _ClassVar[int]
    CUSTOMER_CLIENT_FIELD_NUMBER: _ClassVar[int]
    EMAIL_ADDRESS_FIELD_NUMBER: _ClassVar[int]
    ACCESS_ROLE_FIELD_NUMBER: _ClassVar[int]
    VALIDATE_ONLY_FIELD_NUMBER: _ClassVar[int]
    customer_id: str
    customer_client: _customer_pb2.Customer
    email_address: str
    access_role: _access_role_pb2.AccessRoleEnum.AccessRole
    validate_only: bool
    def __init__(self, customer_id: _Optional[str] = ..., customer_client: _Optional[_Union[_customer_pb2.Customer, _Mapping]] = ..., email_address: _Optional[str] = ..., access_role: _Optional[_Union[_access_role_pb2.AccessRoleEnum.AccessRole, str]] = ..., validate_only: bool = ...) -> None: ...

class CustomerOperation(_message.Message):
    __slots__ = ("update", "update_mask")
    UPDATE_FIELD_NUMBER: _ClassVar[int]
    UPDATE_MASK_FIELD_NUMBER: _ClassVar[int]
    update: _customer_pb2.Customer
    update_mask: _field_mask_pb2.FieldMask
    def __init__(self, update: _Optional[_Union[_customer_pb2.Customer, _Mapping]] = ..., update_mask: _Optional[_Union[_field_mask_pb2.FieldMask, _Mapping]] = ...) -> None: ...

class CreateCustomerClientResponse(_message.Message):
    __slots__ = ("resource_name", "invitation_link")
    RESOURCE_NAME_FIELD_NUMBER: _ClassVar[int]
    INVITATION_LINK_FIELD_NUMBER: _ClassVar[int]
    resource_name: str
    invitation_link: str
    def __init__(self, resource_name: _Optional[str] = ..., invitation_link: _Optional[str] = ...) -> None: ...

class MutateCustomerResponse(_message.Message):
    __slots__ = ("result",)
    RESULT_FIELD_NUMBER: _ClassVar[int]
    result: MutateCustomerResult
    def __init__(self, result: _Optional[_Union[MutateCustomerResult, _Mapping]] = ...) -> None: ...

class MutateCustomerResult(_message.Message):
    __slots__ = ("resource_name", "customer")
    RESOURCE_NAME_FIELD_NUMBER: _ClassVar[int]
    CUSTOMER_FIELD_NUMBER: _ClassVar[int]
    resource_name: str
    customer: _customer_pb2.Customer
    def __init__(self, resource_name: _Optional[str] = ..., customer: _Optional[_Union[_customer_pb2.Customer, _Mapping]] = ...) -> None: ...

class ListAccessibleCustomersRequest(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class ListAccessibleCustomersResponse(_message.Message):
    __slots__ = ("resource_names",)
    RESOURCE_NAMES_FIELD_NUMBER: _ClassVar[int]
    resource_names: _containers.RepeatedScalarFieldContainer[str]
    def __init__(self, resource_names: _Optional[_Iterable[str]] = ...) -> None: ...
