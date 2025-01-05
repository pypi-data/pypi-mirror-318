from google.api import field_behavior_pb2 as _field_behavior_pb2
from google.api import resource_pb2 as _resource_pb2
from google.cloud.channel.v1 import common_pb2 as _common_pb2
from google.cloud.channel.v1 import offers_pb2 as _offers_pb2
from google.cloud.channel.v1 import products_pb2 as _products_pb2
from google.protobuf import timestamp_pb2 as _timestamp_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union
DESCRIPTOR: _descriptor.FileDescriptor

class Entitlement(_message.Message):
    __slots__ = ('name', 'create_time', 'update_time', 'offer', 'commitment_settings', 'provisioning_state', 'provisioned_service', 'suspension_reasons', 'purchase_order_id', 'trial_settings', 'association_info', 'parameters', 'billing_account')

    class ProvisioningState(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        PROVISIONING_STATE_UNSPECIFIED: _ClassVar[Entitlement.ProvisioningState]
        ACTIVE: _ClassVar[Entitlement.ProvisioningState]
        SUSPENDED: _ClassVar[Entitlement.ProvisioningState]
    PROVISIONING_STATE_UNSPECIFIED: Entitlement.ProvisioningState
    ACTIVE: Entitlement.ProvisioningState
    SUSPENDED: Entitlement.ProvisioningState

    class SuspensionReason(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        SUSPENSION_REASON_UNSPECIFIED: _ClassVar[Entitlement.SuspensionReason]
        RESELLER_INITIATED: _ClassVar[Entitlement.SuspensionReason]
        TRIAL_ENDED: _ClassVar[Entitlement.SuspensionReason]
        RENEWAL_WITH_TYPE_CANCEL: _ClassVar[Entitlement.SuspensionReason]
        PENDING_TOS_ACCEPTANCE: _ClassVar[Entitlement.SuspensionReason]
        OTHER: _ClassVar[Entitlement.SuspensionReason]
    SUSPENSION_REASON_UNSPECIFIED: Entitlement.SuspensionReason
    RESELLER_INITIATED: Entitlement.SuspensionReason
    TRIAL_ENDED: Entitlement.SuspensionReason
    RENEWAL_WITH_TYPE_CANCEL: Entitlement.SuspensionReason
    PENDING_TOS_ACCEPTANCE: Entitlement.SuspensionReason
    OTHER: Entitlement.SuspensionReason
    NAME_FIELD_NUMBER: _ClassVar[int]
    CREATE_TIME_FIELD_NUMBER: _ClassVar[int]
    UPDATE_TIME_FIELD_NUMBER: _ClassVar[int]
    OFFER_FIELD_NUMBER: _ClassVar[int]
    COMMITMENT_SETTINGS_FIELD_NUMBER: _ClassVar[int]
    PROVISIONING_STATE_FIELD_NUMBER: _ClassVar[int]
    PROVISIONED_SERVICE_FIELD_NUMBER: _ClassVar[int]
    SUSPENSION_REASONS_FIELD_NUMBER: _ClassVar[int]
    PURCHASE_ORDER_ID_FIELD_NUMBER: _ClassVar[int]
    TRIAL_SETTINGS_FIELD_NUMBER: _ClassVar[int]
    ASSOCIATION_INFO_FIELD_NUMBER: _ClassVar[int]
    PARAMETERS_FIELD_NUMBER: _ClassVar[int]
    BILLING_ACCOUNT_FIELD_NUMBER: _ClassVar[int]
    name: str
    create_time: _timestamp_pb2.Timestamp
    update_time: _timestamp_pb2.Timestamp
    offer: str
    commitment_settings: CommitmentSettings
    provisioning_state: Entitlement.ProvisioningState
    provisioned_service: ProvisionedService
    suspension_reasons: _containers.RepeatedScalarFieldContainer[Entitlement.SuspensionReason]
    purchase_order_id: str
    trial_settings: TrialSettings
    association_info: AssociationInfo
    parameters: _containers.RepeatedCompositeFieldContainer[Parameter]
    billing_account: str

    def __init__(self, name: _Optional[str]=..., create_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]]=..., update_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]]=..., offer: _Optional[str]=..., commitment_settings: _Optional[_Union[CommitmentSettings, _Mapping]]=..., provisioning_state: _Optional[_Union[Entitlement.ProvisioningState, str]]=..., provisioned_service: _Optional[_Union[ProvisionedService, _Mapping]]=..., suspension_reasons: _Optional[_Iterable[_Union[Entitlement.SuspensionReason, str]]]=..., purchase_order_id: _Optional[str]=..., trial_settings: _Optional[_Union[TrialSettings, _Mapping]]=..., association_info: _Optional[_Union[AssociationInfo, _Mapping]]=..., parameters: _Optional[_Iterable[_Union[Parameter, _Mapping]]]=..., billing_account: _Optional[str]=...) -> None:
        ...

class Parameter(_message.Message):
    __slots__ = ('name', 'value', 'editable')
    NAME_FIELD_NUMBER: _ClassVar[int]
    VALUE_FIELD_NUMBER: _ClassVar[int]
    EDITABLE_FIELD_NUMBER: _ClassVar[int]
    name: str
    value: _common_pb2.Value
    editable: bool

    def __init__(self, name: _Optional[str]=..., value: _Optional[_Union[_common_pb2.Value, _Mapping]]=..., editable: bool=...) -> None:
        ...

