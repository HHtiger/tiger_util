#!/bin/sh
while inotifywait -e modify your/listener/file; do
     echo 'begin rsync...'
     parallel-rsync -h remote/ip/lists/file your/listener/file /remote/update/file
     echo 'rsync finished...'
done
