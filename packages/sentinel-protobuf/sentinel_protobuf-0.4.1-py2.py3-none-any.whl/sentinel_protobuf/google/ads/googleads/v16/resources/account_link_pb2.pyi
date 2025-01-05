from google.ads.googleads.v16.enums import account_link_status_pb2 as _account_link_status_pb2
from google.ads.googleads.v16.enums import linked_account_type_pb2 as _linked_account_type_pb2
from google.ads.googleads.v16.enums import mobile_app_vendor_pb2 as _mobile_app_vendor_pb2
from google.api import field_behavior_pb2 as _field_behavior_pb2
from google.api import resource_pb2 as _resource_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class AccountLink(_message.Message):
    __slots__ = ("resource_name", "account_link_id", "status", "type", "third_party_app_analytics")
    RESOURCE_NAME_FIELD_NUMBER: _ClassVar[int]
    ACCOUNT_LINK_ID_FIELD_NUMBER: _ClassVar[int]
    STATUS_FIELD_NUMBER: _ClassVar[int]
    TYPE_FIELD_NUMBER: _ClassVar[int]
    THIRD_PARTY_APP_ANALYTICS_FIELD_NUMBER: _ClassVar[int]
    resource_name: str
    account_link_id: int
    status: _account_link_status_pb2.AccountLinkStatusEnum.AccountLinkStatus
    type: _linked_account_type_pb2.LinkedAccountTypeEnum.LinkedAccountType
    third_party_app_analytics: ThirdPartyAppAnalyticsLinkIdentifier
    def __init__(self, resource_name: _Optional[str] = ..., account_link_id: _Optional[int] = ..., status: _Optional[_Union[_account_link_status_pb2.AccountLinkStatusEnum.AccountLinkStatus, str]] = ..., type: _Optional[_Union[_linked_account_type_pb2.LinkedAccountTypeEnum.LinkedAccountType, str]] = ..., third_party_app_analytics: _Optional[_Union[ThirdPartyAppAnalyticsLinkIdentifier, _Mapping]] = ...) -> None: ...

class ThirdPartyAppAnalyticsLinkIdentifier(_message.Message):
    __slots__ = ("app_analytics_provider_id", "app_id", "app_vendor")
    APP_ANALYTICS_PROVIDER_ID_FIELD_NUMBER: _ClassVar[int]
    APP_ID_FIELD_NUMBER: _ClassVar[int]
    APP_VENDOR_FIELD_NUMBER: _ClassVar[int]
    app_analytics_provider_id: int
    app_id: str
    app_vendor: _mobile_app_vendor_pb2.MobileAppVendorEnum.MobileAppVendor
    def __init__(self, app_analytics_provider_id: _Optional[int] = ..., app_id: _Optional[str] = ..., app_vendor: _Optional[_Union[_mobile_app_vendor_pb2.MobileAppVendorEnum.MobileAppVendor, str]] = ...) -> None: ...
