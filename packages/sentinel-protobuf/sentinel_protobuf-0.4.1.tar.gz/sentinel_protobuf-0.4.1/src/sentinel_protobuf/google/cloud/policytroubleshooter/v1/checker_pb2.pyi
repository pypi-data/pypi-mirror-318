from google.cloud.policytroubleshooter.v1 import explanations_pb2 as _explanations_pb2
from google.api import annotations_pb2 as _annotations_pb2
from google.api import client_pb2 as _client_pb2
from google.rpc import status_pb2 as _status_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union
from google.cloud.policytroubleshooter.v1.explanations_pb2 import AccessTuple as AccessTuple
from google.cloud.policytroubleshooter.v1.explanations_pb2 import ExplainedPolicy as ExplainedPolicy
from google.cloud.policytroubleshooter.v1.explanations_pb2 import BindingExplanation as BindingExplanation
from google.cloud.policytroubleshooter.v1.explanations_pb2 import AccessState as AccessState
from google.cloud.policytroubleshooter.v1.explanations_pb2 import HeuristicRelevance as HeuristicRelevance
DESCRIPTOR: _descriptor.FileDescriptor
ACCESS_STATE_UNSPECIFIED: _explanations_pb2.AccessState
GRANTED: _explanations_pb2.AccessState
NOT_GRANTED: _explanations_pb2.AccessState
UNKNOWN_CONDITIONAL: _explanations_pb2.AccessState
UNKNOWN_INFO_DENIED: _explanations_pb2.AccessState
HEURISTIC_RELEVANCE_UNSPECIFIED: _explanations_pb2.HeuristicRelevance
NORMAL: _explanations_pb2.HeuristicRelevance
HIGH: _explanations_pb2.HeuristicRelevance

class TroubleshootIamPolicyRequest(_message.Message):
    __slots__ = ('access_tuple',)
    ACCESS_TUPLE_FIELD_NUMBER: _ClassVar[int]
    access_tuple: _explanations_pb2.AccessTuple

    def __init__(self, access_tuple: _Optional[_Union[_explanations_pb2.AccessTuple, _Mapping]]=...) -> None:
        ...

class TroubleshootIamPolicyResponse(_message.Message):
    __slots__ = ('access', 'explained_policies', 'errors')
    ACCESS_FIELD_NUMBER: _ClassVar[int]
    EXPLAINED_POLICIES_FIELD_NUMBER: _ClassVar[int]
    ERRORS_FIELD_NUMBER: _ClassVar[int]
    access: _explanations_pb2.AccessState
    explained_policies: _containers.RepeatedCompositeFieldContainer[_explanations_pb2.ExplainedPolicy]
    errors: _containers.RepeatedCompositeFieldContainer[_status_pb2.Status]

    def __init__(self, access: _Optional[_Union[_explanations_pb2.AccessState, str]]=..., explained_policies: _Optional[_Iterable[_Union[_explanations_pb2.ExplainedPolicy, _Mapping]]]=..., errors: _Optional[_Iterable[_Union[_status_pb2.Status, _Mapping]]]=...) -> None:
        ...