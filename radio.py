import vlc
import time
import threading
import urllib.request

class RadioPlayer:
    def __init__(self):
        self.instance = vlc.Instance()
        self.player = self.instance.media_player_new()
        self.stations = {
            'kexp': "https://kexp.streamguys1.com/kexp160.aac",
            'wmse': "https://wmse.streamguys1.com/wmselivemp3",
            'kxry': "https://listen.xray.fm/stream",
            'kcrw': "https://media.kcrw.com/pls/kcrwsimulcast.pls"
        }
        self.current_station = 'kexp'  # Default station
        self.is_playing = False
        
    def get_stream_url(self, url):
        if url.endswith('.pls'):
            try:
                with urllib.request.urlopen(url) as response:
                    pls_content = response.read().decode('utf-8')
                for line in pls_content.split('\n'):
                    if line.startswith('File1='):
                        return line.split('=')[1].strip()
            except Exception as e:
                print(f"Error parsing PLS file: {e}")
                return url
        return url
        
    def play(self, station=None):
        if station:
            if station in self.stations:
                if self.is_playing:
                    self.stop()  # Stop current stream before switching
                self.current_station = station
            else:
                print(f"Station '{station}' not found")
                return
                
        stream_url = self.get_stream_url(self.stations[self.current_station])
        media = self.instance.media_new(stream_url)
        self.player.set_media(media)
        self.player.play()
        self.is_playing = True
        print(f"Playing {self.current_station.upper()}...")
        
    def stop(self):
        self.player.stop()
        self.is_playing = False
        print("Stopped")
        
    def set_volume(self, volume):
        self.player.audio_set_volume(volume)
        print(f"Volume set to {volume}%")
        
    def list_stations(self):
        print("\nAvailable stations:")
        for station in self.stations.keys():
            print(f"- {station.upper()}")

def handle_commands(radio):
    while True:
        command = input("\nEnter command (play/stop/volume/stations/quit): ").lower().strip()
        if command == 'play':
            stations_list = ', '.join(radio.stations.keys())
            station = input(f"Enter station ({stations_list}) or press Enter for current station: ").lower().strip()
            radio.play(station if station else None)
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
        elif command == 'stations':
            radio.list_stations()
        elif command == 'quit':
            radio.stop()
            break
        else:
            print("Unknown command")

if __name__ == "__main__":
    radio = RadioPlayer()
    handle_commands(radio)
