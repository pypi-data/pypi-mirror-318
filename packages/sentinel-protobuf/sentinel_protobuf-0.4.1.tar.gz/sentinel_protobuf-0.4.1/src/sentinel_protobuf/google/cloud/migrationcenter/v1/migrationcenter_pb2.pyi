from google.api import annotations_pb2 as _annotations_pb2
from google.api import client_pb2 as _client_pb2
from google.api import field_behavior_pb2 as _field_behavior_pb2
from google.api import resource_pb2 as _resource_pb2
from google.longrunning import operations_pb2 as _operations_pb2
from google.protobuf import empty_pb2 as _empty_pb2
from google.protobuf import field_mask_pb2 as _field_mask_pb2
from google.protobuf import timestamp_pb2 as _timestamp_pb2
from google.type import date_pb2 as _date_pb2
from google.type import money_pb2 as _money_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union
DESCRIPTOR: _descriptor.FileDescriptor

class AssetView(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    ASSET_VIEW_UNSPECIFIED: _ClassVar[AssetView]
    ASSET_VIEW_BASIC: _ClassVar[AssetView]
    ASSET_VIEW_FULL: _ClassVar[AssetView]

class OperatingSystemFamily(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    OS_FAMILY_UNKNOWN: _ClassVar[OperatingSystemFamily]
    OS_FAMILY_WINDOWS: _ClassVar[OperatingSystemFamily]
    OS_FAMILY_LINUX: _ClassVar[OperatingSystemFamily]
    OS_FAMILY_UNIX: _ClassVar[OperatingSystemFamily]

class ImportJobFormat(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    IMPORT_JOB_FORMAT_UNSPECIFIED: _ClassVar[ImportJobFormat]
    IMPORT_JOB_FORMAT_RVTOOLS_XLSX: _ClassVar[ImportJobFormat]
    IMPORT_JOB_FORMAT_RVTOOLS_CSV: _ClassVar[ImportJobFormat]
    IMPORT_JOB_FORMAT_EXPORTED_AWS_CSV: _ClassVar[ImportJobFormat]
    IMPORT_JOB_FORMAT_EXPORTED_AZURE_CSV: _ClassVar[ImportJobFormat]
    IMPORT_JOB_FORMAT_STRATOZONE_CSV: _ClassVar[ImportJobFormat]

class ImportJobView(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    IMPORT_JOB_VIEW_UNSPECIFIED: _ClassVar[ImportJobView]
    IMPORT_JOB_VIEW_BASIC: _ClassVar[ImportJobView]
    IMPORT_JOB_VIEW_FULL: _ClassVar[ImportJobView]

class ErrorFrameView(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    ERROR_FRAME_VIEW_UNSPECIFIED: _ClassVar[ErrorFrameView]
    ERROR_FRAME_VIEW_BASIC: _ClassVar[ErrorFrameView]
    ERROR_FRAME_VIEW_FULL: _ClassVar[ErrorFrameView]

class PersistentDiskType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    PERSISTENT_DISK_TYPE_UNSPECIFIED: _ClassVar[PersistentDiskType]
    PERSISTENT_DISK_TYPE_STANDARD: _ClassVar[PersistentDiskType]
    PERSISTENT_DISK_TYPE_BALANCED: _ClassVar[PersistentDiskType]
    PERSISTENT_DISK_TYPE_SSD: _ClassVar[PersistentDiskType]

class LicenseType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    LICENSE_TYPE_UNSPECIFIED: _ClassVar[LicenseType]
    LICENSE_TYPE_DEFAULT: _ClassVar[LicenseType]
    LICENSE_TYPE_BRING_YOUR_OWN_LICENSE: _ClassVar[LicenseType]

class SizingOptimizationStrategy(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    SIZING_OPTIMIZATION_STRATEGY_UNSPECIFIED: _ClassVar[SizingOptimizationStrategy]
    SIZING_OPTIMIZATION_STRATEGY_SAME_AS_SOURCE: _ClassVar[SizingOptimizationStrategy]
    SIZING_OPTIMIZATION_STRATEGY_MODERATE: _ClassVar[SizingOptimizationStrategy]
    SIZING_OPTIMIZATION_STRATEGY_AGGRESSIVE: _ClassVar[SizingOptimizationStrategy]

class CommitmentPlan(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    COMMITMENT_PLAN_UNSPECIFIED: _ClassVar[CommitmentPlan]
    COMMITMENT_PLAN_NONE: _ClassVar[CommitmentPlan]
    COMMITMENT_PLAN_ONE_YEAR: _ClassVar[CommitmentPlan]
    COMMITMENT_PLAN_THREE_YEARS: _ClassVar[CommitmentPlan]

class ComputeMigrationTargetProduct(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    COMPUTE_MIGRATION_TARGET_PRODUCT_UNSPECIFIED: _ClassVar[ComputeMigrationTargetProduct]
    COMPUTE_MIGRATION_TARGET_PRODUCT_COMPUTE_ENGINE: _ClassVar[ComputeMigrationTargetProduct]
    COMPUTE_MIGRATION_TARGET_PRODUCT_VMWARE_ENGINE: _ClassVar[ComputeMigrationTargetProduct]
    COMPUTE_MIGRATION_TARGET_PRODUCT_SOLE_TENANCY: _ClassVar[ComputeMigrationTargetProduct]

class ReportView(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    REPORT_VIEW_UNSPECIFIED: _ClassVar[ReportView]
    REPORT_VIEW_BASIC: _ClassVar[ReportView]
    REPORT_VIEW_FULL: _ClassVar[ReportView]
    REPORT_VIEW_STANDARD: _ClassVar[ReportView]
ASSET_VIEW_UNSPECIFIED: AssetView
ASSET_VIEW_BASIC: AssetView
ASSET_VIEW_FULL: AssetView
OS_FAMILY_UNKNOWN: OperatingSystemFamily
OS_FAMILY_WINDOWS: OperatingSystemFamily
OS_FAMILY_LINUX: OperatingSystemFamily
OS_FAMILY_UNIX: OperatingSystemFamily
IMPORT_JOB_FORMAT_UNSPECIFIED: ImportJobFormat
IMPORT_JOB_FORMAT_RVTOOLS_XLSX: ImportJobFormat
IMPORT_JOB_FORMAT_RVTOOLS_CSV: ImportJobFormat
IMPORT_JOB_FORMAT_EXPORTED_AWS_CSV: ImportJobFormat
IMPORT_JOB_FORMAT_EXPORTED_AZURE_CSV: ImportJobFormat
IMPORT_JOB_FORMAT_STRATOZONE_CSV: ImportJobFormat
IMPORT_JOB_VIEW_UNSPECIFIED: ImportJobView
IMPORT_JOB_VIEW_BASIC: ImportJobView
IMPORT_JOB_VIEW_FULL: ImportJobView
ERROR_FRAME_VIEW_UNSPECIFIED: ErrorFrameView
ERROR_FRAME_VIEW_BASIC: ErrorFrameView
ERROR_FRAME_VIEW_FULL: ErrorFrameView
PERSISTENT_DISK_TYPE_UNSPECIFIED: PersistentDiskType
PERSISTENT_DISK_TYPE_STANDARD: PersistentDiskType
PERSISTENT_DISK_TYPE_BALANCED: PersistentDiskType
PERSISTENT_DISK_TYPE_SSD: PersistentDiskType
LICENSE_TYPE_UNSPECIFIED: LicenseType
LICENSE_TYPE_DEFAULT: LicenseType
LICENSE_TYPE_BRING_YOUR_OWN_LICENSE: LicenseType
SIZING_OPTIMIZATION_STRATEGY_UNSPECIFIED: SizingOptimizationStrategy
SIZING_OPTIMIZATION_STRATEGY_SAME_AS_SOURCE: SizingOptimizationStrategy
SIZING_OPTIMIZATION_STRATEGY_MODERATE: SizingOptimizationStrategy
SIZING_OPTIMIZATION_STRATEGY_AGGRESSIVE: SizingOptimizationStrategy
COMMITMENT_PLAN_UNSPECIFIED: CommitmentPlan
COMMITMENT_PLAN_NONE: CommitmentPlan
COMMITMENT_PLAN_ONE_YEAR: CommitmentPlan
COMMITMENT_PLAN_THREE_YEARS: CommitmentPlan
COMPUTE_MIGRATION_TARGET_PRODUCT_UNSPECIFIED: ComputeMigrationTargetProduct
COMPUTE_MIGRATION_TARGET_PRODUCT_COMPUTE_ENGINE: ComputeMigrationTargetProduct
COMPUTE_MIGRATION_TARGET_PRODUCT_VMWARE_ENGINE: ComputeMigrationTargetProduct
COMPUTE_MIGRATION_TARGET_PRODUCT_SOLE_TENANCY: ComputeMigrationTargetProduct
REPORT_VIEW_UNSPECIFIED: ReportView
REPORT_VIEW_BASIC: ReportView
REPORT_VIEW_FULL: ReportView
REPORT_VIEW_STANDARD: ReportView

class Asset(_message.Message):
    __slots__ = ('name', 'create_time', 'update_time', 'labels', 'attributes', 'machine_details', 'insight_list', 'performance_data', 'sources', 'assigned_groups')

    class LabelsEntry(_message.Message):
        __slots__ = ('key', 'value')
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: str

        def __init__(self, key: _Optional[str]=..., value: _Optional[str]=...) -> None:
            ...

    class AttributesEntry(_message.Message):
        __slots__ = ('key', 'value')
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: str

        def __init__(self, key: _Optional[str]=..., value: _Optional[str]=...) -> None:
            ...
    NAME_FIELD_NUMBER: _ClassVar[int]
    CREATE_TIME_FIELD_NUMBER: _ClassVar[int]
    UPDATE_TIME_FIELD_NUMBER: _ClassVar[int]
    LABELS_FIELD_NUMBER: _ClassVar[int]
    ATTRIBUTES_FIELD_NUMBER: _ClassVar[int]
    MACHINE_DETAILS_FIELD_NUMBER: _ClassVar[int]
    INSIGHT_LIST_FIELD_NUMBER: _ClassVar[int]
    PERFORMANCE_DATA_FIELD_NUMBER: _ClassVar[int]
    SOURCES_FIELD_NUMBER: _ClassVar[int]
    ASSIGNED_GROUPS_FIELD_NUMBER: _ClassVar[int]
    name: str
    create_time: _timestamp_pb2.Timestamp
    update_time: _timestamp_pb2.Timestamp
    labels: _containers.ScalarMap[str, str]
    attributes: _containers.ScalarMap[str, str]
    machine_details: MachineDetails
    insight_list: InsightList
    performance_data: AssetPerformanceData
    sources: _containers.RepeatedScalarFieldContainer[str]
    assigned_groups: _containers.RepeatedScalarFieldContainer[str]

    def __init__(self, name: _Optional[str]=..., create_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]]=..., update_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]]=..., labels: _Optional[_Mapping[str, str]]=..., attributes: _Optional[_Mapping[str, str]]=..., machine_details: _Optional[_Union[MachineDetails, _Mapping]]=..., insight_list: _Optional[_Union[InsightList, _Mapping]]=..., performance_data: _Optional[_Union[AssetPerformanceData, _Mapping]]=..., sources: _Optional[_Iterable[str]]=..., assigned_groups: _Optional[_Iterable[str]]=...) -> None:
        ...

class PreferenceSet(_message.Message):
    __slots__ = ('name', 'create_time', 'update_time', 'display_name', 'description', 'virtual_machine_preferences')
    NAME_FIELD_NUMBER: _ClassVar[int]
    CREATE_TIME_FIELD_NUMBER: _ClassVar[int]
    UPDATE_TIME_FIELD_NUMBER: _ClassVar[int]
    DISPLAY_NAME_FIELD_NUMBER: _ClassVar[int]
    DESCRIPTION_FIELD_NUMBER: _ClassVar[int]
    VIRTUAL_MACHINE_PREFERENCES_FIELD_NUMBER: _ClassVar[int]
    name: str
    create_time: _timestamp_pb2.Timestamp
    update_time: _timestamp_pb2.Timestamp
    display_name: str
    description: str
    virtual_machine_preferences: VirtualMachinePreferences

    def __init__(self, name: _Optional[str]=..., create_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]]=..., update_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]]=..., display_name: _Optional[str]=..., description: _Optional[str]=..., virtual_machine_preferences: _Optional[_Union[VirtualMachinePreferences, _Mapping]]=...) -> None:
        ...

class ImportJob(_message.Message):
    __slots__ = ('name', 'display_name', 'create_time', 'update_time', 'complete_time', 'state', 'labels', 'asset_source', 'validation_report', 'execution_report')

    class ImportJobState(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        IMPORT_JOB_STATE_UNSPECIFIED: _ClassVar[ImportJob.ImportJobState]
        IMPORT_JOB_STATE_PENDING: _ClassVar[ImportJob.ImportJobState]
        IMPORT_JOB_STATE_RUNNING: _ClassVar[ImportJob.ImportJobState]
        IMPORT_JOB_STATE_COMPLETED: _ClassVar[ImportJob.ImportJobState]
        IMPORT_JOB_STATE_FAILED: _ClassVar[ImportJob.ImportJobState]
        IMPORT_JOB_STATE_VALIDATING: _ClassVar[ImportJob.ImportJobState]
        IMPORT_JOB_STATE_FAILED_VALIDATION: _ClassVar[ImportJob.ImportJobState]
        IMPORT_JOB_STATE_READY: _ClassVar[ImportJob.ImportJobState]
    IMPORT_JOB_STATE_UNSPECIFIED: ImportJob.ImportJobState
    IMPORT_JOB_STATE_PENDING: ImportJob.ImportJobState
    IMPORT_JOB_STATE_RUNNING: ImportJob.ImportJobState
    IMPORT_JOB_STATE_COMPLETED: ImportJob.ImportJobState
    IMPORT_JOB_STATE_FAILED: ImportJob.ImportJobState
    IMPORT_JOB_STATE_VALIDATING: ImportJob.ImportJobState
    IMPORT_JOB_STATE_FAILED_VALIDATION: ImportJob.ImportJobState
    IMPORT_JOB_STATE_READY: ImportJob.ImportJobState

    class LabelsEntry(_message.Message):
        __slots__ = ('key', 'value')
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: str

        def __init__(self, key: _Optional[str]=..., value: _Optional[str]=...) -> None:
            ...
    NAME_FIELD_NUMBER: _ClassVar[int]
    DISPLAY_NAME_FIELD_NUMBER: _ClassVar[int]
    CREATE_TIME_FIELD_NUMBER: _ClassVar[int]
    UPDATE_TIME_FIELD_NUMBER: _ClassVar[int]
    COMPLETE_TIME_FIELD_NUMBER: _ClassVar[int]
    STATE_FIELD_NUMBER: _ClassVar[int]
    LABELS_FIELD_NUMBER: _ClassVar[int]
    ASSET_SOURCE_FIELD_NUMBER: _ClassVar[int]
    VALIDATION_REPORT_FIELD_NUMBER: _ClassVar[int]
    EXECUTION_REPORT_FIELD_NUMBER: _ClassVar[int]
    name: str
    display_name: str
    create_time: _timestamp_pb2.Timestamp
    update_time: _timestamp_pb2.Timestamp
    complete_time: _timestamp_pb2.Timestamp
    state: ImportJob.ImportJobState
    labels: _containers.ScalarMap[str, str]
    asset_source: str
    validation_report: ValidationReport
    execution_report: ExecutionReport

    def __init__(self, name: _Optional[str]=..., display_name: _Optional[str]=..., create_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]]=..., update_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]]=..., complete_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]]=..., state: _Optional[_Union[ImportJob.ImportJobState, str]]=..., labels: _Optional[_Mapping[str, str]]=..., asset_source: _Optional[str]=..., validation_report: _Optional[_Union[ValidationReport, _Mapping]]=..., execution_report: _Optional[_Union[ExecutionReport, _Mapping]]=...) -> None:
        ...

class ImportDataFile(_message.Message):
    __slots__ = ('name', 'display_name', 'format', 'create_time', 'state', 'upload_file_info')

    class State(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        STATE_UNSPECIFIED: _ClassVar[ImportDataFile.State]
        CREATING: _ClassVar[ImportDataFile.State]
        ACTIVE: _ClassVar[ImportDataFile.State]
    STATE_UNSPECIFIED: ImportDataFile.State
    CREATING: ImportDataFile.State
    ACTIVE: ImportDataFile.State
    NAME_FIELD_NUMBER: _ClassVar[int]
    DISPLAY_NAME_FIELD_NUMBER: _ClassVar[int]
    FORMAT_FIELD_NUMBER: _ClassVar[int]
    CREATE_TIME_FIELD_NUMBER: _ClassVar[int]
    STATE_FIELD_NUMBER: _ClassVar[int]
    UPLOAD_FILE_INFO_FIELD_NUMBER: _ClassVar[int]
    name: str
    display_name: str
    format: ImportJobFormat
    create_time: _timestamp_pb2.Timestamp
    state: ImportDataFile.State
    upload_file_info: UploadFileInfo

    def __init__(self, name: _Optional[str]=..., display_name: _Optional[str]=..., format: _Optional[_Union[ImportJobFormat, str]]=..., create_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]]=..., state: _Optional[_Union[ImportDataFile.State, str]]=..., upload_file_info: _Optional[_Union[UploadFileInfo, _Mapping]]=...) -> None:
        ...

class Group(_message.Message):
    __slots__ = ('name', 'create_time', 'update_time', 'labels', 'display_name', 'description')

    class LabelsEntry(_message.Message):
        __slots__ = ('key', 'value')
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: str

        def __init__(self, key: _Optional[str]=..., value: _Optional[str]=...) -> None:
            ...
    NAME_FIELD_NUMBER: _ClassVar[int]
    CREATE_TIME_FIELD_NUMBER: _ClassVar[int]
    UPDATE_TIME_FIELD_NUMBER: _ClassVar[int]
    LABELS_FIELD_NUMBER: _ClassVar[int]
    DISPLAY_NAME_FIELD_NUMBER: _ClassVar[int]
    DESCRIPTION_FIELD_NUMBER: _ClassVar[int]
    name: str
    create_time: _timestamp_pb2.Timestamp
    update_time: _timestamp_pb2.Timestamp
    labels: _containers.ScalarMap[str, str]
    display_name: str
    description: str

    def __init__(self, name: _Optional[str]=..., create_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]]=..., update_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]]=..., labels: _Optional[_Mapping[str, str]]=..., display_name: _Optional[str]=..., description: _Optional[str]=...) -> None:
        ...

