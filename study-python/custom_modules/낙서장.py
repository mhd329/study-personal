'''from datetime import datetime

def get_logFileName():
    now = datetime.now()
    now = str(now).split(" "|".")[-2]
    filename = now + ".log"
    return filename

print(get_logFileName())'''

import re

source = r'Luke Skywarker 02-123-4567 luke@daum.net\nasd\n\n'
print(source)

m1 = re.findall('\w', source)
m2 = re.findall('\w+', source)
m3 = re.findall('.*', source)
m4 = re.findall(r'.*', source)
m5 = re.findall(".*'", source)
m6 = re.findall("[.*']", source)
m7 = re.findall(".+", source)
m8 = re.findall(r'/w', source)
print("m1 : ", m1)
print("m2 : ", m2)
print("m3 : ", m3)
print("m4 : ", m4)
print("m5 : ", m5)
print("m6 : ", m6)
print("m7 : ", m7)
print("m8 : ", m8)







'''str1 = "C:\nProgram Files\nexample\n.asd"
str2 = r"C:\nProgram Files\nexample\n.asd"

print(str1)
print(str2)'''

matchObj = re.match(
    r'(?P<year>\d{4})-(?P<month>\d\d)-(?P<day>\d\d) (?P=year)\.\2\.\3',
    '2018-07-28 2018.07.28')

print(matchObj.group())

print(re.sub('https?://\S+',
             '[링크](\g<0>)',
             'http://www.google.com and https://greeksharifa.github.io'))

print(re.sub('https?://www\S+',
             '[링크](\g<0>)',
             'http://www.google.com and https://greeksharifa.github.io'))