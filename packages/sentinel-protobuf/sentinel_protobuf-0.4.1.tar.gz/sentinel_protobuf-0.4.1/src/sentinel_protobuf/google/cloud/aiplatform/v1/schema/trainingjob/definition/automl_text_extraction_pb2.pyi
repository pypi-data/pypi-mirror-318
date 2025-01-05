from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Mapping as _Mapping, Optional as _Optional, Union as _Union
DESCRIPTOR: _descriptor.FileDescriptor

class AutoMlTextExtraction(_message.Message):
    __slots__ = ('inputs',)
    INPUTS_FIELD_NUMBER: _ClassVar[int]
    inputs: AutoMlTextExtractionInputs

    def __init__(self, inputs: _Optional[_Union[AutoMlTextExtractionInputs, _Mapping]]=...) -> None:
        ...

class AutoMlTextExtractionInputs(_message.Message):
    __slots__ = ()

    def __init__(self) -> None:
        ...