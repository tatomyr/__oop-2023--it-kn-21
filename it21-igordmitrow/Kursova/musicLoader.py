import os
from mutagen.easyid3 import EasyID3, ID3
from PIL import Image, ImageTk
from mutagen.mp3 import MP3

SAVE_PATH = os.path.dirname(__file__)

class MusicLoader:
    """
    A class to load music from a file
    Can load a bunch of songs from a directory
    Extracts metadata from the music
    """
    def __init__(self, path=SAVE_PATH):
        self.path = path

    

    def load_tracks(self):
        music_data = []
        for file in os.listdir("songs"):
            if file.endswith(".mp3"):
                music_data.append(os.path.join("songs", file))
        return music_data

    def get_metadata(self, filename):
        audio = EasyID3(self.path + '/' + filename)
        metadata = {}
        metadata['title'] = audio.get('title', ['Unknown Title'])[0]
        metadata['artist'] = audio.get('artist', ['Unknown Artist'])[0]
        metadata['album'] = audio.get('album', [''])[0]
        metadata['year'] = audio.get('date', [''])[0]
        metadata['genre'] = audio.get('genre', [''])[0]
        metadata['cover'] = self.create_cover(filename)
        metadata['duration'] = MP3(filename).info.length
        return metadata
    
    def create_cover(self, file_path):
        filename = file_path.replace('.mp3', '').replace('songs/', 'songs/cover/')
        audioFile = ID3(file_path)
        try:
            cover = audioFile.getall("APIC")[0].data
            fb = open(filename + '.png', 'wb')
            fb.write(cover)
            fb.close()
            return filename + '.png'
        except Exception as e:
            return None

    def get_album_cover(self, file_path):
        image = Image.open(self.create_cover(file_path))
        image = image.resize((200, 200))
        python_image = ImageTk.PhotoImage(image)
        return python_image
        