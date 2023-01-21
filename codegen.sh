#!/bin/bash

cp protos/agents.proto mudclimber_py_lib/protos/agents.proto
trap 'rm mudclimber_py_lib/protos/agents.proto' EXIT

python -m grpc_tools.protoc --python_out=. --pyi_out=. --grpc_python_out=. -I. mudclimber_py_lib/protos/agents.proto
