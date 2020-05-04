#!/usr/bin/python3
"""
Python script to export data in the CSV format.
"""
import csv
import requests
import sys

if __name__ == "__main__":

    data = sys.argv[1]

    employee = requests.get('https://jsonplaceholder.typicode.com/users/{}'.
                            format(data)).json()
    t = requests.get('https://jsonplaceholder.typicode.com/todos?userId={}'.
                     format(data)).json()

    with open('{}.csv'.format(data), 'w') as csvfile:
        writer = csv.writer(csvfile, delimiter=',',
                            quoting=csv.QUOTE_ALL)
        for complete in t:
            writer.writerow([data, employee.get('username'),
                            complete.get('completed'), complete.get('title')])
