#!/usr/bin/python3
"""
function that queries the Reddit API and returns
the number of subscribers
(not active users, total subscribers)
for a given subreddit.
"""
import requests


def number_of_subscribers(subreddit):
    subscribers = requests.get('https://www.reddit.com/r/{}/about.json'.
                               format(subreddit),
                               headers={"User-Agent": "Chris"},
                               allow_redirects=False)
    if subscribers.status_code != 200:
        return 0
    return subscribers.json().get("data").get("subscribers")
