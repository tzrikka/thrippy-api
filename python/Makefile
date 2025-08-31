all: py

# https://grpc.io/docs/languages/python/quickstart/
.PHONY: py
py:
	uv sync --active
	uv run --active -m grpc_tools.protoc --proto_path=../proto --python_out=src --pyi_out=src --grpc_python_out=src ../proto/thrippy/v1/credentials.proto
	uv run --active -m grpc_tools.protoc --proto_path=../proto --python_out=src --pyi_out=src --grpc_python_out=src ../proto/thrippy/v1/oauth.proto
	uv run --active -m grpc_tools.protoc --proto_path=../proto --python_out=src --pyi_out=src --grpc_python_out=src ../proto/thrippy/v1/thrippy.proto
