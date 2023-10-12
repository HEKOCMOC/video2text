from argparse import ArgumentParser
from yt_dlp import YoutubeDL

parser = ArgumentParser()
parser.add_argument('--url', type=str, required=True)
args = parser.parse_args()

ydl_opts = {'outtmpl': '../video/%(title)s.mp4'}

YoutubeDL(ydl_opts).download([args.url])