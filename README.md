# ElementZeroQuickSetup
### a script for quickly setting up a minecraft BDS with ElementZero for linux


[Element Zero](https://github.com/Element-0/ElementZero) is a wine compatible modification to the windows bedrock dedicated server version with mod support 

this script is for automatically  setting up a minecraft BDS with ElementZero following [these](https://github.com/Element-0/ElementZero/wiki/Installing-using-docker-image-for-wine) instructions + some starting and stoping scripts and auto start (WIP)

this project is heavily inspired by [James A. Chamber](https://github.com/TheRemote)'s minecraft bedrock server [script](https://github.com/TheRemote/MinecraftBedrockServer)

## Dependencies
you need `docker`, `python` and `screen`

for `docker` check out the official [docs](https://docs.docker.com/engine/install/)

`python` is usually included in most distros

to install `screen` on ubuntu run:
```bash
sudo apt install screen
```
for other distros you have to figure it out yourself
## Usage
first download the script using wget:
```bash
wget https://raw.githubusercontent.com/tuxinal/ElementZeroQuickSetup/master/ezqs.py 
```
(you can also clone the repo if you really want 
to)

then just run it:
```bash
./ezqs.py
# OR
python3 ezqs.py
```
follow the instructions and you are done! 

there should be a new folder in the same directory that you ran the script `cd` into it and run `start.sh` and your server should be up and running!

## Work in progress
- [ ] automatic world backups upon starting
 
- [ ] check for updates upon starting
