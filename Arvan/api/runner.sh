#!/bin/sh

# Enter commands to run your application
service redis-server start
pm2 start --no-daemon counterAPI.js 