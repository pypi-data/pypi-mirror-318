from google.api import annotations_pb2 as _annotations_pb2
from google.api import client_pb2 as _client_pb2
from google.api import field_behavior_pb2 as _field_behavior_pb2
from google.iam.v1 import iam_policy_pb2 as _iam_policy_pb2
from google.iam.v1 import policy_pb2 as _policy_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union
DESCRIPTOR: _descriptor.FileDescriptor

class GeneratePackagesSummaryRequest(_message.Message):
    __slots__ = ('name',)
    NAME_FIELD_NUMBER: _ClassVar[int]
    name: str

    def __init__(self, name: _Optional[str]=...) -> None:
        ...

class PackagesSummaryResponse(_message.Message):
    __slots__ = ('resource_url', 'licenses_summary')

    class LicensesSummary(_message.Message):
        __slots__ = ('license', 'count')
        LICENSE_FIELD_NUMBER: _ClassVar[int]
        COUNT_FIELD_NUMBER: _ClassVar[int]
        license: str
        count: int

        def __init__(self, license: _Optional[str]=..., count: _Optional[int]=...) -> None:
            ...
    RESOURCE_URL_FIELD_NUMBER: _ClassVar[int]
    LICENSES_SUMMARY_FIELD_NUMBER: _ClassVar[int]
    resource_url: str
    licenses_summary: _containers.RepeatedCompositeFieldContainer[PackagesSummaryResponse.LicensesSummary]

    def __init__(self, resource_url: _Optional[str]=..., licenses_summary: _Optional[_Iterable[_Union[PackagesSummaryResponse.LicensesSummary, _Mapping]]]=...) -> None:
        ...

class ExportSBOMRequest(_message.Message):
    __slots__ = ('name',)
    NAME_FIELD_NUMBER: _ClassVar[int]
    name: str

    def __init__(self, name: _Optional[str]=...) -> None:
        ...

class ExportSBOMResponse(_message.Message):
    __slots__ = ('discovery_occurrence_id',)
    DISCOVERY_OCCURRENCE_ID_FIELD_NUMBER: _ClassVar[int]
    discovery_occurrence_id: str

    def __init__(self, discovery_occurrence_id: _Optional[str]=...) -> None:
        ...