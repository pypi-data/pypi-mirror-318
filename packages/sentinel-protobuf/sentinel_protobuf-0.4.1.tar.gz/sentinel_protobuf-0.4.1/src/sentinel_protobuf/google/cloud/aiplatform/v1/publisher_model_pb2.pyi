from google.api import field_behavior_pb2 as _field_behavior_pb2
from google.api import resource_pb2 as _resource_pb2
from google.cloud.aiplatform.v1 import machine_resources_pb2 as _machine_resources_pb2
from google.cloud.aiplatform.v1 import model_pb2 as _model_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class PublisherModel(_message.Message):
    __slots__ = ("name", "version_id", "open_source_category", "supported_actions", "frameworks", "launch_stage", "version_state", "publisher_model_template", "predict_schemata")
    class OpenSourceCategory(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        OPEN_SOURCE_CATEGORY_UNSPECIFIED: _ClassVar[PublisherModel.OpenSourceCategory]
        PROPRIETARY: _ClassVar[PublisherModel.OpenSourceCategory]
        GOOGLE_OWNED_OSS_WITH_GOOGLE_CHECKPOINT: _ClassVar[PublisherModel.OpenSourceCategory]
        THIRD_PARTY_OWNED_OSS_WITH_GOOGLE_CHECKPOINT: _ClassVar[PublisherModel.OpenSourceCategory]
        GOOGLE_OWNED_OSS: _ClassVar[PublisherModel.OpenSourceCategory]
        THIRD_PARTY_OWNED_OSS: _ClassVar[PublisherModel.OpenSourceCategory]
    OPEN_SOURCE_CATEGORY_UNSPECIFIED: PublisherModel.OpenSourceCategory
    PROPRIETARY: PublisherModel.OpenSourceCategory
    GOOGLE_OWNED_OSS_WITH_GOOGLE_CHECKPOINT: PublisherModel.OpenSourceCategory
    THIRD_PARTY_OWNED_OSS_WITH_GOOGLE_CHECKPOINT: PublisherModel.OpenSourceCategory
    GOOGLE_OWNED_OSS: PublisherModel.OpenSourceCategory
    THIRD_PARTY_OWNED_OSS: PublisherModel.OpenSourceCategory
    class LaunchStage(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        LAUNCH_STAGE_UNSPECIFIED: _ClassVar[PublisherModel.LaunchStage]
        EXPERIMENTAL: _ClassVar[PublisherModel.LaunchStage]
        PRIVATE_PREVIEW: _ClassVar[PublisherModel.LaunchStage]
        PUBLIC_PREVIEW: _ClassVar[PublisherModel.LaunchStage]
        GA: _ClassVar[PublisherModel.LaunchStage]
    LAUNCH_STAGE_UNSPECIFIED: PublisherModel.LaunchStage
    EXPERIMENTAL: PublisherModel.LaunchStage
    PRIVATE_PREVIEW: PublisherModel.LaunchStage
    PUBLIC_PREVIEW: PublisherModel.LaunchStage
    GA: PublisherModel.LaunchStage
    class VersionState(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        VERSION_STATE_UNSPECIFIED: _ClassVar[PublisherModel.VersionState]
        VERSION_STATE_STABLE: _ClassVar[PublisherModel.VersionState]
        VERSION_STATE_UNSTABLE: _ClassVar[PublisherModel.VersionState]
    VERSION_STATE_UNSPECIFIED: PublisherModel.VersionState
    VERSION_STATE_STABLE: PublisherModel.VersionState
    VERSION_STATE_UNSTABLE: PublisherModel.VersionState
    class ResourceReference(_message.Message):
        __slots__ = ("uri", "resource_name", "use_case", "description")
        URI_FIELD_NUMBER: _ClassVar[int]
        RESOURCE_NAME_FIELD_NUMBER: _ClassVar[int]
        USE_CASE_FIELD_NUMBER: _ClassVar[int]
        DESCRIPTION_FIELD_NUMBER: _ClassVar[int]
        uri: str
        resource_name: str
        use_case: str
        description: str
        def __init__(self, uri: _Optional[str] = ..., resource_name: _Optional[str] = ..., use_case: _Optional[str] = ..., description: _Optional[str] = ...) -> None: ...
    class Documentation(_message.Message):
        __slots__ = ("title", "content")
        TITLE_FIELD_NUMBER: _ClassVar[int]
        CONTENT_FIELD_NUMBER: _ClassVar[int]
        title: str
        content: str
        def __init__(self, title: _Optional[str] = ..., content: _Optional[str] = ...) -> None: ...
    class CallToAction(_message.Message):
        __slots__ = ("view_rest_api", "open_notebook", "open_notebooks", "create_application", "open_fine_tuning_pipeline", "open_fine_tuning_pipelines", "open_prompt_tuning_pipeline", "open_genie", "deploy", "deploy_gke", "open_generation_ai_studio", "request_access", "open_evaluation_pipeline")
        class RegionalResourceReferences(_message.Message):
            __slots__ = ("references", "title", "resource_title", "resource_use_case", "resource_description")
            class ReferencesEntry(_message.Message):
                __slots__ = ("key", "value")
                KEY_FIELD_NUMBER: _ClassVar[int]
                VALUE_FIELD_NUMBER: _ClassVar[int]
                key: str
                value: PublisherModel.ResourceReference
                def __init__(self, key: _Optional[str] = ..., value: _Optional[_Union[PublisherModel.ResourceReference, _Mapping]] = ...) -> None: ...
            REFERENCES_FIELD_NUMBER: _ClassVar[int]
            TITLE_FIELD_NUMBER: _ClassVar[int]
            RESOURCE_TITLE_FIELD_NUMBER: _ClassVar[int]
            RESOURCE_USE_CASE_FIELD_NUMBER: _ClassVar[int]
            RESOURCE_DESCRIPTION_FIELD_NUMBER: _ClassVar[int]
            references: _containers.MessageMap[str, PublisherModel.ResourceReference]
            title: str
            resource_title: str
            resource_use_case: str
            resource_description: str
            def __init__(self, references: _Optional[_Mapping[str, PublisherModel.ResourceReference]] = ..., title: _Optional[str] = ..., resource_title: _Optional[str] = ..., resource_use_case: _Optional[str] = ..., resource_description: _Optional[str] = ...) -> None: ...
        class ViewRestApi(_message.Message):
            __slots__ = ("documentations", "title")
            DOCUMENTATIONS_FIELD_NUMBER: _ClassVar[int]
            TITLE_FIELD_NUMBER: _ClassVar[int]
            documentations: _containers.RepeatedCompositeFieldContainer[PublisherModel.Documentation]
            title: str
            def __init__(self, documentations: _Optional[_Iterable[_Union[PublisherModel.Documentation, _Mapping]]] = ..., title: _Optional[str] = ...) -> None: ...
        class OpenNotebooks(_message.Message):
            __slots__ = ("notebooks",)
            NOTEBOOKS_FIELD_NUMBER: _ClassVar[int]
            notebooks: _containers.RepeatedCompositeFieldContainer[PublisherModel.CallToAction.RegionalResourceReferences]
            def __init__(self, notebooks: _Optional[_Iterable[_Union[PublisherModel.CallToAction.RegionalResourceReferences, _Mapping]]] = ...) -> None: ...
        class OpenFineTuningPipelines(_message.Message):
            __slots__ = ("fine_tuning_pipelines",)
            FINE_TUNING_PIPELINES_FIELD_NUMBER: _ClassVar[int]
            fine_tuning_pipelines: _containers.RepeatedCompositeFieldContainer[PublisherModel.CallToAction.RegionalResourceReferences]
            def __init__(self, fine_tuning_pipelines: _Optional[_Iterable[_Union[PublisherModel.CallToAction.RegionalResourceReferences, _Mapping]]] = ...) -> None: ...
        class Deploy(_message.Message):
            __slots__ = ("dedicated_resources", "automatic_resources", "shared_resources", "model_display_name", "large_model_reference", "container_spec", "artifact_uri", "deploy_task_name", "deploy_metadata", "title", "public_artifact_uri")
            class DeployMetadata(_message.Message):
                __slots__ = ("labels", "sample_request")
                class LabelsEntry(_message.Message):
                    __slots__ = ("key", "value")
                    KEY_FIELD_NUMBER: _ClassVar[int]
                    VALUE_FIELD_NUMBER: _ClassVar[int]
                    key: str
                    value: str
                    def __init__(self, key: _Optional[str] = ..., value: _Optional[str] = ...) -> None: ...
                LABELS_FIELD_NUMBER: _ClassVar[int]
                SAMPLE_REQUEST_FIELD_NUMBER: _ClassVar[int]
                labels: _containers.ScalarMap[str, str]
                sample_request: str
                def __init__(self, labels: _Optional[_Mapping[str, str]] = ..., sample_request: _Optional[str] = ...) -> None: ...
            DEDICATED_RESOURCES_FIELD_NUMBER: _ClassVar[int]
            AUTOMATIC_RESOURCES_FIELD_NUMBER: _ClassVar[int]
            SHARED_RESOURCES_FIELD_NUMBER: _ClassVar[int]
            MODEL_DISPLAY_NAME_FIELD_NUMBER: _ClassVar[int]
            LARGE_MODEL_REFERENCE_FIELD_NUMBER: _ClassVar[int]
            CONTAINER_SPEC_FIELD_NUMBER: _ClassVar[int]
            ARTIFACT_URI_FIELD_NUMBER: _ClassVar[int]
            DEPLOY_TASK_NAME_FIELD_NUMBER: _ClassVar[int]
            DEPLOY_METADATA_FIELD_NUMBER: _ClassVar[int]
            TITLE_FIELD_NUMBER: _ClassVar[int]
            PUBLIC_ARTIFACT_URI_FIELD_NUMBER: _ClassVar[int]
            dedicated_resources: _machine_resources_pb2.DedicatedResources
            automatic_resources: _machine_resources_pb2.AutomaticResources
            shared_resources: str
            model_display_name: str
            large_model_reference: _model_pb2.LargeModelReference
            container_spec: _model_pb2.ModelContainerSpec
            artifact_uri: str
            deploy_task_name: str
            deploy_metadata: PublisherModel.CallToAction.Deploy.DeployMetadata
            title: str
            public_artifact_uri: str
            def __init__(self, dedicated_resources: _Optional[_Union[_machine_resources_pb2.DedicatedResources, _Mapping]] = ..., automatic_resources: _Optional[_Union[_machine_resources_pb2.AutomaticResources, _Mapping]] = ..., shared_resources: _Optional[str] = ..., model_display_name: _Optional[str] = ..., large_model_reference: _Optional[_Union[_model_pb2.LargeModelReference, _Mapping]] = ..., container_spec: _Optional[_Union[_model_pb2.ModelContainerSpec, _Mapping]] = ..., artifact_uri: _Optional[str] = ..., deploy_task_name: _Optional[str] = ..., deploy_metadata: _Optional[_Union[PublisherModel.CallToAction.Deploy.DeployMetadata, _Mapping]] = ..., title: _Optional[str] = ..., public_artifact_uri: _Optional[str] = ...) -> None: ...
        class DeployGke(_message.Message):
            __slots__ = ("gke_yaml_configs",)
            GKE_YAML_CONFIGS_FIELD_NUMBER: _ClassVar[int]
            gke_yaml_configs: _containers.RepeatedScalarFieldContainer[str]
            def __init__(self, gke_yaml_configs: _Optional[_Iterable[str]] = ...) -> None: ...
        VIEW_REST_API_FIELD_NUMBER: _ClassVar[int]
        OPEN_NOTEBOOK_FIELD_NUMBER: _ClassVar[int]
        OPEN_NOTEBOOKS_FIELD_NUMBER: _ClassVar[int]
        CREATE_APPLICATION_FIELD_NUMBER: _ClassVar[int]
        OPEN_FINE_TUNING_PIPELINE_FIELD_NUMBER: _ClassVar[int]
        OPEN_FINE_TUNING_PIPELINES_FIELD_NUMBER: _ClassVar[int]
        OPEN_PROMPT_TUNING_PIPELINE_FIELD_NUMBER: _ClassVar[int]
        OPEN_GENIE_FIELD_NUMBER: _ClassVar[int]
        DEPLOY_FIELD_NUMBER: _ClassVar[int]
        DEPLOY_GKE_FIELD_NUMBER: _ClassVar[int]
        OPEN_GENERATION_AI_STUDIO_FIELD_NUMBER: _ClassVar[int]
        REQUEST_ACCESS_FIELD_NUMBER: _ClassVar[int]
        OPEN_EVALUATION_PIPELINE_FIELD_NUMBER: _ClassVar[int]
        view_rest_api: PublisherModel.CallToAction.ViewRestApi
        open_notebook: PublisherModel.CallToAction.RegionalResourceReferences
        open_notebooks: PublisherModel.CallToAction.OpenNotebooks
        create_application: PublisherModel.CallToAction.RegionalResourceReferences
        open_fine_tuning_pipeline: PublisherModel.CallToAction.RegionalResourceReferences
        open_fine_tuning_pipelines: PublisherModel.CallToAction.OpenFineTuningPipelines
        open_prompt_tuning_pipeline: PublisherModel.CallToAction.RegionalResourceReferences
        open_genie: PublisherModel.CallToAction.RegionalResourceReferences
        deploy: PublisherModel.CallToAction.Deploy
        deploy_gke: PublisherModel.CallToAction.DeployGke
        open_generation_ai_studio: PublisherModel.CallToAction.RegionalResourceReferences
        request_access: PublisherModel.CallToAction.RegionalResourceReferences
        open_evaluation_pipeline: PublisherModel.CallToAction.RegionalResourceReferences
        def __init__(self, view_rest_api: _Optional[_Union[PublisherModel.CallToAction.ViewRestApi, _Mapping]] = ..., open_notebook: _Optional[_Union[PublisherModel.CallToAction.RegionalResourceReferences, _Mapping]] = ..., open_notebooks: _Optional[_Union[PublisherModel.CallToAction.OpenNotebooks, _Mapping]] = ..., create_application: _Optional[_Union[PublisherModel.CallToAction.RegionalResourceReferences, _Mapping]] = ..., open_fine_tuning_pipeline: _Optional[_Union[PublisherModel.CallToAction.RegionalResourceReferences, _Mapping]] = ..., open_fine_tuning_pipelines: _Optional[_Union[PublisherModel.CallToAction.OpenFineTuningPipelines, _Mapping]] = ..., open_prompt_tuning_pipeline: _Optional[_Union[PublisherModel.CallToAction.RegionalResourceReferences, _Mapping]] = ..., open_genie: _Optional[_Union[PublisherModel.CallToAction.RegionalResourceReferences, _Mapping]] = ..., deploy: _Optional[_Union[PublisherModel.CallToAction.Deploy, _Mapping]] = ..., deploy_gke: _Optional[_Union[PublisherModel.CallToAction.DeployGke, _Mapping]] = ..., open_generation_ai_studio: _Optional[_Union[PublisherModel.CallToAction.RegionalResourceReferences, _Mapping]] = ..., request_access: _Optional[_Union[PublisherModel.CallToAction.RegionalResourceReferences, _Mapping]] = ..., open_evaluation_pipeline: _Optional[_Union[PublisherModel.CallToAction.RegionalResourceReferences, _Mapping]] = ...) -> None: ...
    NAME_FIELD_NUMBER: _ClassVar[int]
    VERSION_ID_FIELD_NUMBER: _ClassVar[int]
    OPEN_SOURCE_CATEGORY_FIELD_NUMBER: _ClassVar[int]
    SUPPORTED_ACTIONS_FIELD_NUMBER: _ClassVar[int]
    FRAMEWORKS_FIELD_NUMBER: _ClassVar[int]
    LAUNCH_STAGE_FIELD_NUMBER: _ClassVar[int]
    VERSION_STATE_FIELD_NUMBER: _ClassVar[int]
    PUBLISHER_MODEL_TEMPLATE_FIELD_NUMBER: _ClassVar[int]
    PREDICT_SCHEMATA_FIELD_NUMBER: _ClassVar[int]
    name: str
    version_id: str
    open_source_category: PublisherModel.OpenSourceCategory
    supported_actions: PublisherModel.CallToAction
    frameworks: _containers.RepeatedScalarFieldContainer[str]
    launch_stage: PublisherModel.LaunchStage
    version_state: PublisherModel.VersionState
    publisher_model_template: str
    predict_schemata: _model_pb2.PredictSchemata
    def __init__(self, name: _Optional[str] = ..., version_id: _Optional[str] = ..., open_source_category: _Optional[_Union[PublisherModel.OpenSourceCategory, str]] = ..., supported_actions: _Optional[_Union[PublisherModel.CallToAction, _Mapping]] = ..., frameworks: _Optional[_Iterable[str]] = ..., launch_stage: _Optional[_Union[PublisherModel.LaunchStage, str]] = ..., version_state: _Optional[_Union[PublisherModel.VersionState, str]] = ..., publisher_model_template: _Optional[str] = ..., predict_schemata: _Optional[_Union[_model_pb2.PredictSchemata, _Mapping]] = ...) -> None: ...
