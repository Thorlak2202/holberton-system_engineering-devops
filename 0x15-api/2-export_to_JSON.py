#!/usr/bin/python3
"""
Python script to export data in the JSON format.
"""
import json
import requests
import sys

if __name__ == "__main__":

    data = sys.argv[1]

    employee = requests.get('https://jsonplaceholder.typicode.com/users/{}'.
                            format(data)).json()
    t = requests.get('https://jsonplaceholder.typicode.com/todos').json()
    completed = []
    result = {}
    for k in t:
        if k.get('userId') == int(data):
            task_json = {"task": k.get('title'),
                         "completed": k.get('completed'),
                         "username": employee.get('username')}
            completed.append(task_json)
    result[data] = completed

    file = data + '.json'
    with open(file, mode='w') as f:
        json.dump(result, f)
