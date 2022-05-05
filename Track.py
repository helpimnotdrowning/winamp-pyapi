import win32api
from pathlib import Path

class Track:
    def __init__(self, filepath: Path) -> None:
        self.filepath = filepath
    
    def get_art(self) -> None: #image
        pass
    
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