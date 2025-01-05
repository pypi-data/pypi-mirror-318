from google.apps.script.type import extension_point_pb2 as _extension_point_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Mapping as _Mapping, Optional as _Optional, Union as _Union
DESCRIPTOR: _descriptor.FileDescriptor

class DriveAddOnManifest(_message.Message):
    __slots__ = ('homepage_trigger', 'on_items_selected_trigger')
    HOMEPAGE_TRIGGER_FIELD_NUMBER: _ClassVar[int]
    ON_ITEMS_SELECTED_TRIGGER_FIELD_NUMBER: _ClassVar[int]
    homepage_trigger: _extension_point_pb2.HomepageExtensionPoint
    on_items_selected_trigger: DriveExtensionPoint

    def __init__(self, homepage_trigger: _Optional[_Union[_extension_point_pb2.HomepageExtensionPoint, _Mapping]]=..., on_items_selected_trigger: _Optional[_Union[DriveExtensionPoint, _Mapping]]=...) -> None:
        ...

class DriveExtensionPoint(_message.Message):
    __slots__ = ('run_function',)
    RUN_FUNCTION_FIELD_NUMBER: _ClassVar[int]
    run_function: str

    def __init__(self, run_function: _Optional[str]=...) -> None:
        ...