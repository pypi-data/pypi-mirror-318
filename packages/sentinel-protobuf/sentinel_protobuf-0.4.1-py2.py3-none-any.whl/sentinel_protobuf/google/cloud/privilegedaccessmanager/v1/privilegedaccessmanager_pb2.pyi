from google.api import annotations_pb2 as _annotations_pb2
from google.api import client_pb2 as _client_pb2
from google.api import field_behavior_pb2 as _field_behavior_pb2
from google.api import resource_pb2 as _resource_pb2
from google.longrunning import operations_pb2 as _operations_pb2
from google.protobuf import duration_pb2 as _duration_pb2
from google.protobuf import field_mask_pb2 as _field_mask_pb2
from google.protobuf import timestamp_pb2 as _timestamp_pb2
from google.rpc import status_pb2 as _status_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union
DESCRIPTOR: _descriptor.FileDescriptor

class CheckOnboardingStatusRequest(_message.Message):
    __slots__ = ('parent',)
    PARENT_FIELD_NUMBER: _ClassVar[int]
    parent: str

    def __init__(self, parent: _Optional[str]=...) -> None:
        ...

class CheckOnboardingStatusResponse(_message.Message):
    __slots__ = ('service_account', 'findings')

    class Finding(_message.Message):
        __slots__ = ('iam_access_denied',)

        class IAMAccessDenied(_message.Message):
            __slots__ = ('missing_permissions',)
            MISSING_PERMISSIONS_FIELD_NUMBER: _ClassVar[int]
            missing_permissions: _containers.RepeatedScalarFieldContainer[str]

            def __init__(self, missing_permissions: _Optional[_Iterable[str]]=...) -> None:
                ...
        IAM_ACCESS_DENIED_FIELD_NUMBER: _ClassVar[int]
        iam_access_denied: CheckOnboardingStatusResponse.Finding.IAMAccessDenied

        def __init__(self, iam_access_denied: _Optional[_Union[CheckOnboardingStatusResponse.Finding.IAMAccessDenied, _Mapping]]=...) -> None:
            ...
    SERVICE_ACCOUNT_FIELD_NUMBER: _ClassVar[int]
    FINDINGS_FIELD_NUMBER: _ClassVar[int]
    service_account: str
    findings: _containers.RepeatedCompositeFieldContainer[CheckOnboardingStatusResponse.Finding]

    def __init__(self, service_account: _Optional[str]=..., findings: _Optional[_Iterable[_Union[CheckOnboardingStatusResponse.Finding, _Mapping]]]=...) -> None:
        ...

