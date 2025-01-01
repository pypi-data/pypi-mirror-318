#!/bin/bash
#
# Builds python auto-generated protobuf files

set -eux

ROOT_DIR=$(pwd)
PROJECT_DIR=$(realpath ../..)
GEN_DIR=$(realpath ./mtmaisdk)

ROOT_DIR=$(pwd)

echo "生成 mtm python sdk PROJECT_DIR:${PROJECT_DIR}, GEN_DIR:${GEN_DIR}"

# deps
version=7.3.0

openapi-generator-cli version || npm install @openapitools/openapi-generator-cli -g

# if [ "$(openapi-generator-cli version)" != "$version" ]; then
#   version-manager set "$version"
# fi

# generate deps from hatchet repo
# cd hatchet/ && sh ./hack/oas/generate-server.sh && cd $ROOT_DIR

# generate python rest client

dst_dir=./mtmaisdk/clients/rest

mkdir -p $dst_dir

tmp_dir=./tmp

# echo "pwd: $(pwd)"
# echo "bin: $(ls -la ./bin)"



# generate into tmp folder
openapi-generator-cli generate -i ${PROJECT_DIR}/bin/oas/openapi.yaml -g python -o ./tmp --skip-validate-spec \
    --library asyncio \
    --global-property=apiTests=false \
    --global-property=apiDocs=true \
    --global-property=modelTests=false \
    --global-property=modelDocs=true \
    --package-name mtmaisdk.clients.rest

mv $tmp_dir/mtmaisdk/clients/rest/api_client.py $dst_dir/api_client.py
mv $tmp_dir/mtmaisdk/clients/rest/configuration.py $dst_dir/configuration.py
mv $tmp_dir/mtmaisdk/clients/rest/api_response.py $dst_dir/api_response.py
mv $tmp_dir/mtmaisdk/clients/rest/exceptions.py $dst_dir/exceptions.py
mv $tmp_dir/mtmaisdk/clients/rest/__init__.py $dst_dir/__init__.py
mv $tmp_dir/mtmaisdk/clients/rest/rest.py $dst_dir/rest.py

openapi-generator-cli generate -i ${PROJECT_DIR}/bin/oas/openapi.yaml -g python -o . --skip-validate-spec \
    --library asyncio \
    --global-property=apis,models \
    --global-property=apiTests=false \
    --global-property=apiDocs=false \
    --global-property=modelTests=false \
    --global-property=modelDocs=false \
    --package-name mtmaisdk.clients.rest

# copy the __init__ files from tmp to the destination since they are not generated for some reason
cp $tmp_dir/mtmaisdk/clients/rest/models/__init__.py $dst_dir/models/__init__.py
cp $tmp_dir/mtmaisdk/clients/rest/api/__init__.py $dst_dir/api/__init__.py

# remove tmp folder
rm -rf $tmp_dir



echo "GEN_DIR:${GEN_DIR}"
poetry run python -m grpc_tools.protoc --proto_path=${PROJECT_DIR}/api-contracts/dispatcher --python_out=${GEN_DIR}/contracts --pyi_out=${GEN_DIR}/contracts --grpc_python_out=${GEN_DIR}/contracts dispatcher.proto
poetry run python -m grpc_tools.protoc --proto_path=${PROJECT_DIR}/api-contracts/events --python_out=${GEN_DIR}/contracts --pyi_out=${GEN_DIR}/contracts --grpc_python_out=${GEN_DIR}/contracts events.proto
poetry run python -m grpc_tools.protoc --proto_path=${PROJECT_DIR}/api-contracts/workflows --python_out=${GEN_DIR}/contracts --pyi_out=${GEN_DIR}/contracts --grpc_python_out=${GEN_DIR}/contracts workflows.proto

OSTYPE=${OSTYPE:-"linux"}
# Fix relative imports in _grpc.py files
if [[ "$OSTYPE" == "darwin"* ]]; then
    # macOS
    find ${GEN_DIR}/contracts -type f -name '*_grpc.py' -print0 | xargs -0 sed -i '' 's/^import \([^ ]*\)_pb2/from . import \1_pb2/'
else
    # Linux and others
    find ${GEN_DIR}/contracts -type f -name '*_grpc.py' -print0 | xargs -0 sed -i 's/^import \([^ ]*\)_pb2/from . import \1_pb2/'
fi

# ensure that pre-commit is applied without errors
# pre-commit run --all-files || pre-commit run --all-files

# apply patch to openapi-generator generated code

# echo "pwd: $(pwd), ROOT_DIR:${ROOT_DIR}"
# patch -p1 --no-backup-if-mismatch <${ROOT_DIR}/openapi_patch.patch
