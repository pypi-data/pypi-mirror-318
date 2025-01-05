from google.api import resource_pb2 as _resource_pb2
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union
DESCRIPTOR: _descriptor.FileDescriptor

class LabelPermission(_message.Message):
    __slots__ = ('person', 'group', 'audience', 'name', 'email', 'role')

    class LabelRole(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        LABEL_ROLE_UNSPECIFIED: _ClassVar[LabelPermission.LabelRole]
        READER: _ClassVar[LabelPermission.LabelRole]
        APPLIER: _ClassVar[LabelPermission.LabelRole]
        ORGANIZER: _ClassVar[LabelPermission.LabelRole]
        EDITOR: _ClassVar[LabelPermission.LabelRole]
    LABEL_ROLE_UNSPECIFIED: LabelPermission.LabelRole
    READER: LabelPermission.LabelRole
    APPLIER: LabelPermission.LabelRole
    ORGANIZER: LabelPermission.LabelRole
    EDITOR: LabelPermission.LabelRole
    PERSON_FIELD_NUMBER: _ClassVar[int]
    GROUP_FIELD_NUMBER: _ClassVar[int]
    AUDIENCE_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    EMAIL_FIELD_NUMBER: _ClassVar[int]
    ROLE_FIELD_NUMBER: _ClassVar[int]
    person: str
    group: str
    audience: str
    name: str
    email: str
    role: LabelPermission.LabelRole

    def __init__(self, person: _Optional[str]=..., group: _Optional[str]=..., audience: _Optional[str]=..., name: _Optional[str]=..., email: _Optional[str]=..., role: _Optional[_Union[LabelPermission.LabelRole, str]]=...) -> None:
        ...