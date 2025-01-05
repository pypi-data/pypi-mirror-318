from google.api import annotations_pb2 as _annotations_pb2
from google.api import client_pb2 as _client_pb2
from google.api import field_behavior_pb2 as _field_behavior_pb2
from google.api import field_info_pb2 as _field_info_pb2
from google.api import resource_pb2 as _resource_pb2
from google.cloud.dataplex.v1 import data_discovery_pb2 as _data_discovery_pb2
from google.cloud.dataplex.v1 import data_profile_pb2 as _data_profile_pb2
from google.cloud.dataplex.v1 import data_quality_pb2 as _data_quality_pb2
from google.cloud.dataplex.v1 import processing_pb2 as _processing_pb2
from google.cloud.dataplex.v1 import resources_pb2 as _resources_pb2
from google.cloud.dataplex.v1 import service_pb2 as _service_pb2
from google.longrunning import operations_pb2 as _operations_pb2
from google.protobuf import empty_pb2 as _empty_pb2
from google.protobuf import field_mask_pb2 as _field_mask_pb2
from google.protobuf import timestamp_pb2 as _timestamp_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class DataScanType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    DATA_SCAN_TYPE_UNSPECIFIED: _ClassVar[DataScanType]
    DATA_QUALITY: _ClassVar[DataScanType]
    DATA_PROFILE: _ClassVar[DataScanType]
    DATA_DISCOVERY: _ClassVar[DataScanType]
DATA_SCAN_TYPE_UNSPECIFIED: DataScanType
DATA_QUALITY: DataScanType
DATA_PROFILE: DataScanType
DATA_DISCOVERY: DataScanType

class CreateDataScanRequest(_message.Message):
    __slots__ = ("parent", "data_scan", "data_scan_id", "validate_only")
    PARENT_FIELD_NUMBER: _ClassVar[int]
    DATA_SCAN_FIELD_NUMBER: _ClassVar[int]
    DATA_SCAN_ID_FIELD_NUMBER: _ClassVar[int]
    VALIDATE_ONLY_FIELD_NUMBER: _ClassVar[int]
    parent: str
    data_scan: DataScan
    data_scan_id: str
    validate_only: bool
    def __init__(self, parent: _Optional[str] = ..., data_scan: _Optional[_Union[DataScan, _Mapping]] = ..., data_scan_id: _Optional[str] = ..., validate_only: bool = ...) -> None: ...

class UpdateDataScanRequest(_message.Message):
    __slots__ = ("data_scan", "update_mask", "validate_only")
    DATA_SCAN_FIELD_NUMBER: _ClassVar[int]
    UPDATE_MASK_FIELD_NUMBER: _ClassVar[int]
    VALIDATE_ONLY_FIELD_NUMBER: _ClassVar[int]
    data_scan: DataScan
    update_mask: _field_mask_pb2.FieldMask
    validate_only: bool
    def __init__(self, data_scan: _Optional[_Union[DataScan, _Mapping]] = ..., update_mask: _Optional[_Union[_field_mask_pb2.FieldMask, _Mapping]] = ..., validate_only: bool = ...) -> None: ...

class DeleteDataScanRequest(_message.Message):
    __slots__ = ("name", "force")
    NAME_FIELD_NUMBER: _ClassVar[int]
    FORCE_FIELD_NUMBER: _ClassVar[int]
    name: str
    force: bool
    def __init__(self, name: _Optional[str] = ..., force: bool = ...) -> None: ...

