# coding=utf-8

import pytube
import os
from progress.bar import Bar
from time import sleep
import progressbar
import time
from tqdm import tqdm

import sys

class youtubeDownloader():

    def askYoutubeLink():
        link = input("Youtube Link: ")
        if("youtube" in link):
            return link
        else:
            return "Youtube Link needed"

    def get_terminal_size():
        """Return the terminal size in rows and columns."""
        rows, columns = os.popen('stty size', 'r').read().split()
        return int(rows), int(columns)

    def display_progress_bar(bytes_received, filesize, ch='#', scale=0.55):
        _, columns = youtubeDownloader.get_terminal_size()
        max_width = int(columns * scale)

        filled = int(round(max_width * bytes_received / float(filesize)))
        remaining = max_width - filled
        bar = ch * filled + ' ' * remaining
        percent = round(100.0 * bytes_received / float(filesize), 1)
        text = "Downloading:{bar}:{percent}%\r".format(bar=bar, percent=percent)
        sys.stdout.write(text)
        sys.stdout.flush()

    def on_progress(stream, chunk, file_handle, bytes_remaining):
        filesize = stream.filesize
        bytes_received = filesize - bytes_remaining
        youtubeDownloader.display_progress_bar(bytes_received, filesize)

    def getHighRes(link):
        ytube_video = pytube.YouTube(link, on_progress_callback=youtubeDownloader.on_progress)
        highResVideo = ytube_video.streams.filter(progressive=True).order_by('resolution').desc().first()
        print("Fetching streams...")
        return highResVideo

    def getAudioOnly(link):

        video = pytube.YouTube(link, on_progress_callback=youtubeDownloader.on_progress)
        audioOnly = video.streams.filter(only_audio=True).all()
        print("Fetching streams...")
        return audioOnly[0]

if __name__ == '__main__':
    app = True
    while (app):
        link = youtubeDownloader.askYoutubeLink()
        type = input("Please enter v for video, a for audio only, e for exit\n")
        if (type == 'v'):
            video = youtubeDownloader.getHighRes(link)
            video.download("./DownloadedVideos/")
            print("Done!")

        elif (type == 'a'):
            audio = youtubeDownloader.getAudioOnly(link)
            audio.download("./DownloadedAudios/")
            print("Done!")

        elif (type == 'e'):
            break;
        else:
            continue;

    print("Done!")
