"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_runtime_version.ValidateProtobufRuntimeVersion(_runtime_version.Domain.PUBLIC, 5, 28, 1, '', 'google/cloud/dialogflow/v2beta1/intent.proto')
_sym_db = _symbol_database.Default()
from .....google.api import annotations_pb2 as google_dot_api_dot_annotations__pb2
from .....google.api import client_pb2 as google_dot_api_dot_client__pb2
from .....google.api import field_behavior_pb2 as google_dot_api_dot_field__behavior__pb2
from .....google.api import resource_pb2 as google_dot_api_dot_resource__pb2
from .....google.cloud.dialogflow.v2beta1 import context_pb2 as google_dot_cloud_dot_dialogflow_dot_v2beta1_dot_context__pb2
from .....google.longrunning import operations_pb2 as google_dot_longrunning_dot_operations__pb2
from google.protobuf import empty_pb2 as google_dot_protobuf_dot_empty__pb2
from google.protobuf import field_mask_pb2 as google_dot_protobuf_dot_field__mask__pb2
from google.protobuf import struct_pb2 as google_dot_protobuf_dot_struct__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n,google/cloud/dialogflow/v2beta1/intent.proto\x12\x1fgoogle.cloud.dialogflow.v2beta1\x1a\x1cgoogle/api/annotations.proto\x1a\x17google/api/client.proto\x1a\x1fgoogle/api/field_behavior.proto\x1a\x19google/api/resource.proto\x1a-google/cloud/dialogflow/v2beta1/context.proto\x1a#google/longrunning/operations.proto\x1a\x1bgoogle/protobuf/empty.proto\x1a google/protobuf/field_mask.proto\x1a\x1cgoogle/protobuf/struct.proto"\xa3O\n\x06Intent\x12\x11\n\x04name\x18\x01 \x01(\tB\x03\xe0A\x01\x12\x19\n\x0cdisplay_name\x18\x02 \x01(\tB\x03\xe0A\x02\x12P\n\rwebhook_state\x18\x06 \x01(\x0e24.google.cloud.dialogflow.v2beta1.Intent.WebhookStateB\x03\xe0A\x01\x12\x15\n\x08priority\x18\x03 \x01(\x05B\x03\xe0A\x01\x12\x18\n\x0bis_fallback\x18\x04 \x01(\x08B\x03\xe0A\x01\x12\x19\n\nml_enabled\x18\x05 \x01(\x08B\x05\x18\x01\xe0A\x01\x12\x18\n\x0bml_disabled\x18\x13 \x01(\x08B\x03\xe0A\x01\x12\x1f\n\x12live_agent_handoff\x18\x14 \x01(\x08B\x03\xe0A\x01\x12\x1c\n\x0fend_interaction\x18\x15 \x01(\x08B\x03\xe0A\x01\x12 \n\x13input_context_names\x18\x07 \x03(\tB\x03\xe0A\x01\x12\x13\n\x06events\x18\x08 \x03(\tB\x03\xe0A\x01\x12U\n\x10training_phrases\x18\t \x03(\x0b26.google.cloud.dialogflow.v2beta1.Intent.TrainingPhraseB\x03\xe0A\x01\x12\x13\n\x06action\x18\n \x01(\tB\x03\xe0A\x01\x12F\n\x0foutput_contexts\x18\x0b \x03(\x0b2(.google.cloud.dialogflow.v2beta1.ContextB\x03\xe0A\x01\x12\x1b\n\x0ereset_contexts\x18\x0c \x01(\x08B\x03\xe0A\x01\x12J\n\nparameters\x18\r \x03(\x0b21.google.cloud.dialogflow.v2beta1.Intent.ParameterB\x03\xe0A\x01\x12A\n\x08messages\x18\x0e \x03(\x0b2/.google.cloud.dialogflow.v2beta1.Intent.Message\x12a\n\x1adefault_response_platforms\x18\x0f \x03(\x0e28.google.cloud.dialogflow.v2beta1.Intent.Message.PlatformB\x03\xe0A\x01\x12&\n\x19root_followup_intent_name\x18\x10 \x01(\tB\x03\xe0A\x03\x12(\n\x1bparent_followup_intent_name\x18\x11 \x01(\tB\x03\xe0A\x01\x12]\n\x14followup_intent_info\x18\x12 \x03(\x0b2:.google.cloud.dialogflow.v2beta1.Intent.FollowupIntentInfoB\x03\xe0A\x03\x1a\xf1\x02\n\x0eTrainingPhrase\x12\x11\n\x04name\x18\x01 \x01(\tB\x03\xe0A\x03\x12N\n\x04type\x18\x02 \x01(\x0e2;.google.cloud.dialogflow.v2beta1.Intent.TrainingPhrase.TypeB\x03\xe0A\x02\x12O\n\x05parts\x18\x03 \x03(\x0b2;.google.cloud.dialogflow.v2beta1.Intent.TrainingPhrase.PartB\x03\xe0A\x02\x12\x1e\n\x11times_added_count\x18\x04 \x01(\x05B\x03\xe0A\x01\x1aN\n\x04Part\x12\x0c\n\x04text\x18\x01 \x01(\t\x12\x13\n\x0bentity_type\x18\x02 \x01(\t\x12\r\n\x05alias\x18\x03 \x01(\t\x12\x14\n\x0cuser_defined\x18\x04 \x01(\x08";\n\x04Type\x12\x14\n\x10TYPE_UNSPECIFIED\x10\x00\x12\x0b\n\x07EXAMPLE\x10\x01\x12\x10\n\x08TEMPLATE\x10\x02\x1a\x02\x08\x01\x1a\xac\x01\n\tParameter\x12\x0c\n\x04name\x18\x01 \x01(\t\x12\x14\n\x0cdisplay_name\x18\x02 \x01(\t\x12\r\n\x05value\x18\x03 \x01(\t\x12\x15\n\rdefault_value\x18\x04 \x01(\t\x12 \n\x18entity_type_display_name\x18\x05 \x01(\t\x12\x11\n\tmandatory\x18\x06 \x01(\x08\x12\x0f\n\x07prompts\x18\x07 \x03(\t\x12\x0f\n\x07is_list\x18\x08 \x01(\x08\x1a\xc2@\n\x07Message\x12D\n\x04text\x18\x01 \x01(\x0b24.google.cloud.dialogflow.v2beta1.Intent.Message.TextH\x00\x12F\n\x05image\x18\x02 \x01(\x0b25.google.cloud.dialogflow.v2beta1.Intent.Message.ImageH\x00\x12U\n\rquick_replies\x18\x03 \x01(\x0b2<.google.cloud.dialogflow.v2beta1.Intent.Message.QuickRepliesH\x00\x12D\n\x04card\x18\x04 \x01(\x0b24.google.cloud.dialogflow.v2beta1.Intent.Message.CardH\x00\x12*\n\x07payload\x18\x05 \x01(\x0b2\x17.google.protobuf.StructH\x00\x12[\n\x10simple_responses\x18\x07 \x01(\x0b2?.google.cloud.dialogflow.v2beta1.Intent.Message.SimpleResponsesH\x00\x12O\n\nbasic_card\x18\x08 \x01(\x0b29.google.cloud.dialogflow.v2beta1.Intent.Message.BasicCardH\x00\x12R\n\x0bsuggestions\x18\t \x01(\x0b2;.google.cloud.dialogflow.v2beta1.Intent.Message.SuggestionsH\x00\x12`\n\x13link_out_suggestion\x18\n \x01(\x0b2A.google.cloud.dialogflow.v2beta1.Intent.Message.LinkOutSuggestionH\x00\x12Q\n\x0blist_select\x18\x0b \x01(\x0b2:.google.cloud.dialogflow.v2beta1.Intent.Message.ListSelectH\x00\x12Y\n\x0fcarousel_select\x18\x0c \x01(\x0b2>.google.cloud.dialogflow.v2beta1.Intent.Message.CarouselSelectH\x00\x12b\n\x14telephony_play_audio\x18\r \x01(\x0b2B.google.cloud.dialogflow.v2beta1.Intent.Message.TelephonyPlayAudioH\x00\x12p\n\x1btelephony_synthesize_speech\x18\x0e \x01(\x0b2I.google.cloud.dialogflow.v2beta1.Intent.Message.TelephonySynthesizeSpeechH\x00\x12h\n\x17telephony_transfer_call\x18\x0f \x01(\x0b2E.google.cloud.dialogflow.v2beta1.Intent.Message.TelephonyTransferCallH\x00\x12K\n\x08rbm_text\x18\x12 \x01(\x0b27.google.cloud.dialogflow.v2beta1.Intent.Message.RbmTextH\x00\x12e\n\x18rbm_standalone_rich_card\x18\x13 \x01(\x0b2A.google.cloud.dialogflow.v2beta1.Intent.Message.RbmStandaloneCardH\x00\x12a\n\x16rbm_carousel_rich_card\x18\x14 \x01(\x0b2?.google.cloud.dialogflow.v2beta1.Intent.Message.RbmCarouselCardH\x00\x12b\n\x14browse_carousel_card\x18\x16 \x01(\x0b2B.google.cloud.dialogflow.v2beta1.Intent.Message.BrowseCarouselCardH\x00\x12O\n\ntable_card\x18\x17 \x01(\x0b29.google.cloud.dialogflow.v2beta1.Intent.Message.TableCardH\x00\x12U\n\rmedia_content\x18\x18 \x01(\x0b2<.google.cloud.dialogflow.v2beta1.Intent.Message.MediaContentH\x00\x12O\n\x08platform\x18\x06 \x01(\x0e28.google.cloud.dialogflow.v2beta1.Intent.Message.PlatformB\x03\xe0A\x01\x1a\x14\n\x04Text\x12\x0c\n\x04text\x18\x01 \x03(\t\x1a6\n\x05Image\x12\x11\n\timage_uri\x18\x01 \x01(\t\x12\x1a\n\x12accessibility_text\x18\x02 \x01(\t\x1a4\n\x0cQuickReplies\x12\r\n\x05title\x18\x01 \x01(\t\x12\x15\n\rquick_replies\x18\x02 \x03(\t\x1a\xb2\x01\n\x04Card\x12\r\n\x05title\x18\x01 \x01(\t\x12\x10\n\x08subtitle\x18\x02 \x01(\t\x12\x11\n\timage_uri\x18\x03 \x01(\t\x12L\n\x07buttons\x18\x04 \x03(\x0b2;.google.cloud.dialogflow.v2beta1.Intent.Message.Card.Button\x1a(\n\x06Button\x12\x0c\n\x04text\x18\x01 \x01(\t\x12\x10\n\x08postback\x18\x02 \x01(\t\x1aL\n\x0eSimpleResponse\x12\x16\n\x0etext_to_speech\x18\x01 \x01(\t\x12\x0c\n\x04ssml\x18\x02 \x01(\t\x12\x14\n\x0cdisplay_text\x18\x03 \x01(\t\x1ak\n\x0fSimpleResponses\x12X\n\x10simple_responses\x18\x01 \x03(\x0b2>.google.cloud.dialogflow.v2beta1.Intent.Message.SimpleResponse\x1a\xfe\x02\n\tBasicCard\x12\r\n\x05title\x18\x01 \x01(\t\x12\x10\n\x08subtitle\x18\x02 \x01(\t\x12\x16\n\x0eformatted_text\x18\x03 \x01(\t\x12D\n\x05image\x18\x04 \x01(\x0b25.google.cloud.dialogflow.v2beta1.Intent.Message.Image\x12Q\n\x07buttons\x18\x05 \x03(\x0b2@.google.cloud.dialogflow.v2beta1.Intent.Message.BasicCard.Button\x1a\x9e\x01\n\x06Button\x12\r\n\x05title\x18\x01 \x01(\t\x12g\n\x0fopen_uri_action\x18\x02 \x01(\x0b2N.google.cloud.dialogflow.v2beta1.Intent.Message.BasicCard.Button.OpenUriAction\x1a\x1c\n\rOpenUriAction\x12\x0b\n\x03uri\x18\x01 \x01(\t\x1a\x1b\n\nSuggestion\x12\r\n\x05title\x18\x01 \x01(\t\x1a^\n\x0bSuggestions\x12O\n\x0bsuggestions\x18\x01 \x03(\x0b2:.google.cloud.dialogflow.v2beta1.Intent.Message.Suggestion\x1a:\n\x11LinkOutSuggestion\x12\x18\n\x10destination_name\x18\x01 \x01(\t\x12\x0b\n\x03uri\x18\x02 \x01(\t\x1a\xc3\x02\n\nListSelect\x12\r\n\x05title\x18\x01 \x01(\t\x12N\n\x05items\x18\x02 \x03(\x0b2?.google.cloud.dialogflow.v2beta1.Intent.Message.ListSelect.Item\x12\x15\n\x08subtitle\x18\x03 \x01(\tB\x03\xe0A\x01\x1a\xbe\x01\n\x04Item\x12L\n\x04info\x18\x01 \x01(\x0b2>.google.cloud.dialogflow.v2beta1.Intent.Message.SelectItemInfo\x12\r\n\x05title\x18\x02 \x01(\t\x12\x13\n\x0bdescription\x18\x03 \x01(\t\x12D\n\x05image\x18\x04 \x01(\x0b25.google.cloud.dialogflow.v2beta1.Intent.Message.Image\x1a\xa5\x02\n\x0eCarouselSelect\x12R\n\x05items\x18\x01 \x03(\x0b2C.google.cloud.dialogflow.v2beta1.Intent.Message.CarouselSelect.Item\x1a\xbe\x01\n\x04Item\x12L\n\x04info\x18\x01 \x01(\x0b2>.google.cloud.dialogflow.v2beta1.Intent.Message.SelectItemInfo\x12\r\n\x05title\x18\x02 \x01(\t\x12\x13\n\x0bdescription\x18\x03 \x01(\t\x12D\n\x05image\x18\x04 \x01(\x0b25.google.cloud.dialogflow.v2beta1.Intent.Message.Image\x1a/\n\x0eSelectItemInfo\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\x10\n\x08synonyms\x18\x02 \x03(\t\x1a\'\n\x12TelephonyPlayAudio\x12\x11\n\taudio_uri\x18\x01 \x01(\t\x1aE\n\x19TelephonySynthesizeSpeech\x12\x0e\n\x04text\x18\x01 \x01(\tH\x00\x12\x0e\n\x04ssml\x18\x02 \x01(\tH\x00B\x08\n\x06source\x1a-\n\x15TelephonyTransferCall\x12\x14\n\x0cphone_number\x18\x01 \x01(\t\x1an\n\x07RbmText\x12\x0c\n\x04text\x18\x01 \x01(\t\x12U\n\x0erbm_suggestion\x18\x02 \x03(\x0b2=.google.cloud.dialogflow.v2beta1.Intent.Message.RbmSuggestion\x1a\x87\x02\n\x0fRbmCarouselCard\x12]\n\ncard_width\x18\x01 \x01(\x0e2I.google.cloud.dialogflow.v2beta1.Intent.Message.RbmCarouselCard.CardWidth\x12U\n\rcard_contents\x18\x02 \x03(\x0b2>.google.cloud.dialogflow.v2beta1.Intent.Message.RbmCardContent">\n\tCardWidth\x12\x1a\n\x16CARD_WIDTH_UNSPECIFIED\x10\x00\x12\t\n\x05SMALL\x10\x01\x12\n\n\x06MEDIUM\x10\x02\x1a\x82\x04\n\x11RbmStandaloneCard\x12k\n\x10card_orientation\x18\x01 \x01(\x0e2Q.google.cloud.dialogflow.v2beta1.Intent.Message.RbmStandaloneCard.CardOrientation\x12|\n\x19thumbnail_image_alignment\x18\x02 \x01(\x0e2Y.google.cloud.dialogflow.v2beta1.Intent.Message.RbmStandaloneCard.ThumbnailImageAlignment\x12T\n\x0ccard_content\x18\x03 \x01(\x0b2>.google.cloud.dialogflow.v2beta1.Intent.Message.RbmCardContent"Q\n\x0fCardOrientation\x12 \n\x1cCARD_ORIENTATION_UNSPECIFIED\x10\x00\x12\x0e\n\nHORIZONTAL\x10\x01\x12\x0c\n\x08VERTICAL\x10\x02"Y\n\x17ThumbnailImageAlignment\x12)\n%THUMBNAIL_IMAGE_ALIGNMENT_UNSPECIFIED\x10\x00\x12\x08\n\x04LEFT\x10\x01\x12\t\n\x05RIGHT\x10\x02\x1a\xb9\x03\n\x0eRbmCardContent\x12\r\n\x05title\x18\x01 \x01(\t\x12\x13\n\x0bdescription\x18\x02 \x01(\t\x12V\n\x05media\x18\x03 \x01(\x0b2G.google.cloud.dialogflow.v2beta1.Intent.Message.RbmCardContent.RbmMedia\x12R\n\x0bsuggestions\x18\x04 \x03(\x0b2=.google.cloud.dialogflow.v2beta1.Intent.Message.RbmSuggestion\x1a\xd6\x01\n\x08RbmMedia\x12\x10\n\x08file_uri\x18\x01 \x01(\t\x12\x15\n\rthumbnail_uri\x18\x02 \x01(\t\x12^\n\x06height\x18\x03 \x01(\x0e2N.google.cloud.dialogflow.v2beta1.Intent.Message.RbmCardContent.RbmMedia.Height"A\n\x06Height\x12\x16\n\x12HEIGHT_UNSPECIFIED\x10\x00\x12\t\n\x05SHORT\x10\x01\x12\n\n\x06MEDIUM\x10\x02\x12\x08\n\x04TALL\x10\x03\x1a\xc7\x01\n\rRbmSuggestion\x12R\n\x05reply\x18\x01 \x01(\x0b2A.google.cloud.dialogflow.v2beta1.Intent.Message.RbmSuggestedReplyH\x00\x12T\n\x06action\x18\x02 \x01(\x0b2B.google.cloud.dialogflow.v2beta1.Intent.Message.RbmSuggestedActionH\x00B\x0c\n\nsuggestion\x1a8\n\x11RbmSuggestedReply\x12\x0c\n\x04text\x18\x01 \x01(\t\x12\x15\n\rpostback_data\x18\x02 \x01(\t\x1a\x9b\x04\n\x12RbmSuggestedAction\x12\x0c\n\x04text\x18\x01 \x01(\t\x12\x15\n\rpostback_data\x18\x02 \x01(\t\x12i\n\x04dial\x18\x03 \x01(\x0b2Y.google.cloud.dialogflow.v2beta1.Intent.Message.RbmSuggestedAction.RbmSuggestedActionDialH\x00\x12p\n\x08open_url\x18\x04 \x01(\x0b2\\.google.cloud.dialogflow.v2beta1.Intent.Message.RbmSuggestedAction.RbmSuggestedActionOpenUriH\x00\x12|\n\x0eshare_location\x18\x05 \x01(\x0b2b.google.cloud.dialogflow.v2beta1.Intent.Message.RbmSuggestedAction.RbmSuggestedActionShareLocationH\x00\x1a.\n\x16RbmSuggestedActionDial\x12\x14\n\x0cphone_number\x18\x01 \x01(\t\x1a(\n\x19RbmSuggestedActionOpenUri\x12\x0b\n\x03uri\x18\x01 \x01(\t\x1a!\n\x1fRbmSuggestedActionShareLocationB\x08\n\x06action\x1a\x8e\x04\n\x0cMediaContent\x12b\n\nmedia_type\x18\x01 \x01(\x0e2N.google.cloud.dialogflow.v2beta1.Intent.Message.MediaContent.ResponseMediaType\x12g\n\rmedia_objects\x18\x02 \x03(\x0b2P.google.cloud.dialogflow.v2beta1.Intent.Message.MediaContent.ResponseMediaObject\x1a\xeb\x01\n\x13ResponseMediaObject\x12\x0c\n\x04name\x18\x01 \x01(\t\x12\x13\n\x0bdescription\x18\x02 \x01(\t\x12L\n\x0blarge_image\x18\x03 \x01(\x0b25.google.cloud.dialogflow.v2beta1.Intent.Message.ImageH\x00\x12E\n\x04icon\x18\x04 \x01(\x0b25.google.cloud.dialogflow.v2beta1.Intent.Message.ImageH\x00\x12\x13\n\x0bcontent_url\x18\x05 \x01(\tB\x07\n\x05image"C\n\x11ResponseMediaType\x12#\n\x1fRESPONSE_MEDIA_TYPE_UNSPECIFIED\x10\x00\x12\t\n\x05AUDIO\x10\x01\x1a\x80\x07\n\x12BrowseCarouselCard\x12h\n\x05items\x18\x01 \x03(\x0b2Y.google.cloud.dialogflow.v2beta1.Intent.Message.BrowseCarouselCard.BrowseCarouselCardItem\x12u\n\x15image_display_options\x18\x02 \x01(\x0e2V.google.cloud.dialogflow.v2beta1.Intent.Message.BrowseCarouselCard.ImageDisplayOptions\x1a\x90\x04\n\x16BrowseCarouselCardItem\x12\x80\x01\n\x0fopen_uri_action\x18\x01 \x01(\x0b2g.google.cloud.dialogflow.v2beta1.Intent.Message.BrowseCarouselCard.BrowseCarouselCardItem.OpenUrlAction\x12\r\n\x05title\x18\x02 \x01(\t\x12\x13\n\x0bdescription\x18\x03 \x01(\t\x12D\n\x05image\x18\x04 \x01(\x0b25.google.cloud.dialogflow.v2beta1.Intent.Message.Image\x12\x0e\n\x06footer\x18\x05 \x01(\t\x1a\xf8\x01\n\rOpenUrlAction\x12\x0b\n\x03url\x18\x01 \x01(\t\x12\x8a\x01\n\rurl_type_hint\x18\x03 \x01(\x0e2s.google.cloud.dialogflow.v2beta1.Intent.Message.BrowseCarouselCard.BrowseCarouselCardItem.OpenUrlAction.UrlTypeHint"M\n\x0bUrlTypeHint\x12\x1d\n\x19URL_TYPE_HINT_UNSPECIFIED\x10\x00\x12\x0e\n\nAMP_ACTION\x10\x01\x12\x0f\n\x0bAMP_CONTENT\x10\x02"v\n\x13ImageDisplayOptions\x12%\n!IMAGE_DISPLAY_OPTIONS_UNSPECIFIED\x10\x00\x12\x08\n\x04GRAY\x10\x01\x12\t\n\x05WHITE\x10\x02\x12\x0b\n\x07CROPPED\x10\x03\x12\x16\n\x12BLURRED_BACKGROUND\x10\x04\x1a\xee\x02\n\tTableCard\x12\r\n\x05title\x18\x01 \x01(\t\x12\x10\n\x08subtitle\x18\x02 \x01(\t\x12D\n\x05image\x18\x03 \x01(\x0b25.google.cloud.dialogflow.v2beta1.Intent.Message.Image\x12[\n\x11column_properties\x18\x04 \x03(\x0b2@.google.cloud.dialogflow.v2beta1.Intent.Message.ColumnProperties\x12J\n\x04rows\x18\x05 \x03(\x0b2<.google.cloud.dialogflow.v2beta1.Intent.Message.TableCardRow\x12Q\n\x07buttons\x18\x06 \x03(\x0b2@.google.cloud.dialogflow.v2beta1.Intent.Message.BasicCard.Button\x1a\xfa\x01\n\x10ColumnProperties\x12\x0e\n\x06header\x18\x01 \x01(\t\x12r\n\x14horizontal_alignment\x18\x02 \x01(\x0e2T.google.cloud.dialogflow.v2beta1.Intent.Message.ColumnProperties.HorizontalAlignment"b\n\x13HorizontalAlignment\x12$\n HORIZONTAL_ALIGNMENT_UNSPECIFIED\x10\x00\x12\x0b\n\x07LEADING\x10\x01\x12\n\n\x06CENTER\x10\x02\x12\x0c\n\x08TRAILING\x10\x03\x1as\n\x0cTableCardRow\x12L\n\x05cells\x18\x01 \x03(\x0b2=.google.cloud.dialogflow.v2beta1.Intent.Message.TableCardCell\x12\x15\n\rdivider_after\x18\x02 \x01(\x08\x1a\x1d\n\rTableCardCell\x12\x0c\n\x04text\x18\x01 \x01(\t"\xaf\x01\n\x08Platform\x12\x18\n\x14PLATFORM_UNSPECIFIED\x10\x00\x12\x0c\n\x08FACEBOOK\x10\x01\x12\t\n\x05SLACK\x10\x02\x12\x0c\n\x08TELEGRAM\x10\x03\x12\x07\n\x03KIK\x10\x04\x12\t\n\x05SKYPE\x10\x05\x12\x08\n\x04LINE\x10\x06\x12\t\n\x05VIBER\x10\x07\x12\x15\n\x11ACTIONS_ON_GOOGLE\x10\x08\x12\r\n\tTELEPHONY\x10\n\x12\x13\n\x0fGOOGLE_HANGOUTS\x10\x0bB\t\n\x07message\x1aW\n\x12FollowupIntentInfo\x12\x1c\n\x14followup_intent_name\x18\x01 \x01(\t\x12#\n\x1bparent_followup_intent_name\x18\x02 \x01(\t"t\n\x0cWebhookState\x12\x1d\n\x19WEBHOOK_STATE_UNSPECIFIED\x10\x00\x12\x19\n\x15WEBHOOK_STATE_ENABLED\x10\x01\x12*\n&WEBHOOK_STATE_ENABLED_FOR_SLOT_FILLING\x10\x02:\x91\x01\xeaA\x8d\x01\n dialogflow.googleapis.com/Intent\x12)projects/{project}/agent/intents/{intent}\x12>projects/{project}/locations/{location}/agent/intents/{intent}"\xd3\x01\n\x12ListIntentsRequest\x128\n\x06parent\x18\x01 \x01(\tB(\xe0A\x02\xfaA"\x12 dialogflow.googleapis.com/Intent\x12\x1a\n\rlanguage_code\x18\x02 \x01(\tB\x03\xe0A\x01\x12@\n\x0bintent_view\x18\x03 \x01(\x0e2+.google.cloud.dialogflow.v2beta1.IntentView\x12\x11\n\tpage_size\x18\x04 \x01(\x05\x12\x12\n\npage_token\x18\x05 \x01(\t"h\n\x13ListIntentsResponse\x128\n\x07intents\x18\x01 \x03(\x0b2\'.google.cloud.dialogflow.v2beta1.Intent\x12\x17\n\x0fnext_page_token\x18\x02 \x01(\t"\xa8\x01\n\x10GetIntentRequest\x126\n\x04name\x18\x01 \x01(\tB(\xe0A\x02\xfaA"\n dialogflow.googleapis.com/Intent\x12\x1a\n\rlanguage_code\x18\x02 \x01(\tB\x03\xe0A\x01\x12@\n\x0bintent_view\x18\x03 \x01(\x0e2+.google.cloud.dialogflow.v2beta1.IntentView"\xeb\x01\n\x13CreateIntentRequest\x128\n\x06parent\x18\x01 \x01(\tB(\xe0A\x02\xfaA"\x12 dialogflow.googleapis.com/Intent\x12<\n\x06intent\x18\x02 \x01(\x0b2\'.google.cloud.dialogflow.v2beta1.IntentB\x03\xe0A\x02\x12\x1a\n\rlanguage_code\x18\x03 \x01(\tB\x03\xe0A\x01\x12@\n\x0bintent_view\x18\x04 \x01(\x0e2+.google.cloud.dialogflow.v2beta1.IntentView"\xe2\x01\n\x13UpdateIntentRequest\x12<\n\x06intent\x18\x01 \x01(\x0b2\'.google.cloud.dialogflow.v2beta1.IntentB\x03\xe0A\x02\x12\x1a\n\rlanguage_code\x18\x02 \x01(\tB\x03\xe0A\x01\x12/\n\x0bupdate_mask\x18\x03 \x01(\x0b2\x1a.google.protobuf.FieldMask\x12@\n\x0bintent_view\x18\x04 \x01(\x0e2+.google.cloud.dialogflow.v2beta1.IntentView"M\n\x13DeleteIntentRequest\x126\n\x04name\x18\x01 \x01(\tB(\xe0A\x02\xfaA"\n dialogflow.googleapis.com/Intent"\xdd\x02\n\x19BatchUpdateIntentsRequest\x128\n\x06parent\x18\x01 \x01(\tB(\xe0A\x02\xfaA"\x12 dialogflow.googleapis.com/Intent\x12\x1a\n\x10intent_batch_uri\x18\x02 \x01(\tH\x00\x12K\n\x13intent_batch_inline\x18\x03 \x01(\x0b2,.google.cloud.dialogflow.v2beta1.IntentBatchH\x00\x12\x1a\n\rlanguage_code\x18\x04 \x01(\tB\x03\xe0A\x01\x12/\n\x0bupdate_mask\x18\x05 \x01(\x0b2\x1a.google.protobuf.FieldMask\x12@\n\x0bintent_view\x18\x06 \x01(\x0e2+.google.cloud.dialogflow.v2beta1.IntentViewB\x0e\n\x0cintent_batch"V\n\x1aBatchUpdateIntentsResponse\x128\n\x07intents\x18\x01 \x03(\x0b2\'.google.cloud.dialogflow.v2beta1.Intent"\x94\x01\n\x19BatchDeleteIntentsRequest\x128\n\x06parent\x18\x01 \x01(\tB(\xe0A\x02\xfaA"\x12 dialogflow.googleapis.com/Intent\x12=\n\x07intents\x18\x02 \x03(\x0b2\'.google.cloud.dialogflow.v2beta1.IntentB\x03\xe0A\x02"G\n\x0bIntentBatch\x128\n\x07intents\x18\x01 \x03(\x0b2\'.google.cloud.dialogflow.v2beta1.Intent*?\n\nIntentView\x12\x1b\n\x17INTENT_VIEW_UNSPECIFIED\x10\x00\x12\x14\n\x10INTENT_VIEW_FULL\x10\x012\xa1\x12\n\x07Intents\x12\x8e\x03\n\x0bListIntents\x123.google.cloud.dialogflow.v2beta1.ListIntentsRequest\x1a4.google.cloud.dialogflow.v2beta1.ListIntentsResponse"\x93\x02\xdaA\x06parent\xdaA\x14parent,language_code\x82\xd3\xe4\x93\x02\xec\x01\x12*/v2beta1/{parent=projects/*/agent}/intentsZ8\x126/v2beta1/{parent=projects/*/locations/*/agent}/intentsZ;\x129/v2beta1/{parent=projects/*/agent/environments/*}/intentsZG\x12E/v2beta1/{parent=projects/*/locations/*/agent/environments/*}/intents\x12\xf2\x01\n\tGetIntent\x121.google.cloud.dialogflow.v2beta1.GetIntentRequest\x1a\'.google.cloud.dialogflow.v2beta1.Intent"\x88\x01\xdaA\x04name\xdaA\x12name,language_code\x82\xd3\xe4\x93\x02f\x12*/v2beta1/{name=projects/*/agent/intents/*}Z8\x126/v2beta1/{name=projects/*/locations/*/agent/intents/*}\x12\x9a\x02\n\x0cCreateIntent\x124.google.cloud.dialogflow.v2beta1.CreateIntentRequest\x1a\'.google.cloud.dialogflow.v2beta1.Intent"\xaa\x01\xdaA\rparent,intent\xdaA\x1bparent,intent,language_code\x82\xd3\xe4\x93\x02v"*/v2beta1/{parent=projects/*/agent}/intents:\x06intentZ@"6/v2beta1/{parent=projects/*/locations/*/agent}/intents:\x06intent\x12\xd3\x02\n\x0cUpdateIntent\x124.google.cloud.dialogflow.v2beta1.UpdateIntentRequest\x1a\'.google.cloud.dialogflow.v2beta1.Intent"\xe3\x01\xdaA\x12intent,update_mask\xdaA\x06intent\xdaA\x14intent,language_code\xdaA intent,language_code,update_mask\x82\xd3\xe4\x93\x02\x84\x0121/v2beta1/{intent.name=projects/*/agent/intents/*}:\x06intentZG2=/v2beta1/{intent.name=projects/*/locations/*/agent/intents/*}:\x06intent\x12\xd1\x01\n\x0cDeleteIntent\x124.google.cloud.dialogflow.v2beta1.DeleteIntentRequest\x1a\x16.google.protobuf.Empty"s\xdaA\x04name\x82\xd3\xe4\x93\x02f**/v2beta1/{name=projects/*/agent/intents/*}Z8*6/v2beta1/{name=projects/*/locations/*/agent/intents/*}\x12\x8b\x03\n\x12BatchUpdateIntents\x12:.google.cloud.dialogflow.v2beta1.BatchUpdateIntentsRequest\x1a\x1d.google.longrunning.Operation"\x99\x02\xcaAT\n:google.cloud.dialogflow.v2beta1.BatchUpdateIntentsResponse\x12\x16google.protobuf.Struct\xdaA\x17parent,intent_batch_uri\xdaA\x1aparent,intent_batch_inline\x82\xd3\xe4\x93\x02\x84\x01"6/v2beta1/{parent=projects/*/agent}/intents:batchUpdate:\x01*ZG"B/v2beta1/{parent=projects/*/locations/*/agent}/intents:batchUpdate:\x01*\x12\xc0\x02\n\x12BatchDeleteIntents\x12:.google.cloud.dialogflow.v2beta1.BatchDeleteIntentsRequest\x1a\x1d.google.longrunning.Operation"\xce\x01\xcaA/\n\x15google.protobuf.Empty\x12\x16google.protobuf.Struct\xdaA\x0eparent,intents\x82\xd3\xe4\x93\x02\x84\x01"6/v2beta1/{parent=projects/*/agent}/intents:batchDelete:\x01*ZG"B/v2beta1/{parent=projects/*/locations/*/agent}/intents:batchDelete:\x01*\x1ax\xcaA\x19dialogflow.googleapis.com\xd2AYhttps://www.googleapis.com/auth/cloud-platform,https://www.googleapis.com/auth/dialogflowB\xa0\x01\n#com.google.cloud.dialogflow.v2beta1B\x0bIntentProtoP\x01ZCcloud.google.com/go/dialogflow/apiv2beta1/dialogflowpb;dialogflowpb\xa2\x02\x02DF\xaa\x02\x1fGoogle.Cloud.Dialogflow.V2Beta1b\x06proto3')
_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'google.cloud.dialogflow.v2beta1.intent_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
    _globals['DESCRIPTOR']._loaded_options = None
    _globals['DESCRIPTOR']._serialized_options = b'\n#com.google.cloud.dialogflow.v2beta1B\x0bIntentProtoP\x01ZCcloud.google.com/go/dialogflow/apiv2beta1/dialogflowpb;dialogflowpb\xa2\x02\x02DF\xaa\x02\x1fGoogle.Cloud.Dialogflow.V2Beta1'
    _globals['_INTENT_TRAININGPHRASE_TYPE'].values_by_name['TEMPLATE']._loaded_options = None
    _globals['_INTENT_TRAININGPHRASE_TYPE'].values_by_name['TEMPLATE']._serialized_options = b'\x08\x01'
    _globals['_INTENT_TRAININGPHRASE'].fields_by_name['name']._loaded_options = None
    _globals['_INTENT_TRAININGPHRASE'].fields_by_name['name']._serialized_options = b'\xe0A\x03'
    _globals['_INTENT_TRAININGPHRASE'].fields_by_name['type']._loaded_options = None
    _globals['_INTENT_TRAININGPHRASE'].fields_by_name['type']._serialized_options = b'\xe0A\x02'
    _globals['_INTENT_TRAININGPHRASE'].fields_by_name['parts']._loaded_options = None
    _globals['_INTENT_TRAININGPHRASE'].fields_by_name['parts']._serialized_options = b'\xe0A\x02'
    _globals['_INTENT_TRAININGPHRASE'].fields_by_name['times_added_count']._loaded_options = None
    _globals['_INTENT_TRAININGPHRASE'].fields_by_name['times_added_count']._serialized_options = b'\xe0A\x01'
    _globals['_INTENT_MESSAGE_LISTSELECT'].fields_by_name['subtitle']._loaded_options = None
    _globals['_INTENT_MESSAGE_LISTSELECT'].fields_by_name['subtitle']._serialized_options = b'\xe0A\x01'
    _globals['_INTENT_MESSAGE'].fields_by_name['platform']._loaded_options = None
    _globals['_INTENT_MESSAGE'].fields_by_name['platform']._serialized_options = b'\xe0A\x01'
    _globals['_INTENT'].fields_by_name['name']._loaded_options = None
    _globals['_INTENT'].fields_by_name['name']._serialized_options = b'\xe0A\x01'
    _globals['_INTENT'].fields_by_name['display_name']._loaded_options = None
    _globals['_INTENT'].fields_by_name['display_name']._serialized_options = b'\xe0A\x02'
    _globals['_INTENT'].fields_by_name['webhook_state']._loaded_options = None
    _globals['_INTENT'].fields_by_name['webhook_state']._serialized_options = b'\xe0A\x01'
    _globals['_INTENT'].fields_by_name['priority']._loaded_options = None
    _globals['_INTENT'].fields_by_name['priority']._serialized_options = b'\xe0A\x01'
    _globals['_INTENT'].fields_by_name['is_fallback']._loaded_options = None
    _globals['_INTENT'].fields_by_name['is_fallback']._serialized_options = b'\xe0A\x01'
    _globals['_INTENT'].fields_by_name['ml_enabled']._loaded_options = None
    _globals['_INTENT'].fields_by_name['ml_enabled']._serialized_options = b'\x18\x01\xe0A\x01'
    _globals['_INTENT'].fields_by_name['ml_disabled']._loaded_options = None
    _globals['_INTENT'].fields_by_name['ml_disabled']._serialized_options = b'\xe0A\x01'
    _globals['_INTENT'].fields_by_name['live_agent_handoff']._loaded_options = None
    _globals['_INTENT'].fields_by_name['live_agent_handoff']._serialized_options = b'\xe0A\x01'
    _globals['_INTENT'].fields_by_name['end_interaction']._loaded_options = None
    _globals['_INTENT'].fields_by_name['end_interaction']._serialized_options = b'\xe0A\x01'
    _globals['_INTENT'].fields_by_name['input_context_names']._loaded_options = None
    _globals['_INTENT'].fields_by_name['input_context_names']._serialized_options = b'\xe0A\x01'
    _globals['_INTENT'].fields_by_name['events']._loaded_options = None
    _globals['_INTENT'].fields_by_name['events']._serialized_options = b'\xe0A\x01'
    _globals['_INTENT'].fields_by_name['training_phrases']._loaded_options = None
    _globals['_INTENT'].fields_by_name['training_phrases']._serialized_options = b'\xe0A\x01'
    _globals['_INTENT'].fields_by_name['action']._loaded_options = None
    _globals['_INTENT'].fields_by_name['action']._serialized_options = b'\xe0A\x01'
    _globals['_INTENT'].fields_by_name['output_contexts']._loaded_options = None
    _globals['_INTENT'].fields_by_name['output_contexts']._serialized_options = b'\xe0A\x01'
    _globals['_INTENT'].fields_by_name['reset_contexts']._loaded_options = None
    _globals['_INTENT'].fields_by_name['reset_contexts']._serialized_options = b'\xe0A\x01'
    _globals['_INTENT'].fields_by_name['parameters']._loaded_options = None
    _globals['_INTENT'].fields_by_name['parameters']._serialized_options = b'\xe0A\x01'
    _globals['_INTENT'].fields_by_name['default_response_platforms']._loaded_options = None
    _globals['_INTENT'].fields_by_name['default_response_platforms']._serialized_options = b'\xe0A\x01'
    _globals['_INTENT'].fields_by_name['root_followup_intent_name']._loaded_options = None
    _globals['_INTENT'].fields_by_name['root_followup_intent_name']._serialized_options = b'\xe0A\x03'
    _globals['_INTENT'].fields_by_name['parent_followup_intent_name']._loaded_options = None
    _globals['_INTENT'].fields_by_name['parent_followup_intent_name']._serialized_options = b'\xe0A\x01'
    _globals['_INTENT'].fields_by_name['followup_intent_info']._loaded_options = None
    _globals['_INTENT'].fields_by_name['followup_intent_info']._serialized_options = b'\xe0A\x03'
    _globals['_INTENT']._loaded_options = None
    _globals['_INTENT']._serialized_options = b'\xeaA\x8d\x01\n dialogflow.googleapis.com/Intent\x12)projects/{project}/agent/intents/{intent}\x12>projects/{project}/locations/{location}/agent/intents/{intent}'
    _globals['_LISTINTENTSREQUEST'].fields_by_name['parent']._loaded_options = None
    _globals['_LISTINTENTSREQUEST'].fields_by_name['parent']._serialized_options = b'\xe0A\x02\xfaA"\x12 dialogflow.googleapis.com/Intent'
    _globals['_LISTINTENTSREQUEST'].fields_by_name['language_code']._loaded_options = None
    _globals['_LISTINTENTSREQUEST'].fields_by_name['language_code']._serialized_options = b'\xe0A\x01'
    _globals['_GETINTENTREQUEST'].fields_by_name['name']._loaded_options = None
    _globals['_GETINTENTREQUEST'].fields_by_name['name']._serialized_options = b'\xe0A\x02\xfaA"\n dialogflow.googleapis.com/Intent'
    _globals['_GETINTENTREQUEST'].fields_by_name['language_code']._loaded_options = None
    _globals['_GETINTENTREQUEST'].fields_by_name['language_code']._serialized_options = b'\xe0A\x01'
    _globals['_CREATEINTENTREQUEST'].fields_by_name['parent']._loaded_options = None
    _globals['_CREATEINTENTREQUEST'].fields_by_name['parent']._serialized_options = b'\xe0A\x02\xfaA"\x12 dialogflow.googleapis.com/Intent'
    _globals['_CREATEINTENTREQUEST'].fields_by_name['intent']._loaded_options = None
    _globals['_CREATEINTENTREQUEST'].fields_by_name['intent']._serialized_options = b'\xe0A\x02'
    _globals['_CREATEINTENTREQUEST'].fields_by_name['language_code']._loaded_options = None
    _globals['_CREATEINTENTREQUEST'].fields_by_name['language_code']._serialized_options = b'\xe0A\x01'
    _globals['_UPDATEINTENTREQUEST'].fields_by_name['intent']._loaded_options = None
    _globals['_UPDATEINTENTREQUEST'].fields_by_name['intent']._serialized_options = b'\xe0A\x02'
    _globals['_UPDATEINTENTREQUEST'].fields_by_name['language_code']._loaded_options = None
    _globals['_UPDATEINTENTREQUEST'].fields_by_name['language_code']._serialized_options = b'\xe0A\x01'
    _globals['_DELETEINTENTREQUEST'].fields_by_name['name']._loaded_options = None
    _globals['_DELETEINTENTREQUEST'].fields_by_name['name']._serialized_options = b'\xe0A\x02\xfaA"\n dialogflow.googleapis.com/Intent'
    _globals['_BATCHUPDATEINTENTSREQUEST'].fields_by_name['parent']._loaded_options = None
    _globals['_BATCHUPDATEINTENTSREQUEST'].fields_by_name['parent']._serialized_options = b'\xe0A\x02\xfaA"\x12 dialogflow.googleapis.com/Intent'
    _globals['_BATCHUPDATEINTENTSREQUEST'].fields_by_name['language_code']._loaded_options = None
    _globals['_BATCHUPDATEINTENTSREQUEST'].fields_by_name['language_code']._serialized_options = b'\xe0A\x01'
    _globals['_BATCHDELETEINTENTSREQUEST'].fields_by_name['parent']._loaded_options = None
    _globals['_BATCHDELETEINTENTSREQUEST'].fields_by_name['parent']._serialized_options = b'\xe0A\x02\xfaA"\x12 dialogflow.googleapis.com/Intent'
    _globals['_BATCHDELETEINTENTSREQUEST'].fields_by_name['intents']._loaded_options = None
    _globals['_BATCHDELETEINTENTSREQUEST'].fields_by_name['intents']._serialized_options = b'\xe0A\x02'
    _globals['_INTENTS']._loaded_options = None
    _globals['_INTENTS']._serialized_options = b'\xcaA\x19dialogflow.googleapis.com\xd2AYhttps://www.googleapis.com/auth/cloud-platform,https://www.googleapis.com/auth/dialogflow'
    _globals['_INTENTS'].methods_by_name['ListIntents']._loaded_options = None
    _globals['_INTENTS'].methods_by_name['ListIntents']._serialized_options = b'\xdaA\x06parent\xdaA\x14parent,language_code\x82\xd3\xe4\x93\x02\xec\x01\x12*/v2beta1/{parent=projects/*/agent}/intentsZ8\x126/v2beta1/{parent=projects/*/locations/*/agent}/intentsZ;\x129/v2beta1/{parent=projects/*/agent/environments/*}/intentsZG\x12E/v2beta1/{parent=projects/*/locations/*/agent/environments/*}/intents'
    _globals['_INTENTS'].methods_by_name['GetIntent']._loaded_options = None
    _globals['_INTENTS'].methods_by_name['GetIntent']._serialized_options = b'\xdaA\x04name\xdaA\x12name,language_code\x82\xd3\xe4\x93\x02f\x12*/v2beta1/{name=projects/*/agent/intents/*}Z8\x126/v2beta1/{name=projects/*/locations/*/agent/intents/*}'
    _globals['_INTENTS'].methods_by_name['CreateIntent']._loaded_options = None
    _globals['_INTENTS'].methods_by_name['CreateIntent']._serialized_options = b'\xdaA\rparent,intent\xdaA\x1bparent,intent,language_code\x82\xd3\xe4\x93\x02v"*/v2beta1/{parent=projects/*/agent}/intents:\x06intentZ@"6/v2beta1/{parent=projects/*/locations/*/agent}/intents:\x06intent'
    _globals['_INTENTS'].methods_by_name['UpdateIntent']._loaded_options = None
    _globals['_INTENTS'].methods_by_name['UpdateIntent']._serialized_options = b'\xdaA\x12intent,update_mask\xdaA\x06intent\xdaA\x14intent,language_code\xdaA intent,language_code,update_mask\x82\xd3\xe4\x93\x02\x84\x0121/v2beta1/{intent.name=projects/*/agent/intents/*}:\x06intentZG2=/v2beta1/{intent.name=projects/*/locations/*/agent/intents/*}:\x06intent'
    _globals['_INTENTS'].methods_by_name['DeleteIntent']._loaded_options = None
    _globals['_INTENTS'].methods_by_name['DeleteIntent']._serialized_options = b'\xdaA\x04name\x82\xd3\xe4\x93\x02f**/v2beta1/{name=projects/*/agent/intents/*}Z8*6/v2beta1/{name=projects/*/locations/*/agent/intents/*}'
    _globals['_INTENTS'].methods_by_name['BatchUpdateIntents']._loaded_options = None
    _globals['_INTENTS'].methods_by_name['BatchUpdateIntents']._serialized_options = b'\xcaAT\n:google.cloud.dialogflow.v2beta1.BatchUpdateIntentsResponse\x12\x16google.protobuf.Struct\xdaA\x17parent,intent_batch_uri\xdaA\x1aparent,intent_batch_inline\x82\xd3\xe4\x93\x02\x84\x01"6/v2beta1/{parent=projects/*/agent}/intents:batchUpdate:\x01*ZG"B/v2beta1/{parent=projects/*/locations/*/agent}/intents:batchUpdate:\x01*'
    _globals['_INTENTS'].methods_by_name['BatchDeleteIntents']._loaded_options = None
    _globals['_INTENTS'].methods_by_name['BatchDeleteIntents']._serialized_options = b'\xcaA/\n\x15google.protobuf.Empty\x12\x16google.protobuf.Struct\xdaA\x0eparent,intents\x82\xd3\xe4\x93\x02\x84\x01"6/v2beta1/{parent=projects/*/agent}/intents:batchDelete:\x01*ZG"B/v2beta1/{parent=projects/*/locations/*/agent}/intents:batchDelete:\x01*'
    _globals['_INTENTVIEW']._serialized_start = 12224
    _globals['_INTENTVIEW']._serialized_end = 12287
    _globals['_INTENT']._serialized_start = 374
    _globals['_INTENT']._serialized_end = 10521
    _globals['_INTENT_TRAININGPHRASE']._serialized_start = 1361
    _globals['_INTENT_TRAININGPHRASE']._serialized_end = 1730
    _globals['_INTENT_TRAININGPHRASE_PART']._serialized_start = 1591
    _globals['_INTENT_TRAININGPHRASE_PART']._serialized_end = 1669
    _globals['_INTENT_TRAININGPHRASE_TYPE']._serialized_start = 1671
    _globals['_INTENT_TRAININGPHRASE_TYPE']._serialized_end = 1730
    _globals['_INTENT_PARAMETER']._serialized_start = 1733
    _globals['_INTENT_PARAMETER']._serialized_end = 1905
    _globals['_INTENT_MESSAGE']._serialized_start = 1908
    _globals['_INTENT_MESSAGE']._serialized_end = 10166
    _globals['_INTENT_MESSAGE_TEXT']._serialized_start = 3740
    _globals['_INTENT_MESSAGE_TEXT']._serialized_end = 3760
    _globals['_INTENT_MESSAGE_IMAGE']._serialized_start = 3762
    _globals['_INTENT_MESSAGE_IMAGE']._serialized_end = 3816
    _globals['_INTENT_MESSAGE_QUICKREPLIES']._serialized_start = 3818
    _globals['_INTENT_MESSAGE_QUICKREPLIES']._serialized_end = 3870
    _globals['_INTENT_MESSAGE_CARD']._serialized_start = 3873
    _globals['_INTENT_MESSAGE_CARD']._serialized_end = 4051
    _globals['_INTENT_MESSAGE_CARD_BUTTON']._serialized_start = 4011
    _globals['_INTENT_MESSAGE_CARD_BUTTON']._serialized_end = 4051
    _globals['_INTENT_MESSAGE_SIMPLERESPONSE']._serialized_start = 4053
    _globals['_INTENT_MESSAGE_SIMPLERESPONSE']._serialized_end = 4129
    _globals['_INTENT_MESSAGE_SIMPLERESPONSES']._serialized_start = 4131
    _globals['_INTENT_MESSAGE_SIMPLERESPONSES']._serialized_end = 4238
    _globals['_INTENT_MESSAGE_BASICCARD']._serialized_start = 4241
    _globals['_INTENT_MESSAGE_BASICCARD']._serialized_end = 4623
    _globals['_INTENT_MESSAGE_BASICCARD_BUTTON']._serialized_start = 4465
    _globals['_INTENT_MESSAGE_BASICCARD_BUTTON']._serialized_end = 4623
    _globals['_INTENT_MESSAGE_BASICCARD_BUTTON_OPENURIACTION']._serialized_start = 4595
    _globals['_INTENT_MESSAGE_BASICCARD_BUTTON_OPENURIACTION']._serialized_end = 4623
    _globals['_INTENT_MESSAGE_SUGGESTION']._serialized_start = 4625
    _globals['_INTENT_MESSAGE_SUGGESTION']._serialized_end = 4652
    _globals['_INTENT_MESSAGE_SUGGESTIONS']._serialized_start = 4654
    _globals['_INTENT_MESSAGE_SUGGESTIONS']._serialized_end = 4748
    _globals['_INTENT_MESSAGE_LINKOUTSUGGESTION']._serialized_start = 4750
    _globals['_INTENT_MESSAGE_LINKOUTSUGGESTION']._serialized_end = 4808
    _globals['_INTENT_MESSAGE_LISTSELECT']._serialized_start = 4811
    _globals['_INTENT_MESSAGE_LISTSELECT']._serialized_end = 5134
    _globals['_INTENT_MESSAGE_LISTSELECT_ITEM']._serialized_start = 4944
    _globals['_INTENT_MESSAGE_LISTSELECT_ITEM']._serialized_end = 5134
    _globals['_INTENT_MESSAGE_CAROUSELSELECT']._serialized_start = 5137
    _globals['_INTENT_MESSAGE_CAROUSELSELECT']._serialized_end = 5430
    _globals['_INTENT_MESSAGE_CAROUSELSELECT_ITEM']._serialized_start = 4944
    _globals['_INTENT_MESSAGE_CAROUSELSELECT_ITEM']._serialized_end = 5134
    _globals['_INTENT_MESSAGE_SELECTITEMINFO']._serialized_start = 5432
    _globals['_INTENT_MESSAGE_SELECTITEMINFO']._serialized_end = 5479
    _globals['_INTENT_MESSAGE_TELEPHONYPLAYAUDIO']._serialized_start = 5481
    _globals['_INTENT_MESSAGE_TELEPHONYPLAYAUDIO']._serialized_end = 5520
    _globals['_INTENT_MESSAGE_TELEPHONYSYNTHESIZESPEECH']._serialized_start = 5522
    _globals['_INTENT_MESSAGE_TELEPHONYSYNTHESIZESPEECH']._serialized_end = 5591
    _globals['_INTENT_MESSAGE_TELEPHONYTRANSFERCALL']._serialized_start = 5593
    _globals['_INTENT_MESSAGE_TELEPHONYTRANSFERCALL']._serialized_end = 5638
    _globals['_INTENT_MESSAGE_RBMTEXT']._serialized_start = 5640
    _globals['_INTENT_MESSAGE_RBMTEXT']._serialized_end = 5750
    _globals['_INTENT_MESSAGE_RBMCAROUSELCARD']._serialized_start = 5753
    _globals['_INTENT_MESSAGE_RBMCAROUSELCARD']._serialized_end = 6016
    _globals['_INTENT_MESSAGE_RBMCAROUSELCARD_CARDWIDTH']._serialized_start = 5954
    _globals['_INTENT_MESSAGE_RBMCAROUSELCARD_CARDWIDTH']._serialized_end = 6016
    _globals['_INTENT_MESSAGE_RBMSTANDALONECARD']._serialized_start = 6019
    _globals['_INTENT_MESSAGE_RBMSTANDALONECARD']._serialized_end = 6533
    _globals['_INTENT_MESSAGE_RBMSTANDALONECARD_CARDORIENTATION']._serialized_start = 6361
    _globals['_INTENT_MESSAGE_RBMSTANDALONECARD_CARDORIENTATION']._serialized_end = 6442
    _globals['_INTENT_MESSAGE_RBMSTANDALONECARD_THUMBNAILIMAGEALIGNMENT']._serialized_start = 6444
    _globals['_INTENT_MESSAGE_RBMSTANDALONECARD_THUMBNAILIMAGEALIGNMENT']._serialized_end = 6533
    _globals['_INTENT_MESSAGE_RBMCARDCONTENT']._serialized_start = 6536
    _globals['_INTENT_MESSAGE_RBMCARDCONTENT']._serialized_end = 6977
    _globals['_INTENT_MESSAGE_RBMCARDCONTENT_RBMMEDIA']._serialized_start = 6763
    _globals['_INTENT_MESSAGE_RBMCARDCONTENT_RBMMEDIA']._serialized_end = 6977
    _globals['_INTENT_MESSAGE_RBMCARDCONTENT_RBMMEDIA_HEIGHT']._serialized_start = 6912
    _globals['_INTENT_MESSAGE_RBMCARDCONTENT_RBMMEDIA_HEIGHT']._serialized_end = 6977
    _globals['_INTENT_MESSAGE_RBMSUGGESTION']._serialized_start = 6980
    _globals['_INTENT_MESSAGE_RBMSUGGESTION']._serialized_end = 7179
    _globals['_INTENT_MESSAGE_RBMSUGGESTEDREPLY']._serialized_start = 7181
    _globals['_INTENT_MESSAGE_RBMSUGGESTEDREPLY']._serialized_end = 7237
    _globals['_INTENT_MESSAGE_RBMSUGGESTEDACTION']._serialized_start = 7240
    _globals['_INTENT_MESSAGE_RBMSUGGESTEDACTION']._serialized_end = 7779
    _globals['_INTENT_MESSAGE_RBMSUGGESTEDACTION_RBMSUGGESTEDACTIONDIAL']._serialized_start = 7646
    _globals['_INTENT_MESSAGE_RBMSUGGESTEDACTION_RBMSUGGESTEDACTIONDIAL']._serialized_end = 7692
    _globals['_INTENT_MESSAGE_RBMSUGGESTEDACTION_RBMSUGGESTEDACTIONOPENURI']._serialized_start = 7694
    _globals['_INTENT_MESSAGE_RBMSUGGESTEDACTION_RBMSUGGESTEDACTIONOPENURI']._serialized_end = 7734
    _globals['_INTENT_MESSAGE_RBMSUGGESTEDACTION_RBMSUGGESTEDACTIONSHARELOCATION']._serialized_start = 7736
    _globals['_INTENT_MESSAGE_RBMSUGGESTEDACTION_RBMSUGGESTEDACTIONSHARELOCATION']._serialized_end = 7769
    _globals['_INTENT_MESSAGE_MEDIACONTENT']._serialized_start = 7782
    _globals['_INTENT_MESSAGE_MEDIACONTENT']._serialized_end = 8308
    _globals['_INTENT_MESSAGE_MEDIACONTENT_RESPONSEMEDIAOBJECT']._serialized_start = 8004
    _globals['_INTENT_MESSAGE_MEDIACONTENT_RESPONSEMEDIAOBJECT']._serialized_end = 8239
    _globals['_INTENT_MESSAGE_MEDIACONTENT_RESPONSEMEDIATYPE']._serialized_start = 8241
    _globals['_INTENT_MESSAGE_MEDIACONTENT_RESPONSEMEDIATYPE']._serialized_end = 8308
    _globals['_INTENT_MESSAGE_BROWSECAROUSELCARD']._serialized_start = 8311
    _globals['_INTENT_MESSAGE_BROWSECAROUSELCARD']._serialized_end = 9207
    _globals['_INTENT_MESSAGE_BROWSECAROUSELCARD_BROWSECAROUSELCARDITEM']._serialized_start = 8559
    _globals['_INTENT_MESSAGE_BROWSECAROUSELCARD_BROWSECAROUSELCARDITEM']._serialized_end = 9087
    _globals['_INTENT_MESSAGE_BROWSECAROUSELCARD_BROWSECAROUSELCARDITEM_OPENURLACTION']._serialized_start = 8839
    _globals['_INTENT_MESSAGE_BROWSECAROUSELCARD_BROWSECAROUSELCARDITEM_OPENURLACTION']._serialized_end = 9087
    _globals['_INTENT_MESSAGE_BROWSECAROUSELCARD_BROWSECAROUSELCARDITEM_OPENURLACTION_URLTYPEHINT']._serialized_start = 9010
    _globals['_INTENT_MESSAGE_BROWSECAROUSELCARD_BROWSECAROUSELCARDITEM_OPENURLACTION_URLTYPEHINT']._serialized_end = 9087
    _globals['_INTENT_MESSAGE_BROWSECAROUSELCARD_IMAGEDISPLAYOPTIONS']._serialized_start = 9089
    _globals['_INTENT_MESSAGE_BROWSECAROUSELCARD_IMAGEDISPLAYOPTIONS']._serialized_end = 9207
    _globals['_INTENT_MESSAGE_TABLECARD']._serialized_start = 9210
    _globals['_INTENT_MESSAGE_TABLECARD']._serialized_end = 9576
    _globals['_INTENT_MESSAGE_COLUMNPROPERTIES']._serialized_start = 9579
    _globals['_INTENT_MESSAGE_COLUMNPROPERTIES']._serialized_end = 9829
    _globals['_INTENT_MESSAGE_COLUMNPROPERTIES_HORIZONTALALIGNMENT']._serialized_start = 9731
    _globals['_INTENT_MESSAGE_COLUMNPROPERTIES_HORIZONTALALIGNMENT']._serialized_end = 9829
    _globals['_INTENT_MESSAGE_TABLECARDROW']._serialized_start = 9831
    _globals['_INTENT_MESSAGE_TABLECARDROW']._serialized_end = 9946
    _globals['_INTENT_MESSAGE_TABLECARDCELL']._serialized_start = 9948
    _globals['_INTENT_MESSAGE_TABLECARDCELL']._serialized_end = 9977
    _globals['_INTENT_MESSAGE_PLATFORM']._serialized_start = 9980
    _globals['_INTENT_MESSAGE_PLATFORM']._serialized_end = 10155
    _globals['_INTENT_FOLLOWUPINTENTINFO']._serialized_start = 10168
    _globals['_INTENT_FOLLOWUPINTENTINFO']._serialized_end = 10255
    _globals['_INTENT_WEBHOOKSTATE']._serialized_start = 10257
    _globals['_INTENT_WEBHOOKSTATE']._serialized_end = 10373
    _globals['_LISTINTENTSREQUEST']._serialized_start = 10524
    _globals['_LISTINTENTSREQUEST']._serialized_end = 10735
    _globals['_LISTINTENTSRESPONSE']._serialized_start = 10737
    _globals['_LISTINTENTSRESPONSE']._serialized_end = 10841
    _globals['_GETINTENTREQUEST']._serialized_start = 10844
    _globals['_GETINTENTREQUEST']._serialized_end = 11012
    _globals['_CREATEINTENTREQUEST']._serialized_start = 11015
    _globals['_CREATEINTENTREQUEST']._serialized_end = 11250
    _globals['_UPDATEINTENTREQUEST']._serialized_start = 11253
    _globals['_UPDATEINTENTREQUEST']._serialized_end = 11479
    _globals['_DELETEINTENTREQUEST']._serialized_start = 11481
    _globals['_DELETEINTENTREQUEST']._serialized_end = 11558
    _globals['_BATCHUPDATEINTENTSREQUEST']._serialized_start = 11561
    _globals['_BATCHUPDATEINTENTSREQUEST']._serialized_end = 11910
    _globals['_BATCHUPDATEINTENTSRESPONSE']._serialized_start = 11912
    _globals['_BATCHUPDATEINTENTSRESPONSE']._serialized_end = 11998
    _globals['_BATCHDELETEINTENTSREQUEST']._serialized_start = 12001
    _globals['_BATCHDELETEINTENTSREQUEST']._serialized_end = 12149
    _globals['_INTENTBATCH']._serialized_start = 12151
    _globals['_INTENTBATCH']._serialized_end = 12222
    _globals['_INTENTS']._serialized_start = 12290
    _globals['_INTENTS']._serialized_end = 14627