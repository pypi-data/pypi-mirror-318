from google.api import field_behavior_pb2 as _field_behavior_pb2
from google.protobuf import timestamp_pb2 as _timestamp_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union
DESCRIPTOR: _descriptor.FileDescriptor

class OperationMetadata(_message.Message):
    __slots__ = ('create_time', 'end_time', 'target', 'verb', 'status_message', 'requested_cancellation', 'api_version')
    CREATE_TIME_FIELD_NUMBER: _ClassVar[int]
    END_TIME_FIELD_NUMBER: _ClassVar[int]
    TARGET_FIELD_NUMBER: _ClassVar[int]
    VERB_FIELD_NUMBER: _ClassVar[int]
    STATUS_MESSAGE_FIELD_NUMBER: _ClassVar[int]
    REQUESTED_CANCELLATION_FIELD_NUMBER: _ClassVar[int]
    API_VERSION_FIELD_NUMBER: _ClassVar[int]
    create_time: _timestamp_pb2.Timestamp
    end_time: _timestamp_pb2.Timestamp
    target: str
    verb: str
    status_message: str
    requested_cancellation: bool
    api_version: str

    def __init__(self, create_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]]=..., end_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]]=..., target: _Optional[str]=..., verb: _Optional[str]=..., status_message: _Optional[str]=..., requested_cancellation: bool=..., api_version: _Optional[str]=...) -> None:
        ...

class TrafficPortSelector(_message.Message):
    __slots__ = ('ports',)
    PORTS_FIELD_NUMBER: _ClassVar[int]
    ports: _containers.RepeatedScalarFieldContainer[str]

    def __init__(self, ports: _Optional[_Iterable[str]]=...) -> None:
        ...

class EndpointMatcher(_message.Message):
    __slots__ = ('metadata_label_matcher',)

    class MetadataLabelMatcher(_message.Message):
        __slots__ = ('metadata_label_match_criteria', 'metadata_labels')

        class MetadataLabelMatchCriteria(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
            __slots__ = ()
            METADATA_LABEL_MATCH_CRITERIA_UNSPECIFIED: _ClassVar[EndpointMatcher.MetadataLabelMatcher.MetadataLabelMatchCriteria]
            MATCH_ANY: _ClassVar[EndpointMatcher.MetadataLabelMatcher.MetadataLabelMatchCriteria]
            MATCH_ALL: _ClassVar[EndpointMatcher.MetadataLabelMatcher.MetadataLabelMatchCriteria]
        METADATA_LABEL_MATCH_CRITERIA_UNSPECIFIED: EndpointMatcher.MetadataLabelMatcher.MetadataLabelMatchCriteria
        MATCH_ANY: EndpointMatcher.MetadataLabelMatcher.MetadataLabelMatchCriteria
        MATCH_ALL: EndpointMatcher.MetadataLabelMatcher.MetadataLabelMatchCriteria

        class MetadataLabels(_message.Message):
            __slots__ = ('label_name', 'label_value')
            LABEL_NAME_FIELD_NUMBER: _ClassVar[int]
            LABEL_VALUE_FIELD_NUMBER: _ClassVar[int]
            label_name: str
            label_value: str

            def __init__(self, label_name: _Optional[str]=..., label_value: _Optional[str]=...) -> None:
                ...
        METADATA_LABEL_MATCH_CRITERIA_FIELD_NUMBER: _ClassVar[int]
        METADATA_LABELS_FIELD_NUMBER: _ClassVar[int]
        metadata_label_match_criteria: EndpointMatcher.MetadataLabelMatcher.MetadataLabelMatchCriteria
        metadata_labels: _containers.RepeatedCompositeFieldContainer[EndpointMatcher.MetadataLabelMatcher.MetadataLabels]

        def __init__(self, metadata_label_match_criteria: _Optional[_Union[EndpointMatcher.MetadataLabelMatcher.MetadataLabelMatchCriteria, str]]=..., metadata_labels: _Optional[_Iterable[_Union[EndpointMatcher.MetadataLabelMatcher.MetadataLabels, _Mapping]]]=...) -> None:
            ...
    METADATA_LABEL_MATCHER_FIELD_NUMBER: _ClassVar[int]
    metadata_label_matcher: EndpointMatcher.MetadataLabelMatcher

    def __init__(self, metadata_label_matcher: _Optional[_Union[EndpointMatcher.MetadataLabelMatcher, _Mapping]]=...) -> None:
        ...