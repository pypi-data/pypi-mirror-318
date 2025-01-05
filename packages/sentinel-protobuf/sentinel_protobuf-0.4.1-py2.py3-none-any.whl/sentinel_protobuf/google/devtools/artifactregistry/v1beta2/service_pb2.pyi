from google.api import annotations_pb2 as _annotations_pb2
from google.api import client_pb2 as _client_pb2
from google.devtools.artifactregistry.v1beta2 import apt_artifact_pb2 as _apt_artifact_pb2
from google.devtools.artifactregistry.v1beta2 import file_pb2 as _file_pb2
from google.devtools.artifactregistry.v1beta2 import package_pb2 as _package_pb2
from google.devtools.artifactregistry.v1beta2 import repository_pb2 as _repository_pb2
from google.devtools.artifactregistry.v1beta2 import settings_pb2 as _settings_pb2
from google.devtools.artifactregistry.v1beta2 import tag_pb2 as _tag_pb2
from google.devtools.artifactregistry.v1beta2 import version_pb2 as _version_pb2
from google.devtools.artifactregistry.v1beta2 import yum_artifact_pb2 as _yum_artifact_pb2
from google.iam.v1 import iam_policy_pb2 as _iam_policy_pb2
from google.iam.v1 import policy_pb2 as _policy_pb2
from google.longrunning import operations_pb2 as _operations_pb2
from google.protobuf import empty_pb2 as _empty_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar
DESCRIPTOR: _descriptor.FileDescriptor

class OperationMetadata(_message.Message):
    __slots__ = ()

    def __init__(self) -> None:
        ...