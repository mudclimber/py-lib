#!/bin/bash

python -m grpc_tools.protoc --python_out=. --pyi_out=. --grpc_python_out=. -I. protos/agents.proto