class Entitlement(_message.Message):
    __slots__ = ('name', 'create_time', 'update_time', 'eligible_users', 'approval_workflow', 'privileged_access', 'max_request_duration', 'state', 'requester_justification_config', 'additional_notification_targets', 'etag')

    class State(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        STATE_UNSPECIFIED: _ClassVar[Entitlement.State]
        CREATING: _ClassVar[Entitlement.State]
        AVAILABLE: _ClassVar[Entitlement.State]
        DELETING: _ClassVar[Entitlement.State]
        DELETED: _ClassVar[Entitlement.State]
        UPDATING: _ClassVar[Entitlement.State]
    STATE_UNSPECIFIED: Entitlement.State
    CREATING: Entitlement.State
    AVAILABLE: Entitlement.State
    DELETING: Entitlement.State
    DELETED: Entitlement.State
    UPDATING: Entitlement.State

    class RequesterJustificationConfig(_message.Message):
        __slots__ = ('not_mandatory', 'unstructured')

        class NotMandatory(_message.Message):
            __slots__ = ()

            def __init__(self) -> None:
                ...

        class Unstructured(_message.Message):
            __slots__ = ()

            def __init__(self) -> None:
                ...
        NOT_MANDATORY_FIELD_NUMBER: _ClassVar[int]
        UNSTRUCTURED_FIELD_NUMBER: _ClassVar[int]
        not_mandatory: Entitlement.RequesterJustificationConfig.NotMandatory
        unstructured: Entitlement.RequesterJustificationConfig.Unstructured

        def __init__(self, not_mandatory: _Optional[_Union[Entitlement.RequesterJustificationConfig.NotMandatory, _Mapping]]=..., unstructured: _Optional[_Union[Entitlement.RequesterJustificationConfig.Unstructured, _Mapping]]=...) -> None:
            ...

    class AdditionalNotificationTargets(_message.Message):
        __slots__ = ('admin_email_recipients', 'requester_email_recipients')
        ADMIN_EMAIL_RECIPIENTS_FIELD_NUMBER: _ClassVar[int]
        REQUESTER_EMAIL_RECIPIENTS_FIELD_NUMBER: _ClassVar[int]
        admin_email_recipients: _containers.RepeatedScalarFieldContainer[str]
        requester_email_recipients: _containers.RepeatedScalarFieldContainer[str]

        def __init__(self, admin_email_recipients: _Optional[_Iterable[str]]=..., requester_email_recipients: _Optional[_Iterable[str]]=...) -> None:
            ...
    NAME_FIELD_NUMBER: _ClassVar[int]
    CREATE_TIME_FIELD_NUMBER: _ClassVar[int]
    UPDATE_TIME_FIELD_NUMBER: _ClassVar[int]
    ELIGIBLE_USERS_FIELD_NUMBER: _ClassVar[int]
    APPROVAL_WORKFLOW_FIELD_NUMBER: _ClassVar[int]
    PRIVILEGED_ACCESS_FIELD_NUMBER: _ClassVar[int]
    MAX_REQUEST_DURATION_FIELD_NUMBER: _ClassVar[int]
    STATE_FIELD_NUMBER: _ClassVar[int]
    REQUESTER_JUSTIFICATION_CONFIG_FIELD_NUMBER: _ClassVar[int]
    ADDITIONAL_NOTIFICATION_TARGETS_FIELD_NUMBER: _ClassVar[int]
    ETAG_FIELD_NUMBER: _ClassVar[int]
    name: str
    create_time: _timestamp_pb2.Timestamp
    update_time: _timestamp_pb2.Timestamp
    eligible_users: _containers.RepeatedCompositeFieldContainer[AccessControlEntry]
    approval_workflow: ApprovalWorkflow
    privileged_access: PrivilegedAccess
    max_request_duration: _duration_pb2.Duration
    state: Entitlement.State
    requester_justification_config: Entitlement.RequesterJustificationConfig
    additional_notification_targets: Entitlement.AdditionalNotificationTargets
    etag: str

    def __init__(self, name: _Optional[str]=..., create_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]]=..., update_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]]=..., eligible_users: _Optional[_Iterable[_Union[AccessControlEntry, _Mapping]]]=..., approval_workflow: _Optional[_Union[ApprovalWorkflow, _Mapping]]=..., privileged_access: _Optional[_Union[PrivilegedAccess, _Mapping]]=..., max_request_duration: _Optional[_Union[_duration_pb2.Duration, _Mapping]]=..., state: _Optional[_Union[Entitlement.State, str]]=..., requester_justification_config: _Optional[_Union[Entitlement.RequesterJustificationConfig, _Mapping]]=..., additional_notification_targets: _Optional[_Union[Entitlement.AdditionalNotificationTargets, _Mapping]]=..., etag: _Optional[str]=...) -> None:
        ...

class AccessControlEntry(_message.Message):
    __slots__ = ('principals',)
    PRINCIPALS_FIELD_NUMBER: _ClassVar[int]
    principals: _containers.RepeatedScalarFieldContainer[str]

    def __init__(self, principals: _Optional[_Iterable[str]]=...) -> None:
        ...

