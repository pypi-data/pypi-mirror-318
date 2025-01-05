from google.api import annotations_pb2 as _annotations_pb2
from google.api import client_pb2 as _client_pb2
from google.api import field_behavior_pb2 as _field_behavior_pb2
from google.api import resource_pb2 as _resource_pb2
from google.cloud.apphub.v1 import application_pb2 as _application_pb2
from google.cloud.apphub.v1 import service_pb2 as _service_pb2
from google.cloud.apphub.v1 import service_project_attachment_pb2 as _service_project_attachment_pb2
from google.cloud.apphub.v1 import workload_pb2 as _workload_pb2
from google.longrunning import operations_pb2 as _operations_pb2
from google.protobuf import empty_pb2 as _empty_pb2
from google.protobuf import field_mask_pb2 as _field_mask_pb2
from google.protobuf import timestamp_pb2 as _timestamp_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union
DESCRIPTOR: _descriptor.FileDescriptor

class LookupServiceProjectAttachmentRequest(_message.Message):
    __slots__ = ('name',)
    NAME_FIELD_NUMBER: _ClassVar[int]
    name: str

    def __init__(self, name: _Optional[str]=...) -> None:
        ...

class LookupServiceProjectAttachmentResponse(_message.Message):
    __slots__ = ('service_project_attachment',)
    SERVICE_PROJECT_ATTACHMENT_FIELD_NUMBER: _ClassVar[int]
    service_project_attachment: _service_project_attachment_pb2.ServiceProjectAttachment

    def __init__(self, service_project_attachment: _Optional[_Union[_service_project_attachment_pb2.ServiceProjectAttachment, _Mapping]]=...) -> None:
        ...

class ListServiceProjectAttachmentsRequest(_message.Message):
    __slots__ = ('parent', 'page_size', 'page_token', 'filter', 'order_by')
    PARENT_FIELD_NUMBER: _ClassVar[int]
    PAGE_SIZE_FIELD_NUMBER: _ClassVar[int]
    PAGE_TOKEN_FIELD_NUMBER: _ClassVar[int]
    FILTER_FIELD_NUMBER: _ClassVar[int]
    ORDER_BY_FIELD_NUMBER: _ClassVar[int]
    parent: str
    page_size: int
    page_token: str
    filter: str
    order_by: str

    def __init__(self, parent: _Optional[str]=..., page_size: _Optional[int]=..., page_token: _Optional[str]=..., filter: _Optional[str]=..., order_by: _Optional[str]=...) -> None:
        ...

class ListServiceProjectAttachmentsResponse(_message.Message):
    __slots__ = ('service_project_attachments', 'next_page_token', 'unreachable')
    SERVICE_PROJECT_ATTACHMENTS_FIELD_NUMBER: _ClassVar[int]
    NEXT_PAGE_TOKEN_FIELD_NUMBER: _ClassVar[int]
    UNREACHABLE_FIELD_NUMBER: _ClassVar[int]
    service_project_attachments: _containers.RepeatedCompositeFieldContainer[_service_project_attachment_pb2.ServiceProjectAttachment]
    next_page_token: str
    unreachable: _containers.RepeatedScalarFieldContainer[str]

    def __init__(self, service_project_attachments: _Optional[_Iterable[_Union[_service_project_attachment_pb2.ServiceProjectAttachment, _Mapping]]]=..., next_page_token: _Optional[str]=..., unreachable: _Optional[_Iterable[str]]=...) -> None:
        ...

class CreateServiceProjectAttachmentRequest(_message.Message):
    __slots__ = ('parent', 'service_project_attachment_id', 'service_project_attachment', 'request_id')
    PARENT_FIELD_NUMBER: _ClassVar[int]
    SERVICE_PROJECT_ATTACHMENT_ID_FIELD_NUMBER: _ClassVar[int]
    SERVICE_PROJECT_ATTACHMENT_FIELD_NUMBER: _ClassVar[int]
    REQUEST_ID_FIELD_NUMBER: _ClassVar[int]
    parent: str
    service_project_attachment_id: str
    service_project_attachment: _service_project_attachment_pb2.ServiceProjectAttachment
    request_id: str

    def __init__(self, parent: _Optional[str]=..., service_project_attachment_id: _Optional[str]=..., service_project_attachment: _Optional[_Union[_service_project_attachment_pb2.ServiceProjectAttachment, _Mapping]]=..., request_id: _Optional[str]=...) -> None:
        ...

