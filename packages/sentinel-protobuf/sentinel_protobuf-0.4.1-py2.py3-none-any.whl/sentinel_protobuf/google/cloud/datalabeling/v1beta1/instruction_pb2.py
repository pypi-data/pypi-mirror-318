"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_runtime_version.ValidateProtobufRuntimeVersion(_runtime_version.Domain.PUBLIC, 5, 28, 1, '', 'google/cloud/datalabeling/v1beta1/instruction.proto')
_sym_db = _symbol_database.Default()
from .....google.api import resource_pb2 as google_dot_api_dot_resource__pb2
from .....google.cloud.datalabeling.v1beta1 import dataset_pb2 as google_dot_cloud_dot_datalabeling_dot_v1beta1_dot_dataset__pb2
from google.protobuf import timestamp_pb2 as google_dot_protobuf_dot_timestamp__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n3google/cloud/datalabeling/v1beta1/instruction.proto\x12!google.cloud.datalabeling.v1beta1\x1a\x19google/api/resource.proto\x1a/google/cloud/datalabeling/v1beta1/dataset.proto\x1a\x1fgoogle/protobuf/timestamp.proto"\xfd\x03\n\x0bInstruction\x12\x0c\n\x04name\x18\x01 \x01(\t\x12\x14\n\x0cdisplay_name\x18\x02 \x01(\t\x12\x13\n\x0bdescription\x18\x03 \x01(\t\x12/\n\x0bcreate_time\x18\x04 \x01(\x0b2\x1a.google.protobuf.Timestamp\x12/\n\x0bupdate_time\x18\x05 \x01(\x0b2\x1a.google.protobuf.Timestamp\x12>\n\tdata_type\x18\x06 \x01(\x0e2+.google.cloud.datalabeling.v1beta1.DataType\x12N\n\x0fcsv_instruction\x18\x07 \x01(\x0b21.google.cloud.datalabeling.v1beta1.CsvInstructionB\x02\x18\x01\x12J\n\x0fpdf_instruction\x18\t \x01(\x0b21.google.cloud.datalabeling.v1beta1.PdfInstruction\x12\x1a\n\x12blocking_resources\x18\n \x03(\t:[\xeaAX\n\'datalabeling.googleapis.com/Instruction\x12-projects/{project}/instructions/{instruction}"&\n\x0eCsvInstruction\x12\x14\n\x0cgcs_file_uri\x18\x01 \x01(\t"&\n\x0ePdfInstruction\x12\x14\n\x0cgcs_file_uri\x18\x01 \x01(\tB\xe3\x01\n%com.google.cloud.datalabeling.v1beta1P\x01ZIcloud.google.com/go/datalabeling/apiv1beta1/datalabelingpb;datalabelingpb\xaa\x02!Google.Cloud.DataLabeling.V1Beta1\xca\x02!Google\\Cloud\\DataLabeling\\V1beta1\xea\x02$Google::Cloud::DataLabeling::V1beta1b\x06proto3')
_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'google.cloud.datalabeling.v1beta1.instruction_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
    _globals['DESCRIPTOR']._loaded_options = None
    _globals['DESCRIPTOR']._serialized_options = b'\n%com.google.cloud.datalabeling.v1beta1P\x01ZIcloud.google.com/go/datalabeling/apiv1beta1/datalabelingpb;datalabelingpb\xaa\x02!Google.Cloud.DataLabeling.V1Beta1\xca\x02!Google\\Cloud\\DataLabeling\\V1beta1\xea\x02$Google::Cloud::DataLabeling::V1beta1'
    _globals['_INSTRUCTION'].fields_by_name['csv_instruction']._loaded_options = None
    _globals['_INSTRUCTION'].fields_by_name['csv_instruction']._serialized_options = b'\x18\x01'
    _globals['_INSTRUCTION']._loaded_options = None
    _globals['_INSTRUCTION']._serialized_options = b"\xeaAX\n'datalabeling.googleapis.com/Instruction\x12-projects/{project}/instructions/{instruction}"
    _globals['_INSTRUCTION']._serialized_start = 200
    _globals['_INSTRUCTION']._serialized_end = 709
    _globals['_CSVINSTRUCTION']._serialized_start = 711
    _globals['_CSVINSTRUCTION']._serialized_end = 749
    _globals['_PDFINSTRUCTION']._serialized_start = 751
    _globals['_PDFINSTRUCTION']._serialized_end = 789