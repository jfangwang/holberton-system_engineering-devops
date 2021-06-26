#!/usr/bin/python3
"""Querying the Reddit API"""

import requests


def recurse(subreddit, hot_list=[], after='null'):
    """Returns Number of Subs"""
    url = "https://www.reddit.com/r/{}/hot.json".format(subreddit)
    h = {
        'User-Agent': 'Python/1.0(Holberton Project)'
    }
    after = {
        "after": after
    }
    req = requests.get(url, headers=h, allow_redirects=False, params=after)
    try:
        after = req.json()['data']['after']
        posts = req.json()['data']['children']
    except:
        return None

    for item in posts:
        hot_list.append(item['data']['title'])
    if after not in ["NULL", 'null', None, "None"]:
        return recurse(subreddit, hot_list, after)
    else:
        return hot_list
