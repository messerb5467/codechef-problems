#!/user/bin/env bash
# No need to support -t at this time since this isn't a multi-image product.
docker build --build-arg UID=$(id -u) --build-arg=$(id -g) .