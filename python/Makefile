all: py

# https://grpc.io/docs/languages/python/quickstart/
# https://pypi.org/project/grpcio/
.PHONY: py
py:
	protoc --proto_path=../proto --python_out=src --pyi_out=src ../proto/thrippy/v1/credentials.proto
	protoc --proto_path=../proto --python_out=src --pyi_out=src ../proto/thrippy/v1/oauth.proto
	protoc --proto_path=../proto --python_out=src --pyi_out=src ../proto/thrippy/v1/thrippy.proto
	uv sync --active
	uv run --active -m grpc_tools.protoc --proto_path=../proto --grpc_python_out=src ../proto/thrippy/v1/thrippy.proto
