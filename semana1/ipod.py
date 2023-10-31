class Song:
    def __init__(self, name, time, artist):
        self.name = name
        self.time = time
        self.artist = artist

    def music_detail(self):
        print(f"Just on time u can heard the song: {self.name} Artist {self.artist} Time {self.time} seconds of duration")

class MusicPlayer:
    def __init__(self):
        self.is_playing = False
        self.volume = 50
        self.playing_queue = []
        self.current_song = ""

    def play_playlist(self, playlist):
        self.playing_queue = playlist
        # ciclo para reproducir --
        if self.playing_queue:
            song = self.playing_queue[0]
            self.play(song)

    def play_single_song(self, song):
        self.playing_queue.append(song)
        self.play(song)

    def play(self, song):
        self.is_playing = True
        self.current_song = song

    def show_status(self):
        if self.is_playing:
            self.current_song.show_details()
        else:
            print("No music is playing")

    def pause(self):
        self.is_playing = False


    def play_next_song(self): # No cambiar atributos
        if self.playing_queue:
            next_song = self.playing_queue.pop(0)
            self.play(next_song)
        else:
            self.pause()

    def play_prev_song(self):  # No cambiar atributos
        if self.playing_queue:
            prev_song = self.playing_queue.pop()
            self.playing_queue.insert(0, self.current_song)
            self.play(prev_song)
        else:
            self.pause()

# change_volume
   
    def change_volume (self, choose_volume):
            if choose_volume >= 0 and choose_volume <= 100:
                self.volume = choose_volume
                print(f"the new volume is:", choose_volume)
            else:
                raise ValueError("the volume state right now is: MUTE")   






music_player = MusicPlayer()

music_player.change_volume(105)

print(music_player.volume)
