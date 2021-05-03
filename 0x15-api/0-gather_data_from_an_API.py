#!/usr/bin/python3
"""task 0"""
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
                name = str(item['name'])
        url = "https://jsonplaceholder.typicode.com/todos"
        r = requests.get(url).json()
        # count tasks
        for item in r:
            if str(item['userId']) == user_id:
                task_count += 1
                if str(item['completed']) == 'True':
                    task_completed += 1
        print("Employee {} is done with tasks({}/{}):"
              .format(name, task_completed, task_count))
        # print out the tasks
        for item in r:
            if str(item['userId']) == user_id and\
               str(item['completed']) == 'True':
                print("\t {}".format(item['title']))
