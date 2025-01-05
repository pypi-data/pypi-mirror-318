from google.ads.googleads.v18.resources import customer_sk_ad_network_conversion_value_schema_pb2 as _customer_sk_ad_network_conversion_value_schema_pb2
from google.api import annotations_pb2 as _annotations_pb2
from google.api import client_pb2 as _client_pb2
from google.api import field_behavior_pb2 as _field_behavior_pb2
from google.api import resource_pb2 as _resource_pb2
from google.rpc import status_pb2 as _status_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Mapping as _Mapping, Optional as _Optional, Union as _Union
DESCRIPTOR: _descriptor.FileDescriptor

class CustomerSkAdNetworkConversionValueSchemaOperation(_message.Message):
    __slots__ = ('update',)
    UPDATE_FIELD_NUMBER: _ClassVar[int]
    update: _customer_sk_ad_network_conversion_value_schema_pb2.CustomerSkAdNetworkConversionValueSchema

    def __init__(self, update: _Optional[_Union[_customer_sk_ad_network_conversion_value_schema_pb2.CustomerSkAdNetworkConversionValueSchema, _Mapping]]=...) -> None:
        ...

class MutateCustomerSkAdNetworkConversionValueSchemaRequest(_message.Message):
    __slots__ = ('customer_id', 'operation', 'validate_only', 'enable_warnings')
    CUSTOMER_ID_FIELD_NUMBER: _ClassVar[int]
    OPERATION_FIELD_NUMBER: _ClassVar[int]
    VALIDATE_ONLY_FIELD_NUMBER: _ClassVar[int]
    ENABLE_WARNINGS_FIELD_NUMBER: _ClassVar[int]
    customer_id: str
    operation: CustomerSkAdNetworkConversionValueSchemaOperation
    validate_only: bool
    enable_warnings: bool

    def __init__(self, customer_id: _Optional[str]=..., operation: _Optional[_Union[CustomerSkAdNetworkConversionValueSchemaOperation, _Mapping]]=..., validate_only: bool=..., enable_warnings: bool=...) -> None:
        ...

class MutateCustomerSkAdNetworkConversionValueSchemaResult(_message.Message):
    __slots__ = ('resource_name', 'app_id')
    RESOURCE_NAME_FIELD_NUMBER: _ClassVar[int]
    APP_ID_FIELD_NUMBER: _ClassVar[int]
    resource_name: str
    app_id: str

    def __init__(self, resource_name: _Optional[str]=..., app_id: _Optional[str]=...) -> None:
        ...

class MutateCustomerSkAdNetworkConversionValueSchemaResponse(_message.Message):
    __slots__ = ('result', 'warning')
    RESULT_FIELD_NUMBER: _ClassVar[int]
    WARNING_FIELD_NUMBER: _ClassVar[int]
    result: MutateCustomerSkAdNetworkConversionValueSchemaResult
    warning: _status_pb2.Status

    def __init__(self, result: _Optional[_Union[MutateCustomerSkAdNetworkConversionValueSchemaResult, _Mapping]]=..., warning: _Optional[_Union[_status_pb2.Status, _Mapping]]=...) -> None:
        ...