class GetServiceProjectAttachmentRequest(_message.Message):
    __slots__ = ('name',)
    NAME_FIELD_NUMBER: _ClassVar[int]
    name: str

    def __init__(self, name: _Optional[str]=...) -> None:
        ...

class DeleteServiceProjectAttachmentRequest(_message.Message):
    __slots__ = ('name', 'request_id')
    NAME_FIELD_NUMBER: _ClassVar[int]
    REQUEST_ID_FIELD_NUMBER: _ClassVar[int]
    name: str
    request_id: str

    def __init__(self, name: _Optional[str]=..., request_id: _Optional[str]=...) -> None:
        ...

class DetachServiceProjectAttachmentRequest(_message.Message):
    __slots__ = ('name',)
    NAME_FIELD_NUMBER: _ClassVar[int]
    name: str

    def __init__(self, name: _Optional[str]=...) -> None:
        ...

class DetachServiceProjectAttachmentResponse(_message.Message):
    __slots__ = ()

    def __init__(self) -> None:
        ...

class ListServicesRequest(_message.Message):
    __slots__ = ('parent', 'page_size', 'page_token', 'filter', 'order_by')
    PARENT_FIELD_NUMBER: _ClassVar[int]
    PAGE_SIZE_FIELD_NUMBER: _ClassVar[int]
    PAGE_TOKEN_FIELD_NUMBER: _ClassVar[int]
    FILTER_FIELD_NUMBER: _ClassVar[int]
    ORDER_BY_FIELD_NUMBER: _ClassVar[int]
    parent: str
    page_size: int
    page_token: str
    filter: str
    order_by: str

    def __init__(self, parent: _Optional[str]=..., page_size: _Optional[int]=..., page_token: _Optional[str]=..., filter: _Optional[str]=..., order_by: _Optional[str]=...) -> None:
        ...

class ListServicesResponse(_message.Message):
    __slots__ = ('services', 'next_page_token', 'unreachable')
    SERVICES_FIELD_NUMBER: _ClassVar[int]
    NEXT_PAGE_TOKEN_FIELD_NUMBER: _ClassVar[int]
    UNREACHABLE_FIELD_NUMBER: _ClassVar[int]
    services: _containers.RepeatedCompositeFieldContainer[_service_pb2.Service]
    next_page_token: str
    unreachable: _containers.RepeatedScalarFieldContainer[str]

    def __init__(self, services: _Optional[_Iterable[_Union[_service_pb2.Service, _Mapping]]]=..., next_page_token: _Optional[str]=..., unreachable: _Optional[_Iterable[str]]=...) -> None:
        ...

class ListDiscoveredServicesRequest(_message.Message):
    __slots__ = ('parent', 'page_size', 'page_token', 'filter', 'order_by')
    PARENT_FIELD_NUMBER: _ClassVar[int]
    PAGE_SIZE_FIELD_NUMBER: _ClassVar[int]
    PAGE_TOKEN_FIELD_NUMBER: _ClassVar[int]
    FILTER_FIELD_NUMBER: _ClassVar[int]
    ORDER_BY_FIELD_NUMBER: _ClassVar[int]
    parent: str
    page_size: int
    page_token: str
    filter: str
    order_by: str

    def __init__(self, parent: _Optional[str]=..., page_size: _Optional[int]=..., page_token: _Optional[str]=..., filter: _Optional[str]=..., order_by: _Optional[str]=...) -> None:
        ...

class ListDiscoveredServicesResponse(_message.Message):
    __slots__ = ('discovered_services', 'next_page_token', 'unreachable')
    DISCOVERED_SERVICES_FIELD_NUMBER: _ClassVar[int]
    NEXT_PAGE_TOKEN_FIELD_NUMBER: _ClassVar[int]
    UNREACHABLE_FIELD_NUMBER: _ClassVar[int]
    discovered_services: _containers.RepeatedCompositeFieldContainer[_service_pb2.DiscoveredService]
    next_page_token: str
    unreachable: _containers.RepeatedScalarFieldContainer[str]

    def __init__(self, discovered_services: _Optional[_Iterable[_Union[_service_pb2.DiscoveredService, _Mapping]]]=..., next_page_token: _Optional[str]=..., unreachable: _Optional[_Iterable[str]]=...) -> None:
        ...

