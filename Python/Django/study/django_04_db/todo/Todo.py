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

# 01
# from datetime import date

# today_ = date.today().isoformat()
# Todo.objects.create(content="실습 제출", priority=5, deadline=today_)

# 02
# todo_list_02 = Todo.objects.order_by("id")
# for todo in todo_list_02:
#     print(todo.content)
#     print(todo.priority)
#     print(todo.completed)
#     print(todo.created_at)
#     print(todo.deadline)
#     print("#" * 50)
# 03
# todo_list_03 = Todo.objects.order_by("-deadline")
# print(todo_list_03)

# 04
# todo_list_04 = Todo.objects.order_by("-priority")
# print(todo_list_04)

# 05
# todo_list_05 = Todo.objects.filter(priority=5).order_by("id")
# print(todo_list_05)

# 06
# todo_list_06 = Todo.objects.filter(completed=True).order_by("id")
# print(todo_list_06)

# 07
# todo_list_07 = Todo.objects.filter(priority=5).count()
# print(todo_list_07)

# 08
# todo_list_08 = Todo.objects.get(id=1)
# print(todo_list_08)

# 09
# todo_list_08.delete()

# 10
# todo_list_10 = Todo.objects.get(id=10)
# todo_list_10.priority = 5
# todo_list_10.save()
# print(todo_list_10.priority)
