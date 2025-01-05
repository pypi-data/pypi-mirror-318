from google.api import annotations_pb2 as _annotations_pb2
from google.api import client_pb2 as _client_pb2
from google.api import field_behavior_pb2 as _field_behavior_pb2
from google.protobuf import any_pb2 as _any_pb2
from google.protobuf import empty_pb2 as _empty_pb2
from google.protobuf import timestamp_pb2 as _timestamp_pb2
from google.rpc import status_pb2 as _status_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union
DESCRIPTOR: _descriptor.FileDescriptor

class AlertFeedbackType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    ALERT_FEEDBACK_TYPE_UNSPECIFIED: _ClassVar[AlertFeedbackType]
    NOT_USEFUL: _ClassVar[AlertFeedbackType]
    SOMEWHAT_USEFUL: _ClassVar[AlertFeedbackType]
    VERY_USEFUL: _ClassVar[AlertFeedbackType]
ALERT_FEEDBACK_TYPE_UNSPECIFIED: AlertFeedbackType
NOT_USEFUL: AlertFeedbackType
SOMEWHAT_USEFUL: AlertFeedbackType
VERY_USEFUL: AlertFeedbackType

class Alert(_message.Message):
    __slots__ = ('customer_id', 'alert_id', 'create_time', 'start_time', 'end_time', 'type', 'source', 'data', 'security_investigation_tool_link', 'deleted', 'metadata', 'update_time', 'etag')
    CUSTOMER_ID_FIELD_NUMBER: _ClassVar[int]
    ALERT_ID_FIELD_NUMBER: _ClassVar[int]
    CREATE_TIME_FIELD_NUMBER: _ClassVar[int]
    START_TIME_FIELD_NUMBER: _ClassVar[int]
    END_TIME_FIELD_NUMBER: _ClassVar[int]
    TYPE_FIELD_NUMBER: _ClassVar[int]
    SOURCE_FIELD_NUMBER: _ClassVar[int]
    DATA_FIELD_NUMBER: _ClassVar[int]
    SECURITY_INVESTIGATION_TOOL_LINK_FIELD_NUMBER: _ClassVar[int]
    DELETED_FIELD_NUMBER: _ClassVar[int]
    METADATA_FIELD_NUMBER: _ClassVar[int]
    UPDATE_TIME_FIELD_NUMBER: _ClassVar[int]
    ETAG_FIELD_NUMBER: _ClassVar[int]
    customer_id: str
    alert_id: str
    create_time: _timestamp_pb2.Timestamp
    start_time: _timestamp_pb2.Timestamp
    end_time: _timestamp_pb2.Timestamp
    type: str
    source: str
    data: _any_pb2.Any
    security_investigation_tool_link: str
    deleted: bool
    metadata: AlertMetadata
    update_time: _timestamp_pb2.Timestamp
    etag: str

    def __init__(self, customer_id: _Optional[str]=..., alert_id: _Optional[str]=..., create_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]]=..., start_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]]=..., end_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]]=..., type: _Optional[str]=..., source: _Optional[str]=..., data: _Optional[_Union[_any_pb2.Any, _Mapping]]=..., security_investigation_tool_link: _Optional[str]=..., deleted: bool=..., metadata: _Optional[_Union[AlertMetadata, _Mapping]]=..., update_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]]=..., etag: _Optional[str]=...) -> None:
        ...

class AlertFeedback(_message.Message):
    __slots__ = ('customer_id', 'alert_id', 'feedback_id', 'create_time', 'type', 'email')
    CUSTOMER_ID_FIELD_NUMBER: _ClassVar[int]
    ALERT_ID_FIELD_NUMBER: _ClassVar[int]
    FEEDBACK_ID_FIELD_NUMBER: _ClassVar[int]
    CREATE_TIME_FIELD_NUMBER: _ClassVar[int]
    TYPE_FIELD_NUMBER: _ClassVar[int]
    EMAIL_FIELD_NUMBER: _ClassVar[int]
    customer_id: str
    alert_id: str
    feedback_id: str
    create_time: _timestamp_pb2.Timestamp
    type: AlertFeedbackType
    email: str

    def __init__(self, customer_id: _Optional[str]=..., alert_id: _Optional[str]=..., feedback_id: _Optional[str]=..., create_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]]=..., type: _Optional[_Union[AlertFeedbackType, str]]=..., email: _Optional[str]=...) -> None:
        ...

