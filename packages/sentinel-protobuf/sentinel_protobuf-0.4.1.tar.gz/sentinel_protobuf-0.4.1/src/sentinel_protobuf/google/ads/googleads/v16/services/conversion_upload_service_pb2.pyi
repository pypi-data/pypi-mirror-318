from google.ads.googleads.v16.common import consent_pb2 as _consent_pb2
from google.ads.googleads.v16.common import offline_user_data_pb2 as _offline_user_data_pb2
from google.ads.googleads.v16.enums import conversion_environment_enum_pb2 as _conversion_environment_enum_pb2
from google.api import annotations_pb2 as _annotations_pb2
from google.api import client_pb2 as _client_pb2
from google.api import field_behavior_pb2 as _field_behavior_pb2
from google.api import resource_pb2 as _resource_pb2
from google.rpc import status_pb2 as _status_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class UploadClickConversionsRequest(_message.Message):
    __slots__ = ("customer_id", "conversions", "partial_failure", "validate_only", "debug_enabled", "job_id")
    CUSTOMER_ID_FIELD_NUMBER: _ClassVar[int]
    CONVERSIONS_FIELD_NUMBER: _ClassVar[int]
    PARTIAL_FAILURE_FIELD_NUMBER: _ClassVar[int]
    VALIDATE_ONLY_FIELD_NUMBER: _ClassVar[int]
    DEBUG_ENABLED_FIELD_NUMBER: _ClassVar[int]
    JOB_ID_FIELD_NUMBER: _ClassVar[int]
    customer_id: str
    conversions: _containers.RepeatedCompositeFieldContainer[ClickConversion]
    partial_failure: bool
    validate_only: bool
    debug_enabled: bool
    job_id: int
    def __init__(self, customer_id: _Optional[str] = ..., conversions: _Optional[_Iterable[_Union[ClickConversion, _Mapping]]] = ..., partial_failure: bool = ..., validate_only: bool = ..., debug_enabled: bool = ..., job_id: _Optional[int] = ...) -> None: ...

class UploadClickConversionsResponse(_message.Message):
    __slots__ = ("partial_failure_error", "results", "job_id")
    PARTIAL_FAILURE_ERROR_FIELD_NUMBER: _ClassVar[int]
    RESULTS_FIELD_NUMBER: _ClassVar[int]
    JOB_ID_FIELD_NUMBER: _ClassVar[int]
    partial_failure_error: _status_pb2.Status
    results: _containers.RepeatedCompositeFieldContainer[ClickConversionResult]
    job_id: int
    def __init__(self, partial_failure_error: _Optional[_Union[_status_pb2.Status, _Mapping]] = ..., results: _Optional[_Iterable[_Union[ClickConversionResult, _Mapping]]] = ..., job_id: _Optional[int] = ...) -> None: ...

class UploadCallConversionsRequest(_message.Message):
    __slots__ = ("customer_id", "conversions", "partial_failure", "validate_only")
    CUSTOMER_ID_FIELD_NUMBER: _ClassVar[int]
    CONVERSIONS_FIELD_NUMBER: _ClassVar[int]
    PARTIAL_FAILURE_FIELD_NUMBER: _ClassVar[int]
    VALIDATE_ONLY_FIELD_NUMBER: _ClassVar[int]
    customer_id: str
    conversions: _containers.RepeatedCompositeFieldContainer[CallConversion]
    partial_failure: bool
    validate_only: bool
    def __init__(self, customer_id: _Optional[str] = ..., conversions: _Optional[_Iterable[_Union[CallConversion, _Mapping]]] = ..., partial_failure: bool = ..., validate_only: bool = ...) -> None: ...

class UploadCallConversionsResponse(_message.Message):
    __slots__ = ("partial_failure_error", "results")
    PARTIAL_FAILURE_ERROR_FIELD_NUMBER: _ClassVar[int]
    RESULTS_FIELD_NUMBER: _ClassVar[int]
    partial_failure_error: _status_pb2.Status
    results: _containers.RepeatedCompositeFieldContainer[CallConversionResult]
    def __init__(self, partial_failure_error: _Optional[_Union[_status_pb2.Status, _Mapping]] = ..., results: _Optional[_Iterable[_Union[CallConversionResult, _Mapping]]] = ...) -> None: ...

