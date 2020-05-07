#!/usr/bin/python3
"""
function that queries the Reddit API
and prints the titles of the first 10
hot posts listed for a given subreddit.
"""
import requests


def top_ten(subreddit):
    top = requests.get('https://www.reddit.com/r/{}/hot.json'.
                       format(subreddit),
                       headers={"User-Agent": "Chris"},
                       allow_redirects=False)
    info = top.json().get("data", {}).get("children", {})
    if top.status_code != 200:
        return print("None")
    for topten in info[:10]:
        print(topten.get("data", {}).get("title"))
