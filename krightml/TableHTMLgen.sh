#!/bin/bash

go build main.go
./main &
SERVER_PID=$!
sleep 2
curl http://localhost:8080/ > Table.html
kill $SERVER_PID
