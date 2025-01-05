"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_runtime_version.ValidateProtobufRuntimeVersion(_runtime_version.Domain.PUBLIC, 5, 28, 1, '', 'google/apps/meet/v2/service.proto')
_sym_db = _symbol_database.Default()
from .....google.api import annotations_pb2 as google_dot_api_dot_annotations__pb2
from .....google.api import client_pb2 as google_dot_api_dot_client__pb2
from .....google.api import field_behavior_pb2 as google_dot_api_dot_field__behavior__pb2
from .....google.api import resource_pb2 as google_dot_api_dot_resource__pb2
from .....google.apps.meet.v2 import resource_pb2 as google_dot_apps_dot_meet_dot_v2_dot_resource__pb2
from google.protobuf import empty_pb2 as google_dot_protobuf_dot_empty__pb2
from google.protobuf import field_mask_pb2 as google_dot_protobuf_dot_field__mask__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n!google/apps/meet/v2/service.proto\x12\x13google.apps.meet.v2\x1a\x1cgoogle/api/annotations.proto\x1a\x17google/api/client.proto\x1a\x1fgoogle/api/field_behavior.proto\x1a\x19google/api/resource.proto\x1a"google/apps/meet/v2/resource.proto\x1a\x1bgoogle/protobuf/empty.proto\x1a google/protobuf/field_mask.proto"?\n\x12CreateSpaceRequest\x12)\n\x05space\x18\x01 \x01(\x0b2\x1a.google.apps.meet.v2.Space"B\n\x0fGetSpaceRequest\x12/\n\x04name\x18\x01 \x01(\tB!\xe0A\x02\xfaA\x1b\n\x19meet.googleapis.com/Space"z\n\x12UpdateSpaceRequest\x12.\n\x05space\x18\x01 \x01(\x0b2\x1a.google.apps.meet.v2.SpaceB\x03\xe0A\x02\x124\n\x0bupdate_mask\x18\x02 \x01(\x0b2\x1a.google.protobuf.FieldMaskB\x03\xe0A\x01"M\n\x1aEndActiveConferenceRequest\x12/\n\x04name\x18\x01 \x01(\tB!\xe0A\x02\xfaA\x1b\n\x19meet.googleapis.com/Space"X\n\x1aGetConferenceRecordRequest\x12:\n\x04name\x18\x01 \x01(\tB,\xe0A\x02\xfaA&\n$meet.googleapis.com/ConferenceRecord"d\n\x1cListConferenceRecordsRequest\x12\x16\n\tpage_size\x18\x01 \x01(\x05B\x03\xe0A\x01\x12\x17\n\npage_token\x18\x02 \x01(\tB\x03\xe0A\x01\x12\x13\n\x06filter\x18\x03 \x01(\tB\x03\xe0A\x01"{\n\x1dListConferenceRecordsResponse\x12A\n\x12conference_records\x18\x01 \x03(\x0b2%.google.apps.meet.v2.ConferenceRecord\x12\x17\n\x0fnext_page_token\x18\x02 \x01(\t"N\n\x15GetParticipantRequest\x125\n\x04name\x18\x01 \x01(\tB\'\xe0A\x02\xfaA!\n\x1fmeet.googleapis.com/Participant"\x8e\x01\n\x17ListParticipantsRequest\x127\n\x06parent\x18\x01 \x01(\tB\'\xe0A\x02\xfaA!\x12\x1fmeet.googleapis.com/Participant\x12\x11\n\tpage_size\x18\x02 \x01(\x05\x12\x12\n\npage_token\x18\x03 \x01(\t\x12\x13\n\x06filter\x18\x04 \x01(\tB\x03\xe0A\x01"\x7f\n\x18ListParticipantsResponse\x126\n\x0cparticipants\x18\x01 \x03(\x0b2 .google.apps.meet.v2.Participant\x12\x17\n\x0fnext_page_token\x18\x02 \x01(\t\x12\x12\n\ntotal_size\x18\x03 \x01(\x05"\\\n\x1cGetParticipantSessionRequest\x12<\n\x04name\x18\x01 \x01(\tB.\xe0A\x02\xfaA(\n&meet.googleapis.com/ParticipantSession"\xa6\x01\n\x1eListParticipantSessionsRequest\x12>\n\x06parent\x18\x01 \x01(\tB.\xe0A\x02\xfaA(\x12&meet.googleapis.com/ParticipantSession\x12\x16\n\tpage_size\x18\x02 \x01(\x05B\x03\xe0A\x01\x12\x17\n\npage_token\x18\x03 \x01(\tB\x03\xe0A\x01\x12\x13\n\x06filter\x18\x04 \x01(\tB\x03\xe0A\x01"\x81\x01\n\x1fListParticipantSessionsResponse\x12E\n\x14participant_sessions\x18\x01 \x03(\x0b2\'.google.apps.meet.v2.ParticipantSession\x12\x17\n\x0fnext_page_token\x18\x02 \x01(\t"J\n\x13GetRecordingRequest\x123\n\x04name\x18\x01 \x01(\tB%\xe0A\x02\xfaA\x1f\n\x1dmeet.googleapis.com/Recording"u\n\x15ListRecordingsRequest\x125\n\x06parent\x18\x01 \x01(\tB%\xe0A\x02\xfaA\x1f\x12\x1dmeet.googleapis.com/Recording\x12\x11\n\tpage_size\x18\x02 \x01(\x05\x12\x12\n\npage_token\x18\x03 \x01(\t"e\n\x16ListRecordingsResponse\x122\n\nrecordings\x18\x01 \x03(\x0b2\x1e.google.apps.meet.v2.Recording\x12\x17\n\x0fnext_page_token\x18\x02 \x01(\t"L\n\x14GetTranscriptRequest\x124\n\x04name\x18\x01 \x01(\tB&\xe0A\x02\xfaA \n\x1emeet.googleapis.com/Transcript"w\n\x16ListTranscriptsRequest\x126\n\x06parent\x18\x01 \x01(\tB&\xe0A\x02\xfaA \x12\x1emeet.googleapis.com/Transcript\x12\x11\n\tpage_size\x18\x02 \x01(\x05\x12\x12\n\npage_token\x18\x03 \x01(\t"h\n\x17ListTranscriptsResponse\x124\n\x0btranscripts\x18\x01 \x03(\x0b2\x1f.google.apps.meet.v2.Transcript\x12\x17\n\x0fnext_page_token\x18\x02 \x01(\t"V\n\x19GetTranscriptEntryRequest\x129\n\x04name\x18\x01 \x01(\tB+\xe0A\x02\xfaA%\n#meet.googleapis.com/TranscriptEntry"\x82\x01\n\x1cListTranscriptEntriesRequest\x12;\n\x06parent\x18\x01 \x01(\tB+\xe0A\x02\xfaA%\x12#meet.googleapis.com/TranscriptEntry\x12\x11\n\tpage_size\x18\x02 \x01(\x05\x12\x12\n\npage_token\x18\x03 \x01(\t"z\n\x1dListTranscriptEntriesResponse\x12@\n\x12transcript_entries\x18\x01 \x03(\x0b2$.google.apps.meet.v2.TranscriptEntry\x12\x17\n\x0fnext_page_token\x18\x02 \x01(\t2\xb1\x05\n\rSpacesService\x12u\n\x0bCreateSpace\x12\'.google.apps.meet.v2.CreateSpaceRequest\x1a\x1a.google.apps.meet.v2.Space"!\xdaA\x05space\x82\xd3\xe4\x93\x02\x13"\n/v2/spaces:\x05space\x12p\n\x08GetSpace\x12$.google.apps.meet.v2.GetSpaceRequest\x1a\x1a.google.apps.meet.v2.Space""\xdaA\x04name\x82\xd3\xe4\x93\x02\x15\x12\x13/v2/{name=spaces/*}\x12\x90\x01\n\x0bUpdateSpace\x12\'.google.apps.meet.v2.UpdateSpaceRequest\x1a\x1a.google.apps.meet.v2.Space"<\xdaA\x11space,update_mask\x82\xd3\xe4\x93\x02"2\x19/v2/{space.name=spaces/*}:\x05space\x12\x99\x01\n\x13EndActiveConference\x12/.google.apps.meet.v2.EndActiveConferenceRequest\x1a\x16.google.protobuf.Empty"9\xdaA\x04name\x82\xd3\xe4\x93\x02,"\'/v2/{name=spaces/*}:endActiveConference:\x01*\x1a\x87\x01\xcaA\x13meet.googleapis.com\xd2Anhttps://www.googleapis.com/auth/meetings.space.created,https://www.googleapis.com/auth/meetings.space.readonly2\xe3\x11\n\x18ConferenceRecordsService\x12\x9c\x01\n\x13GetConferenceRecord\x12/.google.apps.meet.v2.GetConferenceRecordRequest\x1a%.google.apps.meet.v2.ConferenceRecord"-\xdaA\x04name\x82\xd3\xe4\x93\x02 \x12\x1e/v2/{name=conferenceRecords/*}\x12\x9d\x01\n\x15ListConferenceRecords\x121.google.apps.meet.v2.ListConferenceRecordsRequest\x1a2.google.apps.meet.v2.ListConferenceRecordsResponse"\x1d\x82\xd3\xe4\x93\x02\x17\x12\x15/v2/conferenceRecords\x12\x9c\x01\n\x0eGetParticipant\x12*.google.apps.meet.v2.GetParticipantRequest\x1a .google.apps.meet.v2.Participant"<\xdaA\x04name\x82\xd3\xe4\x93\x02/\x12-/v2/{name=conferenceRecords/*/participants/*}\x12\xaf\x01\n\x10ListParticipants\x12,.google.apps.meet.v2.ListParticipantsRequest\x1a-.google.apps.meet.v2.ListParticipantsResponse">\xdaA\x06parent\x82\xd3\xe4\x93\x02/\x12-/v2/{parent=conferenceRecords/*}/participants\x12\xc7\x01\n\x15GetParticipantSession\x121.google.apps.meet.v2.GetParticipantSessionRequest\x1a\'.google.apps.meet.v2.ParticipantSession"R\xdaA\x04name\x82\xd3\xe4\x93\x02E\x12C/v2/{name=conferenceRecords/*/participants/*/participantSessions/*}\x12\xda\x01\n\x17ListParticipantSessions\x123.google.apps.meet.v2.ListParticipantSessionsRequest\x1a4.google.apps.meet.v2.ListParticipantSessionsResponse"T\xdaA\x06parent\x82\xd3\xe4\x93\x02E\x12C/v2/{parent=conferenceRecords/*/participants/*}/participantSessions\x12\x94\x01\n\x0cGetRecording\x12(.google.apps.meet.v2.GetRecordingRequest\x1a\x1e.google.apps.meet.v2.Recording":\xdaA\x04name\x82\xd3\xe4\x93\x02-\x12+/v2/{name=conferenceRecords/*/recordings/*}\x12\xa7\x01\n\x0eListRecordings\x12*.google.apps.meet.v2.ListRecordingsRequest\x1a+.google.apps.meet.v2.ListRecordingsResponse"<\xdaA\x06parent\x82\xd3\xe4\x93\x02-\x12+/v2/{parent=conferenceRecords/*}/recordings\x12\x98\x01\n\rGetTranscript\x12).google.apps.meet.v2.GetTranscriptRequest\x1a\x1f.google.apps.meet.v2.Transcript";\xdaA\x04name\x82\xd3\xe4\x93\x02.\x12,/v2/{name=conferenceRecords/*/transcripts/*}\x12\xab\x01\n\x0fListTranscripts\x12+.google.apps.meet.v2.ListTranscriptsRequest\x1a,.google.apps.meet.v2.ListTranscriptsResponse"=\xdaA\x06parent\x82\xd3\xe4\x93\x02.\x12,/v2/{parent=conferenceRecords/*}/transcripts\x12\xb1\x01\n\x12GetTranscriptEntry\x12..google.apps.meet.v2.GetTranscriptEntryRequest\x1a$.google.apps.meet.v2.TranscriptEntry"E\xdaA\x04name\x82\xd3\xe4\x93\x028\x126/v2/{name=conferenceRecords/*/transcripts/*/entries/*}\x12\xc7\x01\n\x15ListTranscriptEntries\x121.google.apps.meet.v2.ListTranscriptEntriesRequest\x1a2.google.apps.meet.v2.ListTranscriptEntriesResponse"G\xdaA\x06parent\x82\xd3\xe4\x93\x028\x126/v2/{parent=conferenceRecords/*/transcripts/*}/entries\x1a\x87\x01\xcaA\x13meet.googleapis.com\xd2Anhttps://www.googleapis.com/auth/meetings.space.created,https://www.googleapis.com/auth/meetings.space.readonlyB\xa1\x01\n\x17com.google.apps.meet.v2B\x0cServiceProtoP\x01Z1cloud.google.com/go/apps/meet/apiv2/meetpb;meetpb\xaa\x02\x13Google.Apps.Meet.V2\xca\x02\x13Google\\Apps\\Meet\\V2\xea\x02\x16Google::Apps::Meet::V2b\x06proto3')
_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'google.apps.meet.v2.service_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
    _globals['DESCRIPTOR']._loaded_options = None
    _globals['DESCRIPTOR']._serialized_options = b'\n\x17com.google.apps.meet.v2B\x0cServiceProtoP\x01Z1cloud.google.com/go/apps/meet/apiv2/meetpb;meetpb\xaa\x02\x13Google.Apps.Meet.V2\xca\x02\x13Google\\Apps\\Meet\\V2\xea\x02\x16Google::Apps::Meet::V2'
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
    _globals['_SPACESSERVICE']._serialized_options = b'\xcaA\x13meet.googleapis.com\xd2Anhttps://www.googleapis.com/auth/meetings.space.created,https://www.googleapis.com/auth/meetings.space.readonly'
    _globals['_SPACESSERVICE'].methods_by_name['CreateSpace']._loaded_options = None
    _globals['_SPACESSERVICE'].methods_by_name['CreateSpace']._serialized_options = b'\xdaA\x05space\x82\xd3\xe4\x93\x02\x13"\n/v2/spaces:\x05space'
    _globals['_SPACESSERVICE'].methods_by_name['GetSpace']._loaded_options = None
    _globals['_SPACESSERVICE'].methods_by_name['GetSpace']._serialized_options = b'\xdaA\x04name\x82\xd3\xe4\x93\x02\x15\x12\x13/v2/{name=spaces/*}'
    _globals['_SPACESSERVICE'].methods_by_name['UpdateSpace']._loaded_options = None
    _globals['_SPACESSERVICE'].methods_by_name['UpdateSpace']._serialized_options = b'\xdaA\x11space,update_mask\x82\xd3\xe4\x93\x02"2\x19/v2/{space.name=spaces/*}:\x05space'
    _globals['_SPACESSERVICE'].methods_by_name['EndActiveConference']._loaded_options = None
    _globals['_SPACESSERVICE'].methods_by_name['EndActiveConference']._serialized_options = b'\xdaA\x04name\x82\xd3\xe4\x93\x02,"\'/v2/{name=spaces/*}:endActiveConference:\x01*'
    _globals['_CONFERENCERECORDSSERVICE']._loaded_options = None
    _globals['_CONFERENCERECORDSSERVICE']._serialized_options = b'\xcaA\x13meet.googleapis.com\xd2Anhttps://www.googleapis.com/auth/meetings.space.created,https://www.googleapis.com/auth/meetings.space.readonly'
    _globals['_CONFERENCERECORDSSERVICE'].methods_by_name['GetConferenceRecord']._loaded_options = None
    _globals['_CONFERENCERECORDSSERVICE'].methods_by_name['GetConferenceRecord']._serialized_options = b'\xdaA\x04name\x82\xd3\xe4\x93\x02 \x12\x1e/v2/{name=conferenceRecords/*}'
    _globals['_CONFERENCERECORDSSERVICE'].methods_by_name['ListConferenceRecords']._loaded_options = None
    _globals['_CONFERENCERECORDSSERVICE'].methods_by_name['ListConferenceRecords']._serialized_options = b'\x82\xd3\xe4\x93\x02\x17\x12\x15/v2/conferenceRecords'
    _globals['_CONFERENCERECORDSSERVICE'].methods_by_name['GetParticipant']._loaded_options = None
    _globals['_CONFERENCERECORDSSERVICE'].methods_by_name['GetParticipant']._serialized_options = b'\xdaA\x04name\x82\xd3\xe4\x93\x02/\x12-/v2/{name=conferenceRecords/*/participants/*}'
    _globals['_CONFERENCERECORDSSERVICE'].methods_by_name['ListParticipants']._loaded_options = None
    _globals['_CONFERENCERECORDSSERVICE'].methods_by_name['ListParticipants']._serialized_options = b'\xdaA\x06parent\x82\xd3\xe4\x93\x02/\x12-/v2/{parent=conferenceRecords/*}/participants'
    _globals['_CONFERENCERECORDSSERVICE'].methods_by_name['GetParticipantSession']._loaded_options = None
    _globals['_CONFERENCERECORDSSERVICE'].methods_by_name['GetParticipantSession']._serialized_options = b'\xdaA\x04name\x82\xd3\xe4\x93\x02E\x12C/v2/{name=conferenceRecords/*/participants/*/participantSessions/*}'
    _globals['_CONFERENCERECORDSSERVICE'].methods_by_name['ListParticipantSessions']._loaded_options = None
    _globals['_CONFERENCERECORDSSERVICE'].methods_by_name['ListParticipantSessions']._serialized_options = b'\xdaA\x06parent\x82\xd3\xe4\x93\x02E\x12C/v2/{parent=conferenceRecords/*/participants/*}/participantSessions'
    _globals['_CONFERENCERECORDSSERVICE'].methods_by_name['GetRecording']._loaded_options = None
    _globals['_CONFERENCERECORDSSERVICE'].methods_by_name['GetRecording']._serialized_options = b'\xdaA\x04name\x82\xd3\xe4\x93\x02-\x12+/v2/{name=conferenceRecords/*/recordings/*}'
    _globals['_CONFERENCERECORDSSERVICE'].methods_by_name['ListRecordings']._loaded_options = None
    _globals['_CONFERENCERECORDSSERVICE'].methods_by_name['ListRecordings']._serialized_options = b'\xdaA\x06parent\x82\xd3\xe4\x93\x02-\x12+/v2/{parent=conferenceRecords/*}/recordings'
    _globals['_CONFERENCERECORDSSERVICE'].methods_by_name['GetTranscript']._loaded_options = None
    _globals['_CONFERENCERECORDSSERVICE'].methods_by_name['GetTranscript']._serialized_options = b'\xdaA\x04name\x82\xd3\xe4\x93\x02.\x12,/v2/{name=conferenceRecords/*/transcripts/*}'
    _globals['_CONFERENCERECORDSSERVICE'].methods_by_name['ListTranscripts']._loaded_options = None
    _globals['_CONFERENCERECORDSSERVICE'].methods_by_name['ListTranscripts']._serialized_options = b'\xdaA\x06parent\x82\xd3\xe4\x93\x02.\x12,/v2/{parent=conferenceRecords/*}/transcripts'
    _globals['_CONFERENCERECORDSSERVICE'].methods_by_name['GetTranscriptEntry']._loaded_options = None
    _globals['_CONFERENCERECORDSSERVICE'].methods_by_name['GetTranscriptEntry']._serialized_options = b'\xdaA\x04name\x82\xd3\xe4\x93\x028\x126/v2/{name=conferenceRecords/*/transcripts/*/entries/*}'
    _globals['_CONFERENCERECORDSSERVICE'].methods_by_name['ListTranscriptEntries']._loaded_options = None
    _globals['_CONFERENCERECORDSSERVICE'].methods_by_name['ListTranscriptEntries']._serialized_options = b'\xdaA\x06parent\x82\xd3\xe4\x93\x028\x126/v2/{parent=conferenceRecords/*/transcripts/*}/entries'
    _globals['_CREATESPACEREQUEST']._serialized_start = 272
    _globals['_CREATESPACEREQUEST']._serialized_end = 335
    _globals['_GETSPACEREQUEST']._serialized_start = 337
    _globals['_GETSPACEREQUEST']._serialized_end = 403
    _globals['_UPDATESPACEREQUEST']._serialized_start = 405
    _globals['_UPDATESPACEREQUEST']._serialized_end = 527
    _globals['_ENDACTIVECONFERENCEREQUEST']._serialized_start = 529
    _globals['_ENDACTIVECONFERENCEREQUEST']._serialized_end = 606
    _globals['_GETCONFERENCERECORDREQUEST']._serialized_start = 608
    _globals['_GETCONFERENCERECORDREQUEST']._serialized_end = 696
    _globals['_LISTCONFERENCERECORDSREQUEST']._serialized_start = 698
    _globals['_LISTCONFERENCERECORDSREQUEST']._serialized_end = 798
    _globals['_LISTCONFERENCERECORDSRESPONSE']._serialized_start = 800
    _globals['_LISTCONFERENCERECORDSRESPONSE']._serialized_end = 923
    _globals['_GETPARTICIPANTREQUEST']._serialized_start = 925
    _globals['_GETPARTICIPANTREQUEST']._serialized_end = 1003
    _globals['_LISTPARTICIPANTSREQUEST']._serialized_start = 1006
    _globals['_LISTPARTICIPANTSREQUEST']._serialized_end = 1148
    _globals['_LISTPARTICIPANTSRESPONSE']._serialized_start = 1150
    _globals['_LISTPARTICIPANTSRESPONSE']._serialized_end = 1277
    _globals['_GETPARTICIPANTSESSIONREQUEST']._serialized_start = 1279
    _globals['_GETPARTICIPANTSESSIONREQUEST']._serialized_end = 1371
    _globals['_LISTPARTICIPANTSESSIONSREQUEST']._serialized_start = 1374
    _globals['_LISTPARTICIPANTSESSIONSREQUEST']._serialized_end = 1540
    _globals['_LISTPARTICIPANTSESSIONSRESPONSE']._serialized_start = 1543
    _globals['_LISTPARTICIPANTSESSIONSRESPONSE']._serialized_end = 1672
    _globals['_GETRECORDINGREQUEST']._serialized_start = 1674
    _globals['_GETRECORDINGREQUEST']._serialized_end = 1748
    _globals['_LISTRECORDINGSREQUEST']._serialized_start = 1750
    _globals['_LISTRECORDINGSREQUEST']._serialized_end = 1867
    _globals['_LISTRECORDINGSRESPONSE']._serialized_start = 1869
    _globals['_LISTRECORDINGSRESPONSE']._serialized_end = 1970
    _globals['_GETTRANSCRIPTREQUEST']._serialized_start = 1972
    _globals['_GETTRANSCRIPTREQUEST']._serialized_end = 2048
    _globals['_LISTTRANSCRIPTSREQUEST']._serialized_start = 2050
    _globals['_LISTTRANSCRIPTSREQUEST']._serialized_end = 2169
    _globals['_LISTTRANSCRIPTSRESPONSE']._serialized_start = 2171
    _globals['_LISTTRANSCRIPTSRESPONSE']._serialized_end = 2275
    _globals['_GETTRANSCRIPTENTRYREQUEST']._serialized_start = 2277
    _globals['_GETTRANSCRIPTENTRYREQUEST']._serialized_end = 2363
    _globals['_LISTTRANSCRIPTENTRIESREQUEST']._serialized_start = 2366
    _globals['_LISTTRANSCRIPTENTRIESREQUEST']._serialized_end = 2496
    _globals['_LISTTRANSCRIPTENTRIESRESPONSE']._serialized_start = 2498
    _globals['_LISTTRANSCRIPTENTRIESRESPONSE']._serialized_end = 2620
    _globals['_SPACESSERVICE']._serialized_start = 2623
    _globals['_SPACESSERVICE']._serialized_end = 3312
    _globals['_CONFERENCERECORDSSERVICE']._serialized_start = 3315
    _globals['_CONFERENCERECORDSSERVICE']._serialized_end = 5590