from youtubeDownloader import youtubeDownloader
import unittest

class Test(unittest.TestCase):
    def testing(self):
        a = youtubeDownloader.askYoutubeLink()
        self.assertNotEqual(a, "Youtube Link needed")

if __name__ == '__main__':
    unittest.main()
