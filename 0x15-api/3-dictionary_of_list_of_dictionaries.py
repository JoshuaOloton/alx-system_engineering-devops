#!/usr/bin/python3
"""Returns to-do list information for a given employee ID."""
import json
import requests

if __name__ == "__main__":
    url = 'https://jsonplaceholder.typicode.com'
    users = requests.get('{}/users'.format(url)).json()

    with open("todo_all_employees.json", "w") as file:
        json.dump({
            u.get("id"): [{
                "task": todo.get("title"),
                "completed": todo.get("completed"),
                "username": u.get("username")
            } for todo in requests.get(url + "/todos",
                                       params={"userId": u.get("id")}).json()]
            for u in users}, file)
