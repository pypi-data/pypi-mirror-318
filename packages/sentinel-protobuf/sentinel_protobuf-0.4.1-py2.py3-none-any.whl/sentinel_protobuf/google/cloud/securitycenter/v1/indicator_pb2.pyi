from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union
DESCRIPTOR: _descriptor.FileDescriptor

class Indicator(_message.Message):
    __slots__ = ('ip_addresses', 'domains', 'signatures', 'uris')

    class ProcessSignature(_message.Message):
        __slots__ = ('memory_hash_signature', 'yara_rule_signature', 'signature_type')

        class SignatureType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
            __slots__ = ()
            SIGNATURE_TYPE_UNSPECIFIED: _ClassVar[Indicator.ProcessSignature.SignatureType]
            SIGNATURE_TYPE_PROCESS: _ClassVar[Indicator.ProcessSignature.SignatureType]
            SIGNATURE_TYPE_FILE: _ClassVar[Indicator.ProcessSignature.SignatureType]
        SIGNATURE_TYPE_UNSPECIFIED: Indicator.ProcessSignature.SignatureType
        SIGNATURE_TYPE_PROCESS: Indicator.ProcessSignature.SignatureType
        SIGNATURE_TYPE_FILE: Indicator.ProcessSignature.SignatureType

        class MemoryHashSignature(_message.Message):
            __slots__ = ('binary_family', 'detections')

            class Detection(_message.Message):
                __slots__ = ('binary', 'percent_pages_matched')
                BINARY_FIELD_NUMBER: _ClassVar[int]
                PERCENT_PAGES_MATCHED_FIELD_NUMBER: _ClassVar[int]
                binary: str
                percent_pages_matched: float

                def __init__(self, binary: _Optional[str]=..., percent_pages_matched: _Optional[float]=...) -> None:
                    ...
            BINARY_FAMILY_FIELD_NUMBER: _ClassVar[int]
            DETECTIONS_FIELD_NUMBER: _ClassVar[int]
            binary_family: str
            detections: _containers.RepeatedCompositeFieldContainer[Indicator.ProcessSignature.MemoryHashSignature.Detection]

            def __init__(self, binary_family: _Optional[str]=..., detections: _Optional[_Iterable[_Union[Indicator.ProcessSignature.MemoryHashSignature.Detection, _Mapping]]]=...) -> None:
                ...

        class YaraRuleSignature(_message.Message):
            __slots__ = ('yara_rule',)
            YARA_RULE_FIELD_NUMBER: _ClassVar[int]
            yara_rule: str

            def __init__(self, yara_rule: _Optional[str]=...) -> None:
                ...
        MEMORY_HASH_SIGNATURE_FIELD_NUMBER: _ClassVar[int]
        YARA_RULE_SIGNATURE_FIELD_NUMBER: _ClassVar[int]
        SIGNATURE_TYPE_FIELD_NUMBER: _ClassVar[int]
        memory_hash_signature: Indicator.ProcessSignature.MemoryHashSignature
        yara_rule_signature: Indicator.ProcessSignature.YaraRuleSignature
        signature_type: Indicator.ProcessSignature.SignatureType

        def __init__(self, memory_hash_signature: _Optional[_Union[Indicator.ProcessSignature.MemoryHashSignature, _Mapping]]=..., yara_rule_signature: _Optional[_Union[Indicator.ProcessSignature.YaraRuleSignature, _Mapping]]=..., signature_type: _Optional[_Union[Indicator.ProcessSignature.SignatureType, str]]=...) -> None:
            ...
    IP_ADDRESSES_FIELD_NUMBER: _ClassVar[int]
    DOMAINS_FIELD_NUMBER: _ClassVar[int]
    SIGNATURES_FIELD_NUMBER: _ClassVar[int]
    URIS_FIELD_NUMBER: _ClassVar[int]
    ip_addresses: _containers.RepeatedScalarFieldContainer[str]
    domains: _containers.RepeatedScalarFieldContainer[str]
    signatures: _containers.RepeatedCompositeFieldContainer[Indicator.ProcessSignature]
    uris: _containers.RepeatedScalarFieldContainer[str]

    def __init__(self, ip_addresses: _Optional[_Iterable[str]]=..., domains: _Optional[_Iterable[str]]=..., signatures: _Optional[_Iterable[_Union[Indicator.ProcessSignature, _Mapping]]]=..., uris: _Optional[_Iterable[str]]=...) -> None:
        ...