import requests
from typing import Tuple


def _build_url(limit: (int, Tuple), **kwargs) -> str:
    url = ""
    if isinstance(limit, tuple):
        x, y = limit
        url += '&limit={},{}'.format(x, y)
    elif limit:
        url += '&limit={}'.format(limit)

    if kwargs.get('br'):
        url += "&br={}".format(kwargs.get('br'))

    if kwargs.get('mt'):
        url += "&mt={}".format(kwargs.get('mt'))

    if kwargs.get('genre_id'):
        url += "&genre_id={}".format(int(kwargs.get('genre_id')))

    if kwargs.get('genre'):
        url += "&genre={}".format(int(kwargs.get('genre')))
    return url


def station_xml_strip(station):
    item = dict()
    item['name'] = station.get('@name')
    item['id'] = int(station.get('@id'))
    item['br'] = int(station.get('@br'))
    item['genre'] = _get_all_genre(station)
    item['ct'] = station.get('@ct')
    item['lc'] = int(station.get('@lc'))
    item['logo'] = station.get('@logo')
    item['mt'] = station.get('@mt')
    return item


def station_json_strip(station):
    item = dict()
    item.update(**station)
    item['genre'] = _get_all_genre_from_json(station)
    return item


def _get_all_genre(station):
    genre = station.get('@genre')
    for i in range(2, 10):
        genre_ = station.get('@genre{}'.format(i))
        if not genre_:
            return genre
        genre += ", {}".format(genre_)
    return genre


def _get_all_genre_from_json(station):
    genre = station.get('genre')
    for i in range(2, 10):
        genre_ = station.get('genre{}'.format(i))
        if not genre_:
            return genre
        genre += ", {}".format(genre_)
    return genre


def genre_xml_strip(genre):
    item = dict()
    item['name'] = genre.get('@name')
    item['count'] = int(genre.get('@count'))
    return item


def _init_session(session):
    if session is None:
        session = requests.Session()
    return session
