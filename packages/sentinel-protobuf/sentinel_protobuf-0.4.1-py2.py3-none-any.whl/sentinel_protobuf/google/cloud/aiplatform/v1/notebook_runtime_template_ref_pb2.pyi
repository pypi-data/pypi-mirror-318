from google.api import field_behavior_pb2 as _field_behavior_pb2
from google.api import resource_pb2 as _resource_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional
DESCRIPTOR: _descriptor.FileDescriptor

class NotebookRuntimeTemplateRef(_message.Message):
    __slots__ = ('notebook_runtime_template',)
    NOTEBOOK_RUNTIME_TEMPLATE_FIELD_NUMBER: _ClassVar[int]
    notebook_runtime_template: str

    def __init__(self, notebook_runtime_template: _Optional[str]=...) -> None:
        ...