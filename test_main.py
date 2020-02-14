from youtubeDownloader import YoutubeDownloader
import unittest

class Test(unittest.TestCase):
    def testing(self):
        a = YoutubeDownloader.askLink()
        self.assertNotEqual(a, "hi")

if __name__ == '__main__':
    unittest.main()
