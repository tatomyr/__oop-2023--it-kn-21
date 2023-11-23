import os
import yt_dlp

SAVE_PATH = os.path.dirname(__file__) + '/songs'


class Downloader():
    def download_audio(self, track, save_path):
        pass

class DeezerDownloader(Downloader):
    def download_audio(self, track, save_path=SAVE_PATH):
        try:
            return save_path + '/' + track["download"](save_path, quality='MP3_320')
        except Exception as e:
            print(f"Failing to download {track['title']} - {track['artist']['name']}")
            return False
        
class YoutubeDownloader(Downloader):
    def __init__(self) -> None:
        ydl_opts = {"cachedir": False, "cookiefile": "cookies.txt", 'restrictfilenames': True, 'outtmpl': 'songs/%(id)s.%(ext)s', 'writethumbnail': True, 'postprocessors': [{'key': 'FFmpegExtractAudio','preferredcodec': 'mp3','preferredquality': '192'}, {'key': 'EmbedThumbnail'}, {'key': 'FFmpegMetadata'}]}
        self.ydl = yt_dlp.YoutubeDL(ydl_opts)

    def download_audio(self, link):
        try:
            self.ydl.download([link])
            return True
        except Exception as e:
            print(f"Failing to download {link}")
            return False
    
class SpotifyDownloader(Downloader):
    def download_audio(self, track, save_path=SAVE_PATH):
        pass
