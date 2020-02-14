import pytube

class YoutubeDownloader():
    def askLink():
        link = input("Youtube Link: ")
        return link

if __name__ == '__main__':
    print(YoutubeDownloader.askLink())
