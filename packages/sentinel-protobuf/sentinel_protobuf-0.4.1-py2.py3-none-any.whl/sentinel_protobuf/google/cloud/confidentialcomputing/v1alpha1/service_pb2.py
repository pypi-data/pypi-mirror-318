"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_runtime_version.ValidateProtobufRuntimeVersion(_runtime_version.Domain.PUBLIC, 5, 28, 1, '', 'google/cloud/confidentialcomputing/v1alpha1/service.proto')
_sym_db = _symbol_database.Default()
from .....google.api import annotations_pb2 as google_dot_api_dot_annotations__pb2
from .....google.api import client_pb2 as google_dot_api_dot_client__pb2
from .....google.api import field_behavior_pb2 as google_dot_api_dot_field__behavior__pb2
from .....google.api import resource_pb2 as google_dot_api_dot_resource__pb2
from google.protobuf import timestamp_pb2 as google_dot_protobuf_dot_timestamp__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n9google/cloud/confidentialcomputing/v1alpha1/service.proto\x12+google.cloud.confidentialcomputing.v1alpha1\x1a\x1cgoogle/api/annotations.proto\x1a\x17google/api/client.proto\x1a\x1fgoogle/api/field_behavior.proto\x1a\x19google/api/resource.proto\x1a\x1fgoogle/protobuf/timestamp.proto"\xa1\x02\n\tChallenge\x12\x11\n\x04name\x18\x01 \x01(\tB\x03\xe0A\x03\x124\n\x0bcreate_time\x18\x02 \x01(\x0b2\x1a.google.protobuf.TimestampB\x03\xe0A\x03\x124\n\x0bexpire_time\x18\x03 \x01(\x0b2\x1a.google.protobuf.TimestampB\x03\xe0A\x03\x12\x11\n\x04used\x18\x04 \x01(\x08B\x03\xe0A\x03\x12\x12\n\x05nonce\x18\x05 \x01(\x0cB\x03\xe0A\x03:n\xeaAk\n.confidentialcomputing.googleapis.com/Challenge\x129projects/{project}/locations/{location}/challenges/{uuid}"\xa3\x01\n\x16CreateChallengeRequest\x129\n\x06parent\x18\x01 \x01(\tB)\xe0A\x02\xfaA#\n!locations.googleapis.com/Location\x12N\n\tchallenge\x18\x02 \x01(\x0b26.google.cloud.confidentialcomputing.v1alpha1.ChallengeB\x03\xe0A\x02"\x9b\x02\n\x18VerifyAttestationRequest\x12I\n\tchallenge\x18\x01 \x01(\tB6\xe0A\x02\xfaA0\n.confidentialcomputing.googleapis.com/Challenge\x12Y\n\x0fgcp_credentials\x18\x02 \x01(\x0b2;.google.cloud.confidentialcomputing.v1alpha1.GcpCredentialsB\x03\xe0A\x01\x12Y\n\x0ftpm_attestation\x18\x03 \x01(\x0b2;.google.cloud.confidentialcomputing.v1alpha1.TpmAttestationB\x03\xe0A\x02"6\n\x19VerifyAttestationResponse\x12\x19\n\x0cclaims_token\x18\x01 \x01(\x0cB\x03\xe0A\x03"#\n\x0eGcpCredentials\x12\x11\n\tid_tokens\x18\x01 \x03(\x0c"\x9b\x03\n\x0eTpmAttestation\x12Q\n\x06quotes\x18\x01 \x03(\x0b2A.google.cloud.confidentialcomputing.v1alpha1.TpmAttestation.Quote\x12\x15\n\rtcg_event_log\x18\x02 \x01(\x0c\x12\x1b\n\x13canonical_event_log\x18\x03 \x01(\x0c\x12\x0f\n\x07ak_cert\x18\x04 \x01(\x0c\x12\x12\n\ncert_chain\x18\x05 \x03(\x0c\x1a\xdc\x01\n\x05Quote\x12\x11\n\thash_algo\x18\x01 \x01(\x05\x12d\n\npcr_values\x18\x02 \x03(\x0b2P.google.cloud.confidentialcomputing.v1alpha1.TpmAttestation.Quote.PcrValuesEntry\x12\x11\n\traw_quote\x18\x03 \x01(\x0c\x12\x15\n\rraw_signature\x18\x04 \x01(\x0c\x1a0\n\x0ePcrValuesEntry\x12\x0b\n\x03key\x18\x01 \x01(\x05\x12\r\n\x05value\x18\x02 \x01(\x0c:\x028\x012\xdb\x04\n\x15ConfidentialComputing\x12\xea\x01\n\x0fCreateChallenge\x12C.google.cloud.confidentialcomputing.v1alpha1.CreateChallengeRequest\x1a6.google.cloud.confidentialcomputing.v1alpha1.Challenge"Z\xdaA\x10parent,challenge\x82\xd3\xe4\x93\x02A"4/v1alpha1/{parent=projects/*/locations/*}/challenges:\tchallenge\x12\xfa\x01\n\x11VerifyAttestation\x12E.google.cloud.confidentialcomputing.v1alpha1.VerifyAttestationRequest\x1aF.google.cloud.confidentialcomputing.v1alpha1.VerifyAttestationResponse"V\x82\xd3\xe4\x93\x02P"K/v1alpha1/{challenge=projects/*/locations/*/challenges/*}:verifyAttestation:\x01*\x1aX\xcaA$confidentialcomputing.googleapis.com\xd2A.https://www.googleapis.com/auth/cloud-platformB\xb5\x02\n/com.google.cloud.confidentialcomputing.v1alpha1B\x0cServiceProtoP\x01Zecloud.google.com/go/confidentialcomputing/apiv1alpha1/confidentialcomputingpb;confidentialcomputingpb\xaa\x02+Google.Cloud.ConfidentialComputing.V1Alpha1\xca\x02+Google\\Cloud\\ConfidentialComputing\\V1alpha1\xea\x02.Google::Cloud::ConfidentialComputing::V1alpha1b\x06proto3')
_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'google.cloud.confidentialcomputing.v1alpha1.service_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
    _globals['DESCRIPTOR']._loaded_options = None
    _globals['DESCRIPTOR']._serialized_options = b'\n/com.google.cloud.confidentialcomputing.v1alpha1B\x0cServiceProtoP\x01Zecloud.google.com/go/confidentialcomputing/apiv1alpha1/confidentialcomputingpb;confidentialcomputingpb\xaa\x02+Google.Cloud.ConfidentialComputing.V1Alpha1\xca\x02+Google\\Cloud\\ConfidentialComputing\\V1alpha1\xea\x02.Google::Cloud::ConfidentialComputing::V1alpha1'
    _globals['_CHALLENGE'].fields_by_name['name']._loaded_options = None
    _globals['_CHALLENGE'].fields_by_name['name']._serialized_options = b'\xe0A\x03'
    _globals['_CHALLENGE'].fields_by_name['create_time']._loaded_options = None
    _globals['_CHALLENGE'].fields_by_name['create_time']._serialized_options = b'\xe0A\x03'
    _globals['_CHALLENGE'].fields_by_name['expire_time']._loaded_options = None
    _globals['_CHALLENGE'].fields_by_name['expire_time']._serialized_options = b'\xe0A\x03'
    _globals['_CHALLENGE'].fields_by_name['used']._loaded_options = None
    _globals['_CHALLENGE'].fields_by_name['used']._serialized_options = b'\xe0A\x03'
    _globals['_CHALLENGE'].fields_by_name['nonce']._loaded_options = None
    _globals['_CHALLENGE'].fields_by_name['nonce']._serialized_options = b'\xe0A\x03'
    _globals['_CHALLENGE']._loaded_options = None
    _globals['_CHALLENGE']._serialized_options = b'\xeaAk\n.confidentialcomputing.googleapis.com/Challenge\x129projects/{project}/locations/{location}/challenges/{uuid}'
    _globals['_CREATECHALLENGEREQUEST'].fields_by_name['parent']._loaded_options = None
    _globals['_CREATECHALLENGEREQUEST'].fields_by_name['parent']._serialized_options = b'\xe0A\x02\xfaA#\n!locations.googleapis.com/Location'
    _globals['_CREATECHALLENGEREQUEST'].fields_by_name['challenge']._loaded_options = None
    _globals['_CREATECHALLENGEREQUEST'].fields_by_name['challenge']._serialized_options = b'\xe0A\x02'
    _globals['_VERIFYATTESTATIONREQUEST'].fields_by_name['challenge']._loaded_options = None
    _globals['_VERIFYATTESTATIONREQUEST'].fields_by_name['challenge']._serialized_options = b'\xe0A\x02\xfaA0\n.confidentialcomputing.googleapis.com/Challenge'
    _globals['_VERIFYATTESTATIONREQUEST'].fields_by_name['gcp_credentials']._loaded_options = None
    _globals['_VERIFYATTESTATIONREQUEST'].fields_by_name['gcp_credentials']._serialized_options = b'\xe0A\x01'
    _globals['_VERIFYATTESTATIONREQUEST'].fields_by_name['tpm_attestation']._loaded_options = None
    _globals['_VERIFYATTESTATIONREQUEST'].fields_by_name['tpm_attestation']._serialized_options = b'\xe0A\x02'
    _globals['_VERIFYATTESTATIONRESPONSE'].fields_by_name['claims_token']._loaded_options = None
    _globals['_VERIFYATTESTATIONRESPONSE'].fields_by_name['claims_token']._serialized_options = b'\xe0A\x03'
    _globals['_TPMATTESTATION_QUOTE_PCRVALUESENTRY']._loaded_options = None
    _globals['_TPMATTESTATION_QUOTE_PCRVALUESENTRY']._serialized_options = b'8\x01'
    _globals['_CONFIDENTIALCOMPUTING']._loaded_options = None
    _globals['_CONFIDENTIALCOMPUTING']._serialized_options = b'\xcaA$confidentialcomputing.googleapis.com\xd2A.https://www.googleapis.com/auth/cloud-platform'
    _globals['_CONFIDENTIALCOMPUTING'].methods_by_name['CreateChallenge']._loaded_options = None
    _globals['_CONFIDENTIALCOMPUTING'].methods_by_name['CreateChallenge']._serialized_options = b'\xdaA\x10parent,challenge\x82\xd3\xe4\x93\x02A"4/v1alpha1/{parent=projects/*/locations/*}/challenges:\tchallenge'
    _globals['_CONFIDENTIALCOMPUTING'].methods_by_name['VerifyAttestation']._loaded_options = None
    _globals['_CONFIDENTIALCOMPUTING'].methods_by_name['VerifyAttestation']._serialized_options = b'\x82\xd3\xe4\x93\x02P"K/v1alpha1/{challenge=projects/*/locations/*/challenges/*}:verifyAttestation:\x01*'
    _globals['_CHALLENGE']._serialized_start = 255
    _globals['_CHALLENGE']._serialized_end = 544
    _globals['_CREATECHALLENGEREQUEST']._serialized_start = 547
    _globals['_CREATECHALLENGEREQUEST']._serialized_end = 710
    _globals['_VERIFYATTESTATIONREQUEST']._serialized_start = 713
    _globals['_VERIFYATTESTATIONREQUEST']._serialized_end = 996
    _globals['_VERIFYATTESTATIONRESPONSE']._serialized_start = 998
    _globals['_VERIFYATTESTATIONRESPONSE']._serialized_end = 1052
    _globals['_GCPCREDENTIALS']._serialized_start = 1054
    _globals['_GCPCREDENTIALS']._serialized_end = 1089
    _globals['_TPMATTESTATION']._serialized_start = 1092
    _globals['_TPMATTESTATION']._serialized_end = 1503
    _globals['_TPMATTESTATION_QUOTE']._serialized_start = 1283
    _globals['_TPMATTESTATION_QUOTE']._serialized_end = 1503
    _globals['_TPMATTESTATION_QUOTE_PCRVALUESENTRY']._serialized_start = 1455
    _globals['_TPMATTESTATION_QUOTE_PCRVALUESENTRY']._serialized_end = 1503
    _globals['_CONFIDENTIALCOMPUTING']._serialized_start = 1506
    _globals['_CONFIDENTIALCOMPUTING']._serialized_end = 2109