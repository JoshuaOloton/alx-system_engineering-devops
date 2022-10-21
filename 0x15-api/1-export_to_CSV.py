#!/usr/bin/python3
"""Returns to-do list information for a given employee ID."""
import csv
import requests
from sys import argv

if __name__ == "__main__":
    url = 'https://jsonplaceholder.typicode.com'
    users = requests.get('{}/users/{}'.format(url, argv[1])).json()
    userId = users.get('id')
    username = users.get('username')
    todos = requests.get(
        '{}/todos'.format(url), params={'userId': userId}).json()

    with open('{}.csv'.format(argv[1]), mode='w', newline='') as file:
        writer = csv.writer(file, quoting=csv.QUOTE_ALL)

        for todo in todos:
            writer.writerow(
                [userId, username, todo.get("completed"), todo.get("title")])
