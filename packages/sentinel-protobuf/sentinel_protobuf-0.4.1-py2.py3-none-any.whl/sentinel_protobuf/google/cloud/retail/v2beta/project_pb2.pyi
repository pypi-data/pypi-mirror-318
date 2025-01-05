from google.api import field_behavior_pb2 as _field_behavior_pb2
from google.api import resource_pb2 as _resource_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union
DESCRIPTOR: _descriptor.FileDescriptor

class AlertConfig(_message.Message):
    __slots__ = ('name', 'alert_policies')

    class AlertPolicy(_message.Message):
        __slots__ = ('alert_group', 'enroll_status', 'recipients')

        class EnrollStatus(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
            __slots__ = ()
            ENROLL_STATUS_UNSPECIFIED: _ClassVar[AlertConfig.AlertPolicy.EnrollStatus]
            ENROLLED: _ClassVar[AlertConfig.AlertPolicy.EnrollStatus]
            DECLINED: _ClassVar[AlertConfig.AlertPolicy.EnrollStatus]
        ENROLL_STATUS_UNSPECIFIED: AlertConfig.AlertPolicy.EnrollStatus
        ENROLLED: AlertConfig.AlertPolicy.EnrollStatus
        DECLINED: AlertConfig.AlertPolicy.EnrollStatus

        class Recipient(_message.Message):
            __slots__ = ('email_address',)
            EMAIL_ADDRESS_FIELD_NUMBER: _ClassVar[int]
            email_address: str

            def __init__(self, email_address: _Optional[str]=...) -> None:
                ...
        ALERT_GROUP_FIELD_NUMBER: _ClassVar[int]
        ENROLL_STATUS_FIELD_NUMBER: _ClassVar[int]
        RECIPIENTS_FIELD_NUMBER: _ClassVar[int]
        alert_group: str
        enroll_status: AlertConfig.AlertPolicy.EnrollStatus
        recipients: _containers.RepeatedCompositeFieldContainer[AlertConfig.AlertPolicy.Recipient]

        def __init__(self, alert_group: _Optional[str]=..., enroll_status: _Optional[_Union[AlertConfig.AlertPolicy.EnrollStatus, str]]=..., recipients: _Optional[_Iterable[_Union[AlertConfig.AlertPolicy.Recipient, _Mapping]]]=...) -> None:
            ...
    NAME_FIELD_NUMBER: _ClassVar[int]
    ALERT_POLICIES_FIELD_NUMBER: _ClassVar[int]
    name: str
    alert_policies: _containers.RepeatedCompositeFieldContainer[AlertConfig.AlertPolicy]

    def __init__(self, name: _Optional[str]=..., alert_policies: _Optional[_Iterable[_Union[AlertConfig.AlertPolicy, _Mapping]]]=...) -> None:
        ...