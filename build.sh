#!/bin/bash

BUILDALL=""
CORES=$(nproc --all)

if [[ -z $1 ]]; then
    BUILDALL="true"
fi

if [[ $1 == "identity" ]] || [[ -n $BUILDALL ]]; then
    #building identity
    docker build --rm -f identity/dockerfile -t identity identity
fi


# if [[ $1 == "chatting" ]] || [[ -n $BUILDALL ]]; then
#     #building identity
#     docker build --rm -f chatting/dockerfile -t chatting chatting
# fi
# docker run --rm -p 8081:8081 -d identity