class AssociationInfo(_message.Message):
    __slots__ = ('base_entitlement',)
    BASE_ENTITLEMENT_FIELD_NUMBER: _ClassVar[int]
    base_entitlement: str

    def __init__(self, base_entitlement: _Optional[str]=...) -> None:
        ...

class ProvisionedService(_message.Message):
    __slots__ = ('provisioning_id', 'product_id', 'sku_id')
    PROVISIONING_ID_FIELD_NUMBER: _ClassVar[int]
    PRODUCT_ID_FIELD_NUMBER: _ClassVar[int]
    SKU_ID_FIELD_NUMBER: _ClassVar[int]
    provisioning_id: str
    product_id: str
    sku_id: str

    def __init__(self, provisioning_id: _Optional[str]=..., product_id: _Optional[str]=..., sku_id: _Optional[str]=...) -> None:
        ...

class CommitmentSettings(_message.Message):
    __slots__ = ('start_time', 'end_time', 'renewal_settings')
    START_TIME_FIELD_NUMBER: _ClassVar[int]
    END_TIME_FIELD_NUMBER: _ClassVar[int]
    RENEWAL_SETTINGS_FIELD_NUMBER: _ClassVar[int]
    start_time: _timestamp_pb2.Timestamp
    end_time: _timestamp_pb2.Timestamp
    renewal_settings: RenewalSettings

    def __init__(self, start_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]]=..., end_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]]=..., renewal_settings: _Optional[_Union[RenewalSettings, _Mapping]]=...) -> None:
        ...

class RenewalSettings(_message.Message):
    __slots__ = ('enable_renewal', 'resize_unit_count', 'payment_plan', 'payment_cycle')
    ENABLE_RENEWAL_FIELD_NUMBER: _ClassVar[int]
    RESIZE_UNIT_COUNT_FIELD_NUMBER: _ClassVar[int]
    PAYMENT_PLAN_FIELD_NUMBER: _ClassVar[int]
    PAYMENT_CYCLE_FIELD_NUMBER: _ClassVar[int]
    enable_renewal: bool
    resize_unit_count: bool
    payment_plan: _offers_pb2.PaymentPlan
    payment_cycle: _offers_pb2.Period

    def __init__(self, enable_renewal: bool=..., resize_unit_count: bool=..., payment_plan: _Optional[_Union[_offers_pb2.PaymentPlan, str]]=..., payment_cycle: _Optional[_Union[_offers_pb2.Period, _Mapping]]=...) -> None:
        ...

class TrialSettings(_message.Message):
    __slots__ = ('trial', 'end_time')
    TRIAL_FIELD_NUMBER: _ClassVar[int]
    END_TIME_FIELD_NUMBER: _ClassVar[int]
    trial: bool
    end_time: _timestamp_pb2.Timestamp

    def __init__(self, trial: bool=..., end_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]]=...) -> None:
        ...

class TransferableSku(_message.Message):
    __slots__ = ('transfer_eligibility', 'sku', 'legacy_sku')
    TRANSFER_ELIGIBILITY_FIELD_NUMBER: _ClassVar[int]
    SKU_FIELD_NUMBER: _ClassVar[int]
    LEGACY_SKU_FIELD_NUMBER: _ClassVar[int]
    transfer_eligibility: TransferEligibility
    sku: _products_pb2.Sku
    legacy_sku: _products_pb2.Sku

    def __init__(self, transfer_eligibility: _Optional[_Union[TransferEligibility, _Mapping]]=..., sku: _Optional[_Union[_products_pb2.Sku, _Mapping]]=..., legacy_sku: _Optional[_Union[_products_pb2.Sku, _Mapping]]=...) -> None:
        ...

class TransferEligibility(_message.Message):
    __slots__ = ('is_eligible', 'description', 'ineligibility_reason')

    class Reason(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        REASON_UNSPECIFIED: _ClassVar[TransferEligibility.Reason]
        PENDING_TOS_ACCEPTANCE: _ClassVar[TransferEligibility.Reason]
        SKU_NOT_ELIGIBLE: _ClassVar[TransferEligibility.Reason]
        SKU_SUSPENDED: _ClassVar[TransferEligibility.Reason]
        CHANNEL_PARTNER_NOT_AUTHORIZED_FOR_SKU: _ClassVar[TransferEligibility.Reason]
    REASON_UNSPECIFIED: TransferEligibility.Reason
    PENDING_TOS_ACCEPTANCE: TransferEligibility.Reason
    SKU_NOT_ELIGIBLE: TransferEligibility.Reason
    SKU_SUSPENDED: TransferEligibility.Reason
    CHANNEL_PARTNER_NOT_AUTHORIZED_FOR_SKU: TransferEligibility.Reason
    IS_ELIGIBLE_FIELD_NUMBER: _ClassVar[int]
    DESCRIPTION_FIELD_NUMBER: _ClassVar[int]
    INELIGIBILITY_REASON_FIELD_NUMBER: _ClassVar[int]
    is_eligible: bool
    description: str
    ineligibility_reason: TransferEligibility.Reason

    def __init__(self, is_eligible: bool=..., description: _Optional[str]=..., ineligibility_reason: _Optional[_Union[TransferEligibility.Reason, str]]=...) -> None:
        ...