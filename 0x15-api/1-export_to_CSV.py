#!/usr/bin/python3
"""Returns to-do list information for a given employee ID."""
import requests
from sys import argv

url = 'https://jsonplaceholder.typicode.com'
users = requests.get('{}/users/{}'.format(url, argv[1])).json()
userId = users.get('id')

todos = requests.get('{}/todos'.format(url)).json()
todos = list(filter(lambda x: x.get('userId') == userId, todos))
comp_todos = list(filter(lambda x: x.get('completed'), todos))

empName = users.get("name")
print("Employee {} is done with ({}/{})".format(
    empName, len(comp_todos), len(todos)))
for todo in comp_todos:
    print("\t {}".format(todo.get('title')))


