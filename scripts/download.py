from argparse import ArgumentParser
from yt_dlp import YoutubeDL

parser = ArgumentParser()
parser.add_argument('-u', '--url', type=str, required=True,
                    help='accepts video link')
parser.add_argument('-f', '--format', type=str, required=True,
                    default='mp4', help='the format is indicated (.mp4 or .mp3)')
args = parser.parse_args()

if 'mp4' in args.format:
    ydl_opts = {
        'outtmpl': f'../example/%(title)s.mp4',
        'format': 'bestaudio/best'
    }
else:
    ydl_opts = {
        'outtmpl': f'../example/%(title)s.mp3',
        'format': 'bestaudio/best'
    }

YoutubeDL(ydl_opts).download([args.url])
