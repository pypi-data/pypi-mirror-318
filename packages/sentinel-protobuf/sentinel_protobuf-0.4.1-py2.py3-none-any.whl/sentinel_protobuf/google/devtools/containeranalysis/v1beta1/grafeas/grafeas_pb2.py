"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_runtime_version.ValidateProtobufRuntimeVersion(_runtime_version.Domain.PUBLIC, 5, 28, 1, '', 'google/devtools/containeranalysis/v1beta1/grafeas/grafeas.proto')
_sym_db = _symbol_database.Default()
from ......google.api import annotations_pb2 as google_dot_api_dot_annotations__pb2
from ......google.api import client_pb2 as google_dot_api_dot_client__pb2
from ......google.devtools.containeranalysis.v1beta1.attestation import attestation_pb2 as google_dot_devtools_dot_containeranalysis_dot_v1beta1_dot_attestation_dot_attestation__pb2
from ......google.devtools.containeranalysis.v1beta1.build import build_pb2 as google_dot_devtools_dot_containeranalysis_dot_v1beta1_dot_build_dot_build__pb2
from ......google.devtools.containeranalysis.v1beta1.common import common_pb2 as google_dot_devtools_dot_containeranalysis_dot_v1beta1_dot_common_dot_common__pb2
from ......google.devtools.containeranalysis.v1beta1.deployment import deployment_pb2 as google_dot_devtools_dot_containeranalysis_dot_v1beta1_dot_deployment_dot_deployment__pb2
from ......google.devtools.containeranalysis.v1beta1.discovery import discovery_pb2 as google_dot_devtools_dot_containeranalysis_dot_v1beta1_dot_discovery_dot_discovery__pb2
from ......google.devtools.containeranalysis.v1beta1.image import image_pb2 as google_dot_devtools_dot_containeranalysis_dot_v1beta1_dot_image_dot_image__pb2
from ......google.devtools.containeranalysis.v1beta1.package import package_pb2 as google_dot_devtools_dot_containeranalysis_dot_v1beta1_dot_package_dot_package__pb2
from ......google.devtools.containeranalysis.v1beta1.provenance import provenance_pb2 as google_dot_devtools_dot_containeranalysis_dot_v1beta1_dot_provenance_dot_provenance__pb2
from ......google.devtools.containeranalysis.v1beta1.vulnerability import vulnerability_pb2 as google_dot_devtools_dot_containeranalysis_dot_v1beta1_dot_vulnerability_dot_vulnerability__pb2
from google.protobuf import empty_pb2 as google_dot_protobuf_dot_empty__pb2
from google.protobuf import field_mask_pb2 as google_dot_protobuf_dot_field__mask__pb2
from google.protobuf import timestamp_pb2 as google_dot_protobuf_dot_timestamp__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n?google/devtools/containeranalysis/v1beta1/grafeas/grafeas.proto\x12\x0fgrafeas.v1beta1\x1a\x1cgoogle/api/annotations.proto\x1a\x17google/api/client.proto\x1aGgoogle/devtools/containeranalysis/v1beta1/attestation/attestation.proto\x1a;google/devtools/containeranalysis/v1beta1/build/build.proto\x1a=google/devtools/containeranalysis/v1beta1/common/common.proto\x1aEgoogle/devtools/containeranalysis/v1beta1/deployment/deployment.proto\x1aCgoogle/devtools/containeranalysis/v1beta1/discovery/discovery.proto\x1a;google/devtools/containeranalysis/v1beta1/image/image.proto\x1a?google/devtools/containeranalysis/v1beta1/package/package.proto\x1aEgoogle/devtools/containeranalysis/v1beta1/provenance/provenance.proto\x1aKgoogle/devtools/containeranalysis/v1beta1/vulnerability/vulnerability.proto\x1a\x1bgoogle/protobuf/empty.proto\x1a google/protobuf/field_mask.proto\x1a\x1fgoogle/protobuf/timestamp.proto"\x9c\x05\n\nOccurrence\x12\x0c\n\x04name\x18\x01 \x01(\t\x12+\n\x08resource\x18\x02 \x01(\x0b2\x19.grafeas.v1beta1.Resource\x12\x11\n\tnote_name\x18\x03 \x01(\t\x12\'\n\x04kind\x18\x04 \x01(\x0e2\x19.grafeas.v1beta1.NoteKind\x12\x13\n\x0bremediation\x18\x05 \x01(\t\x12/\n\x0bcreate_time\x18\x06 \x01(\x0b2\x1a.google.protobuf.Timestamp\x12/\n\x0bupdate_time\x18\x07 \x01(\x0b2\x1a.google.protobuf.Timestamp\x12?\n\rvulnerability\x18\x08 \x01(\x0b2&.grafeas.v1beta1.vulnerability.DetailsH\x00\x12/\n\x05build\x18\t \x01(\x0b2\x1e.grafeas.v1beta1.build.DetailsH\x00\x127\n\rderived_image\x18\n \x01(\x0b2\x1e.grafeas.v1beta1.image.DetailsH\x00\x128\n\x0cinstallation\x18\x0b \x01(\x0b2 .grafeas.v1beta1.package.DetailsH\x00\x129\n\ndeployment\x18\x0c \x01(\x0b2#.grafeas.v1beta1.deployment.DetailsH\x00\x128\n\ndiscovered\x18\r \x01(\x0b2".grafeas.v1beta1.discovery.DetailsH\x00\x12;\n\x0battestation\x18\x0e \x01(\x0b2$.grafeas.v1beta1.attestation.DetailsH\x00B\t\n\x07details"]\n\x08Resource\x12\x0c\n\x04name\x18\x01 \x01(\t\x12\x0b\n\x03uri\x18\x02 \x01(\t\x126\n\x0ccontent_hash\x18\x03 \x01(\x0b2 .grafeas.v1beta1.provenance.Hash"\x80\x06\n\x04Note\x12\x0c\n\x04name\x18\x01 \x01(\t\x12\x19\n\x11short_description\x18\x02 \x01(\t\x12\x18\n\x10long_description\x18\x03 \x01(\t\x12\'\n\x04kind\x18\x04 \x01(\x0e2\x19.grafeas.v1beta1.NoteKind\x120\n\x0brelated_url\x18\x05 \x03(\x0b2\x1b.grafeas.v1beta1.RelatedUrl\x123\n\x0fexpiration_time\x18\x06 \x01(\x0b2\x1a.google.protobuf.Timestamp\x12/\n\x0bcreate_time\x18\x07 \x01(\x0b2\x1a.google.protobuf.Timestamp\x12/\n\x0bupdate_time\x18\x08 \x01(\x0b2\x1a.google.protobuf.Timestamp\x12\x1a\n\x12related_note_names\x18\t \x03(\t\x12E\n\rvulnerability\x18\n \x01(\x0b2,.grafeas.v1beta1.vulnerability.VulnerabilityH\x00\x12-\n\x05build\x18\x0b \x01(\x0b2\x1c.grafeas.v1beta1.build.BuildH\x00\x122\n\nbase_image\x18\x0c \x01(\x0b2\x1c.grafeas.v1beta1.image.BasisH\x00\x123\n\x07package\x18\r \x01(\x0b2 .grafeas.v1beta1.package.PackageH\x00\x12<\n\ndeployable\x18\x0e \x01(\x0b2&.grafeas.v1beta1.deployment.DeployableH\x00\x129\n\tdiscovery\x18\x0f \x01(\x0b2$.grafeas.v1beta1.discovery.DiscoveryH\x00\x12G\n\x15attestation_authority\x18\x10 \x01(\x0b2&.grafeas.v1beta1.attestation.AuthorityH\x00B\x06\n\x04type"$\n\x14GetOccurrenceRequest\x12\x0c\n\x04name\x18\x01 \x01(\t"_\n\x16ListOccurrencesRequest\x12\x0e\n\x06parent\x18\x01 \x01(\t\x12\x0e\n\x06filter\x18\x02 \x01(\t\x12\x11\n\tpage_size\x18\x03 \x01(\x05\x12\x12\n\npage_token\x18\x04 \x01(\t"d\n\x17ListOccurrencesResponse\x120\n\x0boccurrences\x18\x01 \x03(\x0b2\x1b.grafeas.v1beta1.Occurrence\x12\x17\n\x0fnext_page_token\x18\x02 \x01(\t"\'\n\x17DeleteOccurrenceRequest\x12\x0c\n\x04name\x18\x01 \x01(\t"Z\n\x17CreateOccurrenceRequest\x12\x0e\n\x06parent\x18\x01 \x01(\t\x12/\n\noccurrence\x18\x02 \x01(\x0b2\x1b.grafeas.v1beta1.Occurrence"\x89\x01\n\x17UpdateOccurrenceRequest\x12\x0c\n\x04name\x18\x01 \x01(\t\x12/\n\noccurrence\x18\x02 \x01(\x0b2\x1b.grafeas.v1beta1.Occurrence\x12/\n\x0bupdate_mask\x18\x03 \x01(\x0b2\x1a.google.protobuf.FieldMask"\x1e\n\x0eGetNoteRequest\x12\x0c\n\x04name\x18\x01 \x01(\t"(\n\x18GetOccurrenceNoteRequest\x12\x0c\n\x04name\x18\x01 \x01(\t"Y\n\x10ListNotesRequest\x12\x0e\n\x06parent\x18\x01 \x01(\t\x12\x0e\n\x06filter\x18\x02 \x01(\t\x12\x11\n\tpage_size\x18\x03 \x01(\x05\x12\x12\n\npage_token\x18\x04 \x01(\t"R\n\x11ListNotesResponse\x12$\n\x05notes\x18\x01 \x03(\x0b2\x15.grafeas.v1beta1.Note\x12\x17\n\x0fnext_page_token\x18\x02 \x01(\t"!\n\x11DeleteNoteRequest\x12\x0c\n\x04name\x18\x01 \x01(\t"Y\n\x11CreateNoteRequest\x12\x0e\n\x06parent\x18\x01 \x01(\t\x12\x0f\n\x07note_id\x18\x02 \x01(\t\x12#\n\x04note\x18\x03 \x01(\x0b2\x15.grafeas.v1beta1.Note"w\n\x11UpdateNoteRequest\x12\x0c\n\x04name\x18\x01 \x01(\t\x12#\n\x04note\x18\x02 \x01(\x0b2\x15.grafeas.v1beta1.Note\x12/\n\x0bupdate_mask\x18\x03 \x01(\x0b2\x1a.google.protobuf.FieldMask"a\n\x1aListNoteOccurrencesRequest\x12\x0c\n\x04name\x18\x01 \x01(\t\x12\x0e\n\x06filter\x18\x02 \x01(\t\x12\x11\n\tpage_size\x18\x03 \x01(\x05\x12\x12\n\npage_token\x18\x04 \x01(\t"h\n\x1bListNoteOccurrencesResponse\x120\n\x0boccurrences\x18\x01 \x03(\x0b2\x1b.grafeas.v1beta1.Occurrence\x12\x17\n\x0fnext_page_token\x18\x02 \x01(\t"\xb2\x01\n\x17BatchCreateNotesRequest\x12\x0e\n\x06parent\x18\x01 \x01(\t\x12B\n\x05notes\x18\x02 \x03(\x0b23.grafeas.v1beta1.BatchCreateNotesRequest.NotesEntry\x1aC\n\nNotesEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12$\n\x05value\x18\x02 \x01(\x0b2\x15.grafeas.v1beta1.Note:\x028\x01"@\n\x18BatchCreateNotesResponse\x12$\n\x05notes\x18\x01 \x03(\x0b2\x15.grafeas.v1beta1.Note"a\n\x1dBatchCreateOccurrencesRequest\x12\x0e\n\x06parent\x18\x01 \x01(\t\x120\n\x0boccurrences\x18\x02 \x03(\x0b2\x1b.grafeas.v1beta1.Occurrence"R\n\x1eBatchCreateOccurrencesResponse\x120\n\x0boccurrences\x18\x01 \x03(\x0b2\x1b.grafeas.v1beta1.Occurrence"K\n)GetVulnerabilityOccurrencesSummaryRequest\x12\x0e\n\x06parent\x18\x01 \x01(\t\x12\x0e\n\x06filter\x18\x02 \x01(\t"\xa5\x02\n\x1fVulnerabilityOccurrencesSummary\x12U\n\x06counts\x18\x01 \x03(\x0b2E.grafeas.v1beta1.VulnerabilityOccurrencesSummary.FixableTotalByDigest\x1a\xaa\x01\n\x14FixableTotalByDigest\x12+\n\x08resource\x18\x01 \x01(\x0b2\x19.grafeas.v1beta1.Resource\x129\n\x08severity\x18\x02 \x01(\x0e2\'.grafeas.v1beta1.vulnerability.Severity\x12\x15\n\rfixable_count\x18\x03 \x01(\x03\x12\x13\n\x0btotal_count\x18\x04 \x01(\x032\x98\x12\n\x0eGrafeasV1Beta1\x12\x85\x01\n\rGetOccurrence\x12%.grafeas.v1beta1.GetOccurrenceRequest\x1a\x1b.grafeas.v1beta1.Occurrence"0\x82\xd3\xe4\x93\x02*\x12(/v1beta1/{name=projects/*/occurrences/*}\x12\x96\x01\n\x0fListOccurrences\x12\'.grafeas.v1beta1.ListOccurrencesRequest\x1a(.grafeas.v1beta1.ListOccurrencesResponse"0\x82\xd3\xe4\x93\x02*\x12(/v1beta1/{parent=projects/*}/occurrences\x12\x86\x01\n\x10DeleteOccurrence\x12(.grafeas.v1beta1.DeleteOccurrenceRequest\x1a\x16.google.protobuf.Empty"0\x82\xd3\xe4\x93\x02**(/v1beta1/{name=projects/*/occurrences/*}\x12\x97\x01\n\x10CreateOccurrence\x12(.grafeas.v1beta1.CreateOccurrenceRequest\x1a\x1b.grafeas.v1beta1.Occurrence"<\x82\xd3\xe4\x93\x026"(/v1beta1/{parent=projects/*}/occurrences:\noccurrence\x12\xba\x01\n\x16BatchCreateOccurrences\x12..grafeas.v1beta1.BatchCreateOccurrencesRequest\x1a/.grafeas.v1beta1.BatchCreateOccurrencesResponse"?\x82\xd3\xe4\x93\x029"4/v1beta1/{parent=projects/*}/occurrences:batchCreate:\x01*\x12\x97\x01\n\x10UpdateOccurrence\x12(.grafeas.v1beta1.UpdateOccurrenceRequest\x1a\x1b.grafeas.v1beta1.Occurrence"<\x82\xd3\xe4\x93\x0262(/v1beta1/{name=projects/*/occurrences/*}:\noccurrence\x12\x8d\x01\n\x11GetOccurrenceNote\x12).grafeas.v1beta1.GetOccurrenceNoteRequest\x1a\x15.grafeas.v1beta1.Note"6\x82\xd3\xe4\x93\x020\x12./v1beta1/{name=projects/*/occurrences/*}/notes\x12m\n\x07GetNote\x12\x1f.grafeas.v1beta1.GetNoteRequest\x1a\x15.grafeas.v1beta1.Note"*\x82\xd3\xe4\x93\x02$\x12"/v1beta1/{name=projects/*/notes/*}\x12~\n\tListNotes\x12!.grafeas.v1beta1.ListNotesRequest\x1a".grafeas.v1beta1.ListNotesResponse"*\x82\xd3\xe4\x93\x02$\x12"/v1beta1/{parent=projects/*}/notes\x12t\n\nDeleteNote\x12".grafeas.v1beta1.DeleteNoteRequest\x1a\x16.google.protobuf.Empty"*\x82\xd3\xe4\x93\x02$*"/v1beta1/{name=projects/*/notes/*}\x12y\n\nCreateNote\x12".grafeas.v1beta1.CreateNoteRequest\x1a\x15.grafeas.v1beta1.Note"0\x82\xd3\xe4\x93\x02*""/v1beta1/{parent=projects/*}/notes:\x04note\x12\xa2\x01\n\x10BatchCreateNotes\x12(.grafeas.v1beta1.BatchCreateNotesRequest\x1a).grafeas.v1beta1.BatchCreateNotesResponse"9\x82\xd3\xe4\x93\x023"./v1beta1/{parent=projects/*}/notes:batchCreate:\x01*\x12y\n\nUpdateNote\x12".grafeas.v1beta1.UpdateNoteRequest\x1a\x15.grafeas.v1beta1.Note"0\x82\xd3\xe4\x93\x02*2"/v1beta1/{name=projects/*/notes/*}:\x04note\x12\xa8\x01\n\x13ListNoteOccurrences\x12+.grafeas.v1beta1.ListNoteOccurrencesRequest\x1a,.grafeas.v1beta1.ListNoteOccurrencesResponse"6\x82\xd3\xe4\x93\x020\x12./v1beta1/{name=projects/*/notes/*}/occurrences\x12\xd9\x01\n"GetVulnerabilityOccurrencesSummary\x12:.grafeas.v1beta1.GetVulnerabilityOccurrencesSummaryRequest\x1a0.grafeas.v1beta1.VulnerabilityOccurrencesSummary"E\x82\xd3\xe4\x93\x02?\x12=/v1beta1/{parent=projects/*}/occurrences:vulnerabilitySummary\x1aT\xcaA containeranalysis.googleapis.com\xd2A.https://www.googleapis.com/auth/cloud-platformBv\n\x12io.grafeas.v1beta1P\x01ZXgoogle.golang.org/genproto/googleapis/devtools/containeranalysis/v1beta1/grafeas;grafeas\xa2\x02\x03GRAb\x06proto3')
_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'google.devtools.containeranalysis.v1beta1.grafeas.grafeas_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
    _globals['DESCRIPTOR']._loaded_options = None
    _globals['DESCRIPTOR']._serialized_options = b'\n\x12io.grafeas.v1beta1P\x01ZXgoogle.golang.org/genproto/googleapis/devtools/containeranalysis/v1beta1/grafeas;grafeas\xa2\x02\x03GRA'
    _globals['_BATCHCREATENOTESREQUEST_NOTESENTRY']._loaded_options = None
    _globals['_BATCHCREATENOTESREQUEST_NOTESENTRY']._serialized_options = b'8\x01'
    _globals['_GRAFEASV1BETA1']._loaded_options = None
    _globals['_GRAFEASV1BETA1']._serialized_options = b'\xcaA containeranalysis.googleapis.com\xd2A.https://www.googleapis.com/auth/cloud-platform'
    _globals['_GRAFEASV1BETA1'].methods_by_name['GetOccurrence']._loaded_options = None
    _globals['_GRAFEASV1BETA1'].methods_by_name['GetOccurrence']._serialized_options = b'\x82\xd3\xe4\x93\x02*\x12(/v1beta1/{name=projects/*/occurrences/*}'
    _globals['_GRAFEASV1BETA1'].methods_by_name['ListOccurrences']._loaded_options = None
    _globals['_GRAFEASV1BETA1'].methods_by_name['ListOccurrences']._serialized_options = b'\x82\xd3\xe4\x93\x02*\x12(/v1beta1/{parent=projects/*}/occurrences'
    _globals['_GRAFEASV1BETA1'].methods_by_name['DeleteOccurrence']._loaded_options = None
    _globals['_GRAFEASV1BETA1'].methods_by_name['DeleteOccurrence']._serialized_options = b'\x82\xd3\xe4\x93\x02**(/v1beta1/{name=projects/*/occurrences/*}'
    _globals['_GRAFEASV1BETA1'].methods_by_name['CreateOccurrence']._loaded_options = None
    _globals['_GRAFEASV1BETA1'].methods_by_name['CreateOccurrence']._serialized_options = b'\x82\xd3\xe4\x93\x026"(/v1beta1/{parent=projects/*}/occurrences:\noccurrence'
    _globals['_GRAFEASV1BETA1'].methods_by_name['BatchCreateOccurrences']._loaded_options = None
    _globals['_GRAFEASV1BETA1'].methods_by_name['BatchCreateOccurrences']._serialized_options = b'\x82\xd3\xe4\x93\x029"4/v1beta1/{parent=projects/*}/occurrences:batchCreate:\x01*'
    _globals['_GRAFEASV1BETA1'].methods_by_name['UpdateOccurrence']._loaded_options = None
    _globals['_GRAFEASV1BETA1'].methods_by_name['UpdateOccurrence']._serialized_options = b'\x82\xd3\xe4\x93\x0262(/v1beta1/{name=projects/*/occurrences/*}:\noccurrence'
    _globals['_GRAFEASV1BETA1'].methods_by_name['GetOccurrenceNote']._loaded_options = None
    _globals['_GRAFEASV1BETA1'].methods_by_name['GetOccurrenceNote']._serialized_options = b'\x82\xd3\xe4\x93\x020\x12./v1beta1/{name=projects/*/occurrences/*}/notes'
    _globals['_GRAFEASV1BETA1'].methods_by_name['GetNote']._loaded_options = None
    _globals['_GRAFEASV1BETA1'].methods_by_name['GetNote']._serialized_options = b'\x82\xd3\xe4\x93\x02$\x12"/v1beta1/{name=projects/*/notes/*}'
    _globals['_GRAFEASV1BETA1'].methods_by_name['ListNotes']._loaded_options = None
    _globals['_GRAFEASV1BETA1'].methods_by_name['ListNotes']._serialized_options = b'\x82\xd3\xe4\x93\x02$\x12"/v1beta1/{parent=projects/*}/notes'
    _globals['_GRAFEASV1BETA1'].methods_by_name['DeleteNote']._loaded_options = None
    _globals['_GRAFEASV1BETA1'].methods_by_name['DeleteNote']._serialized_options = b'\x82\xd3\xe4\x93\x02$*"/v1beta1/{name=projects/*/notes/*}'
    _globals['_GRAFEASV1BETA1'].methods_by_name['CreateNote']._loaded_options = None
    _globals['_GRAFEASV1BETA1'].methods_by_name['CreateNote']._serialized_options = b'\x82\xd3\xe4\x93\x02*""/v1beta1/{parent=projects/*}/notes:\x04note'
    _globals['_GRAFEASV1BETA1'].methods_by_name['BatchCreateNotes']._loaded_options = None
    _globals['_GRAFEASV1BETA1'].methods_by_name['BatchCreateNotes']._serialized_options = b'\x82\xd3\xe4\x93\x023"./v1beta1/{parent=projects/*}/notes:batchCreate:\x01*'
    _globals['_GRAFEASV1BETA1'].methods_by_name['UpdateNote']._loaded_options = None
    _globals['_GRAFEASV1BETA1'].methods_by_name['UpdateNote']._serialized_options = b'\x82\xd3\xe4\x93\x02*2"/v1beta1/{name=projects/*/notes/*}:\x04note'
    _globals['_GRAFEASV1BETA1'].methods_by_name['ListNoteOccurrences']._loaded_options = None
    _globals['_GRAFEASV1BETA1'].methods_by_name['ListNoteOccurrences']._serialized_options = b'\x82\xd3\xe4\x93\x020\x12./v1beta1/{name=projects/*/notes/*}/occurrences'
    _globals['_GRAFEASV1BETA1'].methods_by_name['GetVulnerabilityOccurrencesSummary']._loaded_options = None
    _globals['_GRAFEASV1BETA1'].methods_by_name['GetVulnerabilityOccurrencesSummary']._serialized_options = b'\x82\xd3\xe4\x93\x02?\x12=/v1beta1/{parent=projects/*}/occurrences:vulnerabilitySummary'
    _globals['_OCCURRENCE']._serialized_start = 847
    _globals['_OCCURRENCE']._serialized_end = 1515
    _globals['_RESOURCE']._serialized_start = 1517
    _globals['_RESOURCE']._serialized_end = 1610
    _globals['_NOTE']._serialized_start = 1613
    _globals['_NOTE']._serialized_end = 2381
    _globals['_GETOCCURRENCEREQUEST']._serialized_start = 2383
    _globals['_GETOCCURRENCEREQUEST']._serialized_end = 2419
    _globals['_LISTOCCURRENCESREQUEST']._serialized_start = 2421
    _globals['_LISTOCCURRENCESREQUEST']._serialized_end = 2516
    _globals['_LISTOCCURRENCESRESPONSE']._serialized_start = 2518
    _globals['_LISTOCCURRENCESRESPONSE']._serialized_end = 2618
    _globals['_DELETEOCCURRENCEREQUEST']._serialized_start = 2620
    _globals['_DELETEOCCURRENCEREQUEST']._serialized_end = 2659
    _globals['_CREATEOCCURRENCEREQUEST']._serialized_start = 2661
    _globals['_CREATEOCCURRENCEREQUEST']._serialized_end = 2751
    _globals['_UPDATEOCCURRENCEREQUEST']._serialized_start = 2754
    _globals['_UPDATEOCCURRENCEREQUEST']._serialized_end = 2891
    _globals['_GETNOTEREQUEST']._serialized_start = 2893
    _globals['_GETNOTEREQUEST']._serialized_end = 2923
    _globals['_GETOCCURRENCENOTEREQUEST']._serialized_start = 2925
    _globals['_GETOCCURRENCENOTEREQUEST']._serialized_end = 2965
    _globals['_LISTNOTESREQUEST']._serialized_start = 2967
    _globals['_LISTNOTESREQUEST']._serialized_end = 3056
    _globals['_LISTNOTESRESPONSE']._serialized_start = 3058
    _globals['_LISTNOTESRESPONSE']._serialized_end = 3140
    _globals['_DELETENOTEREQUEST']._serialized_start = 3142
    _globals['_DELETENOTEREQUEST']._serialized_end = 3175
    _globals['_CREATENOTEREQUEST']._serialized_start = 3177
    _globals['_CREATENOTEREQUEST']._serialized_end = 3266
    _globals['_UPDATENOTEREQUEST']._serialized_start = 3268
    _globals['_UPDATENOTEREQUEST']._serialized_end = 3387
    _globals['_LISTNOTEOCCURRENCESREQUEST']._serialized_start = 3389
    _globals['_LISTNOTEOCCURRENCESREQUEST']._serialized_end = 3486
    _globals['_LISTNOTEOCCURRENCESRESPONSE']._serialized_start = 3488
    _globals['_LISTNOTEOCCURRENCESRESPONSE']._serialized_end = 3592
    _globals['_BATCHCREATENOTESREQUEST']._serialized_start = 3595
    _globals['_BATCHCREATENOTESREQUEST']._serialized_end = 3773
    _globals['_BATCHCREATENOTESREQUEST_NOTESENTRY']._serialized_start = 3706
    _globals['_BATCHCREATENOTESREQUEST_NOTESENTRY']._serialized_end = 3773
    _globals['_BATCHCREATENOTESRESPONSE']._serialized_start = 3775
    _globals['_BATCHCREATENOTESRESPONSE']._serialized_end = 3839
    _globals['_BATCHCREATEOCCURRENCESREQUEST']._serialized_start = 3841
    _globals['_BATCHCREATEOCCURRENCESREQUEST']._serialized_end = 3938
    _globals['_BATCHCREATEOCCURRENCESRESPONSE']._serialized_start = 3940
    _globals['_BATCHCREATEOCCURRENCESRESPONSE']._serialized_end = 4022
    _globals['_GETVULNERABILITYOCCURRENCESSUMMARYREQUEST']._serialized_start = 4024
    _globals['_GETVULNERABILITYOCCURRENCESSUMMARYREQUEST']._serialized_end = 4099
    _globals['_VULNERABILITYOCCURRENCESSUMMARY']._serialized_start = 4102
    _globals['_VULNERABILITYOCCURRENCESSUMMARY']._serialized_end = 4395
    _globals['_VULNERABILITYOCCURRENCESSUMMARY_FIXABLETOTALBYDIGEST']._serialized_start = 4225
    _globals['_VULNERABILITYOCCURRENCESSUMMARY_FIXABLETOTALBYDIGEST']._serialized_end = 4395
    _globals['_GRAFEASV1BETA1']._serialized_start = 4398
    _globals['_GRAFEASV1BETA1']._serialized_end = 6726