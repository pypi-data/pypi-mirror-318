from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Mapping as _Mapping, Optional as _Optional, Union as _Union
DESCRIPTOR: _descriptor.FileDescriptor

class AutoMlTextClassification(_message.Message):
    __slots__ = ('inputs',)
    INPUTS_FIELD_NUMBER: _ClassVar[int]
    inputs: AutoMlTextClassificationInputs

    def __init__(self, inputs: _Optional[_Union[AutoMlTextClassificationInputs, _Mapping]]=...) -> None:
        ...

class AutoMlTextClassificationInputs(_message.Message):
    __slots__ = ('multi_label',)
    MULTI_LABEL_FIELD_NUMBER: _ClassVar[int]
    multi_label: bool

    def __init__(self, multi_label: bool=...) -> None:
        ...