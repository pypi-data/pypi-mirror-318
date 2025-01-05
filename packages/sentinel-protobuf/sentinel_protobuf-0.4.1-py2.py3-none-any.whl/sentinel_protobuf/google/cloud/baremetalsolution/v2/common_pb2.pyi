from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from typing import ClassVar as _ClassVar
DESCRIPTOR: _descriptor.FileDescriptor

class VolumePerformanceTier(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    VOLUME_PERFORMANCE_TIER_UNSPECIFIED: _ClassVar[VolumePerformanceTier]
    VOLUME_PERFORMANCE_TIER_SHARED: _ClassVar[VolumePerformanceTier]
    VOLUME_PERFORMANCE_TIER_ASSIGNED: _ClassVar[VolumePerformanceTier]
    VOLUME_PERFORMANCE_TIER_HT: _ClassVar[VolumePerformanceTier]

class WorkloadProfile(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    WORKLOAD_PROFILE_UNSPECIFIED: _ClassVar[WorkloadProfile]
    WORKLOAD_PROFILE_GENERIC: _ClassVar[WorkloadProfile]
    WORKLOAD_PROFILE_HANA: _ClassVar[WorkloadProfile]
VOLUME_PERFORMANCE_TIER_UNSPECIFIED: VolumePerformanceTier
VOLUME_PERFORMANCE_TIER_SHARED: VolumePerformanceTier
VOLUME_PERFORMANCE_TIER_ASSIGNED: VolumePerformanceTier
VOLUME_PERFORMANCE_TIER_HT: VolumePerformanceTier
WORKLOAD_PROFILE_UNSPECIFIED: WorkloadProfile
WORKLOAD_PROFILE_GENERIC: WorkloadProfile
WORKLOAD_PROFILE_HANA: WorkloadProfile