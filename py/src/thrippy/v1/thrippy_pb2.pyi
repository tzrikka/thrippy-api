from google.api import annotations_pb2 as _annotations_pb2
from google.api import field_behavior_pb2 as _field_behavior_pb2
from google.protobuf import go_features_pb2 as _go_features_pb2
from thrippy.v1 import credentials_pb2 as _credentials_pb2
from thrippy.v1 import oauth_pb2 as _oauth_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Iterable as _Iterable, Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class CreateLinkRequest(_message.Message):
    __slots__ = ("template", "oauth_config")
    TEMPLATE_FIELD_NUMBER: _ClassVar[int]
    OAUTH_CONFIG_FIELD_NUMBER: _ClassVar[int]
    template: str
    oauth_config: _oauth_pb2.OAuthConfig
    def __init__(self, template: _Optional[str] = ..., oauth_config: _Optional[_Union[_oauth_pb2.OAuthConfig, _Mapping]] = ...) -> None: ...

class CreateLinkResponse(_message.Message):
    __slots__ = ("link_id", "credential_fields")
    LINK_ID_FIELD_NUMBER: _ClassVar[int]
    CREDENTIAL_FIELDS_FIELD_NUMBER: _ClassVar[int]
    link_id: str
    credential_fields: _containers.RepeatedCompositeFieldContainer[_credentials_pb2.CredentialField]
    def __init__(self, link_id: _Optional[str] = ..., credential_fields: _Optional[_Iterable[_Union[_credentials_pb2.CredentialField, _Mapping]]] = ...) -> None: ...

class GetLinkRequest(_message.Message):
    __slots__ = ("link_id",)
    LINK_ID_FIELD_NUMBER: _ClassVar[int]
    link_id: str
    def __init__(self, link_id: _Optional[str] = ...) -> None: ...

class GetLinkResponse(_message.Message):
    __slots__ = ("template", "oauth_config", "credential_fields")
    TEMPLATE_FIELD_NUMBER: _ClassVar[int]
    OAUTH_CONFIG_FIELD_NUMBER: _ClassVar[int]
    CREDENTIAL_FIELDS_FIELD_NUMBER: _ClassVar[int]
    template: str
    oauth_config: _oauth_pb2.OAuthConfig
    credential_fields: _containers.RepeatedCompositeFieldContainer[_credentials_pb2.CredentialField]
    def __init__(self, template: _Optional[str] = ..., oauth_config: _Optional[_Union[_oauth_pb2.OAuthConfig, _Mapping]] = ..., credential_fields: _Optional[_Iterable[_Union[_credentials_pb2.CredentialField, _Mapping]]] = ...) -> None: ...

class DeleteLinkRequest(_message.Message):
    __slots__ = ("link_id", "allow_missing")
    LINK_ID_FIELD_NUMBER: _ClassVar[int]
    ALLOW_MISSING_FIELD_NUMBER: _ClassVar[int]
    link_id: str
    allow_missing: bool
    def __init__(self, link_id: _Optional[str] = ..., allow_missing: bool = ...) -> None: ...

class DeleteLinkResponse(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class SetCredentialsRequest(_message.Message):
    __slots__ = ("link_id", "generic_creds", "token")
    class GenericCredsEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: str
        def __init__(self, key: _Optional[str] = ..., value: _Optional[str] = ...) -> None: ...
    LINK_ID_FIELD_NUMBER: _ClassVar[int]
    GENERIC_CREDS_FIELD_NUMBER: _ClassVar[int]
    TOKEN_FIELD_NUMBER: _ClassVar[int]
    link_id: str
    generic_creds: _containers.ScalarMap[str, str]
    token: _oauth_pb2.OAuthToken
    def __init__(self, link_id: _Optional[str] = ..., generic_creds: _Optional[_Mapping[str, str]] = ..., token: _Optional[_Union[_oauth_pb2.OAuthToken, _Mapping]] = ...) -> None: ...

class SetCredentialsResponse(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class GetCredentialsRequest(_message.Message):
    __slots__ = ("link_id",)
    LINK_ID_FIELD_NUMBER: _ClassVar[int]
    link_id: str
    def __init__(self, link_id: _Optional[str] = ...) -> None: ...

class GetCredentialsResponse(_message.Message):
    __slots__ = ("credentials",)
    class CredentialsEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: str
        def __init__(self, key: _Optional[str] = ..., value: _Optional[str] = ...) -> None: ...
    CREDENTIALS_FIELD_NUMBER: _ClassVar[int]
    credentials: _containers.ScalarMap[str, str]
    def __init__(self, credentials: _Optional[_Mapping[str, str]] = ...) -> None: ...

class DeleteCredentialsRequest(_message.Message):
    __slots__ = ("link_id", "allow_missing")
    LINK_ID_FIELD_NUMBER: _ClassVar[int]
    ALLOW_MISSING_FIELD_NUMBER: _ClassVar[int]
    link_id: str
    allow_missing: bool
    def __init__(self, link_id: _Optional[str] = ..., allow_missing: bool = ...) -> None: ...

class DeleteCredentialsResponse(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class SetMetadataRequest(_message.Message):
    __slots__ = ("link_id", "metadata")
    class MetadataEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: str
        def __init__(self, key: _Optional[str] = ..., value: _Optional[str] = ...) -> None: ...
    LINK_ID_FIELD_NUMBER: _ClassVar[int]
    METADATA_FIELD_NUMBER: _ClassVar[int]
    link_id: str
    metadata: _containers.ScalarMap[str, str]
    def __init__(self, link_id: _Optional[str] = ..., metadata: _Optional[_Mapping[str, str]] = ...) -> None: ...

class SetMetadataResponse(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class GetMetadataRequest(_message.Message):
    __slots__ = ("link_id",)
    LINK_ID_FIELD_NUMBER: _ClassVar[int]
    link_id: str
    def __init__(self, link_id: _Optional[str] = ...) -> None: ...

class GetMetadataResponse(_message.Message):
    __slots__ = ("metadata",)
    class MetadataEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: str
        def __init__(self, key: _Optional[str] = ..., value: _Optional[str] = ...) -> None: ...
    METADATA_FIELD_NUMBER: _ClassVar[int]
    metadata: _containers.ScalarMap[str, str]
    def __init__(self, metadata: _Optional[_Mapping[str, str]] = ...) -> None: ...

class DeleteMetadataRequest(_message.Message):
    __slots__ = ("link_id", "allow_missing")
    LINK_ID_FIELD_NUMBER: _ClassVar[int]
    ALLOW_MISSING_FIELD_NUMBER: _ClassVar[int]
    link_id: str
    allow_missing: bool
    def __init__(self, link_id: _Optional[str] = ..., allow_missing: bool = ...) -> None: ...

class DeleteMetadataResponse(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...
