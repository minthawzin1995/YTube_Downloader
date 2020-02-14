# Imports used in this youtube downloader project
import pytube

# Ask for user input for the youtube video Link
def askLink():
    youtubeLink = input("Youtube Link: ")
    return youtubeLink;

if __name__ == '__main__':
    link = askLink();
    print(link);
