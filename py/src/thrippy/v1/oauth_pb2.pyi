from google.api import field_behavior_pb2 as _field_behavior_pb2
from google.protobuf import go_features_pb2 as _go_features_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Iterable as _Iterable, Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional

DESCRIPTOR: _descriptor.FileDescriptor

class OAuthConfig(_message.Message):
    __slots__ = ("auth_url", "token_url", "auth_style", "client_id", "client_secret", "scopes", "auth_codes", "params")
    class AuthCodesEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: str
        def __init__(self, key: _Optional[str] = ..., value: _Optional[str] = ...) -> None: ...
    class ParamsEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: str
        def __init__(self, key: _Optional[str] = ..., value: _Optional[str] = ...) -> None: ...
    AUTH_URL_FIELD_NUMBER: _ClassVar[int]
    TOKEN_URL_FIELD_NUMBER: _ClassVar[int]
    AUTH_STYLE_FIELD_NUMBER: _ClassVar[int]
    CLIENT_ID_FIELD_NUMBER: _ClassVar[int]
    CLIENT_SECRET_FIELD_NUMBER: _ClassVar[int]
    SCOPES_FIELD_NUMBER: _ClassVar[int]
    AUTH_CODES_FIELD_NUMBER: _ClassVar[int]
    PARAMS_FIELD_NUMBER: _ClassVar[int]
    auth_url: str
    token_url: str
    auth_style: int
    client_id: str
    client_secret: str
    scopes: _containers.RepeatedScalarFieldContainer[str]
    auth_codes: _containers.ScalarMap[str, str]
    params: _containers.ScalarMap[str, str]
    def __init__(self, auth_url: _Optional[str] = ..., token_url: _Optional[str] = ..., auth_style: _Optional[int] = ..., client_id: _Optional[str] = ..., client_secret: _Optional[str] = ..., scopes: _Optional[_Iterable[str]] = ..., auth_codes: _Optional[_Mapping[str, str]] = ..., params: _Optional[_Mapping[str, str]] = ...) -> None: ...

class OAuthToken(_message.Message):
    __slots__ = ("access_token", "expiry", "refresh_token", "token_type")
    ACCESS_TOKEN_FIELD_NUMBER: _ClassVar[int]
    EXPIRY_FIELD_NUMBER: _ClassVar[int]
    REFRESH_TOKEN_FIELD_NUMBER: _ClassVar[int]
    TOKEN_TYPE_FIELD_NUMBER: _ClassVar[int]
    access_token: str
    expiry: str
    refresh_token: str
    token_type: str
    def __init__(self, access_token: _Optional[str] = ..., expiry: _Optional[str] = ..., refresh_token: _Optional[str] = ..., token_type: _Optional[str] = ...) -> None: ...