class ErrorFrame(_message.Message):
    __slots__ = ('name', 'violations', 'original_frame', 'ingestion_time')
    NAME_FIELD_NUMBER: _ClassVar[int]
    VIOLATIONS_FIELD_NUMBER: _ClassVar[int]
    ORIGINAL_FRAME_FIELD_NUMBER: _ClassVar[int]
    INGESTION_TIME_FIELD_NUMBER: _ClassVar[int]
    name: str
    violations: _containers.RepeatedCompositeFieldContainer[FrameViolationEntry]
    original_frame: AssetFrame
    ingestion_time: _timestamp_pb2.Timestamp

    def __init__(self, name: _Optional[str]=..., violations: _Optional[_Iterable[_Union[FrameViolationEntry, _Mapping]]]=..., original_frame: _Optional[_Union[AssetFrame, _Mapping]]=..., ingestion_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]]=...) -> None:
        ...

class Source(_message.Message):
    __slots__ = ('name', 'create_time', 'update_time', 'display_name', 'description', 'type', 'priority', 'managed', 'pending_frame_count', 'error_frame_count', 'state')

    class SourceType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        SOURCE_TYPE_UNKNOWN: _ClassVar[Source.SourceType]
        SOURCE_TYPE_UPLOAD: _ClassVar[Source.SourceType]
        SOURCE_TYPE_GUEST_OS_SCAN: _ClassVar[Source.SourceType]
        SOURCE_TYPE_INVENTORY_SCAN: _ClassVar[Source.SourceType]
        SOURCE_TYPE_CUSTOM: _ClassVar[Source.SourceType]
    SOURCE_TYPE_UNKNOWN: Source.SourceType
    SOURCE_TYPE_UPLOAD: Source.SourceType
    SOURCE_TYPE_GUEST_OS_SCAN: Source.SourceType
    SOURCE_TYPE_INVENTORY_SCAN: Source.SourceType
    SOURCE_TYPE_CUSTOM: Source.SourceType

    class State(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        STATE_UNSPECIFIED: _ClassVar[Source.State]
        ACTIVE: _ClassVar[Source.State]
        DELETING: _ClassVar[Source.State]
        INVALID: _ClassVar[Source.State]
    STATE_UNSPECIFIED: Source.State
    ACTIVE: Source.State
    DELETING: Source.State
    INVALID: Source.State
    NAME_FIELD_NUMBER: _ClassVar[int]
    CREATE_TIME_FIELD_NUMBER: _ClassVar[int]
    UPDATE_TIME_FIELD_NUMBER: _ClassVar[int]
    DISPLAY_NAME_FIELD_NUMBER: _ClassVar[int]
    DESCRIPTION_FIELD_NUMBER: _ClassVar[int]
    TYPE_FIELD_NUMBER: _ClassVar[int]
    PRIORITY_FIELD_NUMBER: _ClassVar[int]
    MANAGED_FIELD_NUMBER: _ClassVar[int]
    PENDING_FRAME_COUNT_FIELD_NUMBER: _ClassVar[int]
    ERROR_FRAME_COUNT_FIELD_NUMBER: _ClassVar[int]
    STATE_FIELD_NUMBER: _ClassVar[int]
    name: str
    create_time: _timestamp_pb2.Timestamp
    update_time: _timestamp_pb2.Timestamp
    display_name: str
    description: str
    type: Source.SourceType
    priority: int
    managed: bool
    pending_frame_count: int
    error_frame_count: int
    state: Source.State

    def __init__(self, name: _Optional[str]=..., create_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]]=..., update_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]]=..., display_name: _Optional[str]=..., description: _Optional[str]=..., type: _Optional[_Union[Source.SourceType, str]]=..., priority: _Optional[int]=..., managed: bool=..., pending_frame_count: _Optional[int]=..., error_frame_count: _Optional[int]=..., state: _Optional[_Union[Source.State, str]]=...) -> None:
        ...

class ReportConfig(_message.Message):
    __slots__ = ('name', 'create_time', 'update_time', 'display_name', 'description', 'group_preferenceset_assignments')

    class GroupPreferenceSetAssignment(_message.Message):
        __slots__ = ('group', 'preference_set')
        GROUP_FIELD_NUMBER: _ClassVar[int]
        PREFERENCE_SET_FIELD_NUMBER: _ClassVar[int]
        group: str
        preference_set: str

        def __init__(self, group: _Optional[str]=..., preference_set: _Optional[str]=...) -> None:
            ...
    NAME_FIELD_NUMBER: _ClassVar[int]
    CREATE_TIME_FIELD_NUMBER: _ClassVar[int]
    UPDATE_TIME_FIELD_NUMBER: _ClassVar[int]
    DISPLAY_NAME_FIELD_NUMBER: _ClassVar[int]
    DESCRIPTION_FIELD_NUMBER: _ClassVar[int]
    GROUP_PREFERENCESET_ASSIGNMENTS_FIELD_NUMBER: _ClassVar[int]
    name: str
    create_time: _timestamp_pb2.Timestamp
    update_time: _timestamp_pb2.Timestamp
    display_name: str
    description: str
    group_preferenceset_assignments: _containers.RepeatedCompositeFieldContainer[ReportConfig.GroupPreferenceSetAssignment]

    def __init__(self, name: _Optional[str]=..., create_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]]=..., update_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]]=..., display_name: _Optional[str]=..., description: _Optional[str]=..., group_preferenceset_assignments: _Optional[_Iterable[_Union[ReportConfig.GroupPreferenceSetAssignment, _Mapping]]]=...) -> None:
        ...

class Report(_message.Message):
    __slots__ = ('name', 'create_time', 'update_time', 'display_name', 'description', 'type', 'state', 'summary')

    class Type(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        TYPE_UNSPECIFIED: _ClassVar[Report.Type]
        TOTAL_COST_OF_OWNERSHIP: _ClassVar[Report.Type]
    TYPE_UNSPECIFIED: Report.Type
    TOTAL_COST_OF_OWNERSHIP: Report.Type

    class State(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        STATE_UNSPECIFIED: _ClassVar[Report.State]
        PENDING: _ClassVar[Report.State]
        SUCCEEDED: _ClassVar[Report.State]
        FAILED: _ClassVar[Report.State]
    STATE_UNSPECIFIED: Report.State
    PENDING: Report.State
    SUCCEEDED: Report.State
    FAILED: Report.State
    NAME_FIELD_NUMBER: _ClassVar[int]
    CREATE_TIME_FIELD_NUMBER: _ClassVar[int]
    UPDATE_TIME_FIELD_NUMBER: _ClassVar[int]
    DISPLAY_NAME_FIELD_NUMBER: _ClassVar[int]
    DESCRIPTION_FIELD_NUMBER: _ClassVar[int]
    TYPE_FIELD_NUMBER: _ClassVar[int]
    STATE_FIELD_NUMBER: _ClassVar[int]
    SUMMARY_FIELD_NUMBER: _ClassVar[int]
    name: str
    create_time: _timestamp_pb2.Timestamp
    update_time: _timestamp_pb2.Timestamp
    display_name: str
    description: str
    type: Report.Type
    state: Report.State
    summary: ReportSummary

    def __init__(self, name: _Optional[str]=..., create_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]]=..., update_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]]=..., display_name: _Optional[str]=..., description: _Optional[str]=..., type: _Optional[_Union[Report.Type, str]]=..., state: _Optional[_Union[Report.State, str]]=..., summary: _Optional[_Union[ReportSummary, _Mapping]]=...) -> None:
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

class ListAssetsRequest(_message.Message):
    __slots__ = ('parent', 'page_size', 'page_token', 'filter', 'order_by', 'view')
    PARENT_FIELD_NUMBER: _ClassVar[int]
    PAGE_SIZE_FIELD_NUMBER: _ClassVar[int]
    PAGE_TOKEN_FIELD_NUMBER: _ClassVar[int]
    FILTER_FIELD_NUMBER: _ClassVar[int]
    ORDER_BY_FIELD_NUMBER: _ClassVar[int]
    VIEW_FIELD_NUMBER: _ClassVar[int]
    parent: str
    page_size: int
    page_token: str
    filter: str
    order_by: str
    view: AssetView

    def __init__(self, parent: _Optional[str]=..., page_size: _Optional[int]=..., page_token: _Optional[str]=..., filter: _Optional[str]=..., order_by: _Optional[str]=..., view: _Optional[_Union[AssetView, str]]=...) -> None:
        ...

class ListAssetsResponse(_message.Message):
    __slots__ = ('assets', 'next_page_token', 'unreachable')
    ASSETS_FIELD_NUMBER: _ClassVar[int]
    NEXT_PAGE_TOKEN_FIELD_NUMBER: _ClassVar[int]
    UNREACHABLE_FIELD_NUMBER: _ClassVar[int]
    assets: _containers.RepeatedCompositeFieldContainer[Asset]
    next_page_token: str
    unreachable: _containers.RepeatedScalarFieldContainer[str]

    def __init__(self, assets: _Optional[_Iterable[_Union[Asset, _Mapping]]]=..., next_page_token: _Optional[str]=..., unreachable: _Optional[_Iterable[str]]=...) -> None:
        ...

class GetAssetRequest(_message.Message):
    __slots__ = ('name', 'view')
    NAME_FIELD_NUMBER: _ClassVar[int]
    VIEW_FIELD_NUMBER: _ClassVar[int]
    name: str
    view: AssetView

    def __init__(self, name: _Optional[str]=..., view: _Optional[_Union[AssetView, str]]=...) -> None:
        ...

class UpdateAssetRequest(_message.Message):
    __slots__ = ('update_mask', 'asset', 'request_id')
    UPDATE_MASK_FIELD_NUMBER: _ClassVar[int]
    ASSET_FIELD_NUMBER: _ClassVar[int]
    REQUEST_ID_FIELD_NUMBER: _ClassVar[int]
    update_mask: _field_mask_pb2.FieldMask
    asset: Asset
    request_id: str

    def __init__(self, update_mask: _Optional[_Union[_field_mask_pb2.FieldMask, _Mapping]]=..., asset: _Optional[_Union[Asset, _Mapping]]=..., request_id: _Optional[str]=...) -> None:
        ...

class BatchUpdateAssetsRequest(_message.Message):
    __slots__ = ('parent', 'requests')
    PARENT_FIELD_NUMBER: _ClassVar[int]
    REQUESTS_FIELD_NUMBER: _ClassVar[int]
    parent: str
    requests: _containers.RepeatedCompositeFieldContainer[UpdateAssetRequest]

    def __init__(self, parent: _Optional[str]=..., requests: _Optional[_Iterable[_Union[UpdateAssetRequest, _Mapping]]]=...) -> None:
        ...

class BatchUpdateAssetsResponse(_message.Message):
    __slots__ = ('assets',)
    ASSETS_FIELD_NUMBER: _ClassVar[int]
    assets: _containers.RepeatedCompositeFieldContainer[Asset]

    def __init__(self, assets: _Optional[_Iterable[_Union[Asset, _Mapping]]]=...) -> None:
        ...

class DeleteAssetRequest(_message.Message):
    __slots__ = ('name', 'request_id')
    NAME_FIELD_NUMBER: _ClassVar[int]
    REQUEST_ID_FIELD_NUMBER: _ClassVar[int]
    name: str
    request_id: str

    def __init__(self, name: _Optional[str]=..., request_id: _Optional[str]=...) -> None:
        ...

class BatchDeleteAssetsRequest(_message.Message):
    __slots__ = ('parent', 'names', 'allow_missing')
    PARENT_FIELD_NUMBER: _ClassVar[int]
    NAMES_FIELD_NUMBER: _ClassVar[int]
    ALLOW_MISSING_FIELD_NUMBER: _ClassVar[int]
    parent: str
    names: _containers.RepeatedScalarFieldContainer[str]
    allow_missing: bool

    def __init__(self, parent: _Optional[str]=..., names: _Optional[_Iterable[str]]=..., allow_missing: bool=...) -> None:
        ...

class ReportAssetFramesRequest(_message.Message):
    __slots__ = ('parent', 'frames', 'source')
    PARENT_FIELD_NUMBER: _ClassVar[int]
    FRAMES_FIELD_NUMBER: _ClassVar[int]
    SOURCE_FIELD_NUMBER: _ClassVar[int]
    parent: str
    frames: Frames
    source: str

    def __init__(self, parent: _Optional[str]=..., frames: _Optional[_Union[Frames, _Mapping]]=..., source: _Optional[str]=...) -> None:
        ...

class ReportAssetFramesResponse(_message.Message):
    __slots__ = ()

    def __init__(self) -> None:
        ...

class AggregateAssetsValuesRequest(_message.Message):
    __slots__ = ('parent', 'aggregations', 'filter')
    PARENT_FIELD_NUMBER: _ClassVar[int]
    AGGREGATIONS_FIELD_NUMBER: _ClassVar[int]
    FILTER_FIELD_NUMBER: _ClassVar[int]
    parent: str
    aggregations: _containers.RepeatedCompositeFieldContainer[Aggregation]
    filter: str

    def __init__(self, parent: _Optional[str]=..., aggregations: _Optional[_Iterable[_Union[Aggregation, _Mapping]]]=..., filter: _Optional[str]=...) -> None:
        ...

class AggregateAssetsValuesResponse(_message.Message):
    __slots__ = ('results',)
    RESULTS_FIELD_NUMBER: _ClassVar[int]
    results: _containers.RepeatedCompositeFieldContainer[AggregationResult]

    def __init__(self, results: _Optional[_Iterable[_Union[AggregationResult, _Mapping]]]=...) -> None:
        ...

class CreateImportJobRequest(_message.Message):
    __slots__ = ('parent', 'import_job_id', 'import_job', 'request_id')
    PARENT_FIELD_NUMBER: _ClassVar[int]
    IMPORT_JOB_ID_FIELD_NUMBER: _ClassVar[int]
    IMPORT_JOB_FIELD_NUMBER: _ClassVar[int]
    REQUEST_ID_FIELD_NUMBER: _ClassVar[int]
    parent: str
    import_job_id: str
    import_job: ImportJob
    request_id: str

    def __init__(self, parent: _Optional[str]=..., import_job_id: _Optional[str]=..., import_job: _Optional[_Union[ImportJob, _Mapping]]=..., request_id: _Optional[str]=...) -> None:
        ...

class ListImportJobsRequest(_message.Message):
    __slots__ = ('parent', 'page_size', 'page_token', 'filter', 'order_by', 'view')
    PARENT_FIELD_NUMBER: _ClassVar[int]
    PAGE_SIZE_FIELD_NUMBER: _ClassVar[int]
    PAGE_TOKEN_FIELD_NUMBER: _ClassVar[int]
    FILTER_FIELD_NUMBER: _ClassVar[int]
    ORDER_BY_FIELD_NUMBER: _ClassVar[int]
    VIEW_FIELD_NUMBER: _ClassVar[int]
    parent: str
    page_size: int
    page_token: str
    filter: str
    order_by: str
    view: ImportJobView

    def __init__(self, parent: _Optional[str]=..., page_size: _Optional[int]=..., page_token: _Optional[str]=..., filter: _Optional[str]=..., order_by: _Optional[str]=..., view: _Optional[_Union[ImportJobView, str]]=...) -> None:
        ...

class ListImportJobsResponse(_message.Message):
    __slots__ = ('import_jobs', 'next_page_token', 'unreachable')
    IMPORT_JOBS_FIELD_NUMBER: _ClassVar[int]
    NEXT_PAGE_TOKEN_FIELD_NUMBER: _ClassVar[int]
    UNREACHABLE_FIELD_NUMBER: _ClassVar[int]
    import_jobs: _containers.RepeatedCompositeFieldContainer[ImportJob]
    next_page_token: str
    unreachable: _containers.RepeatedScalarFieldContainer[str]

    def __init__(self, import_jobs: _Optional[_Iterable[_Union[ImportJob, _Mapping]]]=..., next_page_token: _Optional[str]=..., unreachable: _Optional[_Iterable[str]]=...) -> None:
        ...

class GetImportJobRequest(_message.Message):
    __slots__ = ('name', 'view')
    NAME_FIELD_NUMBER: _ClassVar[int]
    VIEW_FIELD_NUMBER: _ClassVar[int]
    name: str
    view: ImportJobView

    def __init__(self, name: _Optional[str]=..., view: _Optional[_Union[ImportJobView, str]]=...) -> None:
        ...

class DeleteImportJobRequest(_message.Message):
    __slots__ = ('name', 'request_id', 'force')
    NAME_FIELD_NUMBER: _ClassVar[int]
    REQUEST_ID_FIELD_NUMBER: _ClassVar[int]
    FORCE_FIELD_NUMBER: _ClassVar[int]
    name: str
    request_id: str
    force: bool

    def __init__(self, name: _Optional[str]=..., request_id: _Optional[str]=..., force: bool=...) -> None:
        ...

class UpdateImportJobRequest(_message.Message):
    __slots__ = ('update_mask', 'import_job', 'request_id')
    UPDATE_MASK_FIELD_NUMBER: _ClassVar[int]
    IMPORT_JOB_FIELD_NUMBER: _ClassVar[int]
    REQUEST_ID_FIELD_NUMBER: _ClassVar[int]
    update_mask: _field_mask_pb2.FieldMask
    import_job: ImportJob
    request_id: str

    def __init__(self, update_mask: _Optional[_Union[_field_mask_pb2.FieldMask, _Mapping]]=..., import_job: _Optional[_Union[ImportJob, _Mapping]]=..., request_id: _Optional[str]=...) -> None:
        ...

class ValidateImportJobRequest(_message.Message):
    __slots__ = ('name', 'request_id')
    NAME_FIELD_NUMBER: _ClassVar[int]
    REQUEST_ID_FIELD_NUMBER: _ClassVar[int]
    name: str
    request_id: str

    def __init__(self, name: _Optional[str]=..., request_id: _Optional[str]=...) -> None:
        ...

