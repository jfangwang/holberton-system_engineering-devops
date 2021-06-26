#!/usr/bin/python3
"""Querying the Reddit API"""

import requests

def number_of_subscribers(subreddit):
    """Returns Number of Subs"""
    url = "https://www.reddit.com/r/{}/about.json".format(subreddit)
    h = {
        'User-Agent': 'Python/1.0(Holberton Project)'
    }
    req = requests.get(url, headers=h)

    try:
        return req.json()['data']['subscribers']
    except:
        return 0
