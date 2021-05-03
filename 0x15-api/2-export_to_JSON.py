#!/usr/bin/python3
"""task 2"""
import json
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
        # Get Data
        url = "https://jsonplaceholder.typicode.com/todos"
        r = requests.get(url).json()
        mega_dict = {}
        temp_dict = {}
        willy_list = []
        for d in r:
            # Titles, Completed, Username
            if str(d['userId']) == user_id:
                temp_dict = {}
                temp_dict['task'] = d['title']
                temp_dict['username'] = user_name
                temp_dict['completed'] = d['completed']
                willy_list.append(temp_dict)
        mega_dict[user_id] = willy_list
        with open('{}.json'.format(user_id), 'w') as json_file:
            json.dump(mega_dict, json_file)
