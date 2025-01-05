from google.api import field_behavior_pb2 as _field_behavior_pb2
from google.api import resource_pb2 as _resource_pb2
from google.protobuf import timestamp_pb2 as _timestamp_pb2
from google.type import interval_pb2 as _interval_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union
DESCRIPTOR: _descriptor.FileDescriptor

class Violation(_message.Message):
    __slots__ = ('name', 'description', 'begin_time', 'update_time', 'resolve_time', 'category', 'state', 'non_compliant_org_policy', 'folder_id', 'remediation')

    class State(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        STATE_UNSPECIFIED: _ClassVar[Violation.State]
        RESOLVED: _ClassVar[Violation.State]
        UNRESOLVED: _ClassVar[Violation.State]
        EXCEPTION: _ClassVar[Violation.State]
    STATE_UNSPECIFIED: Violation.State
    RESOLVED: Violation.State
    UNRESOLVED: Violation.State
    EXCEPTION: Violation.State

    class Remediation(_message.Message):
        __slots__ = ('instructions', 'compliant_values', 'remediation_type')

        class RemediationType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
            __slots__ = ()
            REMEDIATION_TYPE_UNSPECIFIED: _ClassVar[Violation.Remediation.RemediationType]
            REMEDIATION_BOOLEAN_ORG_POLICY_VIOLATION: _ClassVar[Violation.Remediation.RemediationType]
            REMEDIATION_LIST_ALLOWED_VALUES_ORG_POLICY_VIOLATION: _ClassVar[Violation.Remediation.RemediationType]
            REMEDIATION_LIST_DENIED_VALUES_ORG_POLICY_VIOLATION: _ClassVar[Violation.Remediation.RemediationType]
            REMEDIATION_RESTRICT_CMEK_CRYPTO_KEY_PROJECTS_ORG_POLICY_VIOLATION: _ClassVar[Violation.Remediation.RemediationType]
            REMEDIATION_RESOURCE_VIOLATION: _ClassVar[Violation.Remediation.RemediationType]
        REMEDIATION_TYPE_UNSPECIFIED: Violation.Remediation.RemediationType
        REMEDIATION_BOOLEAN_ORG_POLICY_VIOLATION: Violation.Remediation.RemediationType
        REMEDIATION_LIST_ALLOWED_VALUES_ORG_POLICY_VIOLATION: Violation.Remediation.RemediationType
        REMEDIATION_LIST_DENIED_VALUES_ORG_POLICY_VIOLATION: Violation.Remediation.RemediationType
        REMEDIATION_RESTRICT_CMEK_CRYPTO_KEY_PROJECTS_ORG_POLICY_VIOLATION: Violation.Remediation.RemediationType
        REMEDIATION_RESOURCE_VIOLATION: Violation.Remediation.RemediationType

        class Instructions(_message.Message):
            __slots__ = ('gcloud_instructions', 'console_instructions')

            class Gcloud(_message.Message):
                __slots__ = ('gcloud_commands', 'steps', 'additional_links')
                GCLOUD_COMMANDS_FIELD_NUMBER: _ClassVar[int]
                STEPS_FIELD_NUMBER: _ClassVar[int]
                ADDITIONAL_LINKS_FIELD_NUMBER: _ClassVar[int]
                gcloud_commands: _containers.RepeatedScalarFieldContainer[str]
                steps: _containers.RepeatedScalarFieldContainer[str]
                additional_links: _containers.RepeatedScalarFieldContainer[str]

                def __init__(self, gcloud_commands: _Optional[_Iterable[str]]=..., steps: _Optional[_Iterable[str]]=..., additional_links: _Optional[_Iterable[str]]=...) -> None:
                    ...

            class Console(_message.Message):
                __slots__ = ('console_uris', 'steps', 'additional_links')
                CONSOLE_URIS_FIELD_NUMBER: _ClassVar[int]
                STEPS_FIELD_NUMBER: _ClassVar[int]
                ADDITIONAL_LINKS_FIELD_NUMBER: _ClassVar[int]
                console_uris: _containers.RepeatedScalarFieldContainer[str]
                steps: _containers.RepeatedScalarFieldContainer[str]
                additional_links: _containers.RepeatedScalarFieldContainer[str]

                def __init__(self, console_uris: _Optional[_Iterable[str]]=..., steps: _Optional[_Iterable[str]]=..., additional_links: _Optional[_Iterable[str]]=...) -> None:
                    ...
            GCLOUD_INSTRUCTIONS_FIELD_NUMBER: _ClassVar[int]
            CONSOLE_INSTRUCTIONS_FIELD_NUMBER: _ClassVar[int]
            gcloud_instructions: Violation.Remediation.Instructions.Gcloud
            console_instructions: Violation.Remediation.Instructions.Console

            def __init__(self, gcloud_instructions: _Optional[_Union[Violation.Remediation.Instructions.Gcloud, _Mapping]]=..., console_instructions: _Optional[_Union[Violation.Remediation.Instructions.Console, _Mapping]]=...) -> None:
                ...
        INSTRUCTIONS_FIELD_NUMBER: _ClassVar[int]
        COMPLIANT_VALUES_FIELD_NUMBER: _ClassVar[int]
        REMEDIATION_TYPE_FIELD_NUMBER: _ClassVar[int]
        instructions: Violation.Remediation.Instructions
        compliant_values: _containers.RepeatedScalarFieldContainer[str]
        remediation_type: Violation.Remediation.RemediationType

        def __init__(self, instructions: _Optional[_Union[Violation.Remediation.Instructions, _Mapping]]=..., compliant_values: _Optional[_Iterable[str]]=..., remediation_type: _Optional[_Union[Violation.Remediation.RemediationType, str]]=...) -> None:
            ...
    NAME_FIELD_NUMBER: _ClassVar[int]
    DESCRIPTION_FIELD_NUMBER: _ClassVar[int]
    BEGIN_TIME_FIELD_NUMBER: _ClassVar[int]
    UPDATE_TIME_FIELD_NUMBER: _ClassVar[int]
    RESOLVE_TIME_FIELD_NUMBER: _ClassVar[int]
    CATEGORY_FIELD_NUMBER: _ClassVar[int]
    STATE_FIELD_NUMBER: _ClassVar[int]
    NON_COMPLIANT_ORG_POLICY_FIELD_NUMBER: _ClassVar[int]
    FOLDER_ID_FIELD_NUMBER: _ClassVar[int]
    REMEDIATION_FIELD_NUMBER: _ClassVar[int]
    name: str
    description: str
    begin_time: _timestamp_pb2.Timestamp
    update_time: _timestamp_pb2.Timestamp
    resolve_time: _timestamp_pb2.Timestamp
    category: str
    state: Violation.State
    non_compliant_org_policy: str
    folder_id: int
    remediation: Violation.Remediation

    def __init__(self, name: _Optional[str]=..., description: _Optional[str]=..., begin_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]]=..., update_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]]=..., resolve_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]]=..., category: _Optional[str]=..., state: _Optional[_Union[Violation.State, str]]=..., non_compliant_org_policy: _Optional[str]=..., folder_id: _Optional[int]=..., remediation: _Optional[_Union[Violation.Remediation, _Mapping]]=...) -> None:
        ...

