#!/bin/sh
while inotifywait -e modify your_listener_file; do
     echo 'begin rsync...'
     parallel-rsync -h hostlist_file your_listener_file /remote/update/file
     echo 'rsync finished...'
done
