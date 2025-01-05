from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar
DESCRIPTOR: _descriptor.FileDescriptor

class StructuredSnippetPlaceholderFieldEnum(_message.Message):
    __slots__ = ()

    class StructuredSnippetPlaceholderField(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        UNSPECIFIED: _ClassVar[StructuredSnippetPlaceholderFieldEnum.StructuredSnippetPlaceholderField]
        UNKNOWN: _ClassVar[StructuredSnippetPlaceholderFieldEnum.StructuredSnippetPlaceholderField]
        HEADER: _ClassVar[StructuredSnippetPlaceholderFieldEnum.StructuredSnippetPlaceholderField]
        SNIPPETS: _ClassVar[StructuredSnippetPlaceholderFieldEnum.StructuredSnippetPlaceholderField]
    UNSPECIFIED: StructuredSnippetPlaceholderFieldEnum.StructuredSnippetPlaceholderField
    UNKNOWN: StructuredSnippetPlaceholderFieldEnum.StructuredSnippetPlaceholderField
    HEADER: StructuredSnippetPlaceholderFieldEnum.StructuredSnippetPlaceholderField
    SNIPPETS: StructuredSnippetPlaceholderFieldEnum.StructuredSnippetPlaceholderField

    def __init__(self) -> None:
        ...