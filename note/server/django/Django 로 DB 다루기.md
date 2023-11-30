# Django 로 DB 다루기

<br>

- 주로 디버깅 할 때 유용하게 사용할 수 있다.

<br>

1. 아래와 같이 작성한다.
   - django 를 시작할 때 꼭 필요한 환경변수를 설정하는 부분이다.

```python
import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', '[내 프로젝트 이름].settings')
django.setup()
```

- django 프로젝트의 위치를 알려주는 환경변수를 지정
- `django.setup()` 명령어로 django 환경을 불러온다.
- django 프로젝트의 구성요소들을 외부 스크립트에서 불러오고 조작할 수 있다.

<br>

2. shell_plus 를 실행했을 때 실행되는 패키지들을 파이썬 파일에 복붙한다.
   - 내 컴퓨터의 경우 아래와 같이 로드된다.

```python
import os
import django

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "config.settings")
django.setup()



# Shell Plus Model Imports
from django.contrib.admin.models import LogEntry
from django.contrib.auth.models import Group, Permission, User
from django.contrib.contenttypes.models import ContentType
from django.contrib.sessions.models import Session
from todo.models import Todo

# Shell Plus Django Imports
from django.core.cache import cache
from django.conf import settings
from django.contrib.auth import get_user_model
from django.db import transaction
from django.db.models import Avg, Case, Count, F, Max, Min, Prefetch, Q, Sum, When
from django.utils import timezone
from django.urls import reverse
from django.db.models import Exists, OuterRef, Subquery

from todo.models import *
```

