import vlc
import time
import threading

class RadioPlayer:
    def __init__(self):
        self.instance = vlc.Instance()
        self.player = self.instance.media_player_new()
        self.stream_url = "https://kexp.streamguys1.com/kexp160.aac"
        self.is_playing = False
        
    def play(self):
        if not self.is_playing:
            media = self.instance.media_new(self.stream_url)
            self.player.set_media(media)
            self.player.play()
            self.is_playing = True
            print("Playing...")
        
    def stop(self):
        self.player.stop()
        self.is_playing = False
        print("Stopped")
        
    def set_volume(self, volume):
        self.player.audio_set_volume(volume)
        print(f"Volume set to {volume}%")

def handle_commands(radio):
    while True:
        command = input("\nEnter command (play/stop/volume/quit): ").lower().strip()
        if command == 'play':
            radio.play()
        elif command == 'stop':
            radio.stop()
        elif command == 'volume':
            try:
                vol = int(input("Enter volume (0-100): "))
                if 0 <= vol <= 100:
                    radio.set_volume(vol)
                else:
                    print("Volume must be between 0 and 100")
            except ValueError:
                print("Please enter a valid number")
        elif command == 'quit':
            radio.stop()
            break
        else:
            print("Unknown command")

if __name__ == "__main__":
    radio = RadioPlayer()
    handle_commands(radio)