class RunImportJobRequest(_message.Message):
    __slots__ = ('name', 'request_id')
    NAME_FIELD_NUMBER: _ClassVar[int]
    REQUEST_ID_FIELD_NUMBER: _ClassVar[int]
    name: str
    request_id: str

    def __init__(self, name: _Optional[str]=..., request_id: _Optional[str]=...) -> None:
        ...

class GetImportDataFileRequest(_message.Message):
    __slots__ = ('name',)
    NAME_FIELD_NUMBER: _ClassVar[int]
    name: str

    def __init__(self, name: _Optional[str]=...) -> None:
        ...

class ListImportDataFilesRequest(_message.Message):
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

class ListImportDataFilesResponse(_message.Message):
    __slots__ = ('import_data_files', 'next_page_token', 'unreachable')
    IMPORT_DATA_FILES_FIELD_NUMBER: _ClassVar[int]
    NEXT_PAGE_TOKEN_FIELD_NUMBER: _ClassVar[int]
    UNREACHABLE_FIELD_NUMBER: _ClassVar[int]
    import_data_files: _containers.RepeatedCompositeFieldContainer[ImportDataFile]
    next_page_token: str
    unreachable: _containers.RepeatedScalarFieldContainer[str]

    def __init__(self, import_data_files: _Optional[_Iterable[_Union[ImportDataFile, _Mapping]]]=..., next_page_token: _Optional[str]=..., unreachable: _Optional[_Iterable[str]]=...) -> None:
        ...

class CreateImportDataFileRequest(_message.Message):
    __slots__ = ('parent', 'import_data_file_id', 'import_data_file', 'request_id')
    PARENT_FIELD_NUMBER: _ClassVar[int]
    IMPORT_DATA_FILE_ID_FIELD_NUMBER: _ClassVar[int]
    IMPORT_DATA_FILE_FIELD_NUMBER: _ClassVar[int]
    REQUEST_ID_FIELD_NUMBER: _ClassVar[int]
    parent: str
    import_data_file_id: str
    import_data_file: ImportDataFile
    request_id: str

    def __init__(self, parent: _Optional[str]=..., import_data_file_id: _Optional[str]=..., import_data_file: _Optional[_Union[ImportDataFile, _Mapping]]=..., request_id: _Optional[str]=...) -> None:
        ...

class DeleteImportDataFileRequest(_message.Message):
    __slots__ = ('name', 'request_id')
    NAME_FIELD_NUMBER: _ClassVar[int]
    REQUEST_ID_FIELD_NUMBER: _ClassVar[int]
    name: str
    request_id: str

    def __init__(self, name: _Optional[str]=..., request_id: _Optional[str]=...) -> None:
        ...

class ListGroupsRequest(_message.Message):
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

class ListGroupsResponse(_message.Message):
    __slots__ = ('groups', 'next_page_token', 'unreachable')
    GROUPS_FIELD_NUMBER: _ClassVar[int]
    NEXT_PAGE_TOKEN_FIELD_NUMBER: _ClassVar[int]
    UNREACHABLE_FIELD_NUMBER: _ClassVar[int]
    groups: _containers.RepeatedCompositeFieldContainer[Group]
    next_page_token: str
    unreachable: _containers.RepeatedScalarFieldContainer[str]

    def __init__(self, groups: _Optional[_Iterable[_Union[Group, _Mapping]]]=..., next_page_token: _Optional[str]=..., unreachable: _Optional[_Iterable[str]]=...) -> None:
        ...

class GetGroupRequest(_message.Message):
    __slots__ = ('name',)
    NAME_FIELD_NUMBER: _ClassVar[int]
    name: str

    def __init__(self, name: _Optional[str]=...) -> None:
        ...

class CreateGroupRequest(_message.Message):
    __slots__ = ('parent', 'group_id', 'group', 'request_id')
    PARENT_FIELD_NUMBER: _ClassVar[int]
    GROUP_ID_FIELD_NUMBER: _ClassVar[int]
    GROUP_FIELD_NUMBER: _ClassVar[int]
    REQUEST_ID_FIELD_NUMBER: _ClassVar[int]
    parent: str
    group_id: str
    group: Group
    request_id: str

    def __init__(self, parent: _Optional[str]=..., group_id: _Optional[str]=..., group: _Optional[_Union[Group, _Mapping]]=..., request_id: _Optional[str]=...) -> None:
        ...

class UpdateGroupRequest(_message.Message):
    __slots__ = ('update_mask', 'group', 'request_id')
    UPDATE_MASK_FIELD_NUMBER: _ClassVar[int]
    GROUP_FIELD_NUMBER: _ClassVar[int]
    REQUEST_ID_FIELD_NUMBER: _ClassVar[int]
    update_mask: _field_mask_pb2.FieldMask
    group: Group
    request_id: str

    def __init__(self, update_mask: _Optional[_Union[_field_mask_pb2.FieldMask, _Mapping]]=..., group: _Optional[_Union[Group, _Mapping]]=..., request_id: _Optional[str]=...) -> None:
        ...

class DeleteGroupRequest(_message.Message):
    __slots__ = ('name', 'request_id')
    NAME_FIELD_NUMBER: _ClassVar[int]
    REQUEST_ID_FIELD_NUMBER: _ClassVar[int]
    name: str
    request_id: str

    def __init__(self, name: _Optional[str]=..., request_id: _Optional[str]=...) -> None:
        ...

class AddAssetsToGroupRequest(_message.Message):
    __slots__ = ('group', 'request_id', 'assets', 'allow_existing')
    GROUP_FIELD_NUMBER: _ClassVar[int]
    REQUEST_ID_FIELD_NUMBER: _ClassVar[int]
    ASSETS_FIELD_NUMBER: _ClassVar[int]
    ALLOW_EXISTING_FIELD_NUMBER: _ClassVar[int]
    group: str
    request_id: str
    assets: AssetList
    allow_existing: bool

    def __init__(self, group: _Optional[str]=..., request_id: _Optional[str]=..., assets: _Optional[_Union[AssetList, _Mapping]]=..., allow_existing: bool=...) -> None:
        ...

class RemoveAssetsFromGroupRequest(_message.Message):
    __slots__ = ('group', 'request_id', 'assets', 'allow_missing')
    GROUP_FIELD_NUMBER: _ClassVar[int]
    REQUEST_ID_FIELD_NUMBER: _ClassVar[int]
    ASSETS_FIELD_NUMBER: _ClassVar[int]
    ALLOW_MISSING_FIELD_NUMBER: _ClassVar[int]
    group: str
    request_id: str
    assets: AssetList
    allow_missing: bool

    def __init__(self, group: _Optional[str]=..., request_id: _Optional[str]=..., assets: _Optional[_Union[AssetList, _Mapping]]=..., allow_missing: bool=...) -> None:
        ...

class ListErrorFramesRequest(_message.Message):
    __slots__ = ('parent', 'page_size', 'page_token', 'view')
    PARENT_FIELD_NUMBER: _ClassVar[int]
    PAGE_SIZE_FIELD_NUMBER: _ClassVar[int]
    PAGE_TOKEN_FIELD_NUMBER: _ClassVar[int]
    VIEW_FIELD_NUMBER: _ClassVar[int]
    parent: str
    page_size: int
    page_token: str
    view: ErrorFrameView

    def __init__(self, parent: _Optional[str]=..., page_size: _Optional[int]=..., page_token: _Optional[str]=..., view: _Optional[_Union[ErrorFrameView, str]]=...) -> None:
        ...

class ListErrorFramesResponse(_message.Message):
    __slots__ = ('error_frames', 'next_page_token', 'unreachable')
    ERROR_FRAMES_FIELD_NUMBER: _ClassVar[int]
    NEXT_PAGE_TOKEN_FIELD_NUMBER: _ClassVar[int]
    UNREACHABLE_FIELD_NUMBER: _ClassVar[int]
    error_frames: _containers.RepeatedCompositeFieldContainer[ErrorFrame]
    next_page_token: str
    unreachable: _containers.RepeatedScalarFieldContainer[str]

    def __init__(self, error_frames: _Optional[_Iterable[_Union[ErrorFrame, _Mapping]]]=..., next_page_token: _Optional[str]=..., unreachable: _Optional[_Iterable[str]]=...) -> None:
        ...

class GetErrorFrameRequest(_message.Message):
    __slots__ = ('name', 'view')
    NAME_FIELD_NUMBER: _ClassVar[int]
    VIEW_FIELD_NUMBER: _ClassVar[int]
    name: str
    view: ErrorFrameView

    def __init__(self, name: _Optional[str]=..., view: _Optional[_Union[ErrorFrameView, str]]=...) -> None:
        ...

class ListSourcesRequest(_message.Message):
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

class ListSourcesResponse(_message.Message):
    __slots__ = ('sources', 'next_page_token', 'unreachable')
    SOURCES_FIELD_NUMBER: _ClassVar[int]
    NEXT_PAGE_TOKEN_FIELD_NUMBER: _ClassVar[int]
    UNREACHABLE_FIELD_NUMBER: _ClassVar[int]
    sources: _containers.RepeatedCompositeFieldContainer[Source]
    next_page_token: str
    unreachable: _containers.RepeatedScalarFieldContainer[str]

    def __init__(self, sources: _Optional[_Iterable[_Union[Source, _Mapping]]]=..., next_page_token: _Optional[str]=..., unreachable: _Optional[_Iterable[str]]=...) -> None:
        ...

class GetSourceRequest(_message.Message):
    __slots__ = ('name',)
    NAME_FIELD_NUMBER: _ClassVar[int]
    name: str

    def __init__(self, name: _Optional[str]=...) -> None:
        ...

class CreateSourceRequest(_message.Message):
    __slots__ = ('parent', 'source_id', 'source', 'request_id')
    PARENT_FIELD_NUMBER: _ClassVar[int]
    SOURCE_ID_FIELD_NUMBER: _ClassVar[int]
    SOURCE_FIELD_NUMBER: _ClassVar[int]
    REQUEST_ID_FIELD_NUMBER: _ClassVar[int]
    parent: str
    source_id: str
    source: Source
    request_id: str

    def __init__(self, parent: _Optional[str]=..., source_id: _Optional[str]=..., source: _Optional[_Union[Source, _Mapping]]=..., request_id: _Optional[str]=...) -> None:
        ...

class UpdateSourceRequest(_message.Message):
    __slots__ = ('update_mask', 'source', 'request_id')
    UPDATE_MASK_FIELD_NUMBER: _ClassVar[int]
    SOURCE_FIELD_NUMBER: _ClassVar[int]
    REQUEST_ID_FIELD_NUMBER: _ClassVar[int]
    update_mask: _field_mask_pb2.FieldMask
    source: Source
    request_id: str

    def __init__(self, update_mask: _Optional[_Union[_field_mask_pb2.FieldMask, _Mapping]]=..., source: _Optional[_Union[Source, _Mapping]]=..., request_id: _Optional[str]=...) -> None:
        ...

class DeleteSourceRequest(_message.Message):
    __slots__ = ('name', 'request_id')
    NAME_FIELD_NUMBER: _ClassVar[int]
    REQUEST_ID_FIELD_NUMBER: _ClassVar[int]
    name: str
    request_id: str

    def __init__(self, name: _Optional[str]=..., request_id: _Optional[str]=...) -> None:
        ...

class ListPreferenceSetsRequest(_message.Message):
    __slots__ = ('parent', 'page_size', 'page_token', 'order_by')
    PARENT_FIELD_NUMBER: _ClassVar[int]
    PAGE_SIZE_FIELD_NUMBER: _ClassVar[int]
    PAGE_TOKEN_FIELD_NUMBER: _ClassVar[int]
    ORDER_BY_FIELD_NUMBER: _ClassVar[int]
    parent: str
    page_size: int
    page_token: str
    order_by: str

    def __init__(self, parent: _Optional[str]=..., page_size: _Optional[int]=..., page_token: _Optional[str]=..., order_by: _Optional[str]=...) -> None:
        ...

class ListPreferenceSetsResponse(_message.Message):
    __slots__ = ('preference_sets', 'next_page_token', 'unreachable')
    PREFERENCE_SETS_FIELD_NUMBER: _ClassVar[int]
    NEXT_PAGE_TOKEN_FIELD_NUMBER: _ClassVar[int]
    UNREACHABLE_FIELD_NUMBER: _ClassVar[int]
    preference_sets: _containers.RepeatedCompositeFieldContainer[PreferenceSet]
    next_page_token: str
    unreachable: _containers.RepeatedScalarFieldContainer[str]

    def __init__(self, preference_sets: _Optional[_Iterable[_Union[PreferenceSet, _Mapping]]]=..., next_page_token: _Optional[str]=..., unreachable: _Optional[_Iterable[str]]=...) -> None:
        ...

class GetPreferenceSetRequest(_message.Message):
    __slots__ = ('name',)
    NAME_FIELD_NUMBER: _ClassVar[int]
    name: str

    def __init__(self, name: _Optional[str]=...) -> None:
        ...

class CreatePreferenceSetRequest(_message.Message):
    __slots__ = ('parent', 'preference_set_id', 'preference_set', 'request_id')
    PARENT_FIELD_NUMBER: _ClassVar[int]
    PREFERENCE_SET_ID_FIELD_NUMBER: _ClassVar[int]
    PREFERENCE_SET_FIELD_NUMBER: _ClassVar[int]
    REQUEST_ID_FIELD_NUMBER: _ClassVar[int]
    parent: str
    preference_set_id: str
    preference_set: PreferenceSet
    request_id: str

    def __init__(self, parent: _Optional[str]=..., preference_set_id: _Optional[str]=..., preference_set: _Optional[_Union[PreferenceSet, _Mapping]]=..., request_id: _Optional[str]=...) -> None:
        ...

class UpdatePreferenceSetRequest(_message.Message):
    __slots__ = ('update_mask', 'preference_set', 'request_id')
    UPDATE_MASK_FIELD_NUMBER: _ClassVar[int]
    PREFERENCE_SET_FIELD_NUMBER: _ClassVar[int]
    REQUEST_ID_FIELD_NUMBER: _ClassVar[int]
    update_mask: _field_mask_pb2.FieldMask
    preference_set: PreferenceSet
    request_id: str

    def __init__(self, update_mask: _Optional[_Union[_field_mask_pb2.FieldMask, _Mapping]]=..., preference_set: _Optional[_Union[PreferenceSet, _Mapping]]=..., request_id: _Optional[str]=...) -> None:
        ...

class DeletePreferenceSetRequest(_message.Message):
    __slots__ = ('name', 'request_id')
    NAME_FIELD_NUMBER: _ClassVar[int]
    REQUEST_ID_FIELD_NUMBER: _ClassVar[int]
    name: str
    request_id: str

    def __init__(self, name: _Optional[str]=..., request_id: _Optional[str]=...) -> None:
        ...

class GetSettingsRequest(_message.Message):
    __slots__ = ('name',)
    NAME_FIELD_NUMBER: _ClassVar[int]
    name: str

    def __init__(self, name: _Optional[str]=...) -> None:
        ...

class UpdateSettingsRequest(_message.Message):
    __slots__ = ('update_mask', 'settings', 'request_id')
    UPDATE_MASK_FIELD_NUMBER: _ClassVar[int]
    SETTINGS_FIELD_NUMBER: _ClassVar[int]
    REQUEST_ID_FIELD_NUMBER: _ClassVar[int]
    update_mask: _field_mask_pb2.FieldMask
    settings: Settings
    request_id: str

    def __init__(self, update_mask: _Optional[_Union[_field_mask_pb2.FieldMask, _Mapping]]=..., settings: _Optional[_Union[Settings, _Mapping]]=..., request_id: _Optional[str]=...) -> None:
        ...

class CreateReportConfigRequest(_message.Message):
    __slots__ = ('parent', 'report_config_id', 'report_config', 'request_id')
    PARENT_FIELD_NUMBER: _ClassVar[int]
    REPORT_CONFIG_ID_FIELD_NUMBER: _ClassVar[int]
    REPORT_CONFIG_FIELD_NUMBER: _ClassVar[int]
    REQUEST_ID_FIELD_NUMBER: _ClassVar[int]
    parent: str
    report_config_id: str
    report_config: ReportConfig
    request_id: str

    def __init__(self, parent: _Optional[str]=..., report_config_id: _Optional[str]=..., report_config: _Optional[_Union[ReportConfig, _Mapping]]=..., request_id: _Optional[str]=...) -> None:
        ...

class DeleteReportConfigRequest(_message.Message):
    __slots__ = ('name', 'request_id', 'force')
    NAME_FIELD_NUMBER: _ClassVar[int]
    REQUEST_ID_FIELD_NUMBER: _ClassVar[int]
    FORCE_FIELD_NUMBER: _ClassVar[int]
    name: str
    request_id: str
    force: bool

    def __init__(self, name: _Optional[str]=..., request_id: _Optional[str]=..., force: bool=...) -> None:
        ...

class GetReportRequest(_message.Message):
    __slots__ = ('name', 'view')
    NAME_FIELD_NUMBER: _ClassVar[int]
    VIEW_FIELD_NUMBER: _ClassVar[int]
    name: str
    view: ReportView

    def __init__(self, name: _Optional[str]=..., view: _Optional[_Union[ReportView, str]]=...) -> None:
        ...

class ListReportsRequest(_message.Message):
    __slots__ = ('parent', 'page_size', 'page_token', 'filter', 'order_by', 'view')
    PARENT_FIELD_NUMBER: _ClassVar[int]
    PAGE_SIZE_FIELD_NUMBER: _ClassVar[int]
    PAGE_TOKEN_FIELD_NUMBER: _ClassVar[int]
    FILTER_FIELD_NUMBER: _ClassVar[int]
    ORDER_BY_FIELD_NUMBER: _ClassVar[int]
    VIEW_FIELD_NUMBER: _ClassVar[int]
    parent: str
    page_size: int
    page_token: str
    filter: str
    order_by: str
    view: ReportView

    def __init__(self, parent: _Optional[str]=..., page_size: _Optional[int]=..., page_token: _Optional[str]=..., filter: _Optional[str]=..., order_by: _Optional[str]=..., view: _Optional[_Union[ReportView, str]]=...) -> None:
        ...

