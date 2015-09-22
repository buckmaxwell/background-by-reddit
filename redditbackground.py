import requests
import urllib
import os
import time
from random import shuffle
from config import subreddit1, subreddit2, subreddit3, pictures_path


headers = {'User-Agent': 'backgroundbyreddit:v1.0.0 (by /u/wormywormm)'}
e_resp = requests.get('https://www.reddit.com{s1}/new.json?raw_json=1'.format(s1=subreddit1), headers=headers)
time.sleep(2)
a_resp = requests.get('https://www.reddit.com{s2}/new.json?raw_json=1'.format(s2=subreddit2), headers=headers)
time.sleep(2)
p_resp = requests.get('https://www.reddit.com{s3}/new.json?raw_json=1'.format(s3=subreddit3), headers=headers)


# Remove existing children except default.
pics = os.listdir(pictures_path)
pics_to_delete = [pic for pic in pics if pic[0] != '.']
pics_to_delete.pop() # keep one picture so the directory is never empty
for p in pics_to_delete:
	os.remove('{path}/{filename}'.format(path=pictures_path, filename=p))


# Download new ones
if e_resp.status_code == 200 and a_resp.status_code == 200 and p_resp.status_code ==200:
	the_children = a_resp.json()['data']['children'] + e_resp.json()['data']['children'] + p_resp.json()['data']['children']
	shuffle(the_children) # mix up the order of the links

	for child in the_children:
		link = child['data']['url']
		extention = link.split('.')[-1]
		pid  = child['data']['id']
		name_of_local_file = '{path}/{p_id}.{ext}'.format(path=pictures_path, p_id=pid, ext=extention)
		try:
			if not 'com' in extention and len(extention)<=4:
				urllib.urlretrieve(link, name_of_local_file)
		except Exception as e: # sometimes the extention is not present, wrong, or wack
			print e
