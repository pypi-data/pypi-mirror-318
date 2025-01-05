from google.api import resource_pb2 as _resource_pb2
from google.cloud.automl.v1 import image_pb2 as _image_pb2
from google.cloud.automl.v1 import text_pb2 as _text_pb2
from google.cloud.automl.v1 import translation_pb2 as _translation_pb2
from google.protobuf import timestamp_pb2 as _timestamp_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Mapping as _Mapping, Optional as _Optional, Union as _Union
DESCRIPTOR: _descriptor.FileDescriptor

class Model(_message.Message):
    __slots__ = ('translation_model_metadata', 'image_classification_model_metadata', 'text_classification_model_metadata', 'image_object_detection_model_metadata', 'text_extraction_model_metadata', 'text_sentiment_model_metadata', 'name', 'display_name', 'dataset_id', 'create_time', 'update_time', 'deployment_state', 'etag', 'labels')

    class DeploymentState(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        DEPLOYMENT_STATE_UNSPECIFIED: _ClassVar[Model.DeploymentState]
        DEPLOYED: _ClassVar[Model.DeploymentState]
        UNDEPLOYED: _ClassVar[Model.DeploymentState]
    DEPLOYMENT_STATE_UNSPECIFIED: Model.DeploymentState
    DEPLOYED: Model.DeploymentState
    UNDEPLOYED: Model.DeploymentState

    class LabelsEntry(_message.Message):
        __slots__ = ('key', 'value')
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: str

        def __init__(self, key: _Optional[str]=..., value: _Optional[str]=...) -> None:
            ...
    TRANSLATION_MODEL_METADATA_FIELD_NUMBER: _ClassVar[int]
    IMAGE_CLASSIFICATION_MODEL_METADATA_FIELD_NUMBER: _ClassVar[int]
    TEXT_CLASSIFICATION_MODEL_METADATA_FIELD_NUMBER: _ClassVar[int]
    IMAGE_OBJECT_DETECTION_MODEL_METADATA_FIELD_NUMBER: _ClassVar[int]
    TEXT_EXTRACTION_MODEL_METADATA_FIELD_NUMBER: _ClassVar[int]
    TEXT_SENTIMENT_MODEL_METADATA_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    DISPLAY_NAME_FIELD_NUMBER: _ClassVar[int]
    DATASET_ID_FIELD_NUMBER: _ClassVar[int]
    CREATE_TIME_FIELD_NUMBER: _ClassVar[int]
    UPDATE_TIME_FIELD_NUMBER: _ClassVar[int]
    DEPLOYMENT_STATE_FIELD_NUMBER: _ClassVar[int]
    ETAG_FIELD_NUMBER: _ClassVar[int]
    LABELS_FIELD_NUMBER: _ClassVar[int]
    translation_model_metadata: _translation_pb2.TranslationModelMetadata
    image_classification_model_metadata: _image_pb2.ImageClassificationModelMetadata
    text_classification_model_metadata: _text_pb2.TextClassificationModelMetadata
    image_object_detection_model_metadata: _image_pb2.ImageObjectDetectionModelMetadata
    text_extraction_model_metadata: _text_pb2.TextExtractionModelMetadata
    text_sentiment_model_metadata: _text_pb2.TextSentimentModelMetadata
    name: str
    display_name: str
    dataset_id: str
    create_time: _timestamp_pb2.Timestamp
    update_time: _timestamp_pb2.Timestamp
    deployment_state: Model.DeploymentState
    etag: str
    labels: _containers.ScalarMap[str, str]

    def __init__(self, translation_model_metadata: _Optional[_Union[_translation_pb2.TranslationModelMetadata, _Mapping]]=..., image_classification_model_metadata: _Optional[_Union[_image_pb2.ImageClassificationModelMetadata, _Mapping]]=..., text_classification_model_metadata: _Optional[_Union[_text_pb2.TextClassificationModelMetadata, _Mapping]]=..., image_object_detection_model_metadata: _Optional[_Union[_image_pb2.ImageObjectDetectionModelMetadata, _Mapping]]=..., text_extraction_model_metadata: _Optional[_Union[_text_pb2.TextExtractionModelMetadata, _Mapping]]=..., text_sentiment_model_metadata: _Optional[_Union[_text_pb2.TextSentimentModelMetadata, _Mapping]]=..., name: _Optional[str]=..., display_name: _Optional[str]=..., dataset_id: _Optional[str]=..., create_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]]=..., update_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]]=..., deployment_state: _Optional[_Union[Model.DeploymentState, str]]=..., etag: _Optional[str]=..., labels: _Optional[_Mapping[str, str]]=...) -> None:
        ...