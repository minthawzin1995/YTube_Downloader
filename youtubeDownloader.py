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

    def getListofStream(link):
        # parse into the pytube
        ytube_video = pytube.YouTube(link)
        getStreams = ytube_video.streams.all()
        return getStreams

    def getHighRes(streamList):
        # streams will return a list -> get_by_res first item
        downloadVideo = streamList[0]
        return downloadVideo

if __name__ == '__main__':
    link = youtubeDownloader.askYoutubeLink()
    streamList = youtubeDownloader.getListofStream(link)
    video = youtubeDownloader.getHighRes(streamList)

    # Download the video into the file path
    video.download("./DownloadedVideos/")