class ListReportsResponse(_message.Message):
    __slots__ = ('reports', 'next_page_token', 'unreachable')
    REPORTS_FIELD_NUMBER: _ClassVar[int]
    NEXT_PAGE_TOKEN_FIELD_NUMBER: _ClassVar[int]
    UNREACHABLE_FIELD_NUMBER: _ClassVar[int]
    reports: _containers.RepeatedCompositeFieldContainer[Report]
    next_page_token: str
    unreachable: _containers.RepeatedScalarFieldContainer[str]

    def __init__(self, reports: _Optional[_Iterable[_Union[Report, _Mapping]]]=..., next_page_token: _Optional[str]=..., unreachable: _Optional[_Iterable[str]]=...) -> None:
        ...

class DeleteReportRequest(_message.Message):
    __slots__ = ('name', 'request_id')
    NAME_FIELD_NUMBER: _ClassVar[int]
    REQUEST_ID_FIELD_NUMBER: _ClassVar[int]
    name: str
    request_id: str

    def __init__(self, name: _Optional[str]=..., request_id: _Optional[str]=...) -> None:
        ...

class GetReportConfigRequest(_message.Message):
    __slots__ = ('name',)
    NAME_FIELD_NUMBER: _ClassVar[int]
    name: str

    def __init__(self, name: _Optional[str]=...) -> None:
        ...

class ListReportConfigsRequest(_message.Message):
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

class ListReportConfigsResponse(_message.Message):
    __slots__ = ('report_configs', 'next_page_token', 'unreachable')
    REPORT_CONFIGS_FIELD_NUMBER: _ClassVar[int]
    NEXT_PAGE_TOKEN_FIELD_NUMBER: _ClassVar[int]
    UNREACHABLE_FIELD_NUMBER: _ClassVar[int]
    report_configs: _containers.RepeatedCompositeFieldContainer[ReportConfig]
    next_page_token: str
    unreachable: _containers.RepeatedScalarFieldContainer[str]

    def __init__(self, report_configs: _Optional[_Iterable[_Union[ReportConfig, _Mapping]]]=..., next_page_token: _Optional[str]=..., unreachable: _Optional[_Iterable[str]]=...) -> None:
        ...

class CreateReportRequest(_message.Message):
    __slots__ = ('parent', 'report_id', 'report', 'request_id')
    PARENT_FIELD_NUMBER: _ClassVar[int]
    REPORT_ID_FIELD_NUMBER: _ClassVar[int]
    REPORT_FIELD_NUMBER: _ClassVar[int]
    REQUEST_ID_FIELD_NUMBER: _ClassVar[int]
    parent: str
    report_id: str
    report: Report
    request_id: str

    def __init__(self, parent: _Optional[str]=..., report_id: _Optional[str]=..., report: _Optional[_Union[Report, _Mapping]]=..., request_id: _Optional[str]=...) -> None:
        ...

class Frames(_message.Message):
    __slots__ = ('frames_data',)
    FRAMES_DATA_FIELD_NUMBER: _ClassVar[int]
    frames_data: _containers.RepeatedCompositeFieldContainer[AssetFrame]

    def __init__(self, frames_data: _Optional[_Iterable[_Union[AssetFrame, _Mapping]]]=...) -> None:
        ...

class AssetFrame(_message.Message):
    __slots__ = ('machine_details', 'report_time', 'labels', 'attributes', 'performance_samples', 'trace_token')

    class LabelsEntry(_message.Message):
        __slots__ = ('key', 'value')
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: str

        def __init__(self, key: _Optional[str]=..., value: _Optional[str]=...) -> None:
            ...

    class AttributesEntry(_message.Message):
        __slots__ = ('key', 'value')
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: str

        def __init__(self, key: _Optional[str]=..., value: _Optional[str]=...) -> None:
            ...
    MACHINE_DETAILS_FIELD_NUMBER: _ClassVar[int]
    REPORT_TIME_FIELD_NUMBER: _ClassVar[int]
    LABELS_FIELD_NUMBER: _ClassVar[int]
    ATTRIBUTES_FIELD_NUMBER: _ClassVar[int]
    PERFORMANCE_SAMPLES_FIELD_NUMBER: _ClassVar[int]
    TRACE_TOKEN_FIELD_NUMBER: _ClassVar[int]
    machine_details: MachineDetails
    report_time: _timestamp_pb2.Timestamp
    labels: _containers.ScalarMap[str, str]
    attributes: _containers.ScalarMap[str, str]
    performance_samples: _containers.RepeatedCompositeFieldContainer[PerformanceSample]
    trace_token: str

    def __init__(self, machine_details: _Optional[_Union[MachineDetails, _Mapping]]=..., report_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]]=..., labels: _Optional[_Mapping[str, str]]=..., attributes: _Optional[_Mapping[str, str]]=..., performance_samples: _Optional[_Iterable[_Union[PerformanceSample, _Mapping]]]=..., trace_token: _Optional[str]=...) -> None:
        ...

class MachineDetails(_message.Message):
    __slots__ = ('uuid', 'machine_name', 'create_time', 'core_count', 'memory_mb', 'power_state', 'architecture', 'guest_os', 'network', 'disks', 'platform')

    class PowerState(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        POWER_STATE_UNSPECIFIED: _ClassVar[MachineDetails.PowerState]
        PENDING: _ClassVar[MachineDetails.PowerState]
        ACTIVE: _ClassVar[MachineDetails.PowerState]
        SUSPENDING: _ClassVar[MachineDetails.PowerState]
        SUSPENDED: _ClassVar[MachineDetails.PowerState]
        DELETING: _ClassVar[MachineDetails.PowerState]
        DELETED: _ClassVar[MachineDetails.PowerState]
    POWER_STATE_UNSPECIFIED: MachineDetails.PowerState
    PENDING: MachineDetails.PowerState
    ACTIVE: MachineDetails.PowerState
    SUSPENDING: MachineDetails.PowerState
    SUSPENDED: MachineDetails.PowerState
    DELETING: MachineDetails.PowerState
    DELETED: MachineDetails.PowerState
    UUID_FIELD_NUMBER: _ClassVar[int]
    MACHINE_NAME_FIELD_NUMBER: _ClassVar[int]
    CREATE_TIME_FIELD_NUMBER: _ClassVar[int]
    CORE_COUNT_FIELD_NUMBER: _ClassVar[int]
    MEMORY_MB_FIELD_NUMBER: _ClassVar[int]
    POWER_STATE_FIELD_NUMBER: _ClassVar[int]
    ARCHITECTURE_FIELD_NUMBER: _ClassVar[int]
    GUEST_OS_FIELD_NUMBER: _ClassVar[int]
    NETWORK_FIELD_NUMBER: _ClassVar[int]
    DISKS_FIELD_NUMBER: _ClassVar[int]
    PLATFORM_FIELD_NUMBER: _ClassVar[int]
    uuid: str
    machine_name: str
    create_time: _timestamp_pb2.Timestamp
    core_count: int
    memory_mb: int
    power_state: MachineDetails.PowerState
    architecture: MachineArchitectureDetails
    guest_os: GuestOsDetails
    network: MachineNetworkDetails
    disks: MachineDiskDetails
    platform: PlatformDetails

    def __init__(self, uuid: _Optional[str]=..., machine_name: _Optional[str]=..., create_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]]=..., core_count: _Optional[int]=..., memory_mb: _Optional[int]=..., power_state: _Optional[_Union[MachineDetails.PowerState, str]]=..., architecture: _Optional[_Union[MachineArchitectureDetails, _Mapping]]=..., guest_os: _Optional[_Union[GuestOsDetails, _Mapping]]=..., network: _Optional[_Union[MachineNetworkDetails, _Mapping]]=..., disks: _Optional[_Union[MachineDiskDetails, _Mapping]]=..., platform: _Optional[_Union[PlatformDetails, _Mapping]]=...) -> None:
        ...

