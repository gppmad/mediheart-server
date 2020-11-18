#!/bin/sh
v=0.0.5

docker build -f ./docker/qa/Dockerfile -t mediheart_qa_server:$v . --no-cache
docker tag mediheart_qa_server:$v giuseppemaddiona/mh-server-qa:$v
docker push giuseppemaddiona/mh-server-qa:$v 