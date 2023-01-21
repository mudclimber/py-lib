from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class Agent(_message.Message):
    __slots__ = ["display_name", "rpc", "tcp"]
    DISPLAY_NAME_FIELD_NUMBER: _ClassVar[int]
    RPC_FIELD_NUMBER: _ClassVar[int]
    TCP_FIELD_NUMBER: _ClassVar[int]
    display_name: str
    rpc: RpcConnection
    tcp: TcpConnection
    def __init__(self, tcp: _Optional[_Union[TcpConnection, _Mapping]] = ..., rpc: _Optional[_Union[RpcConnection, _Mapping]] = ..., display_name: _Optional[str] = ...) -> None: ...

class AgentStreamRequest(_message.Message):
    __slots__ = ["disconnect", "login", "read", "resize"]
    DISCONNECT_FIELD_NUMBER: _ClassVar[int]
    LOGIN_FIELD_NUMBER: _ClassVar[int]
    READ_FIELD_NUMBER: _ClassVar[int]
    RESIZE_FIELD_NUMBER: _ClassVar[int]
    disconnect: Disconnect
    login: Login
    read: Read
    resize: Resize
    def __init__(self, login: _Optional[_Union[Login, _Mapping]] = ..., read: _Optional[_Union[Read, _Mapping]] = ..., resize: _Optional[_Union[Resize, _Mapping]] = ..., disconnect: _Optional[_Union[Disconnect, _Mapping]] = ...) -> None: ...

class AgentStreamResponse(_message.Message):
    __slots__ = ["write"]
    WRITE_FIELD_NUMBER: _ClassVar[int]
    write: Write
    def __init__(self, write: _Optional[_Union[Write, _Mapping]] = ...) -> None: ...

class Disconnect(_message.Message):
    __slots__ = []
    def __init__(self) -> None: ...

class Login(_message.Message):
    __slots__ = ["columns", "login", "rows"]
    COLUMNS_FIELD_NUMBER: _ClassVar[int]
    LOGIN_FIELD_NUMBER: _ClassVar[int]
    ROWS_FIELD_NUMBER: _ClassVar[int]
    columns: int
    login: str
    rows: int
    def __init__(self, login: _Optional[str] = ..., columns: _Optional[int] = ..., rows: _Optional[int] = ...) -> None: ...

class NewAgentRequest(_message.Message):
    __slots__ = ["agent"]
    AGENT_FIELD_NUMBER: _ClassVar[int]
    agent: Agent
    def __init__(self, agent: _Optional[_Union[Agent, _Mapping]] = ...) -> None: ...

class NewAgentResponse(_message.Message):
    __slots__ = ["agent_state", "guid", "next_keepalive_deadline"]
    class AgentState(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = []
    ACK: NewAgentResponse.AgentState
    AGENT_STATE_FIELD_NUMBER: _ClassVar[int]
    ALREADY_EXISTS: NewAgentResponse.AgentState
    CONNECTION_ISSUE: NewAgentResponse.AgentState
    GUID_FIELD_NUMBER: _ClassVar[int]
    NEXT_KEEPALIVE_DEADLINE_FIELD_NUMBER: _ClassVar[int]
    agent_state: NewAgentResponse.AgentState
    guid: bytes
    next_keepalive_deadline: int
    def __init__(self, agent_state: _Optional[_Union[NewAgentResponse.AgentState, str]] = ..., next_keepalive_deadline: _Optional[int] = ..., guid: _Optional[bytes] = ...) -> None: ...

class PingRequest(_message.Message):
    __slots__ = ["disconnect", "guid"]
    DISCONNECT_FIELD_NUMBER: _ClassVar[int]
    GUID_FIELD_NUMBER: _ClassVar[int]
    disconnect: bool
    guid: bytes
    def __init__(self, disconnect: bool = ..., guid: _Optional[bytes] = ...) -> None: ...

class PingResponse(_message.Message):
    __slots__ = ["next_keepalive_deadline"]
    NEXT_KEEPALIVE_DEADLINE_FIELD_NUMBER: _ClassVar[int]
    next_keepalive_deadline: int
    def __init__(self, next_keepalive_deadline: _Optional[int] = ...) -> None: ...

class Read(_message.Message):
    __slots__ = ["buf"]
    BUF_FIELD_NUMBER: _ClassVar[int]
    buf: bytes
    def __init__(self, buf: _Optional[bytes] = ...) -> None: ...

class Resize(_message.Message):
    __slots__ = ["columns", "rows"]
    COLUMNS_FIELD_NUMBER: _ClassVar[int]
    ROWS_FIELD_NUMBER: _ClassVar[int]
    columns: int
    rows: int
    def __init__(self, columns: _Optional[int] = ..., rows: _Optional[int] = ...) -> None: ...

class RpcConnection(_message.Message):
    __slots__ = ["host", "port"]
    HOST_FIELD_NUMBER: _ClassVar[int]
    PORT_FIELD_NUMBER: _ClassVar[int]
    host: str
    port: int
    def __init__(self, host: _Optional[str] = ..., port: _Optional[int] = ...) -> None: ...

class TcpConnection(_message.Message):
    __slots__ = ["host", "port"]
    HOST_FIELD_NUMBER: _ClassVar[int]
    PORT_FIELD_NUMBER: _ClassVar[int]
    host: str
    port: int
    def __init__(self, host: _Optional[str] = ..., port: _Optional[int] = ...) -> None: ...

class Write(_message.Message):
    __slots__ = ["buf"]
    BUF_FIELD_NUMBER: _ClassVar[int]
    buf: bytes
    def __init__(self, buf: _Optional[bytes] = ...) -> None: ...