class CreateServiceRequest(_message.Message):
    __slots__ = ('parent', 'service_id', 'service', 'request_id')
    PARENT_FIELD_NUMBER: _ClassVar[int]
    SERVICE_ID_FIELD_NUMBER: _ClassVar[int]
    SERVICE_FIELD_NUMBER: _ClassVar[int]
    REQUEST_ID_FIELD_NUMBER: _ClassVar[int]
    parent: str
    service_id: str
    service: _service_pb2.Service
    request_id: str

    def __init__(self, parent: _Optional[str]=..., service_id: _Optional[str]=..., service: _Optional[_Union[_service_pb2.Service, _Mapping]]=..., request_id: _Optional[str]=...) -> None:
        ...

class GetServiceRequest(_message.Message):
    __slots__ = ('name',)
    NAME_FIELD_NUMBER: _ClassVar[int]
    name: str

    def __init__(self, name: _Optional[str]=...) -> None:
        ...

class GetDiscoveredServiceRequest(_message.Message):
    __slots__ = ('name',)
    NAME_FIELD_NUMBER: _ClassVar[int]
    name: str

    def __init__(self, name: _Optional[str]=...) -> None:
        ...

class LookupDiscoveredServiceRequest(_message.Message):
    __slots__ = ('parent', 'uri')
    PARENT_FIELD_NUMBER: _ClassVar[int]
    URI_FIELD_NUMBER: _ClassVar[int]
    parent: str
    uri: str

    def __init__(self, parent: _Optional[str]=..., uri: _Optional[str]=...) -> None:
        ...

class LookupDiscoveredServiceResponse(_message.Message):
    __slots__ = ('discovered_service',)
    DISCOVERED_SERVICE_FIELD_NUMBER: _ClassVar[int]
    discovered_service: _service_pb2.DiscoveredService

    def __init__(self, discovered_service: _Optional[_Union[_service_pb2.DiscoveredService, _Mapping]]=...) -> None:
        ...

class UpdateServiceRequest(_message.Message):
    __slots__ = ('update_mask', 'service', 'request_id')
    UPDATE_MASK_FIELD_NUMBER: _ClassVar[int]
    SERVICE_FIELD_NUMBER: _ClassVar[int]
    REQUEST_ID_FIELD_NUMBER: _ClassVar[int]
    update_mask: _field_mask_pb2.FieldMask
    service: _service_pb2.Service
    request_id: str

    def __init__(self, update_mask: _Optional[_Union[_field_mask_pb2.FieldMask, _Mapping]]=..., service: _Optional[_Union[_service_pb2.Service, _Mapping]]=..., request_id: _Optional[str]=...) -> None:
        ...

class DeleteServiceRequest(_message.Message):
    __slots__ = ('name', 'request_id')
    NAME_FIELD_NUMBER: _ClassVar[int]
    REQUEST_ID_FIELD_NUMBER: _ClassVar[int]
    name: str
    request_id: str

    def __init__(self, name: _Optional[str]=..., request_id: _Optional[str]=...) -> None:
        ...

class ListApplicationsRequest(_message.Message):
    __slots__ = ('parent', 'page_size', 'page_token', 'filter', 'order_by')
    PARENT_FIELD_NUMBER: _ClassVar[int]
    PAGE_SIZE_FIELD_NUMBER: _ClassVar[int]
    PAGE_TOKEN_FIELD_NUMBER: _ClassVar[int]
    FILTER_FIELD_NUMBER: _ClassVar[int]
    ORDER_BY_FIELD_NUMBER: _ClassVar[int]
    parent: str
    page_size: int
    page_token: str
    filter: str
    order_by: str

    def __init__(self, parent: _Optional[str]=..., page_size: _Optional[int]=..., page_token: _Optional[str]=..., filter: _Optional[str]=..., order_by: _Optional[str]=...) -> None:
        ...

class ListApplicationsResponse(_message.Message):
    __slots__ = ('applications', 'next_page_token', 'unreachable')
    APPLICATIONS_FIELD_NUMBER: _ClassVar[int]
    NEXT_PAGE_TOKEN_FIELD_NUMBER: _ClassVar[int]
    UNREACHABLE_FIELD_NUMBER: _ClassVar[int]
    applications: _containers.RepeatedCompositeFieldContainer[_application_pb2.Application]
    next_page_token: str
    unreachable: _containers.RepeatedScalarFieldContainer[str]

    def __init__(self, applications: _Optional[_Iterable[_Union[_application_pb2.Application, _Mapping]]]=..., next_page_token: _Optional[str]=..., unreachable: _Optional[_Iterable[str]]=...) -> None:
        ...

