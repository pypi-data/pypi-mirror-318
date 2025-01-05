from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional
DESCRIPTOR: _descriptor.FileDescriptor

class AccountLinkingSecret(_message.Message):
    __slots__ = ('encrypted_client_secret', 'encryption_key_version')
    ENCRYPTED_CLIENT_SECRET_FIELD_NUMBER: _ClassVar[int]
    ENCRYPTION_KEY_VERSION_FIELD_NUMBER: _ClassVar[int]
    encrypted_client_secret: bytes
    encryption_key_version: str

    def __init__(self, encrypted_client_secret: _Optional[bytes]=..., encryption_key_version: _Optional[str]=...) -> None:
        ...