class MachineArchitectureDetails(_message.Message):
    __slots__ = ('cpu_architecture', 'cpu_name', 'vendor', 'cpu_thread_count', 'cpu_socket_count', 'bios', 'firmware_type', 'hyperthreading')

    class FirmwareType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        FIRMWARE_TYPE_UNSPECIFIED: _ClassVar[MachineArchitectureDetails.FirmwareType]
        BIOS: _ClassVar[MachineArchitectureDetails.FirmwareType]
        EFI: _ClassVar[MachineArchitectureDetails.FirmwareType]
    FIRMWARE_TYPE_UNSPECIFIED: MachineArchitectureDetails.FirmwareType
    BIOS: MachineArchitectureDetails.FirmwareType
    EFI: MachineArchitectureDetails.FirmwareType

    class CpuHyperThreading(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        CPU_HYPER_THREADING_UNSPECIFIED: _ClassVar[MachineArchitectureDetails.CpuHyperThreading]
        DISABLED: _ClassVar[MachineArchitectureDetails.CpuHyperThreading]
        ENABLED: _ClassVar[MachineArchitectureDetails.CpuHyperThreading]
    CPU_HYPER_THREADING_UNSPECIFIED: MachineArchitectureDetails.CpuHyperThreading
    DISABLED: MachineArchitectureDetails.CpuHyperThreading
    ENABLED: MachineArchitectureDetails.CpuHyperThreading
    CPU_ARCHITECTURE_FIELD_NUMBER: _ClassVar[int]
    CPU_NAME_FIELD_NUMBER: _ClassVar[int]
    VENDOR_FIELD_NUMBER: _ClassVar[int]
    CPU_THREAD_COUNT_FIELD_NUMBER: _ClassVar[int]
    CPU_SOCKET_COUNT_FIELD_NUMBER: _ClassVar[int]
    BIOS_FIELD_NUMBER: _ClassVar[int]
    FIRMWARE_TYPE_FIELD_NUMBER: _ClassVar[int]
    HYPERTHREADING_FIELD_NUMBER: _ClassVar[int]
    cpu_architecture: str
    cpu_name: str
    vendor: str
    cpu_thread_count: int
    cpu_socket_count: int
    bios: BiosDetails
    firmware_type: MachineArchitectureDetails.FirmwareType
    hyperthreading: MachineArchitectureDetails.CpuHyperThreading

    def __init__(self, cpu_architecture: _Optional[str]=..., cpu_name: _Optional[str]=..., vendor: _Optional[str]=..., cpu_thread_count: _Optional[int]=..., cpu_socket_count: _Optional[int]=..., bios: _Optional[_Union[BiosDetails, _Mapping]]=..., firmware_type: _Optional[_Union[MachineArchitectureDetails.FirmwareType, str]]=..., hyperthreading: _Optional[_Union[MachineArchitectureDetails.CpuHyperThreading, str]]=...) -> None:
        ...

class BiosDetails(_message.Message):
    __slots__ = ('bios_name', 'id', 'manufacturer', 'version', 'release_date', 'smbios_uuid')
    BIOS_NAME_FIELD_NUMBER: _ClassVar[int]
    ID_FIELD_NUMBER: _ClassVar[int]
    MANUFACTURER_FIELD_NUMBER: _ClassVar[int]
    VERSION_FIELD_NUMBER: _ClassVar[int]
    RELEASE_DATE_FIELD_NUMBER: _ClassVar[int]
    SMBIOS_UUID_FIELD_NUMBER: _ClassVar[int]
    bios_name: str
    id: str
    manufacturer: str
    version: str
    release_date: _date_pb2.Date
    smbios_uuid: str

    def __init__(self, bios_name: _Optional[str]=..., id: _Optional[str]=..., manufacturer: _Optional[str]=..., version: _Optional[str]=..., release_date: _Optional[_Union[_date_pb2.Date, _Mapping]]=..., smbios_uuid: _Optional[str]=...) -> None:
        ...

class MachineNetworkDetails(_message.Message):
    __slots__ = ('primary_ip_address', 'public_ip_address', 'primary_mac_address', 'adapters')
    PRIMARY_IP_ADDRESS_FIELD_NUMBER: _ClassVar[int]
    PUBLIC_IP_ADDRESS_FIELD_NUMBER: _ClassVar[int]
    PRIMARY_MAC_ADDRESS_FIELD_NUMBER: _ClassVar[int]
    ADAPTERS_FIELD_NUMBER: _ClassVar[int]
    primary_ip_address: str
    public_ip_address: str
    primary_mac_address: str
    adapters: NetworkAdapterList

    def __init__(self, primary_ip_address: _Optional[str]=..., public_ip_address: _Optional[str]=..., primary_mac_address: _Optional[str]=..., adapters: _Optional[_Union[NetworkAdapterList, _Mapping]]=...) -> None:
        ...

class NetworkAdapterList(_message.Message):
    __slots__ = ('entries',)
    ENTRIES_FIELD_NUMBER: _ClassVar[int]
    entries: _containers.RepeatedCompositeFieldContainer[NetworkAdapterDetails]

    def __init__(self, entries: _Optional[_Iterable[_Union[NetworkAdapterDetails, _Mapping]]]=...) -> None:
        ...

class NetworkAdapterDetails(_message.Message):
    __slots__ = ('adapter_type', 'mac_address', 'addresses')
    ADAPTER_TYPE_FIELD_NUMBER: _ClassVar[int]
    MAC_ADDRESS_FIELD_NUMBER: _ClassVar[int]
    ADDRESSES_FIELD_NUMBER: _ClassVar[int]
    adapter_type: str
    mac_address: str
    addresses: NetworkAddressList

    def __init__(self, adapter_type: _Optional[str]=..., mac_address: _Optional[str]=..., addresses: _Optional[_Union[NetworkAddressList, _Mapping]]=...) -> None:
        ...

class NetworkAddressList(_message.Message):
    __slots__ = ('entries',)
    ENTRIES_FIELD_NUMBER: _ClassVar[int]
    entries: _containers.RepeatedCompositeFieldContainer[NetworkAddress]

    def __init__(self, entries: _Optional[_Iterable[_Union[NetworkAddress, _Mapping]]]=...) -> None:
        ...

class NetworkAddress(_message.Message):
    __slots__ = ('ip_address', 'subnet_mask', 'bcast', 'fqdn', 'assignment')

    class AddressAssignment(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        ADDRESS_ASSIGNMENT_UNSPECIFIED: _ClassVar[NetworkAddress.AddressAssignment]
        ADDRESS_ASSIGNMENT_STATIC: _ClassVar[NetworkAddress.AddressAssignment]
        ADDRESS_ASSIGNMENT_DHCP: _ClassVar[NetworkAddress.AddressAssignment]
    ADDRESS_ASSIGNMENT_UNSPECIFIED: NetworkAddress.AddressAssignment
    ADDRESS_ASSIGNMENT_STATIC: NetworkAddress.AddressAssignment
    ADDRESS_ASSIGNMENT_DHCP: NetworkAddress.AddressAssignment
    IP_ADDRESS_FIELD_NUMBER: _ClassVar[int]
    SUBNET_MASK_FIELD_NUMBER: _ClassVar[int]
    BCAST_FIELD_NUMBER: _ClassVar[int]
    FQDN_FIELD_NUMBER: _ClassVar[int]
    ASSIGNMENT_FIELD_NUMBER: _ClassVar[int]
    ip_address: str
    subnet_mask: str
    bcast: str
    fqdn: str
    assignment: NetworkAddress.AddressAssignment

    def __init__(self, ip_address: _Optional[str]=..., subnet_mask: _Optional[str]=..., bcast: _Optional[str]=..., fqdn: _Optional[str]=..., assignment: _Optional[_Union[NetworkAddress.AddressAssignment, str]]=...) -> None:
        ...

class MachineDiskDetails(_message.Message):
    __slots__ = ('total_capacity_bytes', 'total_free_bytes', 'disks')
    TOTAL_CAPACITY_BYTES_FIELD_NUMBER: _ClassVar[int]
    TOTAL_FREE_BYTES_FIELD_NUMBER: _ClassVar[int]
    DISKS_FIELD_NUMBER: _ClassVar[int]
    total_capacity_bytes: int
    total_free_bytes: int
    disks: DiskEntryList

    def __init__(self, total_capacity_bytes: _Optional[int]=..., total_free_bytes: _Optional[int]=..., disks: _Optional[_Union[DiskEntryList, _Mapping]]=...) -> None:
        ...

class DiskEntryList(_message.Message):
    __slots__ = ('entries',)
    ENTRIES_FIELD_NUMBER: _ClassVar[int]
    entries: _containers.RepeatedCompositeFieldContainer[DiskEntry]

    def __init__(self, entries: _Optional[_Iterable[_Union[DiskEntry, _Mapping]]]=...) -> None:
        ...

class DiskEntry(_message.Message):
    __slots__ = ('capacity_bytes', 'free_bytes', 'disk_label', 'disk_label_type', 'interface_type', 'partitions', 'hw_address', 'vmware')

    class InterfaceType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        INTERFACE_TYPE_UNSPECIFIED: _ClassVar[DiskEntry.InterfaceType]
        IDE: _ClassVar[DiskEntry.InterfaceType]
        SATA: _ClassVar[DiskEntry.InterfaceType]
        SAS: _ClassVar[DiskEntry.InterfaceType]
        SCSI: _ClassVar[DiskEntry.InterfaceType]
        NVME: _ClassVar[DiskEntry.InterfaceType]
        FC: _ClassVar[DiskEntry.InterfaceType]
        ISCSI: _ClassVar[DiskEntry.InterfaceType]
    INTERFACE_TYPE_UNSPECIFIED: DiskEntry.InterfaceType
    IDE: DiskEntry.InterfaceType
    SATA: DiskEntry.InterfaceType
    SAS: DiskEntry.InterfaceType
    SCSI: DiskEntry.InterfaceType
    NVME: DiskEntry.InterfaceType
    FC: DiskEntry.InterfaceType
    ISCSI: DiskEntry.InterfaceType
    CAPACITY_BYTES_FIELD_NUMBER: _ClassVar[int]
    FREE_BYTES_FIELD_NUMBER: _ClassVar[int]
    DISK_LABEL_FIELD_NUMBER: _ClassVar[int]
    DISK_LABEL_TYPE_FIELD_NUMBER: _ClassVar[int]
    INTERFACE_TYPE_FIELD_NUMBER: _ClassVar[int]
    PARTITIONS_FIELD_NUMBER: _ClassVar[int]
    HW_ADDRESS_FIELD_NUMBER: _ClassVar[int]
    VMWARE_FIELD_NUMBER: _ClassVar[int]
    capacity_bytes: int
    free_bytes: int
    disk_label: str
    disk_label_type: str
    interface_type: DiskEntry.InterfaceType
    partitions: DiskPartitionList
    hw_address: str
    vmware: VmwareDiskConfig

    def __init__(self, capacity_bytes: _Optional[int]=..., free_bytes: _Optional[int]=..., disk_label: _Optional[str]=..., disk_label_type: _Optional[str]=..., interface_type: _Optional[_Union[DiskEntry.InterfaceType, str]]=..., partitions: _Optional[_Union[DiskPartitionList, _Mapping]]=..., hw_address: _Optional[str]=..., vmware: _Optional[_Union[VmwareDiskConfig, _Mapping]]=...) -> None:
        ...

class DiskPartitionList(_message.Message):
    __slots__ = ('entries',)
    ENTRIES_FIELD_NUMBER: _ClassVar[int]
    entries: _containers.RepeatedCompositeFieldContainer[DiskPartition]

    def __init__(self, entries: _Optional[_Iterable[_Union[DiskPartition, _Mapping]]]=...) -> None:
        ...

class DiskPartition(_message.Message):
    __slots__ = ('type', 'file_system', 'mount_point', 'capacity_bytes', 'free_bytes', 'uuid', 'sub_partitions')
    TYPE_FIELD_NUMBER: _ClassVar[int]
    FILE_SYSTEM_FIELD_NUMBER: _ClassVar[int]
    MOUNT_POINT_FIELD_NUMBER: _ClassVar[int]
    CAPACITY_BYTES_FIELD_NUMBER: _ClassVar[int]
    FREE_BYTES_FIELD_NUMBER: _ClassVar[int]
    UUID_FIELD_NUMBER: _ClassVar[int]
    SUB_PARTITIONS_FIELD_NUMBER: _ClassVar[int]
    type: str
    file_system: str
    mount_point: str
    capacity_bytes: int
    free_bytes: int
    uuid: str
    sub_partitions: DiskPartitionList

    def __init__(self, type: _Optional[str]=..., file_system: _Optional[str]=..., mount_point: _Optional[str]=..., capacity_bytes: _Optional[int]=..., free_bytes: _Optional[int]=..., uuid: _Optional[str]=..., sub_partitions: _Optional[_Union[DiskPartitionList, _Mapping]]=...) -> None:
        ...

class VmwareDiskConfig(_message.Message):
    __slots__ = ('backing_type', 'shared', 'vmdk_mode', 'rdm_compatibility')

    class BackingType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        BACKING_TYPE_UNSPECIFIED: _ClassVar[VmwareDiskConfig.BackingType]
        BACKING_TYPE_FLAT_V1: _ClassVar[VmwareDiskConfig.BackingType]
        BACKING_TYPE_FLAT_V2: _ClassVar[VmwareDiskConfig.BackingType]
        BACKING_TYPE_PMEM: _ClassVar[VmwareDiskConfig.BackingType]
        BACKING_TYPE_RDM_V1: _ClassVar[VmwareDiskConfig.BackingType]
        BACKING_TYPE_RDM_V2: _ClassVar[VmwareDiskConfig.BackingType]
        BACKING_TYPE_SESPARSE: _ClassVar[VmwareDiskConfig.BackingType]
        BACKING_TYPE_SESPARSE_V1: _ClassVar[VmwareDiskConfig.BackingType]
        BACKING_TYPE_SESPARSE_V2: _ClassVar[VmwareDiskConfig.BackingType]
    BACKING_TYPE_UNSPECIFIED: VmwareDiskConfig.BackingType
    BACKING_TYPE_FLAT_V1: VmwareDiskConfig.BackingType
    BACKING_TYPE_FLAT_V2: VmwareDiskConfig.BackingType
    BACKING_TYPE_PMEM: VmwareDiskConfig.BackingType
    BACKING_TYPE_RDM_V1: VmwareDiskConfig.BackingType
    BACKING_TYPE_RDM_V2: VmwareDiskConfig.BackingType
    BACKING_TYPE_SESPARSE: VmwareDiskConfig.BackingType
    BACKING_TYPE_SESPARSE_V1: VmwareDiskConfig.BackingType
    BACKING_TYPE_SESPARSE_V2: VmwareDiskConfig.BackingType

    class VmdkMode(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        VMDK_MODE_UNSPECIFIED: _ClassVar[VmwareDiskConfig.VmdkMode]
        DEPENDENT: _ClassVar[VmwareDiskConfig.VmdkMode]
        INDEPENDENT_PERSISTENT: _ClassVar[VmwareDiskConfig.VmdkMode]
        INDEPENDENT_NONPERSISTENT: _ClassVar[VmwareDiskConfig.VmdkMode]
    VMDK_MODE_UNSPECIFIED: VmwareDiskConfig.VmdkMode
    DEPENDENT: VmwareDiskConfig.VmdkMode
    INDEPENDENT_PERSISTENT: VmwareDiskConfig.VmdkMode
    INDEPENDENT_NONPERSISTENT: VmwareDiskConfig.VmdkMode

    class RdmCompatibility(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        RDM_COMPATIBILITY_UNSPECIFIED: _ClassVar[VmwareDiskConfig.RdmCompatibility]
        PHYSICAL_COMPATIBILITY: _ClassVar[VmwareDiskConfig.RdmCompatibility]
        VIRTUAL_COMPATIBILITY: _ClassVar[VmwareDiskConfig.RdmCompatibility]
    RDM_COMPATIBILITY_UNSPECIFIED: VmwareDiskConfig.RdmCompatibility
    PHYSICAL_COMPATIBILITY: VmwareDiskConfig.RdmCompatibility
    VIRTUAL_COMPATIBILITY: VmwareDiskConfig.RdmCompatibility
    BACKING_TYPE_FIELD_NUMBER: _ClassVar[int]
    SHARED_FIELD_NUMBER: _ClassVar[int]
    VMDK_MODE_FIELD_NUMBER: _ClassVar[int]
    RDM_COMPATIBILITY_FIELD_NUMBER: _ClassVar[int]
    backing_type: VmwareDiskConfig.BackingType
    shared: bool
    vmdk_mode: VmwareDiskConfig.VmdkMode
    rdm_compatibility: VmwareDiskConfig.RdmCompatibility

    def __init__(self, backing_type: _Optional[_Union[VmwareDiskConfig.BackingType, str]]=..., shared: bool=..., vmdk_mode: _Optional[_Union[VmwareDiskConfig.VmdkMode, str]]=..., rdm_compatibility: _Optional[_Union[VmwareDiskConfig.RdmCompatibility, str]]=...) -> None:
        ...

class GuestOsDetails(_message.Message):
    __slots__ = ('os_name', 'family', 'version', 'config', 'runtime')
    OS_NAME_FIELD_NUMBER: _ClassVar[int]
    FAMILY_FIELD_NUMBER: _ClassVar[int]
    VERSION_FIELD_NUMBER: _ClassVar[int]
    CONFIG_FIELD_NUMBER: _ClassVar[int]
    RUNTIME_FIELD_NUMBER: _ClassVar[int]
    os_name: str
    family: OperatingSystemFamily
    version: str
    config: GuestConfigDetails
    runtime: GuestRuntimeDetails

    def __init__(self, os_name: _Optional[str]=..., family: _Optional[_Union[OperatingSystemFamily, str]]=..., version: _Optional[str]=..., config: _Optional[_Union[GuestConfigDetails, _Mapping]]=..., runtime: _Optional[_Union[GuestRuntimeDetails, _Mapping]]=...) -> None:
        ...

class GuestConfigDetails(_message.Message):
    __slots__ = ('issue', 'fstab', 'hosts', 'nfs_exports', 'selinux_mode')

    class SeLinuxMode(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        SE_LINUX_MODE_UNSPECIFIED: _ClassVar[GuestConfigDetails.SeLinuxMode]
        SE_LINUX_MODE_DISABLED: _ClassVar[GuestConfigDetails.SeLinuxMode]
        SE_LINUX_MODE_PERMISSIVE: _ClassVar[GuestConfigDetails.SeLinuxMode]
        SE_LINUX_MODE_ENFORCING: _ClassVar[GuestConfigDetails.SeLinuxMode]
    SE_LINUX_MODE_UNSPECIFIED: GuestConfigDetails.SeLinuxMode
    SE_LINUX_MODE_DISABLED: GuestConfigDetails.SeLinuxMode
    SE_LINUX_MODE_PERMISSIVE: GuestConfigDetails.SeLinuxMode
    SE_LINUX_MODE_ENFORCING: GuestConfigDetails.SeLinuxMode
    ISSUE_FIELD_NUMBER: _ClassVar[int]
    FSTAB_FIELD_NUMBER: _ClassVar[int]
    HOSTS_FIELD_NUMBER: _ClassVar[int]
    NFS_EXPORTS_FIELD_NUMBER: _ClassVar[int]
    SELINUX_MODE_FIELD_NUMBER: _ClassVar[int]
    issue: str
    fstab: FstabEntryList
    hosts: HostsEntryList
    nfs_exports: NfsExportList
    selinux_mode: GuestConfigDetails.SeLinuxMode

    def __init__(self, issue: _Optional[str]=..., fstab: _Optional[_Union[FstabEntryList, _Mapping]]=..., hosts: _Optional[_Union[HostsEntryList, _Mapping]]=..., nfs_exports: _Optional[_Union[NfsExportList, _Mapping]]=..., selinux_mode: _Optional[_Union[GuestConfigDetails.SeLinuxMode, str]]=...) -> None:
        ...

class FstabEntryList(_message.Message):
    __slots__ = ('entries',)
    ENTRIES_FIELD_NUMBER: _ClassVar[int]
    entries: _containers.RepeatedCompositeFieldContainer[FstabEntry]

    def __init__(self, entries: _Optional[_Iterable[_Union[FstabEntry, _Mapping]]]=...) -> None:
        ...

class FstabEntry(_message.Message):
    __slots__ = ('spec', 'file', 'vfstype', 'mntops', 'freq', 'passno')
    SPEC_FIELD_NUMBER: _ClassVar[int]
    FILE_FIELD_NUMBER: _ClassVar[int]
    VFSTYPE_FIELD_NUMBER: _ClassVar[int]
    MNTOPS_FIELD_NUMBER: _ClassVar[int]
    FREQ_FIELD_NUMBER: _ClassVar[int]
    PASSNO_FIELD_NUMBER: _ClassVar[int]
    spec: str
    file: str
    vfstype: str
    mntops: str
    freq: int
    passno: int

    def __init__(self, spec: _Optional[str]=..., file: _Optional[str]=..., vfstype: _Optional[str]=..., mntops: _Optional[str]=..., freq: _Optional[int]=..., passno: _Optional[int]=...) -> None:
        ...

class HostsEntryList(_message.Message):
    __slots__ = ('entries',)
    ENTRIES_FIELD_NUMBER: _ClassVar[int]
    entries: _containers.RepeatedCompositeFieldContainer[HostsEntry]

    def __init__(self, entries: _Optional[_Iterable[_Union[HostsEntry, _Mapping]]]=...) -> None:
        ...

class HostsEntry(_message.Message):
    __slots__ = ('ip', 'host_names')
    IP_FIELD_NUMBER: _ClassVar[int]
    HOST_NAMES_FIELD_NUMBER: _ClassVar[int]
    ip: str
    host_names: _containers.RepeatedScalarFieldContainer[str]

    def __init__(self, ip: _Optional[str]=..., host_names: _Optional[_Iterable[str]]=...) -> None:
        ...

class NfsExportList(_message.Message):
    __slots__ = ('entries',)
    ENTRIES_FIELD_NUMBER: _ClassVar[int]
    entries: _containers.RepeatedCompositeFieldContainer[NfsExport]

    def __init__(self, entries: _Optional[_Iterable[_Union[NfsExport, _Mapping]]]=...) -> None:
        ...

class NfsExport(_message.Message):
    __slots__ = ('export_directory', 'hosts')
    EXPORT_DIRECTORY_FIELD_NUMBER: _ClassVar[int]
    HOSTS_FIELD_NUMBER: _ClassVar[int]
    export_directory: str
    hosts: _containers.RepeatedScalarFieldContainer[str]

    def __init__(self, export_directory: _Optional[str]=..., hosts: _Optional[_Iterable[str]]=...) -> None:
        ...

class GuestRuntimeDetails(_message.Message):
    __slots__ = ('services', 'processes', 'network', 'last_boot_time', 'domain', 'machine_name', 'installed_apps', 'open_file_list')
    SERVICES_FIELD_NUMBER: _ClassVar[int]
    PROCESSES_FIELD_NUMBER: _ClassVar[int]
    NETWORK_FIELD_NUMBER: _ClassVar[int]
    LAST_BOOT_TIME_FIELD_NUMBER: _ClassVar[int]
    DOMAIN_FIELD_NUMBER: _ClassVar[int]
    MACHINE_NAME_FIELD_NUMBER: _ClassVar[int]
    INSTALLED_APPS_FIELD_NUMBER: _ClassVar[int]
    OPEN_FILE_LIST_FIELD_NUMBER: _ClassVar[int]
    services: RunningServiceList
    processes: RunningProcessList
    network: RuntimeNetworkInfo
    last_boot_time: _timestamp_pb2.Timestamp
    domain: str
    machine_name: str
    installed_apps: GuestInstalledApplicationList
    open_file_list: OpenFileList

    def __init__(self, services: _Optional[_Union[RunningServiceList, _Mapping]]=..., processes: _Optional[_Union[RunningProcessList, _Mapping]]=..., network: _Optional[_Union[RuntimeNetworkInfo, _Mapping]]=..., last_boot_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]]=..., domain: _Optional[str]=..., machine_name: _Optional[str]=..., installed_apps: _Optional[_Union[GuestInstalledApplicationList, _Mapping]]=..., open_file_list: _Optional[_Union[OpenFileList, _Mapping]]=...) -> None:
        ...

class RunningServiceList(_message.Message):
    __slots__ = ('entries',)
    ENTRIES_FIELD_NUMBER: _ClassVar[int]
    entries: _containers.RepeatedCompositeFieldContainer[RunningService]

    def __init__(self, entries: _Optional[_Iterable[_Union[RunningService, _Mapping]]]=...) -> None:
        ...

class RunningService(_message.Message):
    __slots__ = ('service_name', 'state', 'start_mode', 'exe_path', 'cmdline', 'pid')

    class State(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        STATE_UNSPECIFIED: _ClassVar[RunningService.State]
        ACTIVE: _ClassVar[RunningService.State]
        PAUSED: _ClassVar[RunningService.State]
        STOPPED: _ClassVar[RunningService.State]
    STATE_UNSPECIFIED: RunningService.State
    ACTIVE: RunningService.State
    PAUSED: RunningService.State
    STOPPED: RunningService.State

    class StartMode(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        START_MODE_UNSPECIFIED: _ClassVar[RunningService.StartMode]
        BOOT: _ClassVar[RunningService.StartMode]
        SYSTEM: _ClassVar[RunningService.StartMode]
        AUTO: _ClassVar[RunningService.StartMode]
        MANUAL: _ClassVar[RunningService.StartMode]
        DISABLED: _ClassVar[RunningService.StartMode]
    START_MODE_UNSPECIFIED: RunningService.StartMode
    BOOT: RunningService.StartMode
    SYSTEM: RunningService.StartMode
    AUTO: RunningService.StartMode
    MANUAL: RunningService.StartMode
    DISABLED: RunningService.StartMode
    SERVICE_NAME_FIELD_NUMBER: _ClassVar[int]
    STATE_FIELD_NUMBER: _ClassVar[int]
    START_MODE_FIELD_NUMBER: _ClassVar[int]
    EXE_PATH_FIELD_NUMBER: _ClassVar[int]
    CMDLINE_FIELD_NUMBER: _ClassVar[int]
    PID_FIELD_NUMBER: _ClassVar[int]
    service_name: str
    state: RunningService.State
    start_mode: RunningService.StartMode
    exe_path: str
    cmdline: str
    pid: int

    def __init__(self, service_name: _Optional[str]=..., state: _Optional[_Union[RunningService.State, str]]=..., start_mode: _Optional[_Union[RunningService.StartMode, str]]=..., exe_path: _Optional[str]=..., cmdline: _Optional[str]=..., pid: _Optional[int]=...) -> None:
        ...

class RunningProcessList(_message.Message):
    __slots__ = ('entries',)
    ENTRIES_FIELD_NUMBER: _ClassVar[int]
    entries: _containers.RepeatedCompositeFieldContainer[RunningProcess]

    def __init__(self, entries: _Optional[_Iterable[_Union[RunningProcess, _Mapping]]]=...) -> None:
        ...

class RunningProcess(_message.Message):
    __slots__ = ('pid', 'exe_path', 'cmdline', 'user', 'attributes')

    class AttributesEntry(_message.Message):
        __slots__ = ('key', 'value')
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: str

        def __init__(self, key: _Optional[str]=..., value: _Optional[str]=...) -> None:
            ...
    PID_FIELD_NUMBER: _ClassVar[int]
    EXE_PATH_FIELD_NUMBER: _ClassVar[int]
    CMDLINE_FIELD_NUMBER: _ClassVar[int]
    USER_FIELD_NUMBER: _ClassVar[int]
    ATTRIBUTES_FIELD_NUMBER: _ClassVar[int]
    pid: int
    exe_path: str
    cmdline: str
    user: str
    attributes: _containers.ScalarMap[str, str]

    def __init__(self, pid: _Optional[int]=..., exe_path: _Optional[str]=..., cmdline: _Optional[str]=..., user: _Optional[str]=..., attributes: _Optional[_Mapping[str, str]]=...) -> None:
        ...

class RuntimeNetworkInfo(_message.Message):
    __slots__ = ('scan_time', 'connections')
    SCAN_TIME_FIELD_NUMBER: _ClassVar[int]
    CONNECTIONS_FIELD_NUMBER: _ClassVar[int]
    scan_time: _timestamp_pb2.Timestamp
    connections: NetworkConnectionList

    def __init__(self, scan_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]]=..., connections: _Optional[_Union[NetworkConnectionList, _Mapping]]=...) -> None:
        ...

class NetworkConnectionList(_message.Message):
    __slots__ = ('entries',)
    ENTRIES_FIELD_NUMBER: _ClassVar[int]
    entries: _containers.RepeatedCompositeFieldContainer[NetworkConnection]

    def __init__(self, entries: _Optional[_Iterable[_Union[NetworkConnection, _Mapping]]]=...) -> None:
        ...

class NetworkConnection(_message.Message):
    __slots__ = ('protocol', 'local_ip_address', 'local_port', 'remote_ip_address', 'remote_port', 'state', 'pid', 'process_name')

    class State(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        STATE_UNSPECIFIED: _ClassVar[NetworkConnection.State]
        OPENING: _ClassVar[NetworkConnection.State]
        OPEN: _ClassVar[NetworkConnection.State]
        LISTEN: _ClassVar[NetworkConnection.State]
        CLOSING: _ClassVar[NetworkConnection.State]
        CLOSED: _ClassVar[NetworkConnection.State]
    STATE_UNSPECIFIED: NetworkConnection.State
    OPENING: NetworkConnection.State
    OPEN: NetworkConnection.State
    LISTEN: NetworkConnection.State
    CLOSING: NetworkConnection.State
    CLOSED: NetworkConnection.State
    PROTOCOL_FIELD_NUMBER: _ClassVar[int]
    LOCAL_IP_ADDRESS_FIELD_NUMBER: _ClassVar[int]
    LOCAL_PORT_FIELD_NUMBER: _ClassVar[int]
    REMOTE_IP_ADDRESS_FIELD_NUMBER: _ClassVar[int]
    REMOTE_PORT_FIELD_NUMBER: _ClassVar[int]
    STATE_FIELD_NUMBER: _ClassVar[int]
    PID_FIELD_NUMBER: _ClassVar[int]
    PROCESS_NAME_FIELD_NUMBER: _ClassVar[int]
    protocol: str
    local_ip_address: str
    local_port: int
    remote_ip_address: str
    remote_port: int
    state: NetworkConnection.State
    pid: int
    process_name: str

    def __init__(self, protocol: _Optional[str]=..., local_ip_address: _Optional[str]=..., local_port: _Optional[int]=..., remote_ip_address: _Optional[str]=..., remote_port: _Optional[int]=..., state: _Optional[_Union[NetworkConnection.State, str]]=..., pid: _Optional[int]=..., process_name: _Optional[str]=...) -> None:
        ...

class GuestInstalledApplicationList(_message.Message):
    __slots__ = ('entries',)
    ENTRIES_FIELD_NUMBER: _ClassVar[int]
    entries: _containers.RepeatedCompositeFieldContainer[GuestInstalledApplication]

    def __init__(self, entries: _Optional[_Iterable[_Union[GuestInstalledApplication, _Mapping]]]=...) -> None:
        ...

class GuestInstalledApplication(_message.Message):
    __slots__ = ('application_name', 'vendor', 'install_time', 'path', 'version')
    APPLICATION_NAME_FIELD_NUMBER: _ClassVar[int]
    VENDOR_FIELD_NUMBER: _ClassVar[int]
    INSTALL_TIME_FIELD_NUMBER: _ClassVar[int]
    PATH_FIELD_NUMBER: _ClassVar[int]
    VERSION_FIELD_NUMBER: _ClassVar[int]
    application_name: str
    vendor: str
    install_time: _timestamp_pb2.Timestamp
    path: str
    version: str

    def __init__(self, application_name: _Optional[str]=..., vendor: _Optional[str]=..., install_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]]=..., path: _Optional[str]=..., version: _Optional[str]=...) -> None:
        ...

class OpenFileList(_message.Message):
    __slots__ = ('entries',)
    ENTRIES_FIELD_NUMBER: _ClassVar[int]
    entries: _containers.RepeatedCompositeFieldContainer[OpenFileDetails]

    def __init__(self, entries: _Optional[_Iterable[_Union[OpenFileDetails, _Mapping]]]=...) -> None:
        ...

class OpenFileDetails(_message.Message):
    __slots__ = ('command', 'user', 'file_type', 'file_path')
    COMMAND_FIELD_NUMBER: _ClassVar[int]
    USER_FIELD_NUMBER: _ClassVar[int]
    FILE_TYPE_FIELD_NUMBER: _ClassVar[int]
    FILE_PATH_FIELD_NUMBER: _ClassVar[int]
    command: str
    user: str
    file_type: str
    file_path: str

    def __init__(self, command: _Optional[str]=..., user: _Optional[str]=..., file_type: _Optional[str]=..., file_path: _Optional[str]=...) -> None:
        ...

class PlatformDetails(_message.Message):
    __slots__ = ('vmware_details', 'aws_ec2_details', 'azure_vm_details', 'generic_details', 'physical_details')
    VMWARE_DETAILS_FIELD_NUMBER: _ClassVar[int]
    AWS_EC2_DETAILS_FIELD_NUMBER: _ClassVar[int]
    AZURE_VM_DETAILS_FIELD_NUMBER: _ClassVar[int]
    GENERIC_DETAILS_FIELD_NUMBER: _ClassVar[int]
    PHYSICAL_DETAILS_FIELD_NUMBER: _ClassVar[int]
    vmware_details: VmwarePlatformDetails
    aws_ec2_details: AwsEc2PlatformDetails
    azure_vm_details: AzureVmPlatformDetails
    generic_details: GenericPlatformDetails
    physical_details: PhysicalPlatformDetails

    def __init__(self, vmware_details: _Optional[_Union[VmwarePlatformDetails, _Mapping]]=..., aws_ec2_details: _Optional[_Union[AwsEc2PlatformDetails, _Mapping]]=..., azure_vm_details: _Optional[_Union[AzureVmPlatformDetails, _Mapping]]=..., generic_details: _Optional[_Union[GenericPlatformDetails, _Mapping]]=..., physical_details: _Optional[_Union[PhysicalPlatformDetails, _Mapping]]=...) -> None:
        ...

class VmwarePlatformDetails(_message.Message):
    __slots__ = ('vcenter_version', 'esx_version', 'osid', 'vcenter_folder', 'vcenter_uri', 'vcenter_vm_id')
    VCENTER_VERSION_FIELD_NUMBER: _ClassVar[int]
    ESX_VERSION_FIELD_NUMBER: _ClassVar[int]
    OSID_FIELD_NUMBER: _ClassVar[int]
    VCENTER_FOLDER_FIELD_NUMBER: _ClassVar[int]
    VCENTER_URI_FIELD_NUMBER: _ClassVar[int]
    VCENTER_VM_ID_FIELD_NUMBER: _ClassVar[int]
    vcenter_version: str
    esx_version: str
    osid: str
    vcenter_folder: str
    vcenter_uri: str
    vcenter_vm_id: str

    def __init__(self, vcenter_version: _Optional[str]=..., esx_version: _Optional[str]=..., osid: _Optional[str]=..., vcenter_folder: _Optional[str]=..., vcenter_uri: _Optional[str]=..., vcenter_vm_id: _Optional[str]=...) -> None:
        ...

class AwsEc2PlatformDetails(_message.Message):
    __slots__ = ('machine_type_label', 'location')
    MACHINE_TYPE_LABEL_FIELD_NUMBER: _ClassVar[int]
    LOCATION_FIELD_NUMBER: _ClassVar[int]
    machine_type_label: str
    location: str

    def __init__(self, machine_type_label: _Optional[str]=..., location: _Optional[str]=...) -> None:
        ...

class AzureVmPlatformDetails(_message.Message):
    __slots__ = ('machine_type_label', 'location', 'provisioning_state')
    MACHINE_TYPE_LABEL_FIELD_NUMBER: _ClassVar[int]
    LOCATION_FIELD_NUMBER: _ClassVar[int]
    PROVISIONING_STATE_FIELD_NUMBER: _ClassVar[int]
    machine_type_label: str
    location: str
    provisioning_state: str

    def __init__(self, machine_type_label: _Optional[str]=..., location: _Optional[str]=..., provisioning_state: _Optional[str]=...) -> None:
        ...

class GenericPlatformDetails(_message.Message):
    __slots__ = ('location',)
    LOCATION_FIELD_NUMBER: _ClassVar[int]
    location: str

    def __init__(self, location: _Optional[str]=...) -> None:
        ...

class PhysicalPlatformDetails(_message.Message):
    __slots__ = ('location',)
    LOCATION_FIELD_NUMBER: _ClassVar[int]
    location: str

    def __init__(self, location: _Optional[str]=...) -> None:
        ...

class MemoryUsageSample(_message.Message):
    __slots__ = ('utilized_percentage',)
    UTILIZED_PERCENTAGE_FIELD_NUMBER: _ClassVar[int]
    utilized_percentage: float

    def __init__(self, utilized_percentage: _Optional[float]=...) -> None:
        ...

class CpuUsageSample(_message.Message):
    __slots__ = ('utilized_percentage',)
    UTILIZED_PERCENTAGE_FIELD_NUMBER: _ClassVar[int]
    utilized_percentage: float

    def __init__(self, utilized_percentage: _Optional[float]=...) -> None:
        ...

class NetworkUsageSample(_message.Message):
    __slots__ = ('average_ingress_bps', 'average_egress_bps')
    AVERAGE_INGRESS_BPS_FIELD_NUMBER: _ClassVar[int]
    AVERAGE_EGRESS_BPS_FIELD_NUMBER: _ClassVar[int]
    average_ingress_bps: float
    average_egress_bps: float

    def __init__(self, average_ingress_bps: _Optional[float]=..., average_egress_bps: _Optional[float]=...) -> None:
        ...

class DiskUsageSample(_message.Message):
    __slots__ = ('average_iops',)
    AVERAGE_IOPS_FIELD_NUMBER: _ClassVar[int]
    average_iops: float

    def __init__(self, average_iops: _Optional[float]=...) -> None:
        ...

class PerformanceSample(_message.Message):
    __slots__ = ('sample_time', 'memory', 'cpu', 'network', 'disk')
    SAMPLE_TIME_FIELD_NUMBER: _ClassVar[int]
    MEMORY_FIELD_NUMBER: _ClassVar[int]
    CPU_FIELD_NUMBER: _ClassVar[int]
    NETWORK_FIELD_NUMBER: _ClassVar[int]
    DISK_FIELD_NUMBER: _ClassVar[int]
    sample_time: _timestamp_pb2.Timestamp
    memory: MemoryUsageSample
    cpu: CpuUsageSample
    network: NetworkUsageSample
    disk: DiskUsageSample

    def __init__(self, sample_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]]=..., memory: _Optional[_Union[MemoryUsageSample, _Mapping]]=..., cpu: _Optional[_Union[CpuUsageSample, _Mapping]]=..., network: _Optional[_Union[NetworkUsageSample, _Mapping]]=..., disk: _Optional[_Union[DiskUsageSample, _Mapping]]=...) -> None:
        ...

