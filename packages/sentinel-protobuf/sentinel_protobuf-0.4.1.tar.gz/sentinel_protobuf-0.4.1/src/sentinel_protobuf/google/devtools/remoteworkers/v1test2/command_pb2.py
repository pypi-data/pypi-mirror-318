"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_runtime_version.ValidateProtobufRuntimeVersion(_runtime_version.Domain.PUBLIC, 5, 28, 1, '', 'google/devtools/remoteworkers/v1test2/command.proto')
_sym_db = _symbol_database.Default()
from google.protobuf import any_pb2 as google_dot_protobuf_dot_any__pb2
from google.protobuf import duration_pb2 as google_dot_protobuf_dot_duration__pb2
from .....google.rpc import status_pb2 as google_dot_rpc_dot_status__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n3google/devtools/remoteworkers/v1test2/command.proto\x12%google.devtools.remoteworkers.v1test2\x1a\x19google/protobuf/any.proto\x1a\x1egoogle/protobuf/duration.proto\x1a\x17google/rpc/status.proto"\xd1\x06\n\x0bCommandTask\x12I\n\x06inputs\x18\x01 \x01(\x0b29.google.devtools.remoteworkers.v1test2.CommandTask.Inputs\x12T\n\x10expected_outputs\x18\x04 \x01(\x0b2:.google.devtools.remoteworkers.v1test2.CommandTask.Outputs\x12M\n\x08timeouts\x18\x05 \x01(\x0b2;.google.devtools.remoteworkers.v1test2.CommandTask.Timeouts\x1a\xd9\x02\n\x06Inputs\x12\x11\n\targuments\x18\x01 \x03(\t\x12<\n\x05files\x18\x02 \x03(\x0b2-.google.devtools.remoteworkers.v1test2.Digest\x12A\n\x0cinline_blobs\x18\x04 \x03(\x0b2+.google.devtools.remoteworkers.v1test2.Blob\x12l\n\x15environment_variables\x18\x03 \x03(\x0b2M.google.devtools.remoteworkers.v1test2.CommandTask.Inputs.EnvironmentVariable\x12\x19\n\x11working_directory\x18\x05 \x01(\t\x1a2\n\x13EnvironmentVariable\x12\x0c\n\x04name\x18\x01 \x01(\t\x12\r\n\x05value\x18\x02 \x01(\t\x1ae\n\x07Outputs\x12\r\n\x05files\x18\x01 \x03(\t\x12\x13\n\x0bdirectories\x18\x02 \x03(\t\x12\x1a\n\x12stdout_destination\x18\x03 \x01(\t\x12\x1a\n\x12stderr_destination\x18\x04 \x01(\t\x1a\x8e\x01\n\x08Timeouts\x12,\n\texecution\x18\x01 \x01(\x0b2\x19.google.protobuf.Duration\x12\'\n\x04idle\x18\x02 \x01(\x0b2\x19.google.protobuf.Duration\x12+\n\x08shutdown\x18\x03 \x01(\x0b2\x19.google.protobuf.Duration"c\n\x0eCommandOutputs\x12\x11\n\texit_code\x18\x01 \x01(\x05\x12>\n\x07outputs\x18\x02 \x01(\x0b2-.google.devtools.remoteworkers.v1test2.Digest"k\n\x0fCommandOverhead\x12+\n\x08duration\x18\x01 \x01(\x0b2\x19.google.protobuf.Duration\x12+\n\x08overhead\x18\x02 \x01(\x0b2\x19.google.protobuf.Duration"\x90\x02\n\rCommandResult\x12"\n\x06status\x18\x01 \x01(\x0b2\x12.google.rpc.Status\x12\x11\n\texit_code\x18\x02 \x01(\x05\x12>\n\x07outputs\x18\x03 \x01(\x0b2-.google.devtools.remoteworkers.v1test2.Digest\x12/\n\x08duration\x18\x04 \x01(\x0b2\x19.google.protobuf.DurationB\x02\x18\x01\x12/\n\x08overhead\x18\x05 \x01(\x0b2\x19.google.protobuf.DurationB\x02\x18\x01\x12&\n\x08metadata\x18\x06 \x03(\x0b2\x14.google.protobuf.Any"\x84\x01\n\x0cFileMetadata\x12\x0c\n\x04path\x18\x01 \x01(\t\x12=\n\x06digest\x18\x02 \x01(\x0b2-.google.devtools.remoteworkers.v1test2.Digest\x12\x10\n\x08contents\x18\x03 \x01(\x0c\x12\x15\n\ris_executable\x18\x04 \x01(\x08"`\n\x11DirectoryMetadata\x12\x0c\n\x04path\x18\x01 \x01(\t\x12=\n\x06digest\x18\x02 \x01(\x0b2-.google.devtools.remoteworkers.v1test2.Digest"*\n\x06Digest\x12\x0c\n\x04hash\x18\x01 \x01(\t\x12\x12\n\nsize_bytes\x18\x02 \x01(\x03"W\n\x04Blob\x12=\n\x06digest\x18\x01 \x01(\x0b2-.google.devtools.remoteworkers.v1test2.Digest\x12\x10\n\x08contents\x18\x02 \x01(\x0c"\x9e\x01\n\tDirectory\x12B\n\x05files\x18\x01 \x03(\x0b23.google.devtools.remoteworkers.v1test2.FileMetadata\x12M\n\x0bdirectories\x18\x02 \x03(\x0b28.google.devtools.remoteworkers.v1test2.DirectoryMetadataB\xea\x01\n)com.google.devtools.remoteworkers.v1test2B\x15RemoteWorkersCommandsP\x01ZRgoogle.golang.org/genproto/googleapis/devtools/remoteworkers/v1test2;remoteworkers\xa2\x02\x02RW\xaa\x02%Google.DevTools.RemoteWorkers.V1Test2\xca\x02"Google\\Cloud\\Remoteworkers\\V1test2b\x06proto3')
_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'google.devtools.remoteworkers.v1test2.command_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
    _globals['DESCRIPTOR']._loaded_options = None
    _globals['DESCRIPTOR']._serialized_options = b'\n)com.google.devtools.remoteworkers.v1test2B\x15RemoteWorkersCommandsP\x01ZRgoogle.golang.org/genproto/googleapis/devtools/remoteworkers/v1test2;remoteworkers\xa2\x02\x02RW\xaa\x02%Google.DevTools.RemoteWorkers.V1Test2\xca\x02"Google\\Cloud\\Remoteworkers\\V1test2'
    _globals['_COMMANDRESULT'].fields_by_name['duration']._loaded_options = None
    _globals['_COMMANDRESULT'].fields_by_name['duration']._serialized_options = b'\x18\x01'
    _globals['_COMMANDRESULT'].fields_by_name['overhead']._loaded_options = None
    _globals['_COMMANDRESULT'].fields_by_name['overhead']._serialized_options = b'\x18\x01'
    _globals['_COMMANDTASK']._serialized_start = 179
    _globals['_COMMANDTASK']._serialized_end = 1028
    _globals['_COMMANDTASK_INPUTS']._serialized_start = 435
    _globals['_COMMANDTASK_INPUTS']._serialized_end = 780
    _globals['_COMMANDTASK_INPUTS_ENVIRONMENTVARIABLE']._serialized_start = 730
    _globals['_COMMANDTASK_INPUTS_ENVIRONMENTVARIABLE']._serialized_end = 780
    _globals['_COMMANDTASK_OUTPUTS']._serialized_start = 782
    _globals['_COMMANDTASK_OUTPUTS']._serialized_end = 883
    _globals['_COMMANDTASK_TIMEOUTS']._serialized_start = 886
    _globals['_COMMANDTASK_TIMEOUTS']._serialized_end = 1028
    _globals['_COMMANDOUTPUTS']._serialized_start = 1030
    _globals['_COMMANDOUTPUTS']._serialized_end = 1129
    _globals['_COMMANDOVERHEAD']._serialized_start = 1131
    _globals['_COMMANDOVERHEAD']._serialized_end = 1238
    _globals['_COMMANDRESULT']._serialized_start = 1241
    _globals['_COMMANDRESULT']._serialized_end = 1513
    _globals['_FILEMETADATA']._serialized_start = 1516
    _globals['_FILEMETADATA']._serialized_end = 1648
    _globals['_DIRECTORYMETADATA']._serialized_start = 1650
    _globals['_DIRECTORYMETADATA']._serialized_end = 1746
    _globals['_DIGEST']._serialized_start = 1748
    _globals['_DIGEST']._serialized_end = 1790
    _globals['_BLOB']._serialized_start = 1792
    _globals['_BLOB']._serialized_end = 1879
    _globals['_DIRECTORY']._serialized_start = 1882
    _globals['_DIRECTORY']._serialized_end = 2040