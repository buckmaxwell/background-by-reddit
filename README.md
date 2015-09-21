# BackgroundByReddit

## Installation (Mac)

**Important.  All photos the ~/Pictures folder will be deleted.  Please move photos you care about to another location before using.** 

### 1. Clone the repo and install requirements
```sh
$ git clone https://github.com/buckmaxwell/background-by-reddit.git
$ cd background-by-reddit
$ pip install -r requirements.txt
```
### 2. Add your username
open reddit background.py in your text editor of choice change 
```python
username = 'INSERT USERNAME HERE'
```
to your username.

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

### 4. Configure settings for background

 1. Right click on desktop background
 2. Select "change desktop background"
 3. Under folders select Pictures
 4. Select the first and click "Change Picture"
 5. Set drop down menu to "5 seconds"
 6. Add a photo or rename a picture in the ~/Picture folder to 'default.jpg'
 

## Installation (Linux)

### Clone the repository and install the crontab

**Important.  All photos the pictures_path folder will be deleted.  Please move photos you care about to another location before using.** 

For the most part the Mac steps should work. But do the following.  In redditbackground.py change pictures_path = '/Users/\<u>/Pictures' to your local picture folder path.

### 1. 
Same as Mac.

### 2. 
open reddit background.py in your text editor of choice change 

```python
pictures_path = '/Users/<u>/Pictures'.format(u=username)
```
to
```python
pictures_path = '/Whatever/path/you/want'
```

### 3. 

Same as Mac.

### 4. 

You gotta figure this out on your own.  If someone does it, please let me know your steps!
 





