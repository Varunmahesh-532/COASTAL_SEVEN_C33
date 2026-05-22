class Camera:

    def take_photo(self):
        print("Taking Photo")

class MusicPlayer:

    def play_music(self):
        print("Playing Music")

class SmartPhone(Camera, MusicPlayer):

    def call(self):
        print("Calling....")

s1 = SmartPhone()
s1.take_photo()
s1.play_music()
s1.call()

