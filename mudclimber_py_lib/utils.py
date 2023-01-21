from protos import agents_pb2_grpc, agents_pb2
import grpc
import asyncio
import typing as t
import traceback
from aiostream import stream
from dataclasses import dataclass
import uuid

members = {}


@dataclass
class MemberEvent:
    buf: bytes


async def _queue_listener(q):
    while True:
        v = await q.get()
        if v:
            yield v


async def loop_tick(guids):
    channel = grpc.insecure_channel('localhost:10101')
    while True:
        for guid in guids:
            stub = agents_pb2_grpc.AgentCommsStub(channel)
            r = agents_pb2.PingRequest(
                disconnect=False,
                guid=guid,
            )
            print(stub.PingAgent(r))
        await asyncio.sleep(5)


async def register_agent_rpc(channel, cb, ct, host, port, display_name):

    stub = agents_pb2_grpc.AgentCommsStub(channel)
    if ct == "tcp":
        loop = asyncio.get_running_loop()
        server = await loop.create_server(cb, host, port)
        agent = agents_pb2.Agent(
            tcp=agents_pb2.TcpConnection(
                host=host,
                port=port,
            ),
            display_name=display_name,
        )
    else:
        server = grpc.aio.server()
        server.add_insecure_port(f"{host}:{port}")
        agents_pb2_grpc.add_AgentStreamsServicer_to_server(cb, server)
        agent = agents_pb2.Agent(
            rpc=agents_pb2.RpcConnection(
                host=host,
                port=port,
            ),
            display_name=display_name,
        )
    r = agents_pb2.NewAgentRequest(agent=agent)
    agent_results = stub.NewAgent(r)

    return (server, agent_results)


class Servicer(agents_pb2_grpc.AgentStreamsServicer):
    login: str
    members: t.Dict[str, t.Any]

    def _set_members(self, members):
        self.members = members

    def write(self, buf: bytes):
        return agents_pb2.AgentStreamResponse(write=agents_pb2.Write(buf=buf))

    # don't want to deal with a true init callback for now
    def on_first_request(self, u):
        pass

    async def AgentStream(self, request_iterator, context):
        u = str(uuid.uuid4())
        self.members[u] = {}
        if not hasattr(self, "_any_requests"):
            self.on_first_request(u)
            self._any_requests = True
        relay_queue = asyncio.Queue()
        try:
            async for req in stream.merge(request_iterator, _queue_listener(relay_queue)).stream():
                if isinstance(req, MemberEvent):
                    yield self.write(req.buf)
                elif type(req) is int:
                    pass
                if isinstance(req, agents_pb2.AgentStreamRequest):
                    print(type(req))
                    frame = req.WhichOneof("frame")
                    if frame == "login":
                        self.members[u]["login"] = req.login.login
                        self.members[u]["geometry"] = (req.login.columns, req.login.rows)
                        self.members[u]["writer"] = relay_queue
                        async for packet in self.on_login(u, req.login.login):
                            if isinstance(packet, agents_pb2.AgentStreamResponse):
                                yield packet
                        print("login complete")
                    elif frame == "read":
                        async for packet in self.on_read(u, req.read.buf):
                            if isinstance(packet, agents_pb2.AgentStreamResponse):
                                yield packet
                            elif not packet:
                                # end the stream
                                async for packet in self.on_close(u):
                                    if isinstance(packet, agents_pb2.AgentStreamResponse):
                                        yield packet
                                return
                    elif frame == "resize":
                        self.members[u]["geometry"] = (req.resize.columns, req.resize.rows)
                        async for packet in self.on_resize(u, req.resize.columns, req.resize.rows):
                            if isinstance(packet, agents_pb2.AgentStreamResponse):
                                yield packet
                    if frame == "disconnect":
                        await self.on_disconnect(u)
        except Exception as e:
            print(e)
            print(traceback.format_exc())
        finally:
            del self.members[u]

    async def on_login(self, u, buf):
        yield 0

    async def on_read(self, u, buf):
        yield 0

    async def on_close(self, u):
        yield 0

    async def on_disconnect(self, u):
        return 0


class Runner:
    servicer: t.Any
    host: str
    port: int

    def __init__(self, servicer, host, port) -> None:
        self.servicer = servicer
        self.host = host
        self.port = port

    async def run(self):
        server = grpc.aio.server()
        server.add_insecure_port(f'{self.host}:{self.port}')
        agents_pb2_grpc.add_AgentStreamsServicer_to_server(self.servicer, server)

        await server.start()
        await server.wait_for_termination()

