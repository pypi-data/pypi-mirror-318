from google.protobuf import wrappers_pb2 as _wrappers_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Mapping as _Mapping, Optional as _Optional, Union as _Union
DESCRIPTOR: _descriptor.FileDescriptor

class MenuItemExtensionPoint(_message.Message):
    __slots__ = ('run_function', 'label', 'logo_url')
    RUN_FUNCTION_FIELD_NUMBER: _ClassVar[int]
    LABEL_FIELD_NUMBER: _ClassVar[int]
    LOGO_URL_FIELD_NUMBER: _ClassVar[int]
    run_function: str
    label: str
    logo_url: str

    def __init__(self, run_function: _Optional[str]=..., label: _Optional[str]=..., logo_url: _Optional[str]=...) -> None:
        ...

class HomepageExtensionPoint(_message.Message):
    __slots__ = ('run_function', 'enabled')
    RUN_FUNCTION_FIELD_NUMBER: _ClassVar[int]
    ENABLED_FIELD_NUMBER: _ClassVar[int]
    run_function: str
    enabled: _wrappers_pb2.BoolValue

    def __init__(self, run_function: _Optional[str]=..., enabled: _Optional[_Union[_wrappers_pb2.BoolValue, _Mapping]]=...) -> None:
        ...

class UniversalActionExtensionPoint(_message.Message):
    __slots__ = ('label', 'open_link', 'run_function')
    LABEL_FIELD_NUMBER: _ClassVar[int]
    OPEN_LINK_FIELD_NUMBER: _ClassVar[int]
    RUN_FUNCTION_FIELD_NUMBER: _ClassVar[int]
    label: str
    open_link: str
    run_function: str

    def __init__(self, label: _Optional[str]=..., open_link: _Optional[str]=..., run_function: _Optional[str]=...) -> None:
        ...