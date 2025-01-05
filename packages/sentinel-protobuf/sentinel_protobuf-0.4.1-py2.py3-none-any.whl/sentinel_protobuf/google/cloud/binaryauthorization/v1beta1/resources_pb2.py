"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_runtime_version.ValidateProtobufRuntimeVersion(_runtime_version.Domain.PUBLIC, 5, 28, 1, '', 'google/cloud/binaryauthorization/v1beta1/resources.proto')
_sym_db = _symbol_database.Default()
from .....google.api import field_behavior_pb2 as google_dot_api_dot_field__behavior__pb2
from .....google.api import resource_pb2 as google_dot_api_dot_resource__pb2
from google.protobuf import timestamp_pb2 as google_dot_protobuf_dot_timestamp__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n8google/cloud/binaryauthorization/v1beta1/resources.proto\x12(google.cloud.binaryauthorization.v1beta1\x1a\x1fgoogle/api/field_behavior.proto\x1a\x19google/api/resource.proto\x1a\x1fgoogle/protobuf/timestamp.proto"\xb1\r\n\x06Policy\x12\x11\n\x04name\x18\x01 \x01(\tB\x03\xe0A\x03\x12\x18\n\x0bdescription\x18\x06 \x01(\tB\x03\xe0A\x01\x12w\n\x1dglobal_policy_evaluation_mode\x18\x07 \x01(\x0e2K.google.cloud.binaryauthorization.v1beta1.Policy.GlobalPolicyEvaluationModeB\x03\xe0A\x01\x12n\n\x1cadmission_whitelist_patterns\x18\x02 \x03(\x0b2C.google.cloud.binaryauthorization.v1beta1.AdmissionWhitelistPatternB\x03\xe0A\x01\x12q\n\x17cluster_admission_rules\x18\x03 \x03(\x0b2K.google.cloud.binaryauthorization.v1beta1.Policy.ClusterAdmissionRulesEntryB\x03\xe0A\x01\x12\x8a\x01\n$kubernetes_namespace_admission_rules\x18\n \x03(\x0b2W.google.cloud.binaryauthorization.v1beta1.Policy.KubernetesNamespaceAdmissionRulesEntryB\x03\xe0A\x01\x12\x95\x01\n*kubernetes_service_account_admission_rules\x18\x08 \x03(\x0b2\\.google.cloud.binaryauthorization.v1beta1.Policy.KubernetesServiceAccountAdmissionRulesEntryB\x03\xe0A\x01\x12\x8d\x01\n&istio_service_identity_admission_rules\x18\t \x03(\x0b2X.google.cloud.binaryauthorization.v1beta1.Policy.IstioServiceIdentityAdmissionRulesEntryB\x03\xe0A\x01\x12\\\n\x16default_admission_rule\x18\x04 \x01(\x0b27.google.cloud.binaryauthorization.v1beta1.AdmissionRuleB\x03\xe0A\x02\x124\n\x0bupdate_time\x18\x05 \x01(\x0b2\x1a.google.protobuf.TimestampB\x03\xe0A\x03\x1au\n\x1aClusterAdmissionRulesEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12F\n\x05value\x18\x02 \x01(\x0b27.google.cloud.binaryauthorization.v1beta1.AdmissionRule:\x028\x01\x1a\x81\x01\n&KubernetesNamespaceAdmissionRulesEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12F\n\x05value\x18\x02 \x01(\x0b27.google.cloud.binaryauthorization.v1beta1.AdmissionRule:\x028\x01\x1a\x86\x01\n+KubernetesServiceAccountAdmissionRulesEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12F\n\x05value\x18\x02 \x01(\x0b27.google.cloud.binaryauthorization.v1beta1.AdmissionRule:\x028\x01\x1a\x82\x01\n\'IstioServiceIdentityAdmissionRulesEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12F\n\x05value\x18\x02 \x01(\x0b27.google.cloud.binaryauthorization.v1beta1.AdmissionRule:\x028\x01"d\n\x1aGlobalPolicyEvaluationMode\x12-\n)GLOBAL_POLICY_EVALUATION_MODE_UNSPECIFIED\x10\x00\x12\n\n\x06ENABLE\x10\x01\x12\x0b\n\x07DISABLE\x10\x02:f\xeaAc\n)binaryauthorization.googleapis.com/Policy\x12\x19projects/{project}/policy\x12\x1blocations/{location}/policy"1\n\x19AdmissionWhitelistPattern\x12\x14\n\x0cname_pattern\x18\x01 \x01(\t"\xe4\x03\n\rAdmissionRule\x12d\n\x0fevaluation_mode\x18\x01 \x01(\x0e2F.google.cloud.binaryauthorization.v1beta1.AdmissionRule.EvaluationModeB\x03\xe0A\x02\x12$\n\x17require_attestations_by\x18\x02 \x03(\tB\x03\xe0A\x01\x12f\n\x10enforcement_mode\x18\x03 \x01(\x0e2G.google.cloud.binaryauthorization.v1beta1.AdmissionRule.EnforcementModeB\x03\xe0A\x02"m\n\x0eEvaluationMode\x12\x1f\n\x1bEVALUATION_MODE_UNSPECIFIED\x10\x00\x12\x10\n\x0cALWAYS_ALLOW\x10\x01\x12\x17\n\x13REQUIRE_ATTESTATION\x10\x02\x12\x0f\n\x0bALWAYS_DENY\x10\x03"p\n\x0fEnforcementMode\x12 \n\x1cENFORCEMENT_MODE_UNSPECIFIED\x10\x00\x12 \n\x1cENFORCED_BLOCK_AND_AUDIT_LOG\x10\x01\x12\x19\n\x15DRYRUN_AUDIT_LOG_ONLY\x10\x02"\xbc\x02\n\x08Attestor\x12\x11\n\x04name\x18\x01 \x01(\tB\x03\xe0A\x02\x12\x18\n\x0bdescription\x18\x06 \x01(\tB\x03\xe0A\x01\x12a\n\x17user_owned_drydock_note\x18\x03 \x01(\x0b2>.google.cloud.binaryauthorization.v1beta1.UserOwnedDrydockNoteH\x00\x124\n\x0bupdate_time\x18\x04 \x01(\x0b2\x1a.google.protobuf.TimestampB\x03\xe0A\x03:Y\xeaAV\n+binaryauthorization.googleapis.com/Attestor\x12\'projects/{project}/attestors/{attestor}B\x0f\n\rattestor_type"\xb9\x01\n\x14UserOwnedDrydockNote\x12\x1b\n\x0enote_reference\x18\x01 \x01(\tB\x03\xe0A\x02\x12U\n\x0bpublic_keys\x18\x02 \x03(\x0b2;.google.cloud.binaryauthorization.v1beta1.AttestorPublicKeyB\x03\xe0A\x01\x12-\n delegation_service_account_email\x18\x03 \x01(\tB\x03\xe0A\x03"\xc4\x04\n\rPkixPublicKey\x12\x16\n\x0epublic_key_pem\x18\x01 \x01(\t\x12g\n\x13signature_algorithm\x18\x02 \x01(\x0e2J.google.cloud.binaryauthorization.v1beta1.PkixPublicKey.SignatureAlgorithm"\xb1\x03\n\x12SignatureAlgorithm\x12#\n\x1fSIGNATURE_ALGORITHM_UNSPECIFIED\x10\x00\x12\x17\n\x13RSA_PSS_2048_SHA256\x10\x01\x12\x17\n\x13RSA_PSS_3072_SHA256\x10\x02\x12\x17\n\x13RSA_PSS_4096_SHA256\x10\x03\x12\x17\n\x13RSA_PSS_4096_SHA512\x10\x04\x12\x1e\n\x1aRSA_SIGN_PKCS1_2048_SHA256\x10\x05\x12\x1e\n\x1aRSA_SIGN_PKCS1_3072_SHA256\x10\x06\x12\x1e\n\x1aRSA_SIGN_PKCS1_4096_SHA256\x10\x07\x12\x1e\n\x1aRSA_SIGN_PKCS1_4096_SHA512\x10\x08\x12\x15\n\x11ECDSA_P256_SHA256\x10\t\x12\x17\n\x13EC_SIGN_P256_SHA256\x10\t\x12\x15\n\x11ECDSA_P384_SHA384\x10\n\x12\x17\n\x13EC_SIGN_P384_SHA384\x10\n\x12\x15\n\x11ECDSA_P521_SHA512\x10\x0b\x12\x17\n\x13EC_SIGN_P521_SHA512\x10\x0b\x1a\x02\x10\x01"\xbf\x01\n\x11AttestorPublicKey\x12\x14\n\x07comment\x18\x01 \x01(\tB\x03\xe0A\x01\x12\n\n\x02id\x18\x02 \x01(\t\x12&\n\x1cascii_armored_pgp_public_key\x18\x03 \x01(\tH\x00\x12R\n\x0fpkix_public_key\x18\x05 \x01(\x0b27.google.cloud.binaryauthorization.v1beta1.PkixPublicKeyH\x00B\x0c\n\npublic_keyB\xba\x02\n,com.google.cloud.binaryauthorization.v1beta1B!BinaryAuthorizationResourcesProtoP\x01Z^cloud.google.com/go/binaryauthorization/apiv1beta1/binaryauthorizationpb;binaryauthorizationpb\xf8\x01\x01\xaa\x02(Google.Cloud.BinaryAuthorization.V1Beta1\xca\x02(Google\\Cloud\\BinaryAuthorization\\V1beta1\xea\x02+Google::Cloud::BinaryAuthorization::V1beta1b\x06proto3')
_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'google.cloud.binaryauthorization.v1beta1.resources_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
    _globals['DESCRIPTOR']._loaded_options = None
    _globals['DESCRIPTOR']._serialized_options = b'\n,com.google.cloud.binaryauthorization.v1beta1B!BinaryAuthorizationResourcesProtoP\x01Z^cloud.google.com/go/binaryauthorization/apiv1beta1/binaryauthorizationpb;binaryauthorizationpb\xf8\x01\x01\xaa\x02(Google.Cloud.BinaryAuthorization.V1Beta1\xca\x02(Google\\Cloud\\BinaryAuthorization\\V1beta1\xea\x02+Google::Cloud::BinaryAuthorization::V1beta1'
    _globals['_POLICY_CLUSTERADMISSIONRULESENTRY']._loaded_options = None
    _globals['_POLICY_CLUSTERADMISSIONRULESENTRY']._serialized_options = b'8\x01'
    _globals['_POLICY_KUBERNETESNAMESPACEADMISSIONRULESENTRY']._loaded_options = None
    _globals['_POLICY_KUBERNETESNAMESPACEADMISSIONRULESENTRY']._serialized_options = b'8\x01'
    _globals['_POLICY_KUBERNETESSERVICEACCOUNTADMISSIONRULESENTRY']._loaded_options = None
    _globals['_POLICY_KUBERNETESSERVICEACCOUNTADMISSIONRULESENTRY']._serialized_options = b'8\x01'
    _globals['_POLICY_ISTIOSERVICEIDENTITYADMISSIONRULESENTRY']._loaded_options = None
    _globals['_POLICY_ISTIOSERVICEIDENTITYADMISSIONRULESENTRY']._serialized_options = b'8\x01'
    _globals['_POLICY'].fields_by_name['name']._loaded_options = None
    _globals['_POLICY'].fields_by_name['name']._serialized_options = b'\xe0A\x03'
    _globals['_POLICY'].fields_by_name['description']._loaded_options = None
    _globals['_POLICY'].fields_by_name['description']._serialized_options = b'\xe0A\x01'
    _globals['_POLICY'].fields_by_name['global_policy_evaluation_mode']._loaded_options = None
    _globals['_POLICY'].fields_by_name['global_policy_evaluation_mode']._serialized_options = b'\xe0A\x01'
    _globals['_POLICY'].fields_by_name['admission_whitelist_patterns']._loaded_options = None
    _globals['_POLICY'].fields_by_name['admission_whitelist_patterns']._serialized_options = b'\xe0A\x01'
    _globals['_POLICY'].fields_by_name['cluster_admission_rules']._loaded_options = None
    _globals['_POLICY'].fields_by_name['cluster_admission_rules']._serialized_options = b'\xe0A\x01'
    _globals['_POLICY'].fields_by_name['kubernetes_namespace_admission_rules']._loaded_options = None
    _globals['_POLICY'].fields_by_name['kubernetes_namespace_admission_rules']._serialized_options = b'\xe0A\x01'
    _globals['_POLICY'].fields_by_name['kubernetes_service_account_admission_rules']._loaded_options = None
    _globals['_POLICY'].fields_by_name['kubernetes_service_account_admission_rules']._serialized_options = b'\xe0A\x01'
    _globals['_POLICY'].fields_by_name['istio_service_identity_admission_rules']._loaded_options = None
    _globals['_POLICY'].fields_by_name['istio_service_identity_admission_rules']._serialized_options = b'\xe0A\x01'
    _globals['_POLICY'].fields_by_name['default_admission_rule']._loaded_options = None
    _globals['_POLICY'].fields_by_name['default_admission_rule']._serialized_options = b'\xe0A\x02'
    _globals['_POLICY'].fields_by_name['update_time']._loaded_options = None
    _globals['_POLICY'].fields_by_name['update_time']._serialized_options = b'\xe0A\x03'
    _globals['_POLICY']._loaded_options = None
    _globals['_POLICY']._serialized_options = b'\xeaAc\n)binaryauthorization.googleapis.com/Policy\x12\x19projects/{project}/policy\x12\x1blocations/{location}/policy'
    _globals['_ADMISSIONRULE'].fields_by_name['evaluation_mode']._loaded_options = None
    _globals['_ADMISSIONRULE'].fields_by_name['evaluation_mode']._serialized_options = b'\xe0A\x02'
    _globals['_ADMISSIONRULE'].fields_by_name['require_attestations_by']._loaded_options = None
    _globals['_ADMISSIONRULE'].fields_by_name['require_attestations_by']._serialized_options = b'\xe0A\x01'
    _globals['_ADMISSIONRULE'].fields_by_name['enforcement_mode']._loaded_options = None
    _globals['_ADMISSIONRULE'].fields_by_name['enforcement_mode']._serialized_options = b'\xe0A\x02'
    _globals['_ATTESTOR'].fields_by_name['name']._loaded_options = None
    _globals['_ATTESTOR'].fields_by_name['name']._serialized_options = b'\xe0A\x02'
    _globals['_ATTESTOR'].fields_by_name['description']._loaded_options = None
    _globals['_ATTESTOR'].fields_by_name['description']._serialized_options = b'\xe0A\x01'
    _globals['_ATTESTOR'].fields_by_name['update_time']._loaded_options = None
    _globals['_ATTESTOR'].fields_by_name['update_time']._serialized_options = b'\xe0A\x03'
    _globals['_ATTESTOR']._loaded_options = None
    _globals['_ATTESTOR']._serialized_options = b"\xeaAV\n+binaryauthorization.googleapis.com/Attestor\x12'projects/{project}/attestors/{attestor}"
    _globals['_USEROWNEDDRYDOCKNOTE'].fields_by_name['note_reference']._loaded_options = None
    _globals['_USEROWNEDDRYDOCKNOTE'].fields_by_name['note_reference']._serialized_options = b'\xe0A\x02'
    _globals['_USEROWNEDDRYDOCKNOTE'].fields_by_name['public_keys']._loaded_options = None
    _globals['_USEROWNEDDRYDOCKNOTE'].fields_by_name['public_keys']._serialized_options = b'\xe0A\x01'
    _globals['_USEROWNEDDRYDOCKNOTE'].fields_by_name['delegation_service_account_email']._loaded_options = None
    _globals['_USEROWNEDDRYDOCKNOTE'].fields_by_name['delegation_service_account_email']._serialized_options = b'\xe0A\x03'
    _globals['_PKIXPUBLICKEY_SIGNATUREALGORITHM']._loaded_options = None
    _globals['_PKIXPUBLICKEY_SIGNATUREALGORITHM']._serialized_options = b'\x10\x01'
    _globals['_ATTESTORPUBLICKEY'].fields_by_name['comment']._loaded_options = None
    _globals['_ATTESTORPUBLICKEY'].fields_by_name['comment']._serialized_options = b'\xe0A\x01'
    _globals['_POLICY']._serialized_start = 196
    _globals['_POLICY']._serialized_end = 1909
    _globals['_POLICY_CLUSTERADMISSIONRULESENTRY']._serialized_start = 1184
    _globals['_POLICY_CLUSTERADMISSIONRULESENTRY']._serialized_end = 1301
    _globals['_POLICY_KUBERNETESNAMESPACEADMISSIONRULESENTRY']._serialized_start = 1304
    _globals['_POLICY_KUBERNETESNAMESPACEADMISSIONRULESENTRY']._serialized_end = 1433
    _globals['_POLICY_KUBERNETESSERVICEACCOUNTADMISSIONRULESENTRY']._serialized_start = 1436
    _globals['_POLICY_KUBERNETESSERVICEACCOUNTADMISSIONRULESENTRY']._serialized_end = 1570
    _globals['_POLICY_ISTIOSERVICEIDENTITYADMISSIONRULESENTRY']._serialized_start = 1573
    _globals['_POLICY_ISTIOSERVICEIDENTITYADMISSIONRULESENTRY']._serialized_end = 1703
    _globals['_POLICY_GLOBALPOLICYEVALUATIONMODE']._serialized_start = 1705
    _globals['_POLICY_GLOBALPOLICYEVALUATIONMODE']._serialized_end = 1805
    _globals['_ADMISSIONWHITELISTPATTERN']._serialized_start = 1911
    _globals['_ADMISSIONWHITELISTPATTERN']._serialized_end = 1960
    _globals['_ADMISSIONRULE']._serialized_start = 1963
    _globals['_ADMISSIONRULE']._serialized_end = 2447
    _globals['_ADMISSIONRULE_EVALUATIONMODE']._serialized_start = 2224
    _globals['_ADMISSIONRULE_EVALUATIONMODE']._serialized_end = 2333
    _globals['_ADMISSIONRULE_ENFORCEMENTMODE']._serialized_start = 2335
    _globals['_ADMISSIONRULE_ENFORCEMENTMODE']._serialized_end = 2447
    _globals['_ATTESTOR']._serialized_start = 2450
    _globals['_ATTESTOR']._serialized_end = 2766
    _globals['_USEROWNEDDRYDOCKNOTE']._serialized_start = 2769
    _globals['_USEROWNEDDRYDOCKNOTE']._serialized_end = 2954
    _globals['_PKIXPUBLICKEY']._serialized_start = 2957
    _globals['_PKIXPUBLICKEY']._serialized_end = 3537
    _globals['_PKIXPUBLICKEY_SIGNATUREALGORITHM']._serialized_start = 3104
    _globals['_PKIXPUBLICKEY_SIGNATUREALGORITHM']._serialized_end = 3537
    _globals['_ATTESTORPUBLICKEY']._serialized_start = 3540
    _globals['_ATTESTORPUBLICKEY']._serialized_end = 3731