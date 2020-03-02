import os
from unittest import TestCase
from shoutcast_api.stations import (
    StationList, Station, get_random_station, get_stations_keywords, get_stations_by_genre,
    get_stations_bitrate_or_genre_id, get_stations_by_now_playing, get_top_500
)

api_key = os.getenv('api_key')


class TestStations(TestCase):

    def test_get_top_500(self):
        response = get_top_500(api_key, limit=5, br=128)
        self.assertIsInstance(response, StationList)
        self.assertEqual(response.station[0].br, 128)

    def test_get_stations_by_now_playing(self):
        response = get_stations_by_now_playing(api_key, ct='john legend', limit=2)
        self.assertIsInstance(response, StationList)
        if len(response.station) > 0:
            self.assertTrue('john legend' in response.station[0].ct.lower())

    def test_get_stations_bitrate_or_genre_id(self):
        response = get_stations_bitrate_or_genre_id(api_key, br=128, genre_id=25, limit=2)
        self.assertIsInstance(response, StationList)
        self.assertEqual(response.station[0].br, 128)

    def test_get_stations_by_genre(self):
        response = get_stations_by_genre(api_key, genre='hip hop', limit=2)
        self.assertIsInstance(response, StationList)
        self.assertTrue('hip hop' in response.station[0].genre.lower())

    def test_get_stations_keywords(self):
        response = get_stations_keywords(api_key, search='Hot', br=128, limit=2)
        self.assertIsInstance(response, StationList)
        self.assertEqual(response.station[0].br, 128)

    def test_get_random_station(self):
        response = get_random_station(api_key, limit=2)
        self.assertIsInstance(response, StationList)

