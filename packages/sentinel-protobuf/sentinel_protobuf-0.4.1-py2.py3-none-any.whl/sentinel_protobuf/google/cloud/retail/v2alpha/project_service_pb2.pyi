from google.api import annotations_pb2 as _annotations_pb2
from google.api import client_pb2 as _client_pb2
from google.api import field_behavior_pb2 as _field_behavior_pb2
from google.api import resource_pb2 as _resource_pb2
from google.cloud.retail.v2alpha import common_pb2 as _common_pb2
from google.cloud.retail.v2alpha import project_pb2 as _project_pb2
from google.longrunning import operations_pb2 as _operations_pb2
from google.protobuf import field_mask_pb2 as _field_mask_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class GetProjectRequest(_message.Message):
    __slots__ = ("name",)
    NAME_FIELD_NUMBER: _ClassVar[int]
    name: str
    def __init__(self, name: _Optional[str] = ...) -> None: ...

class AcceptTermsRequest(_message.Message):
    __slots__ = ("project",)
    PROJECT_FIELD_NUMBER: _ClassVar[int]
    project: str
    def __init__(self, project: _Optional[str] = ...) -> None: ...

class EnrollSolutionRequest(_message.Message):
    __slots__ = ("project", "solution")
    PROJECT_FIELD_NUMBER: _ClassVar[int]
    SOLUTION_FIELD_NUMBER: _ClassVar[int]
    project: str
    solution: _common_pb2.SolutionType
    def __init__(self, project: _Optional[str] = ..., solution: _Optional[_Union[_common_pb2.SolutionType, str]] = ...) -> None: ...

class EnrollSolutionResponse(_message.Message):
    __slots__ = ("enrolled_solution",)
    ENROLLED_SOLUTION_FIELD_NUMBER: _ClassVar[int]
    enrolled_solution: _common_pb2.SolutionType
    def __init__(self, enrolled_solution: _Optional[_Union[_common_pb2.SolutionType, str]] = ...) -> None: ...

class EnrollSolutionMetadata(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class ListEnrolledSolutionsRequest(_message.Message):
    __slots__ = ("parent",)
    PARENT_FIELD_NUMBER: _ClassVar[int]
    parent: str
    def __init__(self, parent: _Optional[str] = ...) -> None: ...

class ListEnrolledSolutionsResponse(_message.Message):
    __slots__ = ("enrolled_solutions",)
    ENROLLED_SOLUTIONS_FIELD_NUMBER: _ClassVar[int]
    enrolled_solutions: _containers.RepeatedScalarFieldContainer[_common_pb2.SolutionType]
    def __init__(self, enrolled_solutions: _Optional[_Iterable[_Union[_common_pb2.SolutionType, str]]] = ...) -> None: ...

class GetLoggingConfigRequest(_message.Message):
    __slots__ = ("name",)
    NAME_FIELD_NUMBER: _ClassVar[int]
    name: str
    def __init__(self, name: _Optional[str] = ...) -> None: ...

class UpdateLoggingConfigRequest(_message.Message):
    __slots__ = ("logging_config", "update_mask")
    LOGGING_CONFIG_FIELD_NUMBER: _ClassVar[int]
    UPDATE_MASK_FIELD_NUMBER: _ClassVar[int]
    logging_config: _project_pb2.LoggingConfig
    update_mask: _field_mask_pb2.FieldMask
    def __init__(self, logging_config: _Optional[_Union[_project_pb2.LoggingConfig, _Mapping]] = ..., update_mask: _Optional[_Union[_field_mask_pb2.FieldMask, _Mapping]] = ...) -> None: ...

class GetAlertConfigRequest(_message.Message):
    __slots__ = ("name",)
    NAME_FIELD_NUMBER: _ClassVar[int]
    name: str
    def __init__(self, name: _Optional[str] = ...) -> None: ...

class UpdateAlertConfigRequest(_message.Message):
    __slots__ = ("alert_config", "update_mask")
    ALERT_CONFIG_FIELD_NUMBER: _ClassVar[int]
    UPDATE_MASK_FIELD_NUMBER: _ClassVar[int]
    alert_config: _project_pb2.AlertConfig
    update_mask: _field_mask_pb2.FieldMask
    def __init__(self, alert_config: _Optional[_Union[_project_pb2.AlertConfig, _Mapping]] = ..., update_mask: _Optional[_Union[_field_mask_pb2.FieldMask, _Mapping]] = ...) -> None: ...
