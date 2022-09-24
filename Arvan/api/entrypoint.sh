#!/bin/sh

echo "Starting the redis daemon"
service redis-server start

echo "Starting the counterAPI daemon"
/bin/sh /api/runner.sh
