from google.api import field_behavior_pb2 as _field_behavior_pb2
from google.api import resource_pb2 as _resource_pb2
from google.cloud.channel.v1 import entitlements_pb2 as _entitlements_pb2
from google.protobuf import timestamp_pb2 as _timestamp_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union
DESCRIPTOR: _descriptor.FileDescriptor

class EntitlementChange(_message.Message):
    __slots__ = ('suspension_reason', 'cancellation_reason', 'activation_reason', 'other_change_reason', 'entitlement', 'offer', 'provisioned_service', 'change_type', 'create_time', 'operator_type', 'parameters', 'operator')

    class ChangeType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        CHANGE_TYPE_UNSPECIFIED: _ClassVar[EntitlementChange.ChangeType]
        CREATED: _ClassVar[EntitlementChange.ChangeType]
        PRICE_PLAN_SWITCHED: _ClassVar[EntitlementChange.ChangeType]
        COMMITMENT_CHANGED: _ClassVar[EntitlementChange.ChangeType]
        RENEWED: _ClassVar[EntitlementChange.ChangeType]
        SUSPENDED: _ClassVar[EntitlementChange.ChangeType]
        ACTIVATED: _ClassVar[EntitlementChange.ChangeType]
        CANCELLED: _ClassVar[EntitlementChange.ChangeType]
        SKU_CHANGED: _ClassVar[EntitlementChange.ChangeType]
        RENEWAL_SETTING_CHANGED: _ClassVar[EntitlementChange.ChangeType]
        PAID_SUBSCRIPTION_STARTED: _ClassVar[EntitlementChange.ChangeType]
        LICENSE_CAP_CHANGED: _ClassVar[EntitlementChange.ChangeType]
        SUSPENSION_DETAILS_CHANGED: _ClassVar[EntitlementChange.ChangeType]
        TRIAL_END_DATE_EXTENDED: _ClassVar[EntitlementChange.ChangeType]
        TRIAL_STARTED: _ClassVar[EntitlementChange.ChangeType]
    CHANGE_TYPE_UNSPECIFIED: EntitlementChange.ChangeType
    CREATED: EntitlementChange.ChangeType
    PRICE_PLAN_SWITCHED: EntitlementChange.ChangeType
    COMMITMENT_CHANGED: EntitlementChange.ChangeType
    RENEWED: EntitlementChange.ChangeType
    SUSPENDED: EntitlementChange.ChangeType
    ACTIVATED: EntitlementChange.ChangeType
    CANCELLED: EntitlementChange.ChangeType
    SKU_CHANGED: EntitlementChange.ChangeType
    RENEWAL_SETTING_CHANGED: EntitlementChange.ChangeType
    PAID_SUBSCRIPTION_STARTED: EntitlementChange.ChangeType
    LICENSE_CAP_CHANGED: EntitlementChange.ChangeType
    SUSPENSION_DETAILS_CHANGED: EntitlementChange.ChangeType
    TRIAL_END_DATE_EXTENDED: EntitlementChange.ChangeType
    TRIAL_STARTED: EntitlementChange.ChangeType

    class OperatorType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        OPERATOR_TYPE_UNSPECIFIED: _ClassVar[EntitlementChange.OperatorType]
        CUSTOMER_SERVICE_REPRESENTATIVE: _ClassVar[EntitlementChange.OperatorType]
        SYSTEM: _ClassVar[EntitlementChange.OperatorType]
        CUSTOMER: _ClassVar[EntitlementChange.OperatorType]
        RESELLER: _ClassVar[EntitlementChange.OperatorType]
    OPERATOR_TYPE_UNSPECIFIED: EntitlementChange.OperatorType
    CUSTOMER_SERVICE_REPRESENTATIVE: EntitlementChange.OperatorType
    SYSTEM: EntitlementChange.OperatorType
    CUSTOMER: EntitlementChange.OperatorType
    RESELLER: EntitlementChange.OperatorType

    class CancellationReason(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        CANCELLATION_REASON_UNSPECIFIED: _ClassVar[EntitlementChange.CancellationReason]
        SERVICE_TERMINATED: _ClassVar[EntitlementChange.CancellationReason]
        RELATIONSHIP_ENDED: _ClassVar[EntitlementChange.CancellationReason]
        PARTIAL_TRANSFER: _ClassVar[EntitlementChange.CancellationReason]
    CANCELLATION_REASON_UNSPECIFIED: EntitlementChange.CancellationReason
    SERVICE_TERMINATED: EntitlementChange.CancellationReason
    RELATIONSHIP_ENDED: EntitlementChange.CancellationReason
    PARTIAL_TRANSFER: EntitlementChange.CancellationReason

    class ActivationReason(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        ACTIVATION_REASON_UNSPECIFIED: _ClassVar[EntitlementChange.ActivationReason]
        RESELLER_REVOKED_SUSPENSION: _ClassVar[EntitlementChange.ActivationReason]
        CUSTOMER_ACCEPTED_PENDING_TOS: _ClassVar[EntitlementChange.ActivationReason]
        RENEWAL_SETTINGS_CHANGED: _ClassVar[EntitlementChange.ActivationReason]
        OTHER_ACTIVATION_REASON: _ClassVar[EntitlementChange.ActivationReason]
    ACTIVATION_REASON_UNSPECIFIED: EntitlementChange.ActivationReason
    RESELLER_REVOKED_SUSPENSION: EntitlementChange.ActivationReason
    CUSTOMER_ACCEPTED_PENDING_TOS: EntitlementChange.ActivationReason
    RENEWAL_SETTINGS_CHANGED: EntitlementChange.ActivationReason
    OTHER_ACTIVATION_REASON: EntitlementChange.ActivationReason
    SUSPENSION_REASON_FIELD_NUMBER: _ClassVar[int]
    CANCELLATION_REASON_FIELD_NUMBER: _ClassVar[int]
    ACTIVATION_REASON_FIELD_NUMBER: _ClassVar[int]
    OTHER_CHANGE_REASON_FIELD_NUMBER: _ClassVar[int]
    ENTITLEMENT_FIELD_NUMBER: _ClassVar[int]
    OFFER_FIELD_NUMBER: _ClassVar[int]
    PROVISIONED_SERVICE_FIELD_NUMBER: _ClassVar[int]
    CHANGE_TYPE_FIELD_NUMBER: _ClassVar[int]
    CREATE_TIME_FIELD_NUMBER: _ClassVar[int]
    OPERATOR_TYPE_FIELD_NUMBER: _ClassVar[int]
    PARAMETERS_FIELD_NUMBER: _ClassVar[int]
    OPERATOR_FIELD_NUMBER: _ClassVar[int]
    suspension_reason: _entitlements_pb2.Entitlement.SuspensionReason
    cancellation_reason: EntitlementChange.CancellationReason
    activation_reason: EntitlementChange.ActivationReason
    other_change_reason: str
    entitlement: str
    offer: str
    provisioned_service: _entitlements_pb2.ProvisionedService
    change_type: EntitlementChange.ChangeType
    create_time: _timestamp_pb2.Timestamp
    operator_type: EntitlementChange.OperatorType
    parameters: _containers.RepeatedCompositeFieldContainer[_entitlements_pb2.Parameter]
    operator: str

    def __init__(self, suspension_reason: _Optional[_Union[_entitlements_pb2.Entitlement.SuspensionReason, str]]=..., cancellation_reason: _Optional[_Union[EntitlementChange.CancellationReason, str]]=..., activation_reason: _Optional[_Union[EntitlementChange.ActivationReason, str]]=..., other_change_reason: _Optional[str]=..., entitlement: _Optional[str]=..., offer: _Optional[str]=..., provisioned_service: _Optional[_Union[_entitlements_pb2.ProvisionedService, _Mapping]]=..., change_type: _Optional[_Union[EntitlementChange.ChangeType, str]]=..., create_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]]=..., operator_type: _Optional[_Union[EntitlementChange.OperatorType, str]]=..., parameters: _Optional[_Iterable[_Union[_entitlements_pb2.Parameter, _Mapping]]]=..., operator: _Optional[str]=...) -> None:
        ...