class ApprovalWorkflow(_message.Message):
    __slots__ = ('manual_approvals',)
    MANUAL_APPROVALS_FIELD_NUMBER: _ClassVar[int]
    manual_approvals: ManualApprovals

    def __init__(self, manual_approvals: _Optional[_Union[ManualApprovals, _Mapping]]=...) -> None:
        ...

class ManualApprovals(_message.Message):
    __slots__ = ('require_approver_justification', 'steps')

    class Step(_message.Message):
        __slots__ = ('approvers', 'approvals_needed', 'approver_email_recipients')
        APPROVERS_FIELD_NUMBER: _ClassVar[int]
        APPROVALS_NEEDED_FIELD_NUMBER: _ClassVar[int]
        APPROVER_EMAIL_RECIPIENTS_FIELD_NUMBER: _ClassVar[int]
        approvers: _containers.RepeatedCompositeFieldContainer[AccessControlEntry]
        approvals_needed: int
        approver_email_recipients: _containers.RepeatedScalarFieldContainer[str]

        def __init__(self, approvers: _Optional[_Iterable[_Union[AccessControlEntry, _Mapping]]]=..., approvals_needed: _Optional[int]=..., approver_email_recipients: _Optional[_Iterable[str]]=...) -> None:
            ...
    REQUIRE_APPROVER_JUSTIFICATION_FIELD_NUMBER: _ClassVar[int]
    STEPS_FIELD_NUMBER: _ClassVar[int]
    require_approver_justification: bool
    steps: _containers.RepeatedCompositeFieldContainer[ManualApprovals.Step]

    def __init__(self, require_approver_justification: bool=..., steps: _Optional[_Iterable[_Union[ManualApprovals.Step, _Mapping]]]=...) -> None:
        ...

class PrivilegedAccess(_message.Message):
    __slots__ = ('gcp_iam_access',)

    class GcpIamAccess(_message.Message):
        __slots__ = ('resource_type', 'resource', 'role_bindings')

        class RoleBinding(_message.Message):
            __slots__ = ('role', 'condition_expression')
            ROLE_FIELD_NUMBER: _ClassVar[int]
            CONDITION_EXPRESSION_FIELD_NUMBER: _ClassVar[int]
            role: str
            condition_expression: str

            def __init__(self, role: _Optional[str]=..., condition_expression: _Optional[str]=...) -> None:
                ...
        RESOURCE_TYPE_FIELD_NUMBER: _ClassVar[int]
        RESOURCE_FIELD_NUMBER: _ClassVar[int]
        ROLE_BINDINGS_FIELD_NUMBER: _ClassVar[int]
        resource_type: str
        resource: str
        role_bindings: _containers.RepeatedCompositeFieldContainer[PrivilegedAccess.GcpIamAccess.RoleBinding]

        def __init__(self, resource_type: _Optional[str]=..., resource: _Optional[str]=..., role_bindings: _Optional[_Iterable[_Union[PrivilegedAccess.GcpIamAccess.RoleBinding, _Mapping]]]=...) -> None:
            ...
    GCP_IAM_ACCESS_FIELD_NUMBER: _ClassVar[int]
    gcp_iam_access: PrivilegedAccess.GcpIamAccess

    def __init__(self, gcp_iam_access: _Optional[_Union[PrivilegedAccess.GcpIamAccess, _Mapping]]=...) -> None:
        ...

class ListEntitlementsRequest(_message.Message):
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

class ListEntitlementsResponse(_message.Message):
    __slots__ = ('entitlements', 'next_page_token', 'unreachable')
    ENTITLEMENTS_FIELD_NUMBER: _ClassVar[int]
    NEXT_PAGE_TOKEN_FIELD_NUMBER: _ClassVar[int]
    UNREACHABLE_FIELD_NUMBER: _ClassVar[int]
    entitlements: _containers.RepeatedCompositeFieldContainer[Entitlement]
    next_page_token: str
    unreachable: _containers.RepeatedScalarFieldContainer[str]

    def __init__(self, entitlements: _Optional[_Iterable[_Union[Entitlement, _Mapping]]]=..., next_page_token: _Optional[str]=..., unreachable: _Optional[_Iterable[str]]=...) -> None:
        ...

