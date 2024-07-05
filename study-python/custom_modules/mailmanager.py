import smtplib
import filemanager

def main():
     sender = "mhd329"+"@naver.com" # 보내는 사람
     receiver = "mhd329"+"@naver.com" # 받는 사람
     username = "mhd329" # 아이디
     password = "gusehd!@qw34ER5^" # 비밀번호

     log = open(filemanager.get_logFilePath(filemanager.get_logFileName()), mode = "r", encoding = "utf-8").read().encode()
     server = smtplib.SMTP('smtp.naver.com:587')
     server.starttls()
     server.login(username, password)
     server.sendmail(sender, receiver, log)
     server.quit()