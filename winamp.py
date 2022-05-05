from pathlib import Path
import win32api
import win32gui

from . import Track

class Winamp:
    def __init__(self) -> None:
        pass
    
    def _send_command(self, command: int):
        pass
    
    def pause(self) -> None:
        pass
    
    def play(self) -> None:
        pass
    
    def stop(self) -> None:
        pass
    
    def set_volume(self, volume: int) -> None:
        pass
    
    def get_volume(self) -> int:
        pass
    
    def mute(self) -> None:
        self.set_volume(0)
    
    def skip_to_next_track(self) -> None:
        pass
    
    def get_next_track(self, index: int = 0) -> None: # maybe return some type of Track object or something??
        pass
    
    def skip_to_previous_track(self) -> None:
        pass
    
    def get_previous_track(self, index: int = 0) -> None: # also maybe return Track object
        pass
    
    def seek(self, time: float) -> None:
        pass
    
    def get_playlist(self) -> None: # would a Playlist object just be a list of Tracks?
        pass
    