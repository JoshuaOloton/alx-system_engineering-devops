#!/usr/bin/python3
"""Returns to-do list information for a given employee ID."""
import json
import requests
import sys

if __name__ == "__main__":
    url = 'https://jsonplaceholder.typicode.com'
    users = requests.get('{}/users/{}'.format(url, sys.argv[1])).json()
    userId = users.get('id')
    username = users.get('username')
    todos = requests.get(
        '{}/todos'.format(url), params={'userId': userId}).json()

    empName = users.get("name")
    with open('{}.json'.format(userId), 'w') as file:
        json.dump({userId: [{
                "task": todo.get("title"),
                "completed": todo.get("completed"),
                "username": username
            } for todo in todos]}, file)
