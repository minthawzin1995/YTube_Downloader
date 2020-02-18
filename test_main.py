from youtubeDownloader import youtubeDownloader
import unittest

class Test(unittest.TestCase):

    testLink = "https://www.youtube.com/watch?v=07d2dXHYb94"

    def test_getListStream(self):
        # test link
        highRes = youtubeDownloader.getHighRes(self.testLink)
        self.assertNotEqual(highRes, [])

    def test_getAudioOnly(self):

        # test Link
        audio = youtubeDownloader.getAudioOnly(self.testLink)
        self.assertNotEqual(audio, [])

if __name__ == '__main__':
    unittest.main()
