from google.type import expr_pb2 as _expr_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union
DESCRIPTOR: _descriptor.FileDescriptor

class CustomConfig(_message.Message):
    __slots__ = ('predicate', 'custom_output', 'resource_selector', 'severity', 'description', 'recommendation')

    class Severity(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        SEVERITY_UNSPECIFIED: _ClassVar[CustomConfig.Severity]
        CRITICAL: _ClassVar[CustomConfig.Severity]
        HIGH: _ClassVar[CustomConfig.Severity]
        MEDIUM: _ClassVar[CustomConfig.Severity]
        LOW: _ClassVar[CustomConfig.Severity]
    SEVERITY_UNSPECIFIED: CustomConfig.Severity
    CRITICAL: CustomConfig.Severity
    HIGH: CustomConfig.Severity
    MEDIUM: CustomConfig.Severity
    LOW: CustomConfig.Severity

    class CustomOutputSpec(_message.Message):
        __slots__ = ('properties',)

        class Property(_message.Message):
            __slots__ = ('name', 'value_expression')
            NAME_FIELD_NUMBER: _ClassVar[int]
            VALUE_EXPRESSION_FIELD_NUMBER: _ClassVar[int]
            name: str
            value_expression: _expr_pb2.Expr

            def __init__(self, name: _Optional[str]=..., value_expression: _Optional[_Union[_expr_pb2.Expr, _Mapping]]=...) -> None:
                ...
        PROPERTIES_FIELD_NUMBER: _ClassVar[int]
        properties: _containers.RepeatedCompositeFieldContainer[CustomConfig.CustomOutputSpec.Property]

        def __init__(self, properties: _Optional[_Iterable[_Union[CustomConfig.CustomOutputSpec.Property, _Mapping]]]=...) -> None:
            ...

    class ResourceSelector(_message.Message):
        __slots__ = ('resource_types',)
        RESOURCE_TYPES_FIELD_NUMBER: _ClassVar[int]
        resource_types: _containers.RepeatedScalarFieldContainer[str]

        def __init__(self, resource_types: _Optional[_Iterable[str]]=...) -> None:
            ...
    PREDICATE_FIELD_NUMBER: _ClassVar[int]
    CUSTOM_OUTPUT_FIELD_NUMBER: _ClassVar[int]
    RESOURCE_SELECTOR_FIELD_NUMBER: _ClassVar[int]
    SEVERITY_FIELD_NUMBER: _ClassVar[int]
    DESCRIPTION_FIELD_NUMBER: _ClassVar[int]
    RECOMMENDATION_FIELD_NUMBER: _ClassVar[int]
    predicate: _expr_pb2.Expr
    custom_output: CustomConfig.CustomOutputSpec
    resource_selector: CustomConfig.ResourceSelector
    severity: CustomConfig.Severity
    description: str
    recommendation: str

    def __init__(self, predicate: _Optional[_Union[_expr_pb2.Expr, _Mapping]]=..., custom_output: _Optional[_Union[CustomConfig.CustomOutputSpec, _Mapping]]=..., resource_selector: _Optional[_Union[CustomConfig.ResourceSelector, _Mapping]]=..., severity: _Optional[_Union[CustomConfig.Severity, str]]=..., description: _Optional[str]=..., recommendation: _Optional[str]=...) -> None:
        ...