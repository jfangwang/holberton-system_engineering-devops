#!/usr/bin/python3
import requests
from sys import argv
import json

if __name__ == "__main__":
    url = "https://jsonplaceholder.typicode.com/users"
    r = requests.get(url).json()
    name = "Willy"
    task_count = 0
    task_completed = 0
    mega_dict = {}
    # Get the user name with user id
    for item in r:
        url = "https://jsonplaceholder.typicode.com/users"
        r = requests.get(url).json()
        user_id = str(item['id'])
        user_name = str(item['username'])
        # Get Data
        url = "https://jsonplaceholder.typicode.com/todos"
        r = requests.get(url).json()
        temp_dict = {}
        willy_list = []
        for d in r:
            # Titles, Completed, Username
            temp_dict = {}
            temp_dict['task'] = d['title']
            temp_dict['username'] = user_name
            temp_dict['completed'] = d['completed']
            willy_list.append(temp_dict)
        mega_dict[user_id] = willy_list
    with open('todo_all_employees.json', 'w') as json_file:
        json.dump(mega_dict, json_file)