class SearchEntitlementsRequest(_message.Message):
    __slots__ = ('parent', 'caller_access_type', 'filter', 'page_size', 'page_token')

    class CallerAccessType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        CALLER_ACCESS_TYPE_UNSPECIFIED: _ClassVar[SearchEntitlementsRequest.CallerAccessType]
        GRANT_REQUESTER: _ClassVar[SearchEntitlementsRequest.CallerAccessType]
        GRANT_APPROVER: _ClassVar[SearchEntitlementsRequest.CallerAccessType]
    CALLER_ACCESS_TYPE_UNSPECIFIED: SearchEntitlementsRequest.CallerAccessType
    GRANT_REQUESTER: SearchEntitlementsRequest.CallerAccessType
    GRANT_APPROVER: SearchEntitlementsRequest.CallerAccessType
    PARENT_FIELD_NUMBER: _ClassVar[int]
    CALLER_ACCESS_TYPE_FIELD_NUMBER: _ClassVar[int]
    FILTER_FIELD_NUMBER: _ClassVar[int]
    PAGE_SIZE_FIELD_NUMBER: _ClassVar[int]
    PAGE_TOKEN_FIELD_NUMBER: _ClassVar[int]
    parent: str
    caller_access_type: SearchEntitlementsRequest.CallerAccessType
    filter: str
    page_size: int
    page_token: str

    def __init__(self, parent: _Optional[str]=..., caller_access_type: _Optional[_Union[SearchEntitlementsRequest.CallerAccessType, str]]=..., filter: _Optional[str]=..., page_size: _Optional[int]=..., page_token: _Optional[str]=...) -> None:
        ...

class SearchEntitlementsResponse(_message.Message):
    __slots__ = ('entitlements', 'next_page_token')
    ENTITLEMENTS_FIELD_NUMBER: _ClassVar[int]
    NEXT_PAGE_TOKEN_FIELD_NUMBER: _ClassVar[int]
    entitlements: _containers.RepeatedCompositeFieldContainer[Entitlement]
    next_page_token: str

    def __init__(self, entitlements: _Optional[_Iterable[_Union[Entitlement, _Mapping]]]=..., next_page_token: _Optional[str]=...) -> None:
        ...

class GetEntitlementRequest(_message.Message):
    __slots__ = ('name',)
    NAME_FIELD_NUMBER: _ClassVar[int]
    name: str

    def __init__(self, name: _Optional[str]=...) -> None:
        ...

class CreateEntitlementRequest(_message.Message):
    __slots__ = ('parent', 'entitlement_id', 'entitlement', 'request_id')
    PARENT_FIELD_NUMBER: _ClassVar[int]
    ENTITLEMENT_ID_FIELD_NUMBER: _ClassVar[int]
    ENTITLEMENT_FIELD_NUMBER: _ClassVar[int]
    REQUEST_ID_FIELD_NUMBER: _ClassVar[int]
    parent: str
    entitlement_id: str
    entitlement: Entitlement
    request_id: str

    def __init__(self, parent: _Optional[str]=..., entitlement_id: _Optional[str]=..., entitlement: _Optional[_Union[Entitlement, _Mapping]]=..., request_id: _Optional[str]=...) -> None:
        ...

class DeleteEntitlementRequest(_message.Message):
    __slots__ = ('name', 'request_id', 'force')
    NAME_FIELD_NUMBER: _ClassVar[int]
    REQUEST_ID_FIELD_NUMBER: _ClassVar[int]
    FORCE_FIELD_NUMBER: _ClassVar[int]
    name: str
    request_id: str
    force: bool

    def __init__(self, name: _Optional[str]=..., request_id: _Optional[str]=..., force: bool=...) -> None:
        ...