class CreateApplicationRequest(_message.Message):
    __slots__ = ('parent', 'application_id', 'application', 'request_id')
    PARENT_FIELD_NUMBER: _ClassVar[int]
    APPLICATION_ID_FIELD_NUMBER: _ClassVar[int]
    APPLICATION_FIELD_NUMBER: _ClassVar[int]
    REQUEST_ID_FIELD_NUMBER: _ClassVar[int]
    parent: str
    application_id: str
    application: _application_pb2.Application
    request_id: str

    def __init__(self, parent: _Optional[str]=..., application_id: _Optional[str]=..., application: _Optional[_Union[_application_pb2.Application, _Mapping]]=..., request_id: _Optional[str]=...) -> None:
        ...

class GetApplicationRequest(_message.Message):
    __slots__ = ('name',)
    NAME_FIELD_NUMBER: _ClassVar[int]
    name: str

    def __init__(self, name: _Optional[str]=...) -> None:
        ...

class UpdateApplicationRequest(_message.Message):
    __slots__ = ('update_mask', 'application', 'request_id')
    UPDATE_MASK_FIELD_NUMBER: _ClassVar[int]
    APPLICATION_FIELD_NUMBER: _ClassVar[int]
    REQUEST_ID_FIELD_NUMBER: _ClassVar[int]
    update_mask: _field_mask_pb2.FieldMask
    application: _application_pb2.Application
    request_id: str

    def __init__(self, update_mask: _Optional[_Union[_field_mask_pb2.FieldMask, _Mapping]]=..., application: _Optional[_Union[_application_pb2.Application, _Mapping]]=..., request_id: _Optional[str]=...) -> None:
        ...

class DeleteApplicationRequest(_message.Message):
    __slots__ = ('name', 'request_id')
    NAME_FIELD_NUMBER: _ClassVar[int]
    REQUEST_ID_FIELD_NUMBER: _ClassVar[int]
    name: str
    request_id: str

    def __init__(self, name: _Optional[str]=..., request_id: _Optional[str]=...) -> None:
        ...

class ListWorkloadsRequest(_message.Message):
    __slots__ = ('parent', 'page_size', 'page_token', 'filter', 'order_by')
    PARENT_FIELD_NUMBER: _ClassVar[int]
    PAGE_SIZE_FIELD_NUMBER: _ClassVar[int]
    PAGE_TOKEN_FIELD_NUMBER: _ClassVar[int]
    FILTER_FIELD_NUMBER: _ClassVar[int]
    ORDER_BY_FIELD_NUMBER: _ClassVar[int]
    parent: str
    page_size: int
    page_token: str
    filter: str
    order_by: str

    def __init__(self, parent: _Optional[str]=..., page_size: _Optional[int]=..., page_token: _Optional[str]=..., filter: _Optional[str]=..., order_by: _Optional[str]=...) -> None:
        ...

class ListWorkloadsResponse(_message.Message):
    __slots__ = ('workloads', 'next_page_token', 'unreachable')
    WORKLOADS_FIELD_NUMBER: _ClassVar[int]
    NEXT_PAGE_TOKEN_FIELD_NUMBER: _ClassVar[int]
    UNREACHABLE_FIELD_NUMBER: _ClassVar[int]
    workloads: _containers.RepeatedCompositeFieldContainer[_workload_pb2.Workload]
    next_page_token: str
    unreachable: _containers.RepeatedScalarFieldContainer[str]

    def __init__(self, workloads: _Optional[_Iterable[_Union[_workload_pb2.Workload, _Mapping]]]=..., next_page_token: _Optional[str]=..., unreachable: _Optional[_Iterable[str]]=...) -> None:
        ...

class ListDiscoveredWorkloadsRequest(_message.Message):
    __slots__ = ('parent', 'page_size', 'page_token', 'filter', 'order_by')
    PARENT_FIELD_NUMBER: _ClassVar[int]
    PAGE_SIZE_FIELD_NUMBER: _ClassVar[int]
    PAGE_TOKEN_FIELD_NUMBER: _ClassVar[int]
    FILTER_FIELD_NUMBER: _ClassVar[int]
    ORDER_BY_FIELD_NUMBER: _ClassVar[int]
    parent: str
    page_size: int
    page_token: str
    filter: str
    order_by: str

    def __init__(self, parent: _Optional[str]=..., page_size: _Optional[int]=..., page_token: _Optional[str]=..., filter: _Optional[str]=..., order_by: _Optional[str]=...) -> None:
        ...

