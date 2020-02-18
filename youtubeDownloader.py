import pytube
import os

class youtubeDownloader():

    def askYoutubeLink():
        link = input("Youtube Link: ")
        if("youtube" in link):
            return link
        else:
            return "Youtube Link needed"

    def on_progress(stream, chunk, file_handle, bytes_remaining):
        total_size = stream.filesize
        bytes_downloaded = total_size - bytes_remaining
        percentage_of_completion = bytes_downloaded / total_size * 100
        print(percentage_of_completion)

    def getHighRes(link):
        ytube_video = pytube.YouTube(link)
        highResVideo = ytube_video.streams.filter(progressive=True).order_by('resolution').desc().first()
        return highResVideo

    def getAudioOnly(link):
        video = pytube.YouTube(link)
        audioOnly = video.streams.filter(only_audio=True).all()
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