class UpdateEntitlementRequest(_message.Message):
    __slots__ = ('entitlement', 'update_mask')
    ENTITLEMENT_FIELD_NUMBER: _ClassVar[int]
    UPDATE_MASK_FIELD_NUMBER: _ClassVar[int]
    entitlement: Entitlement
    update_mask: _field_mask_pb2.FieldMask

    def __init__(self, entitlement: _Optional[_Union[Entitlement, _Mapping]]=..., update_mask: _Optional[_Union[_field_mask_pb2.FieldMask, _Mapping]]=...) -> None:
        ...

class Grant(_message.Message):
    __slots__ = ('name', 'create_time', 'update_time', 'requester', 'requested_duration', 'justification', 'state', 'timeline', 'privileged_access', 'audit_trail', 'additional_email_recipients', 'externally_modified')

    class State(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        STATE_UNSPECIFIED: _ClassVar[Grant.State]
        APPROVAL_AWAITED: _ClassVar[Grant.State]
        DENIED: _ClassVar[Grant.State]
        SCHEDULED: _ClassVar[Grant.State]
        ACTIVATING: _ClassVar[Grant.State]
        ACTIVE: _ClassVar[Grant.State]
        ACTIVATION_FAILED: _ClassVar[Grant.State]
        EXPIRED: _ClassVar[Grant.State]
        REVOKING: _ClassVar[Grant.State]
        REVOKED: _ClassVar[Grant.State]
        ENDED: _ClassVar[Grant.State]
    STATE_UNSPECIFIED: Grant.State
    APPROVAL_AWAITED: Grant.State
    DENIED: Grant.State
    SCHEDULED: Grant.State
    ACTIVATING: Grant.State
    ACTIVE: Grant.State
    ACTIVATION_FAILED: Grant.State
    EXPIRED: Grant.State
    REVOKING: Grant.State
    REVOKED: Grant.State
    ENDED: Grant.State

    class Timeline(_message.Message):
        __slots__ = ('events',)

        class Event(_message.Message):
            __slots__ = ('requested', 'approved', 'denied', 'revoked', 'scheduled', 'activated', 'activation_failed', 'expired', 'ended', 'externally_modified', 'event_time')

            class Requested(_message.Message):
                __slots__ = ('expire_time',)
                EXPIRE_TIME_FIELD_NUMBER: _ClassVar[int]
                expire_time: _timestamp_pb2.Timestamp

                def __init__(self, expire_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]]=...) -> None:
                    ...

            class Approved(_message.Message):
                __slots__ = ('reason', 'actor')
                REASON_FIELD_NUMBER: _ClassVar[int]
                ACTOR_FIELD_NUMBER: _ClassVar[int]
                reason: str
                actor: str

                def __init__(self, reason: _Optional[str]=..., actor: _Optional[str]=...) -> None:
                    ...

            class Denied(_message.Message):
                __slots__ = ('reason', 'actor')
                REASON_FIELD_NUMBER: _ClassVar[int]
                ACTOR_FIELD_NUMBER: _ClassVar[int]
                reason: str
                actor: str

                def __init__(self, reason: _Optional[str]=..., actor: _Optional[str]=...) -> None:
                    ...

            class Revoked(_message.Message):
                __slots__ = ('reason', 'actor')
                REASON_FIELD_NUMBER: _ClassVar[int]
                ACTOR_FIELD_NUMBER: _ClassVar[int]
                reason: str
                actor: str

                def __init__(self, reason: _Optional[str]=..., actor: _Optional[str]=...) -> None:
                    ...

            class Scheduled(_message.Message):
                __slots__ = ('scheduled_activation_time',)
                SCHEDULED_ACTIVATION_TIME_FIELD_NUMBER: _ClassVar[int]
                scheduled_activation_time: _timestamp_pb2.Timestamp

                def __init__(self, scheduled_activation_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]]=...) -> None:
                    ...

            class Activated(_message.Message):
                __slots__ = ()

                def __init__(self) -> None:
                    ...

            class ActivationFailed(_message.Message):
                __slots__ = ('error',)
                ERROR_FIELD_NUMBER: _ClassVar[int]
                error: _status_pb2.Status

                def __init__(self, error: _Optional[_Union[_status_pb2.Status, _Mapping]]=...) -> None:
                    ...

            class Expired(_message.Message):
                __slots__ = ()

                def __init__(self) -> None:
                    ...

            class Ended(_message.Message):
                __slots__ = ()

                def __init__(self) -> None:
                    ...

            class ExternallyModified(_message.Message):
                __slots__ = ()

                def __init__(self) -> None:
                    ...
            REQUESTED_FIELD_NUMBER: _ClassVar[int]
            APPROVED_FIELD_NUMBER: _ClassVar[int]
            DENIED_FIELD_NUMBER: _ClassVar[int]
            REVOKED_FIELD_NUMBER: _ClassVar[int]
            SCHEDULED_FIELD_NUMBER: _ClassVar[int]
            ACTIVATED_FIELD_NUMBER: _ClassVar[int]
            ACTIVATION_FAILED_FIELD_NUMBER: _ClassVar[int]
            EXPIRED_FIELD_NUMBER: _ClassVar[int]
            ENDED_FIELD_NUMBER: _ClassVar[int]
            EXTERNALLY_MODIFIED_FIELD_NUMBER: _ClassVar[int]
            EVENT_TIME_FIELD_NUMBER: _ClassVar[int]
            requested: Grant.Timeline.Event.Requested
            approved: Grant.Timeline.Event.Approved
            denied: Grant.Timeline.Event.Denied
            revoked: Grant.Timeline.Event.Revoked
            scheduled: Grant.Timeline.Event.Scheduled
            activated: Grant.Timeline.Event.Activated
            activation_failed: Grant.Timeline.Event.ActivationFailed
            expired: Grant.Timeline.Event.Expired
            ended: Grant.Timeline.Event.Ended
            externally_modified: Grant.Timeline.Event.ExternallyModified
            event_time: _timestamp_pb2.Timestamp

            def __init__(self, requested: _Optional[_Union[Grant.Timeline.Event.Requested, _Mapping]]=..., approved: _Optional[_Union[Grant.Timeline.Event.Approved, _Mapping]]=..., denied: _Optional[_Union[Grant.Timeline.Event.Denied, _Mapping]]=..., revoked: _Optional[_Union[Grant.Timeline.Event.Revoked, _Mapping]]=..., scheduled: _Optional[_Union[Grant.Timeline.Event.Scheduled, _Mapping]]=..., activated: _Optional[_Union[Grant.Timeline.Event.Activated, _Mapping]]=..., activation_failed: _Optional[_Union[Grant.Timeline.Event.ActivationFailed, _Mapping]]=..., expired: _Optional[_Union[Grant.Timeline.Event.Expired, _Mapping]]=..., ended: _Optional[_Union[Grant.Timeline.Event.Ended, _Mapping]]=..., externally_modified: _Optional[_Union[Grant.Timeline.Event.ExternallyModified, _Mapping]]=..., event_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]]=...) -> None:
                ...
        EVENTS_FIELD_NUMBER: _ClassVar[int]
        events: _containers.RepeatedCompositeFieldContainer[Grant.Timeline.Event]

        def __init__(self, events: _Optional[_Iterable[_Union[Grant.Timeline.Event, _Mapping]]]=...) -> None:
            ...

    class AuditTrail(_message.Message):
        __slots__ = ('access_grant_time', 'access_remove_time')
        ACCESS_GRANT_TIME_FIELD_NUMBER: _ClassVar[int]
        ACCESS_REMOVE_TIME_FIELD_NUMBER: _ClassVar[int]
        access_grant_time: _timestamp_pb2.Timestamp
        access_remove_time: _timestamp_pb2.Timestamp

        def __init__(self, access_grant_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]]=..., access_remove_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]]=...) -> None:
            ...
    NAME_FIELD_NUMBER: _ClassVar[int]
    CREATE_TIME_FIELD_NUMBER: _ClassVar[int]
    UPDATE_TIME_FIELD_NUMBER: _ClassVar[int]
    REQUESTER_FIELD_NUMBER: _ClassVar[int]
    REQUESTED_DURATION_FIELD_NUMBER: _ClassVar[int]
    JUSTIFICATION_FIELD_NUMBER: _ClassVar[int]
    STATE_FIELD_NUMBER: _ClassVar[int]
    TIMELINE_FIELD_NUMBER: _ClassVar[int]
    PRIVILEGED_ACCESS_FIELD_NUMBER: _ClassVar[int]
    AUDIT_TRAIL_FIELD_NUMBER: _ClassVar[int]
    ADDITIONAL_EMAIL_RECIPIENTS_FIELD_NUMBER: _ClassVar[int]
    EXTERNALLY_MODIFIED_FIELD_NUMBER: _ClassVar[int]
    name: str
    create_time: _timestamp_pb2.Timestamp
    update_time: _timestamp_pb2.Timestamp
    requester: str
    requested_duration: _duration_pb2.Duration
    justification: Justification
    state: Grant.State
    timeline: Grant.Timeline
    privileged_access: PrivilegedAccess
    audit_trail: Grant.AuditTrail
    additional_email_recipients: _containers.RepeatedScalarFieldContainer[str]
    externally_modified: bool

    def __init__(self, name: _Optional[str]=..., create_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]]=..., update_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]]=..., requester: _Optional[str]=..., requested_duration: _Optional[_Union[_duration_pb2.Duration, _Mapping]]=..., justification: _Optional[_Union[Justification, _Mapping]]=..., state: _Optional[_Union[Grant.State, str]]=..., timeline: _Optional[_Union[Grant.Timeline, _Mapping]]=..., privileged_access: _Optional[_Union[PrivilegedAccess, _Mapping]]=..., audit_trail: _Optional[_Union[Grant.AuditTrail, _Mapping]]=..., additional_email_recipients: _Optional[_Iterable[str]]=..., externally_modified: bool=...) -> None:
        ...

