import json JSON_FILE_PATH: '/home/agr/work/learn/otus/test_da
from files import JSON_FILE_PATH

with open(JSON_FILE_PATH) as f:    <_io.TextIOWrapper name='/h
users = json.load(f) users: <class 'dict'>: {'users': [{'n
users_list = users['users']

for user in users_list:
    print(user)