class AssetPerformanceData(_message.Message):
    __slots__ = ('daily_resource_usage_aggregations',)
    DAILY_RESOURCE_USAGE_AGGREGATIONS_FIELD_NUMBER: _ClassVar[int]
    daily_resource_usage_aggregations: _containers.RepeatedCompositeFieldContainer[DailyResourceUsageAggregation]

    def __init__(self, daily_resource_usage_aggregations: _Optional[_Iterable[_Union[DailyResourceUsageAggregation, _Mapping]]]=...) -> None:
        ...

class DailyResourceUsageAggregation(_message.Message):
    __slots__ = ('date', 'cpu', 'memory', 'network', 'disk')

    class Stats(_message.Message):
        __slots__ = ('average', 'median', 'nintey_fifth_percentile', 'peak')
        AVERAGE_FIELD_NUMBER: _ClassVar[int]
        MEDIAN_FIELD_NUMBER: _ClassVar[int]
        NINTEY_FIFTH_PERCENTILE_FIELD_NUMBER: _ClassVar[int]
        PEAK_FIELD_NUMBER: _ClassVar[int]
        average: float
        median: float
        nintey_fifth_percentile: float
        peak: float

        def __init__(self, average: _Optional[float]=..., median: _Optional[float]=..., nintey_fifth_percentile: _Optional[float]=..., peak: _Optional[float]=...) -> None:
            ...

    class CPU(_message.Message):
        __slots__ = ('utilization_percentage',)
        UTILIZATION_PERCENTAGE_FIELD_NUMBER: _ClassVar[int]
        utilization_percentage: DailyResourceUsageAggregation.Stats

        def __init__(self, utilization_percentage: _Optional[_Union[DailyResourceUsageAggregation.Stats, _Mapping]]=...) -> None:
            ...

    class Memory(_message.Message):
        __slots__ = ('utilization_percentage',)
        UTILIZATION_PERCENTAGE_FIELD_NUMBER: _ClassVar[int]
        utilization_percentage: DailyResourceUsageAggregation.Stats

        def __init__(self, utilization_percentage: _Optional[_Union[DailyResourceUsageAggregation.Stats, _Mapping]]=...) -> None:
            ...

    class Network(_message.Message):
        __slots__ = ('ingress_bps', 'egress_bps')
        INGRESS_BPS_FIELD_NUMBER: _ClassVar[int]
        EGRESS_BPS_FIELD_NUMBER: _ClassVar[int]
        ingress_bps: DailyResourceUsageAggregation.Stats
        egress_bps: DailyResourceUsageAggregation.Stats

        def __init__(self, ingress_bps: _Optional[_Union[DailyResourceUsageAggregation.Stats, _Mapping]]=..., egress_bps: _Optional[_Union[DailyResourceUsageAggregation.Stats, _Mapping]]=...) -> None:
            ...

    class Disk(_message.Message):
        __slots__ = ('iops',)
        IOPS_FIELD_NUMBER: _ClassVar[int]
        iops: DailyResourceUsageAggregation.Stats

        def __init__(self, iops: _Optional[_Union[DailyResourceUsageAggregation.Stats, _Mapping]]=...) -> None:
            ...
    DATE_FIELD_NUMBER: _ClassVar[int]
    CPU_FIELD_NUMBER: _ClassVar[int]
    MEMORY_FIELD_NUMBER: _ClassVar[int]
    NETWORK_FIELD_NUMBER: _ClassVar[int]
    DISK_FIELD_NUMBER: _ClassVar[int]
    date: _date_pb2.Date
    cpu: DailyResourceUsageAggregation.CPU
    memory: DailyResourceUsageAggregation.Memory
    network: DailyResourceUsageAggregation.Network
    disk: DailyResourceUsageAggregation.Disk

    def __init__(self, date: _Optional[_Union[_date_pb2.Date, _Mapping]]=..., cpu: _Optional[_Union[DailyResourceUsageAggregation.CPU, _Mapping]]=..., memory: _Optional[_Union[DailyResourceUsageAggregation.Memory, _Mapping]]=..., network: _Optional[_Union[DailyResourceUsageAggregation.Network, _Mapping]]=..., disk: _Optional[_Union[DailyResourceUsageAggregation.Disk, _Mapping]]=...) -> None:
        ...

class InsightList(_message.Message):
    __slots__ = ('insights', 'update_time')
    INSIGHTS_FIELD_NUMBER: _ClassVar[int]
    UPDATE_TIME_FIELD_NUMBER: _ClassVar[int]
    insights: _containers.RepeatedCompositeFieldContainer[Insight]
    update_time: _timestamp_pb2.Timestamp

    def __init__(self, insights: _Optional[_Iterable[_Union[Insight, _Mapping]]]=..., update_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]]=...) -> None:
        ...

class Insight(_message.Message):
    __slots__ = ('migration_insight', 'generic_insight')
    MIGRATION_INSIGHT_FIELD_NUMBER: _ClassVar[int]
    GENERIC_INSIGHT_FIELD_NUMBER: _ClassVar[int]
    migration_insight: MigrationInsight
    generic_insight: GenericInsight

    def __init__(self, migration_insight: _Optional[_Union[MigrationInsight, _Mapping]]=..., generic_insight: _Optional[_Union[GenericInsight, _Mapping]]=...) -> None:
        ...

class GenericInsight(_message.Message):
    __slots__ = ('message_id', 'default_message', 'additional_information')
    MESSAGE_ID_FIELD_NUMBER: _ClassVar[int]
    DEFAULT_MESSAGE_FIELD_NUMBER: _ClassVar[int]
    ADDITIONAL_INFORMATION_FIELD_NUMBER: _ClassVar[int]
    message_id: int
    default_message: str
    additional_information: _containers.RepeatedScalarFieldContainer[str]

    def __init__(self, message_id: _Optional[int]=..., default_message: _Optional[str]=..., additional_information: _Optional[_Iterable[str]]=...) -> None:
        ...

class MigrationInsight(_message.Message):
    __slots__ = ('fit', 'compute_engine_target')
    FIT_FIELD_NUMBER: _ClassVar[int]
    COMPUTE_ENGINE_TARGET_FIELD_NUMBER: _ClassVar[int]
    fit: FitDescriptor
    compute_engine_target: ComputeEngineMigrationTarget

    def __init__(self, fit: _Optional[_Union[FitDescriptor, _Mapping]]=..., compute_engine_target: _Optional[_Union[ComputeEngineMigrationTarget, _Mapping]]=...) -> None:
        ...

class ComputeEngineMigrationTarget(_message.Message):
    __slots__ = ('shape',)
    SHAPE_FIELD_NUMBER: _ClassVar[int]
    shape: ComputeEngineShapeDescriptor

    def __init__(self, shape: _Optional[_Union[ComputeEngineShapeDescriptor, _Mapping]]=...) -> None:
        ...

class ComputeEngineShapeDescriptor(_message.Message):
    __slots__ = ('memory_mb', 'physical_core_count', 'logical_core_count', 'series', 'machine_type', 'storage')
    MEMORY_MB_FIELD_NUMBER: _ClassVar[int]
    PHYSICAL_CORE_COUNT_FIELD_NUMBER: _ClassVar[int]
    LOGICAL_CORE_COUNT_FIELD_NUMBER: _ClassVar[int]
    SERIES_FIELD_NUMBER: _ClassVar[int]
    MACHINE_TYPE_FIELD_NUMBER: _ClassVar[int]
    STORAGE_FIELD_NUMBER: _ClassVar[int]
    memory_mb: int
    physical_core_count: int
    logical_core_count: int
    series: str
    machine_type: str
    storage: _containers.RepeatedCompositeFieldContainer[ComputeStorageDescriptor]

    def __init__(self, memory_mb: _Optional[int]=..., physical_core_count: _Optional[int]=..., logical_core_count: _Optional[int]=..., series: _Optional[str]=..., machine_type: _Optional[str]=..., storage: _Optional[_Iterable[_Union[ComputeStorageDescriptor, _Mapping]]]=...) -> None:
        ...

