#!/bin/sh
v=0.0.2

docker build -f ./docker/qa/Dockerfile -t mediheart_qa_server:$v . --no-cache
docker tag mediheart_qa_server:0.0.2 giuseppemaddiona/mh-server-qa:0.0.2
docker push giuseppemaddiona/mh-server-qa:0.0.2 