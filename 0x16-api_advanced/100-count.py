#!/usr/bin/python3
"""Querying the Reddit API"""

import requests


def count_words(subreddit, word_list, after='null', count_list=[]):
    """Returns Number of Subs"""
    # Convert word_list to set to remove duplicates
    # temp = []
    # for w in word_list:
    #     temp.append(w.lower())
    # word_list = set(temp)
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

    # Gets all title names from Query
    for item in posts:
        title = item['data']['title'].lower()
        for word in word_list:
            if word.lower() in title:
                count_list.append(word.lower())
    if after not in ["NULL", 'null', None, "None"]:
        return count_words(subreddit, word_list, after, count_list)
    else:
        my_dict = {i: count_list.count(i) for i in count_list}
        print(my_dict)
        return count_list
