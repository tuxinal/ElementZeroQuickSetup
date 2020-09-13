#!/usr/bin/bash
# Check if server is already started
if screen -list | grep -q "serverName"; then
    echo "Server is already started!  Press screen -r serverName to open it"
    exit 1
fi

cd dirName

echo "starting server to open use screen -r serverName"
screen -dmS serverName /bin/bash -c "docker run --rm -ti --name serverName -p 19132:19132/udp -v dirName/:/data codehz/wine:bdlauncher-runtime"