#!/bin/bash

# アプリ名
APP_NAME=water_gate

# git
git pull

# stop
pm2 stop ${APP_NAME}

# delete
pm2 delete ${APP_NAME}

# build
npm run build

# start
pm2 start npm --name "${APP_NAME}" -- start