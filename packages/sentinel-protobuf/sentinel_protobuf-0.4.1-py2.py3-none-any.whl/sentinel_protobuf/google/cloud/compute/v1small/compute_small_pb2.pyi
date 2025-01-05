from google.api import annotations_pb2 as _annotations_pb2
from google.api import client_pb2 as _client_pb2
from google.api import field_behavior_pb2 as _field_behavior_pb2
from google.api import resource_pb2 as _resource_pb2
from google.cloud import extended_operations_pb2 as _extended_operations_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class Address(_message.Message):
    __slots__ = ("address", "address_type", "creation_timestamp", "description", "id", "ip_version", "kind", "name", "network", "network_tier", "prefix_length", "purpose", "region", "self_link", "status", "subnetwork", "users")
    class AddressType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        UNDEFINED_ADDRESS_TYPE: _ClassVar[Address.AddressType]
        EXTERNAL: _ClassVar[Address.AddressType]
        INTERNAL: _ClassVar[Address.AddressType]
        UNSPECIFIED_TYPE: _ClassVar[Address.AddressType]
    UNDEFINED_ADDRESS_TYPE: Address.AddressType
    EXTERNAL: Address.AddressType
    INTERNAL: Address.AddressType
    UNSPECIFIED_TYPE: Address.AddressType
    class IpVersion(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        UNDEFINED_IP_VERSION: _ClassVar[Address.IpVersion]
        IPV4: _ClassVar[Address.IpVersion]
        IPV6: _ClassVar[Address.IpVersion]
        UNSPECIFIED_VERSION: _ClassVar[Address.IpVersion]
    UNDEFINED_IP_VERSION: Address.IpVersion
    IPV4: Address.IpVersion
    IPV6: Address.IpVersion
    UNSPECIFIED_VERSION: Address.IpVersion
    class NetworkTier(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        UNDEFINED_NETWORK_TIER: _ClassVar[Address.NetworkTier]
        PREMIUM: _ClassVar[Address.NetworkTier]
        STANDARD: _ClassVar[Address.NetworkTier]
    UNDEFINED_NETWORK_TIER: Address.NetworkTier
    PREMIUM: Address.NetworkTier
    STANDARD: Address.NetworkTier
    class Purpose(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        UNDEFINED_PURPOSE: _ClassVar[Address.Purpose]
        DNS_RESOLVER: _ClassVar[Address.Purpose]
        GCE_ENDPOINT: _ClassVar[Address.Purpose]
        NAT_AUTO: _ClassVar[Address.Purpose]
        VPC_PEERING: _ClassVar[Address.Purpose]
    UNDEFINED_PURPOSE: Address.Purpose
    DNS_RESOLVER: Address.Purpose
    GCE_ENDPOINT: Address.Purpose
    NAT_AUTO: Address.Purpose
    VPC_PEERING: Address.Purpose
    class Status(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        UNDEFINED_STATUS: _ClassVar[Address.Status]
        IN_USE: _ClassVar[Address.Status]
        RESERVED: _ClassVar[Address.Status]
        RESERVING: _ClassVar[Address.Status]
    UNDEFINED_STATUS: Address.Status
    IN_USE: Address.Status
    RESERVED: Address.Status
    RESERVING: Address.Status
    ADDRESS_FIELD_NUMBER: _ClassVar[int]
    ADDRESS_TYPE_FIELD_NUMBER: _ClassVar[int]
    CREATION_TIMESTAMP_FIELD_NUMBER: _ClassVar[int]
    DESCRIPTION_FIELD_NUMBER: _ClassVar[int]
    ID_FIELD_NUMBER: _ClassVar[int]
    IP_VERSION_FIELD_NUMBER: _ClassVar[int]
    KIND_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    NETWORK_FIELD_NUMBER: _ClassVar[int]
    NETWORK_TIER_FIELD_NUMBER: _ClassVar[int]
    PREFIX_LENGTH_FIELD_NUMBER: _ClassVar[int]
    PURPOSE_FIELD_NUMBER: _ClassVar[int]
    REGION_FIELD_NUMBER: _ClassVar[int]
    SELF_LINK_FIELD_NUMBER: _ClassVar[int]
    STATUS_FIELD_NUMBER: _ClassVar[int]
    SUBNETWORK_FIELD_NUMBER: _ClassVar[int]
    USERS_FIELD_NUMBER: _ClassVar[int]
    address: str
    address_type: str
    creation_timestamp: str
    description: str
    id: int
    ip_version: str
    kind: str
    name: str
    network: str
    network_tier: str
    prefix_length: int
    purpose: str
    region: str
    self_link: str
    status: str
    subnetwork: str
    users: _containers.RepeatedScalarFieldContainer[str]
    def __init__(self, address: _Optional[str] = ..., address_type: _Optional[str] = ..., creation_timestamp: _Optional[str] = ..., description: _Optional[str] = ..., id: _Optional[int] = ..., ip_version: _Optional[str] = ..., kind: _Optional[str] = ..., name: _Optional[str] = ..., network: _Optional[str] = ..., network_tier: _Optional[str] = ..., prefix_length: _Optional[int] = ..., purpose: _Optional[str] = ..., region: _Optional[str] = ..., self_link: _Optional[str] = ..., status: _Optional[str] = ..., subnetwork: _Optional[str] = ..., users: _Optional[_Iterable[str]] = ...) -> None: ...

class AddressAggregatedList(_message.Message):
    __slots__ = ("id", "items", "kind", "next_page_token", "self_link", "warning")
    class ItemsEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: AddressesScopedList
        def __init__(self, key: _Optional[str] = ..., value: _Optional[_Union[AddressesScopedList, _Mapping]] = ...) -> None: ...
    ID_FIELD_NUMBER: _ClassVar[int]
    ITEMS_FIELD_NUMBER: _ClassVar[int]
    KIND_FIELD_NUMBER: _ClassVar[int]
    NEXT_PAGE_TOKEN_FIELD_NUMBER: _ClassVar[int]
    SELF_LINK_FIELD_NUMBER: _ClassVar[int]
    WARNING_FIELD_NUMBER: _ClassVar[int]
    id: str
    items: _containers.MessageMap[str, AddressesScopedList]
    kind: str
    next_page_token: str
    self_link: str
    warning: Warning
    def __init__(self, id: _Optional[str] = ..., items: _Optional[_Mapping[str, AddressesScopedList]] = ..., kind: _Optional[str] = ..., next_page_token: _Optional[str] = ..., self_link: _Optional[str] = ..., warning: _Optional[_Union[Warning, _Mapping]] = ...) -> None: ...

class AddressList(_message.Message):
    __slots__ = ("id", "items", "kind", "next_page_token", "self_link", "warning")
    ID_FIELD_NUMBER: _ClassVar[int]
    ITEMS_FIELD_NUMBER: _ClassVar[int]
    KIND_FIELD_NUMBER: _ClassVar[int]
    NEXT_PAGE_TOKEN_FIELD_NUMBER: _ClassVar[int]
    SELF_LINK_FIELD_NUMBER: _ClassVar[int]
    WARNING_FIELD_NUMBER: _ClassVar[int]
    id: str
    items: _containers.RepeatedCompositeFieldContainer[Address]
    kind: str
    next_page_token: str
    self_link: str
    warning: Warning
    def __init__(self, id: _Optional[str] = ..., items: _Optional[_Iterable[_Union[Address, _Mapping]]] = ..., kind: _Optional[str] = ..., next_page_token: _Optional[str] = ..., self_link: _Optional[str] = ..., warning: _Optional[_Union[Warning, _Mapping]] = ...) -> None: ...

class AddressesScopedList(_message.Message):
    __slots__ = ("addresses", "warning")
    ADDRESSES_FIELD_NUMBER: _ClassVar[int]
    WARNING_FIELD_NUMBER: _ClassVar[int]
    addresses: _containers.RepeatedCompositeFieldContainer[Address]
    warning: Warning
    def __init__(self, addresses: _Optional[_Iterable[_Union[Address, _Mapping]]] = ..., warning: _Optional[_Union[Warning, _Mapping]] = ...) -> None: ...

class AggregatedListAddressesRequest(_message.Message):
    __slots__ = ("filter", "include_all_scopes", "max_results", "order_by", "page_token", "project")
    FILTER_FIELD_NUMBER: _ClassVar[int]
    INCLUDE_ALL_SCOPES_FIELD_NUMBER: _ClassVar[int]
    MAX_RESULTS_FIELD_NUMBER: _ClassVar[int]
    ORDER_BY_FIELD_NUMBER: _ClassVar[int]
    PAGE_TOKEN_FIELD_NUMBER: _ClassVar[int]
    PROJECT_FIELD_NUMBER: _ClassVar[int]
    filter: str
    include_all_scopes: bool
    max_results: int
    order_by: str
    page_token: str
    project: str
    def __init__(self, filter: _Optional[str] = ..., include_all_scopes: bool = ..., max_results: _Optional[int] = ..., order_by: _Optional[str] = ..., page_token: _Optional[str] = ..., project: _Optional[str] = ...) -> None: ...

class Data(_message.Message):
    __slots__ = ("key", "value")
    KEY_FIELD_NUMBER: _ClassVar[int]
    VALUE_FIELD_NUMBER: _ClassVar[int]
    key: str
    value: str
    def __init__(self, key: _Optional[str] = ..., value: _Optional[str] = ...) -> None: ...

class DeleteAddressRequest(_message.Message):
    __slots__ = ("address", "project", "region", "request_id")
    ADDRESS_FIELD_NUMBER: _ClassVar[int]
    PROJECT_FIELD_NUMBER: _ClassVar[int]
    REGION_FIELD_NUMBER: _ClassVar[int]
    REQUEST_ID_FIELD_NUMBER: _ClassVar[int]
    address: str
    project: str
    region: str
    request_id: str
    def __init__(self, address: _Optional[str] = ..., project: _Optional[str] = ..., region: _Optional[str] = ..., request_id: _Optional[str] = ...) -> None: ...

class Error(_message.Message):
    __slots__ = ("errors",)
    ERRORS_FIELD_NUMBER: _ClassVar[int]
    errors: _containers.RepeatedCompositeFieldContainer[Errors]
    def __init__(self, errors: _Optional[_Iterable[_Union[Errors, _Mapping]]] = ...) -> None: ...

class Errors(_message.Message):
    __slots__ = ("code", "location", "message")
    CODE_FIELD_NUMBER: _ClassVar[int]
    LOCATION_FIELD_NUMBER: _ClassVar[int]
    MESSAGE_FIELD_NUMBER: _ClassVar[int]
    code: str
    location: str
    message: str
    def __init__(self, code: _Optional[str] = ..., location: _Optional[str] = ..., message: _Optional[str] = ...) -> None: ...

class GetRegionOperationRequest(_message.Message):
    __slots__ = ("operation", "project", "region")
    OPERATION_FIELD_NUMBER: _ClassVar[int]
    PROJECT_FIELD_NUMBER: _ClassVar[int]
    REGION_FIELD_NUMBER: _ClassVar[int]
    operation: str
    project: str
    region: str
    def __init__(self, operation: _Optional[str] = ..., project: _Optional[str] = ..., region: _Optional[str] = ...) -> None: ...

class InsertAddressRequest(_message.Message):
    __slots__ = ("address_resource", "project", "region", "request_id")
    ADDRESS_RESOURCE_FIELD_NUMBER: _ClassVar[int]
    PROJECT_FIELD_NUMBER: _ClassVar[int]
    REGION_FIELD_NUMBER: _ClassVar[int]
    REQUEST_ID_FIELD_NUMBER: _ClassVar[int]
    address_resource: Address
    project: str
    region: str
    request_id: str
    def __init__(self, address_resource: _Optional[_Union[Address, _Mapping]] = ..., project: _Optional[str] = ..., region: _Optional[str] = ..., request_id: _Optional[str] = ...) -> None: ...

class ListAddressesRequest(_message.Message):
    __slots__ = ("filter", "max_results", "order_by", "page_token", "project", "region")
    FILTER_FIELD_NUMBER: _ClassVar[int]
    MAX_RESULTS_FIELD_NUMBER: _ClassVar[int]
    ORDER_BY_FIELD_NUMBER: _ClassVar[int]
    PAGE_TOKEN_FIELD_NUMBER: _ClassVar[int]
    PROJECT_FIELD_NUMBER: _ClassVar[int]
    REGION_FIELD_NUMBER: _ClassVar[int]
    filter: str
    max_results: int
    order_by: str
    page_token: str
    project: str
    region: str
    def __init__(self, filter: _Optional[str] = ..., max_results: _Optional[int] = ..., order_by: _Optional[str] = ..., page_token: _Optional[str] = ..., project: _Optional[str] = ..., region: _Optional[str] = ...) -> None: ...

class Operation(_message.Message):
    __slots__ = ("client_operation_id", "creation_timestamp", "description", "end_time", "error", "http_error_message", "http_error_status_code", "id", "insert_time", "kind", "name", "operation_type", "progress", "region", "self_link", "start_time", "status", "status_message", "target_id", "target_link", "user", "warnings", "zone")
    class Status(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        UNDEFINED_STATUS: _ClassVar[Operation.Status]
        DONE: _ClassVar[Operation.Status]
        PENDING: _ClassVar[Operation.Status]
        RUNNING: _ClassVar[Operation.Status]
    UNDEFINED_STATUS: Operation.Status
    DONE: Operation.Status
    PENDING: Operation.Status
    RUNNING: Operation.Status
    CLIENT_OPERATION_ID_FIELD_NUMBER: _ClassVar[int]
    CREATION_TIMESTAMP_FIELD_NUMBER: _ClassVar[int]
    DESCRIPTION_FIELD_NUMBER: _ClassVar[int]
    END_TIME_FIELD_NUMBER: _ClassVar[int]
    ERROR_FIELD_NUMBER: _ClassVar[int]
    HTTP_ERROR_MESSAGE_FIELD_NUMBER: _ClassVar[int]
    HTTP_ERROR_STATUS_CODE_FIELD_NUMBER: _ClassVar[int]
    ID_FIELD_NUMBER: _ClassVar[int]
    INSERT_TIME_FIELD_NUMBER: _ClassVar[int]
    KIND_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    OPERATION_TYPE_FIELD_NUMBER: _ClassVar[int]
    PROGRESS_FIELD_NUMBER: _ClassVar[int]
    REGION_FIELD_NUMBER: _ClassVar[int]
    SELF_LINK_FIELD_NUMBER: _ClassVar[int]
    START_TIME_FIELD_NUMBER: _ClassVar[int]
    STATUS_FIELD_NUMBER: _ClassVar[int]
    STATUS_MESSAGE_FIELD_NUMBER: _ClassVar[int]
    TARGET_ID_FIELD_NUMBER: _ClassVar[int]
    TARGET_LINK_FIELD_NUMBER: _ClassVar[int]
    USER_FIELD_NUMBER: _ClassVar[int]
    WARNINGS_FIELD_NUMBER: _ClassVar[int]
    ZONE_FIELD_NUMBER: _ClassVar[int]
    client_operation_id: str
    creation_timestamp: str
    description: str
    end_time: str
    error: Error
    http_error_message: str
    http_error_status_code: int
    id: int
    insert_time: str
    kind: str
    name: str
    operation_type: str
    progress: int
    region: str
    self_link: str
    start_time: str
    status: Operation.Status
    status_message: str
    target_id: int
    target_link: str
    user: str
    warnings: _containers.RepeatedCompositeFieldContainer[Warnings]
    zone: str
    def __init__(self, client_operation_id: _Optional[str] = ..., creation_timestamp: _Optional[str] = ..., description: _Optional[str] = ..., end_time: _Optional[str] = ..., error: _Optional[_Union[Error, _Mapping]] = ..., http_error_message: _Optional[str] = ..., http_error_status_code: _Optional[int] = ..., id: _Optional[int] = ..., insert_time: _Optional[str] = ..., kind: _Optional[str] = ..., name: _Optional[str] = ..., operation_type: _Optional[str] = ..., progress: _Optional[int] = ..., region: _Optional[str] = ..., self_link: _Optional[str] = ..., start_time: _Optional[str] = ..., status: _Optional[_Union[Operation.Status, str]] = ..., status_message: _Optional[str] = ..., target_id: _Optional[int] = ..., target_link: _Optional[str] = ..., user: _Optional[str] = ..., warnings: _Optional[_Iterable[_Union[Warnings, _Mapping]]] = ..., zone: _Optional[str] = ...) -> None: ...

class WaitRegionOperationRequest(_message.Message):
    __slots__ = ("operation", "project", "region")
    OPERATION_FIELD_NUMBER: _ClassVar[int]
    PROJECT_FIELD_NUMBER: _ClassVar[int]
    REGION_FIELD_NUMBER: _ClassVar[int]
    operation: str
    project: str
    region: str
    def __init__(self, operation: _Optional[str] = ..., project: _Optional[str] = ..., region: _Optional[str] = ...) -> None: ...

class Warning(_message.Message):
    __slots__ = ("code", "data", "message")
    class Code(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        UNDEFINED_CODE: _ClassVar[Warning.Code]
        CLEANUP_FAILED: _ClassVar[Warning.Code]
        DEPRECATED_RESOURCE_USED: _ClassVar[Warning.Code]
        DEPRECATED_TYPE_USED: _ClassVar[Warning.Code]
        DISK_SIZE_LARGER_THAN_IMAGE_SIZE: _ClassVar[Warning.Code]
        EXPERIMENTAL_TYPE_USED: _ClassVar[Warning.Code]
        EXTERNAL_API_WARNING: _ClassVar[Warning.Code]
        FIELD_VALUE_OVERRIDEN: _ClassVar[Warning.Code]
        INJECTED_KERNELS_DEPRECATED: _ClassVar[Warning.Code]
        MISSING_TYPE_DEPENDENCY: _ClassVar[Warning.Code]
        NEXT_HOP_ADDRESS_NOT_ASSIGNED: _ClassVar[Warning.Code]
        NEXT_HOP_CANNOT_IP_FORWARD: _ClassVar[Warning.Code]
        NEXT_HOP_INSTANCE_NOT_FOUND: _ClassVar[Warning.Code]
        NEXT_HOP_INSTANCE_NOT_ON_NETWORK: _ClassVar[Warning.Code]
        NEXT_HOP_NOT_RUNNING: _ClassVar[Warning.Code]
        NOT_CRITICAL_ERROR: _ClassVar[Warning.Code]
        NO_RESULTS_ON_PAGE: _ClassVar[Warning.Code]
        REQUIRED_TOS_AGREEMENT: _ClassVar[Warning.Code]
        RESOURCE_IN_USE_BY_OTHER_RESOURCE_WARNING: _ClassVar[Warning.Code]
        RESOURCE_NOT_DELETED: _ClassVar[Warning.Code]
        SCHEMA_VALIDATION_IGNORED: _ClassVar[Warning.Code]
        SINGLE_INSTANCE_PROPERTY_TEMPLATE: _ClassVar[Warning.Code]
        UNDECLARED_PROPERTIES: _ClassVar[Warning.Code]
        UNREACHABLE: _ClassVar[Warning.Code]
    UNDEFINED_CODE: Warning.Code
    CLEANUP_FAILED: Warning.Code
    DEPRECATED_RESOURCE_USED: Warning.Code
    DEPRECATED_TYPE_USED: Warning.Code
    DISK_SIZE_LARGER_THAN_IMAGE_SIZE: Warning.Code
    EXPERIMENTAL_TYPE_USED: Warning.Code
    EXTERNAL_API_WARNING: Warning.Code
    FIELD_VALUE_OVERRIDEN: Warning.Code
    INJECTED_KERNELS_DEPRECATED: Warning.Code
    MISSING_TYPE_DEPENDENCY: Warning.Code
    NEXT_HOP_ADDRESS_NOT_ASSIGNED: Warning.Code
    NEXT_HOP_CANNOT_IP_FORWARD: Warning.Code
    NEXT_HOP_INSTANCE_NOT_FOUND: Warning.Code
    NEXT_HOP_INSTANCE_NOT_ON_NETWORK: Warning.Code
    NEXT_HOP_NOT_RUNNING: Warning.Code
    NOT_CRITICAL_ERROR: Warning.Code
    NO_RESULTS_ON_PAGE: Warning.Code
    REQUIRED_TOS_AGREEMENT: Warning.Code
    RESOURCE_IN_USE_BY_OTHER_RESOURCE_WARNING: Warning.Code
    RESOURCE_NOT_DELETED: Warning.Code
    SCHEMA_VALIDATION_IGNORED: Warning.Code
    SINGLE_INSTANCE_PROPERTY_TEMPLATE: Warning.Code
    UNDECLARED_PROPERTIES: Warning.Code
    UNREACHABLE: Warning.Code
    CODE_FIELD_NUMBER: _ClassVar[int]
    DATA_FIELD_NUMBER: _ClassVar[int]
    MESSAGE_FIELD_NUMBER: _ClassVar[int]
    code: str
    data: _containers.RepeatedCompositeFieldContainer[Data]
    message: str
    def __init__(self, code: _Optional[str] = ..., data: _Optional[_Iterable[_Union[Data, _Mapping]]] = ..., message: _Optional[str] = ...) -> None: ...

class Warnings(_message.Message):
    __slots__ = ("code", "data", "message")
    class Code(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        UNDEFINED_CODE: _ClassVar[Warnings.Code]
        CLEANUP_FAILED: _ClassVar[Warnings.Code]
        DEPRECATED_RESOURCE_USED: _ClassVar[Warnings.Code]
        DEPRECATED_TYPE_USED: _ClassVar[Warnings.Code]
        DISK_SIZE_LARGER_THAN_IMAGE_SIZE: _ClassVar[Warnings.Code]
        EXPERIMENTAL_TYPE_USED: _ClassVar[Warnings.Code]
        EXTERNAL_API_WARNING: _ClassVar[Warnings.Code]
        FIELD_VALUE_OVERRIDEN: _ClassVar[Warnings.Code]
        INJECTED_KERNELS_DEPRECATED: _ClassVar[Warnings.Code]
        MISSING_TYPE_DEPENDENCY: _ClassVar[Warnings.Code]
        NEXT_HOP_ADDRESS_NOT_ASSIGNED: _ClassVar[Warnings.Code]
        NEXT_HOP_CANNOT_IP_FORWARD: _ClassVar[Warnings.Code]
        NEXT_HOP_INSTANCE_NOT_FOUND: _ClassVar[Warnings.Code]
        NEXT_HOP_INSTANCE_NOT_ON_NETWORK: _ClassVar[Warnings.Code]
        NEXT_HOP_NOT_RUNNING: _ClassVar[Warnings.Code]
        NOT_CRITICAL_ERROR: _ClassVar[Warnings.Code]
        NO_RESULTS_ON_PAGE: _ClassVar[Warnings.Code]
        REQUIRED_TOS_AGREEMENT: _ClassVar[Warnings.Code]
        RESOURCE_IN_USE_BY_OTHER_RESOURCE_WARNING: _ClassVar[Warnings.Code]
        RESOURCE_NOT_DELETED: _ClassVar[Warnings.Code]
        SCHEMA_VALIDATION_IGNORED: _ClassVar[Warnings.Code]
        SINGLE_INSTANCE_PROPERTY_TEMPLATE: _ClassVar[Warnings.Code]
        UNDECLARED_PROPERTIES: _ClassVar[Warnings.Code]
        UNREACHABLE: _ClassVar[Warnings.Code]
    UNDEFINED_CODE: Warnings.Code
    CLEANUP_FAILED: Warnings.Code
    DEPRECATED_RESOURCE_USED: Warnings.Code
    DEPRECATED_TYPE_USED: Warnings.Code
    DISK_SIZE_LARGER_THAN_IMAGE_SIZE: Warnings.Code
    EXPERIMENTAL_TYPE_USED: Warnings.Code
    EXTERNAL_API_WARNING: Warnings.Code
    FIELD_VALUE_OVERRIDEN: Warnings.Code
    INJECTED_KERNELS_DEPRECATED: Warnings.Code
    MISSING_TYPE_DEPENDENCY: Warnings.Code
    NEXT_HOP_ADDRESS_NOT_ASSIGNED: Warnings.Code
    NEXT_HOP_CANNOT_IP_FORWARD: Warnings.Code
    NEXT_HOP_INSTANCE_NOT_FOUND: Warnings.Code
    NEXT_HOP_INSTANCE_NOT_ON_NETWORK: Warnings.Code
    NEXT_HOP_NOT_RUNNING: Warnings.Code
    NOT_CRITICAL_ERROR: Warnings.Code
    NO_RESULTS_ON_PAGE: Warnings.Code
    REQUIRED_TOS_AGREEMENT: Warnings.Code
    RESOURCE_IN_USE_BY_OTHER_RESOURCE_WARNING: Warnings.Code
    RESOURCE_NOT_DELETED: Warnings.Code
    SCHEMA_VALIDATION_IGNORED: Warnings.Code
    SINGLE_INSTANCE_PROPERTY_TEMPLATE: Warnings.Code
    UNDECLARED_PROPERTIES: Warnings.Code
    UNREACHABLE: Warnings.Code
    CODE_FIELD_NUMBER: _ClassVar[int]
    DATA_FIELD_NUMBER: _ClassVar[int]
    MESSAGE_FIELD_NUMBER: _ClassVar[int]
    code: str
    data: _containers.RepeatedCompositeFieldContainer[Data]
    message: str
    def __init__(self, code: _Optional[str] = ..., data: _Optional[_Iterable[_Union[Data, _Mapping]]] = ..., message: _Optional[str] = ...) -> None: ...
