"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_runtime_version.ValidateProtobufRuntimeVersion(_runtime_version.Domain.PUBLIC, 5, 28, 1, '', 'google/devtools/containeranalysis/v1beta1/cvss/cvss.proto')
_sym_db = _symbol_database.Default()
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n9google/devtools/containeranalysis/v1beta1/cvss/cvss.proto\x12\x1dgrafeas.v1beta1.vulnerability"\xdd\n\n\x06CVSSv3\x12\x12\n\nbase_score\x18\x01 \x01(\x02\x12\x1c\n\x14exploitability_score\x18\x02 \x01(\x02\x12\x14\n\x0cimpact_score\x18\x03 \x01(\x02\x12I\n\rattack_vector\x18\x05 \x01(\x0e22.grafeas.v1beta1.vulnerability.CVSSv3.AttackVector\x12Q\n\x11attack_complexity\x18\x06 \x01(\x0e26.grafeas.v1beta1.vulnerability.CVSSv3.AttackComplexity\x12U\n\x13privileges_required\x18\x07 \x01(\x0e28.grafeas.v1beta1.vulnerability.CVSSv3.PrivilegesRequired\x12O\n\x10user_interaction\x18\x08 \x01(\x0e25.grafeas.v1beta1.vulnerability.CVSSv3.UserInteraction\x12:\n\x05scope\x18\t \x01(\x0e2+.grafeas.v1beta1.vulnerability.CVSSv3.Scope\x12L\n\x16confidentiality_impact\x18\n \x01(\x0e2,.grafeas.v1beta1.vulnerability.CVSSv3.Impact\x12F\n\x10integrity_impact\x18\x0b \x01(\x0e2,.grafeas.v1beta1.vulnerability.CVSSv3.Impact\x12I\n\x13availability_impact\x18\x0c \x01(\x0e2,.grafeas.v1beta1.vulnerability.CVSSv3.Impact"\x99\x01\n\x0cAttackVector\x12\x1d\n\x19ATTACK_VECTOR_UNSPECIFIED\x10\x00\x12\x19\n\x15ATTACK_VECTOR_NETWORK\x10\x01\x12\x1a\n\x16ATTACK_VECTOR_ADJACENT\x10\x02\x12\x17\n\x13ATTACK_VECTOR_LOCAL\x10\x03\x12\x1a\n\x16ATTACK_VECTOR_PHYSICAL\x10\x04"l\n\x10AttackComplexity\x12!\n\x1dATTACK_COMPLEXITY_UNSPECIFIED\x10\x00\x12\x19\n\x15ATTACK_COMPLEXITY_LOW\x10\x01\x12\x1a\n\x16ATTACK_COMPLEXITY_HIGH\x10\x02"\x92\x01\n\x12PrivilegesRequired\x12#\n\x1fPRIVILEGES_REQUIRED_UNSPECIFIED\x10\x00\x12\x1c\n\x18PRIVILEGES_REQUIRED_NONE\x10\x01\x12\x1b\n\x17PRIVILEGES_REQUIRED_LOW\x10\x02\x12\x1c\n\x18PRIVILEGES_REQUIRED_HIGH\x10\x03"m\n\x0fUserInteraction\x12 \n\x1cUSER_INTERACTION_UNSPECIFIED\x10\x00\x12\x19\n\x15USER_INTERACTION_NONE\x10\x01\x12\x1d\n\x19USER_INTERACTION_REQUIRED\x10\x02"F\n\x05Scope\x12\x15\n\x11SCOPE_UNSPECIFIED\x10\x00\x12\x13\n\x0fSCOPE_UNCHANGED\x10\x01\x12\x11\n\rSCOPE_CHANGED\x10\x02"R\n\x06Impact\x12\x16\n\x12IMPACT_UNSPECIFIED\x10\x00\x12\x0f\n\x0bIMPACT_HIGH\x10\x01\x12\x0e\n\nIMPACT_LOW\x10\x02\x12\x0f\n\x0bIMPACT_NONE\x10\x03B\x84\x01\n io.grafeas.v1beta1.vulnerabilityP\x01ZXcloud.google.com/go/containeranalysis/apiv1beta1/containeranalysispb;containeranalysispb\xa2\x02\x03GRAb\x06proto3')
_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'google.devtools.containeranalysis.v1beta1.cvss.cvss_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
    _globals['DESCRIPTOR']._loaded_options = None
    _globals['DESCRIPTOR']._serialized_options = b'\n io.grafeas.v1beta1.vulnerabilityP\x01ZXcloud.google.com/go/containeranalysis/apiv1beta1/containeranalysispb;containeranalysispb\xa2\x02\x03GRA'
    _globals['_CVSSV3']._serialized_start = 93
    _globals['_CVSSV3']._serialized_end = 1466
    _globals['_CVSSV3_ATTACKVECTOR']._serialized_start = 787
    _globals['_CVSSV3_ATTACKVECTOR']._serialized_end = 940
    _globals['_CVSSV3_ATTACKCOMPLEXITY']._serialized_start = 942
    _globals['_CVSSV3_ATTACKCOMPLEXITY']._serialized_end = 1050
    _globals['_CVSSV3_PRIVILEGESREQUIRED']._serialized_start = 1053
    _globals['_CVSSV3_PRIVILEGESREQUIRED']._serialized_end = 1199
    _globals['_CVSSV3_USERINTERACTION']._serialized_start = 1201
    _globals['_CVSSV3_USERINTERACTION']._serialized_end = 1310
    _globals['_CVSSV3_SCOPE']._serialized_start = 1312
    _globals['_CVSSV3_SCOPE']._serialized_end = 1382
    _globals['_CVSSV3_IMPACT']._serialized_start = 1384
    _globals['_CVSSV3_IMPACT']._serialized_end = 1466