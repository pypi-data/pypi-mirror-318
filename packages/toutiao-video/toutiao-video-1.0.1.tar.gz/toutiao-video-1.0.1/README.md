# Download videos from toutiao.com

## Installation

```bash
python3 -m pip install toutiao-video
```

## Usage

### Use in CMD
```bash
toutiao --help

# download videos from user feed
toutiao feed -u xxxxx -t xxxxx
toutiao feed -u xxxxx -t xxxxx -O output
toutiao feed -u xxxxx -t xxxxx -l 5
toutiao feed -u xxxxx -t xxxxx -l 1 -d 1080p
toutiao feed -u xxxxx -t xxxxx -l 10 --dryrun

# download video from video url
toutiao video -t xxxxx <video_url>
toutiao video -t xxxxx <video_url> -d 1080p
toutiao video -t xxxxx <video_url> -d 1080p -O output
toutiao video -t xxxxx <video_url> -d 1080p -O output --dryrun
```

### Use in Python

```python

# download videos from user feed
from toutiao.core import TouTiao

toutiao = TouTiao(user_id='user_id', tt_webid='tt_webid')

for n, item in enumerate(toutiao.list_user_feed(), 1):
    if n > 5:
        break()
    print(item)       

# download video from video url
from toutiao.video import ToutiaoVideo
video = ToutiaoVideo(url='<your_video_url>', ttwid='<your_ttwid>')
initial_video = video.get_initial_video()
print(initial_video)
# video.download()
```


## Help

- `tt-webid` and `ttwid`
you can get the value from `Network > Request Headers > Cookie` or `Application > Cookies` on your browser.