class ListDiscoveredWorkloadsResponse(_message.Message):
    __slots__ = ('discovered_workloads', 'next_page_token', 'unreachable')
    DISCOVERED_WORKLOADS_FIELD_NUMBER: _ClassVar[int]
    NEXT_PAGE_TOKEN_FIELD_NUMBER: _ClassVar[int]
    UNREACHABLE_FIELD_NUMBER: _ClassVar[int]
    discovered_workloads: _containers.RepeatedCompositeFieldContainer[_workload_pb2.DiscoveredWorkload]
    next_page_token: str
    unreachable: _containers.RepeatedScalarFieldContainer[str]

    def __init__(self, discovered_workloads: _Optional[_Iterable[_Union[_workload_pb2.DiscoveredWorkload, _Mapping]]]=..., next_page_token: _Optional[str]=..., unreachable: _Optional[_Iterable[str]]=...) -> None:
        ...

class CreateWorkloadRequest(_message.Message):
    __slots__ = ('parent', 'workload_id', 'workload', 'request_id')
    PARENT_FIELD_NUMBER: _ClassVar[int]
    WORKLOAD_ID_FIELD_NUMBER: _ClassVar[int]
    WORKLOAD_FIELD_NUMBER: _ClassVar[int]
    REQUEST_ID_FIELD_NUMBER: _ClassVar[int]
    parent: str
    workload_id: str
    workload: _workload_pb2.Workload
    request_id: str

    def __init__(self, parent: _Optional[str]=..., workload_id: _Optional[str]=..., workload: _Optional[_Union[_workload_pb2.Workload, _Mapping]]=..., request_id: _Optional[str]=...) -> None:
        ...

class GetWorkloadRequest(_message.Message):
    __slots__ = ('name',)
    NAME_FIELD_NUMBER: _ClassVar[int]
    name: str

    def __init__(self, name: _Optional[str]=...) -> None:
        ...

class GetDiscoveredWorkloadRequest(_message.Message):
    __slots__ = ('name',)
    NAME_FIELD_NUMBER: _ClassVar[int]
    name: str

    def __init__(self, name: _Optional[str]=...) -> None:
        ...

class LookupDiscoveredWorkloadRequest(_message.Message):
    __slots__ = ('parent', 'uri')
    PARENT_FIELD_NUMBER: _ClassVar[int]
    URI_FIELD_NUMBER: _ClassVar[int]
    parent: str
    uri: str

    def __init__(self, parent: _Optional[str]=..., uri: _Optional[str]=...) -> None:
        ...

class LookupDiscoveredWorkloadResponse(_message.Message):
    __slots__ = ('discovered_workload',)
    DISCOVERED_WORKLOAD_FIELD_NUMBER: _ClassVar[int]
    discovered_workload: _workload_pb2.DiscoveredWorkload

    def __init__(self, discovered_workload: _Optional[_Union[_workload_pb2.DiscoveredWorkload, _Mapping]]=...) -> None:
        ...

class UpdateWorkloadRequest(_message.Message):
    __slots__ = ('update_mask', 'workload', 'request_id')
    UPDATE_MASK_FIELD_NUMBER: _ClassVar[int]
    WORKLOAD_FIELD_NUMBER: _ClassVar[int]
    REQUEST_ID_FIELD_NUMBER: _ClassVar[int]
    update_mask: _field_mask_pb2.FieldMask
    workload: _workload_pb2.Workload
    request_id: str

    def __init__(self, update_mask: _Optional[_Union[_field_mask_pb2.FieldMask, _Mapping]]=..., workload: _Optional[_Union[_workload_pb2.Workload, _Mapping]]=..., request_id: _Optional[str]=...) -> None:
        ...

class DeleteWorkloadRequest(_message.Message):
    __slots__ = ('name', 'request_id')
    NAME_FIELD_NUMBER: _ClassVar[int]
    REQUEST_ID_FIELD_NUMBER: _ClassVar[int]
    name: str
    request_id: str

    def __init__(self, name: _Optional[str]=..., request_id: _Optional[str]=...) -> None:
        ...

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