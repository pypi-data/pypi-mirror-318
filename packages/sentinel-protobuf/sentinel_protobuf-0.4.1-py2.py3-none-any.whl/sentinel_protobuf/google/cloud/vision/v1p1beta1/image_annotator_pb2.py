"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_runtime_version.ValidateProtobufRuntimeVersion(_runtime_version.Domain.PUBLIC, 5, 28, 1, '', 'google/cloud/vision/v1p1beta1/image_annotator.proto')
_sym_db = _symbol_database.Default()
from .....google.api import annotations_pb2 as google_dot_api_dot_annotations__pb2
from .....google.api import client_pb2 as google_dot_api_dot_client__pb2
from .....google.api import field_behavior_pb2 as google_dot_api_dot_field__behavior__pb2
from .....google.cloud.vision.v1p1beta1 import geometry_pb2 as google_dot_cloud_dot_vision_dot_v1p1beta1_dot_geometry__pb2
from .....google.cloud.vision.v1p1beta1 import text_annotation_pb2 as google_dot_cloud_dot_vision_dot_v1p1beta1_dot_text__annotation__pb2
from .....google.cloud.vision.v1p1beta1 import web_detection_pb2 as google_dot_cloud_dot_vision_dot_v1p1beta1_dot_web__detection__pb2
from .....google.rpc import status_pb2 as google_dot_rpc_dot_status__pb2
from .....google.type import color_pb2 as google_dot_type_dot_color__pb2
from .....google.type import latlng_pb2 as google_dot_type_dot_latlng__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n3google/cloud/vision/v1p1beta1/image_annotator.proto\x12\x1dgoogle.cloud.vision.v1p1beta1\x1a\x1cgoogle/api/annotations.proto\x1a\x17google/api/client.proto\x1a\x1fgoogle/api/field_behavior.proto\x1a,google/cloud/vision/v1p1beta1/geometry.proto\x1a3google/cloud/vision/v1p1beta1/text_annotation.proto\x1a1google/cloud/vision/v1p1beta1/web_detection.proto\x1a\x17google/rpc/status.proto\x1a\x17google/type/color.proto\x1a\x18google/type/latlng.proto"\xe1\x02\n\x07Feature\x129\n\x04type\x18\x01 \x01(\x0e2+.google.cloud.vision.v1p1beta1.Feature.Type\x12\x13\n\x0bmax_results\x18\x02 \x01(\x05\x12\r\n\x05model\x18\x03 \x01(\t"\xf6\x01\n\x04Type\x12\x14\n\x10TYPE_UNSPECIFIED\x10\x00\x12\x12\n\x0eFACE_DETECTION\x10\x01\x12\x16\n\x12LANDMARK_DETECTION\x10\x02\x12\x12\n\x0eLOGO_DETECTION\x10\x03\x12\x13\n\x0fLABEL_DETECTION\x10\x04\x12\x12\n\x0eTEXT_DETECTION\x10\x05\x12\x1b\n\x17DOCUMENT_TEXT_DETECTION\x10\x0b\x12\x19\n\x15SAFE_SEARCH_DETECTION\x10\x06\x12\x14\n\x10IMAGE_PROPERTIES\x10\x07\x12\x0e\n\nCROP_HINTS\x10\t\x12\x11\n\rWEB_DETECTION\x10\n"7\n\x0bImageSource\x12\x15\n\rgcs_image_uri\x18\x01 \x01(\t\x12\x11\n\timage_uri\x18\x02 \x01(\t"T\n\x05Image\x12\x0f\n\x07content\x18\x01 \x01(\x0c\x12:\n\x06source\x18\x02 \x01(\x0b2*.google.cloud.vision.v1p1beta1.ImageSource"\x9b\x0e\n\x0eFaceAnnotation\x12B\n\rbounding_poly\x18\x01 \x01(\x0b2+.google.cloud.vision.v1p1beta1.BoundingPoly\x12E\n\x10fd_bounding_poly\x18\x02 \x01(\x0b2+.google.cloud.vision.v1p1beta1.BoundingPoly\x12I\n\tlandmarks\x18\x03 \x03(\x0b26.google.cloud.vision.v1p1beta1.FaceAnnotation.Landmark\x12\x12\n\nroll_angle\x18\x04 \x01(\x02\x12\x11\n\tpan_angle\x18\x05 \x01(\x02\x12\x12\n\ntilt_angle\x18\x06 \x01(\x02\x12\x1c\n\x14detection_confidence\x18\x07 \x01(\x02\x12\x1e\n\x16landmarking_confidence\x18\x08 \x01(\x02\x12A\n\x0ejoy_likelihood\x18\t \x01(\x0e2).google.cloud.vision.v1p1beta1.Likelihood\x12D\n\x11sorrow_likelihood\x18\n \x01(\x0e2).google.cloud.vision.v1p1beta1.Likelihood\x12C\n\x10anger_likelihood\x18\x0b \x01(\x0e2).google.cloud.vision.v1p1beta1.Likelihood\x12F\n\x13surprise_likelihood\x18\x0c \x01(\x0e2).google.cloud.vision.v1p1beta1.Likelihood\x12K\n\x18under_exposed_likelihood\x18\r \x01(\x0e2).google.cloud.vision.v1p1beta1.Likelihood\x12E\n\x12blurred_likelihood\x18\x0e \x01(\x0e2).google.cloud.vision.v1p1beta1.Likelihood\x12F\n\x13headwear_likelihood\x18\x0f \x01(\x0e2).google.cloud.vision.v1p1beta1.Likelihood\x1a\xc7\x07\n\x08Landmark\x12I\n\x04type\x18\x03 \x01(\x0e2;.google.cloud.vision.v1p1beta1.FaceAnnotation.Landmark.Type\x129\n\x08position\x18\x04 \x01(\x0b2\'.google.cloud.vision.v1p1beta1.Position"\xb4\x06\n\x04Type\x12\x14\n\x10UNKNOWN_LANDMARK\x10\x00\x12\x0c\n\x08LEFT_EYE\x10\x01\x12\r\n\tRIGHT_EYE\x10\x02\x12\x18\n\x14LEFT_OF_LEFT_EYEBROW\x10\x03\x12\x19\n\x15RIGHT_OF_LEFT_EYEBROW\x10\x04\x12\x19\n\x15LEFT_OF_RIGHT_EYEBROW\x10\x05\x12\x1a\n\x16RIGHT_OF_RIGHT_EYEBROW\x10\x06\x12\x19\n\x15MIDPOINT_BETWEEN_EYES\x10\x07\x12\x0c\n\x08NOSE_TIP\x10\x08\x12\r\n\tUPPER_LIP\x10\t\x12\r\n\tLOWER_LIP\x10\n\x12\x0e\n\nMOUTH_LEFT\x10\x0b\x12\x0f\n\x0bMOUTH_RIGHT\x10\x0c\x12\x10\n\x0cMOUTH_CENTER\x10\r\x12\x15\n\x11NOSE_BOTTOM_RIGHT\x10\x0e\x12\x14\n\x10NOSE_BOTTOM_LEFT\x10\x0f\x12\x16\n\x12NOSE_BOTTOM_CENTER\x10\x10\x12\x19\n\x15LEFT_EYE_TOP_BOUNDARY\x10\x11\x12\x19\n\x15LEFT_EYE_RIGHT_CORNER\x10\x12\x12\x1c\n\x18LEFT_EYE_BOTTOM_BOUNDARY\x10\x13\x12\x18\n\x14LEFT_EYE_LEFT_CORNER\x10\x14\x12\x1a\n\x16RIGHT_EYE_TOP_BOUNDARY\x10\x15\x12\x1a\n\x16RIGHT_EYE_RIGHT_CORNER\x10\x16\x12\x1d\n\x19RIGHT_EYE_BOTTOM_BOUNDARY\x10\x17\x12\x19\n\x15RIGHT_EYE_LEFT_CORNER\x10\x18\x12\x1f\n\x1bLEFT_EYEBROW_UPPER_MIDPOINT\x10\x19\x12 \n\x1cRIGHT_EYEBROW_UPPER_MIDPOINT\x10\x1a\x12\x14\n\x10LEFT_EAR_TRAGION\x10\x1b\x12\x15\n\x11RIGHT_EAR_TRAGION\x10\x1c\x12\x12\n\x0eLEFT_EYE_PUPIL\x10\x1d\x12\x13\n\x0fRIGHT_EYE_PUPIL\x10\x1e\x12\x15\n\x11FOREHEAD_GLABELLA\x10\x1f\x12\x11\n\rCHIN_GNATHION\x10 \x12\x14\n\x10CHIN_LEFT_GONION\x10!\x12\x15\n\x11CHIN_RIGHT_GONION\x10""4\n\x0cLocationInfo\x12$\n\x07lat_lng\x18\x01 \x01(\x0b2\x13.google.type.LatLng"=\n\x08Property\x12\x0c\n\x04name\x18\x01 \x01(\t\x12\r\n\x05value\x18\x02 \x01(\t\x12\x14\n\x0cuint64_value\x18\x03 \x01(\x04"\xbc\x02\n\x10EntityAnnotation\x12\x0b\n\x03mid\x18\x01 \x01(\t\x12\x0e\n\x06locale\x18\x02 \x01(\t\x12\x13\n\x0bdescription\x18\x03 \x01(\t\x12\r\n\x05score\x18\x04 \x01(\x02\x12\x12\n\nconfidence\x18\x05 \x01(\x02\x12\x12\n\ntopicality\x18\x06 \x01(\x02\x12B\n\rbounding_poly\x18\x07 \x01(\x0b2+.google.cloud.vision.v1p1beta1.BoundingPoly\x12>\n\tlocations\x18\x08 \x03(\x0b2+.google.cloud.vision.v1p1beta1.LocationInfo\x12;\n\nproperties\x18\t \x03(\x0b2\'.google.cloud.vision.v1p1beta1.Property"\xbc\x02\n\x14SafeSearchAnnotation\x128\n\x05adult\x18\x01 \x01(\x0e2).google.cloud.vision.v1p1beta1.Likelihood\x128\n\x05spoof\x18\x02 \x01(\x0e2).google.cloud.vision.v1p1beta1.Likelihood\x12:\n\x07medical\x18\x03 \x01(\x0e2).google.cloud.vision.v1p1beta1.Likelihood\x12;\n\x08violence\x18\x04 \x01(\x0e2).google.cloud.vision.v1p1beta1.Likelihood\x127\n\x04racy\x18\t \x01(\x0e2).google.cloud.vision.v1p1beta1.Likelihood"a\n\x0bLatLongRect\x12(\n\x0bmin_lat_lng\x18\x01 \x01(\x0b2\x13.google.type.LatLng\x12(\n\x0bmax_lat_lng\x18\x02 \x01(\x0b2\x13.google.type.LatLng"U\n\tColorInfo\x12!\n\x05color\x18\x01 \x01(\x0b2\x12.google.type.Color\x12\r\n\x05score\x18\x02 \x01(\x02\x12\x16\n\x0epixel_fraction\x18\x03 \x01(\x02"T\n\x18DominantColorsAnnotation\x128\n\x06colors\x18\x01 \x03(\x0b2(.google.cloud.vision.v1p1beta1.ColorInfo"c\n\x0fImageProperties\x12P\n\x0fdominant_colors\x18\x01 \x01(\x0b27.google.cloud.vision.v1p1beta1.DominantColorsAnnotation"\x7f\n\x08CropHint\x12B\n\rbounding_poly\x18\x01 \x01(\x0b2+.google.cloud.vision.v1p1beta1.BoundingPoly\x12\x12\n\nconfidence\x18\x02 \x01(\x02\x12\x1b\n\x13importance_fraction\x18\x03 \x01(\x02"R\n\x13CropHintsAnnotation\x12;\n\ncrop_hints\x18\x01 \x03(\x0b2\'.google.cloud.vision.v1p1beta1.CropHint"(\n\x0fCropHintsParams\x12\x15\n\raspect_ratios\x18\x01 \x03(\x02"1\n\x12WebDetectionParams\x12\x1b\n\x13include_geo_results\x18\x02 \x01(\x08"c\n\x13TextDetectionParams\x12.\n&enable_text_detection_confidence_score\x18\t \x01(\x08\x12\x1c\n\x14advanced_ocr_options\x18\x0b \x03(\t"\xd8\x02\n\x0cImageContext\x12A\n\rlat_long_rect\x18\x01 \x01(\x0b2*.google.cloud.vision.v1p1beta1.LatLongRect\x12\x16\n\x0elanguage_hints\x18\x02 \x03(\t\x12I\n\x11crop_hints_params\x18\x04 \x01(\x0b2..google.cloud.vision.v1p1beta1.CropHintsParams\x12O\n\x14web_detection_params\x18\x06 \x01(\x0b21.google.cloud.vision.v1p1beta1.WebDetectionParams\x12Q\n\x15text_detection_params\x18\x0c \x01(\x0b22.google.cloud.vision.v1p1beta1.TextDetectionParams"\xc9\x01\n\x14AnnotateImageRequest\x123\n\x05image\x18\x01 \x01(\x0b2$.google.cloud.vision.v1p1beta1.Image\x128\n\x08features\x18\x02 \x03(\x0b2&.google.cloud.vision.v1p1beta1.Feature\x12B\n\rimage_context\x18\x03 \x01(\x0b2+.google.cloud.vision.v1p1beta1.ImageContext"\xc2\x06\n\x15AnnotateImageResponse\x12G\n\x10face_annotations\x18\x01 \x03(\x0b2-.google.cloud.vision.v1p1beta1.FaceAnnotation\x12M\n\x14landmark_annotations\x18\x02 \x03(\x0b2/.google.cloud.vision.v1p1beta1.EntityAnnotation\x12I\n\x10logo_annotations\x18\x03 \x03(\x0b2/.google.cloud.vision.v1p1beta1.EntityAnnotation\x12J\n\x11label_annotations\x18\x04 \x03(\x0b2/.google.cloud.vision.v1p1beta1.EntityAnnotation\x12I\n\x10text_annotations\x18\x05 \x03(\x0b2/.google.cloud.vision.v1p1beta1.EntityAnnotation\x12K\n\x14full_text_annotation\x18\x0c \x01(\x0b2-.google.cloud.vision.v1p1beta1.TextAnnotation\x12S\n\x16safe_search_annotation\x18\x06 \x01(\x0b23.google.cloud.vision.v1p1beta1.SafeSearchAnnotation\x12S\n\x1bimage_properties_annotation\x18\x08 \x01(\x0b2..google.cloud.vision.v1p1beta1.ImageProperties\x12Q\n\x15crop_hints_annotation\x18\x0b \x01(\x0b22.google.cloud.vision.v1p1beta1.CropHintsAnnotation\x12B\n\rweb_detection\x18\r \x01(\x0b2+.google.cloud.vision.v1p1beta1.WebDetection\x12!\n\x05error\x18\t \x01(\x0b2\x12.google.rpc.Status"h\n\x1aBatchAnnotateImagesRequest\x12J\n\x08requests\x18\x01 \x03(\x0b23.google.cloud.vision.v1p1beta1.AnnotateImageRequestB\x03\xe0A\x02"f\n\x1bBatchAnnotateImagesResponse\x12G\n\tresponses\x18\x01 \x03(\x0b24.google.cloud.vision.v1p1beta1.AnnotateImageResponse*e\n\nLikelihood\x12\x0b\n\x07UNKNOWN\x10\x00\x12\x11\n\rVERY_UNLIKELY\x10\x01\x12\x0c\n\x08UNLIKELY\x10\x02\x12\x0c\n\x08POSSIBLE\x10\x03\x12\n\n\x06LIKELY\x10\x04\x12\x0f\n\x0bVERY_LIKELY\x10\x052\xc9\x02\n\x0eImageAnnotator\x12\xbe\x01\n\x13BatchAnnotateImages\x129.google.cloud.vision.v1p1beta1.BatchAnnotateImagesRequest\x1a:.google.cloud.vision.v1p1beta1.BatchAnnotateImagesResponse"0\xdaA\x08requests\x82\xd3\xe4\x93\x02\x1f"\x1a/v1p1beta1/images:annotate:\x01*\x1av\xcaA\x15vision.googleapis.com\xd2A[https://www.googleapis.com/auth/cloud-platform,https://www.googleapis.com/auth/cloud-visionB{\n!com.google.cloud.vision.v1p1beta1B\x13ImageAnnotatorProtoP\x01Z<cloud.google.com/go/vision/v2/apiv1p1beta1/visionpb;visionpb\xf8\x01\x01b\x06proto3')
_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'google.cloud.vision.v1p1beta1.image_annotator_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
    _globals['DESCRIPTOR']._loaded_options = None
    _globals['DESCRIPTOR']._serialized_options = b'\n!com.google.cloud.vision.v1p1beta1B\x13ImageAnnotatorProtoP\x01Z<cloud.google.com/go/vision/v2/apiv1p1beta1/visionpb;visionpb\xf8\x01\x01'
    _globals['_BATCHANNOTATEIMAGESREQUEST'].fields_by_name['requests']._loaded_options = None
    _globals['_BATCHANNOTATEIMAGESREQUEST'].fields_by_name['requests']._serialized_options = b'\xe0A\x02'
    _globals['_IMAGEANNOTATOR']._loaded_options = None
    _globals['_IMAGEANNOTATOR']._serialized_options = b'\xcaA\x15vision.googleapis.com\xd2A[https://www.googleapis.com/auth/cloud-platform,https://www.googleapis.com/auth/cloud-vision'
    _globals['_IMAGEANNOTATOR'].methods_by_name['BatchAnnotateImages']._loaded_options = None
    _globals['_IMAGEANNOTATOR'].methods_by_name['BatchAnnotateImages']._serialized_options = b'\xdaA\x08requests\x82\xd3\xe4\x93\x02\x1f"\x1a/v1p1beta1/images:annotate:\x01*'
    _globals['_LIKELIHOOD']._serialized_start = 5854
    _globals['_LIKELIHOOD']._serialized_end = 5955
    _globals['_FEATURE']._serialized_start = 401
    _globals['_FEATURE']._serialized_end = 754
    _globals['_FEATURE_TYPE']._serialized_start = 508
    _globals['_FEATURE_TYPE']._serialized_end = 754
    _globals['_IMAGESOURCE']._serialized_start = 756
    _globals['_IMAGESOURCE']._serialized_end = 811
    _globals['_IMAGE']._serialized_start = 813
    _globals['_IMAGE']._serialized_end = 897
    _globals['_FACEANNOTATION']._serialized_start = 900
    _globals['_FACEANNOTATION']._serialized_end = 2719
    _globals['_FACEANNOTATION_LANDMARK']._serialized_start = 1752
    _globals['_FACEANNOTATION_LANDMARK']._serialized_end = 2719
    _globals['_FACEANNOTATION_LANDMARK_TYPE']._serialized_start = 1899
    _globals['_FACEANNOTATION_LANDMARK_TYPE']._serialized_end = 2719
    _globals['_LOCATIONINFO']._serialized_start = 2721
    _globals['_LOCATIONINFO']._serialized_end = 2773
    _globals['_PROPERTY']._serialized_start = 2775
    _globals['_PROPERTY']._serialized_end = 2836
    _globals['_ENTITYANNOTATION']._serialized_start = 2839
    _globals['_ENTITYANNOTATION']._serialized_end = 3155
    _globals['_SAFESEARCHANNOTATION']._serialized_start = 3158
    _globals['_SAFESEARCHANNOTATION']._serialized_end = 3474
    _globals['_LATLONGRECT']._serialized_start = 3476
    _globals['_LATLONGRECT']._serialized_end = 3573
    _globals['_COLORINFO']._serialized_start = 3575
    _globals['_COLORINFO']._serialized_end = 3660
    _globals['_DOMINANTCOLORSANNOTATION']._serialized_start = 3662
    _globals['_DOMINANTCOLORSANNOTATION']._serialized_end = 3746
    _globals['_IMAGEPROPERTIES']._serialized_start = 3748
    _globals['_IMAGEPROPERTIES']._serialized_end = 3847
    _globals['_CROPHINT']._serialized_start = 3849
    _globals['_CROPHINT']._serialized_end = 3976
    _globals['_CROPHINTSANNOTATION']._serialized_start = 3978
    _globals['_CROPHINTSANNOTATION']._serialized_end = 4060
    _globals['_CROPHINTSPARAMS']._serialized_start = 4062
    _globals['_CROPHINTSPARAMS']._serialized_end = 4102
    _globals['_WEBDETECTIONPARAMS']._serialized_start = 4104
    _globals['_WEBDETECTIONPARAMS']._serialized_end = 4153
    _globals['_TEXTDETECTIONPARAMS']._serialized_start = 4155
    _globals['_TEXTDETECTIONPARAMS']._serialized_end = 4254
    _globals['_IMAGECONTEXT']._serialized_start = 4257
    _globals['_IMAGECONTEXT']._serialized_end = 4601
    _globals['_ANNOTATEIMAGEREQUEST']._serialized_start = 4604
    _globals['_ANNOTATEIMAGEREQUEST']._serialized_end = 4805
    _globals['_ANNOTATEIMAGERESPONSE']._serialized_start = 4808
    _globals['_ANNOTATEIMAGERESPONSE']._serialized_end = 5642
    _globals['_BATCHANNOTATEIMAGESREQUEST']._serialized_start = 5644
    _globals['_BATCHANNOTATEIMAGESREQUEST']._serialized_end = 5748
    _globals['_BATCHANNOTATEIMAGESRESPONSE']._serialized_start = 5750
    _globals['_BATCHANNOTATEIMAGESRESPONSE']._serialized_end = 5852
    _globals['_IMAGEANNOTATOR']._serialized_start = 5958
    _globals['_IMAGEANNOTATOR']._serialized_end = 6287