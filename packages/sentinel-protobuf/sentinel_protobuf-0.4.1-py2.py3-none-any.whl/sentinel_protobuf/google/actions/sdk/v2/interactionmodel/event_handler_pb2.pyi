from google.actions.sdk.v2.interactionmodel.prompt import static_prompt_pb2 as _static_prompt_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Mapping as _Mapping, Optional as _Optional, Union as _Union
DESCRIPTOR: _descriptor.FileDescriptor

class EventHandler(_message.Message):
    __slots__ = ('webhook_handler', 'static_prompt', 'static_prompt_name')
    WEBHOOK_HANDLER_FIELD_NUMBER: _ClassVar[int]
    STATIC_PROMPT_FIELD_NUMBER: _ClassVar[int]
    STATIC_PROMPT_NAME_FIELD_NUMBER: _ClassVar[int]
    webhook_handler: str
    static_prompt: _static_prompt_pb2.StaticPrompt
    static_prompt_name: str

    def __init__(self, webhook_handler: _Optional[str]=..., static_prompt: _Optional[_Union[_static_prompt_pb2.StaticPrompt, _Mapping]]=..., static_prompt_name: _Optional[str]=...) -> None:
        ...