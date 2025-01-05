from google.protobuf import timestamp_pb2 as _timestamp_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union
DESCRIPTOR: _descriptor.FileDescriptor

class ContinuousValidationEvent(_message.Message):
    __slots__ = ('pod_event', 'config_error_event')

    class ContinuousValidationPodEvent(_message.Message):
        __slots__ = ('pod_namespace', 'pod', 'policy_name', 'deploy_time', 'end_time', 'verdict', 'images')

        class PolicyConformanceVerdict(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
            __slots__ = ()
            POLICY_CONFORMANCE_VERDICT_UNSPECIFIED: _ClassVar[ContinuousValidationEvent.ContinuousValidationPodEvent.PolicyConformanceVerdict]
            VIOLATES_POLICY: _ClassVar[ContinuousValidationEvent.ContinuousValidationPodEvent.PolicyConformanceVerdict]
        POLICY_CONFORMANCE_VERDICT_UNSPECIFIED: ContinuousValidationEvent.ContinuousValidationPodEvent.PolicyConformanceVerdict
        VIOLATES_POLICY: ContinuousValidationEvent.ContinuousValidationPodEvent.PolicyConformanceVerdict

        class ImageDetails(_message.Message):
            __slots__ = ('image', 'container_name', 'container_type', 'result', 'description', 'check_results')

            class ContainerType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
                __slots__ = ()
                CONTAINER_TYPE_UNSPECIFIED: _ClassVar[ContinuousValidationEvent.ContinuousValidationPodEvent.ImageDetails.ContainerType]
                CONTAINER: _ClassVar[ContinuousValidationEvent.ContinuousValidationPodEvent.ImageDetails.ContainerType]
                INIT_CONTAINER: _ClassVar[ContinuousValidationEvent.ContinuousValidationPodEvent.ImageDetails.ContainerType]
                EPHEMERAL_CONTAINER: _ClassVar[ContinuousValidationEvent.ContinuousValidationPodEvent.ImageDetails.ContainerType]
            CONTAINER_TYPE_UNSPECIFIED: ContinuousValidationEvent.ContinuousValidationPodEvent.ImageDetails.ContainerType
            CONTAINER: ContinuousValidationEvent.ContinuousValidationPodEvent.ImageDetails.ContainerType
            INIT_CONTAINER: ContinuousValidationEvent.ContinuousValidationPodEvent.ImageDetails.ContainerType
            EPHEMERAL_CONTAINER: ContinuousValidationEvent.ContinuousValidationPodEvent.ImageDetails.ContainerType

            class AuditResult(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
                __slots__ = ()
                AUDIT_RESULT_UNSPECIFIED: _ClassVar[ContinuousValidationEvent.ContinuousValidationPodEvent.ImageDetails.AuditResult]
                ALLOW: _ClassVar[ContinuousValidationEvent.ContinuousValidationPodEvent.ImageDetails.AuditResult]
                DENY: _ClassVar[ContinuousValidationEvent.ContinuousValidationPodEvent.ImageDetails.AuditResult]
            AUDIT_RESULT_UNSPECIFIED: ContinuousValidationEvent.ContinuousValidationPodEvent.ImageDetails.AuditResult
            ALLOW: ContinuousValidationEvent.ContinuousValidationPodEvent.ImageDetails.AuditResult
            DENY: ContinuousValidationEvent.ContinuousValidationPodEvent.ImageDetails.AuditResult

            class CheckResult(_message.Message):
                __slots__ = ('check_set_index', 'check_set_name', 'check_set_scope', 'check_index', 'check_name', 'check_type', 'verdict', 'explanation')

                class CheckVerdict(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
                    __slots__ = ()
                    CHECK_VERDICT_UNSPECIFIED: _ClassVar[ContinuousValidationEvent.ContinuousValidationPodEvent.ImageDetails.CheckResult.CheckVerdict]
                    NON_CONFORMANT: _ClassVar[ContinuousValidationEvent.ContinuousValidationPodEvent.ImageDetails.CheckResult.CheckVerdict]
                CHECK_VERDICT_UNSPECIFIED: ContinuousValidationEvent.ContinuousValidationPodEvent.ImageDetails.CheckResult.CheckVerdict
                NON_CONFORMANT: ContinuousValidationEvent.ContinuousValidationPodEvent.ImageDetails.CheckResult.CheckVerdict

                class CheckSetScope(_message.Message):
                    __slots__ = ('kubernetes_service_account', 'kubernetes_namespace')
                    KUBERNETES_SERVICE_ACCOUNT_FIELD_NUMBER: _ClassVar[int]
                    KUBERNETES_NAMESPACE_FIELD_NUMBER: _ClassVar[int]
                    kubernetes_service_account: str
                    kubernetes_namespace: str

                    def __init__(self, kubernetes_service_account: _Optional[str]=..., kubernetes_namespace: _Optional[str]=...) -> None:
                        ...
                CHECK_SET_INDEX_FIELD_NUMBER: _ClassVar[int]
                CHECK_SET_NAME_FIELD_NUMBER: _ClassVar[int]
                CHECK_SET_SCOPE_FIELD_NUMBER: _ClassVar[int]
                CHECK_INDEX_FIELD_NUMBER: _ClassVar[int]
                CHECK_NAME_FIELD_NUMBER: _ClassVar[int]
                CHECK_TYPE_FIELD_NUMBER: _ClassVar[int]
                VERDICT_FIELD_NUMBER: _ClassVar[int]
                EXPLANATION_FIELD_NUMBER: _ClassVar[int]
                check_set_index: str
                check_set_name: str
                check_set_scope: ContinuousValidationEvent.ContinuousValidationPodEvent.ImageDetails.CheckResult.CheckSetScope
                check_index: str
                check_name: str
                check_type: str
                verdict: ContinuousValidationEvent.ContinuousValidationPodEvent.ImageDetails.CheckResult.CheckVerdict
                explanation: str

                def __init__(self, check_set_index: _Optional[str]=..., check_set_name: _Optional[str]=..., check_set_scope: _Optional[_Union[ContinuousValidationEvent.ContinuousValidationPodEvent.ImageDetails.CheckResult.CheckSetScope, _Mapping]]=..., check_index: _Optional[str]=..., check_name: _Optional[str]=..., check_type: _Optional[str]=..., verdict: _Optional[_Union[ContinuousValidationEvent.ContinuousValidationPodEvent.ImageDetails.CheckResult.CheckVerdict, str]]=..., explanation: _Optional[str]=...) -> None:
                    ...
            IMAGE_FIELD_NUMBER: _ClassVar[int]
            CONTAINER_NAME_FIELD_NUMBER: _ClassVar[int]
            CONTAINER_TYPE_FIELD_NUMBER: _ClassVar[int]
            RESULT_FIELD_NUMBER: _ClassVar[int]
            DESCRIPTION_FIELD_NUMBER: _ClassVar[int]
            CHECK_RESULTS_FIELD_NUMBER: _ClassVar[int]
            image: str
            container_name: str
            container_type: ContinuousValidationEvent.ContinuousValidationPodEvent.ImageDetails.ContainerType
            result: ContinuousValidationEvent.ContinuousValidationPodEvent.ImageDetails.AuditResult
            description: str
            check_results: _containers.RepeatedCompositeFieldContainer[ContinuousValidationEvent.ContinuousValidationPodEvent.ImageDetails.CheckResult]

            def __init__(self, image: _Optional[str]=..., container_name: _Optional[str]=..., container_type: _Optional[_Union[ContinuousValidationEvent.ContinuousValidationPodEvent.ImageDetails.ContainerType, str]]=..., result: _Optional[_Union[ContinuousValidationEvent.ContinuousValidationPodEvent.ImageDetails.AuditResult, str]]=..., description: _Optional[str]=..., check_results: _Optional[_Iterable[_Union[ContinuousValidationEvent.ContinuousValidationPodEvent.ImageDetails.CheckResult, _Mapping]]]=...) -> None:
                ...
        POD_NAMESPACE_FIELD_NUMBER: _ClassVar[int]
        POD_FIELD_NUMBER: _ClassVar[int]
        POLICY_NAME_FIELD_NUMBER: _ClassVar[int]
        DEPLOY_TIME_FIELD_NUMBER: _ClassVar[int]
        END_TIME_FIELD_NUMBER: _ClassVar[int]
        VERDICT_FIELD_NUMBER: _ClassVar[int]
        IMAGES_FIELD_NUMBER: _ClassVar[int]
        pod_namespace: str
        pod: str
        policy_name: str
        deploy_time: _timestamp_pb2.Timestamp
        end_time: _timestamp_pb2.Timestamp
        verdict: ContinuousValidationEvent.ContinuousValidationPodEvent.PolicyConformanceVerdict
        images: _containers.RepeatedCompositeFieldContainer[ContinuousValidationEvent.ContinuousValidationPodEvent.ImageDetails]

        def __init__(self, pod_namespace: _Optional[str]=..., pod: _Optional[str]=..., policy_name: _Optional[str]=..., deploy_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]]=..., end_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]]=..., verdict: _Optional[_Union[ContinuousValidationEvent.ContinuousValidationPodEvent.PolicyConformanceVerdict, str]]=..., images: _Optional[_Iterable[_Union[ContinuousValidationEvent.ContinuousValidationPodEvent.ImageDetails, _Mapping]]]=...) -> None:
            ...

    class ConfigErrorEvent(_message.Message):
        __slots__ = ('description',)
        DESCRIPTION_FIELD_NUMBER: _ClassVar[int]
        description: str

        def __init__(self, description: _Optional[str]=...) -> None:
            ...
    POD_EVENT_FIELD_NUMBER: _ClassVar[int]
    CONFIG_ERROR_EVENT_FIELD_NUMBER: _ClassVar[int]
    pod_event: ContinuousValidationEvent.ContinuousValidationPodEvent
    config_error_event: ContinuousValidationEvent.ConfigErrorEvent

    def __init__(self, pod_event: _Optional[_Union[ContinuousValidationEvent.ContinuousValidationPodEvent, _Mapping]]=..., config_error_event: _Optional[_Union[ContinuousValidationEvent.ConfigErrorEvent, _Mapping]]=...) -> None:
        ...