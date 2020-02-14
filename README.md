[![Build Status](https://travis-ci.org/minthawzin1995/YTube_Downloader.svg?branch=master)](https://travis-ci.org/minthawzin1995/YTube_Downloader)
# YouTube Downloader

Simple Python application to download Youtube Videos. Implemented using Python,PyTube and Travis CI for integrated testing. The user can choose their desired outputs such as audio only, etc. in the command line interface. Audio only files will be saved in the directory of ./DownloadedAudios, while the video files will be saved in the directory of ./DownloadedVideos.

## Installation
1. Make sure to install the requirements.txt to get all the necessary packages for the project.
```
pip install -r requirements.txt
```

2. If you are building your own requirements.txt, you need to run this command instead.
```
pip freeze > requirements.txt
```

3. Install pytube library to access the youtube videos.
```
pip install pytube3
```

## Errors Encountered
1. KeyError: 'url_encoded_fmt_stream_map' 

Fixed are provided by https://github.com/nficano/pytube this github repository. Running the command below will install the fixed pytube package:
```
pip install git+git@github.com:nficano/pytube.git
```

2. Try to fix the mixins.py folder in the pytube directory with the following code for apply_descrambler function.
```
    import urllib.parse
    if key == 'url_encoded_fmt_stream_map' and not stream_data.get('url_encoded_fmt_stream_map'):
            formats = json.loads(stream_data['player_response'])['streamingData']['formats']
            formats.extend(json.loads(stream_data['player_response'])['streamingData']['adaptiveFormats'])
            try:
                stream_data[key] = [{u'url': format_item[u'url'],
                                     u'type': format_item[u'mimeType'],
                                     u'quality': format_item[u'quality'],
                                     u'itag': format_item[u'itag']} for format_item in formats]
            except:
                stream_data[key] = [{u'url': urllib.parse.unquote([url_item for url_item in format_item[u'cipher'].split("&") if "url=" in url_item][0].split("=")[1]),
                                      u'sp': urllib.parse.unquote([url_item for url_item in format_item[u'cipher'].split("&") if "sp=" in url_item][0].split("=")[1]),
                                      u's': urllib.parse.unquote([url_item for url_item in format_item[u'cipher'].split("&") if "s=" in url_item][0].split("=")[1]),
                                      u'type': format_item[u'mimeType'],
                                      u'quality': format_item[u'quality'],
                                      u'itag': format_item[u'itag']} for format_item in formats]
    else:
        stream_data[key] = [
            {k: unquote(v) for k, v in parse_qsl(i)}
            for i in stream_data[key].split(',')
        ]
    logger.debug(
        'applying descrambler\n%s',
        pprint.pformat(stream_data[key], indent=2),
    )
```

## Running the application
1. Run the youtubeDownloader.py using the followig command
```
py youtubeDownloader.py
```
2. Copy-paste the URL of the youtube Video in the user input.
3. Choose the desired output. V for video, A for audio only and E for exit
4. The end notification can be seen with a "Done!" message at the end of the command line.

