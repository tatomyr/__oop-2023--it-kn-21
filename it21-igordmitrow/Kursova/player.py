import tkinter as tk
import pyglet
from musicLoader import MusicLoader

class MusicPlayer:
    def __init__(self, root=None):
        self.root = root
        if self.root is None:
            self.root = tk.Toplevel()
        self.root.title("Music Player")
        self.root.geometry("500x500")

        self.playlist = []
        self.current_track = None
        self.current_track_file = None

        self.album_cover_image = None
        self.album_cover_label = tk.Label(self.root)
        self.album_cover_label.pack()

        self.track_info_label = tk.Label(self.root, text="",font=("Helvetica",15,"bold"),bg="grey",fg="white",bd=5)
        self.track_info_label.pack()

        self.track_time_label = tk.Label(self.root, text="")
        self.track_time_label.pack()

        self.track_position_scale = tk.Scale(self.root, from_=0, to=100, orient="horizontal", command=self.set_track_position, showvalue=False)
        self.track_position_scale.set(0)
        self.track_position_scale.pack()

        self.control = tk.LabelFrame(self.root, width=200, height=100, border=0, pady=10)
        self.control.pack()

        self.previous_button = tk.Button(self.control, text="❮❮", command=self.previous_track)
        self.previous_button.grid(row=0,column=0)

        self.play_button = tk.Button(self.control, text="▶︎", command=self.play)
        self.play_button.grid(row=0, column=1)
        
        self.next_button = tk.Button(self.control, text="❯❯", command=self.next_track)
        self.next_button.grid(row=0, column=2)



        self.volume = tk.Label(self.root, text="Volume", justify="center")
        self.volume.pack()
        self.volume_scale = tk.Scale(self.root, from_=0, to=1, resolution=0.1, orient="horizontal", command=self.set_volume)
        self.volume_scale.set(1.0)
        self.volume_scale.pack()

        self.track_timer = None

        self.loader = MusicLoader()
        self.playlist = self.loader.load_tracks()
        print(self.playlist)
        self.load_current_track(self.playlist[0])

    def load_current_track(self, file_path):
        self.player = pyglet.media.Player()
        self.current_track = pyglet.media.load(file_path)
        self.current_track_file = file_path

        self.display_track_info()
        self.load_album_cover(file_path)

        self.player.queue(self.current_track)
        self.track_time_label.config(text="0:00")
        self.track_position_scale.set(0)
        self.track_position_scale["to"] = self.player.source.duration
        self.track_timer = self.root.after(1000, self.update_track_time)

    def play(self, force=False):
        if force:
            self.player.play()
            self.play_button.config(text="⏸")
            return
        if self.player is None:
            return
        if not self.player.playing:
            self.player.play()
            self.play_button.config(text="⏸")
        else:
            self.player.pause()
            self.play_button.config(text="▶︎")


    def set_volume(self, value):
        if self.current_track:
            self.player.volume = float(value)

    def update_track_time(self):
        if self.current_track:
            current_time = self.player.time
            total_time = self.player.source.duration

            if current_time >= total_time:
                self.next_track()
                self.play(True)
                return

            total_minutes = int(total_time // 60)
            total_seconds = int(total_time % 60)
            minutes = int(current_time // 60)
            seconds = int(current_time % 60)
            time_str = f"{minutes}:{seconds:02}/{total_minutes}:{total_seconds:02}"
            self.track_time_label.config(text=time_str)
            if self.player.source:
                total_time = self.player.source.duration
                if total_time > 0:
                    position = int(current_time)
                    self.track_position_scale.set(position)
            self.track_timer = self.root.after(1000, self.update_track_time)

    def set_track_position(self, value):
        if self.current_track:
            total_time = self.player.source.duration
            current_time = self.player.time
            if total_time > 0:
                new_position = int(value)
                if abs(new_position - current_time) > 2:
                    self.player.seek(new_position)

    def next_track(self):
        if self.playlist:
            current_index = self.playlist.index(self.current_track_file)
            if current_index < len(self.playlist) - 1:
                next_track_file = self.playlist[current_index + 1]
                self.load_current_track(next_track_file)
                self.play(True)
            else:
                self.load_current_track(self.playlist[0])
                self.play(True)

    def previous_track(self):
        if self.playlist:
            current_index = self.playlist.index(self.current_track_file)
            if current_index > 0:
                previous_track_file = self.playlist[current_index - 1]
                self.load_current_track(previous_track_file)
                self.play(True)
            else:
                self.load_current_track(self.playlist[-1])
                self.play(True)



    def display_track_info(self):
        metadata = self.loader.get_metadata(self.current_track_file)
        title, artist = metadata['title'], metadata['artist']
        self.track_info_label.labelText = f"Title: {title}\nArtist: {artist}" 
        self.track_info_label.config(text=self.track_info_label.labelText)

    def load_album_cover(self, file_path):
        python_image = self.loader.get_album_cover(file_path)
        if python_image:
            self.album_cover_label.config(image=python_image, width="200", height="200")
            self.album_cover_image = python_image
        else:
            self.album_cover_label.config(image=None)
            self.album_cover_image = None

    def run(self):
        self.root.mainloop()

if __name__ == "__main__":
    root = tk.Tk()
    player = MusicPlayer(root)
    root.mainloop()
