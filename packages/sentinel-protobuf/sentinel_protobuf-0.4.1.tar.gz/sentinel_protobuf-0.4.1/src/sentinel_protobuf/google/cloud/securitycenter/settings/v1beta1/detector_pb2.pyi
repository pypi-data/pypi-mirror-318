from google.api import field_behavior_pb2 as _field_behavior_pb2
from google.cloud.securitycenter.settings.v1beta1 import billing_settings_pb2 as _billing_settings_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Optional as _Optional, Union as _Union
DESCRIPTOR: _descriptor.FileDescriptor

class Detector(_message.Message):
    __slots__ = ('detector', 'component', 'billing_tier', 'detector_labels')
    DETECTOR_FIELD_NUMBER: _ClassVar[int]
    COMPONENT_FIELD_NUMBER: _ClassVar[int]
    BILLING_TIER_FIELD_NUMBER: _ClassVar[int]
    DETECTOR_LABELS_FIELD_NUMBER: _ClassVar[int]
    detector: str
    component: str
    billing_tier: _billing_settings_pb2.BillingTier
    detector_labels: _containers.RepeatedScalarFieldContainer[str]

    def __init__(self, detector: _Optional[str]=..., component: _Optional[str]=..., billing_tier: _Optional[_Union[_billing_settings_pb2.BillingTier, str]]=..., detector_labels: _Optional[_Iterable[str]]=...) -> None:
        ...