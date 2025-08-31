all: protoc-plugins google-deps go python

# https://protobuf.dev/installation/
# https://grpc.io/docs/languages/go/quickstart/
# https://github.com/protocolbuffers/protobuf/releases
# https://github.com/protocolbuffers/protobuf-go/releases
# https://pkg.go.dev/google.golang.org/grpc/cmd/protoc-gen-go-grpc?tab=versions
.PHONY: protoc-plugins
protoc-plugins:
	go install google.golang.org/protobuf/cmd/protoc-gen-go@latest
	go install google.golang.org/grpc/cmd/protoc-gen-go-grpc@latest

# https://github.com/googleapis/googleapis/tree/master/google/api
.PHONY: google-deps
google-deps: protoc-plugins
	curl --create-dirs https://raw.githubusercontent.com/googleapis/googleapis/master/google/api/annotations.proto    -o proto/google/api/annotations.proto
	curl --create-dirs https://raw.githubusercontent.com/googleapis/googleapis/master/google/api/client.proto         -o proto/google/api/client.proto
	curl --create-dirs https://raw.githubusercontent.com/googleapis/googleapis/master/google/api/field_behavior.proto -o proto/google/api/field_behavior.proto
	curl --create-dirs https://raw.githubusercontent.com/googleapis/googleapis/master/google/api/http.proto           -o proto/google/api/http.proto
	curl --create-dirs https://raw.githubusercontent.com/protocolbuffers/protobuf-go/refs/heads/master/src/google/protobuf/go_features.proto -o proto/google/protobuf/go_features.proto

.PHONY: go
go:
	protoc --proto_path=proto --go_out=. --go-grpc_out=. --go_opt=paths=source_relative --go-grpc_opt=paths=source_relative thrippy/v1/credentials.proto
	protoc --proto_path=proto --go_out=. --go-grpc_out=. --go_opt=paths=source_relative --go-grpc_opt=paths=source_relative thrippy/v1/oauth.proto
	protoc --proto_path=proto --go_out=. --go-grpc_out=. --go_opt=paths=source_relative --go-grpc_opt=paths=source_relative thrippy/v1/thrippy.proto

# https://grpc.io/docs/languages/python/quickstart/
.PHONY: python
python:
	$(MAKE) -C python

.PHONY: clean
clean:
	rm -rf proto/google
	rm -rf python/src/thrippy/v1
	rm -rf thrippy
