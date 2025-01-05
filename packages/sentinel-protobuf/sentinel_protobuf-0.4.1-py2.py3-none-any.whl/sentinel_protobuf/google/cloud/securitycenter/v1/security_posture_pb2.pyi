from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union
DESCRIPTOR: _descriptor.FileDescriptor

class SecurityPosture(_message.Message):
    __slots__ = ('name', 'revision_id', 'posture_deployment_resource', 'posture_deployment', 'changed_policy', 'policy_set', 'policy', 'policy_drift_details')

    class PolicyDriftDetails(_message.Message):
        __slots__ = ('field', 'expected_value', 'detected_value')
        FIELD_FIELD_NUMBER: _ClassVar[int]
        EXPECTED_VALUE_FIELD_NUMBER: _ClassVar[int]
        DETECTED_VALUE_FIELD_NUMBER: _ClassVar[int]
        field: str
        expected_value: str
        detected_value: str

        def __init__(self, field: _Optional[str]=..., expected_value: _Optional[str]=..., detected_value: _Optional[str]=...) -> None:
            ...
    NAME_FIELD_NUMBER: _ClassVar[int]
    REVISION_ID_FIELD_NUMBER: _ClassVar[int]
    POSTURE_DEPLOYMENT_RESOURCE_FIELD_NUMBER: _ClassVar[int]
    POSTURE_DEPLOYMENT_FIELD_NUMBER: _ClassVar[int]
    CHANGED_POLICY_FIELD_NUMBER: _ClassVar[int]
    POLICY_SET_FIELD_NUMBER: _ClassVar[int]
    POLICY_FIELD_NUMBER: _ClassVar[int]
    POLICY_DRIFT_DETAILS_FIELD_NUMBER: _ClassVar[int]
    name: str
    revision_id: str
    posture_deployment_resource: str
    posture_deployment: str
    changed_policy: str
    policy_set: str
    policy: str
    policy_drift_details: _containers.RepeatedCompositeFieldContainer[SecurityPosture.PolicyDriftDetails]

    def __init__(self, name: _Optional[str]=..., revision_id: _Optional[str]=..., posture_deployment_resource: _Optional[str]=..., posture_deployment: _Optional[str]=..., changed_policy: _Optional[str]=..., policy_set: _Optional[str]=..., policy: _Optional[str]=..., policy_drift_details: _Optional[_Iterable[_Union[SecurityPosture.PolicyDriftDetails, _Mapping]]]=...) -> None:
        ...