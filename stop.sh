#!/usr/bin/bash
# Check if server is running
if ! screen -list | grep -q "servername"; then
  echo "Server is not currently running!"
  exit 1
fi
echo "stopping server..."
screen -Rd serverName -X stuff "stop$(printf '\r')"
echo "done!"