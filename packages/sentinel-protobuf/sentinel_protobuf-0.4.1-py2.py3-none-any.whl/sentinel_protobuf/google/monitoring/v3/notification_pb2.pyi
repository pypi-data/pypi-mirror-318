from google.api import field_behavior_pb2 as _field_behavior_pb2
from google.api import label_pb2 as _label_pb2
from google.api import launch_stage_pb2 as _launch_stage_pb2
from google.api import resource_pb2 as _resource_pb2
from google.monitoring.v3 import common_pb2 as _common_pb2
from google.monitoring.v3 import mutation_record_pb2 as _mutation_record_pb2
from google.protobuf import wrappers_pb2 as _wrappers_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union
DESCRIPTOR: _descriptor.FileDescriptor

class NotificationChannelDescriptor(_message.Message):
    __slots__ = ('name', 'type', 'display_name', 'description', 'labels', 'supported_tiers', 'launch_stage')
    NAME_FIELD_NUMBER: _ClassVar[int]
    TYPE_FIELD_NUMBER: _ClassVar[int]
    DISPLAY_NAME_FIELD_NUMBER: _ClassVar[int]
    DESCRIPTION_FIELD_NUMBER: _ClassVar[int]
    LABELS_FIELD_NUMBER: _ClassVar[int]
    SUPPORTED_TIERS_FIELD_NUMBER: _ClassVar[int]
    LAUNCH_STAGE_FIELD_NUMBER: _ClassVar[int]
    name: str
    type: str
    display_name: str
    description: str
    labels: _containers.RepeatedCompositeFieldContainer[_label_pb2.LabelDescriptor]
    supported_tiers: _containers.RepeatedScalarFieldContainer[_common_pb2.ServiceTier]
    launch_stage: _launch_stage_pb2.LaunchStage

    def __init__(self, name: _Optional[str]=..., type: _Optional[str]=..., display_name: _Optional[str]=..., description: _Optional[str]=..., labels: _Optional[_Iterable[_Union[_label_pb2.LabelDescriptor, _Mapping]]]=..., supported_tiers: _Optional[_Iterable[_Union[_common_pb2.ServiceTier, str]]]=..., launch_stage: _Optional[_Union[_launch_stage_pb2.LaunchStage, str]]=...) -> None:
        ...

class NotificationChannel(_message.Message):
    __slots__ = ('type', 'name', 'display_name', 'description', 'labels', 'user_labels', 'verification_status', 'enabled', 'creation_record', 'mutation_records')

    class VerificationStatus(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        VERIFICATION_STATUS_UNSPECIFIED: _ClassVar[NotificationChannel.VerificationStatus]
        UNVERIFIED: _ClassVar[NotificationChannel.VerificationStatus]
        VERIFIED: _ClassVar[NotificationChannel.VerificationStatus]
    VERIFICATION_STATUS_UNSPECIFIED: NotificationChannel.VerificationStatus
    UNVERIFIED: NotificationChannel.VerificationStatus
    VERIFIED: NotificationChannel.VerificationStatus

    class LabelsEntry(_message.Message):
        __slots__ = ('key', 'value')
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: str

        def __init__(self, key: _Optional[str]=..., value: _Optional[str]=...) -> None:
            ...

    class UserLabelsEntry(_message.Message):
        __slots__ = ('key', 'value')
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: str

        def __init__(self, key: _Optional[str]=..., value: _Optional[str]=...) -> None:
            ...
    TYPE_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    DISPLAY_NAME_FIELD_NUMBER: _ClassVar[int]
    DESCRIPTION_FIELD_NUMBER: _ClassVar[int]
    LABELS_FIELD_NUMBER: _ClassVar[int]
    USER_LABELS_FIELD_NUMBER: _ClassVar[int]
    VERIFICATION_STATUS_FIELD_NUMBER: _ClassVar[int]
    ENABLED_FIELD_NUMBER: _ClassVar[int]
    CREATION_RECORD_FIELD_NUMBER: _ClassVar[int]
    MUTATION_RECORDS_FIELD_NUMBER: _ClassVar[int]
    type: str
    name: str
    display_name: str
    description: str
    labels: _containers.ScalarMap[str, str]
    user_labels: _containers.ScalarMap[str, str]
    verification_status: NotificationChannel.VerificationStatus
    enabled: _wrappers_pb2.BoolValue
    creation_record: _mutation_record_pb2.MutationRecord
    mutation_records: _containers.RepeatedCompositeFieldContainer[_mutation_record_pb2.MutationRecord]

    def __init__(self, type: _Optional[str]=..., name: _Optional[str]=..., display_name: _Optional[str]=..., description: _Optional[str]=..., labels: _Optional[_Mapping[str, str]]=..., user_labels: _Optional[_Mapping[str, str]]=..., verification_status: _Optional[_Union[NotificationChannel.VerificationStatus, str]]=..., enabled: _Optional[_Union[_wrappers_pb2.BoolValue, _Mapping]]=..., creation_record: _Optional[_Union[_mutation_record_pb2.MutationRecord, _Mapping]]=..., mutation_records: _Optional[_Iterable[_Union[_mutation_record_pb2.MutationRecord, _Mapping]]]=...) -> None:
        ...