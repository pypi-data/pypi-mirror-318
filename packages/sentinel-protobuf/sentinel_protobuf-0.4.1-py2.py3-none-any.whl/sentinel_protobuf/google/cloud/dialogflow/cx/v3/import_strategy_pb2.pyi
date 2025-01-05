from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from typing import ClassVar as _ClassVar
DESCRIPTOR: _descriptor.FileDescriptor

class ImportStrategy(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    IMPORT_STRATEGY_UNSPECIFIED: _ClassVar[ImportStrategy]
    IMPORT_STRATEGY_CREATE_NEW: _ClassVar[ImportStrategy]
    IMPORT_STRATEGY_REPLACE: _ClassVar[ImportStrategy]
    IMPORT_STRATEGY_KEEP: _ClassVar[ImportStrategy]
    IMPORT_STRATEGY_MERGE: _ClassVar[ImportStrategy]
    IMPORT_STRATEGY_THROW_ERROR: _ClassVar[ImportStrategy]
IMPORT_STRATEGY_UNSPECIFIED: ImportStrategy
IMPORT_STRATEGY_CREATE_NEW: ImportStrategy
IMPORT_STRATEGY_REPLACE: ImportStrategy
IMPORT_STRATEGY_KEEP: ImportStrategy
IMPORT_STRATEGY_MERGE: ImportStrategy
IMPORT_STRATEGY_THROW_ERROR: ImportStrategy