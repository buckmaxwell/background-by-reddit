# BackgroundByReddit

## Installation

### 1. Clone the repo, install requirements, make BackgroundByReddit folder
```sh
$ git clone https://github.com/buckmaxwell/background-by-reddit.git
$
$ cd background-by-reddit
$ pip install -r requirements.txt
$
$ mkdir ~/BackgroundByReddit
$ mv default.jpg ~/BackgroundByReddit
$ 
```

### 2. Configure your settings
open config.py in your text editor of choice and configure your settings!
```python
###
# Fill out your username, if not on Mac make sure the path to BackgroundByReddit is correct -- do not use ~/
###

username = 'max' # => insert your personal computer username here
pictures_path = '/Users/{u}/BackgroundByReddit'.format(u=username) # => all pictures in this path will be deleted

###
# Configure subreddits 1-3 with your favorite picture heavy subreddits
#
# Suggestions:
#	/r/earthporn
#	/r/pics
#	/r/carporn
#	/r/teacuppigs
#	/r/bookporn
# 	/r/matureladiesboners
#   /r/wallpaper
#	/r/art
#	/r/pics
#
# Get creative!
#
###


subreddit1 = '/r/wallpaper' 
subreddit2 = '/r/art'
subreddit3 = '/r/pics'
```

### 3. Edit the crontab


```
$ crontab -e
```
This final command will open the crontab, presumably in vim.

 1. press 'i' 
 2. Add the following line to the file:
```sh
0,3,6,9,12,15,18,21,24,27,30,33,36,39,42,45,48,51,54,57	*	*	*	*	python <path>/<to>/background-by-reddit/redditbackground.py
```
 3. press 'esc'
 4. type 'ZZ'

### 4. Configure settings for background (this process will vary slightly for diffent Operating Systems)

 1. Right click on desktop background
 2. Select "change desktop background"
 3. Under folders select BackgroundByReddit -- if this is not there by default add the folder by clicking the + sign
 4. Select the first picture and click "Change Picture"
 5. Set drop down menu to "5 seconds" 
