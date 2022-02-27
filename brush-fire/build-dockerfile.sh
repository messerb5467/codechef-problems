#!/usr/bin/env bash
# No need to support -t at this time since this isn't a multi-image product.
docker build  --build-arg username=$(id -u -n) --build-arg uid=$(id -u) --build-arg gid=$(id -g) . -t bush-fire:latest