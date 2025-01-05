from google.api import annotations_pb2 as _annotations_pb2
from google.api import client_pb2 as _client_pb2
from google.api import field_behavior_pb2 as _field_behavior_pb2
from google.api import resource_pb2 as _resource_pb2
from google.protobuf import empty_pb2 as _empty_pb2
from google.protobuf import field_mask_pb2 as _field_mask_pb2
from google.protobuf import wrappers_pb2 as _wrappers_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class GetRegionRequest(_message.Message):
    __slots__ = ("name",)
    NAME_FIELD_NUMBER: _ClassVar[int]
    name: str
    def __init__(self, name: _Optional[str] = ...) -> None: ...

class CreateRegionRequest(_message.Message):
    __slots__ = ("parent", "region_id", "region")
    PARENT_FIELD_NUMBER: _ClassVar[int]
    REGION_ID_FIELD_NUMBER: _ClassVar[int]
    REGION_FIELD_NUMBER: _ClassVar[int]
    parent: str
    region_id: str
    region: Region
    def __init__(self, parent: _Optional[str] = ..., region_id: _Optional[str] = ..., region: _Optional[_Union[Region, _Mapping]] = ...) -> None: ...

class UpdateRegionRequest(_message.Message):
    __slots__ = ("region", "update_mask")
    REGION_FIELD_NUMBER: _ClassVar[int]
    UPDATE_MASK_FIELD_NUMBER: _ClassVar[int]
    region: Region
    update_mask: _field_mask_pb2.FieldMask
    def __init__(self, region: _Optional[_Union[Region, _Mapping]] = ..., update_mask: _Optional[_Union[_field_mask_pb2.FieldMask, _Mapping]] = ...) -> None: ...

class DeleteRegionRequest(_message.Message):
    __slots__ = ("name",)
    NAME_FIELD_NUMBER: _ClassVar[int]
    name: str
    def __init__(self, name: _Optional[str] = ...) -> None: ...

class ListRegionsRequest(_message.Message):
    __slots__ = ("parent", "page_size", "page_token")
    PARENT_FIELD_NUMBER: _ClassVar[int]
    PAGE_SIZE_FIELD_NUMBER: _ClassVar[int]
    PAGE_TOKEN_FIELD_NUMBER: _ClassVar[int]
    parent: str
    page_size: int
    page_token: str
    def __init__(self, parent: _Optional[str] = ..., page_size: _Optional[int] = ..., page_token: _Optional[str] = ...) -> None: ...

class ListRegionsResponse(_message.Message):
    __slots__ = ("regions", "next_page_token")
    REGIONS_FIELD_NUMBER: _ClassVar[int]
    NEXT_PAGE_TOKEN_FIELD_NUMBER: _ClassVar[int]
    regions: _containers.RepeatedCompositeFieldContainer[Region]
    next_page_token: str
    def __init__(self, regions: _Optional[_Iterable[_Union[Region, _Mapping]]] = ..., next_page_token: _Optional[str] = ...) -> None: ...

class Region(_message.Message):
    __slots__ = ("name", "display_name", "postal_code_area", "geotarget_area", "regional_inventory_eligible", "shipping_eligible")
    class PostalCodeArea(_message.Message):
        __slots__ = ("region_code", "postal_codes")
        class PostalCodeRange(_message.Message):
            __slots__ = ("begin", "end")
            BEGIN_FIELD_NUMBER: _ClassVar[int]
            END_FIELD_NUMBER: _ClassVar[int]
            begin: str
            end: str
            def __init__(self, begin: _Optional[str] = ..., end: _Optional[str] = ...) -> None: ...
        REGION_CODE_FIELD_NUMBER: _ClassVar[int]
        POSTAL_CODES_FIELD_NUMBER: _ClassVar[int]
        region_code: str
        postal_codes: _containers.RepeatedCompositeFieldContainer[Region.PostalCodeArea.PostalCodeRange]
        def __init__(self, region_code: _Optional[str] = ..., postal_codes: _Optional[_Iterable[_Union[Region.PostalCodeArea.PostalCodeRange, _Mapping]]] = ...) -> None: ...
    class GeoTargetArea(_message.Message):
        __slots__ = ("geotarget_criteria_ids",)
        GEOTARGET_CRITERIA_IDS_FIELD_NUMBER: _ClassVar[int]
        geotarget_criteria_ids: _containers.RepeatedScalarFieldContainer[int]
        def __init__(self, geotarget_criteria_ids: _Optional[_Iterable[int]] = ...) -> None: ...
    NAME_FIELD_NUMBER: _ClassVar[int]
    DISPLAY_NAME_FIELD_NUMBER: _ClassVar[int]
    POSTAL_CODE_AREA_FIELD_NUMBER: _ClassVar[int]
    GEOTARGET_AREA_FIELD_NUMBER: _ClassVar[int]
    REGIONAL_INVENTORY_ELIGIBLE_FIELD_NUMBER: _ClassVar[int]
    SHIPPING_ELIGIBLE_FIELD_NUMBER: _ClassVar[int]
    name: str
    display_name: str
    postal_code_area: Region.PostalCodeArea
    geotarget_area: Region.GeoTargetArea
    regional_inventory_eligible: _wrappers_pb2.BoolValue
    shipping_eligible: _wrappers_pb2.BoolValue
    def __init__(self, name: _Optional[str] = ..., display_name: _Optional[str] = ..., postal_code_area: _Optional[_Union[Region.PostalCodeArea, _Mapping]] = ..., geotarget_area: _Optional[_Union[Region.GeoTargetArea, _Mapping]] = ..., regional_inventory_eligible: _Optional[_Union[_wrappers_pb2.BoolValue, _Mapping]] = ..., shipping_eligible: _Optional[_Union[_wrappers_pb2.BoolValue, _Mapping]] = ...) -> None: ...
