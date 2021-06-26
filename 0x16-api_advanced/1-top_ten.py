#!/usr/bin/python3
"""Querying the Reddit API"""

import requests


def top_ten(subreddit):
    """Returns Number of Subs"""
    url = "https://www.reddit.com/r/{}/hot.json".format(subreddit)
    h = {
        'User-Agent': 'Python/1.0(Holberton Project)'
    }
    req = requests.get(url, headers=h, allow_redirects=False)
    count = 0

    posts = req.json()['data']['children']
    if posts == []:
        print(None)
    else:
        try:
            for item in posts:
                if count < 10:
                    count = count + 1
                    print(item['data']['title'])
        except:
            print(None)
