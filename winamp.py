from pathlib import Path
import win32api

class Track:
    def __init__(self, title, album) -> None:
        self.title = None
    
    def get_art(self) -> None: #image
    
    def get_artist(self) -> str:
        pass
    
    def get_title(self) -> str:
        pass
    
    def get_album(self) -> str:
        pass
    
    def get_length(self) -> float:
        pass
    
    def get_track_number(self) -> int:
        pass
    
    def get_genre(self) -> str:
        pass
    
    def set_rating(self, rating: int) -> None:
        pass
    
    def get_rating(self) -> int:
        pass
    
    def get_play_count(self) -> int:
        pass
    
    def get_last_played(self) -> str: # return date object?? later...
        pass
    
    def get_last_updated(self) -> str: # ^^^
        pass
    
    def get_year(self) -> int:
        pass
    
    def get_filename(self) -> Path:
        pass
    
    def get_comment(self) -> str:
        pass
    
    def get_filesize(self) -> int:
        pass
    
    def get_bitrate(self) -> int:
        pass
    
    def get_disc(self) -> int:
        pass
    
    def get_disk(self) -> int:
        return self.get_discs()
    
    def get_album_artist(self) -> str:
        pass
    
    def get_album_gain(self) -> float:
        pass
    
    def get_track_gain(self) -> float:
        pass
    
    def get_publisher(self) -> str:
        pass
    
    def get_composer(self) -> str:
        pass
    
    def is_podcast(self) -> bool:
        pass
    
    def get_podcast_channel(self) -> str:
        pass
    
    def get_podcast_publish_date(self) -> str:
        pass
    
    def get_bpm(self) -> int:
        pass
    
    def get_category(self) -> str:
        pass
    
    def get_director(self) -> str:
        pass
    
    def get_producer(self) -> str:
        pass
    
    def get_dimension(self) -> str: # ????????
        pass
    
    def get_date_added(self) -> str: # date
        pass

class winamp:
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
    