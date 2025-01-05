"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_runtime_version.ValidateProtobufRuntimeVersion(_runtime_version.Domain.PUBLIC, 5, 28, 1, '', 'google/cloud/securitycenter/v2/attack_path.proto')
_sym_db = _symbol_database.Default()
from .....google.api import resource_pb2 as google_dot_api_dot_resource__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n0google/cloud/securitycenter/v2/attack_path.proto\x12\x1egoogle.cloud.securitycenter.v2\x1a\x19google/api/resource.proto"\xf0\n\n\nAttackPath\x12\x0c\n\x04name\x18\x01 \x01(\t\x12M\n\npath_nodes\x18\x02 \x03(\x0b29.google.cloud.securitycenter.v2.AttackPath.AttackPathNode\x12H\n\x05edges\x18\x03 \x03(\x0b29.google.cloud.securitycenter.v2.AttackPath.AttackPathEdge\x1a\xbd\x06\n\x0eAttackPathNode\x12\x10\n\x08resource\x18\x01 \x01(\t\x12\x15\n\rresource_type\x18\x02 \x01(\t\x12\x14\n\x0cdisplay_name\x18\x03 \x01(\t\x12p\n\x13associated_findings\x18\x04 \x03(\x0b2S.google.cloud.securitycenter.v2.AttackPath.AttackPathNode.PathNodeAssociatedFinding\x12\x0c\n\x04uuid\x18\x05 \x01(\t\x12^\n\x0cattack_steps\x18\x06 \x03(\x0b2H.google.cloud.securitycenter.v2.AttackPath.AttackPathNode.AttackStepNode\x1a^\n\x19PathNodeAssociatedFinding\x12\x19\n\x11canonical_finding\x18\x01 \x01(\t\x12\x18\n\x10finding_category\x18\x02 \x01(\t\x12\x0c\n\x04name\x18\x03 \x01(\t\x1a\xb0\x02\n\x0eAttackStepNode\x12\x0c\n\x04uuid\x18\x01 \x01(\t\x12P\n\x04type\x18\x02 \x01(\x0e2B.google.cloud.securitycenter.v2.AttackPath.AttackPathNode.NodeType\x12\x14\n\x0cdisplay_name\x18\x03 \x01(\t\x12d\n\x06labels\x18\x04 \x03(\x0b2T.google.cloud.securitycenter.v2.AttackPath.AttackPathNode.AttackStepNode.LabelsEntry\x12\x13\n\x0bdescription\x18\x05 \x01(\t\x1a-\n\x0bLabelsEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\r\n\x05value\x18\x02 \x01(\t:\x028\x01"y\n\x08NodeType\x12\x19\n\x15NODE_TYPE_UNSPECIFIED\x10\x00\x12\x11\n\rNODE_TYPE_AND\x10\x01\x12\x10\n\x0cNODE_TYPE_OR\x10\x02\x12\x15\n\x11NODE_TYPE_DEFENSE\x10\x03\x12\x16\n\x12NODE_TYPE_ATTACKER\x10\x04\x1a5\n\x0eAttackPathEdge\x12\x0e\n\x06source\x18\x01 \x01(\t\x12\x13\n\x0bdestination\x18\x02 \x01(\t:\xc3\x02\xeaA\xbf\x02\n(securitycenter.googleapis.com/AttackPath\x12qorganizations/{organization}/simulations/{simulation}/valuedResources/{valued_resource}/attackPaths/{attack_path}\x12\x86\x01organizations/{organization}/locations/{location}/simulations/{simulation}/valuedResources/{valued_resource}/attackPaths/{attack_path}*\x0battackPaths2\nattackPathB\xe9\x01\n"com.google.cloud.securitycenter.v2B\x0fAttackPathProtoP\x01ZJcloud.google.com/go/securitycenter/apiv2/securitycenterpb;securitycenterpb\xaa\x02\x1eGoogle.Cloud.SecurityCenter.V2\xca\x02\x1eGoogle\\Cloud\\SecurityCenter\\V2\xea\x02!Google::Cloud::SecurityCenter::V2b\x06proto3')
_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'google.cloud.securitycenter.v2.attack_path_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
    _globals['DESCRIPTOR']._loaded_options = None
    _globals['DESCRIPTOR']._serialized_options = b'\n"com.google.cloud.securitycenter.v2B\x0fAttackPathProtoP\x01ZJcloud.google.com/go/securitycenter/apiv2/securitycenterpb;securitycenterpb\xaa\x02\x1eGoogle.Cloud.SecurityCenter.V2\xca\x02\x1eGoogle\\Cloud\\SecurityCenter\\V2\xea\x02!Google::Cloud::SecurityCenter::V2'
    _globals['_ATTACKPATH_ATTACKPATHNODE_ATTACKSTEPNODE_LABELSENTRY']._loaded_options = None
    _globals['_ATTACKPATH_ATTACKPATHNODE_ATTACKSTEPNODE_LABELSENTRY']._serialized_options = b'8\x01'
    _globals['_ATTACKPATH']._loaded_options = None
    _globals['_ATTACKPATH']._serialized_options = b'\xeaA\xbf\x02\n(securitycenter.googleapis.com/AttackPath\x12qorganizations/{organization}/simulations/{simulation}/valuedResources/{valued_resource}/attackPaths/{attack_path}\x12\x86\x01organizations/{organization}/locations/{location}/simulations/{simulation}/valuedResources/{valued_resource}/attackPaths/{attack_path}*\x0battackPaths2\nattackPath'
    _globals['_ATTACKPATH']._serialized_start = 112
    _globals['_ATTACKPATH']._serialized_end = 1504
    _globals['_ATTACKPATH_ATTACKPATHNODE']._serialized_start = 294
    _globals['_ATTACKPATH_ATTACKPATHNODE']._serialized_end = 1123
    _globals['_ATTACKPATH_ATTACKPATHNODE_PATHNODEASSOCIATEDFINDING']._serialized_start = 599
    _globals['_ATTACKPATH_ATTACKPATHNODE_PATHNODEASSOCIATEDFINDING']._serialized_end = 693
    _globals['_ATTACKPATH_ATTACKPATHNODE_ATTACKSTEPNODE']._serialized_start = 696
    _globals['_ATTACKPATH_ATTACKPATHNODE_ATTACKSTEPNODE']._serialized_end = 1000
    _globals['_ATTACKPATH_ATTACKPATHNODE_ATTACKSTEPNODE_LABELSENTRY']._serialized_start = 955
    _globals['_ATTACKPATH_ATTACKPATHNODE_ATTACKSTEPNODE_LABELSENTRY']._serialized_end = 1000
    _globals['_ATTACKPATH_ATTACKPATHNODE_NODETYPE']._serialized_start = 1002
    _globals['_ATTACKPATH_ATTACKPATHNODE_NODETYPE']._serialized_end = 1123
    _globals['_ATTACKPATH_ATTACKPATHEDGE']._serialized_start = 1125
    _globals['_ATTACKPATH_ATTACKPATHEDGE']._serialized_end = 1178