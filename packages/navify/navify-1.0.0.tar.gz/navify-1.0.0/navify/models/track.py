from dataclasses import dataclass, field
from typing import List, Optional, Self

from navify.utilities import clean_str, calculate_str_similarity, calculate_int_closeness

@dataclass
class Track:
    """Represents a single track."""

    title: str = field(default=None)
    """Title of the track."""
    
    album_name: Optional[str] = field(default=None)
    """Name of the album containing the track."""

    primary_artist: Optional[str] = field(default=None)
    """Primary (album) artist for the track."""

    additional_artists: List[str] = field(default_factory=list)
    """Additional artist names for the track."""

    duration_seconds: Optional[int] = field(default=None)
    """Duration of the track in seconds."""

    track_number: Optional[int] = field(default=None)
    """Track number on the album."""

    release_year: Optional[int] = field(default=None)
    """Year the track was released."""

    isrc: Optional[str] = field(default=None)
    """International Standard Recording Code for the track."""

    musicbrainz_id: Optional[str] = field(default=None)
    """MusicBrainz ID for the track."""
    
    service_id: Optional[str] = field(default=None)
    """Source-service specific ID for the track."""

    service_name: str = field(default='unknown')
    """Source service for the track."""

    service_data: Optional[dict] = field(default_factory=dict)
    """Raw JSON response data from the source service."""

    def __str__(self) -> str:
        return f"{self.track_number}. - {self.primary_artist} - {self.title}"
    
    def __repr__(self) -> str:
        return self.__str__()
    
    def __eq__(self, other: Optional[Self]) -> bool:
        if not other:
            return False
        
        return self.service_id == other.service_id and self.service_name == other.service_name
    
    def matches(self, other: Optional[Self], treshold: float = 0.6) -> bool:
        """
        Compares two tracks for equality, regardless of their source service.
        For primitive matching, use the __eq__ method (== operator).
        """

        if not other:
            return False

        variables = [
            calculate_str_similarity(clean_str(self.title), clean_str(other.title)), # title similarity
            calculate_str_similarity(clean_str(self.primary_artist), clean_str(other.primary_artist)), # primary/album artist similarity
            calculate_str_similarity(clean_str(self.album_name), clean_str(other.album_name)), # album name similarity
            calculate_int_closeness(self.duration_seconds, other.duration_seconds), # duration similarity
            calculate_int_closeness(self.track_number, other.track_number), # track number similarity
            calculate_int_closeness(self.release_year, other.release_year), # release year similarity
        ]

        similarity_ratio = sum(variables) / len(variables)

        return similarity_ratio >= treshold