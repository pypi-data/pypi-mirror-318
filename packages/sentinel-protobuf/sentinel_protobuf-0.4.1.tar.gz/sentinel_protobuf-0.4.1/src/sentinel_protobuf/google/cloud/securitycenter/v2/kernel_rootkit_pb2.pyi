from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional
DESCRIPTOR: _descriptor.FileDescriptor

class KernelRootkit(_message.Message):
    __slots__ = ('name', 'unexpected_code_modification', 'unexpected_read_only_data_modification', 'unexpected_ftrace_handler', 'unexpected_kprobe_handler', 'unexpected_kernel_code_pages', 'unexpected_system_call_handler', 'unexpected_interrupt_handler', 'unexpected_processes_in_runqueue')
    NAME_FIELD_NUMBER: _ClassVar[int]
    UNEXPECTED_CODE_MODIFICATION_FIELD_NUMBER: _ClassVar[int]
    UNEXPECTED_READ_ONLY_DATA_MODIFICATION_FIELD_NUMBER: _ClassVar[int]
    UNEXPECTED_FTRACE_HANDLER_FIELD_NUMBER: _ClassVar[int]
    UNEXPECTED_KPROBE_HANDLER_FIELD_NUMBER: _ClassVar[int]
    UNEXPECTED_KERNEL_CODE_PAGES_FIELD_NUMBER: _ClassVar[int]
    UNEXPECTED_SYSTEM_CALL_HANDLER_FIELD_NUMBER: _ClassVar[int]
    UNEXPECTED_INTERRUPT_HANDLER_FIELD_NUMBER: _ClassVar[int]
    UNEXPECTED_PROCESSES_IN_RUNQUEUE_FIELD_NUMBER: _ClassVar[int]
    name: str
    unexpected_code_modification: bool
    unexpected_read_only_data_modification: bool
    unexpected_ftrace_handler: bool
    unexpected_kprobe_handler: bool
    unexpected_kernel_code_pages: bool
    unexpected_system_call_handler: bool
    unexpected_interrupt_handler: bool
    unexpected_processes_in_runqueue: bool

    def __init__(self, name: _Optional[str]=..., unexpected_code_modification: bool=..., unexpected_read_only_data_modification: bool=..., unexpected_ftrace_handler: bool=..., unexpected_kprobe_handler: bool=..., unexpected_kernel_code_pages: bool=..., unexpected_system_call_handler: bool=..., unexpected_interrupt_handler: bool=..., unexpected_processes_in_runqueue: bool=...) -> None:
        ...