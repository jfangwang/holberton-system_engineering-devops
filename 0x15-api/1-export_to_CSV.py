#!/usr/bin/python3
"""task 1"""
import csv
import requests
from sys import argv

if __name__ == "__main__":
    if len(argv) == 2:
        user_id = str(argv[1])
        url = "https://jsonplaceholder.typicode.com/users"
        r = requests.get(url).json()
        name = "Willy"
        task_count = 0
        task_completed = 0
        # Get the user name with user id
        for item in r:
            if str(item['id']) == user_id:
                user_name = str(item['username'])
        url = "https://jsonplaceholder.typicode.com/todos"
        r = requests.get(url).json()
        # Count tasks
        for item in r:
            if str(item['userId']) == user_id:
                task_count += 1
            if str(item['userId']) == user_id and\
               str(item['completed']) == 'True':
                task_completed += 1
        with open('2.csv', mode='w') as employee_file:
            employee_writer = csv.writer(employee_file,
                                         delimiter=',',
                                         quotechar='"',
                                         quoting=csv.QUOTE_ALL)
            for item in r:
                if str(item['userId']) == user_id:
                    employee_writer.writerow([user_id, user_name,
                                             str(item['completed']),
                                             str(item['title'])])
