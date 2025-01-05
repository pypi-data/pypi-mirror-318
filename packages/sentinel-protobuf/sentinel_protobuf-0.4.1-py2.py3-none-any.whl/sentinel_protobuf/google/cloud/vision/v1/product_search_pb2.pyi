from google.api import resource_pb2 as _resource_pb2
from google.cloud.vision.v1 import geometry_pb2 as _geometry_pb2
from google.cloud.vision.v1 import product_search_service_pb2 as _product_search_service_pb2
from google.protobuf import timestamp_pb2 as _timestamp_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union
DESCRIPTOR: _descriptor.FileDescriptor

class ProductSearchParams(_message.Message):
    __slots__ = ('bounding_poly', 'product_set', 'product_categories', 'filter')
    BOUNDING_POLY_FIELD_NUMBER: _ClassVar[int]
    PRODUCT_SET_FIELD_NUMBER: _ClassVar[int]
    PRODUCT_CATEGORIES_FIELD_NUMBER: _ClassVar[int]
    FILTER_FIELD_NUMBER: _ClassVar[int]
    bounding_poly: _geometry_pb2.BoundingPoly
    product_set: str
    product_categories: _containers.RepeatedScalarFieldContainer[str]
    filter: str

    def __init__(self, bounding_poly: _Optional[_Union[_geometry_pb2.BoundingPoly, _Mapping]]=..., product_set: _Optional[str]=..., product_categories: _Optional[_Iterable[str]]=..., filter: _Optional[str]=...) -> None:
        ...

class ProductSearchResults(_message.Message):
    __slots__ = ('index_time', 'results', 'product_grouped_results')

    class Result(_message.Message):
        __slots__ = ('product', 'score', 'image')
        PRODUCT_FIELD_NUMBER: _ClassVar[int]
        SCORE_FIELD_NUMBER: _ClassVar[int]
        IMAGE_FIELD_NUMBER: _ClassVar[int]
        product: _product_search_service_pb2.Product
        score: float
        image: str

        def __init__(self, product: _Optional[_Union[_product_search_service_pb2.Product, _Mapping]]=..., score: _Optional[float]=..., image: _Optional[str]=...) -> None:
            ...

    class ObjectAnnotation(_message.Message):
        __slots__ = ('mid', 'language_code', 'name', 'score')
        MID_FIELD_NUMBER: _ClassVar[int]
        LANGUAGE_CODE_FIELD_NUMBER: _ClassVar[int]
        NAME_FIELD_NUMBER: _ClassVar[int]
        SCORE_FIELD_NUMBER: _ClassVar[int]
        mid: str
        language_code: str
        name: str
        score: float

        def __init__(self, mid: _Optional[str]=..., language_code: _Optional[str]=..., name: _Optional[str]=..., score: _Optional[float]=...) -> None:
            ...

    class GroupedResult(_message.Message):
        __slots__ = ('bounding_poly', 'results', 'object_annotations')
        BOUNDING_POLY_FIELD_NUMBER: _ClassVar[int]
        RESULTS_FIELD_NUMBER: _ClassVar[int]
        OBJECT_ANNOTATIONS_FIELD_NUMBER: _ClassVar[int]
        bounding_poly: _geometry_pb2.BoundingPoly
        results: _containers.RepeatedCompositeFieldContainer[ProductSearchResults.Result]
        object_annotations: _containers.RepeatedCompositeFieldContainer[ProductSearchResults.ObjectAnnotation]

        def __init__(self, bounding_poly: _Optional[_Union[_geometry_pb2.BoundingPoly, _Mapping]]=..., results: _Optional[_Iterable[_Union[ProductSearchResults.Result, _Mapping]]]=..., object_annotations: _Optional[_Iterable[_Union[ProductSearchResults.ObjectAnnotation, _Mapping]]]=...) -> None:
            ...
    INDEX_TIME_FIELD_NUMBER: _ClassVar[int]
    RESULTS_FIELD_NUMBER: _ClassVar[int]
    PRODUCT_GROUPED_RESULTS_FIELD_NUMBER: _ClassVar[int]
    index_time: _timestamp_pb2.Timestamp
    results: _containers.RepeatedCompositeFieldContainer[ProductSearchResults.Result]
    product_grouped_results: _containers.RepeatedCompositeFieldContainer[ProductSearchResults.GroupedResult]

    def __init__(self, index_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]]=..., results: _Optional[_Iterable[_Union[ProductSearchResults.Result, _Mapping]]]=..., product_grouped_results: _Optional[_Iterable[_Union[ProductSearchResults.GroupedResult, _Mapping]]]=...) -> None:
        ...