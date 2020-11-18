from unittest import TestCase
from shoutcast_api.tunein import (
    Track, TrackList, get_stations_stream_url, tunein_to_station
)
from shoutcast_api.shoutcast_request import tuneins


class TestTunein(TestCase):
    def test_get_stations_stream_url(self):
        response = get_stations_stream_url(station_id=99311623)
        self.assertIsInstance(response, TrackList)
        if len(response.tracks) > 0:
            track = response.tracks[0]
            self.assertIsInstance(track, Track)

    def test_tunein_to_station(self):
        response = tunein_to_station(base=tuneins[0], station_id=99466001)
        self.assertIsInstance(response, str)
