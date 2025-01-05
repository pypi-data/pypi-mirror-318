from google.ads.googleads.v18.enums import access_invitation_status_pb2 as _access_invitation_status_pb2
from google.ads.googleads.v18.enums import access_role_pb2 as _access_role_pb2
from google.api import field_behavior_pb2 as _field_behavior_pb2
from google.api import resource_pb2 as _resource_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union
DESCRIPTOR: _descriptor.FileDescriptor

class CustomerUserAccessInvitation(_message.Message):
    __slots__ = ('resource_name', 'invitation_id', 'access_role', 'email_address', 'creation_date_time', 'invitation_status')
    RESOURCE_NAME_FIELD_NUMBER: _ClassVar[int]
    INVITATION_ID_FIELD_NUMBER: _ClassVar[int]
    ACCESS_ROLE_FIELD_NUMBER: _ClassVar[int]
    EMAIL_ADDRESS_FIELD_NUMBER: _ClassVar[int]
    CREATION_DATE_TIME_FIELD_NUMBER: _ClassVar[int]
    INVITATION_STATUS_FIELD_NUMBER: _ClassVar[int]
    resource_name: str
    invitation_id: int
    access_role: _access_role_pb2.AccessRoleEnum.AccessRole
    email_address: str
    creation_date_time: str
    invitation_status: _access_invitation_status_pb2.AccessInvitationStatusEnum.AccessInvitationStatus

    def __init__(self, resource_name: _Optional[str]=..., invitation_id: _Optional[int]=..., access_role: _Optional[_Union[_access_role_pb2.AccessRoleEnum.AccessRole, str]]=..., email_address: _Optional[str]=..., creation_date_time: _Optional[str]=..., invitation_status: _Optional[_Union[_access_invitation_status_pb2.AccessInvitationStatusEnum.AccessInvitationStatus, str]]=...) -> None:
        ...