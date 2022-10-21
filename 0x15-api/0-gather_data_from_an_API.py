#!/usr/bin/python3
"""Returns to-do list information for a given employee ID."""
import requests
from sys import argv

if __name__ == "__main__":
    url = 'https://jsonplaceholder.typicode.com'
    users = requests.get('{}/users/{}'.format(url, argv[1])).json()
    userId = users.get('id')

    todos = requests.get(
        '{}/todos'.format(url),
        params={'userId': userId}).json()

    completed = list(filter(lambda x: x.get('completed'), todos))

    empName = users.get("name")
    print("Employee {} is done with tasks({}/{}):".format(
        empName, len(completed), len(todos)))
    [print("\t {}".format(todo.get('title'))) for todo in completed]
