import pytube

class youtubeDownloader():
    def askYoutubeLink():
        link = input("Youtube Link: ")
        if("youtube" in link):
            return link
        else:
            return "Youtube Link needed"

if __name__ == '__main__':
    print(youtubeDownloader.askYoutubeLink())