class ClickConversion(_message.Message):
    __slots__ = ("gclid", "gbraid", "wbraid", "conversion_action", "conversion_date_time", "conversion_value", "currency_code", "order_id", "external_attribution_data", "custom_variables", "cart_data", "user_identifiers", "conversion_environment", "consent")
    GCLID_FIELD_NUMBER: _ClassVar[int]
    GBRAID_FIELD_NUMBER: _ClassVar[int]
    WBRAID_FIELD_NUMBER: _ClassVar[int]
    CONVERSION_ACTION_FIELD_NUMBER: _ClassVar[int]
    CONVERSION_DATE_TIME_FIELD_NUMBER: _ClassVar[int]
    CONVERSION_VALUE_FIELD_NUMBER: _ClassVar[int]
    CURRENCY_CODE_FIELD_NUMBER: _ClassVar[int]
    ORDER_ID_FIELD_NUMBER: _ClassVar[int]
    EXTERNAL_ATTRIBUTION_DATA_FIELD_NUMBER: _ClassVar[int]
    CUSTOM_VARIABLES_FIELD_NUMBER: _ClassVar[int]
    CART_DATA_FIELD_NUMBER: _ClassVar[int]
    USER_IDENTIFIERS_FIELD_NUMBER: _ClassVar[int]
    CONVERSION_ENVIRONMENT_FIELD_NUMBER: _ClassVar[int]
    CONSENT_FIELD_NUMBER: _ClassVar[int]
    gclid: str
    gbraid: str
    wbraid: str
    conversion_action: str
    conversion_date_time: str
    conversion_value: float
    currency_code: str
    order_id: str
    external_attribution_data: ExternalAttributionData
    custom_variables: _containers.RepeatedCompositeFieldContainer[CustomVariable]
    cart_data: CartData
    user_identifiers: _containers.RepeatedCompositeFieldContainer[_offline_user_data_pb2.UserIdentifier]
    conversion_environment: _conversion_environment_enum_pb2.ConversionEnvironmentEnum.ConversionEnvironment
    consent: _consent_pb2.Consent
    def __init__(self, gclid: _Optional[str] = ..., gbraid: _Optional[str] = ..., wbraid: _Optional[str] = ..., conversion_action: _Optional[str] = ..., conversion_date_time: _Optional[str] = ..., conversion_value: _Optional[float] = ..., currency_code: _Optional[str] = ..., order_id: _Optional[str] = ..., external_attribution_data: _Optional[_Union[ExternalAttributionData, _Mapping]] = ..., custom_variables: _Optional[_Iterable[_Union[CustomVariable, _Mapping]]] = ..., cart_data: _Optional[_Union[CartData, _Mapping]] = ..., user_identifiers: _Optional[_Iterable[_Union[_offline_user_data_pb2.UserIdentifier, _Mapping]]] = ..., conversion_environment: _Optional[_Union[_conversion_environment_enum_pb2.ConversionEnvironmentEnum.ConversionEnvironment, str]] = ..., consent: _Optional[_Union[_consent_pb2.Consent, _Mapping]] = ...) -> None: ...

class CallConversion(_message.Message):
    __slots__ = ("caller_id", "call_start_date_time", "conversion_action", "conversion_date_time", "conversion_value", "currency_code", "custom_variables", "consent")
    CALLER_ID_FIELD_NUMBER: _ClassVar[int]
    CALL_START_DATE_TIME_FIELD_NUMBER: _ClassVar[int]
    CONVERSION_ACTION_FIELD_NUMBER: _ClassVar[int]
    CONVERSION_DATE_TIME_FIELD_NUMBER: _ClassVar[int]
    CONVERSION_VALUE_FIELD_NUMBER: _ClassVar[int]
    CURRENCY_CODE_FIELD_NUMBER: _ClassVar[int]
    CUSTOM_VARIABLES_FIELD_NUMBER: _ClassVar[int]
    CONSENT_FIELD_NUMBER: _ClassVar[int]
    caller_id: str
    call_start_date_time: str
    conversion_action: str
    conversion_date_time: str
    conversion_value: float
    currency_code: str
    custom_variables: _containers.RepeatedCompositeFieldContainer[CustomVariable]
    consent: _consent_pb2.Consent
    def __init__(self, caller_id: _Optional[str] = ..., call_start_date_time: _Optional[str] = ..., conversion_action: _Optional[str] = ..., conversion_date_time: _Optional[str] = ..., conversion_value: _Optional[float] = ..., currency_code: _Optional[str] = ..., custom_variables: _Optional[_Iterable[_Union[CustomVariable, _Mapping]]] = ..., consent: _Optional[_Union[_consent_pb2.Consent, _Mapping]] = ...) -> None: ...

