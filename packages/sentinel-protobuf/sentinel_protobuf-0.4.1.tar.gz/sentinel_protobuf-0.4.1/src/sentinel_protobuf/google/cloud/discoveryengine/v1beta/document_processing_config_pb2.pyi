from google.api import field_behavior_pb2 as _field_behavior_pb2
from google.api import resource_pb2 as _resource_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union
DESCRIPTOR: _descriptor.FileDescriptor

class DocumentProcessingConfig(_message.Message):
    __slots__ = ('name', 'chunking_config', 'default_parsing_config', 'parsing_config_overrides')

    class ChunkingConfig(_message.Message):
        __slots__ = ('layout_based_chunking_config',)

        class LayoutBasedChunkingConfig(_message.Message):
            __slots__ = ('chunk_size', 'include_ancestor_headings')
            CHUNK_SIZE_FIELD_NUMBER: _ClassVar[int]
            INCLUDE_ANCESTOR_HEADINGS_FIELD_NUMBER: _ClassVar[int]
            chunk_size: int
            include_ancestor_headings: bool

            def __init__(self, chunk_size: _Optional[int]=..., include_ancestor_headings: bool=...) -> None:
                ...
        LAYOUT_BASED_CHUNKING_CONFIG_FIELD_NUMBER: _ClassVar[int]
        layout_based_chunking_config: DocumentProcessingConfig.ChunkingConfig.LayoutBasedChunkingConfig

        def __init__(self, layout_based_chunking_config: _Optional[_Union[DocumentProcessingConfig.ChunkingConfig.LayoutBasedChunkingConfig, _Mapping]]=...) -> None:
            ...

    class ParsingConfig(_message.Message):
        __slots__ = ('digital_parsing_config', 'ocr_parsing_config', 'layout_parsing_config')

        class DigitalParsingConfig(_message.Message):
            __slots__ = ()

            def __init__(self) -> None:
                ...

        class OcrParsingConfig(_message.Message):
            __slots__ = ('enhanced_document_elements', 'use_native_text')
            ENHANCED_DOCUMENT_ELEMENTS_FIELD_NUMBER: _ClassVar[int]
            USE_NATIVE_TEXT_FIELD_NUMBER: _ClassVar[int]
            enhanced_document_elements: _containers.RepeatedScalarFieldContainer[str]
            use_native_text: bool

            def __init__(self, enhanced_document_elements: _Optional[_Iterable[str]]=..., use_native_text: bool=...) -> None:
                ...

        class LayoutParsingConfig(_message.Message):
            __slots__ = ()

            def __init__(self) -> None:
                ...
        DIGITAL_PARSING_CONFIG_FIELD_NUMBER: _ClassVar[int]
        OCR_PARSING_CONFIG_FIELD_NUMBER: _ClassVar[int]
        LAYOUT_PARSING_CONFIG_FIELD_NUMBER: _ClassVar[int]
        digital_parsing_config: DocumentProcessingConfig.ParsingConfig.DigitalParsingConfig
        ocr_parsing_config: DocumentProcessingConfig.ParsingConfig.OcrParsingConfig
        layout_parsing_config: DocumentProcessingConfig.ParsingConfig.LayoutParsingConfig

        def __init__(self, digital_parsing_config: _Optional[_Union[DocumentProcessingConfig.ParsingConfig.DigitalParsingConfig, _Mapping]]=..., ocr_parsing_config: _Optional[_Union[DocumentProcessingConfig.ParsingConfig.OcrParsingConfig, _Mapping]]=..., layout_parsing_config: _Optional[_Union[DocumentProcessingConfig.ParsingConfig.LayoutParsingConfig, _Mapping]]=...) -> None:
            ...

    class ParsingConfigOverridesEntry(_message.Message):
        __slots__ = ('key', 'value')
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: DocumentProcessingConfig.ParsingConfig

        def __init__(self, key: _Optional[str]=..., value: _Optional[_Union[DocumentProcessingConfig.ParsingConfig, _Mapping]]=...) -> None:
            ...
    NAME_FIELD_NUMBER: _ClassVar[int]
    CHUNKING_CONFIG_FIELD_NUMBER: _ClassVar[int]
    DEFAULT_PARSING_CONFIG_FIELD_NUMBER: _ClassVar[int]
    PARSING_CONFIG_OVERRIDES_FIELD_NUMBER: _ClassVar[int]
    name: str
    chunking_config: DocumentProcessingConfig.ChunkingConfig
    default_parsing_config: DocumentProcessingConfig.ParsingConfig
    parsing_config_overrides: _containers.MessageMap[str, DocumentProcessingConfig.ParsingConfig]

    def __init__(self, name: _Optional[str]=..., chunking_config: _Optional[_Union[DocumentProcessingConfig.ChunkingConfig, _Mapping]]=..., default_parsing_config: _Optional[_Union[DocumentProcessingConfig.ParsingConfig, _Mapping]]=..., parsing_config_overrides: _Optional[_Mapping[str, DocumentProcessingConfig.ParsingConfig]]=...) -> None:
        ...