from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from typing import ClassVar as _ClassVar
DESCRIPTOR: _descriptor.FileDescriptor

class AcceleratorType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    ACCELERATOR_TYPE_UNSPECIFIED: _ClassVar[AcceleratorType]
    NVIDIA_TESLA_K80: _ClassVar[AcceleratorType]
    NVIDIA_TESLA_P100: _ClassVar[AcceleratorType]
    NVIDIA_TESLA_V100: _ClassVar[AcceleratorType]
    NVIDIA_TESLA_P4: _ClassVar[AcceleratorType]
    NVIDIA_TESLA_T4: _ClassVar[AcceleratorType]
    NVIDIA_TESLA_A100: _ClassVar[AcceleratorType]
    NVIDIA_A100_80GB: _ClassVar[AcceleratorType]
    NVIDIA_L4: _ClassVar[AcceleratorType]
    NVIDIA_H100_80GB: _ClassVar[AcceleratorType]
    NVIDIA_H100_MEGA_80GB: _ClassVar[AcceleratorType]
    TPU_V2: _ClassVar[AcceleratorType]
    TPU_V3: _ClassVar[AcceleratorType]
    TPU_V4_POD: _ClassVar[AcceleratorType]
    TPU_V5_LITEPOD: _ClassVar[AcceleratorType]
ACCELERATOR_TYPE_UNSPECIFIED: AcceleratorType
NVIDIA_TESLA_K80: AcceleratorType
NVIDIA_TESLA_P100: AcceleratorType
NVIDIA_TESLA_V100: AcceleratorType
NVIDIA_TESLA_P4: AcceleratorType
NVIDIA_TESLA_T4: AcceleratorType
NVIDIA_TESLA_A100: AcceleratorType
NVIDIA_A100_80GB: AcceleratorType
NVIDIA_L4: AcceleratorType
NVIDIA_H100_80GB: AcceleratorType
NVIDIA_H100_MEGA_80GB: AcceleratorType
TPU_V2: AcceleratorType
TPU_V3: AcceleratorType
TPU_V4_POD: AcceleratorType
TPU_V5_LITEPOD: AcceleratorType