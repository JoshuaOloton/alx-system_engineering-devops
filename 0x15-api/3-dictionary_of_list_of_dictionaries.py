#!/usr/bin/python3
"""Returns to-do list information for a given employee ID."""
import json
import requests

if __name__ == "__main__":
    url = 'https://jsonplaceholder.typicode.com'
    users = requests.get('{}/users'.format(url)).json()

    with open("todo_all_employees.json", "w") as file:
        json.dump({user.get('id'): [
            {
                "task": todo.get("title"),
                "completed": todo.get("completed"),
                "username": user.get('username')
            } for todo in requests.get(
                '{}/todos'.format(url), params={'userId': user.get('id')}).json()
            ] for user in users}, file)
