import os
from unittest import TestCase
from shoutcast_api.genres import (
 get_all_genres, get_primary_genres_json, get_genres_details_by_id,
 get_genres_by_sub_genres, GenreList, Genre, get_secondary_genres_json
)

try:
    import requests_cache
    import datetime

    expire_after = datetime.timedelta(days=3)
    session = requests_cache.CachedSession(cache_name='cache', backend='sqlite', expire_after=expire_after)
except ImportError:
    session = None

api_key = os.getenv('SHOUTCAST_API_KEY')


class TestGenre(TestCase):
    def test_get_all_genres(self):
        response = get_all_genres(api_key, session=session)
        self.assertIsInstance(response, GenreList)

    def test_get_primary_genres_json(self):
        response = get_primary_genres_json(api_key, session=session)
        self.assertIsInstance(response, GenreList)

    def test_get_genres_details_by_id(self):
        response = get_genres_details_by_id(api_key, genre_id=25, session=session)
        self.assertIsInstance(response, Genre)
        self.assertEqual(response.id, 25)

    def test_get_genres_by_sub_genres_haschildren_false_return_genre_with_haschildren_false(self):
        response = get_genres_by_sub_genres(api_key, haschildren=False, session=session)
        self.assertIsInstance(response, GenreList)
        self.assertEqual(response.genres[0].haschildren, False)

    def test_get_genres_by_sub_genres_haschildren_true_return_genre_with_haschildren_true(self):
        response = get_genres_by_sub_genres(api_key, haschildren=True, session=session)
        self.assertIsInstance(response, GenreList)
        self.assertEqual(response.genres[0].haschildren, True)

    def test_get_secondary_genres_json(self):
        response = get_secondary_genres_json(api_key, parentid=1, session=session)
        self.assertIsInstance(response, GenreList)
        self.assertEqual(response.genres[0].parentid, 1)
