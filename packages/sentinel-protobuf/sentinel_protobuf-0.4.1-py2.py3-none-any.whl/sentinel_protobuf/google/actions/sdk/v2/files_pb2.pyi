from google.actions.sdk.v2 import config_file_pb2 as _config_file_pb2
from google.actions.sdk.v2 import data_file_pb2 as _data_file_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Mapping as _Mapping, Optional as _Optional, Union as _Union
DESCRIPTOR: _descriptor.FileDescriptor

class Files(_message.Message):
    __slots__ = ('config_files', 'data_files')
    CONFIG_FILES_FIELD_NUMBER: _ClassVar[int]
    DATA_FILES_FIELD_NUMBER: _ClassVar[int]
    config_files: _config_file_pb2.ConfigFiles
    data_files: _data_file_pb2.DataFiles

    def __init__(self, config_files: _Optional[_Union[_config_file_pb2.ConfigFiles, _Mapping]]=..., data_files: _Optional[_Union[_data_file_pb2.DataFiles, _Mapping]]=...) -> None:
        ...