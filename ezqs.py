#!/usr/bin/python3
# elementZero minecraft bedrock server setup script by Tuxinal
import urllib.request
import os.path
import zipfile
import subprocess
from getpass import getpass,getuser
def findWindowsLink():
    if os.path.exists("./version.html"):
        os.remove("./version.html")
    urllib.request.urlretrieve("https://minecraft.net/en-us/download/server/bedrock/","./version.html")
    # would be a bit nicer if this wasn't bash code
    link = subprocess.Popen(["grep -o 'https://minecraft.azureedge.net/bin-win/[^\"]*' version.html"]
        ,stdout=subprocess.PIPE,shell=True,universal_newlines=True)
    linkName = link.stdout.read().rsplit()[0]
    fileName = linkName.split("/")
    return linkName,fileName[4]
def inputYN(prompt):
    # input prompt with a yes/no
    while True:
        inputData = input(prompt+": ")
        if input(prompt+" = "+ inputData +" [Y,n]") in ("N","n"):
            continue
        else:
            break
    return inputData
serverName = inputYN("server name")
print("downloading elementZero...")
if not os.path.exists("./ez.zip"):
    # this clearly is not a good way too download the latest release
    # if you know a better method a pull request would be appreciated 
    urllib.request.urlretrieve("https://github.com/Element-0/ElementZero/releases/download/v0.1.0-6/ElementZero-v0.1.0-6-win64.zip","./ez.zip")
else:
    print("file already downloaded!")
    if input("do you want to redownload? [y,N]") in ("y", "Y"):
        urllib.request.urlretrieve("https://github.com/Element-0/ElementZero/releases/download/v0.1.0-6/ElementZero-v0.1.0-6-win64.zip","./ez.zip")
        print("done!")
if os.path.exists("./"+serverName):
    print("server folder already exists!")
else:
    ez = zipfile.ZipFile("./ez.zip")
    print("extracting...")
    ez.extractall()
    for BDSFileName in os.listdir(os.getcwd()):
        if BDSFileName.startswith("ElementZero"):
            os.rename(BDSFileName,serverName)
    print("done!")
print("checking for the latest minecraft version...")
link, BDSFileName = findWindowsLink()
if os.path.exists(BDSFileName):
    print("\nlatest BDS is already downloaded!")
else:
    urllib.request.urlretrieve(link,BDSFileName)
mc = zipfile.ZipFile(BDSFileName)
mc.extractall(serverName)
fullDir = os.getcwd()+"/"+serverName
if os.path.exists("./start.sh"):
    os.remove("./start.sh")
urllib.request.urlretrieve("https://raw.githubusercontent.com/tuxinal/ElementZeroQuickSetup/master/start.sh","start.sh")
start = open("start.sh")
startServer = open(serverName+"/start.sh","w+")
startServer.write(start.read().replace("servername",serverName).replace("dirname",fullDir))
if os.path.exists("./stop.sh"):
    os.remove("./stop.sh")
urllib.request.urlretrieve("https://raw.githubusercontent.com/tuxinal/ElementZeroQuickSetup/master/stop.sh","stop.sh")
stop = open("stop.sh")
stopServer = open(serverName+"/stop.sh","w+")
stopServer.write(stop.read().replace("serverName",serverName))
os.mkdir("./{}/downloads".format(serverName))
os.mkdir("./{}/backups".format(serverName))
if input("do you want to auto start your server?[Y,n]") in ("Y","y",""):
    serviceName = serverName+".service"
    urllib.request.urlretrieve("https://raw.githubusercontent.com/tuxinal/ElementZeroQuickSetup/master/minecraftbe.service",serviceName)
    serviceFile = open(serviceName,"r")
    serviceData = serviceFile.read().replace("servername",serverName).replace("dirname",fullDir).replace("replace",getuser())
    serviceFile.close()
    serviceFile = open(serviceName,"w")
    serviceFile.write(serviceData)
    serviceFile.close()
    while True:
        # this code is litrally put together with tape
        sudoPassword = getpass()
        passwordCheck = subprocess.Popen(["echo {} | sudo -S whoami".format(sudoPassword)],stdout=subprocess.PIPE,shell = True, text = True)
        try:
            user = passwordCheck.stdout.read().rsplit()[0]
        except:
            print("Error: password is probably wrong")
            continue
        break
    # enable systemd service
    subprocess.Popen(["sudo mv {} /etc/systemd/system/".format(serviceName)], shell = True).wait()
    subprocess.Popen(["sudo systemctl enable {}".format(serverName)], shell = True).wait()
if input("delete downloaded files? [y,N]") in ("Y","y"):
    print("deleting junk...")
    os.remove(BDSFileName)
    os.remove("version.html")
    os.remove("start.sh")
    os.remove("stop.sh")
    os.remove("ez.zip")
    print("done!")
