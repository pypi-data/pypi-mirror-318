from google.api import field_behavior_pb2 as _field_behavior_pb2
from google.api import resource_pb2 as _resource_pb2
from google.protobuf import timestamp_pb2 as _timestamp_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Mapping as _Mapping, Optional as _Optional, Union as _Union
DESCRIPTOR: _descriptor.FileDescriptor

class Environment(_message.Message):
    __slots__ = ('name', 'display_name', 'description', 'vm_image', 'container_image', 'post_startup_script', 'create_time')
    NAME_FIELD_NUMBER: _ClassVar[int]
    DISPLAY_NAME_FIELD_NUMBER: _ClassVar[int]
    DESCRIPTION_FIELD_NUMBER: _ClassVar[int]
    VM_IMAGE_FIELD_NUMBER: _ClassVar[int]
    CONTAINER_IMAGE_FIELD_NUMBER: _ClassVar[int]
    POST_STARTUP_SCRIPT_FIELD_NUMBER: _ClassVar[int]
    CREATE_TIME_FIELD_NUMBER: _ClassVar[int]
    name: str
    display_name: str
    description: str
    vm_image: VmImage
    container_image: ContainerImage
    post_startup_script: str
    create_time: _timestamp_pb2.Timestamp

    def __init__(self, name: _Optional[str]=..., display_name: _Optional[str]=..., description: _Optional[str]=..., vm_image: _Optional[_Union[VmImage, _Mapping]]=..., container_image: _Optional[_Union[ContainerImage, _Mapping]]=..., post_startup_script: _Optional[str]=..., create_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]]=...) -> None:
        ...

class VmImage(_message.Message):
    __slots__ = ('project', 'image_name', 'image_family')
    PROJECT_FIELD_NUMBER: _ClassVar[int]
    IMAGE_NAME_FIELD_NUMBER: _ClassVar[int]
    IMAGE_FAMILY_FIELD_NUMBER: _ClassVar[int]
    project: str
    image_name: str
    image_family: str

    def __init__(self, project: _Optional[str]=..., image_name: _Optional[str]=..., image_family: _Optional[str]=...) -> None:
        ...

class ContainerImage(_message.Message):
    __slots__ = ('repository', 'tag')
    REPOSITORY_FIELD_NUMBER: _ClassVar[int]
    TAG_FIELD_NUMBER: _ClassVar[int]
    repository: str
    tag: str

    def __init__(self, repository: _Optional[str]=..., tag: _Optional[str]=...) -> None:
        ...