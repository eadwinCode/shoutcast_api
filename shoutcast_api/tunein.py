from typing import List
from .models import Track, TrackList, Tunein
from .shoutcast_request import call_api_tunein, call_api_tunein_any


def get_stations_stream_url(station_id: int, session=None) -> TrackList:
    """
    Get station streaming url as List[Track]
    :param station_id: shoutcast station id
    :param session: request_cache session if available
    :return: class `TrackList`
    """
    tracks = []
    response = call_api_tunein(station_id, session=session)
    playlist = response.get('playlist')
    api_track_list = playlist.get('trackList')

    api_tracks = api_track_list.get('track', [])

    if not isinstance(api_tracks, list):
        return TrackList([Track(api_tracks)])

    for item in api_tracks:
        tracks.append(Track(item))

    return TrackList(tracks)


def tunein_to_station(base: Tunein, station_id: int, session=None) -> str:
    """

    :param base: value is taken from the tunein node and based on the playlist format required
    (as PLS, M3U and XSPF formats are supported)
    :param station_id: station id
    :param session: request_cache session if available
    :return: str
    """
    return call_api_tunein_any(base, station_id, session=session)
