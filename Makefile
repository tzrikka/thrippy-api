all: protoc-plugins google-deps go

# https://protobuf.dev/installation/
# https://grpc.io/docs/languages/go/quickstart/
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

.PHONY: go
go:
	rm -rf thrippypb
	protoc --proto_path=proto --go_out=. --go-grpc_out=. --go_opt=paths=source_relative --go-grpc_opt=paths=source_relative thrippy/v1/oauth.proto
	protoc --proto_path=proto --go_out=. --go-grpc_out=. --go_opt=paths=source_relative --go-grpc_opt=paths=source_relative thrippy/v1/thrippy.proto
	mv thrippy/ thrippypb/

.PHONY: clean
clean:
	rm -rf proto/google
	rm -rf thrippy
	rm -rf thrippypb