class ComputeStorageDescriptor(_message.Message):
    __slots__ = ('type', 'size_gb')
    TYPE_FIELD_NUMBER: _ClassVar[int]
    SIZE_GB_FIELD_NUMBER: _ClassVar[int]
    type: PersistentDiskType
    size_gb: int

    def __init__(self, type: _Optional[_Union[PersistentDiskType, str]]=..., size_gb: _Optional[int]=...) -> None:
        ...

class FitDescriptor(_message.Message):
    __slots__ = ('fit_level',)

    class FitLevel(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        FIT_LEVEL_UNSPECIFIED: _ClassVar[FitDescriptor.FitLevel]
        FIT: _ClassVar[FitDescriptor.FitLevel]
        NO_FIT: _ClassVar[FitDescriptor.FitLevel]
        REQUIRES_EFFORT: _ClassVar[FitDescriptor.FitLevel]
    FIT_LEVEL_UNSPECIFIED: FitDescriptor.FitLevel
    FIT: FitDescriptor.FitLevel
    NO_FIT: FitDescriptor.FitLevel
    REQUIRES_EFFORT: FitDescriptor.FitLevel
    FIT_LEVEL_FIELD_NUMBER: _ClassVar[int]
    fit_level: FitDescriptor.FitLevel

    def __init__(self, fit_level: _Optional[_Union[FitDescriptor.FitLevel, str]]=...) -> None:
        ...

class Aggregation(_message.Message):
    __slots__ = ('field', 'count', 'sum', 'histogram', 'frequency')

    class Count(_message.Message):
        __slots__ = ()

        def __init__(self) -> None:
            ...

    class Sum(_message.Message):
        __slots__ = ()

        def __init__(self) -> None:
            ...

    class Histogram(_message.Message):
        __slots__ = ('lower_bounds',)
        LOWER_BOUNDS_FIELD_NUMBER: _ClassVar[int]
        lower_bounds: _containers.RepeatedScalarFieldContainer[float]

        def __init__(self, lower_bounds: _Optional[_Iterable[float]]=...) -> None:
            ...

    class Frequency(_message.Message):
        __slots__ = ()

        def __init__(self) -> None:
            ...
    FIELD_FIELD_NUMBER: _ClassVar[int]
    COUNT_FIELD_NUMBER: _ClassVar[int]
    SUM_FIELD_NUMBER: _ClassVar[int]
    HISTOGRAM_FIELD_NUMBER: _ClassVar[int]
    FREQUENCY_FIELD_NUMBER: _ClassVar[int]
    field: str
    count: Aggregation.Count
    sum: Aggregation.Sum
    histogram: Aggregation.Histogram
    frequency: Aggregation.Frequency

    def __init__(self, field: _Optional[str]=..., count: _Optional[_Union[Aggregation.Count, _Mapping]]=..., sum: _Optional[_Union[Aggregation.Sum, _Mapping]]=..., histogram: _Optional[_Union[Aggregation.Histogram, _Mapping]]=..., frequency: _Optional[_Union[Aggregation.Frequency, _Mapping]]=...) -> None:
        ...

class AggregationResult(_message.Message):
    __slots__ = ('field', 'count', 'sum', 'histogram', 'frequency')

    class Count(_message.Message):
        __slots__ = ('value',)
        VALUE_FIELD_NUMBER: _ClassVar[int]
        value: int

        def __init__(self, value: _Optional[int]=...) -> None:
            ...

    class Sum(_message.Message):
        __slots__ = ('value',)
        VALUE_FIELD_NUMBER: _ClassVar[int]
        value: float

        def __init__(self, value: _Optional[float]=...) -> None:
            ...

    class Histogram(_message.Message):
        __slots__ = ('buckets',)

        class Bucket(_message.Message):
            __slots__ = ('lower_bound', 'upper_bound', 'count')
            LOWER_BOUND_FIELD_NUMBER: _ClassVar[int]
            UPPER_BOUND_FIELD_NUMBER: _ClassVar[int]
            COUNT_FIELD_NUMBER: _ClassVar[int]
            lower_bound: float
            upper_bound: float
            count: int

            def __init__(self, lower_bound: _Optional[float]=..., upper_bound: _Optional[float]=..., count: _Optional[int]=...) -> None:
                ...
        BUCKETS_FIELD_NUMBER: _ClassVar[int]
        buckets: _containers.RepeatedCompositeFieldContainer[AggregationResult.Histogram.Bucket]

        def __init__(self, buckets: _Optional[_Iterable[_Union[AggregationResult.Histogram.Bucket, _Mapping]]]=...) -> None:
            ...

    class Frequency(_message.Message):
        __slots__ = ('values',)

        class ValuesEntry(_message.Message):
            __slots__ = ('key', 'value')
            KEY_FIELD_NUMBER: _ClassVar[int]
            VALUE_FIELD_NUMBER: _ClassVar[int]
            key: str
            value: int

            def __init__(self, key: _Optional[str]=..., value: _Optional[int]=...) -> None:
                ...
        VALUES_FIELD_NUMBER: _ClassVar[int]
        values: _containers.ScalarMap[str, int]

        def __init__(self, values: _Optional[_Mapping[str, int]]=...) -> None:
            ...
    FIELD_FIELD_NUMBER: _ClassVar[int]
    COUNT_FIELD_NUMBER: _ClassVar[int]
    SUM_FIELD_NUMBER: _ClassVar[int]
    HISTOGRAM_FIELD_NUMBER: _ClassVar[int]
    FREQUENCY_FIELD_NUMBER: _ClassVar[int]
    field: str
    count: AggregationResult.Count
    sum: AggregationResult.Sum
    histogram: AggregationResult.Histogram
    frequency: AggregationResult.Frequency

    def __init__(self, field: _Optional[str]=..., count: _Optional[_Union[AggregationResult.Count, _Mapping]]=..., sum: _Optional[_Union[AggregationResult.Sum, _Mapping]]=..., histogram: _Optional[_Union[AggregationResult.Histogram, _Mapping]]=..., frequency: _Optional[_Union[AggregationResult.Frequency, _Mapping]]=...) -> None:
        ...

class FileValidationReport(_message.Message):
    __slots__ = ('file_name', 'row_errors', 'partial_report', 'file_errors')
    FILE_NAME_FIELD_NUMBER: _ClassVar[int]
    ROW_ERRORS_FIELD_NUMBER: _ClassVar[int]
    PARTIAL_REPORT_FIELD_NUMBER: _ClassVar[int]
    FILE_ERRORS_FIELD_NUMBER: _ClassVar[int]
    file_name: str
    row_errors: _containers.RepeatedCompositeFieldContainer[ImportRowError]
    partial_report: bool
    file_errors: _containers.RepeatedCompositeFieldContainer[ImportError]

    def __init__(self, file_name: _Optional[str]=..., row_errors: _Optional[_Iterable[_Union[ImportRowError, _Mapping]]]=..., partial_report: bool=..., file_errors: _Optional[_Iterable[_Union[ImportError, _Mapping]]]=...) -> None:
        ...

class ValidationReport(_message.Message):
    __slots__ = ('file_validations', 'job_errors')
    FILE_VALIDATIONS_FIELD_NUMBER: _ClassVar[int]
    JOB_ERRORS_FIELD_NUMBER: _ClassVar[int]
    file_validations: _containers.RepeatedCompositeFieldContainer[FileValidationReport]
    job_errors: _containers.RepeatedCompositeFieldContainer[ImportError]

    def __init__(self, file_validations: _Optional[_Iterable[_Union[FileValidationReport, _Mapping]]]=..., job_errors: _Optional[_Iterable[_Union[ImportError, _Mapping]]]=...) -> None:
        ...

class ExecutionReport(_message.Message):
    __slots__ = ('frames_reported', 'execution_errors', 'total_rows_count')
    FRAMES_REPORTED_FIELD_NUMBER: _ClassVar[int]
    EXECUTION_ERRORS_FIELD_NUMBER: _ClassVar[int]
    TOTAL_ROWS_COUNT_FIELD_NUMBER: _ClassVar[int]
    frames_reported: int
    execution_errors: ValidationReport
    total_rows_count: int

    def __init__(self, frames_reported: _Optional[int]=..., execution_errors: _Optional[_Union[ValidationReport, _Mapping]]=..., total_rows_count: _Optional[int]=...) -> None:
        ...

class ImportError(_message.Message):
    __slots__ = ('error_details', 'severity')

    class Severity(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        SEVERITY_UNSPECIFIED: _ClassVar[ImportError.Severity]
        ERROR: _ClassVar[ImportError.Severity]
        WARNING: _ClassVar[ImportError.Severity]
        INFO: _ClassVar[ImportError.Severity]
    SEVERITY_UNSPECIFIED: ImportError.Severity
    ERROR: ImportError.Severity
    WARNING: ImportError.Severity
    INFO: ImportError.Severity
    ERROR_DETAILS_FIELD_NUMBER: _ClassVar[int]
    SEVERITY_FIELD_NUMBER: _ClassVar[int]
    error_details: str
    severity: ImportError.Severity

    def __init__(self, error_details: _Optional[str]=..., severity: _Optional[_Union[ImportError.Severity, str]]=...) -> None:
        ...

class ImportRowError(_message.Message):
    __slots__ = ('row_number', 'vm_name', 'vm_uuid', 'errors')
    ROW_NUMBER_FIELD_NUMBER: _ClassVar[int]
    VM_NAME_FIELD_NUMBER: _ClassVar[int]
    VM_UUID_FIELD_NUMBER: _ClassVar[int]
    ERRORS_FIELD_NUMBER: _ClassVar[int]
    row_number: int
    vm_name: str
    vm_uuid: str
    errors: _containers.RepeatedCompositeFieldContainer[ImportError]

    def __init__(self, row_number: _Optional[int]=..., vm_name: _Optional[str]=..., vm_uuid: _Optional[str]=..., errors: _Optional[_Iterable[_Union[ImportError, _Mapping]]]=...) -> None:
        ...

class UploadFileInfo(_message.Message):
    __slots__ = ('signed_uri', 'headers', 'uri_expiration_time')

    class HeadersEntry(_message.Message):
        __slots__ = ('key', 'value')
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: str

        def __init__(self, key: _Optional[str]=..., value: _Optional[str]=...) -> None:
            ...
    SIGNED_URI_FIELD_NUMBER: _ClassVar[int]
    HEADERS_FIELD_NUMBER: _ClassVar[int]
    URI_EXPIRATION_TIME_FIELD_NUMBER: _ClassVar[int]
    signed_uri: str
    headers: _containers.ScalarMap[str, str]
    uri_expiration_time: _timestamp_pb2.Timestamp

    def __init__(self, signed_uri: _Optional[str]=..., headers: _Optional[_Mapping[str, str]]=..., uri_expiration_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]]=...) -> None:
        ...

class AssetList(_message.Message):
    __slots__ = ('asset_ids',)
    ASSET_IDS_FIELD_NUMBER: _ClassVar[int]
    asset_ids: _containers.RepeatedScalarFieldContainer[str]

    def __init__(self, asset_ids: _Optional[_Iterable[str]]=...) -> None:
        ...

class FrameViolationEntry(_message.Message):
    __slots__ = ('field', 'violation')
    FIELD_FIELD_NUMBER: _ClassVar[int]
    VIOLATION_FIELD_NUMBER: _ClassVar[int]
    field: str
    violation: str

    def __init__(self, field: _Optional[str]=..., violation: _Optional[str]=...) -> None:
        ...

class VirtualMachinePreferences(_message.Message):
    __slots__ = ('target_product', 'region_preferences', 'commitment_plan', 'sizing_optimization_strategy', 'compute_engine_preferences', 'vmware_engine_preferences', 'sole_tenancy_preferences')
    TARGET_PRODUCT_FIELD_NUMBER: _ClassVar[int]
    REGION_PREFERENCES_FIELD_NUMBER: _ClassVar[int]
    COMMITMENT_PLAN_FIELD_NUMBER: _ClassVar[int]
    SIZING_OPTIMIZATION_STRATEGY_FIELD_NUMBER: _ClassVar[int]
    COMPUTE_ENGINE_PREFERENCES_FIELD_NUMBER: _ClassVar[int]
    VMWARE_ENGINE_PREFERENCES_FIELD_NUMBER: _ClassVar[int]
    SOLE_TENANCY_PREFERENCES_FIELD_NUMBER: _ClassVar[int]
    target_product: ComputeMigrationTargetProduct
    region_preferences: RegionPreferences
    commitment_plan: CommitmentPlan
    sizing_optimization_strategy: SizingOptimizationStrategy
    compute_engine_preferences: ComputeEnginePreferences
    vmware_engine_preferences: VmwareEnginePreferences
    sole_tenancy_preferences: SoleTenancyPreferences

    def __init__(self, target_product: _Optional[_Union[ComputeMigrationTargetProduct, str]]=..., region_preferences: _Optional[_Union[RegionPreferences, _Mapping]]=..., commitment_plan: _Optional[_Union[CommitmentPlan, str]]=..., sizing_optimization_strategy: _Optional[_Union[SizingOptimizationStrategy, str]]=..., compute_engine_preferences: _Optional[_Union[ComputeEnginePreferences, _Mapping]]=..., vmware_engine_preferences: _Optional[_Union[VmwareEnginePreferences, _Mapping]]=..., sole_tenancy_preferences: _Optional[_Union[SoleTenancyPreferences, _Mapping]]=...) -> None:
        ...

class ComputeEnginePreferences(_message.Message):
    __slots__ = ('machine_preferences', 'license_type')
    MACHINE_PREFERENCES_FIELD_NUMBER: _ClassVar[int]
    LICENSE_TYPE_FIELD_NUMBER: _ClassVar[int]
    machine_preferences: MachinePreferences
    license_type: LicenseType

    def __init__(self, machine_preferences: _Optional[_Union[MachinePreferences, _Mapping]]=..., license_type: _Optional[_Union[LicenseType, str]]=...) -> None:
        ...

class MachinePreferences(_message.Message):
    __slots__ = ('allowed_machine_series',)
    ALLOWED_MACHINE_SERIES_FIELD_NUMBER: _ClassVar[int]
    allowed_machine_series: _containers.RepeatedCompositeFieldContainer[MachineSeries]

    def __init__(self, allowed_machine_series: _Optional[_Iterable[_Union[MachineSeries, _Mapping]]]=...) -> None:
        ...

class MachineSeries(_message.Message):
    __slots__ = ('code',)
    CODE_FIELD_NUMBER: _ClassVar[int]
    code: str

    def __init__(self, code: _Optional[str]=...) -> None:
        ...

