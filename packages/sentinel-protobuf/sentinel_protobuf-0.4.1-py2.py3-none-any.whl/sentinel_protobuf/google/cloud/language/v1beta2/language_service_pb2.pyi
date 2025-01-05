from google.api import annotations_pb2 as _annotations_pb2
from google.api import client_pb2 as _client_pb2
from google.api import field_behavior_pb2 as _field_behavior_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union
DESCRIPTOR: _descriptor.FileDescriptor

class EncodingType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    NONE: _ClassVar[EncodingType]
    UTF8: _ClassVar[EncodingType]
    UTF16: _ClassVar[EncodingType]
    UTF32: _ClassVar[EncodingType]
NONE: EncodingType
UTF8: EncodingType
UTF16: EncodingType
UTF32: EncodingType

class Document(_message.Message):
    __slots__ = ('type', 'content', 'gcs_content_uri', 'language', 'reference_web_uri', 'boilerplate_handling')

    class Type(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        TYPE_UNSPECIFIED: _ClassVar[Document.Type]
        PLAIN_TEXT: _ClassVar[Document.Type]
        HTML: _ClassVar[Document.Type]
    TYPE_UNSPECIFIED: Document.Type
    PLAIN_TEXT: Document.Type
    HTML: Document.Type

    class BoilerplateHandling(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        BOILERPLATE_HANDLING_UNSPECIFIED: _ClassVar[Document.BoilerplateHandling]
        SKIP_BOILERPLATE: _ClassVar[Document.BoilerplateHandling]
        KEEP_BOILERPLATE: _ClassVar[Document.BoilerplateHandling]
    BOILERPLATE_HANDLING_UNSPECIFIED: Document.BoilerplateHandling
    SKIP_BOILERPLATE: Document.BoilerplateHandling
    KEEP_BOILERPLATE: Document.BoilerplateHandling
    TYPE_FIELD_NUMBER: _ClassVar[int]
    CONTENT_FIELD_NUMBER: _ClassVar[int]
    GCS_CONTENT_URI_FIELD_NUMBER: _ClassVar[int]
    LANGUAGE_FIELD_NUMBER: _ClassVar[int]
    REFERENCE_WEB_URI_FIELD_NUMBER: _ClassVar[int]
    BOILERPLATE_HANDLING_FIELD_NUMBER: _ClassVar[int]
    type: Document.Type
    content: str
    gcs_content_uri: str
    language: str
    reference_web_uri: str
    boilerplate_handling: Document.BoilerplateHandling

    def __init__(self, type: _Optional[_Union[Document.Type, str]]=..., content: _Optional[str]=..., gcs_content_uri: _Optional[str]=..., language: _Optional[str]=..., reference_web_uri: _Optional[str]=..., boilerplate_handling: _Optional[_Union[Document.BoilerplateHandling, str]]=...) -> None:
        ...

class Sentence(_message.Message):
    __slots__ = ('text', 'sentiment')
    TEXT_FIELD_NUMBER: _ClassVar[int]
    SENTIMENT_FIELD_NUMBER: _ClassVar[int]
    text: TextSpan
    sentiment: Sentiment

    def __init__(self, text: _Optional[_Union[TextSpan, _Mapping]]=..., sentiment: _Optional[_Union[Sentiment, _Mapping]]=...) -> None:
        ...

class Entity(_message.Message):
    __slots__ = ('name', 'type', 'metadata', 'salience', 'mentions', 'sentiment')

    class Type(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        UNKNOWN: _ClassVar[Entity.Type]
        PERSON: _ClassVar[Entity.Type]
        LOCATION: _ClassVar[Entity.Type]
        ORGANIZATION: _ClassVar[Entity.Type]
        EVENT: _ClassVar[Entity.Type]
        WORK_OF_ART: _ClassVar[Entity.Type]
        CONSUMER_GOOD: _ClassVar[Entity.Type]
        OTHER: _ClassVar[Entity.Type]
        PHONE_NUMBER: _ClassVar[Entity.Type]
        ADDRESS: _ClassVar[Entity.Type]
        DATE: _ClassVar[Entity.Type]
        NUMBER: _ClassVar[Entity.Type]
        PRICE: _ClassVar[Entity.Type]
    UNKNOWN: Entity.Type
    PERSON: Entity.Type
    LOCATION: Entity.Type
    ORGANIZATION: Entity.Type
    EVENT: Entity.Type
    WORK_OF_ART: Entity.Type
    CONSUMER_GOOD: Entity.Type
    OTHER: Entity.Type
    PHONE_NUMBER: Entity.Type
    ADDRESS: Entity.Type
    DATE: Entity.Type
    NUMBER: Entity.Type
    PRICE: Entity.Type

    class MetadataEntry(_message.Message):
        __slots__ = ('key', 'value')
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: str

        def __init__(self, key: _Optional[str]=..., value: _Optional[str]=...) -> None:
            ...
    NAME_FIELD_NUMBER: _ClassVar[int]
    TYPE_FIELD_NUMBER: _ClassVar[int]
    METADATA_FIELD_NUMBER: _ClassVar[int]
    SALIENCE_FIELD_NUMBER: _ClassVar[int]
    MENTIONS_FIELD_NUMBER: _ClassVar[int]
    SENTIMENT_FIELD_NUMBER: _ClassVar[int]
    name: str
    type: Entity.Type
    metadata: _containers.ScalarMap[str, str]
    salience: float
    mentions: _containers.RepeatedCompositeFieldContainer[EntityMention]
    sentiment: Sentiment

    def __init__(self, name: _Optional[str]=..., type: _Optional[_Union[Entity.Type, str]]=..., metadata: _Optional[_Mapping[str, str]]=..., salience: _Optional[float]=..., mentions: _Optional[_Iterable[_Union[EntityMention, _Mapping]]]=..., sentiment: _Optional[_Union[Sentiment, _Mapping]]=...) -> None:
        ...

class Token(_message.Message):
    __slots__ = ('text', 'part_of_speech', 'dependency_edge', 'lemma')
    TEXT_FIELD_NUMBER: _ClassVar[int]
    PART_OF_SPEECH_FIELD_NUMBER: _ClassVar[int]
    DEPENDENCY_EDGE_FIELD_NUMBER: _ClassVar[int]
    LEMMA_FIELD_NUMBER: _ClassVar[int]
    text: TextSpan
    part_of_speech: PartOfSpeech
    dependency_edge: DependencyEdge
    lemma: str

    def __init__(self, text: _Optional[_Union[TextSpan, _Mapping]]=..., part_of_speech: _Optional[_Union[PartOfSpeech, _Mapping]]=..., dependency_edge: _Optional[_Union[DependencyEdge, _Mapping]]=..., lemma: _Optional[str]=...) -> None:
        ...

class Sentiment(_message.Message):
    __slots__ = ('magnitude', 'score')
    MAGNITUDE_FIELD_NUMBER: _ClassVar[int]
    SCORE_FIELD_NUMBER: _ClassVar[int]
    magnitude: float
    score: float

    def __init__(self, magnitude: _Optional[float]=..., score: _Optional[float]=...) -> None:
        ...

class PartOfSpeech(_message.Message):
    __slots__ = ('tag', 'aspect', 'case', 'form', 'gender', 'mood', 'number', 'person', 'proper', 'reciprocity', 'tense', 'voice')

    class Tag(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        UNKNOWN: _ClassVar[PartOfSpeech.Tag]
        ADJ: _ClassVar[PartOfSpeech.Tag]
        ADP: _ClassVar[PartOfSpeech.Tag]
        ADV: _ClassVar[PartOfSpeech.Tag]
        CONJ: _ClassVar[PartOfSpeech.Tag]
        DET: _ClassVar[PartOfSpeech.Tag]
        NOUN: _ClassVar[PartOfSpeech.Tag]
        NUM: _ClassVar[PartOfSpeech.Tag]
        PRON: _ClassVar[PartOfSpeech.Tag]
        PRT: _ClassVar[PartOfSpeech.Tag]
        PUNCT: _ClassVar[PartOfSpeech.Tag]
        VERB: _ClassVar[PartOfSpeech.Tag]
        X: _ClassVar[PartOfSpeech.Tag]
        AFFIX: _ClassVar[PartOfSpeech.Tag]
    UNKNOWN: PartOfSpeech.Tag
    ADJ: PartOfSpeech.Tag
    ADP: PartOfSpeech.Tag
    ADV: PartOfSpeech.Tag
    CONJ: PartOfSpeech.Tag
    DET: PartOfSpeech.Tag
    NOUN: PartOfSpeech.Tag
    NUM: PartOfSpeech.Tag
    PRON: PartOfSpeech.Tag
    PRT: PartOfSpeech.Tag
    PUNCT: PartOfSpeech.Tag
    VERB: PartOfSpeech.Tag
    X: PartOfSpeech.Tag
    AFFIX: PartOfSpeech.Tag

    class Aspect(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        ASPECT_UNKNOWN: _ClassVar[PartOfSpeech.Aspect]
        PERFECTIVE: _ClassVar[PartOfSpeech.Aspect]
        IMPERFECTIVE: _ClassVar[PartOfSpeech.Aspect]
        PROGRESSIVE: _ClassVar[PartOfSpeech.Aspect]
    ASPECT_UNKNOWN: PartOfSpeech.Aspect
    PERFECTIVE: PartOfSpeech.Aspect
    IMPERFECTIVE: PartOfSpeech.Aspect
    PROGRESSIVE: PartOfSpeech.Aspect

    class Case(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        CASE_UNKNOWN: _ClassVar[PartOfSpeech.Case]
        ACCUSATIVE: _ClassVar[PartOfSpeech.Case]
        ADVERBIAL: _ClassVar[PartOfSpeech.Case]
        COMPLEMENTIVE: _ClassVar[PartOfSpeech.Case]
        DATIVE: _ClassVar[PartOfSpeech.Case]
        GENITIVE: _ClassVar[PartOfSpeech.Case]
        INSTRUMENTAL: _ClassVar[PartOfSpeech.Case]
        LOCATIVE: _ClassVar[PartOfSpeech.Case]
        NOMINATIVE: _ClassVar[PartOfSpeech.Case]
        OBLIQUE: _ClassVar[PartOfSpeech.Case]
        PARTITIVE: _ClassVar[PartOfSpeech.Case]
        PREPOSITIONAL: _ClassVar[PartOfSpeech.Case]
        REFLEXIVE_CASE: _ClassVar[PartOfSpeech.Case]
        RELATIVE_CASE: _ClassVar[PartOfSpeech.Case]
        VOCATIVE: _ClassVar[PartOfSpeech.Case]
    CASE_UNKNOWN: PartOfSpeech.Case
    ACCUSATIVE: PartOfSpeech.Case
    ADVERBIAL: PartOfSpeech.Case
    COMPLEMENTIVE: PartOfSpeech.Case
    DATIVE: PartOfSpeech.Case
    GENITIVE: PartOfSpeech.Case
    INSTRUMENTAL: PartOfSpeech.Case
    LOCATIVE: PartOfSpeech.Case
    NOMINATIVE: PartOfSpeech.Case
    OBLIQUE: PartOfSpeech.Case
    PARTITIVE: PartOfSpeech.Case
    PREPOSITIONAL: PartOfSpeech.Case
    REFLEXIVE_CASE: PartOfSpeech.Case
    RELATIVE_CASE: PartOfSpeech.Case
    VOCATIVE: PartOfSpeech.Case

    class Form(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        FORM_UNKNOWN: _ClassVar[PartOfSpeech.Form]
        ADNOMIAL: _ClassVar[PartOfSpeech.Form]
        AUXILIARY: _ClassVar[PartOfSpeech.Form]
        COMPLEMENTIZER: _ClassVar[PartOfSpeech.Form]
        FINAL_ENDING: _ClassVar[PartOfSpeech.Form]
        GERUND: _ClassVar[PartOfSpeech.Form]
        REALIS: _ClassVar[PartOfSpeech.Form]
        IRREALIS: _ClassVar[PartOfSpeech.Form]
        SHORT: _ClassVar[PartOfSpeech.Form]
        LONG: _ClassVar[PartOfSpeech.Form]
        ORDER: _ClassVar[PartOfSpeech.Form]
        SPECIFIC: _ClassVar[PartOfSpeech.Form]
    FORM_UNKNOWN: PartOfSpeech.Form
    ADNOMIAL: PartOfSpeech.Form
    AUXILIARY: PartOfSpeech.Form
    COMPLEMENTIZER: PartOfSpeech.Form
    FINAL_ENDING: PartOfSpeech.Form
    GERUND: PartOfSpeech.Form
    REALIS: PartOfSpeech.Form
    IRREALIS: PartOfSpeech.Form
    SHORT: PartOfSpeech.Form
    LONG: PartOfSpeech.Form
    ORDER: PartOfSpeech.Form
    SPECIFIC: PartOfSpeech.Form

    class Gender(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        GENDER_UNKNOWN: _ClassVar[PartOfSpeech.Gender]
        FEMININE: _ClassVar[PartOfSpeech.Gender]
        MASCULINE: _ClassVar[PartOfSpeech.Gender]
        NEUTER: _ClassVar[PartOfSpeech.Gender]
    GENDER_UNKNOWN: PartOfSpeech.Gender
    FEMININE: PartOfSpeech.Gender
    MASCULINE: PartOfSpeech.Gender
    NEUTER: PartOfSpeech.Gender

    class Mood(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        MOOD_UNKNOWN: _ClassVar[PartOfSpeech.Mood]
        CONDITIONAL_MOOD: _ClassVar[PartOfSpeech.Mood]
        IMPERATIVE: _ClassVar[PartOfSpeech.Mood]
        INDICATIVE: _ClassVar[PartOfSpeech.Mood]
        INTERROGATIVE: _ClassVar[PartOfSpeech.Mood]
        JUSSIVE: _ClassVar[PartOfSpeech.Mood]
        SUBJUNCTIVE: _ClassVar[PartOfSpeech.Mood]
    MOOD_UNKNOWN: PartOfSpeech.Mood
    CONDITIONAL_MOOD: PartOfSpeech.Mood
    IMPERATIVE: PartOfSpeech.Mood
    INDICATIVE: PartOfSpeech.Mood
    INTERROGATIVE: PartOfSpeech.Mood
    JUSSIVE: PartOfSpeech.Mood
    SUBJUNCTIVE: PartOfSpeech.Mood

    class Number(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        NUMBER_UNKNOWN: _ClassVar[PartOfSpeech.Number]
        SINGULAR: _ClassVar[PartOfSpeech.Number]
        PLURAL: _ClassVar[PartOfSpeech.Number]
        DUAL: _ClassVar[PartOfSpeech.Number]
    NUMBER_UNKNOWN: PartOfSpeech.Number
    SINGULAR: PartOfSpeech.Number
    PLURAL: PartOfSpeech.Number
    DUAL: PartOfSpeech.Number

    class Person(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        PERSON_UNKNOWN: _ClassVar[PartOfSpeech.Person]
        FIRST: _ClassVar[PartOfSpeech.Person]
        SECOND: _ClassVar[PartOfSpeech.Person]
        THIRD: _ClassVar[PartOfSpeech.Person]
        REFLEXIVE_PERSON: _ClassVar[PartOfSpeech.Person]
    PERSON_UNKNOWN: PartOfSpeech.Person
    FIRST: PartOfSpeech.Person
    SECOND: PartOfSpeech.Person
    THIRD: PartOfSpeech.Person
    REFLEXIVE_PERSON: PartOfSpeech.Person

    class Proper(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        PROPER_UNKNOWN: _ClassVar[PartOfSpeech.Proper]
        PROPER: _ClassVar[PartOfSpeech.Proper]
        NOT_PROPER: _ClassVar[PartOfSpeech.Proper]
    PROPER_UNKNOWN: PartOfSpeech.Proper
    PROPER: PartOfSpeech.Proper
    NOT_PROPER: PartOfSpeech.Proper

    class Reciprocity(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        RECIPROCITY_UNKNOWN: _ClassVar[PartOfSpeech.Reciprocity]
        RECIPROCAL: _ClassVar[PartOfSpeech.Reciprocity]
        NON_RECIPROCAL: _ClassVar[PartOfSpeech.Reciprocity]
    RECIPROCITY_UNKNOWN: PartOfSpeech.Reciprocity
    RECIPROCAL: PartOfSpeech.Reciprocity
    NON_RECIPROCAL: PartOfSpeech.Reciprocity

    class Tense(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        TENSE_UNKNOWN: _ClassVar[PartOfSpeech.Tense]
        CONDITIONAL_TENSE: _ClassVar[PartOfSpeech.Tense]
        FUTURE: _ClassVar[PartOfSpeech.Tense]
        PAST: _ClassVar[PartOfSpeech.Tense]
        PRESENT: _ClassVar[PartOfSpeech.Tense]
        IMPERFECT: _ClassVar[PartOfSpeech.Tense]
        PLUPERFECT: _ClassVar[PartOfSpeech.Tense]
    TENSE_UNKNOWN: PartOfSpeech.Tense
    CONDITIONAL_TENSE: PartOfSpeech.Tense
    FUTURE: PartOfSpeech.Tense
    PAST: PartOfSpeech.Tense
    PRESENT: PartOfSpeech.Tense
    IMPERFECT: PartOfSpeech.Tense
    PLUPERFECT: PartOfSpeech.Tense

    class Voice(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        VOICE_UNKNOWN: _ClassVar[PartOfSpeech.Voice]
        ACTIVE: _ClassVar[PartOfSpeech.Voice]
        CAUSATIVE: _ClassVar[PartOfSpeech.Voice]
        PASSIVE: _ClassVar[PartOfSpeech.Voice]
    VOICE_UNKNOWN: PartOfSpeech.Voice
    ACTIVE: PartOfSpeech.Voice
    CAUSATIVE: PartOfSpeech.Voice
    PASSIVE: PartOfSpeech.Voice
    TAG_FIELD_NUMBER: _ClassVar[int]
    ASPECT_FIELD_NUMBER: _ClassVar[int]
    CASE_FIELD_NUMBER: _ClassVar[int]
    FORM_FIELD_NUMBER: _ClassVar[int]
    GENDER_FIELD_NUMBER: _ClassVar[int]
    MOOD_FIELD_NUMBER: _ClassVar[int]
    NUMBER_FIELD_NUMBER: _ClassVar[int]
    PERSON_FIELD_NUMBER: _ClassVar[int]
    PROPER_FIELD_NUMBER: _ClassVar[int]
    RECIPROCITY_FIELD_NUMBER: _ClassVar[int]
    TENSE_FIELD_NUMBER: _ClassVar[int]
    VOICE_FIELD_NUMBER: _ClassVar[int]
    tag: PartOfSpeech.Tag
    aspect: PartOfSpeech.Aspect
    case: PartOfSpeech.Case
    form: PartOfSpeech.Form
    gender: PartOfSpeech.Gender
    mood: PartOfSpeech.Mood
    number: PartOfSpeech.Number
    person: PartOfSpeech.Person
    proper: PartOfSpeech.Proper
    reciprocity: PartOfSpeech.Reciprocity
    tense: PartOfSpeech.Tense
    voice: PartOfSpeech.Voice

    def __init__(self, tag: _Optional[_Union[PartOfSpeech.Tag, str]]=..., aspect: _Optional[_Union[PartOfSpeech.Aspect, str]]=..., case: _Optional[_Union[PartOfSpeech.Case, str]]=..., form: _Optional[_Union[PartOfSpeech.Form, str]]=..., gender: _Optional[_Union[PartOfSpeech.Gender, str]]=..., mood: _Optional[_Union[PartOfSpeech.Mood, str]]=..., number: _Optional[_Union[PartOfSpeech.Number, str]]=..., person: _Optional[_Union[PartOfSpeech.Person, str]]=..., proper: _Optional[_Union[PartOfSpeech.Proper, str]]=..., reciprocity: _Optional[_Union[PartOfSpeech.Reciprocity, str]]=..., tense: _Optional[_Union[PartOfSpeech.Tense, str]]=..., voice: _Optional[_Union[PartOfSpeech.Voice, str]]=...) -> None:
        ...

class DependencyEdge(_message.Message):
    __slots__ = ('head_token_index', 'label')

    class Label(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        UNKNOWN: _ClassVar[DependencyEdge.Label]
        ABBREV: _ClassVar[DependencyEdge.Label]
        ACOMP: _ClassVar[DependencyEdge.Label]
        ADVCL: _ClassVar[DependencyEdge.Label]
        ADVMOD: _ClassVar[DependencyEdge.Label]
        AMOD: _ClassVar[DependencyEdge.Label]
        APPOS: _ClassVar[DependencyEdge.Label]
        ATTR: _ClassVar[DependencyEdge.Label]
        AUX: _ClassVar[DependencyEdge.Label]
        AUXPASS: _ClassVar[DependencyEdge.Label]
        CC: _ClassVar[DependencyEdge.Label]
        CCOMP: _ClassVar[DependencyEdge.Label]
        CONJ: _ClassVar[DependencyEdge.Label]
        CSUBJ: _ClassVar[DependencyEdge.Label]
        CSUBJPASS: _ClassVar[DependencyEdge.Label]
        DEP: _ClassVar[DependencyEdge.Label]
        DET: _ClassVar[DependencyEdge.Label]
        DISCOURSE: _ClassVar[DependencyEdge.Label]
        DOBJ: _ClassVar[DependencyEdge.Label]
        EXPL: _ClassVar[DependencyEdge.Label]
        GOESWITH: _ClassVar[DependencyEdge.Label]
        IOBJ: _ClassVar[DependencyEdge.Label]
        MARK: _ClassVar[DependencyEdge.Label]
        MWE: _ClassVar[DependencyEdge.Label]
        MWV: _ClassVar[DependencyEdge.Label]
        NEG: _ClassVar[DependencyEdge.Label]
        NN: _ClassVar[DependencyEdge.Label]
        NPADVMOD: _ClassVar[DependencyEdge.Label]
        NSUBJ: _ClassVar[DependencyEdge.Label]
        NSUBJPASS: _ClassVar[DependencyEdge.Label]
        NUM: _ClassVar[DependencyEdge.Label]
        NUMBER: _ClassVar[DependencyEdge.Label]
        P: _ClassVar[DependencyEdge.Label]
        PARATAXIS: _ClassVar[DependencyEdge.Label]
        PARTMOD: _ClassVar[DependencyEdge.Label]
        PCOMP: _ClassVar[DependencyEdge.Label]
        POBJ: _ClassVar[DependencyEdge.Label]
        POSS: _ClassVar[DependencyEdge.Label]
        POSTNEG: _ClassVar[DependencyEdge.Label]
        PRECOMP: _ClassVar[DependencyEdge.Label]
        PRECONJ: _ClassVar[DependencyEdge.Label]
        PREDET: _ClassVar[DependencyEdge.Label]
        PREF: _ClassVar[DependencyEdge.Label]
        PREP: _ClassVar[DependencyEdge.Label]
        PRONL: _ClassVar[DependencyEdge.Label]
        PRT: _ClassVar[DependencyEdge.Label]
        PS: _ClassVar[DependencyEdge.Label]
        QUANTMOD: _ClassVar[DependencyEdge.Label]
        RCMOD: _ClassVar[DependencyEdge.Label]
        RCMODREL: _ClassVar[DependencyEdge.Label]
        RDROP: _ClassVar[DependencyEdge.Label]
        REF: _ClassVar[DependencyEdge.Label]
        REMNANT: _ClassVar[DependencyEdge.Label]
        REPARANDUM: _ClassVar[DependencyEdge.Label]
        ROOT: _ClassVar[DependencyEdge.Label]
        SNUM: _ClassVar[DependencyEdge.Label]
        SUFF: _ClassVar[DependencyEdge.Label]
        TMOD: _ClassVar[DependencyEdge.Label]
        TOPIC: _ClassVar[DependencyEdge.Label]
        VMOD: _ClassVar[DependencyEdge.Label]
        VOCATIVE: _ClassVar[DependencyEdge.Label]
        XCOMP: _ClassVar[DependencyEdge.Label]
        SUFFIX: _ClassVar[DependencyEdge.Label]
        TITLE: _ClassVar[DependencyEdge.Label]
        ADVPHMOD: _ClassVar[DependencyEdge.Label]
        AUXCAUS: _ClassVar[DependencyEdge.Label]
        AUXVV: _ClassVar[DependencyEdge.Label]
        DTMOD: _ClassVar[DependencyEdge.Label]
        FOREIGN: _ClassVar[DependencyEdge.Label]
        KW: _ClassVar[DependencyEdge.Label]
        LIST: _ClassVar[DependencyEdge.Label]
        NOMC: _ClassVar[DependencyEdge.Label]
        NOMCSUBJ: _ClassVar[DependencyEdge.Label]
        NOMCSUBJPASS: _ClassVar[DependencyEdge.Label]
        NUMC: _ClassVar[DependencyEdge.Label]
        COP: _ClassVar[DependencyEdge.Label]
        DISLOCATED: _ClassVar[DependencyEdge.Label]
        ASP: _ClassVar[DependencyEdge.Label]
        GMOD: _ClassVar[DependencyEdge.Label]
        GOBJ: _ClassVar[DependencyEdge.Label]
        INFMOD: _ClassVar[DependencyEdge.Label]
        MES: _ClassVar[DependencyEdge.Label]
        NCOMP: _ClassVar[DependencyEdge.Label]
    UNKNOWN: DependencyEdge.Label
    ABBREV: DependencyEdge.Label
    ACOMP: DependencyEdge.Label
    ADVCL: DependencyEdge.Label
    ADVMOD: DependencyEdge.Label
    AMOD: DependencyEdge.Label
    APPOS: DependencyEdge.Label
    ATTR: DependencyEdge.Label
    AUX: DependencyEdge.Label
    AUXPASS: DependencyEdge.Label
    CC: DependencyEdge.Label
    CCOMP: DependencyEdge.Label
    CONJ: DependencyEdge.Label
    CSUBJ: DependencyEdge.Label
    CSUBJPASS: DependencyEdge.Label
    DEP: DependencyEdge.Label
    DET: DependencyEdge.Label
    DISCOURSE: DependencyEdge.Label
    DOBJ: DependencyEdge.Label
    EXPL: DependencyEdge.Label
    GOESWITH: DependencyEdge.Label
    IOBJ: DependencyEdge.Label
    MARK: DependencyEdge.Label
    MWE: DependencyEdge.Label
    MWV: DependencyEdge.Label
    NEG: DependencyEdge.Label
    NN: DependencyEdge.Label
    NPADVMOD: DependencyEdge.Label
    NSUBJ: DependencyEdge.Label
    NSUBJPASS: DependencyEdge.Label
    NUM: DependencyEdge.Label
    NUMBER: DependencyEdge.Label
    P: DependencyEdge.Label
    PARATAXIS: DependencyEdge.Label
    PARTMOD: DependencyEdge.Label
    PCOMP: DependencyEdge.Label
    POBJ: DependencyEdge.Label
    POSS: DependencyEdge.Label
    POSTNEG: DependencyEdge.Label
    PRECOMP: DependencyEdge.Label
    PRECONJ: DependencyEdge.Label
    PREDET: DependencyEdge.Label
    PREF: DependencyEdge.Label
    PREP: DependencyEdge.Label
    PRONL: DependencyEdge.Label
    PRT: DependencyEdge.Label
    PS: DependencyEdge.Label
    QUANTMOD: DependencyEdge.Label
    RCMOD: DependencyEdge.Label
    RCMODREL: DependencyEdge.Label
    RDROP: DependencyEdge.Label
    REF: DependencyEdge.Label
    REMNANT: DependencyEdge.Label
    REPARANDUM: DependencyEdge.Label
    ROOT: DependencyEdge.Label
    SNUM: DependencyEdge.Label
    SUFF: DependencyEdge.Label
    TMOD: DependencyEdge.Label
    TOPIC: DependencyEdge.Label
    VMOD: DependencyEdge.Label
    VOCATIVE: DependencyEdge.Label
    XCOMP: DependencyEdge.Label
    SUFFIX: DependencyEdge.Label
    TITLE: DependencyEdge.Label
    ADVPHMOD: DependencyEdge.Label
    AUXCAUS: DependencyEdge.Label
    AUXVV: DependencyEdge.Label
    DTMOD: DependencyEdge.Label
    FOREIGN: DependencyEdge.Label
    KW: DependencyEdge.Label
    LIST: DependencyEdge.Label
    NOMC: DependencyEdge.Label
    NOMCSUBJ: DependencyEdge.Label
    NOMCSUBJPASS: DependencyEdge.Label
    NUMC: DependencyEdge.Label
    COP: DependencyEdge.Label
    DISLOCATED: DependencyEdge.Label
    ASP: DependencyEdge.Label
    GMOD: DependencyEdge.Label
    GOBJ: DependencyEdge.Label
    INFMOD: DependencyEdge.Label
    MES: DependencyEdge.Label
    NCOMP: DependencyEdge.Label
    HEAD_TOKEN_INDEX_FIELD_NUMBER: _ClassVar[int]
    LABEL_FIELD_NUMBER: _ClassVar[int]
    head_token_index: int
    label: DependencyEdge.Label

    def __init__(self, head_token_index: _Optional[int]=..., label: _Optional[_Union[DependencyEdge.Label, str]]=...) -> None:
        ...

class EntityMention(_message.Message):
    __slots__ = ('text', 'type', 'sentiment')

    class Type(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        TYPE_UNKNOWN: _ClassVar[EntityMention.Type]
        PROPER: _ClassVar[EntityMention.Type]
        COMMON: _ClassVar[EntityMention.Type]
    TYPE_UNKNOWN: EntityMention.Type
    PROPER: EntityMention.Type
    COMMON: EntityMention.Type
    TEXT_FIELD_NUMBER: _ClassVar[int]
    TYPE_FIELD_NUMBER: _ClassVar[int]
    SENTIMENT_FIELD_NUMBER: _ClassVar[int]
    text: TextSpan
    type: EntityMention.Type
    sentiment: Sentiment

    def __init__(self, text: _Optional[_Union[TextSpan, _Mapping]]=..., type: _Optional[_Union[EntityMention.Type, str]]=..., sentiment: _Optional[_Union[Sentiment, _Mapping]]=...) -> None:
        ...

class TextSpan(_message.Message):
    __slots__ = ('content', 'begin_offset')
    CONTENT_FIELD_NUMBER: _ClassVar[int]
    BEGIN_OFFSET_FIELD_NUMBER: _ClassVar[int]
    content: str
    begin_offset: int

    def __init__(self, content: _Optional[str]=..., begin_offset: _Optional[int]=...) -> None:
        ...

class ClassificationCategory(_message.Message):
    __slots__ = ('name', 'confidence')
    NAME_FIELD_NUMBER: _ClassVar[int]
    CONFIDENCE_FIELD_NUMBER: _ClassVar[int]
    name: str
    confidence: float

    def __init__(self, name: _Optional[str]=..., confidence: _Optional[float]=...) -> None:
        ...

class ClassificationModelOptions(_message.Message):
    __slots__ = ('v1_model', 'v2_model')

    class V1Model(_message.Message):
        __slots__ = ()

        def __init__(self) -> None:
            ...

    class V2Model(_message.Message):
        __slots__ = ('content_categories_version',)

        class ContentCategoriesVersion(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
            __slots__ = ()
            CONTENT_CATEGORIES_VERSION_UNSPECIFIED: _ClassVar[ClassificationModelOptions.V2Model.ContentCategoriesVersion]
            V1: _ClassVar[ClassificationModelOptions.V2Model.ContentCategoriesVersion]
            V2: _ClassVar[ClassificationModelOptions.V2Model.ContentCategoriesVersion]
        CONTENT_CATEGORIES_VERSION_UNSPECIFIED: ClassificationModelOptions.V2Model.ContentCategoriesVersion
        V1: ClassificationModelOptions.V2Model.ContentCategoriesVersion
        V2: ClassificationModelOptions.V2Model.ContentCategoriesVersion
        CONTENT_CATEGORIES_VERSION_FIELD_NUMBER: _ClassVar[int]
        content_categories_version: ClassificationModelOptions.V2Model.ContentCategoriesVersion

        def __init__(self, content_categories_version: _Optional[_Union[ClassificationModelOptions.V2Model.ContentCategoriesVersion, str]]=...) -> None:
            ...
    V1_MODEL_FIELD_NUMBER: _ClassVar[int]
    V2_MODEL_FIELD_NUMBER: _ClassVar[int]
    v1_model: ClassificationModelOptions.V1Model
    v2_model: ClassificationModelOptions.V2Model

    def __init__(self, v1_model: _Optional[_Union[ClassificationModelOptions.V1Model, _Mapping]]=..., v2_model: _Optional[_Union[ClassificationModelOptions.V2Model, _Mapping]]=...) -> None:
        ...

class AnalyzeSentimentRequest(_message.Message):
    __slots__ = ('document', 'encoding_type')
    DOCUMENT_FIELD_NUMBER: _ClassVar[int]
    ENCODING_TYPE_FIELD_NUMBER: _ClassVar[int]
    document: Document
    encoding_type: EncodingType

    def __init__(self, document: _Optional[_Union[Document, _Mapping]]=..., encoding_type: _Optional[_Union[EncodingType, str]]=...) -> None:
        ...

class AnalyzeSentimentResponse(_message.Message):
    __slots__ = ('document_sentiment', 'language', 'sentences')
    DOCUMENT_SENTIMENT_FIELD_NUMBER: _ClassVar[int]
    LANGUAGE_FIELD_NUMBER: _ClassVar[int]
    SENTENCES_FIELD_NUMBER: _ClassVar[int]
    document_sentiment: Sentiment
    language: str
    sentences: _containers.RepeatedCompositeFieldContainer[Sentence]

    def __init__(self, document_sentiment: _Optional[_Union[Sentiment, _Mapping]]=..., language: _Optional[str]=..., sentences: _Optional[_Iterable[_Union[Sentence, _Mapping]]]=...) -> None:
        ...

class AnalyzeEntitySentimentRequest(_message.Message):
    __slots__ = ('document', 'encoding_type')
    DOCUMENT_FIELD_NUMBER: _ClassVar[int]
    ENCODING_TYPE_FIELD_NUMBER: _ClassVar[int]
    document: Document
    encoding_type: EncodingType

    def __init__(self, document: _Optional[_Union[Document, _Mapping]]=..., encoding_type: _Optional[_Union[EncodingType, str]]=...) -> None:
        ...

class AnalyzeEntitySentimentResponse(_message.Message):
    __slots__ = ('entities', 'language')
    ENTITIES_FIELD_NUMBER: _ClassVar[int]
    LANGUAGE_FIELD_NUMBER: _ClassVar[int]
    entities: _containers.RepeatedCompositeFieldContainer[Entity]
    language: str

    def __init__(self, entities: _Optional[_Iterable[_Union[Entity, _Mapping]]]=..., language: _Optional[str]=...) -> None:
        ...

class AnalyzeEntitiesRequest(_message.Message):
    __slots__ = ('document', 'encoding_type')
    DOCUMENT_FIELD_NUMBER: _ClassVar[int]
    ENCODING_TYPE_FIELD_NUMBER: _ClassVar[int]
    document: Document
    encoding_type: EncodingType

    def __init__(self, document: _Optional[_Union[Document, _Mapping]]=..., encoding_type: _Optional[_Union[EncodingType, str]]=...) -> None:
        ...

class AnalyzeEntitiesResponse(_message.Message):
    __slots__ = ('entities', 'language')
    ENTITIES_FIELD_NUMBER: _ClassVar[int]
    LANGUAGE_FIELD_NUMBER: _ClassVar[int]
    entities: _containers.RepeatedCompositeFieldContainer[Entity]
    language: str

    def __init__(self, entities: _Optional[_Iterable[_Union[Entity, _Mapping]]]=..., language: _Optional[str]=...) -> None:
        ...

class AnalyzeSyntaxRequest(_message.Message):
    __slots__ = ('document', 'encoding_type')
    DOCUMENT_FIELD_NUMBER: _ClassVar[int]
    ENCODING_TYPE_FIELD_NUMBER: _ClassVar[int]
    document: Document
    encoding_type: EncodingType

    def __init__(self, document: _Optional[_Union[Document, _Mapping]]=..., encoding_type: _Optional[_Union[EncodingType, str]]=...) -> None:
        ...

class AnalyzeSyntaxResponse(_message.Message):
    __slots__ = ('sentences', 'tokens', 'language')
    SENTENCES_FIELD_NUMBER: _ClassVar[int]
    TOKENS_FIELD_NUMBER: _ClassVar[int]
    LANGUAGE_FIELD_NUMBER: _ClassVar[int]
    sentences: _containers.RepeatedCompositeFieldContainer[Sentence]
    tokens: _containers.RepeatedCompositeFieldContainer[Token]
    language: str

    def __init__(self, sentences: _Optional[_Iterable[_Union[Sentence, _Mapping]]]=..., tokens: _Optional[_Iterable[_Union[Token, _Mapping]]]=..., language: _Optional[str]=...) -> None:
        ...

class ClassifyTextRequest(_message.Message):
    __slots__ = ('document', 'classification_model_options')
    DOCUMENT_FIELD_NUMBER: _ClassVar[int]
    CLASSIFICATION_MODEL_OPTIONS_FIELD_NUMBER: _ClassVar[int]
    document: Document
    classification_model_options: ClassificationModelOptions

    def __init__(self, document: _Optional[_Union[Document, _Mapping]]=..., classification_model_options: _Optional[_Union[ClassificationModelOptions, _Mapping]]=...) -> None:
        ...

class ClassifyTextResponse(_message.Message):
    __slots__ = ('categories',)
    CATEGORIES_FIELD_NUMBER: _ClassVar[int]
    categories: _containers.RepeatedCompositeFieldContainer[ClassificationCategory]

    def __init__(self, categories: _Optional[_Iterable[_Union[ClassificationCategory, _Mapping]]]=...) -> None:
        ...

class ModerateTextRequest(_message.Message):
    __slots__ = ('document',)
    DOCUMENT_FIELD_NUMBER: _ClassVar[int]
    document: Document

    def __init__(self, document: _Optional[_Union[Document, _Mapping]]=...) -> None:
        ...

class ModerateTextResponse(_message.Message):
    __slots__ = ('moderation_categories',)
    MODERATION_CATEGORIES_FIELD_NUMBER: _ClassVar[int]
    moderation_categories: _containers.RepeatedCompositeFieldContainer[ClassificationCategory]

    def __init__(self, moderation_categories: _Optional[_Iterable[_Union[ClassificationCategory, _Mapping]]]=...) -> None:
        ...

class AnnotateTextRequest(_message.Message):
    __slots__ = ('document', 'features', 'encoding_type')

    class Features(_message.Message):
        __slots__ = ('extract_syntax', 'extract_entities', 'extract_document_sentiment', 'extract_entity_sentiment', 'classify_text', 'moderate_text', 'classification_model_options')
        EXTRACT_SYNTAX_FIELD_NUMBER: _ClassVar[int]
        EXTRACT_ENTITIES_FIELD_NUMBER: _ClassVar[int]
        EXTRACT_DOCUMENT_SENTIMENT_FIELD_NUMBER: _ClassVar[int]
        EXTRACT_ENTITY_SENTIMENT_FIELD_NUMBER: _ClassVar[int]
        CLASSIFY_TEXT_FIELD_NUMBER: _ClassVar[int]
        MODERATE_TEXT_FIELD_NUMBER: _ClassVar[int]
        CLASSIFICATION_MODEL_OPTIONS_FIELD_NUMBER: _ClassVar[int]
        extract_syntax: bool
        extract_entities: bool
        extract_document_sentiment: bool
        extract_entity_sentiment: bool
        classify_text: bool
        moderate_text: bool
        classification_model_options: ClassificationModelOptions

        def __init__(self, extract_syntax: bool=..., extract_entities: bool=..., extract_document_sentiment: bool=..., extract_entity_sentiment: bool=..., classify_text: bool=..., moderate_text: bool=..., classification_model_options: _Optional[_Union[ClassificationModelOptions, _Mapping]]=...) -> None:
            ...
    DOCUMENT_FIELD_NUMBER: _ClassVar[int]
    FEATURES_FIELD_NUMBER: _ClassVar[int]
    ENCODING_TYPE_FIELD_NUMBER: _ClassVar[int]
    document: Document
    features: AnnotateTextRequest.Features
    encoding_type: EncodingType

    def __init__(self, document: _Optional[_Union[Document, _Mapping]]=..., features: _Optional[_Union[AnnotateTextRequest.Features, _Mapping]]=..., encoding_type: _Optional[_Union[EncodingType, str]]=...) -> None:
        ...

class AnnotateTextResponse(_message.Message):
    __slots__ = ('sentences', 'tokens', 'entities', 'document_sentiment', 'language', 'categories', 'moderation_categories')
    SENTENCES_FIELD_NUMBER: _ClassVar[int]
    TOKENS_FIELD_NUMBER: _ClassVar[int]
    ENTITIES_FIELD_NUMBER: _ClassVar[int]
    DOCUMENT_SENTIMENT_FIELD_NUMBER: _ClassVar[int]
    LANGUAGE_FIELD_NUMBER: _ClassVar[int]
    CATEGORIES_FIELD_NUMBER: _ClassVar[int]
    MODERATION_CATEGORIES_FIELD_NUMBER: _ClassVar[int]
    sentences: _containers.RepeatedCompositeFieldContainer[Sentence]
    tokens: _containers.RepeatedCompositeFieldContainer[Token]
    entities: _containers.RepeatedCompositeFieldContainer[Entity]
    document_sentiment: Sentiment
    language: str
    categories: _containers.RepeatedCompositeFieldContainer[ClassificationCategory]
    moderation_categories: _containers.RepeatedCompositeFieldContainer[ClassificationCategory]

    def __init__(self, sentences: _Optional[_Iterable[_Union[Sentence, _Mapping]]]=..., tokens: _Optional[_Iterable[_Union[Token, _Mapping]]]=..., entities: _Optional[_Iterable[_Union[Entity, _Mapping]]]=..., document_sentiment: _Optional[_Union[Sentiment, _Mapping]]=..., language: _Optional[str]=..., categories: _Optional[_Iterable[_Union[ClassificationCategory, _Mapping]]]=..., moderation_categories: _Optional[_Iterable[_Union[ClassificationCategory, _Mapping]]]=...) -> None:
        ...