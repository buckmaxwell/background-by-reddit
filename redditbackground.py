import requests
import urllib
import os
import time
from random import shuffle
from config import subreddits, pictures_path


headers = {"User-Agent": "backgroundbyreddit:v1.0.0 (by /u/wormywormm)"}

# Download new pictures
the_children = []
for subreddit in subreddits:
    resp = requests.get(f"https://www.reddit.com{subreddit}/new.json?raw_json=1")
    resp.raise_for_status()
    the_children += resp.json()["data"]["children"]
    time.sleep(2)

shuffle(the_children)  # mix up the order of the links

# Remove existing pictures except default.
pics = os.listdir(pictures_path)
pics_to_delete = [pic for pic in pics if pic[0] != "."]
pics_to_delete.pop()  # keep one picture so the directory is never empty
for filename in pics_to_delete:
    os.remove(f"{pictures_path}/{filename}")


for child in the_children:
    link = child["data"]["url"]
    extention = link.split(".")[-1]
    pid = child["data"]["id"]
    name_of_local_file = f"{pictures_path}/{pid}.{extention}"
    try:
        if not "com" in extention and len(extention) <= 4:
            urllib.urlretrieve(link, name_of_local_file)
    except Exception as e:  # sometimes the extention is not present, wrong, or wack
        print(e)