class VmwareEnginePreferences(_message.Message):
    __slots__ = ('cpu_overcommit_ratio', 'memory_overcommit_ratio', 'storage_deduplication_compression_ratio', 'commitment_plan')

    class CommitmentPlan(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        COMMITMENT_PLAN_UNSPECIFIED: _ClassVar[VmwareEnginePreferences.CommitmentPlan]
        ON_DEMAND: _ClassVar[VmwareEnginePreferences.CommitmentPlan]
        COMMITMENT_1_YEAR_MONTHLY_PAYMENTS: _ClassVar[VmwareEnginePreferences.CommitmentPlan]
        COMMITMENT_3_YEAR_MONTHLY_PAYMENTS: _ClassVar[VmwareEnginePreferences.CommitmentPlan]
        COMMITMENT_1_YEAR_UPFRONT_PAYMENT: _ClassVar[VmwareEnginePreferences.CommitmentPlan]
        COMMITMENT_3_YEAR_UPFRONT_PAYMENT: _ClassVar[VmwareEnginePreferences.CommitmentPlan]
    COMMITMENT_PLAN_UNSPECIFIED: VmwareEnginePreferences.CommitmentPlan
    ON_DEMAND: VmwareEnginePreferences.CommitmentPlan
    COMMITMENT_1_YEAR_MONTHLY_PAYMENTS: VmwareEnginePreferences.CommitmentPlan
    COMMITMENT_3_YEAR_MONTHLY_PAYMENTS: VmwareEnginePreferences.CommitmentPlan
    COMMITMENT_1_YEAR_UPFRONT_PAYMENT: VmwareEnginePreferences.CommitmentPlan
    COMMITMENT_3_YEAR_UPFRONT_PAYMENT: VmwareEnginePreferences.CommitmentPlan
    CPU_OVERCOMMIT_RATIO_FIELD_NUMBER: _ClassVar[int]
    MEMORY_OVERCOMMIT_RATIO_FIELD_NUMBER: _ClassVar[int]
    STORAGE_DEDUPLICATION_COMPRESSION_RATIO_FIELD_NUMBER: _ClassVar[int]
    COMMITMENT_PLAN_FIELD_NUMBER: _ClassVar[int]
    cpu_overcommit_ratio: float
    memory_overcommit_ratio: float
    storage_deduplication_compression_ratio: float
    commitment_plan: VmwareEnginePreferences.CommitmentPlan

    def __init__(self, cpu_overcommit_ratio: _Optional[float]=..., memory_overcommit_ratio: _Optional[float]=..., storage_deduplication_compression_ratio: _Optional[float]=..., commitment_plan: _Optional[_Union[VmwareEnginePreferences.CommitmentPlan, str]]=...) -> None:
        ...

class SoleTenancyPreferences(_message.Message):
    __slots__ = ('cpu_overcommit_ratio', 'host_maintenance_policy', 'commitment_plan', 'node_types')

    class HostMaintenancePolicy(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        HOST_MAINTENANCE_POLICY_UNSPECIFIED: _ClassVar[SoleTenancyPreferences.HostMaintenancePolicy]
        HOST_MAINTENANCE_POLICY_DEFAULT: _ClassVar[SoleTenancyPreferences.HostMaintenancePolicy]
        HOST_MAINTENANCE_POLICY_RESTART_IN_PLACE: _ClassVar[SoleTenancyPreferences.HostMaintenancePolicy]
        HOST_MAINTENANCE_POLICY_MIGRATE_WITHIN_NODE_GROUP: _ClassVar[SoleTenancyPreferences.HostMaintenancePolicy]
    HOST_MAINTENANCE_POLICY_UNSPECIFIED: SoleTenancyPreferences.HostMaintenancePolicy
    HOST_MAINTENANCE_POLICY_DEFAULT: SoleTenancyPreferences.HostMaintenancePolicy
    HOST_MAINTENANCE_POLICY_RESTART_IN_PLACE: SoleTenancyPreferences.HostMaintenancePolicy
    HOST_MAINTENANCE_POLICY_MIGRATE_WITHIN_NODE_GROUP: SoleTenancyPreferences.HostMaintenancePolicy

    class CommitmentPlan(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        COMMITMENT_PLAN_UNSPECIFIED: _ClassVar[SoleTenancyPreferences.CommitmentPlan]
        ON_DEMAND: _ClassVar[SoleTenancyPreferences.CommitmentPlan]
        COMMITMENT_1_YEAR: _ClassVar[SoleTenancyPreferences.CommitmentPlan]
        COMMITMENT_3_YEAR: _ClassVar[SoleTenancyPreferences.CommitmentPlan]
    COMMITMENT_PLAN_UNSPECIFIED: SoleTenancyPreferences.CommitmentPlan
    ON_DEMAND: SoleTenancyPreferences.CommitmentPlan
    COMMITMENT_1_YEAR: SoleTenancyPreferences.CommitmentPlan
    COMMITMENT_3_YEAR: SoleTenancyPreferences.CommitmentPlan
    CPU_OVERCOMMIT_RATIO_FIELD_NUMBER: _ClassVar[int]
    HOST_MAINTENANCE_POLICY_FIELD_NUMBER: _ClassVar[int]
    COMMITMENT_PLAN_FIELD_NUMBER: _ClassVar[int]
    NODE_TYPES_FIELD_NUMBER: _ClassVar[int]
    cpu_overcommit_ratio: float
    host_maintenance_policy: SoleTenancyPreferences.HostMaintenancePolicy
    commitment_plan: SoleTenancyPreferences.CommitmentPlan
    node_types: _containers.RepeatedCompositeFieldContainer[SoleTenantNodeType]

    def __init__(self, cpu_overcommit_ratio: _Optional[float]=..., host_maintenance_policy: _Optional[_Union[SoleTenancyPreferences.HostMaintenancePolicy, str]]=..., commitment_plan: _Optional[_Union[SoleTenancyPreferences.CommitmentPlan, str]]=..., node_types: _Optional[_Iterable[_Union[SoleTenantNodeType, _Mapping]]]=...) -> None:
        ...

class SoleTenantNodeType(_message.Message):
    __slots__ = ('node_name',)
    NODE_NAME_FIELD_NUMBER: _ClassVar[int]
    node_name: str

    def __init__(self, node_name: _Optional[str]=...) -> None:
        ...

class RegionPreferences(_message.Message):
    __slots__ = ('preferred_regions',)
    PREFERRED_REGIONS_FIELD_NUMBER: _ClassVar[int]
    preferred_regions: _containers.RepeatedScalarFieldContainer[str]

    def __init__(self, preferred_regions: _Optional[_Iterable[str]]=...) -> None:
        ...

class Settings(_message.Message):
    __slots__ = ('name', 'preference_set')
    NAME_FIELD_NUMBER: _ClassVar[int]
    PREFERENCE_SET_FIELD_NUMBER: _ClassVar[int]
    name: str
    preference_set: str

    def __init__(self, name: _Optional[str]=..., preference_set: _Optional[str]=...) -> None:
        ...

class ReportSummary(_message.Message):
    __slots__ = ('all_assets_stats', 'group_findings')

    class ChartData(_message.Message):
        __slots__ = ('data_points',)

        class DataPoint(_message.Message):
            __slots__ = ('label', 'value')
            LABEL_FIELD_NUMBER: _ClassVar[int]
            VALUE_FIELD_NUMBER: _ClassVar[int]
            label: str
            value: float

            def __init__(self, label: _Optional[str]=..., value: _Optional[float]=...) -> None:
                ...
        DATA_POINTS_FIELD_NUMBER: _ClassVar[int]
        data_points: _containers.RepeatedCompositeFieldContainer[ReportSummary.ChartData.DataPoint]

        def __init__(self, data_points: _Optional[_Iterable[_Union[ReportSummary.ChartData.DataPoint, _Mapping]]]=...) -> None:
            ...

    class UtilizationChartData(_message.Message):
        __slots__ = ('used', 'free')
        USED_FIELD_NUMBER: _ClassVar[int]
        FREE_FIELD_NUMBER: _ClassVar[int]
        used: int
        free: int

        def __init__(self, used: _Optional[int]=..., free: _Optional[int]=...) -> None:
            ...

    class HistogramChartData(_message.Message):
        __slots__ = ('buckets',)

        class Bucket(_message.Message):
            __slots__ = ('lower_bound', 'upper_bound', 'count')
            LOWER_BOUND_FIELD_NUMBER: _ClassVar[int]
            UPPER_BOUND_FIELD_NUMBER: _ClassVar[int]
            COUNT_FIELD_NUMBER: _ClassVar[int]
            lower_bound: int
            upper_bound: int
            count: int

            def __init__(self, lower_bound: _Optional[int]=..., upper_bound: _Optional[int]=..., count: _Optional[int]=...) -> None:
                ...
        BUCKETS_FIELD_NUMBER: _ClassVar[int]
        buckets: _containers.RepeatedCompositeFieldContainer[ReportSummary.HistogramChartData.Bucket]

        def __init__(self, buckets: _Optional[_Iterable[_Union[ReportSummary.HistogramChartData.Bucket, _Mapping]]]=...) -> None:
            ...

    class AssetAggregateStats(_message.Message):
        __slots__ = ('total_memory_bytes', 'total_storage_bytes', 'total_cores', 'total_assets', 'memory_utilization_chart', 'storage_utilization_chart', 'operating_system', 'core_count_histogram', 'memory_bytes_histogram', 'storage_bytes_histogram')
        TOTAL_MEMORY_BYTES_FIELD_NUMBER: _ClassVar[int]
        TOTAL_STORAGE_BYTES_FIELD_NUMBER: _ClassVar[int]
        TOTAL_CORES_FIELD_NUMBER: _ClassVar[int]
        TOTAL_ASSETS_FIELD_NUMBER: _ClassVar[int]
        MEMORY_UTILIZATION_CHART_FIELD_NUMBER: _ClassVar[int]
        STORAGE_UTILIZATION_CHART_FIELD_NUMBER: _ClassVar[int]
        OPERATING_SYSTEM_FIELD_NUMBER: _ClassVar[int]
        CORE_COUNT_HISTOGRAM_FIELD_NUMBER: _ClassVar[int]
        MEMORY_BYTES_HISTOGRAM_FIELD_NUMBER: _ClassVar[int]
        STORAGE_BYTES_HISTOGRAM_FIELD_NUMBER: _ClassVar[int]
        total_memory_bytes: int
        total_storage_bytes: int
        total_cores: int
        total_assets: int
        memory_utilization_chart: ReportSummary.UtilizationChartData
        storage_utilization_chart: ReportSummary.UtilizationChartData
        operating_system: ReportSummary.ChartData
        core_count_histogram: ReportSummary.HistogramChartData
        memory_bytes_histogram: ReportSummary.HistogramChartData
        storage_bytes_histogram: ReportSummary.HistogramChartData

        def __init__(self, total_memory_bytes: _Optional[int]=..., total_storage_bytes: _Optional[int]=..., total_cores: _Optional[int]=..., total_assets: _Optional[int]=..., memory_utilization_chart: _Optional[_Union[ReportSummary.UtilizationChartData, _Mapping]]=..., storage_utilization_chart: _Optional[_Union[ReportSummary.UtilizationChartData, _Mapping]]=..., operating_system: _Optional[_Union[ReportSummary.ChartData, _Mapping]]=..., core_count_histogram: _Optional[_Union[ReportSummary.HistogramChartData, _Mapping]]=..., memory_bytes_histogram: _Optional[_Union[ReportSummary.HistogramChartData, _Mapping]]=..., storage_bytes_histogram: _Optional[_Union[ReportSummary.HistogramChartData, _Mapping]]=...) -> None:
            ...

    class MachineSeriesAllocation(_message.Message):
        __slots__ = ('machine_series', 'allocated_asset_count')
        MACHINE_SERIES_FIELD_NUMBER: _ClassVar[int]
        ALLOCATED_ASSET_COUNT_FIELD_NUMBER: _ClassVar[int]
        machine_series: MachineSeries
        allocated_asset_count: int

        def __init__(self, machine_series: _Optional[_Union[MachineSeries, _Mapping]]=..., allocated_asset_count: _Optional[int]=...) -> None:
            ...

    class ComputeEngineFinding(_message.Message):
        __slots__ = ('allocated_regions', 'allocated_asset_count', 'machine_series_allocations', 'allocated_disk_types')
        ALLOCATED_REGIONS_FIELD_NUMBER: _ClassVar[int]
        ALLOCATED_ASSET_COUNT_FIELD_NUMBER: _ClassVar[int]
        MACHINE_SERIES_ALLOCATIONS_FIELD_NUMBER: _ClassVar[int]
        ALLOCATED_DISK_TYPES_FIELD_NUMBER: _ClassVar[int]
        allocated_regions: _containers.RepeatedScalarFieldContainer[str]
        allocated_asset_count: int
        machine_series_allocations: _containers.RepeatedCompositeFieldContainer[ReportSummary.MachineSeriesAllocation]
        allocated_disk_types: _containers.RepeatedScalarFieldContainer[PersistentDiskType]

        def __init__(self, allocated_regions: _Optional[_Iterable[str]]=..., allocated_asset_count: _Optional[int]=..., machine_series_allocations: _Optional[_Iterable[_Union[ReportSummary.MachineSeriesAllocation, _Mapping]]]=..., allocated_disk_types: _Optional[_Iterable[_Union[PersistentDiskType, str]]]=...) -> None:
            ...

    class VmwareEngineFinding(_message.Message):
        __slots__ = ('allocated_regions', 'allocated_asset_count', 'node_allocations')
        ALLOCATED_REGIONS_FIELD_NUMBER: _ClassVar[int]
        ALLOCATED_ASSET_COUNT_FIELD_NUMBER: _ClassVar[int]
        NODE_ALLOCATIONS_FIELD_NUMBER: _ClassVar[int]
        allocated_regions: _containers.RepeatedScalarFieldContainer[str]
        allocated_asset_count: int
        node_allocations: _containers.RepeatedCompositeFieldContainer[ReportSummary.VmwareNodeAllocation]

        def __init__(self, allocated_regions: _Optional[_Iterable[str]]=..., allocated_asset_count: _Optional[int]=..., node_allocations: _Optional[_Iterable[_Union[ReportSummary.VmwareNodeAllocation, _Mapping]]]=...) -> None:
            ...

    class VmwareNodeAllocation(_message.Message):
        __slots__ = ('vmware_node', 'node_count', 'allocated_asset_count')
        VMWARE_NODE_FIELD_NUMBER: _ClassVar[int]
        NODE_COUNT_FIELD_NUMBER: _ClassVar[int]
        ALLOCATED_ASSET_COUNT_FIELD_NUMBER: _ClassVar[int]
        vmware_node: ReportSummary.VmwareNode
        node_count: int
        allocated_asset_count: int

        def __init__(self, vmware_node: _Optional[_Union[ReportSummary.VmwareNode, _Mapping]]=..., node_count: _Optional[int]=..., allocated_asset_count: _Optional[int]=...) -> None:
            ...

    class VmwareNode(_message.Message):
        __slots__ = ('code',)
        CODE_FIELD_NUMBER: _ClassVar[int]
        code: str

        def __init__(self, code: _Optional[str]=...) -> None:
            ...

    class SoleTenantFinding(_message.Message):
        __slots__ = ('allocated_regions', 'allocated_asset_count', 'node_allocations')
        ALLOCATED_REGIONS_FIELD_NUMBER: _ClassVar[int]
        ALLOCATED_ASSET_COUNT_FIELD_NUMBER: _ClassVar[int]
        NODE_ALLOCATIONS_FIELD_NUMBER: _ClassVar[int]
        allocated_regions: _containers.RepeatedScalarFieldContainer[str]
        allocated_asset_count: int
        node_allocations: _containers.RepeatedCompositeFieldContainer[ReportSummary.SoleTenantNodeAllocation]

        def __init__(self, allocated_regions: _Optional[_Iterable[str]]=..., allocated_asset_count: _Optional[int]=..., node_allocations: _Optional[_Iterable[_Union[ReportSummary.SoleTenantNodeAllocation, _Mapping]]]=...) -> None:
            ...

    class SoleTenantNodeAllocation(_message.Message):
        __slots__ = ('node', 'node_count', 'allocated_asset_count')
        NODE_FIELD_NUMBER: _ClassVar[int]
        NODE_COUNT_FIELD_NUMBER: _ClassVar[int]
        ALLOCATED_ASSET_COUNT_FIELD_NUMBER: _ClassVar[int]
        node: SoleTenantNodeType
        node_count: int
        allocated_asset_count: int

        def __init__(self, node: _Optional[_Union[SoleTenantNodeType, _Mapping]]=..., node_count: _Optional[int]=..., allocated_asset_count: _Optional[int]=...) -> None:
            ...

    class GroupPreferenceSetFinding(_message.Message):
        __slots__ = ('display_name', 'description', 'machine_preferences', 'monthly_cost_total', 'monthly_cost_compute', 'monthly_cost_os_license', 'monthly_cost_network_egress', 'monthly_cost_storage', 'monthly_cost_other', 'compute_engine_finding', 'vmware_engine_finding', 'sole_tenant_finding')
        DISPLAY_NAME_FIELD_NUMBER: _ClassVar[int]
        DESCRIPTION_FIELD_NUMBER: _ClassVar[int]
        MACHINE_PREFERENCES_FIELD_NUMBER: _ClassVar[int]
        MONTHLY_COST_TOTAL_FIELD_NUMBER: _ClassVar[int]
        MONTHLY_COST_COMPUTE_FIELD_NUMBER: _ClassVar[int]
        MONTHLY_COST_OS_LICENSE_FIELD_NUMBER: _ClassVar[int]
        MONTHLY_COST_NETWORK_EGRESS_FIELD_NUMBER: _ClassVar[int]
        MONTHLY_COST_STORAGE_FIELD_NUMBER: _ClassVar[int]
        MONTHLY_COST_OTHER_FIELD_NUMBER: _ClassVar[int]
        COMPUTE_ENGINE_FINDING_FIELD_NUMBER: _ClassVar[int]
        VMWARE_ENGINE_FINDING_FIELD_NUMBER: _ClassVar[int]
        SOLE_TENANT_FINDING_FIELD_NUMBER: _ClassVar[int]
        display_name: str
        description: str
        machine_preferences: VirtualMachinePreferences
        monthly_cost_total: _money_pb2.Money
        monthly_cost_compute: _money_pb2.Money
        monthly_cost_os_license: _money_pb2.Money
        monthly_cost_network_egress: _money_pb2.Money
        monthly_cost_storage: _money_pb2.Money
        monthly_cost_other: _money_pb2.Money
        compute_engine_finding: ReportSummary.ComputeEngineFinding
        vmware_engine_finding: ReportSummary.VmwareEngineFinding
        sole_tenant_finding: ReportSummary.SoleTenantFinding

        def __init__(self, display_name: _Optional[str]=..., description: _Optional[str]=..., machine_preferences: _Optional[_Union[VirtualMachinePreferences, _Mapping]]=..., monthly_cost_total: _Optional[_Union[_money_pb2.Money, _Mapping]]=..., monthly_cost_compute: _Optional[_Union[_money_pb2.Money, _Mapping]]=..., monthly_cost_os_license: _Optional[_Union[_money_pb2.Money, _Mapping]]=..., monthly_cost_network_egress: _Optional[_Union[_money_pb2.Money, _Mapping]]=..., monthly_cost_storage: _Optional[_Union[_money_pb2.Money, _Mapping]]=..., monthly_cost_other: _Optional[_Union[_money_pb2.Money, _Mapping]]=..., compute_engine_finding: _Optional[_Union[ReportSummary.ComputeEngineFinding, _Mapping]]=..., vmware_engine_finding: _Optional[_Union[ReportSummary.VmwareEngineFinding, _Mapping]]=..., sole_tenant_finding: _Optional[_Union[ReportSummary.SoleTenantFinding, _Mapping]]=...) -> None:
            ...

    class GroupFinding(_message.Message):
        __slots__ = ('display_name', 'description', 'asset_aggregate_stats', 'overlapping_asset_count', 'preference_set_findings')
        DISPLAY_NAME_FIELD_NUMBER: _ClassVar[int]
        DESCRIPTION_FIELD_NUMBER: _ClassVar[int]
        ASSET_AGGREGATE_STATS_FIELD_NUMBER: _ClassVar[int]
        OVERLAPPING_ASSET_COUNT_FIELD_NUMBER: _ClassVar[int]
        PREFERENCE_SET_FINDINGS_FIELD_NUMBER: _ClassVar[int]
        display_name: str
        description: str
        asset_aggregate_stats: ReportSummary.AssetAggregateStats
        overlapping_asset_count: int
        preference_set_findings: _containers.RepeatedCompositeFieldContainer[ReportSummary.GroupPreferenceSetFinding]

        def __init__(self, display_name: _Optional[str]=..., description: _Optional[str]=..., asset_aggregate_stats: _Optional[_Union[ReportSummary.AssetAggregateStats, _Mapping]]=..., overlapping_asset_count: _Optional[int]=..., preference_set_findings: _Optional[_Iterable[_Union[ReportSummary.GroupPreferenceSetFinding, _Mapping]]]=...) -> None:
            ...
    ALL_ASSETS_STATS_FIELD_NUMBER: _ClassVar[int]
    GROUP_FINDINGS_FIELD_NUMBER: _ClassVar[int]
    all_assets_stats: ReportSummary.AssetAggregateStats
    group_findings: _containers.RepeatedCompositeFieldContainer[ReportSummary.GroupFinding]

    def __init__(self, all_assets_stats: _Optional[_Union[ReportSummary.AssetAggregateStats, _Mapping]]=..., group_findings: _Optional[_Iterable[_Union[ReportSummary.GroupFinding, _Mapping]]]=...) -> None:
        ...