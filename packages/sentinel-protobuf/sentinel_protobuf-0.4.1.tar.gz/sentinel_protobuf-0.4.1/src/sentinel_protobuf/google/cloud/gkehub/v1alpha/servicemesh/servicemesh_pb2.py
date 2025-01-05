"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_runtime_version.ValidateProtobufRuntimeVersion(_runtime_version.Domain.PUBLIC, 5, 28, 1, '', 'google/cloud/gkehub/v1alpha/servicemesh/servicemesh.proto')
_sym_db = _symbol_database.Default()
from ......google.api import field_behavior_pb2 as google_dot_api_dot_field__behavior__pb2
from google.protobuf import struct_pb2 as google_dot_protobuf_dot_struct__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n9google/cloud/gkehub/v1alpha/servicemesh/servicemesh.proto\x12\'google.cloud.gkehub.servicemesh.v1alpha\x1a\x1fgoogle/api/field_behavior.proto\x1a\x1cgoogle/protobuf/struct.proto"h\n\x0cFeatureState\x12X\n\x11analysis_messages\x18\x01 \x03(\x0b28.google.cloud.gkehub.servicemesh.v1alpha.AnalysisMessageB\x03\xe0A\x03"k\n\x0fMembershipState\x12X\n\x11analysis_messages\x18\x01 \x03(\x0b28.google.cloud.gkehub.servicemesh.v1alpha.AnalysisMessageB\x03\xe0A\x03"\xc2\x02\n\x13AnalysisMessageBase\x12O\n\x04type\x18\x01 \x01(\x0b2A.google.cloud.gkehub.servicemesh.v1alpha.AnalysisMessageBase.Type\x12Q\n\x05level\x18\x02 \x01(\x0e2B.google.cloud.gkehub.servicemesh.v1alpha.AnalysisMessageBase.Level\x12\x19\n\x11documentation_url\x18\x03 \x01(\t\x1a*\n\x04Type\x12\x14\n\x0cdisplay_name\x18\x01 \x01(\t\x12\x0c\n\x04code\x18\x02 \x01(\t"@\n\x05Level\x12\x15\n\x11LEVEL_UNSPECIFIED\x10\x00\x12\t\n\x05ERROR\x10\x03\x12\x0b\n\x07WARNING\x10\x08\x12\x08\n\x04INFO\x10\x0c"\xb9\x01\n\x0fAnalysisMessage\x12R\n\x0cmessage_base\x18\x01 \x01(\x0b2<.google.cloud.gkehub.servicemesh.v1alpha.AnalysisMessageBase\x12\x13\n\x0bdescription\x18\x02 \x01(\t\x12\x16\n\x0eresource_paths\x18\x03 \x03(\t\x12%\n\x04args\x18\x04 \x01(\x0b2\x17.google.protobuf.StructB\x92\x02\n+com.google.cloud.gkehub.servicemesh.v1alphaB\x10ServiceMeshProtoP\x01ZMcloud.google.com/go/gkehub/servicemesh/apiv1alpha/servicemeshpb;servicemeshpb\xaa\x02\'Google.Cloud.GkeHub.ServiceMesh.V1Alpha\xca\x02\'Google\\Cloud\\GkeHub\\ServiceMesh\\V1alpha\xea\x02+Google::Cloud::GkeHub::ServiceMesh::V1alphab\x06proto3')
_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'google.cloud.gkehub.v1alpha.servicemesh.servicemesh_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
    _globals['DESCRIPTOR']._loaded_options = None
    _globals['DESCRIPTOR']._serialized_options = b"\n+com.google.cloud.gkehub.servicemesh.v1alphaB\x10ServiceMeshProtoP\x01ZMcloud.google.com/go/gkehub/servicemesh/apiv1alpha/servicemeshpb;servicemeshpb\xaa\x02'Google.Cloud.GkeHub.ServiceMesh.V1Alpha\xca\x02'Google\\Cloud\\GkeHub\\ServiceMesh\\V1alpha\xea\x02+Google::Cloud::GkeHub::ServiceMesh::V1alpha"
    _globals['_FEATURESTATE'].fields_by_name['analysis_messages']._loaded_options = None
    _globals['_FEATURESTATE'].fields_by_name['analysis_messages']._serialized_options = b'\xe0A\x03'
    _globals['_MEMBERSHIPSTATE'].fields_by_name['analysis_messages']._loaded_options = None
    _globals['_MEMBERSHIPSTATE'].fields_by_name['analysis_messages']._serialized_options = b'\xe0A\x03'
    _globals['_FEATURESTATE']._serialized_start = 165
    _globals['_FEATURESTATE']._serialized_end = 269
    _globals['_MEMBERSHIPSTATE']._serialized_start = 271
    _globals['_MEMBERSHIPSTATE']._serialized_end = 378
    _globals['_ANALYSISMESSAGEBASE']._serialized_start = 381
    _globals['_ANALYSISMESSAGEBASE']._serialized_end = 703
    _globals['_ANALYSISMESSAGEBASE_TYPE']._serialized_start = 595
    _globals['_ANALYSISMESSAGEBASE_TYPE']._serialized_end = 637
    _globals['_ANALYSISMESSAGEBASE_LEVEL']._serialized_start = 639
    _globals['_ANALYSISMESSAGEBASE_LEVEL']._serialized_end = 703
    _globals['_ANALYSISMESSAGE']._serialized_start = 706
    _globals['_ANALYSISMESSAGE']._serialized_end = 891