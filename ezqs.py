#!/usr/bin/python3
# elementZero minecraft bedrock server setup script by Tuxinal
import urllib.request
import os.path
import zipfile
import subprocess
def findWindowsLink():
    if os.path.exists("./version.html"):
        os.remove("./version.html")
    urllib.request.urlretrieve("https://minecraft.net/en-us/download/server/bedrock/","./version.html")
    # would be a bit nicer if this wasn't bash code
    link = subprocess.Popen(["grep -o 'https://minecraft.azureedge.net/bin-win/[^\"]*' {}".format("./version.html")]
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
    for fileName in os.listdir(os.getcwd()):
        if fileName.startswith("ElementZero"):
            os.rename(fileName,serverName)
    print("done!")
print("checking for the latest minecraft version")
link, fileName = findWindowsLink()
if os.path.exists(fileName):
    print("\nlatest BDS is already downloaded!")
else:
    urllib.request.urlretrieve(link,fileName)
mc = zipfile.ZipFile(fileName)
mc.extractall(serverName)
fullDir = os.getcwd()+"/"+serverName
start = open("start.sh")
startServer = open(serverName+"/start.sh","w+")
startServer.write(start.read().replace("serverName",serverName).replace("dirName",fullDir))
if input("delete downloaded files? [y,N]") in ("Y","y"):
    print("deleting junk...")
    os.remove(fileName)
    os.remove("version.html")
    os.remove("ez.zip")
    print("done!")
