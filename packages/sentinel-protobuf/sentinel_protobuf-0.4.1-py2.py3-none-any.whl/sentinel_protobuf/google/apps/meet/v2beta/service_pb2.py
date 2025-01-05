"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_runtime_version.ValidateProtobufRuntimeVersion(_runtime_version.Domain.PUBLIC, 5, 28, 1, '', 'google/apps/meet/v2beta/service.proto')
_sym_db = _symbol_database.Default()
from .....google.api import annotations_pb2 as google_dot_api_dot_annotations__pb2
from .....google.api import client_pb2 as google_dot_api_dot_client__pb2
from .....google.api import field_behavior_pb2 as google_dot_api_dot_field__behavior__pb2
from .....google.api import resource_pb2 as google_dot_api_dot_resource__pb2
from .....google.apps.meet.v2beta import resource_pb2 as google_dot_apps_dot_meet_dot_v2beta_dot_resource__pb2
from google.protobuf import empty_pb2 as google_dot_protobuf_dot_empty__pb2
from google.protobuf import field_mask_pb2 as google_dot_protobuf_dot_field__mask__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n%google/apps/meet/v2beta/service.proto\x12\x17google.apps.meet.v2beta\x1a\x1cgoogle/api/annotations.proto\x1a\x17google/api/client.proto\x1a\x1fgoogle/api/field_behavior.proto\x1a\x19google/api/resource.proto\x1a&google/apps/meet/v2beta/resource.proto\x1a\x1bgoogle/protobuf/empty.proto\x1a google/protobuf/field_mask.proto"C\n\x12CreateSpaceRequest\x12-\n\x05space\x18\x01 \x01(\x0b2\x1e.google.apps.meet.v2beta.Space"B\n\x0fGetSpaceRequest\x12/\n\x04name\x18\x01 \x01(\tB!\xe0A\x02\xfaA\x1b\n\x19meet.googleapis.com/Space"~\n\x12UpdateSpaceRequest\x122\n\x05space\x18\x01 \x01(\x0b2\x1e.google.apps.meet.v2beta.SpaceB\x03\xe0A\x02\x124\n\x0bupdate_mask\x18\x02 \x01(\x0b2\x1a.google.protobuf.FieldMaskB\x03\xe0A\x01"M\n\x1aEndActiveConferenceRequest\x12/\n\x04name\x18\x01 \x01(\tB!\xe0A\x02\xfaA\x1b\n\x19meet.googleapis.com/Space"X\n\x1aGetConferenceRecordRequest\x12:\n\x04name\x18\x01 \x01(\tB,\xe0A\x02\xfaA&\n$meet.googleapis.com/ConferenceRecord"d\n\x1cListConferenceRecordsRequest\x12\x16\n\tpage_size\x18\x01 \x01(\x05B\x03\xe0A\x01\x12\x17\n\npage_token\x18\x02 \x01(\tB\x03\xe0A\x01\x12\x13\n\x06filter\x18\x03 \x01(\tB\x03\xe0A\x01"\x7f\n\x1dListConferenceRecordsResponse\x12E\n\x12conference_records\x18\x01 \x03(\x0b2).google.apps.meet.v2beta.ConferenceRecord\x12\x17\n\x0fnext_page_token\x18\x02 \x01(\t"N\n\x15GetParticipantRequest\x125\n\x04name\x18\x01 \x01(\tB\'\xe0A\x02\xfaA!\n\x1fmeet.googleapis.com/Participant"\x8e\x01\n\x17ListParticipantsRequest\x127\n\x06parent\x18\x01 \x01(\tB\'\xe0A\x02\xfaA!\x12\x1fmeet.googleapis.com/Participant\x12\x11\n\tpage_size\x18\x02 \x01(\x05\x12\x12\n\npage_token\x18\x03 \x01(\t\x12\x13\n\x06filter\x18\x04 \x01(\tB\x03\xe0A\x01"\x83\x01\n\x18ListParticipantsResponse\x12:\n\x0cparticipants\x18\x01 \x03(\x0b2$.google.apps.meet.v2beta.Participant\x12\x17\n\x0fnext_page_token\x18\x02 \x01(\t\x12\x12\n\ntotal_size\x18\x03 \x01(\x05"\\\n\x1cGetParticipantSessionRequest\x12<\n\x04name\x18\x01 \x01(\tB.\xe0A\x02\xfaA(\n&meet.googleapis.com/ParticipantSession"\xa6\x01\n\x1eListParticipantSessionsRequest\x12>\n\x06parent\x18\x01 \x01(\tB.\xe0A\x02\xfaA(\x12&meet.googleapis.com/ParticipantSession\x12\x16\n\tpage_size\x18\x02 \x01(\x05B\x03\xe0A\x01\x12\x17\n\npage_token\x18\x03 \x01(\tB\x03\xe0A\x01\x12\x13\n\x06filter\x18\x04 \x01(\tB\x03\xe0A\x01"\x85\x01\n\x1fListParticipantSessionsResponse\x12I\n\x14participant_sessions\x18\x01 \x03(\x0b2+.google.apps.meet.v2beta.ParticipantSession\x12\x17\n\x0fnext_page_token\x18\x02 \x01(\t"J\n\x13GetRecordingRequest\x123\n\x04name\x18\x01 \x01(\tB%\xe0A\x02\xfaA\x1f\n\x1dmeet.googleapis.com/Recording"u\n\x15ListRecordingsRequest\x125\n\x06parent\x18\x01 \x01(\tB%\xe0A\x02\xfaA\x1f\x12\x1dmeet.googleapis.com/Recording\x12\x11\n\tpage_size\x18\x02 \x01(\x05\x12\x12\n\npage_token\x18\x03 \x01(\t"i\n\x16ListRecordingsResponse\x126\n\nrecordings\x18\x01 \x03(\x0b2".google.apps.meet.v2beta.Recording\x12\x17\n\x0fnext_page_token\x18\x02 \x01(\t"L\n\x14GetTranscriptRequest\x124\n\x04name\x18\x01 \x01(\tB&\xe0A\x02\xfaA \n\x1emeet.googleapis.com/Transcript"w\n\x16ListTranscriptsRequest\x126\n\x06parent\x18\x01 \x01(\tB&\xe0A\x02\xfaA \x12\x1emeet.googleapis.com/Transcript\x12\x11\n\tpage_size\x18\x02 \x01(\x05\x12\x12\n\npage_token\x18\x03 \x01(\t"l\n\x17ListTranscriptsResponse\x128\n\x0btranscripts\x18\x01 \x03(\x0b2#.google.apps.meet.v2beta.Transcript\x12\x17\n\x0fnext_page_token\x18\x02 \x01(\t"V\n\x19GetTranscriptEntryRequest\x129\n\x04name\x18\x01 \x01(\tB+\xe0A\x02\xfaA%\n#meet.googleapis.com/TranscriptEntry"\x82\x01\n\x1cListTranscriptEntriesRequest\x12;\n\x06parent\x18\x01 \x01(\tB+\xe0A\x02\xfaA%\x12#meet.googleapis.com/TranscriptEntry\x12\x11\n\tpage_size\x18\x02 \x01(\x05\x12\x12\n\npage_token\x18\x03 \x01(\t"~\n\x1dListTranscriptEntriesResponse\x12D\n\x12transcript_entries\x18\x01 \x03(\x0b2(.google.apps.meet.v2beta.TranscriptEntry\x12\x17\n\x0fnext_page_token\x18\x02 \x01(\t2\xec\x04\n\rSpacesService\x12\x81\x01\n\x0bCreateSpace\x12+.google.apps.meet.v2beta.CreateSpaceRequest\x1a\x1e.google.apps.meet.v2beta.Space"%\xdaA\x05space\x82\xd3\xe4\x93\x02\x17"\x0e/v2beta/spaces:\x05space\x12|\n\x08GetSpace\x12(.google.apps.meet.v2beta.GetSpaceRequest\x1a\x1e.google.apps.meet.v2beta.Space"&\xdaA\x04name\x82\xd3\xe4\x93\x02\x19\x12\x17/v2beta/{name=spaces/*}\x12\x9c\x01\n\x0bUpdateSpace\x12+.google.apps.meet.v2beta.UpdateSpaceRequest\x1a\x1e.google.apps.meet.v2beta.Space"@\xdaA\x11space,update_mask\x82\xd3\xe4\x93\x02&2\x1d/v2beta/{space.name=spaces/*}:\x05space\x12\xa1\x01\n\x13EndActiveConference\x123.google.apps.meet.v2beta.EndActiveConferenceRequest\x1a\x16.google.protobuf.Empty"=\xdaA\x04name\x82\xd3\xe4\x93\x020"+/v2beta/{name=spaces/*}:endActiveConference:\x01*\x1a\x16\xcaA\x13meet.googleapis.com2\x81\x12\n\x18ConferenceRecordsService\x12\xa8\x01\n\x13GetConferenceRecord\x123.google.apps.meet.v2beta.GetConferenceRecordRequest\x1a).google.apps.meet.v2beta.ConferenceRecord"1\xdaA\x04name\x82\xd3\xe4\x93\x02$\x12"/v2beta/{name=conferenceRecords/*}\x12\xa9\x01\n\x15ListConferenceRecords\x125.google.apps.meet.v2beta.ListConferenceRecordsRequest\x1a6.google.apps.meet.v2beta.ListConferenceRecordsResponse"!\x82\xd3\xe4\x93\x02\x1b\x12\x19/v2beta/conferenceRecords\x12\xa8\x01\n\x0eGetParticipant\x12..google.apps.meet.v2beta.GetParticipantRequest\x1a$.google.apps.meet.v2beta.Participant"@\xdaA\x04name\x82\xd3\xe4\x93\x023\x121/v2beta/{name=conferenceRecords/*/participants/*}\x12\xbb\x01\n\x10ListParticipants\x120.google.apps.meet.v2beta.ListParticipantsRequest\x1a1.google.apps.meet.v2beta.ListParticipantsResponse"B\xdaA\x06parent\x82\xd3\xe4\x93\x023\x121/v2beta/{parent=conferenceRecords/*}/participants\x12\xd3\x01\n\x15GetParticipantSession\x125.google.apps.meet.v2beta.GetParticipantSessionRequest\x1a+.google.apps.meet.v2beta.ParticipantSession"V\xdaA\x04name\x82\xd3\xe4\x93\x02I\x12G/v2beta/{name=conferenceRecords/*/participants/*/participantSessions/*}\x12\xe6\x01\n\x17ListParticipantSessions\x127.google.apps.meet.v2beta.ListParticipantSessionsRequest\x1a8.google.apps.meet.v2beta.ListParticipantSessionsResponse"X\xdaA\x06parent\x82\xd3\xe4\x93\x02I\x12G/v2beta/{parent=conferenceRecords/*/participants/*}/participantSessions\x12\xa0\x01\n\x0cGetRecording\x12,.google.apps.meet.v2beta.GetRecordingRequest\x1a".google.apps.meet.v2beta.Recording">\xdaA\x04name\x82\xd3\xe4\x93\x021\x12//v2beta/{name=conferenceRecords/*/recordings/*}\x12\xb3\x01\n\x0eListRecordings\x12..google.apps.meet.v2beta.ListRecordingsRequest\x1a/.google.apps.meet.v2beta.ListRecordingsResponse"@\xdaA\x06parent\x82\xd3\xe4\x93\x021\x12//v2beta/{parent=conferenceRecords/*}/recordings\x12\xa4\x01\n\rGetTranscript\x12-.google.apps.meet.v2beta.GetTranscriptRequest\x1a#.google.apps.meet.v2beta.Transcript"?\xdaA\x04name\x82\xd3\xe4\x93\x022\x120/v2beta/{name=conferenceRecords/*/transcripts/*}\x12\xb7\x01\n\x0fListTranscripts\x12/.google.apps.meet.v2beta.ListTranscriptsRequest\x1a0.google.apps.meet.v2beta.ListTranscriptsResponse"A\xdaA\x06parent\x82\xd3\xe4\x93\x022\x120/v2beta/{parent=conferenceRecords/*}/transcripts\x12\xbd\x01\n\x12GetTranscriptEntry\x122.google.apps.meet.v2beta.GetTranscriptEntryRequest\x1a(.google.apps.meet.v2beta.TranscriptEntry"I\xdaA\x04name\x82\xd3\xe4\x93\x02<\x12:/v2beta/{name=conferenceRecords/*/transcripts/*/entries/*}\x12\xd3\x01\n\x15ListTranscriptEntries\x125.google.apps.meet.v2beta.ListTranscriptEntriesRequest\x1a6.google.apps.meet.v2beta.ListTranscriptEntriesResponse"K\xdaA\x06parent\x82\xd3\xe4\x93\x02<\x12:/v2beta/{parent=conferenceRecords/*/transcripts/*}/entries\x1a\x16\xcaA\x13meet.googleapis.comB\xb5\x01\n\x1bcom.google.apps.meet.v2betaB\x0cServiceProtoP\x01Z5cloud.google.com/go/apps/meet/apiv2beta/meetpb;meetpb\xaa\x02\x17Google.Apps.Meet.V2Beta\xca\x02\x17Google\\Apps\\Meet\\V2beta\xea\x02\x1aGoogle::Apps::Meet::V2betab\x06proto3')
_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'google.apps.meet.v2beta.service_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
    _globals['DESCRIPTOR']._loaded_options = None
    _globals['DESCRIPTOR']._serialized_options = b'\n\x1bcom.google.apps.meet.v2betaB\x0cServiceProtoP\x01Z5cloud.google.com/go/apps/meet/apiv2beta/meetpb;meetpb\xaa\x02\x17Google.Apps.Meet.V2Beta\xca\x02\x17Google\\Apps\\Meet\\V2beta\xea\x02\x1aGoogle::Apps::Meet::V2beta'
    _globals['_GETSPACEREQUEST'].fields_by_name['name']._loaded_options = None
    _globals['_GETSPACEREQUEST'].fields_by_name['name']._serialized_options = b'\xe0A\x02\xfaA\x1b\n\x19meet.googleapis.com/Space'
    _globals['_UPDATESPACEREQUEST'].fields_by_name['space']._loaded_options = None
    _globals['_UPDATESPACEREQUEST'].fields_by_name['space']._serialized_options = b'\xe0A\x02'
    _globals['_UPDATESPACEREQUEST'].fields_by_name['update_mask']._loaded_options = None
    _globals['_UPDATESPACEREQUEST'].fields_by_name['update_mask']._serialized_options = b'\xe0A\x01'
    _globals['_ENDACTIVECONFERENCEREQUEST'].fields_by_name['name']._loaded_options = None
    _globals['_ENDACTIVECONFERENCEREQUEST'].fields_by_name['name']._serialized_options = b'\xe0A\x02\xfaA\x1b\n\x19meet.googleapis.com/Space'
    _globals['_GETCONFERENCERECORDREQUEST'].fields_by_name['name']._loaded_options = None
    _globals['_GETCONFERENCERECORDREQUEST'].fields_by_name['name']._serialized_options = b'\xe0A\x02\xfaA&\n$meet.googleapis.com/ConferenceRecord'
    _globals['_LISTCONFERENCERECORDSREQUEST'].fields_by_name['page_size']._loaded_options = None
    _globals['_LISTCONFERENCERECORDSREQUEST'].fields_by_name['page_size']._serialized_options = b'\xe0A\x01'
    _globals['_LISTCONFERENCERECORDSREQUEST'].fields_by_name['page_token']._loaded_options = None
    _globals['_LISTCONFERENCERECORDSREQUEST'].fields_by_name['page_token']._serialized_options = b'\xe0A\x01'
    _globals['_LISTCONFERENCERECORDSREQUEST'].fields_by_name['filter']._loaded_options = None
    _globals['_LISTCONFERENCERECORDSREQUEST'].fields_by_name['filter']._serialized_options = b'\xe0A\x01'
    _globals['_GETPARTICIPANTREQUEST'].fields_by_name['name']._loaded_options = None
    _globals['_GETPARTICIPANTREQUEST'].fields_by_name['name']._serialized_options = b'\xe0A\x02\xfaA!\n\x1fmeet.googleapis.com/Participant'
    _globals['_LISTPARTICIPANTSREQUEST'].fields_by_name['parent']._loaded_options = None
    _globals['_LISTPARTICIPANTSREQUEST'].fields_by_name['parent']._serialized_options = b'\xe0A\x02\xfaA!\x12\x1fmeet.googleapis.com/Participant'
    _globals['_LISTPARTICIPANTSREQUEST'].fields_by_name['filter']._loaded_options = None
    _globals['_LISTPARTICIPANTSREQUEST'].fields_by_name['filter']._serialized_options = b'\xe0A\x01'
    _globals['_GETPARTICIPANTSESSIONREQUEST'].fields_by_name['name']._loaded_options = None
    _globals['_GETPARTICIPANTSESSIONREQUEST'].fields_by_name['name']._serialized_options = b'\xe0A\x02\xfaA(\n&meet.googleapis.com/ParticipantSession'
    _globals['_LISTPARTICIPANTSESSIONSREQUEST'].fields_by_name['parent']._loaded_options = None
    _globals['_LISTPARTICIPANTSESSIONSREQUEST'].fields_by_name['parent']._serialized_options = b'\xe0A\x02\xfaA(\x12&meet.googleapis.com/ParticipantSession'
    _globals['_LISTPARTICIPANTSESSIONSREQUEST'].fields_by_name['page_size']._loaded_options = None
    _globals['_LISTPARTICIPANTSESSIONSREQUEST'].fields_by_name['page_size']._serialized_options = b'\xe0A\x01'
    _globals['_LISTPARTICIPANTSESSIONSREQUEST'].fields_by_name['page_token']._loaded_options = None
    _globals['_LISTPARTICIPANTSESSIONSREQUEST'].fields_by_name['page_token']._serialized_options = b'\xe0A\x01'
    _globals['_LISTPARTICIPANTSESSIONSREQUEST'].fields_by_name['filter']._loaded_options = None
    _globals['_LISTPARTICIPANTSESSIONSREQUEST'].fields_by_name['filter']._serialized_options = b'\xe0A\x01'
    _globals['_GETRECORDINGREQUEST'].fields_by_name['name']._loaded_options = None
    _globals['_GETRECORDINGREQUEST'].fields_by_name['name']._serialized_options = b'\xe0A\x02\xfaA\x1f\n\x1dmeet.googleapis.com/Recording'
    _globals['_LISTRECORDINGSREQUEST'].fields_by_name['parent']._loaded_options = None
    _globals['_LISTRECORDINGSREQUEST'].fields_by_name['parent']._serialized_options = b'\xe0A\x02\xfaA\x1f\x12\x1dmeet.googleapis.com/Recording'
    _globals['_GETTRANSCRIPTREQUEST'].fields_by_name['name']._loaded_options = None
    _globals['_GETTRANSCRIPTREQUEST'].fields_by_name['name']._serialized_options = b'\xe0A\x02\xfaA \n\x1emeet.googleapis.com/Transcript'
    _globals['_LISTTRANSCRIPTSREQUEST'].fields_by_name['parent']._loaded_options = None
    _globals['_LISTTRANSCRIPTSREQUEST'].fields_by_name['parent']._serialized_options = b'\xe0A\x02\xfaA \x12\x1emeet.googleapis.com/Transcript'
    _globals['_GETTRANSCRIPTENTRYREQUEST'].fields_by_name['name']._loaded_options = None
    _globals['_GETTRANSCRIPTENTRYREQUEST'].fields_by_name['name']._serialized_options = b'\xe0A\x02\xfaA%\n#meet.googleapis.com/TranscriptEntry'
    _globals['_LISTTRANSCRIPTENTRIESREQUEST'].fields_by_name['parent']._loaded_options = None
    _globals['_LISTTRANSCRIPTENTRIESREQUEST'].fields_by_name['parent']._serialized_options = b'\xe0A\x02\xfaA%\x12#meet.googleapis.com/TranscriptEntry'
    _globals['_SPACESSERVICE']._loaded_options = None
    _globals['_SPACESSERVICE']._serialized_options = b'\xcaA\x13meet.googleapis.com'
    _globals['_SPACESSERVICE'].methods_by_name['CreateSpace']._loaded_options = None
    _globals['_SPACESSERVICE'].methods_by_name['CreateSpace']._serialized_options = b'\xdaA\x05space\x82\xd3\xe4\x93\x02\x17"\x0e/v2beta/spaces:\x05space'
    _globals['_SPACESSERVICE'].methods_by_name['GetSpace']._loaded_options = None
    _globals['_SPACESSERVICE'].methods_by_name['GetSpace']._serialized_options = b'\xdaA\x04name\x82\xd3\xe4\x93\x02\x19\x12\x17/v2beta/{name=spaces/*}'
    _globals['_SPACESSERVICE'].methods_by_name['UpdateSpace']._loaded_options = None
    _globals['_SPACESSERVICE'].methods_by_name['UpdateSpace']._serialized_options = b'\xdaA\x11space,update_mask\x82\xd3\xe4\x93\x02&2\x1d/v2beta/{space.name=spaces/*}:\x05space'
    _globals['_SPACESSERVICE'].methods_by_name['EndActiveConference']._loaded_options = None
    _globals['_SPACESSERVICE'].methods_by_name['EndActiveConference']._serialized_options = b'\xdaA\x04name\x82\xd3\xe4\x93\x020"+/v2beta/{name=spaces/*}:endActiveConference:\x01*'
    _globals['_CONFERENCERECORDSSERVICE']._loaded_options = None
    _globals['_CONFERENCERECORDSSERVICE']._serialized_options = b'\xcaA\x13meet.googleapis.com'
    _globals['_CONFERENCERECORDSSERVICE'].methods_by_name['GetConferenceRecord']._loaded_options = None
    _globals['_CONFERENCERECORDSSERVICE'].methods_by_name['GetConferenceRecord']._serialized_options = b'\xdaA\x04name\x82\xd3\xe4\x93\x02$\x12"/v2beta/{name=conferenceRecords/*}'
    _globals['_CONFERENCERECORDSSERVICE'].methods_by_name['ListConferenceRecords']._loaded_options = None
    _globals['_CONFERENCERECORDSSERVICE'].methods_by_name['ListConferenceRecords']._serialized_options = b'\x82\xd3\xe4\x93\x02\x1b\x12\x19/v2beta/conferenceRecords'
    _globals['_CONFERENCERECORDSSERVICE'].methods_by_name['GetParticipant']._loaded_options = None
    _globals['_CONFERENCERECORDSSERVICE'].methods_by_name['GetParticipant']._serialized_options = b'\xdaA\x04name\x82\xd3\xe4\x93\x023\x121/v2beta/{name=conferenceRecords/*/participants/*}'
    _globals['_CONFERENCERECORDSSERVICE'].methods_by_name['ListParticipants']._loaded_options = None
    _globals['_CONFERENCERECORDSSERVICE'].methods_by_name['ListParticipants']._serialized_options = b'\xdaA\x06parent\x82\xd3\xe4\x93\x023\x121/v2beta/{parent=conferenceRecords/*}/participants'
    _globals['_CONFERENCERECORDSSERVICE'].methods_by_name['GetParticipantSession']._loaded_options = None
    _globals['_CONFERENCERECORDSSERVICE'].methods_by_name['GetParticipantSession']._serialized_options = b'\xdaA\x04name\x82\xd3\xe4\x93\x02I\x12G/v2beta/{name=conferenceRecords/*/participants/*/participantSessions/*}'
    _globals['_CONFERENCERECORDSSERVICE'].methods_by_name['ListParticipantSessions']._loaded_options = None
    _globals['_CONFERENCERECORDSSERVICE'].methods_by_name['ListParticipantSessions']._serialized_options = b'\xdaA\x06parent\x82\xd3\xe4\x93\x02I\x12G/v2beta/{parent=conferenceRecords/*/participants/*}/participantSessions'
    _globals['_CONFERENCERECORDSSERVICE'].methods_by_name['GetRecording']._loaded_options = None
    _globals['_CONFERENCERECORDSSERVICE'].methods_by_name['GetRecording']._serialized_options = b'\xdaA\x04name\x82\xd3\xe4\x93\x021\x12//v2beta/{name=conferenceRecords/*/recordings/*}'
    _globals['_CONFERENCERECORDSSERVICE'].methods_by_name['ListRecordings']._loaded_options = None
    _globals['_CONFERENCERECORDSSERVICE'].methods_by_name['ListRecordings']._serialized_options = b'\xdaA\x06parent\x82\xd3\xe4\x93\x021\x12//v2beta/{parent=conferenceRecords/*}/recordings'
    _globals['_CONFERENCERECORDSSERVICE'].methods_by_name['GetTranscript']._loaded_options = None
    _globals['_CONFERENCERECORDSSERVICE'].methods_by_name['GetTranscript']._serialized_options = b'\xdaA\x04name\x82\xd3\xe4\x93\x022\x120/v2beta/{name=conferenceRecords/*/transcripts/*}'
    _globals['_CONFERENCERECORDSSERVICE'].methods_by_name['ListTranscripts']._loaded_options = None
    _globals['_CONFERENCERECORDSSERVICE'].methods_by_name['ListTranscripts']._serialized_options = b'\xdaA\x06parent\x82\xd3\xe4\x93\x022\x120/v2beta/{parent=conferenceRecords/*}/transcripts'
    _globals['_CONFERENCERECORDSSERVICE'].methods_by_name['GetTranscriptEntry']._loaded_options = None
    _globals['_CONFERENCERECORDSSERVICE'].methods_by_name['GetTranscriptEntry']._serialized_options = b'\xdaA\x04name\x82\xd3\xe4\x93\x02<\x12:/v2beta/{name=conferenceRecords/*/transcripts/*/entries/*}'
    _globals['_CONFERENCERECORDSSERVICE'].methods_by_name['ListTranscriptEntries']._loaded_options = None
    _globals['_CONFERENCERECORDSSERVICE'].methods_by_name['ListTranscriptEntries']._serialized_options = b'\xdaA\x06parent\x82\xd3\xe4\x93\x02<\x12:/v2beta/{parent=conferenceRecords/*/transcripts/*}/entries'
    _globals['_CREATESPACEREQUEST']._serialized_start = 284
    _globals['_CREATESPACEREQUEST']._serialized_end = 351
    _globals['_GETSPACEREQUEST']._serialized_start = 353
    _globals['_GETSPACEREQUEST']._serialized_end = 419
    _globals['_UPDATESPACEREQUEST']._serialized_start = 421
    _globals['_UPDATESPACEREQUEST']._serialized_end = 547
    _globals['_ENDACTIVECONFERENCEREQUEST']._serialized_start = 549
    _globals['_ENDACTIVECONFERENCEREQUEST']._serialized_end = 626
    _globals['_GETCONFERENCERECORDREQUEST']._serialized_start = 628
    _globals['_GETCONFERENCERECORDREQUEST']._serialized_end = 716
    _globals['_LISTCONFERENCERECORDSREQUEST']._serialized_start = 718
    _globals['_LISTCONFERENCERECORDSREQUEST']._serialized_end = 818
    _globals['_LISTCONFERENCERECORDSRESPONSE']._serialized_start = 820
    _globals['_LISTCONFERENCERECORDSRESPONSE']._serialized_end = 947
    _globals['_GETPARTICIPANTREQUEST']._serialized_start = 949
    _globals['_GETPARTICIPANTREQUEST']._serialized_end = 1027
    _globals['_LISTPARTICIPANTSREQUEST']._serialized_start = 1030
    _globals['_LISTPARTICIPANTSREQUEST']._serialized_end = 1172
    _globals['_LISTPARTICIPANTSRESPONSE']._serialized_start = 1175
    _globals['_LISTPARTICIPANTSRESPONSE']._serialized_end = 1306
    _globals['_GETPARTICIPANTSESSIONREQUEST']._serialized_start = 1308
    _globals['_GETPARTICIPANTSESSIONREQUEST']._serialized_end = 1400
    _globals['_LISTPARTICIPANTSESSIONSREQUEST']._serialized_start = 1403
    _globals['_LISTPARTICIPANTSESSIONSREQUEST']._serialized_end = 1569
    _globals['_LISTPARTICIPANTSESSIONSRESPONSE']._serialized_start = 1572
    _globals['_LISTPARTICIPANTSESSIONSRESPONSE']._serialized_end = 1705
    _globals['_GETRECORDINGREQUEST']._serialized_start = 1707
    _globals['_GETRECORDINGREQUEST']._serialized_end = 1781
    _globals['_LISTRECORDINGSREQUEST']._serialized_start = 1783
    _globals['_LISTRECORDINGSREQUEST']._serialized_end = 1900
    _globals['_LISTRECORDINGSRESPONSE']._serialized_start = 1902
    _globals['_LISTRECORDINGSRESPONSE']._serialized_end = 2007
    _globals['_GETTRANSCRIPTREQUEST']._serialized_start = 2009
    _globals['_GETTRANSCRIPTREQUEST']._serialized_end = 2085
    _globals['_LISTTRANSCRIPTSREQUEST']._serialized_start = 2087
    _globals['_LISTTRANSCRIPTSREQUEST']._serialized_end = 2206
    _globals['_LISTTRANSCRIPTSRESPONSE']._serialized_start = 2208
    _globals['_LISTTRANSCRIPTSRESPONSE']._serialized_end = 2316
    _globals['_GETTRANSCRIPTENTRYREQUEST']._serialized_start = 2318
    _globals['_GETTRANSCRIPTENTRYREQUEST']._serialized_end = 2404
    _globals['_LISTTRANSCRIPTENTRIESREQUEST']._serialized_start = 2407
    _globals['_LISTTRANSCRIPTENTRIESREQUEST']._serialized_end = 2537
    _globals['_LISTTRANSCRIPTENTRIESRESPONSE']._serialized_start = 2539
    _globals['_LISTTRANSCRIPTENTRIESRESPONSE']._serialized_end = 2665
    _globals['_SPACESSERVICE']._serialized_start = 2668
    _globals['_SPACESSERVICE']._serialized_end = 3288
    _globals['_CONFERENCERECORDSSERVICE']._serialized_start = 3291
    _globals['_CONFERENCERECORDSSERVICE']._serialized_end = 5596