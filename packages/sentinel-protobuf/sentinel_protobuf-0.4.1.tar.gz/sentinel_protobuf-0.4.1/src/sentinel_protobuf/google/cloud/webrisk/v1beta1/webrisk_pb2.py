"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_runtime_version.ValidateProtobufRuntimeVersion(_runtime_version.Domain.PUBLIC, 5, 28, 1, '', 'google/cloud/webrisk/v1beta1/webrisk.proto')
_sym_db = _symbol_database.Default()
from .....google.api import annotations_pb2 as google_dot_api_dot_annotations__pb2
from .....google.api import client_pb2 as google_dot_api_dot_client__pb2
from .....google.api import field_behavior_pb2 as google_dot_api_dot_field__behavior__pb2
from google.protobuf import timestamp_pb2 as google_dot_protobuf_dot_timestamp__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n*google/cloud/webrisk/v1beta1/webrisk.proto\x12\x1cgoogle.cloud.webrisk.v1beta1\x1a\x1cgoogle/api/annotations.proto\x1a\x17google/api/client.proto\x1a\x1fgoogle/api/field_behavior.proto\x1a\x1fgoogle/protobuf/timestamp.proto"\xf2\x02\n\x1cComputeThreatListDiffRequest\x12B\n\x0bthreat_type\x18\x01 \x01(\x0e2(.google.cloud.webrisk.v1beta1.ThreatTypeB\x03\xe0A\x02\x12\x15\n\rversion_token\x18\x02 \x01(\x0c\x12`\n\x0bconstraints\x18\x03 \x01(\x0b2F.google.cloud.webrisk.v1beta1.ComputeThreatListDiffRequest.ConstraintsB\x03\xe0A\x02\x1a\x94\x01\n\x0bConstraints\x12\x18\n\x10max_diff_entries\x18\x01 \x01(\x05\x12\x1c\n\x14max_database_entries\x18\x02 \x01(\x05\x12M\n\x16supported_compressions\x18\x03 \x03(\x0e2-.google.cloud.webrisk.v1beta1.CompressionType"\x9a\x04\n\x1dComputeThreatListDiffResponse\x12_\n\rresponse_type\x18\x04 \x01(\x0e2H.google.cloud.webrisk.v1beta1.ComputeThreatListDiffResponse.ResponseType\x12E\n\tadditions\x18\x05 \x01(\x0b22.google.cloud.webrisk.v1beta1.ThreatEntryAdditions\x12C\n\x08removals\x18\x06 \x01(\x0b21.google.cloud.webrisk.v1beta1.ThreatEntryRemovals\x12\x19\n\x11new_version_token\x18\x07 \x01(\x0c\x12V\n\x08checksum\x18\x08 \x01(\x0b2D.google.cloud.webrisk.v1beta1.ComputeThreatListDiffResponse.Checksum\x129\n\x15recommended_next_diff\x18\x02 \x01(\x0b2\x1a.google.protobuf.Timestamp\x1a\x1a\n\x08Checksum\x12\x0e\n\x06sha256\x18\x01 \x01(\x0c"B\n\x0cResponseType\x12\x1d\n\x19RESPONSE_TYPE_UNSPECIFIED\x10\x00\x12\x08\n\x04DIFF\x10\x01\x12\t\n\x05RESET\x10\x02"j\n\x11SearchUrisRequest\x12\x10\n\x03uri\x18\x01 \x01(\tB\x03\xe0A\x02\x12C\n\x0cthreat_types\x18\x02 \x03(\x0e2(.google.cloud.webrisk.v1beta1.ThreatTypeB\x03\xe0A\x02"\xde\x01\n\x12SearchUrisResponse\x12J\n\x06threat\x18\x01 \x01(\x0b2:.google.cloud.webrisk.v1beta1.SearchUrisResponse.ThreatUri\x1a|\n\tThreatUri\x12>\n\x0cthreat_types\x18\x01 \x03(\x0e2(.google.cloud.webrisk.v1beta1.ThreatType\x12/\n\x0bexpire_time\x18\x02 \x01(\x0b2\x1a.google.protobuf.Timestamp"o\n\x13SearchHashesRequest\x12\x13\n\x0bhash_prefix\x18\x01 \x01(\x0c\x12C\n\x0cthreat_types\x18\x02 \x03(\x0e2(.google.cloud.webrisk.v1beta1.ThreatTypeB\x03\xe0A\x02"\xae\x02\n\x14SearchHashesResponse\x12N\n\x07threats\x18\x01 \x03(\x0b2=.google.cloud.webrisk.v1beta1.SearchHashesResponse.ThreatHash\x128\n\x14negative_expire_time\x18\x02 \x01(\x0b2\x1a.google.protobuf.Timestamp\x1a\x8b\x01\n\nThreatHash\x12>\n\x0cthreat_types\x18\x01 \x03(\x0e2(.google.cloud.webrisk.v1beta1.ThreatType\x12\x0c\n\x04hash\x18\x02 \x01(\x0c\x12/\n\x0bexpire_time\x18\x03 \x01(\x0b2\x1a.google.protobuf.Timestamp"\x99\x01\n\x14ThreatEntryAdditions\x12;\n\nraw_hashes\x18\x01 \x03(\x0b2\'.google.cloud.webrisk.v1beta1.RawHashes\x12D\n\x0brice_hashes\x18\x02 \x01(\x0b2/.google.cloud.webrisk.v1beta1.RiceDeltaEncoding"\x9b\x01\n\x13ThreatEntryRemovals\x12=\n\x0braw_indices\x18\x01 \x01(\x0b2(.google.cloud.webrisk.v1beta1.RawIndices\x12E\n\x0crice_indices\x18\x02 \x01(\x0b2/.google.cloud.webrisk.v1beta1.RiceDeltaEncoding"\x1d\n\nRawIndices\x12\x0f\n\x07indices\x18\x01 \x03(\x05"4\n\tRawHashes\x12\x13\n\x0bprefix_size\x18\x01 \x01(\x05\x12\x12\n\nraw_hashes\x18\x02 \x01(\x0c"k\n\x11RiceDeltaEncoding\x12\x13\n\x0bfirst_value\x18\x01 \x01(\x03\x12\x16\n\x0erice_parameter\x18\x02 \x01(\x05\x12\x13\n\x0bentry_count\x18\x03 \x01(\x05\x12\x14\n\x0cencoded_data\x18\x04 \x01(\x0c*e\n\nThreatType\x12\x1b\n\x17THREAT_TYPE_UNSPECIFIED\x10\x00\x12\x0b\n\x07MALWARE\x10\x01\x12\x16\n\x12SOCIAL_ENGINEERING\x10\x02\x12\x15\n\x11UNWANTED_SOFTWARE\x10\x03*F\n\x0fCompressionType\x12 \n\x1cCOMPRESSION_TYPE_UNSPECIFIED\x10\x00\x12\x07\n\x03RAW\x10\x01\x12\x08\n\x04RICE\x10\x022\x9e\x05\n\x15WebRiskServiceV1Beta1\x12\xe2\x01\n\x15ComputeThreatListDiff\x12:.google.cloud.webrisk.v1beta1.ComputeThreatListDiffRequest\x1a;.google.cloud.webrisk.v1beta1.ComputeThreatListDiffResponse"P\xdaA%threat_type,version_token,constraints\x82\xd3\xe4\x93\x02"\x12 /v1beta1/threatLists:computeDiff\x12\xa0\x01\n\nSearchUris\x12/.google.cloud.webrisk.v1beta1.SearchUrisRequest\x1a0.google.cloud.webrisk.v1beta1.SearchUrisResponse"/\xdaA\x10uri,threat_types\x82\xd3\xe4\x93\x02\x16\x12\x14/v1beta1/uris:search\x12\xb0\x01\n\x0cSearchHashes\x121.google.cloud.webrisk.v1beta1.SearchHashesRequest\x1a2.google.cloud.webrisk.v1beta1.SearchHashesResponse"9\xdaA\x18hash_prefix,threat_types\x82\xd3\xe4\x93\x02\x18\x12\x16/v1beta1/hashes:search\x1aJ\xcaA\x16webrisk.googleapis.com\xd2A.https://www.googleapis.com/auth/cloud-platformB\xcf\x01\n\x1acom.google.webrisk.v1beta1B\x0cWebRiskProtoP\x01Z:cloud.google.com/go/webrisk/apiv1beta1/webriskpb;webriskpb\xa2\x02\x04GCWR\xaa\x02\x1cGoogle.Cloud.WebRisk.V1Beta1\xca\x02\x1cGoogle\\Cloud\\WebRisk\\V1beta1\xea\x02\x1fGoogle::Cloud::WebRisk::V1beta1b\x06proto3')
_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'google.cloud.webrisk.v1beta1.webrisk_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
    _globals['DESCRIPTOR']._loaded_options = None
    _globals['DESCRIPTOR']._serialized_options = b'\n\x1acom.google.webrisk.v1beta1B\x0cWebRiskProtoP\x01Z:cloud.google.com/go/webrisk/apiv1beta1/webriskpb;webriskpb\xa2\x02\x04GCWR\xaa\x02\x1cGoogle.Cloud.WebRisk.V1Beta1\xca\x02\x1cGoogle\\Cloud\\WebRisk\\V1beta1\xea\x02\x1fGoogle::Cloud::WebRisk::V1beta1'
    _globals['_COMPUTETHREATLISTDIFFREQUEST'].fields_by_name['threat_type']._loaded_options = None
    _globals['_COMPUTETHREATLISTDIFFREQUEST'].fields_by_name['threat_type']._serialized_options = b'\xe0A\x02'
    _globals['_COMPUTETHREATLISTDIFFREQUEST'].fields_by_name['constraints']._loaded_options = None
    _globals['_COMPUTETHREATLISTDIFFREQUEST'].fields_by_name['constraints']._serialized_options = b'\xe0A\x02'
    _globals['_SEARCHURISREQUEST'].fields_by_name['uri']._loaded_options = None
    _globals['_SEARCHURISREQUEST'].fields_by_name['uri']._serialized_options = b'\xe0A\x02'
    _globals['_SEARCHURISREQUEST'].fields_by_name['threat_types']._loaded_options = None
    _globals['_SEARCHURISREQUEST'].fields_by_name['threat_types']._serialized_options = b'\xe0A\x02'
    _globals['_SEARCHHASHESREQUEST'].fields_by_name['threat_types']._loaded_options = None
    _globals['_SEARCHHASHESREQUEST'].fields_by_name['threat_types']._serialized_options = b'\xe0A\x02'
    _globals['_WEBRISKSERVICEV1BETA1']._loaded_options = None
    _globals['_WEBRISKSERVICEV1BETA1']._serialized_options = b'\xcaA\x16webrisk.googleapis.com\xd2A.https://www.googleapis.com/auth/cloud-platform'
    _globals['_WEBRISKSERVICEV1BETA1'].methods_by_name['ComputeThreatListDiff']._loaded_options = None
    _globals['_WEBRISKSERVICEV1BETA1'].methods_by_name['ComputeThreatListDiff']._serialized_options = b'\xdaA%threat_type,version_token,constraints\x82\xd3\xe4\x93\x02"\x12 /v1beta1/threatLists:computeDiff'
    _globals['_WEBRISKSERVICEV1BETA1'].methods_by_name['SearchUris']._loaded_options = None
    _globals['_WEBRISKSERVICEV1BETA1'].methods_by_name['SearchUris']._serialized_options = b'\xdaA\x10uri,threat_types\x82\xd3\xe4\x93\x02\x16\x12\x14/v1beta1/uris:search'
    _globals['_WEBRISKSERVICEV1BETA1'].methods_by_name['SearchHashes']._loaded_options = None
    _globals['_WEBRISKSERVICEV1BETA1'].methods_by_name['SearchHashes']._serialized_options = b'\xdaA\x18hash_prefix,threat_types\x82\xd3\xe4\x93\x02\x18\x12\x16/v1beta1/hashes:search'
    _globals['_THREATTYPE']._serialized_start = 2370
    _globals['_THREATTYPE']._serialized_end = 2471
    _globals['_COMPRESSIONTYPE']._serialized_start = 2473
    _globals['_COMPRESSIONTYPE']._serialized_end = 2543
    _globals['_COMPUTETHREATLISTDIFFREQUEST']._serialized_start = 198
    _globals['_COMPUTETHREATLISTDIFFREQUEST']._serialized_end = 568
    _globals['_COMPUTETHREATLISTDIFFREQUEST_CONSTRAINTS']._serialized_start = 420
    _globals['_COMPUTETHREATLISTDIFFREQUEST_CONSTRAINTS']._serialized_end = 568
    _globals['_COMPUTETHREATLISTDIFFRESPONSE']._serialized_start = 571
    _globals['_COMPUTETHREATLISTDIFFRESPONSE']._serialized_end = 1109
    _globals['_COMPUTETHREATLISTDIFFRESPONSE_CHECKSUM']._serialized_start = 1015
    _globals['_COMPUTETHREATLISTDIFFRESPONSE_CHECKSUM']._serialized_end = 1041
    _globals['_COMPUTETHREATLISTDIFFRESPONSE_RESPONSETYPE']._serialized_start = 1043
    _globals['_COMPUTETHREATLISTDIFFRESPONSE_RESPONSETYPE']._serialized_end = 1109
    _globals['_SEARCHURISREQUEST']._serialized_start = 1111
    _globals['_SEARCHURISREQUEST']._serialized_end = 1217
    _globals['_SEARCHURISRESPONSE']._serialized_start = 1220
    _globals['_SEARCHURISRESPONSE']._serialized_end = 1442
    _globals['_SEARCHURISRESPONSE_THREATURI']._serialized_start = 1318
    _globals['_SEARCHURISRESPONSE_THREATURI']._serialized_end = 1442
    _globals['_SEARCHHASHESREQUEST']._serialized_start = 1444
    _globals['_SEARCHHASHESREQUEST']._serialized_end = 1555
    _globals['_SEARCHHASHESRESPONSE']._serialized_start = 1558
    _globals['_SEARCHHASHESRESPONSE']._serialized_end = 1860
    _globals['_SEARCHHASHESRESPONSE_THREATHASH']._serialized_start = 1721
    _globals['_SEARCHHASHESRESPONSE_THREATHASH']._serialized_end = 1860
    _globals['_THREATENTRYADDITIONS']._serialized_start = 1863
    _globals['_THREATENTRYADDITIONS']._serialized_end = 2016
    _globals['_THREATENTRYREMOVALS']._serialized_start = 2019
    _globals['_THREATENTRYREMOVALS']._serialized_end = 2174
    _globals['_RAWINDICES']._serialized_start = 2176
    _globals['_RAWINDICES']._serialized_end = 2205
    _globals['_RAWHASHES']._serialized_start = 2207
    _globals['_RAWHASHES']._serialized_end = 2259
    _globals['_RICEDELTAENCODING']._serialized_start = 2261
    _globals['_RICEDELTAENCODING']._serialized_end = 2368
    _globals['_WEBRISKSERVICEV1BETA1']._serialized_start = 2546
    _globals['_WEBRISKSERVICEV1BETA1']._serialized_end = 3216