class ExternalAttributionData(_message.Message):
    __slots__ = ("external_attribution_credit", "external_attribution_model")
    EXTERNAL_ATTRIBUTION_CREDIT_FIELD_NUMBER: _ClassVar[int]
    EXTERNAL_ATTRIBUTION_MODEL_FIELD_NUMBER: _ClassVar[int]
    external_attribution_credit: float
    external_attribution_model: str
    def __init__(self, external_attribution_credit: _Optional[float] = ..., external_attribution_model: _Optional[str] = ...) -> None: ...

class ClickConversionResult(_message.Message):
    __slots__ = ("gclid", "gbraid", "wbraid", "conversion_action", "conversion_date_time", "user_identifiers")
    GCLID_FIELD_NUMBER: _ClassVar[int]
    GBRAID_FIELD_NUMBER: _ClassVar[int]
    WBRAID_FIELD_NUMBER: _ClassVar[int]
    CONVERSION_ACTION_FIELD_NUMBER: _ClassVar[int]
    CONVERSION_DATE_TIME_FIELD_NUMBER: _ClassVar[int]
    USER_IDENTIFIERS_FIELD_NUMBER: _ClassVar[int]
    gclid: str
    gbraid: str
    wbraid: str
    conversion_action: str
    conversion_date_time: str
    user_identifiers: _containers.RepeatedCompositeFieldContainer[_offline_user_data_pb2.UserIdentifier]
    def __init__(self, gclid: _Optional[str] = ..., gbraid: _Optional[str] = ..., wbraid: _Optional[str] = ..., conversion_action: _Optional[str] = ..., conversion_date_time: _Optional[str] = ..., user_identifiers: _Optional[_Iterable[_Union[_offline_user_data_pb2.UserIdentifier, _Mapping]]] = ...) -> None: ...

class CallConversionResult(_message.Message):
    __slots__ = ("caller_id", "call_start_date_time", "conversion_action", "conversion_date_time")
    CALLER_ID_FIELD_NUMBER: _ClassVar[int]
    CALL_START_DATE_TIME_FIELD_NUMBER: _ClassVar[int]
    CONVERSION_ACTION_FIELD_NUMBER: _ClassVar[int]
    CONVERSION_DATE_TIME_FIELD_NUMBER: _ClassVar[int]
    caller_id: str
    call_start_date_time: str
    conversion_action: str
    conversion_date_time: str
    def __init__(self, caller_id: _Optional[str] = ..., call_start_date_time: _Optional[str] = ..., conversion_action: _Optional[str] = ..., conversion_date_time: _Optional[str] = ...) -> None: ...

class CustomVariable(_message.Message):
    __slots__ = ("conversion_custom_variable", "value")
    CONVERSION_CUSTOM_VARIABLE_FIELD_NUMBER: _ClassVar[int]
    VALUE_FIELD_NUMBER: _ClassVar[int]
    conversion_custom_variable: str
    value: str
    def __init__(self, conversion_custom_variable: _Optional[str] = ..., value: _Optional[str] = ...) -> None: ...

class CartData(_message.Message):
    __slots__ = ("merchant_id", "feed_country_code", "feed_language_code", "local_transaction_cost", "items")
    class Item(_message.Message):
        __slots__ = ("product_id", "quantity", "unit_price")
        PRODUCT_ID_FIELD_NUMBER: _ClassVar[int]
        QUANTITY_FIELD_NUMBER: _ClassVar[int]
        UNIT_PRICE_FIELD_NUMBER: _ClassVar[int]
        product_id: str
        quantity: int
        unit_price: float
        def __init__(self, product_id: _Optional[str] = ..., quantity: _Optional[int] = ..., unit_price: _Optional[float] = ...) -> None: ...
    MERCHANT_ID_FIELD_NUMBER: _ClassVar[int]
    FEED_COUNTRY_CODE_FIELD_NUMBER: _ClassVar[int]
    FEED_LANGUAGE_CODE_FIELD_NUMBER: _ClassVar[int]
    LOCAL_TRANSACTION_COST_FIELD_NUMBER: _ClassVar[int]
    ITEMS_FIELD_NUMBER: _ClassVar[int]
    merchant_id: int
    feed_country_code: str
    feed_language_code: str
    local_transaction_cost: float
    items: _containers.RepeatedCompositeFieldContainer[CartData.Item]
    def __init__(self, merchant_id: _Optional[int] = ..., feed_country_code: _Optional[str] = ..., feed_language_code: _Optional[str] = ..., local_transaction_cost: _Optional[float] = ..., items: _Optional[_Iterable[_Union[CartData.Item, _Mapping]]] = ...) -> None: ...
