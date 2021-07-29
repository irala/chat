#!/bin/bash


COMPOSE="docker-compose  "

for ms in "$@" ; do
    BUILD="$ms"

    echo ">>>>> Create $BUILD"
    ./build.sh "$BUILD" &
done

wait


for ms in "$@" ; do
    echo ">>>>>>> Launch $@"
    $COMPOSE up -d "$ms"
done

echo ">>>>>>> Logs"
$COMPOSE logs -f "$@"

