from google.api import annotations_pb2 as _annotations_pb2
from google.api import client_pb2 as _client_pb2
from google.api import field_behavior_pb2 as _field_behavior_pb2
from google.api import resource_pb2 as _resource_pb2
from google.iam.v1 import iam_policy_pb2 as _iam_policy_pb2
from google.iam.v1 import policy_pb2 as _policy_pb2
from google.protobuf import empty_pb2 as _empty_pb2
from google.protobuf import field_mask_pb2 as _field_mask_pb2
from google.protobuf import wrappers_pb2 as _wrappers_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union
DESCRIPTOR: _descriptor.FileDescriptor

class DataExchange(_message.Message):
    __slots__ = ('name', 'display_name', 'description', 'primary_contact', 'documentation', 'listing_count', 'icon')
    NAME_FIELD_NUMBER: _ClassVar[int]
    DISPLAY_NAME_FIELD_NUMBER: _ClassVar[int]
    DESCRIPTION_FIELD_NUMBER: _ClassVar[int]
    PRIMARY_CONTACT_FIELD_NUMBER: _ClassVar[int]
    DOCUMENTATION_FIELD_NUMBER: _ClassVar[int]
    LISTING_COUNT_FIELD_NUMBER: _ClassVar[int]
    ICON_FIELD_NUMBER: _ClassVar[int]
    name: str
    display_name: str
    description: str
    primary_contact: str
    documentation: str
    listing_count: int
    icon: bytes

    def __init__(self, name: _Optional[str]=..., display_name: _Optional[str]=..., description: _Optional[str]=..., primary_contact: _Optional[str]=..., documentation: _Optional[str]=..., listing_count: _Optional[int]=..., icon: _Optional[bytes]=...) -> None:
        ...

class DataProvider(_message.Message):
    __slots__ = ('name', 'primary_contact')
    NAME_FIELD_NUMBER: _ClassVar[int]
    PRIMARY_CONTACT_FIELD_NUMBER: _ClassVar[int]
    name: str
    primary_contact: str

    def __init__(self, name: _Optional[str]=..., primary_contact: _Optional[str]=...) -> None:
        ...

class Publisher(_message.Message):
    __slots__ = ('name', 'primary_contact')
    NAME_FIELD_NUMBER: _ClassVar[int]
    PRIMARY_CONTACT_FIELD_NUMBER: _ClassVar[int]
    name: str
    primary_contact: str

    def __init__(self, name: _Optional[str]=..., primary_contact: _Optional[str]=...) -> None:
        ...

class DestinationDatasetReference(_message.Message):
    __slots__ = ('dataset_id', 'project_id')
    DATASET_ID_FIELD_NUMBER: _ClassVar[int]
    PROJECT_ID_FIELD_NUMBER: _ClassVar[int]
    dataset_id: str
    project_id: str

    def __init__(self, dataset_id: _Optional[str]=..., project_id: _Optional[str]=...) -> None:
        ...

class DestinationDataset(_message.Message):
    __slots__ = ('dataset_reference', 'friendly_name', 'description', 'labels', 'location')

    class LabelsEntry(_message.Message):
        __slots__ = ('key', 'value')
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: str

        def __init__(self, key: _Optional[str]=..., value: _Optional[str]=...) -> None:
            ...
    DATASET_REFERENCE_FIELD_NUMBER: _ClassVar[int]
    FRIENDLY_NAME_FIELD_NUMBER: _ClassVar[int]
    DESCRIPTION_FIELD_NUMBER: _ClassVar[int]
    LABELS_FIELD_NUMBER: _ClassVar[int]
    LOCATION_FIELD_NUMBER: _ClassVar[int]
    dataset_reference: DestinationDatasetReference
    friendly_name: _wrappers_pb2.StringValue
    description: _wrappers_pb2.StringValue
    labels: _containers.ScalarMap[str, str]
    location: str

    def __init__(self, dataset_reference: _Optional[_Union[DestinationDatasetReference, _Mapping]]=..., friendly_name: _Optional[_Union[_wrappers_pb2.StringValue, _Mapping]]=..., description: _Optional[_Union[_wrappers_pb2.StringValue, _Mapping]]=..., labels: _Optional[_Mapping[str, str]]=..., location: _Optional[str]=...) -> None:
        ...

