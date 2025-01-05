"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_runtime_version.ValidateProtobufRuntimeVersion(_runtime_version.Domain.PUBLIC, 5, 28, 1, '', 'google/cloud/vision/v1/image_annotator.proto')
_sym_db = _symbol_database.Default()
from .....google.api import annotations_pb2 as google_dot_api_dot_annotations__pb2
from .....google.api import client_pb2 as google_dot_api_dot_client__pb2
from .....google.api import field_behavior_pb2 as google_dot_api_dot_field__behavior__pb2
from .....google.cloud.vision.v1 import geometry_pb2 as google_dot_cloud_dot_vision_dot_v1_dot_geometry__pb2
from .....google.cloud.vision.v1 import product_search_pb2 as google_dot_cloud_dot_vision_dot_v1_dot_product__search__pb2
from .....google.cloud.vision.v1 import text_annotation_pb2 as google_dot_cloud_dot_vision_dot_v1_dot_text__annotation__pb2
from .....google.cloud.vision.v1 import web_detection_pb2 as google_dot_cloud_dot_vision_dot_v1_dot_web__detection__pb2
from .....google.longrunning import operations_pb2 as google_dot_longrunning_dot_operations__pb2
from google.protobuf import timestamp_pb2 as google_dot_protobuf_dot_timestamp__pb2
from .....google.rpc import status_pb2 as google_dot_rpc_dot_status__pb2
from .....google.type import color_pb2 as google_dot_type_dot_color__pb2
from .....google.type import latlng_pb2 as google_dot_type_dot_latlng__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n,google/cloud/vision/v1/image_annotator.proto\x12\x16google.cloud.vision.v1\x1a\x1cgoogle/api/annotations.proto\x1a\x17google/api/client.proto\x1a\x1fgoogle/api/field_behavior.proto\x1a%google/cloud/vision/v1/geometry.proto\x1a+google/cloud/vision/v1/product_search.proto\x1a,google/cloud/vision/v1/text_annotation.proto\x1a*google/cloud/vision/v1/web_detection.proto\x1a#google/longrunning/operations.proto\x1a\x1fgoogle/protobuf/timestamp.proto\x1a\x17google/rpc/status.proto\x1a\x17google/type/color.proto\x1a\x18google/type/latlng.proto"\x87\x03\n\x07Feature\x122\n\x04type\x18\x01 \x01(\x0e2$.google.cloud.vision.v1.Feature.Type\x12\x13\n\x0bmax_results\x18\x02 \x01(\x05\x12\r\n\x05model\x18\x03 \x01(\t"\xa3\x02\n\x04Type\x12\x14\n\x10TYPE_UNSPECIFIED\x10\x00\x12\x12\n\x0eFACE_DETECTION\x10\x01\x12\x16\n\x12LANDMARK_DETECTION\x10\x02\x12\x12\n\x0eLOGO_DETECTION\x10\x03\x12\x13\n\x0fLABEL_DETECTION\x10\x04\x12\x12\n\x0eTEXT_DETECTION\x10\x05\x12\x1b\n\x17DOCUMENT_TEXT_DETECTION\x10\x0b\x12\x19\n\x15SAFE_SEARCH_DETECTION\x10\x06\x12\x14\n\x10IMAGE_PROPERTIES\x10\x07\x12\x0e\n\nCROP_HINTS\x10\t\x12\x11\n\rWEB_DETECTION\x10\n\x12\x12\n\x0ePRODUCT_SEARCH\x10\x0c\x12\x17\n\x13OBJECT_LOCALIZATION\x10\x13"7\n\x0bImageSource\x12\x15\n\rgcs_image_uri\x18\x01 \x01(\t\x12\x11\n\timage_uri\x18\x02 \x01(\t"M\n\x05Image\x12\x0f\n\x07content\x18\x01 \x01(\x0c\x123\n\x06source\x18\x02 \x01(\x0b2#.google.cloud.vision.v1.ImageSource"\xf6\r\n\x0eFaceAnnotation\x12;\n\rbounding_poly\x18\x01 \x01(\x0b2$.google.cloud.vision.v1.BoundingPoly\x12>\n\x10fd_bounding_poly\x18\x02 \x01(\x0b2$.google.cloud.vision.v1.BoundingPoly\x12B\n\tlandmarks\x18\x03 \x03(\x0b2/.google.cloud.vision.v1.FaceAnnotation.Landmark\x12\x12\n\nroll_angle\x18\x04 \x01(\x02\x12\x11\n\tpan_angle\x18\x05 \x01(\x02\x12\x12\n\ntilt_angle\x18\x06 \x01(\x02\x12\x1c\n\x14detection_confidence\x18\x07 \x01(\x02\x12\x1e\n\x16landmarking_confidence\x18\x08 \x01(\x02\x12:\n\x0ejoy_likelihood\x18\t \x01(\x0e2".google.cloud.vision.v1.Likelihood\x12=\n\x11sorrow_likelihood\x18\n \x01(\x0e2".google.cloud.vision.v1.Likelihood\x12<\n\x10anger_likelihood\x18\x0b \x01(\x0e2".google.cloud.vision.v1.Likelihood\x12?\n\x13surprise_likelihood\x18\x0c \x01(\x0e2".google.cloud.vision.v1.Likelihood\x12D\n\x18under_exposed_likelihood\x18\r \x01(\x0e2".google.cloud.vision.v1.Likelihood\x12>\n\x12blurred_likelihood\x18\x0e \x01(\x0e2".google.cloud.vision.v1.Likelihood\x12?\n\x13headwear_likelihood\x18\x0f \x01(\x0e2".google.cloud.vision.v1.Likelihood\x1a\xe8\x07\n\x08Landmark\x12B\n\x04type\x18\x03 \x01(\x0e24.google.cloud.vision.v1.FaceAnnotation.Landmark.Type\x122\n\x08position\x18\x04 \x01(\x0b2 .google.cloud.vision.v1.Position"\xe3\x06\n\x04Type\x12\x14\n\x10UNKNOWN_LANDMARK\x10\x00\x12\x0c\n\x08LEFT_EYE\x10\x01\x12\r\n\tRIGHT_EYE\x10\x02\x12\x18\n\x14LEFT_OF_LEFT_EYEBROW\x10\x03\x12\x19\n\x15RIGHT_OF_LEFT_EYEBROW\x10\x04\x12\x19\n\x15LEFT_OF_RIGHT_EYEBROW\x10\x05\x12\x1a\n\x16RIGHT_OF_RIGHT_EYEBROW\x10\x06\x12\x19\n\x15MIDPOINT_BETWEEN_EYES\x10\x07\x12\x0c\n\x08NOSE_TIP\x10\x08\x12\r\n\tUPPER_LIP\x10\t\x12\r\n\tLOWER_LIP\x10\n\x12\x0e\n\nMOUTH_LEFT\x10\x0b\x12\x0f\n\x0bMOUTH_RIGHT\x10\x0c\x12\x10\n\x0cMOUTH_CENTER\x10\r\x12\x15\n\x11NOSE_BOTTOM_RIGHT\x10\x0e\x12\x14\n\x10NOSE_BOTTOM_LEFT\x10\x0f\x12\x16\n\x12NOSE_BOTTOM_CENTER\x10\x10\x12\x19\n\x15LEFT_EYE_TOP_BOUNDARY\x10\x11\x12\x19\n\x15LEFT_EYE_RIGHT_CORNER\x10\x12\x12\x1c\n\x18LEFT_EYE_BOTTOM_BOUNDARY\x10\x13\x12\x18\n\x14LEFT_EYE_LEFT_CORNER\x10\x14\x12\x1a\n\x16RIGHT_EYE_TOP_BOUNDARY\x10\x15\x12\x1a\n\x16RIGHT_EYE_RIGHT_CORNER\x10\x16\x12\x1d\n\x19RIGHT_EYE_BOTTOM_BOUNDARY\x10\x17\x12\x19\n\x15RIGHT_EYE_LEFT_CORNER\x10\x18\x12\x1f\n\x1bLEFT_EYEBROW_UPPER_MIDPOINT\x10\x19\x12 \n\x1cRIGHT_EYEBROW_UPPER_MIDPOINT\x10\x1a\x12\x14\n\x10LEFT_EAR_TRAGION\x10\x1b\x12\x15\n\x11RIGHT_EAR_TRAGION\x10\x1c\x12\x12\n\x0eLEFT_EYE_PUPIL\x10\x1d\x12\x13\n\x0fRIGHT_EYE_PUPIL\x10\x1e\x12\x15\n\x11FOREHEAD_GLABELLA\x10\x1f\x12\x11\n\rCHIN_GNATHION\x10 \x12\x14\n\x10CHIN_LEFT_GONION\x10!\x12\x15\n\x11CHIN_RIGHT_GONION\x10"\x12\x15\n\x11LEFT_CHEEK_CENTER\x10#\x12\x16\n\x12RIGHT_CHEEK_CENTER\x10$"4\n\x0cLocationInfo\x12$\n\x07lat_lng\x18\x01 \x01(\x0b2\x13.google.type.LatLng"=\n\x08Property\x12\x0c\n\x04name\x18\x01 \x01(\t\x12\r\n\x05value\x18\x02 \x01(\t\x12\x14\n\x0cuint64_value\x18\x03 \x01(\x04"\xab\x02\n\x10EntityAnnotation\x12\x0b\n\x03mid\x18\x01 \x01(\t\x12\x0e\n\x06locale\x18\x02 \x01(\t\x12\x13\n\x0bdescription\x18\x03 \x01(\t\x12\r\n\x05score\x18\x04 \x01(\x02\x12\x16\n\nconfidence\x18\x05 \x01(\x02B\x02\x18\x01\x12\x12\n\ntopicality\x18\x06 \x01(\x02\x12;\n\rbounding_poly\x18\x07 \x01(\x0b2$.google.cloud.vision.v1.BoundingPoly\x127\n\tlocations\x18\x08 \x03(\x0b2$.google.cloud.vision.v1.LocationInfo\x124\n\nproperties\x18\t \x03(\x0b2 .google.cloud.vision.v1.Property"\x99\x01\n\x19LocalizedObjectAnnotation\x12\x0b\n\x03mid\x18\x01 \x01(\t\x12\x15\n\rlanguage_code\x18\x02 \x01(\t\x12\x0c\n\x04name\x18\x03 \x01(\t\x12\r\n\x05score\x18\x04 \x01(\x02\x12;\n\rbounding_poly\x18\x05 \x01(\x0b2$.google.cloud.vision.v1.BoundingPoly"\x99\x02\n\x14SafeSearchAnnotation\x121\n\x05adult\x18\x01 \x01(\x0e2".google.cloud.vision.v1.Likelihood\x121\n\x05spoof\x18\x02 \x01(\x0e2".google.cloud.vision.v1.Likelihood\x123\n\x07medical\x18\x03 \x01(\x0e2".google.cloud.vision.v1.Likelihood\x124\n\x08violence\x18\x04 \x01(\x0e2".google.cloud.vision.v1.Likelihood\x120\n\x04racy\x18\t \x01(\x0e2".google.cloud.vision.v1.Likelihood"a\n\x0bLatLongRect\x12(\n\x0bmin_lat_lng\x18\x01 \x01(\x0b2\x13.google.type.LatLng\x12(\n\x0bmax_lat_lng\x18\x02 \x01(\x0b2\x13.google.type.LatLng"U\n\tColorInfo\x12!\n\x05color\x18\x01 \x01(\x0b2\x12.google.type.Color\x12\r\n\x05score\x18\x02 \x01(\x02\x12\x16\n\x0epixel_fraction\x18\x03 \x01(\x02"M\n\x18DominantColorsAnnotation\x121\n\x06colors\x18\x01 \x03(\x0b2!.google.cloud.vision.v1.ColorInfo"\\\n\x0fImageProperties\x12I\n\x0fdominant_colors\x18\x01 \x01(\x0b20.google.cloud.vision.v1.DominantColorsAnnotation"x\n\x08CropHint\x12;\n\rbounding_poly\x18\x01 \x01(\x0b2$.google.cloud.vision.v1.BoundingPoly\x12\x12\n\nconfidence\x18\x02 \x01(\x02\x12\x1b\n\x13importance_fraction\x18\x03 \x01(\x02"K\n\x13CropHintsAnnotation\x124\n\ncrop_hints\x18\x01 \x03(\x0b2 .google.cloud.vision.v1.CropHint"(\n\x0fCropHintsParams\x12\x15\n\raspect_ratios\x18\x01 \x03(\x02"5\n\x12WebDetectionParams\x12\x1f\n\x13include_geo_results\x18\x02 \x01(\x08B\x02\x18\x01"c\n\x13TextDetectionParams\x12.\n&enable_text_detection_confidence_score\x18\t \x01(\x08\x12\x1c\n\x14advanced_ocr_options\x18\x0b \x03(\t"\x88\x03\n\x0cImageContext\x12:\n\rlat_long_rect\x18\x01 \x01(\x0b2#.google.cloud.vision.v1.LatLongRect\x12\x16\n\x0elanguage_hints\x18\x02 \x03(\t\x12B\n\x11crop_hints_params\x18\x04 \x01(\x0b2\'.google.cloud.vision.v1.CropHintsParams\x12J\n\x15product_search_params\x18\x05 \x01(\x0b2+.google.cloud.vision.v1.ProductSearchParams\x12H\n\x14web_detection_params\x18\x06 \x01(\x0b2*.google.cloud.vision.v1.WebDetectionParams\x12J\n\x15text_detection_params\x18\x0c \x01(\x0b2+.google.cloud.vision.v1.TextDetectionParams"\xb4\x01\n\x14AnnotateImageRequest\x12,\n\x05image\x18\x01 \x01(\x0b2\x1d.google.cloud.vision.v1.Image\x121\n\x08features\x18\x02 \x03(\x0b2\x1f.google.cloud.vision.v1.Feature\x12;\n\rimage_context\x18\x03 \x01(\x0b2$.google.cloud.vision.v1.ImageContext":\n\x16ImageAnnotationContext\x12\x0b\n\x03uri\x18\x01 \x01(\t\x12\x13\n\x0bpage_number\x18\x02 \x01(\x05"\xe4\x07\n\x15AnnotateImageResponse\x12@\n\x10face_annotations\x18\x01 \x03(\x0b2&.google.cloud.vision.v1.FaceAnnotation\x12F\n\x14landmark_annotations\x18\x02 \x03(\x0b2(.google.cloud.vision.v1.EntityAnnotation\x12B\n\x10logo_annotations\x18\x03 \x03(\x0b2(.google.cloud.vision.v1.EntityAnnotation\x12C\n\x11label_annotations\x18\x04 \x03(\x0b2(.google.cloud.vision.v1.EntityAnnotation\x12W\n\x1clocalized_object_annotations\x18\x16 \x03(\x0b21.google.cloud.vision.v1.LocalizedObjectAnnotation\x12B\n\x10text_annotations\x18\x05 \x03(\x0b2(.google.cloud.vision.v1.EntityAnnotation\x12D\n\x14full_text_annotation\x18\x0c \x01(\x0b2&.google.cloud.vision.v1.TextAnnotation\x12L\n\x16safe_search_annotation\x18\x06 \x01(\x0b2,.google.cloud.vision.v1.SafeSearchAnnotation\x12L\n\x1bimage_properties_annotation\x18\x08 \x01(\x0b2\'.google.cloud.vision.v1.ImageProperties\x12J\n\x15crop_hints_annotation\x18\x0b \x01(\x0b2+.google.cloud.vision.v1.CropHintsAnnotation\x12;\n\rweb_detection\x18\r \x01(\x0b2$.google.cloud.vision.v1.WebDetection\x12L\n\x16product_search_results\x18\x0e \x01(\x0b2,.google.cloud.vision.v1.ProductSearchResults\x12!\n\x05error\x18\t \x01(\x0b2\x12.google.rpc.Status\x12?\n\x07context\x18\x15 \x01(\x0b2..google.cloud.vision.v1.ImageAnnotationContext"\xf5\x01\n\x1aBatchAnnotateImagesRequest\x12C\n\x08requests\x18\x01 \x03(\x0b2,.google.cloud.vision.v1.AnnotateImageRequestB\x03\xe0A\x02\x12\x0e\n\x06parent\x18\x04 \x01(\t\x12S\n\x06labels\x18\x05 \x03(\x0b2>.google.cloud.vision.v1.BatchAnnotateImagesRequest.LabelsEntryB\x03\xe0A\x01\x1a-\n\x0bLabelsEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\r\n\x05value\x18\x02 \x01(\t:\x028\x01"_\n\x1bBatchAnnotateImagesResponse\x12@\n\tresponses\x18\x01 \x03(\x0b2-.google.cloud.vision.v1.AnnotateImageResponse"\xcf\x01\n\x13AnnotateFileRequest\x129\n\x0cinput_config\x18\x01 \x01(\x0b2#.google.cloud.vision.v1.InputConfig\x121\n\x08features\x18\x02 \x03(\x0b2\x1f.google.cloud.vision.v1.Feature\x12;\n\rimage_context\x18\x03 \x01(\x0b2$.google.cloud.vision.v1.ImageContext\x12\r\n\x05pages\x18\x04 \x03(\x05"\xcb\x01\n\x14AnnotateFileResponse\x129\n\x0cinput_config\x18\x01 \x01(\x0b2#.google.cloud.vision.v1.InputConfig\x12@\n\tresponses\x18\x02 \x03(\x0b2-.google.cloud.vision.v1.AnnotateImageResponse\x12\x13\n\x0btotal_pages\x18\x03 \x01(\x05\x12!\n\x05error\x18\x04 \x01(\x0b2\x12.google.rpc.Status"\xf2\x01\n\x19BatchAnnotateFilesRequest\x12B\n\x08requests\x18\x01 \x03(\x0b2+.google.cloud.vision.v1.AnnotateFileRequestB\x03\xe0A\x02\x12\x0e\n\x06parent\x18\x03 \x01(\t\x12R\n\x06labels\x18\x05 \x03(\x0b2=.google.cloud.vision.v1.BatchAnnotateFilesRequest.LabelsEntryB\x03\xe0A\x01\x1a-\n\x0bLabelsEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\r\n\x05value\x18\x02 \x01(\t:\x028\x01"]\n\x1aBatchAnnotateFilesResponse\x12?\n\tresponses\x18\x01 \x03(\x0b2,.google.cloud.vision.v1.AnnotateFileResponse"\x82\x02\n\x18AsyncAnnotateFileRequest\x129\n\x0cinput_config\x18\x01 \x01(\x0b2#.google.cloud.vision.v1.InputConfig\x121\n\x08features\x18\x02 \x03(\x0b2\x1f.google.cloud.vision.v1.Feature\x12;\n\rimage_context\x18\x03 \x01(\x0b2$.google.cloud.vision.v1.ImageContext\x12;\n\routput_config\x18\x04 \x01(\x0b2$.google.cloud.vision.v1.OutputConfig"X\n\x19AsyncAnnotateFileResponse\x12;\n\routput_config\x18\x01 \x01(\x0b2$.google.cloud.vision.v1.OutputConfig"\xc1\x02\n\x1fAsyncBatchAnnotateImagesRequest\x12C\n\x08requests\x18\x01 \x03(\x0b2,.google.cloud.vision.v1.AnnotateImageRequestB\x03\xe0A\x02\x12@\n\routput_config\x18\x02 \x01(\x0b2$.google.cloud.vision.v1.OutputConfigB\x03\xe0A\x02\x12\x0e\n\x06parent\x18\x04 \x01(\t\x12X\n\x06labels\x18\x05 \x03(\x0b2C.google.cloud.vision.v1.AsyncBatchAnnotateImagesRequest.LabelsEntryB\x03\xe0A\x01\x1a-\n\x0bLabelsEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\r\n\x05value\x18\x02 \x01(\t:\x028\x01"_\n AsyncBatchAnnotateImagesResponse\x12;\n\routput_config\x18\x01 \x01(\x0b2$.google.cloud.vision.v1.OutputConfig"\x81\x02\n\x1eAsyncBatchAnnotateFilesRequest\x12G\n\x08requests\x18\x01 \x03(\x0b20.google.cloud.vision.v1.AsyncAnnotateFileRequestB\x03\xe0A\x02\x12\x0e\n\x06parent\x18\x04 \x01(\t\x12W\n\x06labels\x18\x05 \x03(\x0b2B.google.cloud.vision.v1.AsyncBatchAnnotateFilesRequest.LabelsEntryB\x03\xe0A\x01\x1a-\n\x0bLabelsEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\r\n\x05value\x18\x02 \x01(\t:\x028\x01"g\n\x1fAsyncBatchAnnotateFilesResponse\x12D\n\tresponses\x18\x01 \x03(\x0b21.google.cloud.vision.v1.AsyncAnnotateFileResponse"h\n\x0bInputConfig\x125\n\ngcs_source\x18\x01 \x01(\x0b2!.google.cloud.vision.v1.GcsSource\x12\x0f\n\x07content\x18\x03 \x01(\x0c\x12\x11\n\tmime_type\x18\x02 \x01(\t"c\n\x0cOutputConfig\x12?\n\x0fgcs_destination\x18\x01 \x01(\x0b2&.google.cloud.vision.v1.GcsDestination\x12\x12\n\nbatch_size\x18\x02 \x01(\x05"\x18\n\tGcsSource\x12\x0b\n\x03uri\x18\x01 \x01(\t"\x1d\n\x0eGcsDestination\x12\x0b\n\x03uri\x18\x01 \x01(\t"\x88\x02\n\x11OperationMetadata\x12>\n\x05state\x18\x01 \x01(\x0e2/.google.cloud.vision.v1.OperationMetadata.State\x12/\n\x0bcreate_time\x18\x05 \x01(\x0b2\x1a.google.protobuf.Timestamp\x12/\n\x0bupdate_time\x18\x06 \x01(\x0b2\x1a.google.protobuf.Timestamp"Q\n\x05State\x12\x15\n\x11STATE_UNSPECIFIED\x10\x00\x12\x0b\n\x07CREATED\x10\x01\x12\x0b\n\x07RUNNING\x10\x02\x12\x08\n\x04DONE\x10\x03\x12\r\n\tCANCELLED\x10\x04*e\n\nLikelihood\x12\x0b\n\x07UNKNOWN\x10\x00\x12\x11\n\rVERY_UNLIKELY\x10\x01\x12\x0c\n\x08UNLIKELY\x10\x02\x12\x0c\n\x08POSSIBLE\x10\x03\x12\n\n\x06LIKELY\x10\x04\x12\x0f\n\x0bVERY_LIKELY\x10\x052\xf5\n\n\x0eImageAnnotator\x12\x93\x02\n\x13BatchAnnotateImages\x122.google.cloud.vision.v1.BatchAnnotateImagesRequest\x1a3.google.cloud.vision.v1.BatchAnnotateImagesResponse"\x92\x01\xdaA\x08requests\x82\xd3\xe4\x93\x02\x80\x01"\x13/v1/images:annotate:\x01*Z8"3/v1/{parent=projects/*/locations/*}/images:annotate:\x01*Z,"\'/v1/{parent=projects/*}/images:annotate:\x01*\x12\x8c\x02\n\x12BatchAnnotateFiles\x121.google.cloud.vision.v1.BatchAnnotateFilesRequest\x1a2.google.cloud.vision.v1.BatchAnnotateFilesResponse"\x8e\x01\xdaA\x08requests\x82\xd3\xe4\x93\x02}"\x12/v1/files:annotate:\x01*Z7"2/v1/{parent=projects/*/locations/*}/files:annotate:\x01*Z+"&/v1/{parent=projects/*}/files:annotate:\x01*\x12\xeb\x02\n\x18AsyncBatchAnnotateImages\x127.google.cloud.vision.v1.AsyncBatchAnnotateImagesRequest\x1a\x1d.google.longrunning.Operation"\xf6\x01\xcaA5\n AsyncBatchAnnotateImagesResponse\x12\x11OperationMetadata\xdaA\x16requests,output_config\x82\xd3\xe4\x93\x02\x9e\x01"\x1d/v1/images:asyncBatchAnnotate:\x01*ZB"=/v1/{parent=projects/*/locations/*}/images:asyncBatchAnnotate:\x01*Z6"1/v1/{parent=projects/*}/images:asyncBatchAnnotate:\x01*\x12\xd7\x02\n\x17AsyncBatchAnnotateFiles\x126.google.cloud.vision.v1.AsyncBatchAnnotateFilesRequest\x1a\x1d.google.longrunning.Operation"\xe4\x01\xcaA4\n\x1fAsyncBatchAnnotateFilesResponse\x12\x11OperationMetadata\xdaA\x08requests\x82\xd3\xe4\x93\x02\x9b\x01"\x1c/v1/files:asyncBatchAnnotate:\x01*ZA"</v1/{parent=projects/*/locations/*}/files:asyncBatchAnnotate:\x01*Z5"0/v1/{parent=projects/*}/files:asyncBatchAnnotate:\x01*\x1av\xcaA\x15vision.googleapis.com\xd2A[https://www.googleapis.com/auth/cloud-platform,https://www.googleapis.com/auth/cloud-visionBt\n\x1acom.google.cloud.vision.v1B\x13ImageAnnotatorProtoP\x01Z5cloud.google.com/go/vision/v2/apiv1/visionpb;visionpb\xf8\x01\x01\xa2\x02\x04GCVNb\x06proto3')
_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'google.cloud.vision.v1.image_annotator_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
    _globals['DESCRIPTOR']._loaded_options = None
    _globals['DESCRIPTOR']._serialized_options = b'\n\x1acom.google.cloud.vision.v1B\x13ImageAnnotatorProtoP\x01Z5cloud.google.com/go/vision/v2/apiv1/visionpb;visionpb\xf8\x01\x01\xa2\x02\x04GCVN'
    _globals['_ENTITYANNOTATION'].fields_by_name['confidence']._loaded_options = None
    _globals['_ENTITYANNOTATION'].fields_by_name['confidence']._serialized_options = b'\x18\x01'
    _globals['_WEBDETECTIONPARAMS'].fields_by_name['include_geo_results']._loaded_options = None
    _globals['_WEBDETECTIONPARAMS'].fields_by_name['include_geo_results']._serialized_options = b'\x18\x01'
    _globals['_BATCHANNOTATEIMAGESREQUEST_LABELSENTRY']._loaded_options = None
    _globals['_BATCHANNOTATEIMAGESREQUEST_LABELSENTRY']._serialized_options = b'8\x01'
    _globals['_BATCHANNOTATEIMAGESREQUEST'].fields_by_name['requests']._loaded_options = None
    _globals['_BATCHANNOTATEIMAGESREQUEST'].fields_by_name['requests']._serialized_options = b'\xe0A\x02'
    _globals['_BATCHANNOTATEIMAGESREQUEST'].fields_by_name['labels']._loaded_options = None
    _globals['_BATCHANNOTATEIMAGESREQUEST'].fields_by_name['labels']._serialized_options = b'\xe0A\x01'
    _globals['_BATCHANNOTATEFILESREQUEST_LABELSENTRY']._loaded_options = None
    _globals['_BATCHANNOTATEFILESREQUEST_LABELSENTRY']._serialized_options = b'8\x01'
    _globals['_BATCHANNOTATEFILESREQUEST'].fields_by_name['requests']._loaded_options = None
    _globals['_BATCHANNOTATEFILESREQUEST'].fields_by_name['requests']._serialized_options = b'\xe0A\x02'
    _globals['_BATCHANNOTATEFILESREQUEST'].fields_by_name['labels']._loaded_options = None
    _globals['_BATCHANNOTATEFILESREQUEST'].fields_by_name['labels']._serialized_options = b'\xe0A\x01'
    _globals['_ASYNCBATCHANNOTATEIMAGESREQUEST_LABELSENTRY']._loaded_options = None
    _globals['_ASYNCBATCHANNOTATEIMAGESREQUEST_LABELSENTRY']._serialized_options = b'8\x01'
    _globals['_ASYNCBATCHANNOTATEIMAGESREQUEST'].fields_by_name['requests']._loaded_options = None
    _globals['_ASYNCBATCHANNOTATEIMAGESREQUEST'].fields_by_name['requests']._serialized_options = b'\xe0A\x02'
    _globals['_ASYNCBATCHANNOTATEIMAGESREQUEST'].fields_by_name['output_config']._loaded_options = None
    _globals['_ASYNCBATCHANNOTATEIMAGESREQUEST'].fields_by_name['output_config']._serialized_options = b'\xe0A\x02'
    _globals['_ASYNCBATCHANNOTATEIMAGESREQUEST'].fields_by_name['labels']._loaded_options = None
    _globals['_ASYNCBATCHANNOTATEIMAGESREQUEST'].fields_by_name['labels']._serialized_options = b'\xe0A\x01'
    _globals['_ASYNCBATCHANNOTATEFILESREQUEST_LABELSENTRY']._loaded_options = None
    _globals['_ASYNCBATCHANNOTATEFILESREQUEST_LABELSENTRY']._serialized_options = b'8\x01'
    _globals['_ASYNCBATCHANNOTATEFILESREQUEST'].fields_by_name['requests']._loaded_options = None
    _globals['_ASYNCBATCHANNOTATEFILESREQUEST'].fields_by_name['requests']._serialized_options = b'\xe0A\x02'
    _globals['_ASYNCBATCHANNOTATEFILESREQUEST'].fields_by_name['labels']._loaded_options = None
    _globals['_ASYNCBATCHANNOTATEFILESREQUEST'].fields_by_name['labels']._serialized_options = b'\xe0A\x01'
    _globals['_IMAGEANNOTATOR']._loaded_options = None
    _globals['_IMAGEANNOTATOR']._serialized_options = b'\xcaA\x15vision.googleapis.com\xd2A[https://www.googleapis.com/auth/cloud-platform,https://www.googleapis.com/auth/cloud-vision'
    _globals['_IMAGEANNOTATOR'].methods_by_name['BatchAnnotateImages']._loaded_options = None
    _globals['_IMAGEANNOTATOR'].methods_by_name['BatchAnnotateImages']._serialized_options = b'\xdaA\x08requests\x82\xd3\xe4\x93\x02\x80\x01"\x13/v1/images:annotate:\x01*Z8"3/v1/{parent=projects/*/locations/*}/images:annotate:\x01*Z,"\'/v1/{parent=projects/*}/images:annotate:\x01*'
    _globals['_IMAGEANNOTATOR'].methods_by_name['BatchAnnotateFiles']._loaded_options = None
    _globals['_IMAGEANNOTATOR'].methods_by_name['BatchAnnotateFiles']._serialized_options = b'\xdaA\x08requests\x82\xd3\xe4\x93\x02}"\x12/v1/files:annotate:\x01*Z7"2/v1/{parent=projects/*/locations/*}/files:annotate:\x01*Z+"&/v1/{parent=projects/*}/files:annotate:\x01*'
    _globals['_IMAGEANNOTATOR'].methods_by_name['AsyncBatchAnnotateImages']._loaded_options = None
    _globals['_IMAGEANNOTATOR'].methods_by_name['AsyncBatchAnnotateImages']._serialized_options = b'\xcaA5\n AsyncBatchAnnotateImagesResponse\x12\x11OperationMetadata\xdaA\x16requests,output_config\x82\xd3\xe4\x93\x02\x9e\x01"\x1d/v1/images:asyncBatchAnnotate:\x01*ZB"=/v1/{parent=projects/*/locations/*}/images:asyncBatchAnnotate:\x01*Z6"1/v1/{parent=projects/*}/images:asyncBatchAnnotate:\x01*'
    _globals['_IMAGEANNOTATOR'].methods_by_name['AsyncBatchAnnotateFiles']._loaded_options = None
    _globals['_IMAGEANNOTATOR'].methods_by_name['AsyncBatchAnnotateFiles']._serialized_options = b'\xcaA4\n\x1fAsyncBatchAnnotateFilesResponse\x12\x11OperationMetadata\xdaA\x08requests\x82\xd3\xe4\x93\x02\x9b\x01"\x1c/v1/files:asyncBatchAnnotate:\x01*ZA"</v1/{parent=projects/*/locations/*}/files:asyncBatchAnnotate:\x01*Z5"0/v1/{parent=projects/*}/files:asyncBatchAnnotate:\x01*'
    _globals['_LIKELIHOOD']._serialized_start = 8816
    _globals['_LIKELIHOOD']._serialized_end = 8917
    _globals['_FEATURE']._serialized_start = 481
    _globals['_FEATURE']._serialized_end = 872
    _globals['_FEATURE_TYPE']._serialized_start = 581
    _globals['_FEATURE_TYPE']._serialized_end = 872
    _globals['_IMAGESOURCE']._serialized_start = 874
    _globals['_IMAGESOURCE']._serialized_end = 929
    _globals['_IMAGE']._serialized_start = 931
    _globals['_IMAGE']._serialized_end = 1008
    _globals['_FACEANNOTATION']._serialized_start = 1011
    _globals['_FACEANNOTATION']._serialized_end = 2793
    _globals['_FACEANNOTATION_LANDMARK']._serialized_start = 1793
    _globals['_FACEANNOTATION_LANDMARK']._serialized_end = 2793
    _globals['_FACEANNOTATION_LANDMARK_TYPE']._serialized_start = 1926
    _globals['_FACEANNOTATION_LANDMARK_TYPE']._serialized_end = 2793
    _globals['_LOCATIONINFO']._serialized_start = 2795
    _globals['_LOCATIONINFO']._serialized_end = 2847
    _globals['_PROPERTY']._serialized_start = 2849
    _globals['_PROPERTY']._serialized_end = 2910
    _globals['_ENTITYANNOTATION']._serialized_start = 2913
    _globals['_ENTITYANNOTATION']._serialized_end = 3212
    _globals['_LOCALIZEDOBJECTANNOTATION']._serialized_start = 3215
    _globals['_LOCALIZEDOBJECTANNOTATION']._serialized_end = 3368
    _globals['_SAFESEARCHANNOTATION']._serialized_start = 3371
    _globals['_SAFESEARCHANNOTATION']._serialized_end = 3652
    _globals['_LATLONGRECT']._serialized_start = 3654
    _globals['_LATLONGRECT']._serialized_end = 3751
    _globals['_COLORINFO']._serialized_start = 3753
    _globals['_COLORINFO']._serialized_end = 3838
    _globals['_DOMINANTCOLORSANNOTATION']._serialized_start = 3840
    _globals['_DOMINANTCOLORSANNOTATION']._serialized_end = 3917
    _globals['_IMAGEPROPERTIES']._serialized_start = 3919
    _globals['_IMAGEPROPERTIES']._serialized_end = 4011
    _globals['_CROPHINT']._serialized_start = 4013
    _globals['_CROPHINT']._serialized_end = 4133
    _globals['_CROPHINTSANNOTATION']._serialized_start = 4135
    _globals['_CROPHINTSANNOTATION']._serialized_end = 4210
    _globals['_CROPHINTSPARAMS']._serialized_start = 4212
    _globals['_CROPHINTSPARAMS']._serialized_end = 4252
    _globals['_WEBDETECTIONPARAMS']._serialized_start = 4254
    _globals['_WEBDETECTIONPARAMS']._serialized_end = 4307
    _globals['_TEXTDETECTIONPARAMS']._serialized_start = 4309
    _globals['_TEXTDETECTIONPARAMS']._serialized_end = 4408
    _globals['_IMAGECONTEXT']._serialized_start = 4411
    _globals['_IMAGECONTEXT']._serialized_end = 4803
    _globals['_ANNOTATEIMAGEREQUEST']._serialized_start = 4806
    _globals['_ANNOTATEIMAGEREQUEST']._serialized_end = 4986
    _globals['_IMAGEANNOTATIONCONTEXT']._serialized_start = 4988
    _globals['_IMAGEANNOTATIONCONTEXT']._serialized_end = 5046
    _globals['_ANNOTATEIMAGERESPONSE']._serialized_start = 5049
    _globals['_ANNOTATEIMAGERESPONSE']._serialized_end = 6045
    _globals['_BATCHANNOTATEIMAGESREQUEST']._serialized_start = 6048
    _globals['_BATCHANNOTATEIMAGESREQUEST']._serialized_end = 6293
    _globals['_BATCHANNOTATEIMAGESREQUEST_LABELSENTRY']._serialized_start = 6248
    _globals['_BATCHANNOTATEIMAGESREQUEST_LABELSENTRY']._serialized_end = 6293
    _globals['_BATCHANNOTATEIMAGESRESPONSE']._serialized_start = 6295
    _globals['_BATCHANNOTATEIMAGESRESPONSE']._serialized_end = 6390
    _globals['_ANNOTATEFILEREQUEST']._serialized_start = 6393
    _globals['_ANNOTATEFILEREQUEST']._serialized_end = 6600
    _globals['_ANNOTATEFILERESPONSE']._serialized_start = 6603
    _globals['_ANNOTATEFILERESPONSE']._serialized_end = 6806
    _globals['_BATCHANNOTATEFILESREQUEST']._serialized_start = 6809
    _globals['_BATCHANNOTATEFILESREQUEST']._serialized_end = 7051
    _globals['_BATCHANNOTATEFILESREQUEST_LABELSENTRY']._serialized_start = 6248
    _globals['_BATCHANNOTATEFILESREQUEST_LABELSENTRY']._serialized_end = 6293
    _globals['_BATCHANNOTATEFILESRESPONSE']._serialized_start = 7053
    _globals['_BATCHANNOTATEFILESRESPONSE']._serialized_end = 7146
    _globals['_ASYNCANNOTATEFILEREQUEST']._serialized_start = 7149
    _globals['_ASYNCANNOTATEFILEREQUEST']._serialized_end = 7407
    _globals['_ASYNCANNOTATEFILERESPONSE']._serialized_start = 7409
    _globals['_ASYNCANNOTATEFILERESPONSE']._serialized_end = 7497
    _globals['_ASYNCBATCHANNOTATEIMAGESREQUEST']._serialized_start = 7500
    _globals['_ASYNCBATCHANNOTATEIMAGESREQUEST']._serialized_end = 7821
    _globals['_ASYNCBATCHANNOTATEIMAGESREQUEST_LABELSENTRY']._serialized_start = 6248
    _globals['_ASYNCBATCHANNOTATEIMAGESREQUEST_LABELSENTRY']._serialized_end = 6293
    _globals['_ASYNCBATCHANNOTATEIMAGESRESPONSE']._serialized_start = 7823
    _globals['_ASYNCBATCHANNOTATEIMAGESRESPONSE']._serialized_end = 7918
    _globals['_ASYNCBATCHANNOTATEFILESREQUEST']._serialized_start = 7921
    _globals['_ASYNCBATCHANNOTATEFILESREQUEST']._serialized_end = 8178
    _globals['_ASYNCBATCHANNOTATEFILESREQUEST_LABELSENTRY']._serialized_start = 6248
    _globals['_ASYNCBATCHANNOTATEFILESREQUEST_LABELSENTRY']._serialized_end = 6293
    _globals['_ASYNCBATCHANNOTATEFILESRESPONSE']._serialized_start = 8180
    _globals['_ASYNCBATCHANNOTATEFILESRESPONSE']._serialized_end = 8283
    _globals['_INPUTCONFIG']._serialized_start = 8285
    _globals['_INPUTCONFIG']._serialized_end = 8389
    _globals['_OUTPUTCONFIG']._serialized_start = 8391
    _globals['_OUTPUTCONFIG']._serialized_end = 8490
    _globals['_GCSSOURCE']._serialized_start = 8492
    _globals['_GCSSOURCE']._serialized_end = 8516
    _globals['_GCSDESTINATION']._serialized_start = 8518
    _globals['_GCSDESTINATION']._serialized_end = 8547
    _globals['_OPERATIONMETADATA']._serialized_start = 8550
    _globals['_OPERATIONMETADATA']._serialized_end = 8814
    _globals['_OPERATIONMETADATA_STATE']._serialized_start = 8733
    _globals['_OPERATIONMETADATA_STATE']._serialized_end = 8814
    _globals['_IMAGEANNOTATOR']._serialized_start = 8920
    _globals['_IMAGEANNOTATOR']._serialized_end = 10317