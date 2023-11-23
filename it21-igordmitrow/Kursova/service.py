from pydeezer import Deezer
from downloader import DeezerDownloader, YoutubeDownloader
import os

class MusicService():
    def __init__(self) -> None:
        self.downloader = None

    def search_music(self, query: str) -> list:
        """
        Search for music based on the query
        @param query: The query to search for
        @return: A list of results
        """
        pass

    def get_audio_url(self, track_id: str) -> str:
        """
        Get the audio URL for a track
        @param track_id: The ID of the track
        @return: The URL of the track
        """
        pass


class YoutubeService(MusicService):
    def __init__(self) -> None:
        super().__init__()
        self.downloader = YoutubeDownloader()
    
    def start_downloading(self, selected_track):
        return self.downloader.download_audio(selected_track)

class DeezerService(MusicService):
    def __init__(self) -> None:
        super().__init__()
        self.deezer = Deezer()
        arl = os.environ.get('DEEZER')
        self.deezer.login_via_arl(arl)
        self.downloader = DeezerDownloader()

    def search_music(self, query) -> list:
        searchs = self.deezer.search_tracks(query)
        return searchs
 
    def start_downloading(self, selected_track, t='track'):
        try:
            if t == 'id':
                track = self.deezer.get_track(selected_track)
            else:
                track = self.deezer.get_track(selected_track['id'])
            status = self.downloader.download_audio(track)
            return status
        except:
            return False