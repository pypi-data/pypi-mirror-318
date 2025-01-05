from google.api import field_behavior_pb2 as _field_behavior_pb2
from google.api import resource_pb2 as _resource_pb2
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class Entitlement(_message.Message):
    __slots__ = ("name", "cloud_account_details", "entitlement_id", "state")
    class State(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        STATE_UNSPECIFIED: _ClassVar[Entitlement.State]
        ACCOUNT_NOT_LINKED: _ClassVar[Entitlement.State]
        ACCOUNT_NOT_ACTIVE: _ClassVar[Entitlement.State]
        ACTIVE: _ClassVar[Entitlement.State]
    STATE_UNSPECIFIED: Entitlement.State
    ACCOUNT_NOT_LINKED: Entitlement.State
    ACCOUNT_NOT_ACTIVE: Entitlement.State
    ACTIVE: Entitlement.State
    NAME_FIELD_NUMBER: _ClassVar[int]
    CLOUD_ACCOUNT_DETAILS_FIELD_NUMBER: _ClassVar[int]
    ENTITLEMENT_ID_FIELD_NUMBER: _ClassVar[int]
    STATE_FIELD_NUMBER: _ClassVar[int]
    name: str
    cloud_account_details: CloudAccountDetails
    entitlement_id: str
    state: Entitlement.State
    def __init__(self, name: _Optional[str] = ..., cloud_account_details: _Optional[_Union[CloudAccountDetails, _Mapping]] = ..., entitlement_id: _Optional[str] = ..., state: _Optional[_Union[Entitlement.State, str]] = ...) -> None: ...

class CloudAccountDetails(_message.Message):
    __slots__ = ("cloud_account", "cloud_account_home_region", "link_existing_account_uri", "account_creation_uri")
    CLOUD_ACCOUNT_FIELD_NUMBER: _ClassVar[int]
    CLOUD_ACCOUNT_HOME_REGION_FIELD_NUMBER: _ClassVar[int]
    LINK_EXISTING_ACCOUNT_URI_FIELD_NUMBER: _ClassVar[int]
    ACCOUNT_CREATION_URI_FIELD_NUMBER: _ClassVar[int]
    cloud_account: str
    cloud_account_home_region: str
    link_existing_account_uri: str
    account_creation_uri: str
    def __init__(self, cloud_account: _Optional[str] = ..., cloud_account_home_region: _Optional[str] = ..., link_existing_account_uri: _Optional[str] = ..., account_creation_uri: _Optional[str] = ...) -> None: ...
