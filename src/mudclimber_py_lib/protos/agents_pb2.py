# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: mudclimber_py_lib/protos/agents.proto
"""Generated protocol buffer code."""
from google.protobuf.internal import builder as _builder
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n%mudclimber_py_lib/protos/agents.proto\x12\x11hub_protos.agents\"+\n\rTcpConnection\x12\x0c\n\x04host\x18\x01 \x01(\t\x12\x0c\n\x04port\x18\x02 \x01(\r\"+\n\rRpcConnection\x12\x0c\n\x04host\x18\x01 \x01(\t\x12\x0c\n\x04port\x18\x02 \x01(\r\"\x8d\x01\n\x05\x41gent\x12/\n\x03tcp\x18\x01 \x01(\x0b\x32 .hub_protos.agents.TcpConnectionH\x00\x12/\n\x03rpc\x18\x02 \x01(\x0b\x32 .hub_protos.agents.RpcConnectionH\x00\x12\x14\n\x0c\x64isplay_name\x18\x03 \x01(\tB\x0c\n\nconnection\":\n\x0fNewAgentRequest\x12\'\n\x05\x61gent\x18\x01 \x01(\x0b\x32\x18.hub_protos.agents.Agent\"\xc7\x01\n\x10NewAgentResponse\x12\x43\n\x0b\x61gent_state\x18\x01 \x01(\x0e\x32..hub_protos.agents.NewAgentResponse.AgentState\x12\x1f\n\x17next_keepalive_deadline\x18\x02 \x01(\x04\x12\x0c\n\x04guid\x18\x03 \x01(\x0c\"?\n\nAgentState\x12\x07\n\x03\x41\x43K\x10\x00\x12\x12\n\x0e\x41LREADY_EXISTS\x10\x01\x12\x14\n\x10\x43ONNECTION_ISSUE\x10\x02\"/\n\x0bPingRequest\x12\x12\n\ndisconnect\x18\x01 \x01(\x08\x12\x0c\n\x04guid\x18\x02 \x01(\x0c\"/\n\x0cPingResponse\x12\x1f\n\x17next_keepalive_deadline\x18\x01 \x01(\x04\"5\n\x05Login\x12\r\n\x05login\x18\x01 \x01(\t\x12\x0f\n\x07\x63olumns\x18\x02 \x01(\r\x12\x0c\n\x04rows\x18\x03 \x01(\r\"\x13\n\x04Read\x12\x0b\n\x03\x62uf\x18\x01 \x01(\x0c\"\'\n\x06Resize\x12\x0f\n\x07\x63olumns\x18\x01 \x01(\r\x12\x0c\n\x04rows\x18\x02 \x01(\r\"\x0c\n\nDisconnect\"\xd3\x01\n\x12\x41gentStreamRequest\x12)\n\x05login\x18\x01 \x01(\x0b\x32\x18.hub_protos.agents.LoginH\x00\x12\'\n\x04read\x18\x02 \x01(\x0b\x32\x17.hub_protos.agents.ReadH\x00\x12+\n\x06resize\x18\x03 \x01(\x0b\x32\x19.hub_protos.agents.ResizeH\x00\x12\x33\n\ndisconnect\x18\x04 \x01(\x0b\x32\x1d.hub_protos.agents.DisconnectH\x00\x42\x07\n\x05\x66rame\"\x14\n\x05Write\x12\x0b\n\x03\x62uf\x18\x01 \x01(\x0c\">\n\x13\x41gentStreamResponse\x12\'\n\x05write\x18\x01 \x01(\x0b\x32\x18.hub_protos.agents.Write2\xaf\x01\n\nAgentComms\x12S\n\x08NewAgent\x12\".hub_protos.agents.NewAgentRequest\x1a#.hub_protos.agents.NewAgentResponse\x12L\n\tPingAgent\x12\x1e.hub_protos.agents.PingRequest\x1a\x1f.hub_protos.agents.PingResponse2p\n\x0c\x41gentStreams\x12`\n\x0b\x41gentStream\x12%.hub_protos.agents.AgentStreamRequest\x1a&.hub_protos.agents.AgentStreamResponse(\x01\x30\x01\x62\x06proto3')

_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, globals())
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'mudclimber_py_lib.protos.agents_pb2', globals())
if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  _TCPCONNECTION._serialized_start=60
  _TCPCONNECTION._serialized_end=103
  _RPCCONNECTION._serialized_start=105
  _RPCCONNECTION._serialized_end=148
  _AGENT._serialized_start=151
  _AGENT._serialized_end=292
  _NEWAGENTREQUEST._serialized_start=294
  _NEWAGENTREQUEST._serialized_end=352
  _NEWAGENTRESPONSE._serialized_start=355
  _NEWAGENTRESPONSE._serialized_end=554
  _NEWAGENTRESPONSE_AGENTSTATE._serialized_start=491
  _NEWAGENTRESPONSE_AGENTSTATE._serialized_end=554
  _PINGREQUEST._serialized_start=556
  _PINGREQUEST._serialized_end=603
  _PINGRESPONSE._serialized_start=605
  _PINGRESPONSE._serialized_end=652
  _LOGIN._serialized_start=654
  _LOGIN._serialized_end=707
  _READ._serialized_start=709
  _READ._serialized_end=728
  _RESIZE._serialized_start=730
  _RESIZE._serialized_end=769
  _DISCONNECT._serialized_start=771
  _DISCONNECT._serialized_end=783
  _AGENTSTREAMREQUEST._serialized_start=786
  _AGENTSTREAMREQUEST._serialized_end=997
  _WRITE._serialized_start=999
  _WRITE._serialized_end=1019
  _AGENTSTREAMRESPONSE._serialized_start=1021
  _AGENTSTREAMRESPONSE._serialized_end=1083
  _AGENTCOMMS._serialized_start=1086
  _AGENTCOMMS._serialized_end=1261
  _AGENTSTREAMS._serialized_start=1263
  _AGENTSTREAMS._serialized_end=1375
# @@protoc_insertion_point(module_scope)