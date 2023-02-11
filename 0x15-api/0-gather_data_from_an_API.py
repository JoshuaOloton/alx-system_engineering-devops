#!/usr/bin/python3
"""Returns to-do list information for a given employee ID."""
import requests
from sys import argv

if __name__ == "__main__":
    base_url = "https://jsonplaceholder.typicode.com"
    id = argv[1]
    todos = requests.get("{}/todos".
                         format(base_url), params={"userId": id}).json()
    completed = list(filter(lambda todo: todo.get("completed"), todos))
    users = requests.get("{}/users/{}".format(base_url, id)).json()
    print("Employee {} is done with tasks({}/{}):".
          format(users.get("name"), len(completed), len(todos)))
    [print("\t {}".format(todo.get('title'))) for todo in completed]