class ListViolationsRequest(_message.Message):
    __slots__ = ('parent', 'page_size', 'page_token', 'filter', 'order_by', 'interval')
    PARENT_FIELD_NUMBER: _ClassVar[int]
    PAGE_SIZE_FIELD_NUMBER: _ClassVar[int]
    PAGE_TOKEN_FIELD_NUMBER: _ClassVar[int]
    FILTER_FIELD_NUMBER: _ClassVar[int]
    ORDER_BY_FIELD_NUMBER: _ClassVar[int]
    INTERVAL_FIELD_NUMBER: _ClassVar[int]
    parent: str
    page_size: int
    page_token: str
    filter: str
    order_by: str
    interval: _interval_pb2.Interval

    def __init__(self, parent: _Optional[str]=..., page_size: _Optional[int]=..., page_token: _Optional[str]=..., filter: _Optional[str]=..., order_by: _Optional[str]=..., interval: _Optional[_Union[_interval_pb2.Interval, _Mapping]]=...) -> None:
        ...

class ListViolationsResponse(_message.Message):
    __slots__ = ('violations', 'next_page_token', 'unreachable')
    VIOLATIONS_FIELD_NUMBER: _ClassVar[int]
    NEXT_PAGE_TOKEN_FIELD_NUMBER: _ClassVar[int]
    UNREACHABLE_FIELD_NUMBER: _ClassVar[int]
    violations: _containers.RepeatedCompositeFieldContainer[Violation]
    next_page_token: str
    unreachable: _containers.RepeatedScalarFieldContainer[str]

    def __init__(self, violations: _Optional[_Iterable[_Union[Violation, _Mapping]]]=..., next_page_token: _Optional[str]=..., unreachable: _Optional[_Iterable[str]]=...) -> None:
        ...

class GetViolationRequest(_message.Message):
    __slots__ = ('name',)
    NAME_FIELD_NUMBER: _ClassVar[int]
    name: str

    def __init__(self, name: _Optional[str]=...) -> None:
        ...