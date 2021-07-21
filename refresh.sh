#!/bin/bash


for ms in "$@" ; do
    BUILD="$ms"

    echo ">>>>> Create $BUILD"
    ./build.sh "$BUILD" &
done

wait

docker-compose up 