class GetDataScanRequest(_message.Message):
    __slots__ = ("name", "view")
    class DataScanView(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        DATA_SCAN_VIEW_UNSPECIFIED: _ClassVar[GetDataScanRequest.DataScanView]
        BASIC: _ClassVar[GetDataScanRequest.DataScanView]
        FULL: _ClassVar[GetDataScanRequest.DataScanView]
    DATA_SCAN_VIEW_UNSPECIFIED: GetDataScanRequest.DataScanView
    BASIC: GetDataScanRequest.DataScanView
    FULL: GetDataScanRequest.DataScanView
    NAME_FIELD_NUMBER: _ClassVar[int]
    VIEW_FIELD_NUMBER: _ClassVar[int]
    name: str
    view: GetDataScanRequest.DataScanView
    def __init__(self, name: _Optional[str] = ..., view: _Optional[_Union[GetDataScanRequest.DataScanView, str]] = ...) -> None: ...

class ListDataScansRequest(_message.Message):
    __slots__ = ("parent", "page_size", "page_token", "filter", "order_by")
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
    def __init__(self, parent: _Optional[str] = ..., page_size: _Optional[int] = ..., page_token: _Optional[str] = ..., filter: _Optional[str] = ..., order_by: _Optional[str] = ...) -> None: ...

class ListDataScansResponse(_message.Message):
    __slots__ = ("data_scans", "next_page_token", "unreachable")
    DATA_SCANS_FIELD_NUMBER: _ClassVar[int]
    NEXT_PAGE_TOKEN_FIELD_NUMBER: _ClassVar[int]
    UNREACHABLE_FIELD_NUMBER: _ClassVar[int]
    data_scans: _containers.RepeatedCompositeFieldContainer[DataScan]
    next_page_token: str
    unreachable: _containers.RepeatedScalarFieldContainer[str]
    def __init__(self, data_scans: _Optional[_Iterable[_Union[DataScan, _Mapping]]] = ..., next_page_token: _Optional[str] = ..., unreachable: _Optional[_Iterable[str]] = ...) -> None: ...

class RunDataScanRequest(_message.Message):
    __slots__ = ("name",)
    NAME_FIELD_NUMBER: _ClassVar[int]
    name: str
    def __init__(self, name: _Optional[str] = ...) -> None: ...

class RunDataScanResponse(_message.Message):
    __slots__ = ("job",)
    JOB_FIELD_NUMBER: _ClassVar[int]
    job: DataScanJob
    def __init__(self, job: _Optional[_Union[DataScanJob, _Mapping]] = ...) -> None: ...

class GetDataScanJobRequest(_message.Message):
    __slots__ = ("name", "view")
    class DataScanJobView(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        DATA_SCAN_JOB_VIEW_UNSPECIFIED: _ClassVar[GetDataScanJobRequest.DataScanJobView]
        BASIC: _ClassVar[GetDataScanJobRequest.DataScanJobView]
        FULL: _ClassVar[GetDataScanJobRequest.DataScanJobView]
    DATA_SCAN_JOB_VIEW_UNSPECIFIED: GetDataScanJobRequest.DataScanJobView
    BASIC: GetDataScanJobRequest.DataScanJobView
    FULL: GetDataScanJobRequest.DataScanJobView
    NAME_FIELD_NUMBER: _ClassVar[int]
    VIEW_FIELD_NUMBER: _ClassVar[int]
    name: str
    view: GetDataScanJobRequest.DataScanJobView
    def __init__(self, name: _Optional[str] = ..., view: _Optional[_Union[GetDataScanJobRequest.DataScanJobView, str]] = ...) -> None: ...

class ListDataScanJobsRequest(_message.Message):
    __slots__ = ("parent", "page_size", "page_token", "filter")
    PARENT_FIELD_NUMBER: _ClassVar[int]
    PAGE_SIZE_FIELD_NUMBER: _ClassVar[int]
    PAGE_TOKEN_FIELD_NUMBER: _ClassVar[int]
    FILTER_FIELD_NUMBER: _ClassVar[int]
    parent: str
    page_size: int
    page_token: str
    filter: str
    def __init__(self, parent: _Optional[str] = ..., page_size: _Optional[int] = ..., page_token: _Optional[str] = ..., filter: _Optional[str] = ...) -> None: ...

class ListDataScanJobsResponse(_message.Message):
    __slots__ = ("data_scan_jobs", "next_page_token")
    DATA_SCAN_JOBS_FIELD_NUMBER: _ClassVar[int]
    NEXT_PAGE_TOKEN_FIELD_NUMBER: _ClassVar[int]
    data_scan_jobs: _containers.RepeatedCompositeFieldContainer[DataScanJob]
    next_page_token: str
    def __init__(self, data_scan_jobs: _Optional[_Iterable[_Union[DataScanJob, _Mapping]]] = ..., next_page_token: _Optional[str] = ...) -> None: ...

class GenerateDataQualityRulesRequest(_message.Message):
    __slots__ = ("name",)
    NAME_FIELD_NUMBER: _ClassVar[int]
    name: str
    def __init__(self, name: _Optional[str] = ...) -> None: ...

class GenerateDataQualityRulesResponse(_message.Message):
    __slots__ = ("rule",)
    RULE_FIELD_NUMBER: _ClassVar[int]
    rule: _containers.RepeatedCompositeFieldContainer[_data_quality_pb2.DataQualityRule]
    def __init__(self, rule: _Optional[_Iterable[_Union[_data_quality_pb2.DataQualityRule, _Mapping]]] = ...) -> None: ...

class DataScan(_message.Message):
    __slots__ = ("name", "uid", "description", "display_name", "labels", "state", "create_time", "update_time", "data", "execution_spec", "execution_status", "type", "data_quality_spec", "data_profile_spec", "data_discovery_spec", "data_quality_result", "data_profile_result", "data_discovery_result")
    class ExecutionSpec(_message.Message):
        __slots__ = ("trigger", "field")
        TRIGGER_FIELD_NUMBER: _ClassVar[int]
        FIELD_FIELD_NUMBER: _ClassVar[int]
        trigger: _processing_pb2.Trigger
        field: str
        def __init__(self, trigger: _Optional[_Union[_processing_pb2.Trigger, _Mapping]] = ..., field: _Optional[str] = ...) -> None: ...
    class ExecutionStatus(_message.Message):
        __slots__ = ("latest_job_start_time", "latest_job_end_time", "latest_job_create_time")
        LATEST_JOB_START_TIME_FIELD_NUMBER: _ClassVar[int]
        LATEST_JOB_END_TIME_FIELD_NUMBER: _ClassVar[int]
        LATEST_JOB_CREATE_TIME_FIELD_NUMBER: _ClassVar[int]
        latest_job_start_time: _timestamp_pb2.Timestamp
        latest_job_end_time: _timestamp_pb2.Timestamp
        latest_job_create_time: _timestamp_pb2.Timestamp
        def __init__(self, latest_job_start_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., latest_job_end_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., latest_job_create_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ...) -> None: ...
    class LabelsEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: str
        def __init__(self, key: _Optional[str] = ..., value: _Optional[str] = ...) -> None: ...
    NAME_FIELD_NUMBER: _ClassVar[int]
    UID_FIELD_NUMBER: _ClassVar[int]
    DESCRIPTION_FIELD_NUMBER: _ClassVar[int]
    DISPLAY_NAME_FIELD_NUMBER: _ClassVar[int]
    LABELS_FIELD_NUMBER: _ClassVar[int]
    STATE_FIELD_NUMBER: _ClassVar[int]
    CREATE_TIME_FIELD_NUMBER: _ClassVar[int]
    UPDATE_TIME_FIELD_NUMBER: _ClassVar[int]
    DATA_FIELD_NUMBER: _ClassVar[int]
    EXECUTION_SPEC_FIELD_NUMBER: _ClassVar[int]
    EXECUTION_STATUS_FIELD_NUMBER: _ClassVar[int]
    TYPE_FIELD_NUMBER: _ClassVar[int]
    DATA_QUALITY_SPEC_FIELD_NUMBER: _ClassVar[int]
    DATA_PROFILE_SPEC_FIELD_NUMBER: _ClassVar[int]
    DATA_DISCOVERY_SPEC_FIELD_NUMBER: _ClassVar[int]
    DATA_QUALITY_RESULT_FIELD_NUMBER: _ClassVar[int]
    DATA_PROFILE_RESULT_FIELD_NUMBER: _ClassVar[int]
    DATA_DISCOVERY_RESULT_FIELD_NUMBER: _ClassVar[int]
    name: str
    uid: str
    description: str
    display_name: str
    labels: _containers.ScalarMap[str, str]
    state: _resources_pb2.State
    create_time: _timestamp_pb2.Timestamp
    update_time: _timestamp_pb2.Timestamp
    data: _processing_pb2.DataSource
    execution_spec: DataScan.ExecutionSpec
    execution_status: DataScan.ExecutionStatus
    type: DataScanType
    data_quality_spec: _data_quality_pb2.DataQualitySpec
    data_profile_spec: _data_profile_pb2.DataProfileSpec
    data_discovery_spec: _data_discovery_pb2.DataDiscoverySpec
    data_quality_result: _data_quality_pb2.DataQualityResult
    data_profile_result: _data_profile_pb2.DataProfileResult
    data_discovery_result: _data_discovery_pb2.DataDiscoveryResult
    def __init__(self, name: _Optional[str] = ..., uid: _Optional[str] = ..., description: _Optional[str] = ..., display_name: _Optional[str] = ..., labels: _Optional[_Mapping[str, str]] = ..., state: _Optional[_Union[_resources_pb2.State, str]] = ..., create_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., update_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., data: _Optional[_Union[_processing_pb2.DataSource, _Mapping]] = ..., execution_spec: _Optional[_Union[DataScan.ExecutionSpec, _Mapping]] = ..., execution_status: _Optional[_Union[DataScan.ExecutionStatus, _Mapping]] = ..., type: _Optional[_Union[DataScanType, str]] = ..., data_quality_spec: _Optional[_Union[_data_quality_pb2.DataQualitySpec, _Mapping]] = ..., data_profile_spec: _Optional[_Union[_data_profile_pb2.DataProfileSpec, _Mapping]] = ..., data_discovery_spec: _Optional[_Union[_data_discovery_pb2.DataDiscoverySpec, _Mapping]] = ..., data_quality_result: _Optional[_Union[_data_quality_pb2.DataQualityResult, _Mapping]] = ..., data_profile_result: _Optional[_Union[_data_profile_pb2.DataProfileResult, _Mapping]] = ..., data_discovery_result: _Optional[_Union[_data_discovery_pb2.DataDiscoveryResult, _Mapping]] = ...) -> None: ...

class DataScanJob(_message.Message):
    __slots__ = ("name", "uid", "create_time", "start_time", "end_time", "state", "message", "type", "data_quality_spec", "data_profile_spec", "data_discovery_spec", "data_quality_result", "data_profile_result", "data_discovery_result")
    class State(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        STATE_UNSPECIFIED: _ClassVar[DataScanJob.State]
        RUNNING: _ClassVar[DataScanJob.State]
        CANCELING: _ClassVar[DataScanJob.State]
        CANCELLED: _ClassVar[DataScanJob.State]
        SUCCEEDED: _ClassVar[DataScanJob.State]
        FAILED: _ClassVar[DataScanJob.State]
        PENDING: _ClassVar[DataScanJob.State]
    STATE_UNSPECIFIED: DataScanJob.State
    RUNNING: DataScanJob.State
    CANCELING: DataScanJob.State
    CANCELLED: DataScanJob.State
    SUCCEEDED: DataScanJob.State
    FAILED: DataScanJob.State
    PENDING: DataScanJob.State
    NAME_FIELD_NUMBER: _ClassVar[int]
    UID_FIELD_NUMBER: _ClassVar[int]
    CREATE_TIME_FIELD_NUMBER: _ClassVar[int]
    START_TIME_FIELD_NUMBER: _ClassVar[int]
    END_TIME_FIELD_NUMBER: _ClassVar[int]
    STATE_FIELD_NUMBER: _ClassVar[int]
    MESSAGE_FIELD_NUMBER: _ClassVar[int]
    TYPE_FIELD_NUMBER: _ClassVar[int]
    DATA_QUALITY_SPEC_FIELD_NUMBER: _ClassVar[int]
    DATA_PROFILE_SPEC_FIELD_NUMBER: _ClassVar[int]
    DATA_DISCOVERY_SPEC_FIELD_NUMBER: _ClassVar[int]
    DATA_QUALITY_RESULT_FIELD_NUMBER: _ClassVar[int]
    DATA_PROFILE_RESULT_FIELD_NUMBER: _ClassVar[int]
    DATA_DISCOVERY_RESULT_FIELD_NUMBER: _ClassVar[int]
    name: str
    uid: str
    create_time: _timestamp_pb2.Timestamp
    start_time: _timestamp_pb2.Timestamp
    end_time: _timestamp_pb2.Timestamp
    state: DataScanJob.State
    message: str
    type: DataScanType
    data_quality_spec: _data_quality_pb2.DataQualitySpec
    data_profile_spec: _data_profile_pb2.DataProfileSpec
    data_discovery_spec: _data_discovery_pb2.DataDiscoverySpec
    data_quality_result: _data_quality_pb2.DataQualityResult
    data_profile_result: _data_profile_pb2.DataProfileResult
    data_discovery_result: _data_discovery_pb2.DataDiscoveryResult
    def __init__(self, name: _Optional[str] = ..., uid: _Optional[str] = ..., create_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., start_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., end_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., state: _Optional[_Union[DataScanJob.State, str]] = ..., message: _Optional[str] = ..., type: _Optional[_Union[DataScanType, str]] = ..., data_quality_spec: _Optional[_Union[_data_quality_pb2.DataQualitySpec, _Mapping]] = ..., data_profile_spec: _Optional[_Union[_data_profile_pb2.DataProfileSpec, _Mapping]] = ..., data_discovery_spec: _Optional[_Union[_data_discovery_pb2.DataDiscoverySpec, _Mapping]] = ..., data_quality_result: _Optional[_Union[_data_quality_pb2.DataQualityResult, _Mapping]] = ..., data_profile_result: _Optional[_Union[_data_profile_pb2.DataProfileResult, _Mapping]] = ..., data_discovery_result: _Optional[_Union[_data_discovery_pb2.DataDiscoveryResult, _Mapping]] = ...) -> None: ...
