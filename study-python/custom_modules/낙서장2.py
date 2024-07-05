import re
from datetime import datetime
import os
import getpass
from datetime import datetime

username = getpass.getuser()

now = datetime.now()
matchObj = re.match(
    r'(?P<year>\d{4})-(?P<month>\d{2})-(?P<day>\d{2}) (?P=year)\.(?P=month)\.(?P=day)',
    '2018-07-28 2018.07.28')

print(matchObj.group())
print(matchObj.groups())
print(matchObj.group(1))