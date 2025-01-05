from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Mapping as _Mapping, Optional as _Optional, Union as _Union
DESCRIPTOR: _descriptor.FileDescriptor

class QueryDriveActivityRequest(_message.Message):
    __slots__ = ('item_name', 'ancestor_name', 'consolidation_strategy', 'page_size', 'page_token', 'filter')
    ITEM_NAME_FIELD_NUMBER: _ClassVar[int]
    ANCESTOR_NAME_FIELD_NUMBER: _ClassVar[int]
    CONSOLIDATION_STRATEGY_FIELD_NUMBER: _ClassVar[int]
    PAGE_SIZE_FIELD_NUMBER: _ClassVar[int]
    PAGE_TOKEN_FIELD_NUMBER: _ClassVar[int]
    FILTER_FIELD_NUMBER: _ClassVar[int]
    item_name: str
    ancestor_name: str
    consolidation_strategy: ConsolidationStrategy
    page_size: int
    page_token: str
    filter: str

    def __init__(self, item_name: _Optional[str]=..., ancestor_name: _Optional[str]=..., consolidation_strategy: _Optional[_Union[ConsolidationStrategy, _Mapping]]=..., page_size: _Optional[int]=..., page_token: _Optional[str]=..., filter: _Optional[str]=...) -> None:
        ...

class ConsolidationStrategy(_message.Message):
    __slots__ = ('none', 'legacy')

    class NoConsolidation(_message.Message):
        __slots__ = ()

        def __init__(self) -> None:
            ...

    class Legacy(_message.Message):
        __slots__ = ()

        def __init__(self) -> None:
            ...
    NONE_FIELD_NUMBER: _ClassVar[int]
    LEGACY_FIELD_NUMBER: _ClassVar[int]
    none: ConsolidationStrategy.NoConsolidation
    legacy: ConsolidationStrategy.Legacy

    def __init__(self, none: _Optional[_Union[ConsolidationStrategy.NoConsolidation, _Mapping]]=..., legacy: _Optional[_Union[ConsolidationStrategy.Legacy, _Mapping]]=...) -> None:
        ...