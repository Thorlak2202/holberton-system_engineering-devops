#!/usr/bin/python3
"""
Python script to export data in the JSON format.
"""
import json
import requests
import sys

if __name__ == "__main__":

    user = requests.get('https://jsonplaceholder.typicode.com/users').json()
    t = requests.get('https://jsonplaceholder.typicode.com/todos').json()
    result = {}
    for k in user:
        tasks = []
        for todo in t:
            if todo.get('userId') == k.get('id'):
                json_file = {"username": k.get('username'),
                             "task": todo.get('title'),
                             "completed": todo.get('completed')}
                tasks.append(json_file)
        result[k.get('id')] = tasks

    file = 'todo_all_employees' + '.json'
    with open(file, mode='w') as f:
        json.dump(result, f)
