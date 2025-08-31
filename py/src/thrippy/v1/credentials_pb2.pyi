from google.api import field_behavior_pb2 as _field_behavior_pb2
from google.protobuf import go_features_pb2 as _go_features_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Iterable as _Iterable
from typing import ClassVar as _ClassVar, Optional as _Optional

DESCRIPTOR: _descriptor.FileDescriptor

class CredentialField(_message.Message):
    __slots__ = ("name", "description", "links", "manual", "optional")
    NAME_FIELD_NUMBER: _ClassVar[int]
    DESCRIPTION_FIELD_NUMBER: _ClassVar[int]
    LINKS_FIELD_NUMBER: _ClassVar[int]
    MANUAL_FIELD_NUMBER: _ClassVar[int]
    OPTIONAL_FIELD_NUMBER: _ClassVar[int]
    name: str
    description: str
    links: _containers.RepeatedScalarFieldContainer[str]
    manual: bool
    optional: bool
    def __init__(self, name: _Optional[str] = ..., description: _Optional[str] = ..., links: _Optional[_Iterable[str]] = ..., manual: bool = ..., optional: bool = ...) -> None: ...
