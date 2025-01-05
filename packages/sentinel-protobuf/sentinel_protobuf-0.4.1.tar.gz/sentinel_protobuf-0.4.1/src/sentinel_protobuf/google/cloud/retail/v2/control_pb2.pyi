from google.api import field_behavior_pb2 as _field_behavior_pb2
from google.api import resource_pb2 as _resource_pb2
from google.cloud.retail.v2 import common_pb2 as _common_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class Control(_message.Message):
    __slots__ = ("rule", "name", "display_name", "associated_serving_config_ids", "solution_types", "search_solution_use_case")
    RULE_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    DISPLAY_NAME_FIELD_NUMBER: _ClassVar[int]
    ASSOCIATED_SERVING_CONFIG_IDS_FIELD_NUMBER: _ClassVar[int]
    SOLUTION_TYPES_FIELD_NUMBER: _ClassVar[int]
    SEARCH_SOLUTION_USE_CASE_FIELD_NUMBER: _ClassVar[int]
    rule: _common_pb2.Rule
    name: str
    display_name: str
    associated_serving_config_ids: _containers.RepeatedScalarFieldContainer[str]
    solution_types: _containers.RepeatedScalarFieldContainer[_common_pb2.SolutionType]
    search_solution_use_case: _containers.RepeatedScalarFieldContainer[_common_pb2.SearchSolutionUseCase]
    def __init__(self, rule: _Optional[_Union[_common_pb2.Rule, _Mapping]] = ..., name: _Optional[str] = ..., display_name: _Optional[str] = ..., associated_serving_config_ids: _Optional[_Iterable[str]] = ..., solution_types: _Optional[_Iterable[_Union[_common_pb2.SolutionType, str]]] = ..., search_solution_use_case: _Optional[_Iterable[_Union[_common_pb2.SearchSolutionUseCase, str]]] = ...) -> None: ...