class Justification(_message.Message):
    __slots__ = ('unstructured_justification',)
    UNSTRUCTURED_JUSTIFICATION_FIELD_NUMBER: _ClassVar[int]
    unstructured_justification: str

    def __init__(self, unstructured_justification: _Optional[str]=...) -> None:
        ...

class ListGrantsRequest(_message.Message):
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

class ListGrantsResponse(_message.Message):
    __slots__ = ('grants', 'next_page_token', 'unreachable')
    GRANTS_FIELD_NUMBER: _ClassVar[int]
    NEXT_PAGE_TOKEN_FIELD_NUMBER: _ClassVar[int]
    UNREACHABLE_FIELD_NUMBER: _ClassVar[int]
    grants: _containers.RepeatedCompositeFieldContainer[Grant]
    next_page_token: str
    unreachable: _containers.RepeatedScalarFieldContainer[str]

    def __init__(self, grants: _Optional[_Iterable[_Union[Grant, _Mapping]]]=..., next_page_token: _Optional[str]=..., unreachable: _Optional[_Iterable[str]]=...) -> None:
        ...

class SearchGrantsRequest(_message.Message):
    __slots__ = ('parent', 'caller_relationship', 'filter', 'page_size', 'page_token')

    class CallerRelationshipType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        CALLER_RELATIONSHIP_TYPE_UNSPECIFIED: _ClassVar[SearchGrantsRequest.CallerRelationshipType]
        HAD_CREATED: _ClassVar[SearchGrantsRequest.CallerRelationshipType]
        CAN_APPROVE: _ClassVar[SearchGrantsRequest.CallerRelationshipType]
        HAD_APPROVED: _ClassVar[SearchGrantsRequest.CallerRelationshipType]
    CALLER_RELATIONSHIP_TYPE_UNSPECIFIED: SearchGrantsRequest.CallerRelationshipType
    HAD_CREATED: SearchGrantsRequest.CallerRelationshipType
    CAN_APPROVE: SearchGrantsRequest.CallerRelationshipType
    HAD_APPROVED: SearchGrantsRequest.CallerRelationshipType
    PARENT_FIELD_NUMBER: _ClassVar[int]
    CALLER_RELATIONSHIP_FIELD_NUMBER: _ClassVar[int]
    FILTER_FIELD_NUMBER: _ClassVar[int]
    PAGE_SIZE_FIELD_NUMBER: _ClassVar[int]
    PAGE_TOKEN_FIELD_NUMBER: _ClassVar[int]
    parent: str
    caller_relationship: SearchGrantsRequest.CallerRelationshipType
    filter: str
    page_size: int
    page_token: str

    def __init__(self, parent: _Optional[str]=..., caller_relationship: _Optional[_Union[SearchGrantsRequest.CallerRelationshipType, str]]=..., filter: _Optional[str]=..., page_size: _Optional[int]=..., page_token: _Optional[str]=...) -> None:
        ...

