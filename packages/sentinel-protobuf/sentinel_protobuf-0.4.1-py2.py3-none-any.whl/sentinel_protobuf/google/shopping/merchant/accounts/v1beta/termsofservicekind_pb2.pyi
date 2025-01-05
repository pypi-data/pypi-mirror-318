from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from typing import ClassVar as _ClassVar
DESCRIPTOR: _descriptor.FileDescriptor

class TermsOfServiceKind(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    TERMS_OF_SERVICE_KIND_UNSPECIFIED: _ClassVar[TermsOfServiceKind]
    MERCHANT_CENTER: _ClassVar[TermsOfServiceKind]
TERMS_OF_SERVICE_KIND_UNSPECIFIED: TermsOfServiceKind
MERCHANT_CENTER: TermsOfServiceKind