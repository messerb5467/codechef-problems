#!/usr/bin/env bash
TAG="latest"

usage() {
  echo "$0 [-t tag_name]"
  echo "   Optional:"
  echo "       -t tag_name Build the docker image with the specified tag name."
}

while getopts "t:h" option; do
  case "${option}" in
    t)
      re_undesired_start_chars="^[.-]"
      re_proper_tag_format="[a-zA-z0-9_.-]+"
      tag_length=${#OPTARG}
      if ! [[ $OPTARG =~ $re_undesired_start_chars ]] &&
           [[ $OPTARG =~ $re_proper_format ]] &&
           [[ "$tag_length" -ge 1 && "$tag_length" -le 128 ]]; then
        TAG=${OPTARG}
      fi
      ;;
    h)
      usage
      exit 1
      ;;
    *)
      usage
      exit 2
      ;;
  esac
done
docker build  --build-arg username=$(id -u -n) --build-arg uid=$(id -u) --build-arg gid=$(id -g) . -t "bush-fire:${TAG}"