from __future__ import unicode_literals
import youtube_dl
import requests
import sys

def download(artist, title):
    ytdl_opts = {
        'format': 'bestaudio/best',
        'outtmpl': artist + ' - ' + title,
    }
    # Get youtube link
    yt_link = youtube_dl.YoutubeDL(ytdl_opts).extract_info(
        'ytsearch1:' + artist + ' ' + title + ' audio',
        download=True
    )['entries'][0]['webpage_url']

def download_from_link(link, file_name):
    with open(file_name, "wb") as f:
        print("Downloading %s" % file_name)
        response = requests.get(link, stream=True)
        total_length = response.headers.get('content-length')

        if total_length is None: # no content length header
            f.write(response.content)
        else:
            dl = 0
            total_length = int(total_length)
            for data in response.iter_content(chunk_size=4096):
                dl += len(data)
                f.write(data)
                done = int(50 * dl / total_length)
                sys.stdout.write("\r[%s%s]" % ('=' * done, ' ' * (50-done)) )
                sys.stdout.flush()
            print("\n")