class SearchGrantsResponse(_message.Message):
    __slots__ = ('grants', 'next_page_token')
    GRANTS_FIELD_NUMBER: _ClassVar[int]
    NEXT_PAGE_TOKEN_FIELD_NUMBER: _ClassVar[int]
    grants: _containers.RepeatedCompositeFieldContainer[Grant]
    next_page_token: str

    def __init__(self, grants: _Optional[_Iterable[_Union[Grant, _Mapping]]]=..., next_page_token: _Optional[str]=...) -> None:
        ...

class GetGrantRequest(_message.Message):
    __slots__ = ('name',)
    NAME_FIELD_NUMBER: _ClassVar[int]
    name: str

    def __init__(self, name: _Optional[str]=...) -> None:
        ...

class ApproveGrantRequest(_message.Message):
    __slots__ = ('name', 'reason')
    NAME_FIELD_NUMBER: _ClassVar[int]
    REASON_FIELD_NUMBER: _ClassVar[int]
    name: str
    reason: str

    def __init__(self, name: _Optional[str]=..., reason: _Optional[str]=...) -> None:
        ...

class DenyGrantRequest(_message.Message):
    __slots__ = ('name', 'reason')
    NAME_FIELD_NUMBER: _ClassVar[int]
    REASON_FIELD_NUMBER: _ClassVar[int]
    name: str
    reason: str

    def __init__(self, name: _Optional[str]=..., reason: _Optional[str]=...) -> None:
        ...

class RevokeGrantRequest(_message.Message):
    __slots__ = ('name', 'reason')
    NAME_FIELD_NUMBER: _ClassVar[int]
    REASON_FIELD_NUMBER: _ClassVar[int]
    name: str
    reason: str

    def __init__(self, name: _Optional[str]=..., reason: _Optional[str]=...) -> None:
        ...

class CreateGrantRequest(_message.Message):
    __slots__ = ('parent', 'grant', 'request_id')
    PARENT_FIELD_NUMBER: _ClassVar[int]
    GRANT_FIELD_NUMBER: _ClassVar[int]
    REQUEST_ID_FIELD_NUMBER: _ClassVar[int]
    parent: str
    grant: Grant
    request_id: str

    def __init__(self, parent: _Optional[str]=..., grant: _Optional[_Union[Grant, _Mapping]]=..., request_id: _Optional[str]=...) -> None:
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