class AlertMetadata(_message.Message):
    __slots__ = ('customer_id', 'alert_id', 'status', 'assignee', 'update_time', 'severity', 'etag')
    CUSTOMER_ID_FIELD_NUMBER: _ClassVar[int]
    ALERT_ID_FIELD_NUMBER: _ClassVar[int]
    STATUS_FIELD_NUMBER: _ClassVar[int]
    ASSIGNEE_FIELD_NUMBER: _ClassVar[int]
    UPDATE_TIME_FIELD_NUMBER: _ClassVar[int]
    SEVERITY_FIELD_NUMBER: _ClassVar[int]
    ETAG_FIELD_NUMBER: _ClassVar[int]
    customer_id: str
    alert_id: str
    status: str
    assignee: str
    update_time: _timestamp_pb2.Timestamp
    severity: str
    etag: str

    def __init__(self, customer_id: _Optional[str]=..., alert_id: _Optional[str]=..., status: _Optional[str]=..., assignee: _Optional[str]=..., update_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]]=..., severity: _Optional[str]=..., etag: _Optional[str]=...) -> None:
        ...

class Settings(_message.Message):
    __slots__ = ('notifications',)

    class Notification(_message.Message):
        __slots__ = ('cloud_pubsub_topic',)

        class PayloadFormat(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
            __slots__ = ()
            PAYLOAD_FORMAT_UNSPECIFIED: _ClassVar[Settings.Notification.PayloadFormat]
            JSON: _ClassVar[Settings.Notification.PayloadFormat]
        PAYLOAD_FORMAT_UNSPECIFIED: Settings.Notification.PayloadFormat
        JSON: Settings.Notification.PayloadFormat

        class CloudPubsubTopic(_message.Message):
            __slots__ = ('topic_name', 'payload_format')
            TOPIC_NAME_FIELD_NUMBER: _ClassVar[int]
            PAYLOAD_FORMAT_FIELD_NUMBER: _ClassVar[int]
            topic_name: str
            payload_format: Settings.Notification.PayloadFormat

            def __init__(self, topic_name: _Optional[str]=..., payload_format: _Optional[_Union[Settings.Notification.PayloadFormat, str]]=...) -> None:
                ...
        CLOUD_PUBSUB_TOPIC_FIELD_NUMBER: _ClassVar[int]
        cloud_pubsub_topic: Settings.Notification.CloudPubsubTopic

        def __init__(self, cloud_pubsub_topic: _Optional[_Union[Settings.Notification.CloudPubsubTopic, _Mapping]]=...) -> None:
            ...
    NOTIFICATIONS_FIELD_NUMBER: _ClassVar[int]
    notifications: _containers.RepeatedCompositeFieldContainer[Settings.Notification]

    def __init__(self, notifications: _Optional[_Iterable[_Union[Settings.Notification, _Mapping]]]=...) -> None:
        ...

class BatchDeleteAlertsRequest(_message.Message):
    __slots__ = ('customer_id', 'alert_id')
    CUSTOMER_ID_FIELD_NUMBER: _ClassVar[int]
    ALERT_ID_FIELD_NUMBER: _ClassVar[int]
    customer_id: str
    alert_id: _containers.RepeatedScalarFieldContainer[str]

    def __init__(self, customer_id: _Optional[str]=..., alert_id: _Optional[_Iterable[str]]=...) -> None:
        ...

class BatchDeleteAlertsResponse(_message.Message):
    __slots__ = ('success_alert_ids', 'failed_alert_status')

    class FailedAlertStatusEntry(_message.Message):
        __slots__ = ('key', 'value')
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: _status_pb2.Status

        def __init__(self, key: _Optional[str]=..., value: _Optional[_Union[_status_pb2.Status, _Mapping]]=...) -> None:
            ...
    SUCCESS_ALERT_IDS_FIELD_NUMBER: _ClassVar[int]
    FAILED_ALERT_STATUS_FIELD_NUMBER: _ClassVar[int]
    success_alert_ids: _containers.RepeatedScalarFieldContainer[str]
    failed_alert_status: _containers.MessageMap[str, _status_pb2.Status]

    def __init__(self, success_alert_ids: _Optional[_Iterable[str]]=..., failed_alert_status: _Optional[_Mapping[str, _status_pb2.Status]]=...) -> None:
        ...

class BatchUndeleteAlertsRequest(_message.Message):
    __slots__ = ('customer_id', 'alert_id')
    CUSTOMER_ID_FIELD_NUMBER: _ClassVar[int]
    ALERT_ID_FIELD_NUMBER: _ClassVar[int]
    customer_id: str
    alert_id: _containers.RepeatedScalarFieldContainer[str]

    def __init__(self, customer_id: _Optional[str]=..., alert_id: _Optional[_Iterable[str]]=...) -> None:
        ...

class BatchUndeleteAlertsResponse(_message.Message):
    __slots__ = ('success_alert_ids', 'failed_alert_status')

    class FailedAlertStatusEntry(_message.Message):
        __slots__ = ('key', 'value')
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: _status_pb2.Status

        def __init__(self, key: _Optional[str]=..., value: _Optional[_Union[_status_pb2.Status, _Mapping]]=...) -> None:
            ...
    SUCCESS_ALERT_IDS_FIELD_NUMBER: _ClassVar[int]
    FAILED_ALERT_STATUS_FIELD_NUMBER: _ClassVar[int]
    success_alert_ids: _containers.RepeatedScalarFieldContainer[str]
    failed_alert_status: _containers.MessageMap[str, _status_pb2.Status]

    def __init__(self, success_alert_ids: _Optional[_Iterable[str]]=..., failed_alert_status: _Optional[_Mapping[str, _status_pb2.Status]]=...) -> None:
        ...

class ListAlertsRequest(_message.Message):
    __slots__ = ('customer_id', 'page_size', 'page_token', 'filter', 'order_by')
    CUSTOMER_ID_FIELD_NUMBER: _ClassVar[int]
    PAGE_SIZE_FIELD_NUMBER: _ClassVar[int]
    PAGE_TOKEN_FIELD_NUMBER: _ClassVar[int]
    FILTER_FIELD_NUMBER: _ClassVar[int]
    ORDER_BY_FIELD_NUMBER: _ClassVar[int]
    customer_id: str
    page_size: int
    page_token: str
    filter: str
    order_by: str

    def __init__(self, customer_id: _Optional[str]=..., page_size: _Optional[int]=..., page_token: _Optional[str]=..., filter: _Optional[str]=..., order_by: _Optional[str]=...) -> None:
        ...

class ListAlertsResponse(_message.Message):
    __slots__ = ('alerts', 'next_page_token')
    ALERTS_FIELD_NUMBER: _ClassVar[int]
    NEXT_PAGE_TOKEN_FIELD_NUMBER: _ClassVar[int]
    alerts: _containers.RepeatedCompositeFieldContainer[Alert]
    next_page_token: str

    def __init__(self, alerts: _Optional[_Iterable[_Union[Alert, _Mapping]]]=..., next_page_token: _Optional[str]=...) -> None:
        ...

class GetAlertRequest(_message.Message):
    __slots__ = ('customer_id', 'alert_id')
    CUSTOMER_ID_FIELD_NUMBER: _ClassVar[int]
    ALERT_ID_FIELD_NUMBER: _ClassVar[int]
    customer_id: str
    alert_id: str

    def __init__(self, customer_id: _Optional[str]=..., alert_id: _Optional[str]=...) -> None:
        ...

class DeleteAlertRequest(_message.Message):
    __slots__ = ('customer_id', 'alert_id')
    CUSTOMER_ID_FIELD_NUMBER: _ClassVar[int]
    ALERT_ID_FIELD_NUMBER: _ClassVar[int]
    customer_id: str
    alert_id: str

    def __init__(self, customer_id: _Optional[str]=..., alert_id: _Optional[str]=...) -> None:
        ...

class UndeleteAlertRequest(_message.Message):
    __slots__ = ('customer_id', 'alert_id')
    CUSTOMER_ID_FIELD_NUMBER: _ClassVar[int]
    ALERT_ID_FIELD_NUMBER: _ClassVar[int]
    customer_id: str
    alert_id: str

    def __init__(self, customer_id: _Optional[str]=..., alert_id: _Optional[str]=...) -> None:
        ...

class CreateAlertFeedbackRequest(_message.Message):
    __slots__ = ('customer_id', 'alert_id', 'feedback')
    CUSTOMER_ID_FIELD_NUMBER: _ClassVar[int]
    ALERT_ID_FIELD_NUMBER: _ClassVar[int]
    FEEDBACK_FIELD_NUMBER: _ClassVar[int]
    customer_id: str
    alert_id: str
    feedback: AlertFeedback

    def __init__(self, customer_id: _Optional[str]=..., alert_id: _Optional[str]=..., feedback: _Optional[_Union[AlertFeedback, _Mapping]]=...) -> None:
        ...

class ListAlertFeedbackRequest(_message.Message):
    __slots__ = ('customer_id', 'alert_id', 'filter')
    CUSTOMER_ID_FIELD_NUMBER: _ClassVar[int]
    ALERT_ID_FIELD_NUMBER: _ClassVar[int]
    FILTER_FIELD_NUMBER: _ClassVar[int]
    customer_id: str
    alert_id: str
    filter: str

    def __init__(self, customer_id: _Optional[str]=..., alert_id: _Optional[str]=..., filter: _Optional[str]=...) -> None:
        ...

class ListAlertFeedbackResponse(_message.Message):
    __slots__ = ('feedback',)
    FEEDBACK_FIELD_NUMBER: _ClassVar[int]
    feedback: _containers.RepeatedCompositeFieldContainer[AlertFeedback]

    def __init__(self, feedback: _Optional[_Iterable[_Union[AlertFeedback, _Mapping]]]=...) -> None:
        ...

class GetAlertMetadataRequest(_message.Message):
    __slots__ = ('customer_id', 'alert_id')
    CUSTOMER_ID_FIELD_NUMBER: _ClassVar[int]
    ALERT_ID_FIELD_NUMBER: _ClassVar[int]
    customer_id: str
    alert_id: str

    def __init__(self, customer_id: _Optional[str]=..., alert_id: _Optional[str]=...) -> None:
        ...

class GetSettingsRequest(_message.Message):
    __slots__ = ('customer_id',)
    CUSTOMER_ID_FIELD_NUMBER: _ClassVar[int]
    customer_id: str

    def __init__(self, customer_id: _Optional[str]=...) -> None:
        ...

class UpdateSettingsRequest(_message.Message):
    __slots__ = ('customer_id', 'settings')
    CUSTOMER_ID_FIELD_NUMBER: _ClassVar[int]
    SETTINGS_FIELD_NUMBER: _ClassVar[int]
    customer_id: str
    settings: Settings

    def __init__(self, customer_id: _Optional[str]=..., settings: _Optional[_Union[Settings, _Mapping]]=...) -> None:
        ...