class Listing(_message.Message):
    __slots__ = ('bigquery_dataset', 'name', 'display_name', 'description', 'primary_contact', 'documentation', 'state', 'icon', 'data_provider', 'categories', 'publisher', 'request_access')

    class State(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        STATE_UNSPECIFIED: _ClassVar[Listing.State]
        ACTIVE: _ClassVar[Listing.State]
    STATE_UNSPECIFIED: Listing.State
    ACTIVE: Listing.State

    class Category(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        CATEGORY_UNSPECIFIED: _ClassVar[Listing.Category]
        CATEGORY_OTHERS: _ClassVar[Listing.Category]
        CATEGORY_ADVERTISING_AND_MARKETING: _ClassVar[Listing.Category]
        CATEGORY_COMMERCE: _ClassVar[Listing.Category]
        CATEGORY_CLIMATE_AND_ENVIRONMENT: _ClassVar[Listing.Category]
        CATEGORY_DEMOGRAPHICS: _ClassVar[Listing.Category]
        CATEGORY_ECONOMICS: _ClassVar[Listing.Category]
        CATEGORY_EDUCATION: _ClassVar[Listing.Category]
        CATEGORY_ENERGY: _ClassVar[Listing.Category]
        CATEGORY_FINANCIAL: _ClassVar[Listing.Category]
        CATEGORY_GAMING: _ClassVar[Listing.Category]
        CATEGORY_GEOSPATIAL: _ClassVar[Listing.Category]
        CATEGORY_HEALTHCARE_AND_LIFE_SCIENCE: _ClassVar[Listing.Category]
        CATEGORY_MEDIA: _ClassVar[Listing.Category]
        CATEGORY_PUBLIC_SECTOR: _ClassVar[Listing.Category]
        CATEGORY_RETAIL: _ClassVar[Listing.Category]
        CATEGORY_SPORTS: _ClassVar[Listing.Category]
        CATEGORY_SCIENCE_AND_RESEARCH: _ClassVar[Listing.Category]
        CATEGORY_TRANSPORTATION_AND_LOGISTICS: _ClassVar[Listing.Category]
        CATEGORY_TRAVEL_AND_TOURISM: _ClassVar[Listing.Category]
    CATEGORY_UNSPECIFIED: Listing.Category
    CATEGORY_OTHERS: Listing.Category
    CATEGORY_ADVERTISING_AND_MARKETING: Listing.Category
    CATEGORY_COMMERCE: Listing.Category
    CATEGORY_CLIMATE_AND_ENVIRONMENT: Listing.Category
    CATEGORY_DEMOGRAPHICS: Listing.Category
    CATEGORY_ECONOMICS: Listing.Category
    CATEGORY_EDUCATION: Listing.Category
    CATEGORY_ENERGY: Listing.Category
    CATEGORY_FINANCIAL: Listing.Category
    CATEGORY_GAMING: Listing.Category
    CATEGORY_GEOSPATIAL: Listing.Category
    CATEGORY_HEALTHCARE_AND_LIFE_SCIENCE: Listing.Category
    CATEGORY_MEDIA: Listing.Category
    CATEGORY_PUBLIC_SECTOR: Listing.Category
    CATEGORY_RETAIL: Listing.Category
    CATEGORY_SPORTS: Listing.Category
    CATEGORY_SCIENCE_AND_RESEARCH: Listing.Category
    CATEGORY_TRANSPORTATION_AND_LOGISTICS: Listing.Category
    CATEGORY_TRAVEL_AND_TOURISM: Listing.Category

    class BigQueryDatasetSource(_message.Message):
        __slots__ = ('dataset',)
        DATASET_FIELD_NUMBER: _ClassVar[int]
        dataset: str

        def __init__(self, dataset: _Optional[str]=...) -> None:
            ...
    BIGQUERY_DATASET_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    DISPLAY_NAME_FIELD_NUMBER: _ClassVar[int]
    DESCRIPTION_FIELD_NUMBER: _ClassVar[int]
    PRIMARY_CONTACT_FIELD_NUMBER: _ClassVar[int]
    DOCUMENTATION_FIELD_NUMBER: _ClassVar[int]
    STATE_FIELD_NUMBER: _ClassVar[int]
    ICON_FIELD_NUMBER: _ClassVar[int]
    DATA_PROVIDER_FIELD_NUMBER: _ClassVar[int]
    CATEGORIES_FIELD_NUMBER: _ClassVar[int]
    PUBLISHER_FIELD_NUMBER: _ClassVar[int]
    REQUEST_ACCESS_FIELD_NUMBER: _ClassVar[int]
    bigquery_dataset: Listing.BigQueryDatasetSource
    name: str
    display_name: str
    description: str
    primary_contact: str
    documentation: str
    state: Listing.State
    icon: bytes
    data_provider: DataProvider
    categories: _containers.RepeatedScalarFieldContainer[Listing.Category]
    publisher: Publisher
    request_access: str

    def __init__(self, bigquery_dataset: _Optional[_Union[Listing.BigQueryDatasetSource, _Mapping]]=..., name: _Optional[str]=..., display_name: _Optional[str]=..., description: _Optional[str]=..., primary_contact: _Optional[str]=..., documentation: _Optional[str]=..., state: _Optional[_Union[Listing.State, str]]=..., icon: _Optional[bytes]=..., data_provider: _Optional[_Union[DataProvider, _Mapping]]=..., categories: _Optional[_Iterable[_Union[Listing.Category, str]]]=..., publisher: _Optional[_Union[Publisher, _Mapping]]=..., request_access: _Optional[str]=...) -> None:
        ...

class ListDataExchangesRequest(_message.Message):
    __slots__ = ('parent', 'page_size', 'page_token')
    PARENT_FIELD_NUMBER: _ClassVar[int]
    PAGE_SIZE_FIELD_NUMBER: _ClassVar[int]
    PAGE_TOKEN_FIELD_NUMBER: _ClassVar[int]
    parent: str
    page_size: int
    page_token: str

    def __init__(self, parent: _Optional[str]=..., page_size: _Optional[int]=..., page_token: _Optional[str]=...) -> None:
        ...

class ListDataExchangesResponse(_message.Message):
    __slots__ = ('data_exchanges', 'next_page_token')
    DATA_EXCHANGES_FIELD_NUMBER: _ClassVar[int]
    NEXT_PAGE_TOKEN_FIELD_NUMBER: _ClassVar[int]
    data_exchanges: _containers.RepeatedCompositeFieldContainer[DataExchange]
    next_page_token: str

    def __init__(self, data_exchanges: _Optional[_Iterable[_Union[DataExchange, _Mapping]]]=..., next_page_token: _Optional[str]=...) -> None:
        ...

class ListOrgDataExchangesRequest(_message.Message):
    __slots__ = ('organization', 'page_size', 'page_token')
    ORGANIZATION_FIELD_NUMBER: _ClassVar[int]
    PAGE_SIZE_FIELD_NUMBER: _ClassVar[int]
    PAGE_TOKEN_FIELD_NUMBER: _ClassVar[int]
    organization: str
    page_size: int
    page_token: str

    def __init__(self, organization: _Optional[str]=..., page_size: _Optional[int]=..., page_token: _Optional[str]=...) -> None:
        ...

class ListOrgDataExchangesResponse(_message.Message):
    __slots__ = ('data_exchanges', 'next_page_token')
    DATA_EXCHANGES_FIELD_NUMBER: _ClassVar[int]
    NEXT_PAGE_TOKEN_FIELD_NUMBER: _ClassVar[int]
    data_exchanges: _containers.RepeatedCompositeFieldContainer[DataExchange]
    next_page_token: str

    def __init__(self, data_exchanges: _Optional[_Iterable[_Union[DataExchange, _Mapping]]]=..., next_page_token: _Optional[str]=...) -> None:
        ...

class GetDataExchangeRequest(_message.Message):
    __slots__ = ('name',)
    NAME_FIELD_NUMBER: _ClassVar[int]
    name: str

    def __init__(self, name: _Optional[str]=...) -> None:
        ...

class CreateDataExchangeRequest(_message.Message):
    __slots__ = ('parent', 'data_exchange_id', 'data_exchange')
    PARENT_FIELD_NUMBER: _ClassVar[int]
    DATA_EXCHANGE_ID_FIELD_NUMBER: _ClassVar[int]
    DATA_EXCHANGE_FIELD_NUMBER: _ClassVar[int]
    parent: str
    data_exchange_id: str
    data_exchange: DataExchange

    def __init__(self, parent: _Optional[str]=..., data_exchange_id: _Optional[str]=..., data_exchange: _Optional[_Union[DataExchange, _Mapping]]=...) -> None:
        ...

class UpdateDataExchangeRequest(_message.Message):
    __slots__ = ('update_mask', 'data_exchange')
    UPDATE_MASK_FIELD_NUMBER: _ClassVar[int]
    DATA_EXCHANGE_FIELD_NUMBER: _ClassVar[int]
    update_mask: _field_mask_pb2.FieldMask
    data_exchange: DataExchange

    def __init__(self, update_mask: _Optional[_Union[_field_mask_pb2.FieldMask, _Mapping]]=..., data_exchange: _Optional[_Union[DataExchange, _Mapping]]=...) -> None:
        ...

class DeleteDataExchangeRequest(_message.Message):
    __slots__ = ('name',)
    NAME_FIELD_NUMBER: _ClassVar[int]
    name: str

    def __init__(self, name: _Optional[str]=...) -> None:
        ...

class ListListingsRequest(_message.Message):
    __slots__ = ('parent', 'page_size', 'page_token')
    PARENT_FIELD_NUMBER: _ClassVar[int]
    PAGE_SIZE_FIELD_NUMBER: _ClassVar[int]
    PAGE_TOKEN_FIELD_NUMBER: _ClassVar[int]
    parent: str
    page_size: int
    page_token: str

    def __init__(self, parent: _Optional[str]=..., page_size: _Optional[int]=..., page_token: _Optional[str]=...) -> None:
        ...

class ListListingsResponse(_message.Message):
    __slots__ = ('listings', 'next_page_token')
    LISTINGS_FIELD_NUMBER: _ClassVar[int]
    NEXT_PAGE_TOKEN_FIELD_NUMBER: _ClassVar[int]
    listings: _containers.RepeatedCompositeFieldContainer[Listing]
    next_page_token: str

    def __init__(self, listings: _Optional[_Iterable[_Union[Listing, _Mapping]]]=..., next_page_token: _Optional[str]=...) -> None:
        ...

class GetListingRequest(_message.Message):
    __slots__ = ('name',)
    NAME_FIELD_NUMBER: _ClassVar[int]
    name: str

    def __init__(self, name: _Optional[str]=...) -> None:
        ...

class CreateListingRequest(_message.Message):
    __slots__ = ('parent', 'listing_id', 'listing')
    PARENT_FIELD_NUMBER: _ClassVar[int]
    LISTING_ID_FIELD_NUMBER: _ClassVar[int]
    LISTING_FIELD_NUMBER: _ClassVar[int]
    parent: str
    listing_id: str
    listing: Listing

    def __init__(self, parent: _Optional[str]=..., listing_id: _Optional[str]=..., listing: _Optional[_Union[Listing, _Mapping]]=...) -> None:
        ...

class UpdateListingRequest(_message.Message):
    __slots__ = ('update_mask', 'listing')
    UPDATE_MASK_FIELD_NUMBER: _ClassVar[int]
    LISTING_FIELD_NUMBER: _ClassVar[int]
    update_mask: _field_mask_pb2.FieldMask
    listing: Listing

    def __init__(self, update_mask: _Optional[_Union[_field_mask_pb2.FieldMask, _Mapping]]=..., listing: _Optional[_Union[Listing, _Mapping]]=...) -> None:
        ...

class DeleteListingRequest(_message.Message):
    __slots__ = ('name',)
    NAME_FIELD_NUMBER: _ClassVar[int]
    name: str

    def __init__(self, name: _Optional[str]=...) -> None:
        ...

class SubscribeListingRequest(_message.Message):
    __slots__ = ('destination_dataset', 'name')
    DESTINATION_DATASET_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    destination_dataset: DestinationDataset
    name: str

    def __init__(self, destination_dataset: _Optional[_Union[DestinationDataset, _Mapping]]=..., name: _Optional[str]=...) -> None:
        ...

class SubscribeListingResponse(_message.Message):
    __slots__ = ()

    def __init__(self) -> None:
        ...