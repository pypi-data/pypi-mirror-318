import click

from toutiao import version_info
from toutiao.core import TouTiao
from toutiao.video import ToutiaoVideo


CONTEXT_SETTINGS = dict(
    help_option_names=['-?', '-h', '--help'],
    max_content_width=200,
)

__epilog__ = click.style('contact: {author} <{author_email}>', fg='cyan').format(**version_info)
@click.group(
    name=version_info['prog'],
    help=click.style(version_info['desc'], italic=True, fg='cyan', bold=True),
    context_settings=CONTEXT_SETTINGS,
    no_args_is_help=True,
    epilog=__epilog__,
)
def cli():
    pass


__epilog__ = click.style('''
\n\b
examples:
    {prog} feed -u xxxxx -t xxxxx
    {prog} feed -u xxxxx -t xxxxx -O output
    {prog} feed -u xxxxx -t xxxxx -l 5
    {prog} feed -u xxxxx -t xxxxx -l 1 -d 1080p
    {prog} feed -u xxxxx -t xxxxx -l 10 --dryrun
''', fg='yellow').format(**version_info)
@cli.command(
    help=click.style('download videos from user feed', fg='green'),
    epilog=__epilog__,
    no_args_is_help=True,
)
@click.option('-u', '--user-id', help='the user_id (token)', required=True)
@click.option('-t', '--tt-webid', help='the tt_webid in cookies', required=True, envvar='TT_WEBID', show_envvar=True)
@click.option('-O', '--outdir', help='output directory', default='download', show_default=True)
@click.option('-d', '--definition', help='the video definition to download', default='720p')
@click.option('-l', '--limit', help='the max number of videos to download', type=int, default=1, show_default=True)
@click.option('--dryrun', help='dryrun mode', is_flag=True)
@click.version_option(version=version_info['version'], prog_name=version_info['prog'])
def feed(user_id, tt_webid, outdir, definition, limit, dryrun):

    toutiao = TouTiao(user_id=user_id, tt_webid=tt_webid)

    for n, item in enumerate(toutiao.list_user_feed(), 1):
        print(n, item['title'])

        if dryrun:
            toutiao.show_video_list(item, definition=definition)
        else:
            toutiao.download(item, definition=definition, outdir=outdir)

        if n >= limit:
            break


__epilog__ = click.style('''
\n\b
examples:
    {prog} video -t xxxxx <video_url>
    {prog} video -t xxxxx <video_url> -d 1080p
    {prog} video -t xxxxx <video_url> -d 1080p -O output
    {prog} video -t xxxxx <video_url> -d 1080p -O output --dryrun
''', fg='yellow').format(**version_info)
@cli.command(
    help=click.style('download video from url', fg='green'),
    epilog=__epilog__,
    no_args_is_help=True,
)
@click.option('-t', '--ttwid', help='the ttwid in cookies', required=True, envvar='TTWID', show_envvar=True)
@click.option('-O', '--outdir', help='output directory', default='download', show_default=True)
@click.option('-d', '--definition', help='the video definition to download', default='720p')
@click.option('--dryrun', help='dryrun mode', is_flag=True)
@click.argument('url')
def video(ttwid, url, outdir, definition, dryrun):
    video = ToutiaoVideo(url=url, ttwid=ttwid)
    video.download(definition=definition, outdir=outdir, dryrun=dryrun)


def main():
    cli()


if __name__ == '__main__':
    main()
