import os
import json
import urllib
from webrequests import WebRequest as WR


class ToutiaoVideo(object):
    """Video downloader for Toutiao

    Options:
        url: video url, like '7136207326266728712' or 'https://www.toutiao.com/video/7136207326266728712/'
        ttwid: get it from request headers on your browser
    """
    def __init__(self, url, ttwid):
        self.cookies = {'ttwid': ttwid}
        self.url = self.check_url(url)

    def check_url(self, url):
        if url.startswith('https:'):
            return url
        return f'https://www.toutiao.com/video/{url}/'

    def get_initial_video(self):
        soup = WR.get_soup(self.url, cookies=self.cookies)
        text = soup.select_one('#RENDER_DATA').text
        data = json.loads(urllib.parse.unquote(text))
        initial_video = data['data']['initialVideo']
        return initial_video
    
    def download(self, definition=None, outfile=None, outdir=None, dryrun=False):
        initial_video = self.get_initial_video()
        video_list = initial_video['videoPlayInfo']['video_list']
        for video in video_list:
            if definition == video['video_meta']['definition']:
                break

        definition = definition or video['video_meta']['definition']
        main_url = video['main_url']
        title = initial_video['title']
        outfile = outfile or title + '.mp4'
        if outdir:
            outfile = os.path.join(outdir, outfile)
        if dryrun:
            print('definition:', definition)
            print('outfile:', outfile)
            print('main_url:', main_url)
        else:
            WR.download(main_url, outfile)


if __name__ == '__main__':
    url = 'https://www.toutiao.com/video/7455505335042703923/'
    ttwid = '1%7CHfGA7xhwGip4hLYYJLXeA-doleVw9P-MwfwkC826B3Q%7C1735888745%7Ccadb54832432a99a108738ccee0396727b0a1392623a20134c1b4e28eebcd619'
    video = ToutiaoVideo(url, ttwid)
    # video.download()
    video.download(definition='720p')