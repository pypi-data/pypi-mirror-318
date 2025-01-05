from google.api import field_behavior_pb2 as _field_behavior_pb2
from google.api import resource_pb2 as _resource_pb2
from google.cloud.talent.v4beta1 import common_pb2 as _common_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union
DESCRIPTOR: _descriptor.FileDescriptor

class Company(_message.Message):
    __slots__ = ('name', 'display_name', 'external_id', 'size', 'headquarters_address', 'hiring_agency', 'eeo_text', 'website_uri', 'career_site_uri', 'image_uri', 'keyword_searchable_job_custom_attributes', 'derived_info', 'suspended')

    class DerivedInfo(_message.Message):
        __slots__ = ('headquarters_location',)
        HEADQUARTERS_LOCATION_FIELD_NUMBER: _ClassVar[int]
        headquarters_location: _common_pb2.Location

        def __init__(self, headquarters_location: _Optional[_Union[_common_pb2.Location, _Mapping]]=...) -> None:
            ...
    NAME_FIELD_NUMBER: _ClassVar[int]
    DISPLAY_NAME_FIELD_NUMBER: _ClassVar[int]
    EXTERNAL_ID_FIELD_NUMBER: _ClassVar[int]
    SIZE_FIELD_NUMBER: _ClassVar[int]
    HEADQUARTERS_ADDRESS_FIELD_NUMBER: _ClassVar[int]
    HIRING_AGENCY_FIELD_NUMBER: _ClassVar[int]
    EEO_TEXT_FIELD_NUMBER: _ClassVar[int]
    WEBSITE_URI_FIELD_NUMBER: _ClassVar[int]
    CAREER_SITE_URI_FIELD_NUMBER: _ClassVar[int]
    IMAGE_URI_FIELD_NUMBER: _ClassVar[int]
    KEYWORD_SEARCHABLE_JOB_CUSTOM_ATTRIBUTES_FIELD_NUMBER: _ClassVar[int]
    DERIVED_INFO_FIELD_NUMBER: _ClassVar[int]
    SUSPENDED_FIELD_NUMBER: _ClassVar[int]
    name: str
    display_name: str
    external_id: str
    size: _common_pb2.CompanySize
    headquarters_address: str
    hiring_agency: bool
    eeo_text: str
    website_uri: str
    career_site_uri: str
    image_uri: str
    keyword_searchable_job_custom_attributes: _containers.RepeatedScalarFieldContainer[str]
    derived_info: Company.DerivedInfo
    suspended: bool

    def __init__(self, name: _Optional[str]=..., display_name: _Optional[str]=..., external_id: _Optional[str]=..., size: _Optional[_Union[_common_pb2.CompanySize, str]]=..., headquarters_address: _Optional[str]=..., hiring_agency: bool=..., eeo_text: _Optional[str]=..., website_uri: _Optional[str]=..., career_site_uri: _Optional[str]=..., image_uri: _Optional[str]=..., keyword_searchable_job_custom_attributes: _Optional[_Iterable[str]]=..., derived_info: _Optional[_Union[Company.DerivedInfo, _Mapping]]=..., suspended: bool=...) -> None:
        ...