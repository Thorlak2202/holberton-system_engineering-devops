#!/usr/bin/python3
"""
Python script that takes in a URL and an email,
sends a POST request to the passed URL with the
email as a parameter, and displays the body of
the response
"""
import requests
import sys

if __name__ == "__main__":
    
    data = sys.argv[1]

    employee = requests.get('https://jsonplaceholder.typicode.com/users/{}'.
                            format(data)).json()
    tasks = requests.get('https://jsonplaceholder.typicode.com/todos?userId={}'.
                         format(data)).json()
    completed = []
    for complete in tasks:
        if complete.get('completed') is True:
            completed.append(complete.get('title'))

    print("Employee {} is done with tasks({}/{}):".format(employee.get('name'), len(completed),len(tasks)))
    for todo in completed:
        print("\t {}".format(todo))
