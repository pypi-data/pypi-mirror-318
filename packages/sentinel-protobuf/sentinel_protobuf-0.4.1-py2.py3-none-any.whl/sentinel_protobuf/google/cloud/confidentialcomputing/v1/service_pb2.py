"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_runtime_version.ValidateProtobufRuntimeVersion(_runtime_version.Domain.PUBLIC, 5, 28, 1, '', 'google/cloud/confidentialcomputing/v1/service.proto')
_sym_db = _symbol_database.Default()
from .....google.api import annotations_pb2 as google_dot_api_dot_annotations__pb2
from .....google.api import client_pb2 as google_dot_api_dot_client__pb2
from .....google.api import field_behavior_pb2 as google_dot_api_dot_field__behavior__pb2
from .....google.api import resource_pb2 as google_dot_api_dot_resource__pb2
from google.protobuf import timestamp_pb2 as google_dot_protobuf_dot_timestamp__pb2
from .....google.rpc import status_pb2 as google_dot_rpc_dot_status__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n3google/cloud/confidentialcomputing/v1/service.proto\x12%google.cloud.confidentialcomputing.v1\x1a\x1cgoogle/api/annotations.proto\x1a\x17google/api/client.proto\x1a\x1fgoogle/api/field_behavior.proto\x1a\x19google/api/resource.proto\x1a\x1fgoogle/protobuf/timestamp.proto\x1a\x17google/rpc/status.proto"\xa5\x02\n\tChallenge\x12\x11\n\x04name\x18\x01 \x01(\tB\x03\xe0A\x03\x124\n\x0bcreate_time\x18\x02 \x01(\x0b2\x1a.google.protobuf.TimestampB\x03\xe0A\x03\x124\n\x0bexpire_time\x18\x03 \x01(\x0b2\x1a.google.protobuf.TimestampB\x03\xe0A\x03\x12\x11\n\x04used\x18\x04 \x01(\x08B\x03\xe0A\x03\x12\x16\n\ttpm_nonce\x18\x06 \x01(\tB\x03\xe0A\x03:n\xeaAk\n.confidentialcomputing.googleapis.com/Challenge\x129projects/{project}/locations/{location}/challenges/{uuid}"\x9d\x01\n\x16CreateChallengeRequest\x129\n\x06parent\x18\x01 \x01(\tB)\xe0A\x02\xfaA#\n!locations.googleapis.com/Location\x12H\n\tchallenge\x18\x02 \x01(\x0b20.google.cloud.confidentialcomputing.v1.ChallengeB\x03\xe0A\x02"\x88\x05\n\x18VerifyAttestationRequest\x12Q\n\x07td_ccel\x18\x06 \x01(\x0b29.google.cloud.confidentialcomputing.v1.TdxCcelAttestationB\x03\xe0A\x01H\x00\x12\\\n\x13sev_snp_attestation\x18\x07 \x01(\x0b28.google.cloud.confidentialcomputing.v1.SevSnpAttestationB\x03\xe0A\x01H\x00\x12I\n\tchallenge\x18\x01 \x01(\tB6\xe0A\x02\xfaA0\n.confidentialcomputing.googleapis.com/Challenge\x12S\n\x0fgcp_credentials\x18\x02 \x01(\x0b25.google.cloud.confidentialcomputing.v1.GcpCredentialsB\x03\xe0A\x01\x12S\n\x0ftpm_attestation\x18\x03 \x01(\x0b25.google.cloud.confidentialcomputing.v1.TpmAttestationB\x03\xe0A\x02\x12b\n\x17confidential_space_info\x18\x04 \x01(\x0b2<.google.cloud.confidentialcomputing.v1.ConfidentialSpaceInfoB\x03\xe0A\x01\x12O\n\rtoken_options\x18\x05 \x01(\x0b23.google.cloud.confidentialcomputing.v1.TokenOptionsB\x03\xe0A\x01B\x11\n\x0ftee_attestation"\x83\x01\n\x12TdxCcelAttestation\x12\x1c\n\x0fccel_acpi_table\x18\x01 \x01(\x0cB\x03\xe0A\x01\x12\x16\n\tccel_data\x18\x02 \x01(\x0cB\x03\xe0A\x01\x12 \n\x13canonical_event_log\x18\x03 \x01(\x0cB\x03\xe0A\x01\x12\x15\n\x08td_quote\x18\x04 \x01(\x0cB\x03\xe0A\x01"?\n\x11SevSnpAttestation\x12\x13\n\x06report\x18\x01 \x01(\x0cB\x03\xe0A\x01\x12\x15\n\x08aux_blob\x18\x02 \x01(\x0cB\x03\xe0A\x01"l\n\x19VerifyAttestationResponse\x12\x1e\n\x11oidc_claims_token\x18\x02 \x01(\tB\x03\xe0A\x03\x12/\n\x0epartial_errors\x18\x03 \x03(\x0b2\x12.google.rpc.StatusB\x03\xe0A\x03"3\n\x0eGcpCredentials\x12!\n\x19service_account_id_tokens\x18\x02 \x03(\t"\xa6\x05\n\x0cTokenOptions\x12v\n\x1aaws_principal_tags_options\x18\x04 \x01(\x0b2K.google.cloud.confidentialcomputing.v1.TokenOptions.AwsPrincipalTagsOptionsB\x03\xe0A\x01H\x00\x12\x15\n\x08audience\x18\x01 \x01(\tB\x03\xe0A\x01\x12\x12\n\x05nonce\x18\x02 \x03(\tB\x03\xe0A\x01\x12I\n\ntoken_type\x18\x03 \x01(\x0e20.google.cloud.confidentialcomputing.v1.TokenTypeB\x03\xe0A\x01\x1a\x91\x03\n\x17AwsPrincipalTagsOptions\x12\x85\x01\n\x16allowed_principal_tags\x18\x01 \x01(\x0b2`.google.cloud.confidentialcomputing.v1.TokenOptions.AwsPrincipalTagsOptions.AllowedPrincipalTagsB\x03\xe0A\x01\x1a\xed\x01\n\x14AllowedPrincipalTags\x12\xa2\x01\n\x1acontainer_image_signatures\x18\x01 \x01(\x0b2y.google.cloud.confidentialcomputing.v1.TokenOptions.AwsPrincipalTagsOptions.AllowedPrincipalTags.ContainerImageSignaturesB\x03\xe0A\x01\x1a0\n\x18ContainerImageSignatures\x12\x14\n\x07key_ids\x18\x01 \x03(\tB\x03\xe0A\x01B\x14\n\x12token_type_options"\x8f\x03\n\x0eTpmAttestation\x12K\n\x06quotes\x18\x01 \x03(\x0b2;.google.cloud.confidentialcomputing.v1.TpmAttestation.Quote\x12\x15\n\rtcg_event_log\x18\x02 \x01(\x0c\x12\x1b\n\x13canonical_event_log\x18\x03 \x01(\x0c\x12\x0f\n\x07ak_cert\x18\x04 \x01(\x0c\x12\x12\n\ncert_chain\x18\x05 \x03(\x0c\x1a\xd6\x01\n\x05Quote\x12\x11\n\thash_algo\x18\x01 \x01(\x05\x12^\n\npcr_values\x18\x02 \x03(\x0b2J.google.cloud.confidentialcomputing.v1.TpmAttestation.Quote.PcrValuesEntry\x12\x11\n\traw_quote\x18\x03 \x01(\x0c\x12\x15\n\rraw_signature\x18\x04 \x01(\x0c\x1a0\n\x0ePcrValuesEntry\x12\x0b\n\x03key\x18\x01 \x01(\x05\x12\r\n\x05value\x18\x02 \x01(\x0c:\x028\x01"j\n\x15ConfidentialSpaceInfo\x12Q\n\x0fsigned_entities\x18\x01 \x03(\x0b23.google.cloud.confidentialcomputing.v1.SignedEntityB\x03\xe0A\x01"w\n\x0cSignedEntity\x12g\n\x1acontainer_image_signatures\x18\x01 \x03(\x0b2>.google.cloud.confidentialcomputing.v1.ContainerImageSignatureB\x03\xe0A\x01"\xaf\x01\n\x17ContainerImageSignature\x12\x14\n\x07payload\x18\x01 \x01(\x0cB\x03\xe0A\x01\x12\x16\n\tsignature\x18\x02 \x01(\x0cB\x03\xe0A\x01\x12\x17\n\npublic_key\x18\x03 \x01(\x0cB\x03\xe0A\x01\x12M\n\x07sig_alg\x18\x04 \x01(\x0e27.google.cloud.confidentialcomputing.v1.SigningAlgorithmB\x03\xe0A\x01*\x7f\n\x10SigningAlgorithm\x12!\n\x1dSIGNING_ALGORITHM_UNSPECIFIED\x10\x00\x12\x15\n\x11RSASSA_PSS_SHA256\x10\x01\x12\x1a\n\x16RSASSA_PKCS1V15_SHA256\x10\x02\x12\x15\n\x11ECDSA_P256_SHA256\x10\x03*\x8e\x01\n\tTokenType\x12\x1a\n\x16TOKEN_TYPE_UNSPECIFIED\x10\x00\x12\x13\n\x0fTOKEN_TYPE_OIDC\x10\x01\x12\x12\n\x0eTOKEN_TYPE_PKI\x10\x02\x12\x1a\n\x16TOKEN_TYPE_LIMITED_AWS\x10\x03\x12 \n\x1cTOKEN_TYPE_AWS_PRINCIPALTAGS\x10\x042\xb7\x04\n\x15ConfidentialComputing\x12\xd8\x01\n\x0fCreateChallenge\x12=.google.cloud.confidentialcomputing.v1.CreateChallengeRequest\x1a0.google.cloud.confidentialcomputing.v1.Challenge"T\xdaA\x10parent,challenge\x82\xd3\xe4\x93\x02;"./v1/{parent=projects/*/locations/*}/challenges:\tchallenge\x12\xe8\x01\n\x11VerifyAttestation\x12?.google.cloud.confidentialcomputing.v1.VerifyAttestationRequest\x1a@.google.cloud.confidentialcomputing.v1.VerifyAttestationResponse"P\x82\xd3\xe4\x93\x02J"E/v1/{challenge=projects/*/locations/*/challenges/*}:verifyAttestation:\x01*\x1aX\xcaA$confidentialcomputing.googleapis.com\xd2A.https://www.googleapis.com/auth/cloud-platformB\x97\x02\n)com.google.cloud.confidentialcomputing.v1B\x0cServiceProtoP\x01Z_cloud.google.com/go/confidentialcomputing/apiv1/confidentialcomputingpb;confidentialcomputingpb\xaa\x02%Google.Cloud.ConfidentialComputing.V1\xca\x02%Google\\Cloud\\ConfidentialComputing\\V1\xea\x02(Google::Cloud::ConfidentialComputing::V1b\x06proto3')
_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'google.cloud.confidentialcomputing.v1.service_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
    _globals['DESCRIPTOR']._loaded_options = None
    _globals['DESCRIPTOR']._serialized_options = b'\n)com.google.cloud.confidentialcomputing.v1B\x0cServiceProtoP\x01Z_cloud.google.com/go/confidentialcomputing/apiv1/confidentialcomputingpb;confidentialcomputingpb\xaa\x02%Google.Cloud.ConfidentialComputing.V1\xca\x02%Google\\Cloud\\ConfidentialComputing\\V1\xea\x02(Google::Cloud::ConfidentialComputing::V1'
    _globals['_CHALLENGE'].fields_by_name['name']._loaded_options = None
    _globals['_CHALLENGE'].fields_by_name['name']._serialized_options = b'\xe0A\x03'
    _globals['_CHALLENGE'].fields_by_name['create_time']._loaded_options = None
    _globals['_CHALLENGE'].fields_by_name['create_time']._serialized_options = b'\xe0A\x03'
    _globals['_CHALLENGE'].fields_by_name['expire_time']._loaded_options = None
    _globals['_CHALLENGE'].fields_by_name['expire_time']._serialized_options = b'\xe0A\x03'
    _globals['_CHALLENGE'].fields_by_name['used']._loaded_options = None
    _globals['_CHALLENGE'].fields_by_name['used']._serialized_options = b'\xe0A\x03'
    _globals['_CHALLENGE'].fields_by_name['tpm_nonce']._loaded_options = None
    _globals['_CHALLENGE'].fields_by_name['tpm_nonce']._serialized_options = b'\xe0A\x03'
    _globals['_CHALLENGE']._loaded_options = None
    _globals['_CHALLENGE']._serialized_options = b'\xeaAk\n.confidentialcomputing.googleapis.com/Challenge\x129projects/{project}/locations/{location}/challenges/{uuid}'
    _globals['_CREATECHALLENGEREQUEST'].fields_by_name['parent']._loaded_options = None
    _globals['_CREATECHALLENGEREQUEST'].fields_by_name['parent']._serialized_options = b'\xe0A\x02\xfaA#\n!locations.googleapis.com/Location'
    _globals['_CREATECHALLENGEREQUEST'].fields_by_name['challenge']._loaded_options = None
    _globals['_CREATECHALLENGEREQUEST'].fields_by_name['challenge']._serialized_options = b'\xe0A\x02'
    _globals['_VERIFYATTESTATIONREQUEST'].fields_by_name['td_ccel']._loaded_options = None
    _globals['_VERIFYATTESTATIONREQUEST'].fields_by_name['td_ccel']._serialized_options = b'\xe0A\x01'
    _globals['_VERIFYATTESTATIONREQUEST'].fields_by_name['sev_snp_attestation']._loaded_options = None
    _globals['_VERIFYATTESTATIONREQUEST'].fields_by_name['sev_snp_attestation']._serialized_options = b'\xe0A\x01'
    _globals['_VERIFYATTESTATIONREQUEST'].fields_by_name['challenge']._loaded_options = None
    _globals['_VERIFYATTESTATIONREQUEST'].fields_by_name['challenge']._serialized_options = b'\xe0A\x02\xfaA0\n.confidentialcomputing.googleapis.com/Challenge'
    _globals['_VERIFYATTESTATIONREQUEST'].fields_by_name['gcp_credentials']._loaded_options = None
    _globals['_VERIFYATTESTATIONREQUEST'].fields_by_name['gcp_credentials']._serialized_options = b'\xe0A\x01'
    _globals['_VERIFYATTESTATIONREQUEST'].fields_by_name['tpm_attestation']._loaded_options = None
    _globals['_VERIFYATTESTATIONREQUEST'].fields_by_name['tpm_attestation']._serialized_options = b'\xe0A\x02'
    _globals['_VERIFYATTESTATIONREQUEST'].fields_by_name['confidential_space_info']._loaded_options = None
    _globals['_VERIFYATTESTATIONREQUEST'].fields_by_name['confidential_space_info']._serialized_options = b'\xe0A\x01'
    _globals['_VERIFYATTESTATIONREQUEST'].fields_by_name['token_options']._loaded_options = None
    _globals['_VERIFYATTESTATIONREQUEST'].fields_by_name['token_options']._serialized_options = b'\xe0A\x01'
    _globals['_TDXCCELATTESTATION'].fields_by_name['ccel_acpi_table']._loaded_options = None
    _globals['_TDXCCELATTESTATION'].fields_by_name['ccel_acpi_table']._serialized_options = b'\xe0A\x01'
    _globals['_TDXCCELATTESTATION'].fields_by_name['ccel_data']._loaded_options = None
    _globals['_TDXCCELATTESTATION'].fields_by_name['ccel_data']._serialized_options = b'\xe0A\x01'
    _globals['_TDXCCELATTESTATION'].fields_by_name['canonical_event_log']._loaded_options = None
    _globals['_TDXCCELATTESTATION'].fields_by_name['canonical_event_log']._serialized_options = b'\xe0A\x01'
    _globals['_TDXCCELATTESTATION'].fields_by_name['td_quote']._loaded_options = None
    _globals['_TDXCCELATTESTATION'].fields_by_name['td_quote']._serialized_options = b'\xe0A\x01'
    _globals['_SEVSNPATTESTATION'].fields_by_name['report']._loaded_options = None
    _globals['_SEVSNPATTESTATION'].fields_by_name['report']._serialized_options = b'\xe0A\x01'
    _globals['_SEVSNPATTESTATION'].fields_by_name['aux_blob']._loaded_options = None
    _globals['_SEVSNPATTESTATION'].fields_by_name['aux_blob']._serialized_options = b'\xe0A\x01'
    _globals['_VERIFYATTESTATIONRESPONSE'].fields_by_name['oidc_claims_token']._loaded_options = None
    _globals['_VERIFYATTESTATIONRESPONSE'].fields_by_name['oidc_claims_token']._serialized_options = b'\xe0A\x03'
    _globals['_VERIFYATTESTATIONRESPONSE'].fields_by_name['partial_errors']._loaded_options = None
    _globals['_VERIFYATTESTATIONRESPONSE'].fields_by_name['partial_errors']._serialized_options = b'\xe0A\x03'
    _globals['_TOKENOPTIONS_AWSPRINCIPALTAGSOPTIONS_ALLOWEDPRINCIPALTAGS_CONTAINERIMAGESIGNATURES'].fields_by_name['key_ids']._loaded_options = None
    _globals['_TOKENOPTIONS_AWSPRINCIPALTAGSOPTIONS_ALLOWEDPRINCIPALTAGS_CONTAINERIMAGESIGNATURES'].fields_by_name['key_ids']._serialized_options = b'\xe0A\x01'
    _globals['_TOKENOPTIONS_AWSPRINCIPALTAGSOPTIONS_ALLOWEDPRINCIPALTAGS'].fields_by_name['container_image_signatures']._loaded_options = None
    _globals['_TOKENOPTIONS_AWSPRINCIPALTAGSOPTIONS_ALLOWEDPRINCIPALTAGS'].fields_by_name['container_image_signatures']._serialized_options = b'\xe0A\x01'
    _globals['_TOKENOPTIONS_AWSPRINCIPALTAGSOPTIONS'].fields_by_name['allowed_principal_tags']._loaded_options = None
    _globals['_TOKENOPTIONS_AWSPRINCIPALTAGSOPTIONS'].fields_by_name['allowed_principal_tags']._serialized_options = b'\xe0A\x01'
    _globals['_TOKENOPTIONS'].fields_by_name['aws_principal_tags_options']._loaded_options = None
    _globals['_TOKENOPTIONS'].fields_by_name['aws_principal_tags_options']._serialized_options = b'\xe0A\x01'
    _globals['_TOKENOPTIONS'].fields_by_name['audience']._loaded_options = None
    _globals['_TOKENOPTIONS'].fields_by_name['audience']._serialized_options = b'\xe0A\x01'
    _globals['_TOKENOPTIONS'].fields_by_name['nonce']._loaded_options = None
    _globals['_TOKENOPTIONS'].fields_by_name['nonce']._serialized_options = b'\xe0A\x01'
    _globals['_TOKENOPTIONS'].fields_by_name['token_type']._loaded_options = None
    _globals['_TOKENOPTIONS'].fields_by_name['token_type']._serialized_options = b'\xe0A\x01'
    _globals['_TPMATTESTATION_QUOTE_PCRVALUESENTRY']._loaded_options = None
    _globals['_TPMATTESTATION_QUOTE_PCRVALUESENTRY']._serialized_options = b'8\x01'
    _globals['_CONFIDENTIALSPACEINFO'].fields_by_name['signed_entities']._loaded_options = None
    _globals['_CONFIDENTIALSPACEINFO'].fields_by_name['signed_entities']._serialized_options = b'\xe0A\x01'
    _globals['_SIGNEDENTITY'].fields_by_name['container_image_signatures']._loaded_options = None
    _globals['_SIGNEDENTITY'].fields_by_name['container_image_signatures']._serialized_options = b'\xe0A\x01'
    _globals['_CONTAINERIMAGESIGNATURE'].fields_by_name['payload']._loaded_options = None
    _globals['_CONTAINERIMAGESIGNATURE'].fields_by_name['payload']._serialized_options = b'\xe0A\x01'
    _globals['_CONTAINERIMAGESIGNATURE'].fields_by_name['signature']._loaded_options = None
    _globals['_CONTAINERIMAGESIGNATURE'].fields_by_name['signature']._serialized_options = b'\xe0A\x01'
    _globals['_CONTAINERIMAGESIGNATURE'].fields_by_name['public_key']._loaded_options = None
    _globals['_CONTAINERIMAGESIGNATURE'].fields_by_name['public_key']._serialized_options = b'\xe0A\x01'
    _globals['_CONTAINERIMAGESIGNATURE'].fields_by_name['sig_alg']._loaded_options = None
    _globals['_CONTAINERIMAGESIGNATURE'].fields_by_name['sig_alg']._serialized_options = b'\xe0A\x01'
    _globals['_CONFIDENTIALCOMPUTING']._loaded_options = None
    _globals['_CONFIDENTIALCOMPUTING']._serialized_options = b'\xcaA$confidentialcomputing.googleapis.com\xd2A.https://www.googleapis.com/auth/cloud-platform'
    _globals['_CONFIDENTIALCOMPUTING'].methods_by_name['CreateChallenge']._loaded_options = None
    _globals['_CONFIDENTIALCOMPUTING'].methods_by_name['CreateChallenge']._serialized_options = b'\xdaA\x10parent,challenge\x82\xd3\xe4\x93\x02;"./v1/{parent=projects/*/locations/*}/challenges:\tchallenge'
    _globals['_CONFIDENTIALCOMPUTING'].methods_by_name['VerifyAttestation']._loaded_options = None
    _globals['_CONFIDENTIALCOMPUTING'].methods_by_name['VerifyAttestation']._serialized_options = b'\x82\xd3\xe4\x93\x02J"E/v1/{challenge=projects/*/locations/*/challenges/*}:verifyAttestation:\x01*'
    _globals['_SIGNINGALGORITHM']._serialized_start = 3226
    _globals['_SIGNINGALGORITHM']._serialized_end = 3353
    _globals['_TOKENTYPE']._serialized_start = 3356
    _globals['_TOKENTYPE']._serialized_end = 3498
    _globals['_CHALLENGE']._serialized_start = 268
    _globals['_CHALLENGE']._serialized_end = 561
    _globals['_CREATECHALLENGEREQUEST']._serialized_start = 564
    _globals['_CREATECHALLENGEREQUEST']._serialized_end = 721
    _globals['_VERIFYATTESTATIONREQUEST']._serialized_start = 724
    _globals['_VERIFYATTESTATIONREQUEST']._serialized_end = 1372
    _globals['_TDXCCELATTESTATION']._serialized_start = 1375
    _globals['_TDXCCELATTESTATION']._serialized_end = 1506
    _globals['_SEVSNPATTESTATION']._serialized_start = 1508
    _globals['_SEVSNPATTESTATION']._serialized_end = 1571
    _globals['_VERIFYATTESTATIONRESPONSE']._serialized_start = 1573
    _globals['_VERIFYATTESTATIONRESPONSE']._serialized_end = 1681
    _globals['_GCPCREDENTIALS']._serialized_start = 1683
    _globals['_GCPCREDENTIALS']._serialized_end = 1734
    _globals['_TOKENOPTIONS']._serialized_start = 1737
    _globals['_TOKENOPTIONS']._serialized_end = 2415
    _globals['_TOKENOPTIONS_AWSPRINCIPALTAGSOPTIONS']._serialized_start = 1992
    _globals['_TOKENOPTIONS_AWSPRINCIPALTAGSOPTIONS']._serialized_end = 2393
    _globals['_TOKENOPTIONS_AWSPRINCIPALTAGSOPTIONS_ALLOWEDPRINCIPALTAGS']._serialized_start = 2156
    _globals['_TOKENOPTIONS_AWSPRINCIPALTAGSOPTIONS_ALLOWEDPRINCIPALTAGS']._serialized_end = 2393
    _globals['_TOKENOPTIONS_AWSPRINCIPALTAGSOPTIONS_ALLOWEDPRINCIPALTAGS_CONTAINERIMAGESIGNATURES']._serialized_start = 2345
    _globals['_TOKENOPTIONS_AWSPRINCIPALTAGSOPTIONS_ALLOWEDPRINCIPALTAGS_CONTAINERIMAGESIGNATURES']._serialized_end = 2393
    _globals['_TPMATTESTATION']._serialized_start = 2418
    _globals['_TPMATTESTATION']._serialized_end = 2817
    _globals['_TPMATTESTATION_QUOTE']._serialized_start = 2603
    _globals['_TPMATTESTATION_QUOTE']._serialized_end = 2817
    _globals['_TPMATTESTATION_QUOTE_PCRVALUESENTRY']._serialized_start = 2769
    _globals['_TPMATTESTATION_QUOTE_PCRVALUESENTRY']._serialized_end = 2817
    _globals['_CONFIDENTIALSPACEINFO']._serialized_start = 2819
    _globals['_CONFIDENTIALSPACEINFO']._serialized_end = 2925
    _globals['_SIGNEDENTITY']._serialized_start = 2927
    _globals['_SIGNEDENTITY']._serialized_end = 3046
    _globals['_CONTAINERIMAGESIGNATURE']._serialized_start = 3049
    _globals['_CONTAINERIMAGESIGNATURE']._serialized_end = 3224
    _globals['_CONFIDENTIALCOMPUTING']._serialized_start = 3501
    _globals['_CONFIDENTIALCOMPUTING']._serialized_end = 4068